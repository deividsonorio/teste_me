from django.core.management.base import BaseCommand
from django.db.models import Avg
from reader.models import LogRequest
from django.conf import settings
import datetime
import logging
import csv


class Command(BaseCommand):
    help = 'Displays current time'

    log_file = settings.MEDIA_ROOT + settings.LOG_FILE

    def add_arguments(self, parser):
        parser.add_argument('-a', '--arquivo', type=str, help='Caminho onde o arquivo deve ser salvo '
                                                              '(incluindo nome e extensão). '
                                                              'Para caminhos no Windows inserir barras de escape. '
                                                              "Windows: C:\\\processar\\\logs.txt | "
                                                              'Linux: ./media/process/logs.txt', )

    def handle(self, *args, **options):
        begin_time = datetime.datetime.now()

        file = settings.MEDIA_CSV_PROCESS + begin_time.strftime("%Y%m%d-%H%M%S-") + 'servico_tempo_medio.csv'

        if options['arquivo']:
            file = options['arquivo']

        start_message = 'Criando CSV de tempo médio. (%s)' % begin_time
        self.stdout.write(self.style.SUCCESS(start_message))
        logging.info(start_message)

        try:
            requests_info = LogRequest.objects.values('service') \
                .annotate(Avg('proxy')) \
                .annotate(Avg('gateway')) \
                .annotate(Avg('request'))

            with open(file, 'w', newline='', encoding="utf-8") as csvfile:
                fieldnames = ['Serviço', 'Tempo médio Proxy', 'Tempo médio Gateway', 'Tempo médio Request']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for info in requests_info:
                    writer.writerow({
                        'Serviço': info['service'],
                        'Tempo médio Proxy': info['proxy__avg'],
                        'Tempo médio Gateway': info['gateway__avg'],
                        'Tempo médio Request': info['request__avg'],
                    })

            time = datetime.datetime.now() - begin_time
            self.stdout.write(self.style.SUCCESS('CSV de tempo médio processado com sucesso. Tempo: (%s)' % time))

        except Exception as e:
            self.stdout.write(self.style.ERROR('Houve um erro: (%s)') % e)
