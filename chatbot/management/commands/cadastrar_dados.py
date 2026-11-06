# Importa a classe base do Django para criar comandos personalizados.
from django.core.management.base import BaseCommand

# Importa os modelos que representam as categorias e informações do chatbot.
from chatbot.models import Categoria, Informacao


# Cria um comando personalizado que pode ser executado pelo terminal do Django.
class Command(BaseCommand):

    # Método principal executado quando o comando é chamado.
    # O Django executa esse método automaticamente.
    def handle(self, *args, **kwargs):

        # Dicionário que armazena as categorias do chatbot e seus textos de introdução.
        # Cada categoria agrupa um assunto, como lentes, tratamentos e materiais.
        categorias = {
            "Conhecer as lentes": (
                "Conheça os tipos de lentes disponíveis e suas "
                "características. Você pode consultar os modelos "
                "de lentes, os tipos de grau e as lentes de contato."
            ),
            "Conhecer os tratamentos": (
                "Os tratamentos das lentes oferecem diferentes "
                "características para o uso dos óculos. Conheça as "
                "opções disponíveis e entenda suas funções."
            ),
            "Conhecer os materiais": (
                "Conheça os principais materiais utilizados na "
                "fabricação das lentes e suas diferenças em "
                "resistência, leveza e espessura."
            ),
            "Campo de visão": (
                "As lentes multifocais possuem áreas destinadas "
                "à visão de longe, intermediária e de perto. "
                "Conheça as diferenças entre os campos de visão."
            ),
            "Exame de vista": (
                "Na Ótica Renew, o exame de vista é gratuito e "
                "pode ser realizado antes da compra dos óculos. "
                "Confira os horários de atendimento."
            ),
            "Informações sobre a Ótica Renew": "",
            "Quero fazer orçamento": (
                "O chatbot não realiza orçamentos automaticamente, "
                "mas pode ajudar você a conhecer os tipos de lentes, "
                "materiais e tratamentos disponíveis.\n\n"
                "Para solicitar um orçamento, entre em contato com "
                "a equipe da Ótica Renew.\n\n"
                "Você já sabe qual tipo de lente ou produto está procurando?"
            ),
            "Mensagens do chatbot": "",
        }

        # Dicionário auxiliar para guardar os objetos de categoria criados ou encontrados.
        # Assim, podemos reutilizar essas categorias ao cadastrar as informações.
        objetos_categoria = {}

        # Percorre o dicionário, obtendo o nome e a introdução de cada categoria.
        for nome, introducao in categorias.items():

            # Procura uma categoria pelo nome.
            # Se ela já existir, atualiza seus dados; se não existir, cria uma nova.
            # update_or_create evita criar categorias duplicadas a cada execução.
            categoria, _ = Categoria.objects.update_or_create(
                nome=nome,
                defaults={"introducao": introducao}
            )

            # Guarda a categoria encontrada ou criada para utilizá-la depois.
            objetos_categoria[nome] = categoria

        # Lista com os conteúdos que serão cadastrados no banco de dados.
        # Cada item representa uma mensagem ou opção disponível no chatbot.
        dados = [

            # Mensagens gerais utilizadas durante a conversa.
            {
                "categoria": "Mensagens do chatbot",
                "titulo": "bem_vindo",
                "resposta": (
                    "Olá! Seja bem-vindo à Ótica Renew!\n"
                    "Sou o assistente virtual de pré-atendimento "
                    "e estou aqui para ajudar você.\n"
                    "Selecione uma opção no menu para começar."
                ),
            },
            {
                "categoria": "Mensagens do chatbot",
                "titulo": "opcao_invalida",
                "resposta": (
                    "Não entendi sua resposta. Por favor, selecione "
                    "uma das opções disponíveis no menu."
                ),
            },
            {
                "categoria": "Mensagens do chatbot",
                "titulo": "encerramento",
                "resposta": (
                    "Agradecemos por entrar em contato com a "
                    "Ótica Renew!\n"
                    "Esperamos ter ajudado. Estamos à disposição "
                    "quando precisar."
                ),
            },

            # Conteúdos relacionados aos diferentes tipos de lentes.
            {
                "categoria": "Conhecer as lentes",
                "titulo": "lentes_visao_simples",
                "resposta": (
                    "As lentes de visão simples, também chamadas "
                    "de monofocais, corrigem uma única distância: "
                    "perto ou longe.\n"
                    "São indicadas para quem precisa de correção "
                    "em apenas uma dessas distâncias, conforme "
                    "a prescrição visual."
                ),
            },
            {
                "categoria": "Conhecer as lentes",
                "titulo": "lentes_multifocal",
                "resposta": (
                    "As lentes multifocais permitem enxergar de "
                    "longe, em distâncias intermediárias, como "
                    "o computador, e de perto, como o celular, "
                    "usando um único par de óculos.\n"
                    "A adaptação varia de pessoa para pessoa, e "
                    "o preço depende da marca, do modelo e das "
                    "tecnologias da lente.\n"
                    "Consulte também a opção Campo de visão para "
                    "entender melhor como essas lentes funcionam."
                ),
            },
            {
                "categoria": "Conhecer as lentes",
                "titulo": "lentes_ocupacional",
                "resposta": (
                    "As lentes ocupacionais são feitas para oferecer "
                    "conforto na visão de perto e em distâncias "
                    "intermediárias, como ao usar o computador ou "
                    "ler documentos.\n"
                    "Podem ser úteis para quem precisa dessas "
                    "distâncias no dia a dia, mas geralmente não "
                    "são destinadas à visão de longe."
                ),
            },
            {
                "categoria": "Conhecer as lentes",
                "titulo": "lentes_tipos_grau",
                "resposta": (
                    "Os tipos de grau apresentam características "
                    "diferentes. Selecione uma opção para conhecer "
                    "cada um deles."
                ),
            },
            {
                "categoria": "Conhecer as lentes",
                "titulo": "lentes_contato",
                "resposta": (
                    "As lentes de contato são uma alternativa prática "
                    "aos óculos.\n"
                    "A BioView e a Bausch + Lomb oferecem diferentes "
                    "modelos para correção visual, com opções que "
                    "atendem a diferentes necessidades de grau.\n"
                    "A escolha deve considerar as características "
                    "dos olhos e a orientação de um oftalmologista."
                ),
            },

            # Submenu com informações sobre os tipos de grau.
            # A chave "pai" indica que essas informações pertencem a um menu principal.
            {
                "categoria": "Conhecer as lentes",
                "pai": "lentes_tipos_grau",
                "titulo": "lentes_miopia",
                "resposta": (
                    "A miopia dificulta enxergar objetos distantes "
                    "com nitidez, enquanto a visão de perto costuma "
                    "ser mais clara.\n"
                    "Sua correção utiliza lentes negativas, que "
                    "geralmente são mais finas no centro e mais "
                    "espessas nas bordas."
                ),
            },
            {
                "categoria": "Conhecer as lentes",
                "pai": "lentes_tipos_grau",
                "titulo": "lentes_hipermetropia",
                "resposta": (
                    "A hipermetropia pode dificultar a visão de perto "
                    "e causar cansaço visual durante atividades "
                    "como leitura.\n"
                    "Sua correção utiliza lentes positivas, que "
                    "geralmente são mais espessas no centro e mais "
                    "finas nas bordas."
                ),
            },
            {
                "categoria": "Conhecer as lentes",
                "pai": "lentes_tipos_grau",
                "titulo": "lentes_astigmatismo",
                "resposta": (
                    "O astigmatismo pode causar visão embaçada ou "
                    "distorcida tanto de perto quanto de longe.\n"
                    "A correção utiliza lentes cilíndricas, que "
                    "compensam diferenças na curvatura da córnea "
                    "ou do cristalino. A prescrição também informa "
                    "um eixo de orientação entre 0° e 180°."
                ),
            },
            {
                "categoria": "Conhecer as lentes",
                "pai": "lentes_tipos_grau",
                "titulo": "lentes_presbiopia",
                "resposta": (
                    "A presbiopia é uma alteração natural da visão "
                    "relacionada à idade, geralmente percebida a "
                    "partir dos 40 anos. Ela dificulta o foco em "
                    "objetos próximos.\n"
                    "Isso acontece porque o cristalino perde "
                    "gradualmente sua flexibilidade. A correção "
                    "pode ser feita com óculos para perto ou lentes "
                    "multifocais, conforme a necessidade visual.\n"
                    "Com o passar dos anos, a adição para perto "
                    "pode aumentar."
                ),
            },

            # Informações que explicam a diferença entre os campos de visão.
            {
                "categoria": "Campo de visão",
                "titulo": "campo_visao_convencional",
                "resposta": (
                    "Nas lentes multifocais convencionais, o desenho "
                    "do campo de visão é padronizado, com áreas "
                    "destinadas à visão de longe, intermediária e "
                    "de perto.\n"
                    "O campo de visão é o mesmo para todos os usuários. "
                    "O que muda é o grau da lente e as medidas de "
                    "altura necessárias para a montagem, de acordo "
                    "com as características de cada pessoa.\n"
                    "Por serem lentes convencionais, geralmente "
                    "apresentam um corredor visual mais estreito, "
                    "podendo exigir um tempo de adaptação um pouco "
                    "maior, que varia de pessoa para pessoa."
                ),
            },
            {
                "categoria": "Campo de visão",
                "titulo": "campo_visao_digital",
                "resposta": (
                    "As lentes multifocais digitais utilizam a "
                    "tecnologia Freeform, que permite desenvolver "
                    "lentes personalizadas especificamente para "
                    "cada pessoa.\n"
                    "Diferentemente das lentes convencionais, "
                    "as digitais são produzidas considerando "
                    "características individuais, permitindo uma "
                    "distribuição mais ampla e personalizada dos "
                    "campos de visão, com corredores visuais "
                    "melhor distribuídos e menos distorções laterais.\n"
                    "Essa personalização proporciona maior conforto "
                    "visual e pode facilitar a adaptação. Os "
                    "laboratórios digitais também oferecem diferentes "
                    "opções de corredores progressivos, permitindo "
                    "escolher o desenho mais adequado às necessidades "
                    "e à rotina de cada pessoa.\n"
                    "Na Ótica Renew, nossa equipe pode apresentar "
                    "essas opções e ajudar você a identificar "
                    "o corredor visual mais adequado."
                ),
            },

            # Conteúdos sobre os tratamentos aplicados às lentes.
            {
                "categoria": "Conhecer os tratamentos",
                "titulo": "tratamentos_filtro_antirreflexo",
                "resposta": (
                    "O tratamento antirreflexo reduz os reflexos "
                    "de luz na superfície das lentes, ajudando a "
                    "proporcionar mais conforto visual e nitidez, "
                    "especialmente em ambientes iluminados.\n"
                    "Ele não deve ser confundido com o filtro "
                    "de luz azul."
                ),
            },
            {
                "categoria": "Conhecer os tratamentos",
                "titulo": "tratamentos_filtro_azul",
                "resposta": (
                    "O tratamento com filtro azul bloqueia a luz "
                    "nociva emitida por computadores, celulares e "
                    "outros eletrônicos, protegendo os olhos no "
                    "dia a dia. Ele ajuda a reduzir a fadiga ocular "
                    "e o ressecamento, proporcionando mais conforto "
                    "e bem-estar durante as horas em frente às telas."
                ),
            },
            {
                "categoria": "Conhecer os tratamentos",
                "titulo": "tratamentos_fotocromatica",
                "resposta": (
                    "As lentes fotocromáticas escurecem quando "
                    "expostas à radiação ultravioleta e voltam "
                    "a ficar mais claras em ambientes internos.\n"
                    "A mudança de tonalidade leva algum tempo "
                    "para acontecer. São uma opção prática para "
                    "quem deseja adaptar as lentes às condições "
                    "de iluminação."
                ),
            },
            {
                "categoria": "Conhecer os tratamentos",
                "titulo": "tratamentos_transitions",
                "resposta": (
                    "As lentes Transitions contam com tecnologia "
                    "avançada de escurecimento, que se adapta à "
                    "luminosidade do ambiente: quanto mais intensa "
                    "a claridade, mais escuras as lentes ficam. "
                    "Em ambientes internos ou com menor luminosidade, "
                    "elas clareiam novamente.\n"
                    "Além de oferecer praticidade no dia a dia, "
                    "as lentes proporcionam proteção contra os "
                    "raios UVA e UVB e contam com filtro de luz "
                    "azul incorporado à própria tecnologia da lente."
                ),
            },

            # Conteúdos sobre os materiais utilizados na fabricação das lentes.
            {
                "categoria": "Conhecer os materiais",
                "titulo": "materiais_resina",
                "resposta": (
                    "As lentes de resina são leves e oferecem "
                    "boa qualidade óptica, sendo uma opção comum "
                    "para óculos de uso diário.\n"
                    "São versáteis e podem receber diferentes "
                    "tratamentos, conforme a necessidade do usuário."
                ),
            },
            {
                "categoria": "Conhecer os materiais",
                "titulo": "materiais_policarbonato",
                "resposta": (
                    "As lentes de policarbonato são leves e "
                    "resistentes a impactos, sendo indicadas para "
                    "quem busca maior segurança e conforto.\n"
                    "São uma opção interessante para crianças, "
                    "esportistas e pessoas que precisam de lentes "
                    "mais resistentes."
                ),
            },
            {
                "categoria": "Conhecer os materiais",
                "titulo": "materiais_alto_indice",
                "resposta": (
                    "As lentes de alto índice permitem corrigir "
                    "o grau com lentes mais finas do que as "
                    "convencionais em muitas situações.\n"
                    "Existem diferentes índices, como 1.60, 1.67 "
                    "e 1.74. A escolha depende do grau, da armação "
                    "e das características da lente."
                ),
            },

            # Informação sobre os dias e horários disponíveis para o exame de vista.
            {
                "categoria": "Exame de vista",
                "titulo": "exame_horarios",
                "resposta": (
                    "O exame de vista é gratuito e pode ser realizado "
                    "antes da compra dos óculos.\n\n"
                    "Horários de atendimento:\n"
                    "• Segunda, terça, quinta e sexta-feira: "
                    "das 9h às 17h.\n"
                    "• Quarta-feira: das 9h às 12h.\n\n"
                    "Os horários estão sujeitos a alterações devido "
                    "a imprevistos ou à disponibilidade da médica."
                ),
            },

            # Informações institucionais sobre a Ótica Renew.
            {
                "categoria": "Informações sobre a Ótica Renew",
                "titulo": "informacoes_horarios",
                "resposta": (
                    "Horários de funcionamento da loja:\n"
                    "• Segunda a sexta-feira: das 9h às 18h.\n"
                    "• Sábado: das 9h às 13h.\n"
                    "• Domingo: fechado."
                ),
            },
            {
                "categoria": "Informações sobre a Ótica Renew",
                "titulo": "informacoes_endereco",
                "resposta": (
                    "Onde estamos?\n\n"
                    "Ótica Renew\n"
                    "Rua Dr. Feliciano Sodré, nº 215\n"
                    "Loja 18 – Centro\n"
                    "São Gonçalo – Rio de Janeiro\n\n"
                    "Venha nos visitar! Nossa equipe está pronta "
                    "para ajudar você a conhecer nossas opções "
                    "de lentes, armações e tratamentos.\n\n"
                    "Como chegar pelo Google Maps:\n"
                    "https://www.google.com/maps/search/?api=1&query=Otica+Renew+Rua+Doutor+Feliciano+Sodre+215+Loja+18+Sao+Goncalo+RJ&query_place_id=ChIJ4YL1rf6bmQAR7OKx5jRhNhw"
                ),
            },
            {
                "categoria": "Informações sobre a Ótica Renew",
                "titulo": "informacoes_pagamentos",
                "resposta": (
                    "Formas de pagamento aceitas:\n"
                    "• Dinheiro.\n"
                    "• Pix.\n"
                    "• Cartão de débito.\n"
                    "• Cartão de crédito.\n\n"
                    "Para confirmar as opções disponíveis e as "
                    "condições de parcelamento, consulte a equipe "
                    "da loja."
                ),
            },

            # Fluxo de atendimento para quem deseja solicitar um orçamento.
            # O chatbot não calcula valores; direciona o usuário para a equipe da loja.
            {
                "categoria": "Quero fazer orçamento",
                "titulo": "orcamento_positiva",
                "resposta": (
                    "Para solicitar seu orçamento, fale com a equipe "
                    "da Ótica Renew pelo WhatsApp:\n"
                    "https://wa.me/552126070247\n"
                    "Nossa equipe estará à disposição para ajudar você!"
                ),
            },
            {
                "categoria": "Quero fazer orçamento",
                "titulo": "orcamento_negativa",
                "resposta": (
                    "Sem problemas! Você pode continuar conhecendo "
                    "as opções disponíveis ou voltar ao menu principal."
                ),
            },
        ]

        # Remove os tipos de grau duplicados que estão sem um menu pai.
        # Isso evita manter registros antigos fora da estrutura de submenu.
        Informacao.objects.filter(
            categoria=objetos_categoria["Conhecer as lentes"],
            titulo__in=[
                "lentes_miopia",
                "lentes_hipermetropia",
                "lentes_astigmatismo",
                "lentes_presbiopia"
            ],
            pai__isnull=True
        ).delete()

        # Percorre todos os conteúdos definidos na lista "dados".
        # Cada item será cadastrado ou atualizado no banco.
        for item in dados:

            # Recupera a categoria correspondente ao conteúdo atual.
            # O nome é usado como chave no dicionário criado anteriormente.
            categoria = objetos_categoria[item["categoria"]]

            # Por padrão, o conteúdo não terá um item pai.
            # Essa variável será preenchida somente para os submenus.
            pai = None

            # Verifica se o item possui a chave "pai".
            # Se possuir, significa que ele é uma opção dentro de outro menu.
            if "pai" in item:

                # Busca no banco a informação que será o menu principal.
                # pai__isnull=True garante que seja um item principal,
                # e não outro submenu.
                pai = Informacao.objects.get(
                    categoria=categoria,
                    titulo=item["pai"],
                    pai__isnull=True
                )

            # Cria ou atualiza a informação no banco de dados.
            # A combinação de categoria, título e pai identifica o registro.
            # Se já existir, atualiza a resposta; caso contrário, cria um novo.
            Informacao.objects.update_or_create(
                categoria=categoria,
                titulo=item["titulo"],
                pai=pai,
                defaults={
                    "resposta": item["resposta"]
                }
            )

        # Lista de títulos antigos que não devem mais permanecer no banco.
        # Essa limpeza evita que opções de versões anteriores continuem aparecendo.
        titulos_antigos = [
            "lentes_introducao",
            "tratamentos_introducao",
            "materiais_introducao",
            "campo_visao_introducao",
            "exame_introducao",
            "informacoes_introducao",
            "orcamento_introducao",
            "lentes_atigmatismo"
        ]

        # Localiza e exclui os registros que possuem algum dos títulos antigos.
        Informacao.objects.filter(
            titulo__in=titulos_antigos
        ).delete()

        # Exibe uma mensagem de sucesso no terminal após finalizar o cadastro.
        # self.stdout.write escreve a mensagem no terminal.
        # self.style.SUCCESS aplica a formatação visual de sucesso do Django.
        self.stdout.write(
            self.style.SUCCESS(
                "Banco populado e informações atualizadas com sucesso!"
            )
        )