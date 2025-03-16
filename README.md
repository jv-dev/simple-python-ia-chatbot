*   **`.env`:** Armazena sua chave de API, mantendo-a fora do código-fonte, por questões de segurança.
*   **`main.py`:** O coração do chatbot. Contém a lógica para receber as perguntas, interagir com a API e exibir as respostas.
*   **`services/gemini_service.py`:** Responsável por toda a comunicação com a API Gemini. Deixa o código mais organizado.
* **`requirements.txt`**: Este arquivo é usado para manter um controle de todas as bibliotecas externas que seu código utiliza.

## Explicação do Código

### `main.py`

*   **`get_user_question()`:** Pede que o usuário faça uma pergunta, através do terminal.
*   **`process_response()`:** Formata a pergunta do usuário, envia para o serviço Gemini, recebe a resposta e mostra essa resposta ao usuário. **Agora esta função não guarda mais o historico da conversa, ele está sendo guardado na função `handle_questions`**.
*   **`handle_questions()`:** É aqui que o loop de perguntas e respostas acontece. O usuário pode fazer até 3 perguntas. **É aqui que é armazenado o historico da conversa**.
*   **`execute_chat_bot()`:** Inicializa o serviço Gemini, define o prompt base e começa a interação com o usuário.

### `services/gemini_service.py`

*   **`__init__()`:** É o construtor da classe. Ele inicializa o modelo Gemini (`gemini-1.5-flash`) e prepara a API para ser usada.
* **`get_base_context()`**: Define o prompt base, ou seja, o comportamento inicial do modelo.
*   **`generate_chat_response(self, messages)`:** Esta função recebe o histórico da conversa e envia para o modelo Gemini. Em seguida, retorna a resposta gerada pelo modelo.
* **`_format_messages(messages)`**: Esta funcao recebe a lista de mensagens, e as formata no formato correto, para que possam ser enviadas para o modelo Gemini.
*   **`__get_genai()`:** Configura a API Gemini, utilizando a chave da API que está no arquivo `.env`.

## Contribuições

Sinta-se à vontade para contribuir com o projeto! Se você deseja participar, siga estes passos:

1.  Faça um "fork" do repositório.
2.  Crie uma nova branch para a funcionalidade ou correção de bug que você deseja adicionar.
3.  Faça as alterações desejadas.
4.  Envie um "pull request" para que suas mudanças sejam analisadas e, possivelmente, incorporadas ao projeto.

## Licença

Este projeto é distribuído sob a [Licença MIT](LICENSE). Consulte o arquivo `LICENSE` para mais detalhes.

## Autor

*   João Victor Cardoso de Souza - [Perfil do GitHub](https://github.com/jv-dev)

---