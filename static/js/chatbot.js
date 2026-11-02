
let conversaIniciada = false;

let menuAtual = null;

let historicoMenus = [];

const URL_WHATSAPP = 'https://wa.me/552126070247';

const nomesOpcoes = {
    lentes_visao_simples: 'Lentes de visão simples',
    lentes_multifocal: 'Lentes multifocais',
    lentes_ocupacional: 'Lentes ocupacionais',
    lentes_tipos_grau: 'Tipos de grau',
    lentes_contato: 'Lentes de contato',

    lentes_miopia: 'Miopia',
    lentes_hipermetropia: 'Hipermetropia',
    lentes_astigmatismo: 'Astigmatismo',
    lentes_atigmatismo: 'Astigmatismo',
    lentes_presbiopia: 'Presbiopia',

    campo_visao_convencional: 'Campo de visão convencional',
    campo_visao_digital: 'Campo de visão digital',

    tratamentos_filtro_antirreflexo: 'Antirreflexo',
    tratamentos_filtro_azul: 'Filtro de luz azul',
    tratamentos_fotocromatica: 'Lentes fotocromáticas',
    tratamentos_transitions: 'Transitions',

    materiais_resina: 'Resina',
    materiais_policarbonato: 'Policarbonato',
    materiais_alto_indice: 'Alto índice',

    exame_horarios: 'Horários do exame',

    informacoes_horarios: 'Horários de funcionamento',
    informacoes_endereco: 'Endereço da loja',
    informacoes_pagamentos: 'Formas de pagamento',

    orcamento_positiva: 'Quero fazer meu orçamento',
    orcamento_negativa: 'Não quero fazer meu orçamento'
};


// Abre e fecha a janela sem encerrar a conversa.
function toggleChat() {

    const chatBox = document.getElementById('chat-caixa');
    const botaoChat = document.querySelector('.chatbot-flutuante');

    chatBox.classList.toggle('ativo');

    if (botaoChat) {
        botaoChat.classList.toggle(
            'ativo',
            chatBox.classList.contains('ativo')
        );
    }

    if (chatBox.classList.contains('ativo') && !conversaIniciada) {
        conversaIniciada = true;
        carregarMenuPrincipal(true);
    }
}


// Posiciona a conversa no início da interação mais recente.
// O usuário controla a rolagem a partir desse ponto.
function posicionarInteracao(mensagem) {

    const mensagens = document.getElementById('chat-mensagens');

    requestAnimationFrame(() => {

        const posicao = mensagem.getBoundingClientRect().top
            - mensagens.getBoundingClientRect().top
            + mensagens.scrollTop;

        mensagens.scrollTop = posicao;
    });
}


// Cria o conteúdo da mensagem e transforma URLs em links.
function adicionarTextoComLinks(conteudo, texto) {

    const regexUrl = /https?:\/\/[^\s]+/g;

    let inicio = 0;
    let resultado;

    while ((resultado = regexUrl.exec(texto)) !== null) {

        // Adiciona o texto que aparece antes do link.
        conteudo.appendChild(
            document.createTextNode(texto.slice(inicio, resultado.index))
        );

        let url = resultado[0];

        // Retira pontuações que possam estar depois do endereço.
        let pontuacao = '';

        while (/[.,!?;:]$/.test(url)) {
            pontuacao = url.slice(-1) + pontuacao;
            url = url.slice(0, -1);
        }

        // Cria o link clicável.
        const link = document.createElement('a');

        link.href = url;
        link.textContent = 'Abrir localização no Google Maps';
        link.target = '_blank';
        link.rel = 'noopener noreferrer';

        conteudo.appendChild(link);

        // Adiciona a pontuação que foi retirada.
        if (pontuacao) {
            conteudo.appendChild(
                document.createTextNode(pontuacao)
            );
        }

        inicio = resultado.index + resultado[0].length;
    }

    // Adiciona o restante do texto depois do último link.
    conteudo.appendChild(
        document.createTextNode(texto.slice(inicio))
    );
}


// Cria uma mensagem na conversa.
function adicionarMensagem(texto, tipo) {

    const mensagens = document.getElementById('chat-mensagens');

    const mensagem = document.createElement('div');
    mensagem.className = `msg ${tipo}`;

    const conteudo = document.createElement('span');

    // Agora as URLs são exibidas como links clicáveis.
    adicionarTextoComLinks(conteudo, texto);

    mensagem.appendChild(conteudo);
    mensagens.appendChild(mensagem);

    return mensagem;
}


// Cria os botões de opções.
function adicionarBotao(container, texto, acao, classe = 'btn-opcao') {

    const botao = document.createElement('button');

    botao.type = 'button';
    botao.className = classe;
    botao.textContent = texto;
    botao.addEventListener('click', acao);

    container.appendChild(botao);
}


// Traduz os identificadores do banco.
function obterNomeOpcao(titulo) {

    return nomesOpcoes[titulo] || titulo;
}


// Adiciona os botões de navegação.
function adicionarNavegacao(container, incluirVoltar = true) {

    if (incluirVoltar) {
        adicionarBotao(
            container,
            'Voltar ao menu anterior',
            voltarMenuAnterior,
            'btn-navegacao'
        );
    }

    adicionarBotao(
        container,
        'Voltar ao menu principal',
        voltarMenuPrincipal,
        'btn-navegacao'
    );

    adicionarBotao(
        container,
        'Limpar conversa',
        limparConversa,
        'btn-navegacao'
    );

    adicionarBotao(
        container,
        'Encerrar conversa',
        encerrarConversa,
        'btn-navegacao'
    );
}


// Carrega as categorias principais.
async function carregarMenuPrincipal(primeiraAbertura = false) {

    menuAtual = null;
    historicoMenus = [];

    let mensagemInicio;

    if (primeiraAbertura) {

        mensagemInicio = adicionarMensagem(
            'Olá! Seja bem-vindo à Ótica Renew!\n' +
            'Sou o assistente virtual de pré-atendimento e estou aqui para ajudar você.',
            'bot'
        );

    } else {

        mensagemInicio = adicionarMensagem(
            'Como posso ajudar?',
            'bot'
        );
    }

    try {

        const response = await fetch('/api/chat/categorias/');

        if (!response.ok) {
            throw new Error('Não foi possível carregar as categorias.');
        }

        const dados = await response.json();

        const mensagem = adicionarMensagem(
            'Escolha uma opção para começar:',
            'bot'
        );

        const opcoes = document.createElement('div');
        opcoes.className = 'chat-opcoes';
        mensagem.appendChild(opcoes);

        dados.categorias.forEach(categoria => {

            adicionarBotao(opcoes, categoria.nome, () => {
                abrirCategoria(categoria.nome);
            });
        });

        adicionarBotao(
            opcoes,
            'Limpar conversa',
            limparConversa,
            'btn-navegacao'
        );

        adicionarBotao(
            opcoes,
            'Encerrar conversa',
            encerrarConversa,
            'btn-navegacao'
        );

        // Não rola automaticamente para o final.
        posicionarInteracao(mensagemInicio);

    } catch (erro) {

        console.error(erro);

        adicionarMensagem(
            'Não foi possível carregar as opções. Tente novamente.',
            'bot'
        );
    }
}


// Abre uma categoria.
async function abrirCategoria(nomeCategoria) {

    historicoMenus.push({ tipo: 'principal' });

    const mensagemInicio = adicionarMensagem(nomeCategoria, 'user');

    menuAtual = {
        categoria: nomeCategoria,
        pai: null
    };

    await carregarOpcoesCategoria(mensagemInicio);
}


// Carrega as opções da categoria ou do submenu.
async function carregarOpcoesCategoria(mensagemInicio = null) {

    const { categoria, pai } = menuAtual;

    try {

        let url = `/api/chat/categoria/${encodeURIComponent(categoria)}/`;

        if (pai) {
            url += `?pai=${encodeURIComponent(pai)}`;
        }

        const response = await fetch(url);

        if (!response.ok) {
            throw new Error('Não foi possível carregar as opções.');
        }

        const dados = await response.json();

        if (!mensagemInicio) {
            mensagemInicio = adicionarMensagem(
                obterNomeOpcao(pai),
                'user'
            );
        }

        if (!pai && dados.introducao) {
            adicionarMensagem(dados.introducao, 'bot');
        }

        const mensagem = adicionarMensagem(
            pai
                ? 'Escolha uma das opções:'
                : 'O que você gostaria de conhecer?',
            'bot'
        );

        const opcoes = document.createElement('div');
        opcoes.className = 'chat-opcoes';
        mensagem.appendChild(opcoes);

        dados.itens.forEach(item => {

            adicionarBotao(
                opcoes,
                obterNomeOpcao(item.titulo),
                () => selecionarOpcao(item)
            );
        });

        adicionarNavegacao(opcoes);

        // Mostra o início da interação, não o final das opções.
        posicionarInteracao(mensagemInicio);

    } catch (erro) {

        console.error(erro);

        adicionarMensagem(
            'Não foi possível carregar as opções. Tente novamente.',
            'bot'
        );
    }
}


// Processa a opção selecionada.
async function selecionarOpcao(item) {

    const nomeOpcao = obterNomeOpcao(item.titulo);

    const mensagemInicio = adicionarMensagem(nomeOpcao, 'user');

    historicoMenus.push({ ...menuAtual });

    // Encaminha o usuário para o WhatsApp.
    if (item.titulo === 'orcamento_positiva') {

        adicionarMensagem(
            'Para solicitar seu orçamento, entre em contato com nossa equipe pelo WhatsApp.',
            'bot'
        );

        const mensagem = adicionarMensagem(
            'Clique abaixo para conversar com a Ótica Renew:',
            'bot'
        );

        const opcoes = document.createElement('div');
        opcoes.className = 'chat-opcoes';
        mensagem.appendChild(opcoes);

        adicionarBotao(
            opcoes,
            'Conversar pelo WhatsApp',
            () => window.open(
                URL_WHATSAPP,
                '_blank',
                'noopener,noreferrer'
            )
        );

        adicionarNavegacao(opcoes);

        posicionarInteracao(mensagemInicio);

        return;
    }

    adicionarMensagem(item.resposta, 'bot');

    // Abre o submenu quando existem opções vinculadas.
    if (item.tem_subitens) {

        menuAtual = {
            categoria: menuAtual.categoria,
            pai: item.titulo
        };

        await carregarOpcoesCategoria(mensagemInicio);

        return;
    }

    const mensagens = document.getElementById('chat-mensagens');

    const opcoes = document.createElement('div');
    opcoes.className = 'chat-opcoes';

    mensagens.appendChild(opcoes);

    adicionarNavegacao(opcoes);

    posicionarInteracao(mensagemInicio);
}


// Volta ao menu anterior.
async function voltarMenuAnterior() {

    const mensagemInicio = adicionarMensagem(
        'Voltar ao menu anterior',
        'user'
    );

    if (historicoMenus.length === 0) {
        await carregarMenuPrincipal(false);
        posicionarInteracao(mensagemInicio);
        return;
    }

    const menuAnterior = historicoMenus.pop();

    if (menuAnterior.tipo === 'principal') {
        await carregarMenuPrincipal(false);
        posicionarInteracao(mensagemInicio);
        return;
    }

    menuAtual = menuAnterior;

    await carregarOpcoesCategoria(mensagemInicio);
}


// Volta ao menu principal.
async function voltarMenuPrincipal() {

    const mensagemInicio = adicionarMensagem(
        'Voltar ao menu principal',
        'user'
    );

    historicoMenus = [];

    await carregarMenuPrincipal(false);

    posicionarInteracao(mensagemInicio);
}


// Limpa a conversa e inicia novamente.
function limparConversa() {

    const mensagens = document.getElementById('chat-mensagens');

    mensagens.innerHTML = '';

    menuAtual = null;
    historicoMenus = [];
    conversaIniciada = true;

    carregarMenuPrincipal(true);
}


// Encerra o atendimento sem fechar a janela.
function encerrarConversa() {

    menuAtual = null;
    historicoMenus = [];

    const mensagemInicio = adicionarMensagem(
        'Encerrar conversa',
        'user'
    );

    const mensagem = adicionarMensagem(
        'Agradecemos por entrar em contato com a Ótica Renew!\n' +
        'Esperamos ter ajudado. Estamos à disposição quando precisar.',
        'bot'
    );

    const opcoes = document.createElement('div');
    opcoes.className = 'chat-opcoes';
    mensagem.appendChild(opcoes);

    adicionarBotao(
        opcoes,
        'Reiniciar atendimento',
        limparConversa,
        'btn-navegacao'
    );

    posicionarInteracao(mensagemInicio);
}