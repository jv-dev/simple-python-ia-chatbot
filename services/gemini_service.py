import os

import google.generativeai as genai


class GeminiService:
    def __init__(self):
        self.__get_genai()
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def generate_chat_response(self, messages):
        self.__get_genai()

        response = self.model.generate_content(messages)
        return response.text

    @staticmethod
    def get_base_context():
        return """
            Você é um Assistente Financeiro Pessoal, especializado em ajudar usuários com finanças pessoais, orçamento, investimentos e planejamento financeiro. \
            Você deve responder de forma clara, amigável e em português brasileiro. \
            Suas principais funções são: \
            1. Ajudar o usuário a controlar gastos e criar orçamentos. \
            2. Fornecer dicas sobre como economizar dinheiro. \
            3. Explicar conceitos básicos de investimentos, como poupança, CDB, ações e fundos imobiliários. \
            4. Ajudar o usuário a definir metas financeiras de curto, médio e longo prazo. \
            5. Responder perguntas sobre educação financeira. \
            Sempre que possível, use exemplos práticos e sugira ferramentas ou aplicativos que possam ajudar o usuário. \
            Se o usuário fornecer informações sobre sua renda ou gastos, você pode ajudar a calcular quanto ele pode economizar ou investir. \
        """

    @staticmethod
    def _format_messages(messages):
        formatted_messages = []
        for msg in messages:
            formatted_messages.append({"role": msg["role"], "parts": [msg["content"]]})
        return formatted_messages

    @staticmethod
    def __get_genai():
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("A variável de ambiente GEMINI_API_KEY não está definida.")
        genai.configure(api_key=api_key)
