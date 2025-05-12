"""
URL configuration for Farmacia_UBS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views # Importe auth_views UMA VEZ, no topo.

urlpatterns = [
    path('admin/', admin.site.urls),

    # URLs de autenticação
    # Certifique-se de que você tem um template chamado 'login.html'
    # na sua pasta de templates (ex: 'templates/login.html' ou 'farmacia/templates/login.html')
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    # URL de Logout
    # 'next_page='login'' redirecionará para a página de login após o logout.
    # Se preferir redirecionar para a página inicial, e sua página inicial
    # tem o nome 'home' (definido em farmacia/urls.py), você pode usar 'next_page='home''.
    # A sua última definição estava usando 'next_page='login'', então vou manter isso.
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Inclui as URLs do seu app 'farmacia'
    # Deixar o path como '' significa que as URLs de 'farmacia.urls'
    # serão acessadas a partir da raiz do site (ex: http://localhost:8000/SUA_URL_DE_FARMACIA)
    path('', include('farmacia.urls')),
]