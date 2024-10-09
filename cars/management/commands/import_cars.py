from django.core.management.base import BaseCommand, CommandParser
import gspread
import gspread.utils
from cars.models import Car
import pandas as pd
import os


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'spreadsheet_url',
            type=str,
            help='url da planilha com as placas dos carros'
        )

        parser.add_argument(
            '--sheet_name',
            type=str,
            help='Nome da aba que contém as placas dos carros',
            required=False
        )

    def handle(self, *args, **options):
        spreadsheet_url = options['spreadsheet_url']
        sheet_name = options['sheet_name']

        gs = gspread.auth.service_account(filename=os.environ.get('TOKEN_GSPREAD'))

        sh = gs.open_by_url(spreadsheet_url)

        if sheet_name:
            ws = sh.worksheet(sheet_name).get_all_records(expected_headers=['Nome completo', 'TELEFONE DE CONTATO', 'Equipe', 'Deseja fazer uso do estacionamento?', 'Placa do veículo.', 'Marca, modelo e cor', 'Carros por equipe'])
        else:
            ws = sh.get_worksheet(1).get_all_records(expected_headers=['Nome completo', 'TELEFONE DE CONTATO', 'Equipe', 'Deseja fazer uso do estacionamento?', 'Placa do veículo.', 'Marca, modelo e cor', 'Carros por equipe'])

        df = pd.DataFrame(ws)

        for car in df.iterrows():
            full_name = car[1]['Nome completo']
            phone_number = car[1]['TELEFONE DE CONTATO']
            team = car[1]['Equipe']
            want_to_use_parking_slot = car[1]['Deseja fazer uso do estacionamento?']
            car_identification = car[1]['Placa do veículo.']
            car_model = car[1]['Marca, modelo e cor']
            cars_per_team = car[1]['Carros por equipe']
            if cars_per_team and want_to_use_parking_slot == 'Sim':
                if cars_per_team > 1:
                    licence_plates = car_identification.split(',')
                    car_models = car_model.split(',')

                    if len(licence_plates) != len(car_models):
                        self.stdout.write(self.style.ERROR(f'ERRO AO CADASTRAR OS CARROS DE {full_name} O NÚMERO DE PLACAS E DE CARROS NÃO É EQUIVALENTE.'))
                        continue

                    for index, licence_plate in enumerate(licence_plates):
                        try:
                            Car.objects.create(
                                full_name=full_name,
                                phone_number=phone_number,
                                team=team,
                                car_identification=licence_plate.strip().upper(),
                                car_model=car_models[index].strip(),
                                cars_per_team=1,
                            )
                        except Exception as error:
                            self.stdout.write(self.style.ERROR(f'NÃO FOI POSSÍVEL CADASTRAR {full_name} - {licence_plate} ERRO: {error}'))
                        else:
                            self.stdout.write(self.style.SUCCESS(f'{full_name} - {licence_plate}  CADASTRADO COM SUCESSO'))

                else:
                    try:
                        Car.objects.create(
                            full_name=full_name,
                            phone_number=phone_number,
                            team=team,
                            car_identification=car_identification.strip().upper(),
                            car_model=car_model.strip(),
                            cars_per_team=1
                            )
                    except Exception as error:
                        self.stdout.write(self.style.ERROR(f'NÃO FOI POSSÍVEL CADASTRAR {full_name} - {car_identification} ERRO: {error}'))
                    else:
                        self.stdout.write(self.style.SUCCESS(f'{full_name} - {car_identification}  CADASTRADO COM SUCESSO'))

