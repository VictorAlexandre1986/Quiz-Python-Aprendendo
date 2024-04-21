import sys
import pyttsx3
import speech_recognition as sr

class QuizApp():
    def __init__(self):

        self.score = 0
        self.question_index = 0

        self.questions = [
            {"question": "Qual é a capital do Brasil?", "options": ["Brasília", "Rio de Janeiro", "São Paulo", "Salvador"], "answer": "Brasília"},
            {"question": "Qual é o maior planeta do Sistema Solar?", "options": ["Júpiter", "Saturno", "Marte", "Terra"], "answer": "Júpiter"},
            {"question": "Quem escreveu 'Dom Quixote'?", "options": ["Miguel de Cervantes", "William Shakespeare", "Friedrich Nietzsche", "Charles Dickens"], "answer": "Miguel de Cervantes"},
            {"question": "Quantos elementos químicos a tabela periódica possui?", "options": ["118", "92", "100", "150"], "answer": "118"},
            {"question": "Quem pintou 'Mona Lisa'?", "options": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"], "answer": "Leonardo da Vinci"},
            {"question": "Quem descobriu a penicilina?", "options": ["Alexander Fleming", "Marie Curie", "Louis Pasteur", "Albert Einstein"], "answer": "Alexander Fleming"},
            {"question": "Qual é o segundo maior país do mundo em área?", "options": ["Canadá", "Estados Unidos", "China", "Brasil"], "answer": "Canadá"},
            {"question": "Qual é o símbolo químico do ouro?", "options": ["Au", "Ag", "Fe", "Hg"], "answer": "Au"},
            {"question": "Quantos continentes existem?", "options": ["7", "5", "6", "8"], "answer": "7"},
            {"question": "Quem foi o primeiro presidente do Brasil?", "options": ["Deodoro da Fonseca", "Getúlio Vargas", "Juscelino Kubitschek", "Tancredo Neves"], "answer": "Deodoro da Fonseca"}
        ]

       
        self.setup_voice_recognition()
        self.engine = pyttsx3.init()

    def speak_question(self):
        engine = pyttsx3.init()
        engine.say(self.questions[self.question_index]["question"])
        for option in self.questions[self.question_index]["options"]:
            engine.say(option)
        engine.runAndWait()

    def setup_voice_recognition(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen_for_answer(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        try:
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source)

            user_answer = self.recognizer.recognize_google(audio, language='pt-BR')
            print(user_answer)
            return user_answer
        except sr.UnknownValueError:
            print("Não foi possível entender a fala")
        except sr.RequestError as e:
            print("Erro ao requisitar resultados; {0}".format(e))
        

    def check_answer(self,user_answer):
        user_answer = user_answer
        print(user_answer)
        if user_answer == self.questions[self.question_index]["answer"]:
            self.score += 1
            self.engine.say('Resposta correta')
            self.engine.say(f'Seu score é de : {self.score} pontos')
        else:
            self.engine.say('Resposta incorreta')
            self.engine.say(f'A resposta correta é : {self.questions[self.question_index]["answer"]}')

        self.question_index += 1
        if self.question_index < len(self.questions):
            self.speak_question()
        else:
            self.engine.say('Fim do Quiz , seu score final é de', self.score)

 


if __name__ == "__main__":
    quiz_app = QuizApp()
    while True:
        quiz_app.speak_question()
        resposta = quiz_app.listen_for_answer()
        quiz_app.check_answer(resposta)