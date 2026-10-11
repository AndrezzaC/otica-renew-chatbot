
from django.core.management.base import BaseCommand
from chatbot.models import Categoria, Informacao


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        # -------------------------------------------------------------
        # BIBLIOTECA DE CATEGORIAS E INFORMAÇÕES
        # -------------------------------------------------------------

        # Categorias
        categorias = [
            "Conhecer as lentes",
            "Conhecer os tratamentos",
            "Conhecer os materiais",
            "Campo de visão",
            "Exame de vista",
            "Informações sobre a Ótica Renew",
            "Quero fazer orçamento",
            "Mensagens do chatbot",
        ]

        for nome in categorias:
            Categoria.objects.get_or_create(nome=nome)

        # Informações
        dados = [

            # ---------------------------------------------------------
            # MENSAGENS DO CHATBOT
            # ---------------------------------------------------------

            {
                "categoria": "Mensagens do chatbot",
                "titulo": "bem_vindo",
                "resposta": """Olá! Seja bem-vindo à Ótica Renew!
Sou o assistente virtual de pré-atendimento e estou aqui para ajudar você a conhecer nossas opções.
Selecione uma opção no menu para começar."""
            },
            {
                "categoria": "Mensagens do chatbot",
                "titulo": "opcao_invalida",
                "resposta": """Não entendi sua resposta. Por favor, selecione uma das opções disponíveis no menu para continuarmos seu atendimento."""
            },
            {
                "categoria": "Mensagens do chatbot",
                "titulo": "encerramento",
                "resposta": """Agradecemos por entrar em contato com a Ótica Renew!
Esperamos ter ajudado. Estamos à disposição para atender você novamente quando precisar."""
            },

            # ---------------------------------------------------------
            # CONHECER AS LENTES
            # ---------------------------------------------------------

            {
                "categoria": "Conhecer as lentes",
                "titulo": "lentes_introducao",
                "resposta": """Conheça os tipos de lentes disponíveis e descubra as características de cada opção para encontrar a que melhor atende às suas necessidades.
Selecione uma opção abaixo para saber mais."""
            },
            {
                "categoria": "Conhecer as lentes",
                "titulo": "lentes_visao_simples",
                "resposta": """As lentes de visão simples, também chamadas de monofocais, corrigem uma única distância: perto ou longe.
São indicadas para quem precisa de correção em apenas uma dessas distâncias, conforme a prescrição visual."""
            },
            {
                "categoria": "Conhecer as lentes",
                "titulo": "lentes_multifocal",
                "resposta": """As lentes multifocais permitem enxergar de longe, em distâncias intermediárias, como o computador, e de perto, como o celular, usando um único par de óculos.
A adaptação varia de pessoa para pessoa, e o preço depende da marca, do modelo e das tecnologias da lente.
Acesse a opção Campo de visão para entender melhor como funciona a visão através dessas lentes."""
            },
            {
                "categoria": "Conhecer as lentes",
                "titulo": "lentes_ocupacional",
                "resposta": """As lentes ocupacionais são feitas para oferecer conforto na visão de perto e em distâncias intermediárias, como ao usar o computador ou ler documentos.
Podem ser úteis para quem precisa dessas distâncias no dia a dia, mas geralmente não são destinadas à visão de longe."""
            },
            {
                "categoria": "Conhecer as lentes",
                "titulo": "lentes_tipos_grau",
                "resposta": """Selecione uma opção para conhecer os diferentes tipos de grau e entender suas características."""
            },
            {
                "categoria": "Conhecer as lentes",
                "titulo": "lentes_miopia",
                "resposta": """A miopia dificulta enxergar objetos distantes com nitidez, enquanto a visão de perto costuma ser mais clara.
Pode ser corrigida com lentes específicas para esse tipo de grau."""
            },
            {
                "categoria": "Conhecer as lentes",
                "titulo": "lentes_hipermetropia",
                "resposta": """A hipermetropia pode dificultar a visão de perto e causar cansaço visual durante atividades como leitura.
Sua correção é feita com lentes adequadas ao grau de cada pessoa."""
            },
            {
                "categoria": "Conhecer as lentes",
                "titulo": "lentes_atigmatismo",
                "resposta": """O astigmatismo pode causar visão embaçada ou distorcida tanto de perto quanto de longe.
A correção utiliza lentes específicas para compensar a irregularidade na curvatura da córnea ou do cristalino."""
            },
            {
                "categoria": "Conhecer as lentes",
                "titulo": "lentes_presbiopia",
                "resposta": """A presbiopia é uma alteração natural da visão relacionada à idade, que dificulta o foco em objetos próximos.
Pode ser corrigida com lentes adequadas, como lentes para leitura ou multifocais."""
            },
            {
                "categoria": "Conhecer as lentes",
                "titulo": "lentes_contato",
                "resposta": """As lentes de contato são uma alternativa prática aos óculos.
A BioView e a Bausch + Lomb oferecem diferentes modelos para correção visual, com opções que atendem a diferentes necessidades de grau.
A escolha deve considerar as características dos olhos e a orientação de um oftalmologista."""
            },

            # ---------------------------------------------------------
            # CAMPO DE VISÃO
            # ---------------------------------------------------------

            {
                "categoria": "Campo de visão",
                "titulo": "campo_visao_introducao",
                "resposta": """As lentes multifocais possuem áreas para enxergar de longe, em distâncias intermediárias, como o computador, e de perto, como o celular.
A distribuição dessas áreas varia conforme o modelo da lente. A adaptação pode variar de pessoa para pessoa."""
            },

            # ---------------------------------------------------------
            # CONHECER OS TRATAMENTOS
            # ---------------------------------------------------------

            {
                "categoria": "Conhecer os tratamentos",
                "titulo": "tratamentos_introducao",
                "resposta": """Os tratamentos das lentes ajudam a melhorar o conforto visual e a proteção durante o uso dos óculos.
Conheça as opções disponíveis e suas características para identificar quais podem atender melhor às suas necessidades.
Selecione um tratamento para saber mais."""
            },
            {
                "categoria": "Conhecer os tratamentos",
                "titulo": "tratamentos_filtro_antirreflexo",
                "resposta": """O tratamento antirreflexo reduz os reflexos de luz na superfície das lentes, proporcionando uma visão mais confortável e melhorando a nitidez, especialmente em ambientes iluminados e durante o uso de telas."""
            },
            {
                "categoria": "Conhecer os tratamentos",
                "titulo": "tratamentos_filtro_azul",
                "resposta": """O tratamento com filtro azul ajuda a filtrar parte da luz azul emitida por telas e outras fontes luminosas.
Sua utilidade depende das necessidades individuais, e não há evidências sólidas de que reduza o cansaço visual causado pelo uso de dispositivos digitais."""
            },
            {
                "categoria": "Conhecer os tratamentos",
                "titulo": "tratamentos_fotocromatica",
                "resposta": """As lentes fotocromáticas escurecem quando expostas à radiação ultravioleta e voltam a ficar mais claras em ambientes internos.
São uma opção prática para quem deseja adaptar a tonalidade das lentes conforme as condições de iluminação."""
            },
            {
                "categoria": "Conhecer os tratamentos",
                "titulo": "tratamentos_transitions",
                "resposta": """As lentes Transitions escurecem quando expostas à luz solar e voltam a ficar mais claras em ambientes internos.
Essa tecnologia ajuda a proporcionar conforto visual em diferentes condições de iluminação e oferece proteção contra raios UV, conforme as especificações do produto."""
            },

            # ---------------------------------------------------------
            # CONHECER OS MATERIAIS
            # ---------------------------------------------------------

            {
                "categoria": "Conhecer os materiais",
                "titulo": "materiais_introducao",
                "resposta": """Conheça os principais materiais utilizados na fabricação das lentes, como resina, policarbonato e lentes de alto índice.
Descubra as características de cada opção e suas diferenças em resistência, leveza e espessura.
Selecione um material abaixo para saber mais."""
            },
            {
                "categoria": "Conhecer os materiais",
                "titulo": "materiais_resina",
                "resposta": """As lentes de resina são leves e oferecem boa qualidade óptica, sendo uma opção comum para óculos de uso diário.
São versáteis e podem receber diferentes tratamentos, conforme a necessidade do usuário."""
            },
            {
                "categoria": "Conhecer os materiais",
                "titulo": "materiais_policarbonato",
                "resposta": """As lentes de policarbonato são leves e resistentes a impactos, sendo indicadas para quem busca maior segurança e conforto.
São uma opção interessante para crianças, esportistas e pessoas que precisam de lentes mais resistentes."""
            },
            {
                "categoria": "Conhecer os materiais",
                "titulo": "materiais_alto_indice",
                "resposta": """As lentes de alto índice permitem corrigir o grau com lentes mais finas do que as convencionais em muitas situações.
São uma opção para quem busca reduzir a espessura das lentes, dependendo do grau e do modelo escolhido."""
            },

            # ---------------------------------------------------------
            # EXAME DE VISTA
            # ---------------------------------------------------------

            {
                "categoria": "Exame de vista",
                "titulo": "exame_introducao",
                "resposta": """O exame de vista é fundamental para avaliar sua saúde visual e identificar possíveis necessidades de correção do grau.
Na Ótica Renew, o exame é gratuito e pode ser realizado antes da compra dos óculos, permitindo que você conheça suas necessidades visuais antes de escolher suas lentes."""
            },
            {
                "categoria": "Exame de vista",
                "titulo": "exame_horarios",
                "resposta": """O atendimento médico para realização do exame de vista acontece de segunda a sexta-feira, das 9h às 17h, e às quartas-feiras, das 9h às 12h.
O exame é gratuito e pode ser realizado antes da compra dos óculos.
Os horários estão sujeitos a alterações devido a imprevistos."""
            },

            # ---------------------------------------------------------
            # INFORMAÇÕES SOBRE A ÓTICA RENEW
            # ---------------------------------------------------------

            {
                "categoria": "Informações sobre a Ótica Renew",
                "titulo": "informacoes_introducao",
                "resposta": """Conheça melhor a Ótica Renew e confira informações importantes sobre nosso atendimento, incluindo horários de funcionamento, endereço e formas de pagamento.
Selecione uma das opções abaixo para consultar os detalhes e esclarecer suas dúvidas."""
            },
            {
                "categoria": "Informações sobre a Ótica Renew",
                "titulo": "informacoes_horarios",
                "resposta": """A Ótica Renew funciona de segunda a sexta-feira, das 9h às 18h, e aos sábados, das 9h às 13h. Aos domingos, a loja permanece fechada."""
            },
            {
                "categoria": "Informações sobre a Ótica Renew",
                "titulo": "informacoes_endereco",
                "resposta": """A Ótica Renew está localizada na Rua Dr. Feliciano Sodré, nº 215, Loja 18, no Centro de São Gonçalo, Rio de Janeiro.
Você pode visitar nossa loja para conhecer nossos produtos, conferir as opções de lentes e armações e receber atendimento personalizado da nossa equipe."""
            },
            {
                "categoria": "Informações sobre a Ótica Renew",
                "titulo": "informacoes_pagamentos",
                "resposta": """A Ótica Renew aceita dinheiro, Pix, cartões de débito e crédito.
Para confirmar as opções disponíveis e as condições de parcelamento, consulte a equipe da loja."""
            },

            # ---------------------------------------------------------
            # QUERO FAZER ORÇAMENTO
            # ---------------------------------------------------------

            {
                "categoria": "Quero fazer orçamento",
                "titulo": "orcamento_introducao",
                "resposta": """O chatbot não realiza orçamentos automaticamente, mas pode ajudar você a conhecer os tipos de lentes, materiais e tratamentos disponíveis antes de realizar sua compra.
Para solicitar um orçamento, entre em contato com a equipe da Ótica Renew.
Você já sabe qual tipo de lente ou produto está procurando?"""
            },
            {
                "categoria": "Quero fazer orçamento",
                "titulo": "orcamento_negativa",
                "resposta": """Sem problemas! Vamos ajudar você a conhecer as opções disponíveis.
Selecione a categoria desejada para descobrir qual produto ou serviço atende melhor às suas necessidades."""
            },
            {
                "categoria": "Quero fazer orçamento",
                "titulo": "orcamento_positiva",
                "resposta": """Para solicitar seu orçamento, fale com a equipe da Ótica Renew pelo WhatsApp:
https://wa.me/552126070247
Nossa equipe estará à disposição para ajudar você!"""
            },
        ]

        # Cria as informações novas e atualiza as existentes
        for item in dados:
            categoria = Categoria.objects.get(
                nome=item["categoria"]
            )

            Informacao.objects.update_or_create(
                categoria=categoria,
                titulo=item["titulo"],
                defaults={
                    "resposta": item["resposta"]
                }
            )

        self.stdout.write(
            self.style.SUCCESS(
                "Banco populado e informações atualizadas com sucesso!"
            )
        )