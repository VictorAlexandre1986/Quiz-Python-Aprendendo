import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton, QPushButton, QMessageBox, QLabel
from PyQt5.QtCore import QTimer
import pyttsx3
import speech_recognition as sr

class QuizApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quiz App")
        self.setGeometry(100, 100, 400, 200)

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

        self.setup_ui()
        self.speak_question()
        self.setup_voice_recognition()

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
        try:
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source, timeout=5)

            user_answer = self.recognizer.recognize_google(audio)
            for radio_button in self.radio_buttons:
                if radio_button.text().lower() == user_answer.lower():
                    radio_button.setChecked(True)
                    break
        except sr.UnknownValueError:
            QMessageBox.warning(self, "Aviso", "Não foi possível entender sua resposta.")
        except sr.RequestError:
            QMessageBox.warning(self, "Aviso", "Erro na conexão com o serviço de reconhecimento de voz.")

    def check_answer(self):
        for radio_button in self.radio_buttons:
            if radio_button.isChecked():
                user_answer = radio_button.text()
                break
        else:
            QMessageBox.warning(self, "Aviso", "Selecione uma opção antes de responder.")
            return

        if user_answer == self.questions[self.question_index]["answer"]:
            self.score += 1
            QMessageBox.information(self, "Correto", "Resposta correta!")
        else:
            QMessageBox.information(self, "Incorreto", "Resposta incorreta.")

        self.question_index += 1
        if self.question_index < len(self.questions):
            self.clear_selection()  # Limpar seleção dos botões de rádio
            self.question_label.setText(self.questions[self.question_index]["question"])
            for radio_button, option in zip(self.radio_buttons, self.questions[self.question_index]["options"]):
                radio_button.setText(option)
            self.score_label.setText(f"Score: {self.score}")
            self.speak_question()
        else:
            QMessageBox.information(self, "Fim do Quiz", f"Quiz finalizado! Seu score final: {self.score}")

    def setup_ui(self):
        layout = QVBoxLayout()

        self.question_label = QLabel(self.questions[self.question_index]["question"])
        layout.addWidget(self.question_label)

        self.radio_buttons = []
        for option in self.questions[self.question_index]["options"]:
            radio_button = QRadioButton(option)
            layout.addWidget(radio_button)
            self.radio_buttons.append(radio_button)

        self.answer_button = QPushButton("Responder")
        self.answer_button.clicked.connect(self.check_answer)
        layout.addWidget(self.answer_button)

        self.score_label = QLabel(f"Score: {self.score}")
        layout.addWidget(self.score_label)

        self.setLayout(layout)

    def clear_selection(self):
        for radio_button in self.radio_buttons:
            radio_button.setChecked(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    quiz_app = QuizApp()
    quiz_app.show()
    QTimer.singleShot(1000, quiz_app.listen_for_answer)  # Iniciar o reconhecimento de voz após 1 segundo
    sys.exit(app.exec_())
