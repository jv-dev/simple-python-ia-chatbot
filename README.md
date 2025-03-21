## Sobre o Projeto

Este chatbot foi criado para ser seu companheiro na jornada rumo à saúde financeira. Ele não é apenas um robô que responde perguntas; é um assistente que:

*   **Orienta nas suas finanças:** Te ajuda a entender melhor como lidar com seu dinheiro.
*   **Planeja o seu orçamento:** Auxilia na criação e gestão do seu orçamento pessoal.
*   **Explica investimentos:** Descomplica o mundo dos investimentos, explicando conceitos como poupança, CDB, ações e fundos imobilirios.
*   **Ajuda a definir metas:** Te ajuda a criar e acompanhar metas financeiras, sejam elas de curto, médio ou longo prazo.
*   **Responde às suas dúvidas:** Tira suas dúvidas sobre educação financeira de forma simples e clara.
*   **É intuitivo**: Você conversa com o chatbot de maneira simples e natural.
*   **É inteligente**: Ele usa o poder do modelo Gemini 1.5 Flash, da Google, para te dar as melhores respostas.
*   **É seguro**: Mantém sua chave de API privada, fora do código.
*   **Gera um resumo**: Ao final da conversa, ele gera um resumo de tudo que foi falado.

Em resumo, este projeto é uma porta de entrada para você começar a dominar suas finanças pessoais, com a ajuda da tecnologia e da inteligência artificial.

## Como Começar

### Pré-requisitos

*   **Python 3.9+:** Certifique-se de ter o Python 3.9 ou uma versão superior instalado em seu computador.
*   **Projeto Google Cloud:** Você precisará de um projeto no Google Cloud com a API Gemini ativada.
*   **Chave de API:** Obtenha uma chave de API para o Gemini no Google Cloud.
*   **Ambiente Virtual (Recomendado):** Recomenda-se criar um ambiente virtual para isolar as dependências do projeto.

### Passo a Passo para Executar o Projeto

1.  **Clone o Repositório:**
    *(Substitua `seu-usuario` pelo seu nome de usuário do GitHub.)*
2.  **Crie um Ambiente Virtual (Recomendado):**
3.  **Instale as Dependências:**
    *   Primeiro, certifique-se de que você está dentro do ambiente virtual.
    *   Instale a biblioteca `google-generativeai`:
4.  **Crie o Arquivo `.env`:**
    *   Crie um arquivo chamado `.env` no diretório raiz do projeto.
    *   Adicione sua chave de API Gemini ao arquivo: *(Substitua `SUA_CHAVE_DE_API_AQUI` pela sua chave de API real.)*

### Executando o Chatbot

1.  **Inicie o Chatbot:**
2.  **Interaja:** O chatbot irá exibir a mensagem: "Olá! Bem-vindo ao seu Assistente Financeiro Pessoal.". Digite suas perguntas e converse com seu novo assistente financeiro! Você pode fazer até 3 perguntas. Para encerrar antes, digite `sair`.

## Explicação do Código

### `main.py`

*   **`get_user_question()`:** Pede que o usuário faça uma pergunta, através do terminal.
*   **`process_response()`:** Formata a pergunta do usuário, envia para o serviço Gemini, recebe a resposta e mostra essa resposta ao usuário. **Agora esta função não guarda mais o histórico da conversa, ele está sendo guardado na função `handle_questions`**.
*   **`handle_questions()`:** É aqui que o loop de perguntas e respostas acontece. O usuário pode fazer até 3 perguntas. **É aqui que é armazenado o histórico da conversa**.
*   **`execute_chat_bot()`:** Inicializa o serviço Gemini, define o prompt base e começa a interação com o usuário.
* **`generate_summary()`**: Gera um resumo da conversa, usando o modelo Gemini.

### `services/gemini_service.py`

*   **`__init__()`:** É o construtor da classe. Ele inicializa o modelo Gemini (`gemini-1.5-flash`) e prepara a API para ser usada.
*   **`get_base_context()`**: Define o prompt base, ou seja, o comportamento inicial do modelo.
*   **`generate_chat_response(self, messages)`:** Esta função recebe o histórico da conversa e envia para o modelo Gemini. Em seguida, retorna a resposta gerada pelo modelo.
*   **`_format_messages(messages)`**: Esta função recebe a lista de mensagens, e as formata no formato correto, para que possam ser enviadas para o modelo Gemini.
*   **`__get_genai()`:** Configura a API Gemini, utilizando a chave da API que está no arquivo `.env`.

## Contribuições

Sinta-se à vontade para contribuir com o projeto! Se você deseja participar, siga estes passos:

1.  Faça um "fork" do repositório.
2.  Crie uma nova branch para a funcionalidade ou correção de bug que você deseja adicionar.
3.  Faça as alterações desejadas.
4.  Envie um "pull request" para que suas mudanças sejam analisadas e, possivelmente, incorporadas ao projeto.

## Apresentação

<iframe width="560" height="315" src="https://www.youtube.com/embed/I92ilXqa4HQ" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Autor

*   João Victor Cardoso de Souza

---