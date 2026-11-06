# Importa a classe responsável pelas configurações de aplicativos do Django.
from django.apps import AppConfig


# Define a configuração do aplicativo chatbot.
class ChatbotConfig(AppConfig):

    # Informa ao Django o nome do aplicativo ao qual essa configuração pertence.
    name = 'chatbot'