from typing import Any
from django.core.management.base import BaseCommand, CommandParser
import gspread.utils
from entries.models import Entry
import gspread
import pandas as pd
import os


class Command(BaseCommand):

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            'spreadsheet_url',
            type=str,
            help='url da planilha com as inscrições'
        )

        #parser.add_argument(
        #    'sheet_name',
        #    type='str',
        #    help='Nome da aba que contém as inscrições'
        #)

    def handle(self, *args: Any, **options: Any) -> str | None:
        spreadsheet_url = options['spreadsheet_url']
        #sheet_name = options['sheet_name']

        gs = gspread.service_account(filename=os.environ.get('TOKEN_GSPREAD'))
        
        sh = gs.open_by_url(spreadsheet_url)

        ws = sh.get_worksheet(1).get_all_records(head=2, value_render_option=gspread.utils.ValueRenderOption(value='UNFORMATTED_VALUE'))
        df = pd.DataFrame(ws)

        for entry in df.itertuples():

            if entry[10] == 'FEMININO (OPEN)' or entry[9] == 'FEMININO (OPEN)':
                category = 'FEMININO'
                age_category = 'OPEN'
            else:
                category = entry[9]
                age_category = entry[10]           
            
            self.stdout.write(self.style.NOTICE(entry[2]))

            if entry[8] == 'OC6' or entry[8] == 'V6':
                
                Entry.objects.create(
                    name1=entry[2].upper(),
                    name2=entry[3].upper(),
                    name3=entry[4].upper(),
                    name4=entry[5].upper(),
                    name5=entry[6].upper(),
                    name6=entry[7].upper(),
                    boat_class=entry[8],
                    sex_category=category,
                    age_category=age_category,
                    vest_number=entry[11],
                )
            
            elif entry[8] == 'OC2' or entry[8] == 'V2':
                Entry.objects.create(
                    name1=entry[2].upper(),
                    name2=entry[3].upper(),
                    boat_class=entry[8],
                    sex_category=category,
                    age_category=age_category,
                    vest_number=entry[11],
                )
            
            else:
                Entry.objects.create(
                    name1=entry[2].upper(),
                    boat_class=entry[8],
                    sex_category=category,
                    age_category=age_category,
                    vest_number=entry[11],
                )
        
        self.stdout.write(self.style.SUCCESS('INSCRIÇÕES IMPORTADAS COM SUCESSO'))

                