from django.urls import path
from . import views

urlpatterns = [
    path('processar_logs/', views.processar_logs, name='processar_logs'),
    path('csv_tempo_medio/', views.csv_tempo_medio, name='csv_tempo_medio'),
    path('csv_requisicoes_servico/', views.csv_requisicoes_servico, name='csv_requisicoes_servico'),
    path('csv_requisicoes_consumidor/', views.csv_requisicoes_consumidor, name='csv_requisicoes_consumidor'),
]
