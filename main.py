from services.gemini_service import GeminiService


def get_user_question():
    user_question = input("Faça sua pergunta (ou digite 'sair' para encerrar): ")
    return user_question


def process_response(gemini_service, messages, user_question):
    messages = messages + "\nUsuário: " + user_question
    response = gemini_service.generate_chat_response(messages)
    print(f"Resposta: {response}\n")
    return messages


def handle_questions(gemini_service, messages):
    counter = 0
    while counter < 3:
        user_question = get_user_question()

        if user_question.lower() == "sair":
            print("Encerrando o chatbot.")
            return

        messages = process_response(gemini_service, messages, user_question)
        counter += 1

    print("Espero que eu tenha ajudado! Até mais.")

def execute_chat_bot():
    gemini_service = GeminiService()
    messages = GeminiService.get_base_context()
    handle_welcome_message()
    handle_questions(gemini_service, messages)


def handle_welcome_message():
    print("Olá! Bem-vindo ao seu Assistente Financeiro Pessoal.")
    print("Eu sou um chatbot baseado em IA, projetado para te ajudar com suas finanças.")
    print("Estou aqui para responder suas perguntas sobre orçamento, investimentos, planejamento financeiro e muito mais!")
    print("Vamos começar!\n")


execute_chat_bot()
