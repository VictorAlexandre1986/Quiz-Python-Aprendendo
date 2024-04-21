import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox, QLabel, QLineEdit

class QuizApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quiz App")
        self.setGeometry(100, 100, 400, 200)

        self.score = 0
        self.question_index = 0

        self.questions = [
            {"question": "Qual é a capital do Brasil?", "answer": "Brasília"},
            {"question": "Qual é o maior planeta do Sistema Solar?", "answer": "Júpiter"},
            {"question": "Quem escreveu 'Dom Quixote'?", "answer": "Miguel de Cervantes"},
            {"question": "Quantos elementos químicos a tabela periódica possui?", "answer": "118"},
            {"question": "Quem pintou 'Mona Lisa'?", "answer": "Leonardo da Vinci"},
            {"question": "Quem descobriu a penicilina?", "answer": "Alexander Fleming"},
            {"question": "Qual é o segundo maior país do mundo em área?", "answer": "Canadá"},
            {"question": "Qual é o símbolo químico do ouro?", "answer": "Au"},
            {"question": "Quantos continentes existem?", "answer": "7"},
            {"question": "Quem foi o primeiro presidente do Brasil?", "answer": "Deodoro da Fonseca"}
        ]

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.question_label = QLabel(self.questions[self.question_index]["question"])
        layout.addWidget(self.question_label)

        self.answer_edit = QLineEdit()
        layout.addWidget(self.answer_edit)

        self.answer_button = QPushButton("Responder")
        self.answer_button.clicked.connect(self.check_answer)
        layout.addWidget(self.answer_button)

        self.score_label = QLabel(f"Score: {self.score}")
        layout.addWidget(self.score_label)

        self.setLayout(layout)

    def check_answer(self):
        user_answer = self.answer_edit.text()
        if user_answer.lower() == self.questions[self.question_index]["answer"].lower():
            self.score += 1
            QMessageBox.information(self, "Correto", "Resposta correta!")
        else:
            QMessageBox.information(self, "Incorreto", "Resposta incorreta.")

        self.question_index += 1
        if self.question_index < len(self.questions):
            self.question_label.setText(self.questions[self.question_index]["question"])
            self.score_label.setText(f"Score: {self.score}")
            self.answer_edit.clear()
        else:
            QMessageBox.information(self, "Fim do Quiz", f"Quiz finalizado! Seu score final: {self.score}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    quiz_app = QuizApp()
    quiz_app.show()
    sys.exit(app.exec_())
