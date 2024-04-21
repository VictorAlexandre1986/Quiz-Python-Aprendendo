import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton, QPushButton, QMessageBox, QLabel
from questoes import questions

class QuizApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quiz App")
        self.setGeometry(100, 100, 400, 200)
        self.questions = questions
        self.score = 0
        self.question_index = 0



        self.setup_ui()

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
        else:
            QMessageBox.information(self, "Fim do Quiz", f"Quiz finalizado! Seu score final: {self.score}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    quiz_app = QuizApp()
    quiz_app.show()
    sys.exit(app.exec_())
