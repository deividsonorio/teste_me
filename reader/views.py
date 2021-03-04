from asgiref.sync import sync_to_async
from django.http import JsonResponse
from django.core import management
from django.conf import settings
from pathlib import Path
import asyncio


@sync_to_async
def task_processar_logs():
    management.call_command('processar_logs', verbosity=0)


async def processar_logs(request):

    log_file = Path(settings.MEDIA_LOG_PROCESS + settings.LOG_FILE)

    if log_file.is_file():
        json_response = {
            "status": "success",
            "data": {},
            "message": "Tarefa de processamento de arquivo de log iniciada",
        }

        asyncio.create_task(task_processar_logs(), name="processar_logs")
        return JsonResponse(json_response)

    json_response = {
        "status": "fail",
        "data": {},
        "message": "Arquivo de log não encontrado em %s" % log_file,
    }
    return JsonResponse(json_response)


@sync_to_async
def task_csv_tempo_medio():
    management.call_command('csv_tempo_medio', verbosity=0)


async def csv_tempo_medio(request):
    json_response = {
        "status": "success",
        "data": {},
        "message": "Criação de CSV de tempo médio iniciada",
    }

    asyncio.create_task(task_csv_tempo_medio(), name="csv_tempo_medio")
    return JsonResponse(json_response)


@sync_to_async
def task_csv_requisicoes_consumidor():
    management.call_command('csv_requisicoes_consumidor', verbosity=0)


async def csv_requisicoes_consumidor(request):
    json_response = {
        "status": "success",
        "data": {},
        "message": "Criação de CSV de número de requisições por consumidor",
    }

    asyncio.create_task(task_csv_requisicoes_consumidor(), name="csv_requisicoes_consumidor")
    return JsonResponse(json_response)


@sync_to_async
def task_csv_requisicoes_servico():
    management.call_command('csv_requisicoes_servico', verbosity=0)


async def csv_requisicoes_servico(request):
    json_response = {
        "status": "success",
        "data": {},
        "message": "Criação de CSV de número de requisições por serviço",
    }

    asyncio.create_task(task_csv_requisicoes_servico(), name="csv_requisicoes_servico")
    return JsonResponse(json_response)
