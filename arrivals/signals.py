from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from gspread.utils import rowcol_to_a1
from arrivals.models import Arrival
from entries.models import Entry
from starts.models import Start
import gspread
import time
import datetime
from dotenv import load_dotenv
import os


load_dotenv()


def connecting_gspread(spreadsheet_url, sheet_name):
    gs = gspread.service_account(filename=os.environ.get('TOKEN_GSPREAD'))
    sh = gs.open_by_url(spreadsheet_url)
    wk = sh.worksheet(sheet_name)
    return wk


def get_competitor_details(entries, vest_number):
    competitor = entries.filter(vest_number=vest_number).first()
    boat_class = competitor.boat_class.capitalize() if competitor.boat_class not in ['OC1', 'OC2', 'V1', 'V2', 'OC6', 'V6'] else competitor.boat_class
    sex_category = competitor.sex_category.title()
    age_category = '+40' if competitor.age_category == 40 or competitor.age_category == '40' else competitor.age_category.title()
    return competitor, boat_class, sex_category, age_category


def calculate_competing_time(arrival_time, boat_class):
    start_time = Start.objects.filter(category=boat_class).first().start_time
    temp_diff = arrival_time - start_time
    total_seconds = int(temp_diff.total_seconds())
    hours, rest = divmod(total_seconds, 3600)
    minutes, seconds = divmod(rest, 60)
    return f'{hours:02}:{minutes:02}:{seconds:02}'


def build_competitor_name(competitor):
    name = ''
    for name_part in [competitor.name1, competitor.name2, competitor.name3, competitor.name4, competitor.name5, competitor.name6]:
        if name_part:
            name += f'{name_part}\n'
    return name[:-2]


def find_table_column(wksheet, tablename):
    title_line = wksheet.row_values(2)
    for index, value in enumerate(title_line):
        if value == tablename:
            return index
    return None


def get_inserting_position_and_line(wksheet, col):
    positions_col = wksheet.col_values(col + 1)
    if positions_col[-1] == 'Posição':
        arrival_position = 1
    else:
        arrival_position = int(positions_col[-1].replace('º', '')) + 1
    inserting_line = len(positions_col) + 1
    return arrival_position, inserting_line


def get_update_position_and_line_by_time(wksheet, col, competing_time):
    time_col = wksheet.col_values(col + 3)
    if time_col[-1] == 'Tempo':
        return '1', len(time_col) + 1, []
    
    for index, time in enumerate(time_col):
        parts = time.split(':')
        if len(parts) == 3:
            hour = parts[0] if parts[0] != '' else 0
            minute = parts[1] if parts[1] != '' else 0
            second = parts[2] if parts[2] != '' else 0
            time = datetime.timedelta(hours=int(parts[0]), minutes=int(parts[1]), seconds=int(parts[2]))
            competing_time_parts = competing_time.split(':')
            competing_time = datetime.timedelta(hours=int(competing_time_parts[0]), minutes=int(competing_time_parts[1]), seconds=int(competing_time_parts[2]))
            if competing_time < time:
                inserting_line = index + 2
                if inserting_line < len(time_col):
                    next_lines = wksheet.get(f'{rowcol_to_a1(inserting_line+1, col+1)}:{rowcol_to_a1(len(time_col), col+3)}')

                arrival_position = index - 3

                return arrival_position, inserting_line, next_lines

    else:
        return f'{len(time_col) - 2}', len(time_col) + 1, []
        

def get_update_position_and_line_by_name(wksheet, col, old_name):
    name_col = wksheet.col_values(col+2)
    for index, name in enumerate(name_col):
        if name == old_name:
            updating_line = index + 1
            return updating_line



def update_spreadsheet(wksheet, inserting_line, table_initial_col, table_final_col,values: list):
    try:
        wksheet.update(
            values=[values],
            range_name=f'{rowcol_to_a1(inserting_line, table_initial_col + 1)}:{rowcol_to_a1(inserting_line, table_final_col + 1)}'
        )
    except Exception as e:
        print(f'erro 1 - {e}')
        time.sleep(1)
        try:
            wksheet.update(
                values=[values],
                range_name=f'{rowcol_to_a1(inserting_line, table_initial_col + 1)}:{rowcol_to_a1(inserting_line, table_final_col + 1)}'
            )
        except Exception as er:
            print(f'erro 2 - {er}')


def handle_existing_arrival(wrong_vest_number, wksheet, table_initial_col, entries):
        table_final_col = table_initial_col + 2
        arrival_names = wksheet.col_values(table_initial_col + 2)
        wrong_name = build_competitor_name(entries.filter(vest_number=wrong_vest_number).first())
        for index, name in enumerate(arrival_names):

            if name.upper() == wrong_name.upper():
                deleting_line = index + 1
                wksheet.batch_clear([f'{rowcol_to_a1(deleting_line, table_initial_col + 1)}:{rowcol_to_a1(deleting_line, table_final_col + 1)}'])

                if deleting_line < len(arrival_names):
                    print('cheguei aqui')
                    next_lines = wksheet.get(f'{rowcol_to_a1(deleting_line+1, table_initial_col+1)}:{rowcol_to_a1(len(arrival_names), table_final_col+1)}')
                    wksheet.update(
                        values=next_lines,
                        range_name=f'{rowcol_to_a1(deleting_line, table_initial_col+1)}:{rowcol_to_a1(len(arrival_names)-1, table_final_col+1)}'
                    )


@receiver(pre_save, sender=Arrival)
def update_arrival_by_category(sender, instance, **kwargs):
    wrong_arrival = sender.objects.filter(id=instance.id).first()

    if wrong_arrival is not None:

        wrong_vest_number = wrong_arrival.vest_number

        entries = Entry.objects.all()
        competitor, boat_class, sex_category, age_category = get_competitor_details(entries, instance.vest_number)
        tablename = f'{boat_class} {sex_category} {age_category}'

        wrong_competitor = entries.filter(vest_number=wrong_vest_number).first()
        wrong_boat_class = wrong_competitor.boat_class.capitalize()
        wrong_sex_category = wrong_competitor.sex_category.title()
        wrong_age_category = '+40' if wrong_competitor.age_category == 40 or wrong_competitor.age_category == '40' else wrong_competitor.age_category.title()
        wrong_tablename = f'{wrong_boat_class} {wrong_sex_category} {wrong_age_category}'

        wrong_wksheet = connecting_gspread(os.environ.get('URL_SPREADSHEET_SUMULA'), wrong_boat_class)
        wksheet = connecting_gspread(os.environ.get('URL_SPREADSHEET_SUMULA'), boat_class)
        table_initial_col = find_table_column(wrong_wksheet, wrong_tablename)


        if tablename == wrong_tablename:
            wrong_competitor_name = build_competitor_name(wrong_competitor)
            competitor_name = build_competitor_name(competitor)
            updating_line = get_update_position_and_line_by_name(wksheet, table_initial_col, wrong_competitor_name)
            table_final_col = table_initial_col
            update_spreadsheet(wksheet, updating_line, table_initial_col+1, table_final_col+1, values=[competitor_name])
            
        else:
            competing_time = calculate_competing_time(wrong_arrival.arrival_time, wrong_boat_class)
            handle_existing_arrival(wrong_vest_number, wrong_wksheet, table_initial_col, entries)
            table_initial_col = find_table_column(wksheet, tablename)
            arrival_position, inserting_line, next_lines = get_update_position_and_line_by_time(wksheet, table_initial_col, competing_time)
            competitor_name = build_competitor_name(competitor)
            updating_values = [f'{arrival_position}º', competitor_name.upper(), competing_time]
            table_final_col = table_initial_col + 2
            update_spreadsheet(wksheet, inserting_line, table_initial_col, table_final_col, updating_values)
            if len(next_lines) > 0:
                update_spreadsheet(wksheet, inserting_line + 1, table_initial_col, table_final_col, values=next_lines)




@receiver(post_save, sender=Arrival)
def register_arrival_by_category(sender, instance, created, **kwargs):
    if created:
        entries = Entry.objects.all()
        competitor, boat_class, sex_category, age_category = get_competitor_details(entries, instance.vest_number)
        tablename = f'{boat_class} {sex_category} {age_category}'
        wksheet = connecting_gspread(os.environ.get('URL_SPREADSHEET_SUMULA'), boat_class)
        table_initial_col = find_table_column(wksheet, tablename)
        table_final_col = table_initial_col + 2

        arrival_position, inserting_line = get_inserting_position_and_line(wksheet, table_initial_col)
        competitor_name = build_competitor_name(competitor)
        competing_time = calculate_competing_time(instance.arrival_time, boat_class)

        updating_values = [f'{arrival_position}º', competitor_name.upper(), competing_time]
        update_spreadsheet(wksheet, inserting_line, table_initial_col, table_final_col, updating_values)
