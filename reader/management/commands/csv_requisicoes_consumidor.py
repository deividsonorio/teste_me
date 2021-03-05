from django.core.management.base import BaseCommand
from django.db.models import Avg, Count
from reader.models import LogRequest
from django.conf import settings
import datetime
import logging
import csv


class Command(BaseCommand):
    help = 'Gera relatório CSV de Requisições do Consumidor'

    def add_arguments(self, parser):
        parser.add_argument('-a', '--arquivo', type=str, help='Caminho onde o arquivo deve ser salvo '
                                                              '(incluindo nome e extensão). '
                                                              'Para caminhos no Windows inserir barras de escape. '
                                                              "Windows: C:\\\processar\\\logs.txt | "
                                                              'Linux: ./media/process/logs.txt', )

    def handle(self, *args, **options):
        begin_time = datetime.datetime.now()

        file = settings.MEDIA_CSV_PROCESS + begin_time.strftime("%Y%m%d-%H%M%S-") + 'requisicoes_consumidor.csv'

        if options['arquivo']:
            file = options['arquivo']

        start_message = 'Criando CSV requisições consumidor. (%s)' % begin_time
        self.stdout.write(self.style.SUCCESS(start_message))
        logging.info(start_message)

        try:
            requests_info = LogRequest.objects.values('consumer').annotate(Count('consumer'))

            with open(file, 'w', newline='', encoding="utf-8") as csvfile:
                fieldnames = ['Consumidor', 'Numero Requisicoes']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for info in requests_info:
                    writer.writerow({
                        'Consumidor': info['consumer'],
                        'Numero Requisicoes': info['consumer__count'],
                    })

            time = datetime.datetime.now() - begin_time
            self.stdout.write(self.style.SUCCESS('CSV requisições consumidor. Tempo: (%s)' % time))

        except Exception as e:
            self.stdout.write(self.style.ERROR('Houve um erro: (%s)') % e)
