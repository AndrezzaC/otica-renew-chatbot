# Define os endereços principais do projeto, encaminha as páginas para a aplicação do chatbot. Desse jeito o Django sabe qual função chamar quando alguém acessar cada endereço

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chatbot.urls')),
]
