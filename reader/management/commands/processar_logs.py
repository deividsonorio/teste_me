from django.core.management.base import BaseCommand
from reader.models import LogRequest
from django.conf import settings
import datetime
import jsonlines
import logging
import os


class Command(BaseCommand):
    help = 'Processa arquivo de logs e salva na base de dados. Arquivo deve ser colocado em ./media/process/logs.txt'

    log_file = settings.MEDIA_LOG_PROCESS + settings.LOG_FILE

    def add_arguments(self, parser):
        parser.add_argument('-a', '--arquivo', type=str, help='Arquivo a ser processado (arquivo com linhas de json). '
                                                              'Para caminhos no Windows inserir barras de escape. '
                                                              "Windows: C:\\\processar\\\logs.txt | "
                                                              'Linux: ./media/process/logs.txt', )

    def handle(self, *args, **options):
        file = self.log_file
        if options['arquivo']:
            file = options['arquivo']

        begin_time = datetime.datetime.now()
        start_message = 'Processamento de log iniciado. (%s)' % begin_time
        self.stdout.write(self.style.SUCCESS(start_message))
        logging.info(start_message)

        # LogRequest.objects.all().delete()

        try:
            self.stdout.write("Processando...")

            with jsonlines.open(file, mode='r') as reader:
                objs = [
                    LogRequest(
                        service=log_line['service']['id'],
                        consumer=log_line['authenticated_entity']['consumer_id']['uuid'],
                        proxy=log_line['latencies']['proxy'],
                        gateway=log_line['latencies']['gateway'],
                        request=log_line['latencies']['request'],
                        started_at=log_line['started_at'],
                        line=log_line,
                    )
                    for log_line in reader.iter(type=dict, skip_invalid=True)
                ]

                LogRequest.objects.bulk_create(objs)

            time = datetime.datetime.now() - begin_time

            # Rename file to avoid process it again (if not passed as argument)
            if not options['arquivo']:
                os.rename(self.log_file,
                          settings.MEDIA_LOG_PROCESS + begin_time.strftime("%Y%m%d-%H%M%S-") + settings.LOG_FILE)

            self.stdout.write(self.style.SUCCESS('Arquivo de log processado com sucesso. Tempo: (%s)' % time))

        except jsonlines.InvalidLineError as invalid:
            self.stdout.write(self.style.ERROR('Houve um erro: (%s)') % invalid)

        except IOError:
            self.stdout.write(self.style.ERROR('Houve um erro ao processar o arquivo de log (%s)' % file))
            logging.error('Houve um erro ao processar o arquivo de log (%s)' % file)

        except Exception as e:
            self.stdout.write(self.style.ERROR('Houve um erro inesperado (%s)') % e)
