# Ótica Renew — Site Institucional e Chatbot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.13.15-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.1.2-092E20?style=for-the-badge&logo=django&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

**Projeto Extensionista — Aplicação de Cloud, IoT e Indústria 4.0 em Python**

</div>

---

## Sobre o projeto

O projeto Ótica Renew foi desenvolvido como parte das atividades do Projeto Extensionista da disciplina **Aplicação de Cloud, IoT e Indústria 4.0 em Python**.

A proposta consiste no desenvolvimento de um site institucional para a Ótica Renew, localizada em São Gonçalo, Rio de Janeiro, com a integração de um chatbot para realizar o pré-atendimento dos visitantes.

O objetivo é facilitar o acesso às informações da ótica, apresentando seus produtos, tipos de lentes, tratamentos e materiais, além de oferecer um canal inicial de comunicação com os clientes.

O sistema não realiza vendas on-line, cálculos de preços ou geração de orçamentos. Quando o visitante demonstra interesse em realizar um orçamento, o chatbot direciona o atendimento para o WhatsApp oficial da ótica.

## Objetivos

- Desenvolver um site institucional para apresentação da Ótica Renew.
- Integrar a interface desenvolvida em HTML e CSS ao framework Django.
- Implementar um banco de dados para armazenar as informações utilizadas pelo chatbot.
- Desenvolver um chatbot de pré-atendimento com navegação por menus e submenus.
- Facilitar o acesso dos visitantes às informações da empresa.

## Funcionalidades

### Site institucional

- Página inicial com apresentação da ótica.
- Página Sobre, com informações institucionais.
- Página Produtos, com apresentação dos produtos e opções disponíveis.
- Página Contato, com informações de atendimento e localização.

### Chatbot de pré-atendimento

O chatbot utiliza uma estrutura de menus e submenus para organizar as informações e orientar a navegação dos visitantes.

Entre as opções disponíveis estão:

- Conhecer os tipos de lentes.
- Conhecer os tratamentos.
- Conhecer os materiais das lentes.
- Consultar informações sobre campo de visão.
- Obter informações sobre exame de vista.
- Conhecer melhor a Ótica Renew.
- Solicitar orçamento pelo WhatsApp.

O chatbot também disponibiliza opções para retornar ao menu anterior, limpar a conversa e encerrar o atendimento.

## Tecnologias utilizadas

| Tecnologia | Aplicação no projeto |
|---|---|
| Python | Linguagem utilizada no desenvolvimento do back-end. |
| Django | Framework responsável pela estrutura e processamento da aplicação. |
| HTML5 | Estrutura das páginas do site. |
| CSS3 | Estilização e organização visual das páginas. |
| JavaScript | Interações e funcionamento do chatbot. |
| SQLite | Banco de dados utilizado para armazenar as informações do chatbot. |

## Banco de dados

O projeto utiliza SQLite, integrado ao Django, para armazenar as informações consultadas pelo chatbot.

Foram desenvolvidos dois modelos principais:

- **Categoria:** organiza os grupos de informações disponíveis no chatbot.
- **Informacao:** armazena os títulos e conteúdos das respostas, permitindo também a organização de subitens por meio de um relacionamento entre registros.

A comunicação entre o chatbot e o banco de dados é realizada por meio do ORM do Django, permitindo consultar as informações cadastradas e retornar as respostas correspondentes às opções selecionadas pelo visitante.

## Estrutura do projeto

```text
otica-renew-chatbot/
│
├── chatbot/
│   ├── management/
│   │   └── commands/
│   │       └── cadastrar_dados.py
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── images/
│   └── js/
│       └── chatbot.js
│
├── templates/
│   ├── index.html
│   ├── sobre.html
│   ├── produtos.html
│   └── contato.html
│
├── db.sqlite3
├── manage.py
└── requirements.txt
```

## Equipe e divisão das atividades

O desenvolvimento foi organizado em três blocos de atividades, conforme o planejamento estabelecido pela equipe.

### Andrezza Magalhães Cardoso — Bloco 1 e complementações

**Integração do Front-end com o Back-end**

- Desenvolvimento da documentação inicial do projeto.
- Desenvolvimento da interface do site utilizando HTML e CSS.
- Integração das páginas existentes ao Django.
- Organização dos templates e arquivos estáticos.
- Criação das rotas das páginas.
- Adaptação dos links e referências necessárias para o funcionamento dentro do Django.
- Verificação do funcionamento do site após a integração.

**Complementações no Bloco 2 — Banco de Dados e Integração com o Chatbot**

- Integração entre o chatbot, o Django e o banco de dados.
- Implementação das consultas utilizando o ORM do Django.
- Complementação e correção das informações cadastradas para atender ao escopo definido.
- Ajustes na comunicação entre o chatbot e o banco de dados.

### Júlio César — Bloco 2

**Banco de Dados e Integração com o Chatbot**

- Desenvolvimento da estrutura inicial do banco de dados SQLite.
- Criação dos modelos necessários no Django.
- Configuração das migrations.
- Preparação da estrutura inicial para armazenamento das informações utilizadas pelo chatbot.

### Stefany — Bloco 3

**Desenvolvimento do Chatbot e Testes**

- Desenvolvimento da estrutura de interação do chatbot.
- Implementação do menu principal e das opções de navegação.
- Desenvolvimento das respostas e caminhos condicionais.
- Implementação dos retornos entre menus.
- Tratamento de opções inválidas.
- Integração do chatbot ao front-end.
- Desenvolvimento das funcionalidades de interação e encerramento da conversa.
- Testes e validações

## Testes e validação

Foram realizadas verificações da aplicação e testes funcionais para avaliar o comportamento do site e do chatbot.

Entre os pontos verificados estão:

- Carregamento das páginas institucionais.
- Abertura e navegação do chatbot.
- Consulta às categorias e informações cadastradas.
- Navegação entre menus e submenus.
- Retorno ao menu anterior.
- Limpeza e encerramento da conversa.
- Funcionamento dos links de localização e contato pelo WhatsApp.

As evidências, os resultados obtidos e os ajustes identificados são apresentados no relatório de desenvolvimento do projeto.

## Hospedagem

As informações sobre a disponibilização e o acesso à versão hospedada do projeto serão adicionadas após a configuração do ambiente de publicação.

---

**Ótica Renew — Projeto Extensionista | 2026**