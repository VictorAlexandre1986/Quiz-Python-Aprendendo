import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox, QLabel, QRadioButton, QButtonGroup


class QuizApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quiz App")
        self.setGeometry(100, 100, 400, 300)

        self.score = 0
        self.question_index = 0

        self.questions = [
            {"question": "Qual é a capital do Brasil?", "options": ["Rio de Janeiro", "São Paulo", "Brasília", "Belo Horizonte"], "answer": "Brasília"},
            {"question": "Qual é o maior planeta do Sistema Solar?", "options": ["Terra", "Júpiter", "Vênus", "Marte"], "answer": "Júpiter"},
            {"question": "Quem escreveu 'Dom Quixote'?", "options": ["Miguel de Cervantes", "William Shakespeare", "Charles Dickens", "Friedrich Nietzsche"], "answer": "Miguel de Cervantes"},
            {"question": "Quantos elementos químicos a tabela periódica possui?", "options": ["92", "108", "118", "128"], "answer": "118"},
            {"question": "Quem pintou 'Mona Lisa'?", "options": ["Pablo Picasso", "Leonardo da Vinci", "Vincent van Gogh", "Michelangelo"], "answer": "Leonardo da Vinci"},
            {"question": "Quem descobriu a penicilina?", "options": ["Louis Pasteur", "Alexander Fleming", "Robert Koch", "Joseph Lister"], "answer": "Alexander Fleming"},
            {"question": "Qual é o segundo maior país do mundo em área?", "options": ["Estados Unidos", "China", "Rússia", "Canadá"], "answer": "Canadá"},
            {"question": "Qual é o símbolo químico do ouro?", "options": ["Ag", "Fe", "Au", "Cu"], "answer": "Au"},
            {"question": "Quantos continentes existem?", "options": ["5", "6", "7", "8"], "answer": "7"},
            {"question": "Quem foi o primeiro presidente do Brasil?", "options": ["Dom Pedro II", "Getúlio Vargas", "Deodoro da Fonseca", "Juscelino Kubitschek"], "answer": "Deodoro da Fonseca"}
        ]

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.question_label = QLabel(self.questions[self.question_index]["question"])
        layout.addWidget(self.question_label)

        self.options_group = QButtonGroup()

        options = self.questions[self.question_index]["options"]
        for i, option in enumerate(options):
            radio_button = QRadioButton(option)
            self.options_group.addButton(radio_button, i)
            layout.addWidget(radio_button)

        self.answer_button = QPushButton("Responder")
        self.answer_button.clicked.connect(self.check_answer)
        layout.addWidget(self.answer_button)

        self.score_label = QLabel(f"Score: {self.score}")
        layout.addWidget(self.score_label)

        self.setLayout(layout)

    def check_answer(self):
        selected_button = self.options_group.checkedId()
        if selected_button != -1:
            selected_option = self.options_group.button(selected_button).text()
            correct_answer = self.questions[self.question_index]["answer"]
            if selected_option == correct_answer:
                self.score += 1
                QMessageBox.information(self, "Correto", "Resposta correta!")
            else:
                QMessageBox.information(self, "Incorreto", "Resposta incorreta.")

            self.question_index += 1
            if self.question_index < len(self.questions):
                self.question_label.setText(self.questions[self.question_index]["question"])
                options = self.questions[self.question_index]["options"]
                for i, option in enumerate(options):
                    self.options_group.button(i).setText(option)
                self.score_label.setText(f"Score: {self.score}")
            else:
                QMessageBox.information(self, "Fim do Quiz", f"Quiz finalizado! Seu score final: {self.score}")
        else:
            QMessageBox.warning(self, "Erro", "Selecione uma opção antes de responder.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    quiz_app = QuizApp()
    quiz_app.show()
    sys.exit(app.exec_())
