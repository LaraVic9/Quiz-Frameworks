import json

class Answer:
    def __init__(self, alt, correto):
        self.alt = alt
        self.correto = correto

class Question:
    def __init__(self, id, pergunta, respostas, nivel, dica):
        self.id = id
        self.pergunta = pergunta
        self.respostas = [Answer(r["alt"], r["correto"]) for r in respostas]
        self.nivel = nivel
        self.dica = dica

    def get_correct_answer(self):
        for resposta in self.respostas:
            if resposta.correto:
                return resposta

def run_quiz(questions):
    score = 0

    for question in questions:
        print(f"Pergunta: {question.pergunta}")
        for i, resposta in enumerate(question.respostas, start=1):
            print(f"{i}. {resposta.alt}")

        user_answer = input("Escolha a letra da resposta correta: ").strip().lower()

        correct_answer = question.get_correct_answer().alt.lower()
        if user_answer == correct_answer:
            print("Resposta correta!")
            score += 1
        else:
            print("Resposta incorreta.")

        print(f"Resposta correta: {correct_answer}\n")

    print(f"Sua pontuação final é: {score}/{len(questions)}")

# Carregar as perguntas do arquivo JSON
with open('quiz.json', 'r') as file:
    data = json.load(file)

perguntas = data["perguntas"]

# Criar objetos Question a partir dos dados do arquivo JSON
lista_de_perguntas = []
for pergunta_data in perguntas:
    question = Question(
        pergunta_data["id"],
        pergunta_data["pergunta"],
        pergunta_data["respostas"],
        pergunta_data["nivel"],
        pergunta_data["dica"]
    )
    lista_de_perguntas.append(question)

# Executar o quiz com as perguntas carregadas
run_quiz(lista_de_perguntas)
