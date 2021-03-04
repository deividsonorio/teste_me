from django.conf import settings
from django.test import TestCase
from reader.models import LogRequest
from django.core.management import call_command
from io import StringIO


class CommandTestCase(TestCase):
    def test_processar_logs_success(self):
        test_file = settings.MEDIA_TEST + 'teste.txt'
        out = StringIO()
        call_command('processar_logs', arquivo=test_file, stdout=out)
        self.assertIn('Processamento de log iniciado', out.getvalue())
        self.assertIn('Arquivo de log processado com sucesso', out.getvalue())

    def test_processar_logs_not_found(self):
        test_file = settings.MEDIA_TEST + 'testando.txt'
        out = StringIO()
        call_command('processar_logs', arquivo=test_file, stdout=out)
        self.failureException(out.getvalue())
        self.assertIn('Houve um erro ao processar o arquivo de log', out.getvalue())

    def test_processar_logs_wrong_option(self):
        out = StringIO()
        with self.assertRaises(TypeError) as ctx:
            call_command('processar_logs', teste="none", stdout=out)
        self.assertIn("Unknown option(s)", str(ctx.exception))

    def test_csv_requisicoes_consumidor(self):
        test_file = settings.MEDIA_TEST + 'teste.txt'
        out = StringIO()
        call_command('processar_logs', arquivo=test_file, stdout=out)
        call_command('csv_requisicoes_consumidor', arquivo='./media/tests/consumidor.csv', stdout=out)
        self.assertIn('Criando CSV requisições consumidor', out.getvalue())
        self.assertIn('CSV requisições consumidor. Tempo', out.getvalue())

    def test_csv_requisicoes_consumidor_no_directory(self):
        test_file = settings.MEDIA_TEST + 'teste.txt'
        out = StringIO()
        call_command('processar_logs', arquivo=test_file, stdout=out)
        call_command('csv_requisicoes_consumidor', arquivo='./media/foo/bar/consumidor.csv', stdout=out)
        self.assertIn('Houve um erro', out.getvalue())

    def test_csv_requisicoes_consumidor_wrong_option(self):
        out = StringIO()
        with self.assertRaises(TypeError) as ctx:
            call_command('csv_requisicoes_consumidor', teste="none", stdout=out)
        self.assertIn("Unknown option(s)", str(ctx.exception))

    def test_csv_requisicoes_servico(self):
        test_file = settings.MEDIA_TEST + 'teste.txt'
        out = StringIO()
        call_command('processar_logs', arquivo=test_file, stdout=out)
        call_command('csv_requisicoes_servico', arquivo='./media/tests/servico.csv', stdout=out)
        self.assertIn('Criando CSV requisições serviço', out.getvalue())
        self.assertIn('CSV requisições serviço. Tempo', out.getvalue())

    def test_csv_requisicoes_servico_no_directory(self):
        test_file = settings.MEDIA_TEST + 'teste.txt'
        out = StringIO()
        call_command('processar_logs', arquivo=test_file, stdout=out)
        call_command('csv_requisicoes_servico', arquivo='./media/foo/bar/servico.csv', stdout=out)
        self.assertIn('Houve um erro', out.getvalue())

    def test_csv_requisicoes_servico_wrong_option(self):
        out = StringIO()
        with self.assertRaises(TypeError) as ctx:
            call_command('csv_requisicoes_servico', teste="none", stdout=out)
        self.assertIn("Unknown option(s)", str(ctx.exception))

    def test_csv_tempo_medio(self):
        test_file = settings.MEDIA_TEST + 'teste.txt'
        out = StringIO()
        call_command('processar_logs', arquivo=test_file, stdout=out)
        call_command('csv_tempo_medio', arquivo='./media/tests/tempo.csv', stdout=out)
        self.assertIn('Criando CSV de tempo médio', out.getvalue())
        self.assertIn('CSV de tempo médio processado com sucesso. Tempo', out.getvalue())

    def test_csv_tempo_medio_no_directory(self):
        test_file = settings.MEDIA_TEST + 'teste.txt'
        out = StringIO()
        call_command('processar_logs', arquivo=test_file, stdout=out)
        call_command('csv_tempo_medio', arquivo='./media/foo/bar/tempo.csv', stdout=out)
        self.assertIn('Houve um erro', out.getvalue())

    def test_csv_tempo_medio_wrong_option(self):
        out = StringIO()
        with self.assertRaises(TypeError) as ctx:
            call_command('csv_tempo_medio', teste="none", stdout=out)
        self.assertIn("Unknown option(s)", str(ctx.exception))


class LogRequestCase(TestCase):
    def setUp(self):
        LogRequest.objects.create(
            service="service1", 
            consumer="consumer1",
            proxy=1,
            gateway=2,
            request=3,
            line='{"teste": 1}',
            started_at ='123456',
            )

        LogRequest.objects.create(
            service="service2", 
            consumer="consumer2",
            proxy=10,
            gateway=20,
            request=30,
            line='{"teste": 2}',
            started_at ='1234560',
            )

    def test_log_request_model(self):
        """LogRequest model test"""
        service1 = LogRequest.objects.get(service="service1")
        service2 = LogRequest.objects.get(service="service2")

        self.assertEqual(service1.consumer, 'consumer1')
        self.assertEqual(service1.proxy, 1)
        self.assertEqual(service1.gateway, 2)
        self.assertEqual(service1.request, 3)
        self.assertEqual(service1.line, '{"teste": 1}')
        self.assertEqual(service1.started_at, '123456')

        self.assertEqual(service2.consumer, 'consumer2')
        self.assertEqual(service2.proxy, 10)
        self.assertEqual(service2.gateway, 20)
        self.assertEqual(service2.request, 30)
        self.assertEqual(service2.line, '{"teste": 2}')
        self.assertEqual(service2.started_at, '1234560')
