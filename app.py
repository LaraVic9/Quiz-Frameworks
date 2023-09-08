import json
import random

# Função para converter o nível de dificuldade de número para palavra
def nivel_para_palavra(nivel):
    if nivel == 1:
        return "Fácil"
    elif nivel == 2:
        return "Moderado"
    elif nivel == 3:
        return "Difícil"
    else:
        return "Desconhecido"

# Classe para representar uma pergunta
class Question:
    def __init__(self, id, pergunta, respostas, nivel, dica):
        self.id = id
        self.pergunta = pergunta
        self.respostas = respostas
        self.nivel = nivel
        self.dica = dica

    def display(self):
        print(f"Pergunta (Nível: {nivel_para_palavra(self.nivel)}):")
        print(self.pergunta)
        for i, resposta in enumerate(self.respostas, start=1):
            print(f"{i}. {resposta['alt']}")

    def check_resposta(self, user_resposta):
        correct_resposta = next((resposta for resposta in self.respostas if resposta["correto"]), None)
        if(resposta for resposta in self.respostas if resposta["correto"] == 'True'):
            return correct_resposta and correct_resposta["alt"].lower() == user_resposta.lower()
        else:
            print("Ops... algo deu errado")
        

# Estratégia de embaralhamento para perguntas de nível Fácil
class FacilShuffleStrategy:
    def shuffle(self, questions):
        return random.sample(questions, len(questions))

# Estratégia de embaralhamento para perguntas de nível Moderado
class ModeradoShuffleStrategy:
    def shuffle(self, questions):
        return random.sample(questions, len(questions))

# Estratégia de embaralhamento para perguntas de nível Difícil
class DificilShuffleStrategy:
    def shuffle(self, questions):
        return random.sample(questions, len(questions))

# Função para carregar perguntas de um arquivo JSON
def load_questions_from_json(quiz):
    with open('quiz.json', 'r') as quiz:
        data = json.load(quiz)

# Função para carregar perguntas de um arquivo JSON
def load_questions_from_json(quiz):
    with open('quiz.json', 'r') as quiz:
        data = json.load(quiz)

    perguntas_data = data["perguntas"]
    perguntas = []

    for pergunta_data in perguntas_data:
        id = pergunta_data["id"]
        pergunta = pergunta_data["pergunta"]
        respostas = pergunta_data["respostas"]
        nivel = pergunta_data["nivel"]
        dica = pergunta_data["dica"]
        perguntas.append(Question(id, pergunta, respostas, nivel, dica))

    return perguntas

# Função para embaralhar perguntas com base na estratégia de embaralhamento
def shuffle_questions(questions, shuffle_strategy):
    return shuffle_strategy.shuffle(questions)

# Exemplo de uso
perguntas = load_questions_from_json('perguntas.json')

# Crie instâncias das estratégias de embaralhamento para cada nível
facil_shuffle = FacilShuffleStrategy()
moderado_shuffle = ModeradoShuffleStrategy()
dificil_shuffle = DificilShuffleStrategy()

# Separe perguntas por nível
facil_questions = [pergunta for pergunta in perguntas if pergunta.nivel == "Fácil"]
moderado_questions = [pergunta for pergunta in perguntas if pergunta.nivel == "Moderado"]
dificil_questions = [pergunta for pergunta in perguntas if pergunta.nivel == "Difícil"]

for index, pergunta in enumerate(perguntas, start=1):
    print(f"Pergunta {index}:")
    pergunta.display()

    user_resposta = input("Digite a letra da resposta correta: ")

    if pergunta.check_resposta(user_resposta):
        print("Resposta correta!\n")
    else:
        print("Resposta incorreta. Dica: " + pergunta.dica + "\n")
