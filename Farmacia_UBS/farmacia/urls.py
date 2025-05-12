# C:\Users\BRUNO\Desktop\Projeto-Integrador-I---UNIVESP-master\Farmacia_UBS\farmacia\urls.py

from django.urls import path
# A LogoutView foi movida para o urls.py principal do projeto,
# então não precisamos importar auth_views aqui, a menos que você tenha
# outras views de autenticação que queira definir especificamente neste app.
# Se 'login' e 'logout' estão sendo gerenciados no urls.py principal,
# você pode remover a importação de auth_views daqui se não for usada para mais nada.
# Para este exemplo, vou remover, assumindo que o logout está no principal.
# Se você decidir manter o logout aqui, descomente a linha abaixo.
# from django.contrib.auth import views as auth_views

from . import views  # Importa as views do seu app farmacia

# app_name = 'farmacia'  # Opcional: para namespacing de URLs.
                        # Se usar, nos templates {% url 'farmacia:nome_da_url' %}

urlpatterns = [
    # URL raiz para o app 'farmacia'.
    # Se o include no urls.py principal é path('', include('farmacia.urls')),
    # então esta URL '' corresponderá a http://localhost:8000/
    path('', views.home, name='home'), # A view 'home' já lida com a listagem de medicamentos.

    # URL para registro de novos usuários
    path('registro/', views.registrar_usuario, name='registro'),

    # URLs para funcionalidades de medicamentos
    path('cadastrar_medicamento/', views.cadastrar_medicamento, name='cadastrar_medicamento'),

    # URL de edição - definida uma vez
    path('editar/<int:id>/', views.editar_medicamento, name='editar'),

    path('registrar_saida/', views.registrar_saida, name='registrar_saida'), # Nome da URL corrigido de 'saida' para 'registrar_saida' para consistência com a view

    # A view 'lista_medicamentos' e o path duplicado para '' e 'editar' foram removidos
    # pois 'views.home' já parece ser a principal listagem e 'editar' já estava definido.
    # Se 'lista_medicamentos' for uma view distinta com um propósito diferente,
    # você precisaria dar a ela um path único, por exemplo:
    # path('lista-completa/', views.lista_medicamentos, name='lista_de_medicamentos'),
]

# Seções comentadas podem ser removidas se não forem usadas.
# from django.urls import path
# from . import views
# urlpatterns = [
    # ...
    # path('accounts/profile/', views.profile, name='profile'),
# ]