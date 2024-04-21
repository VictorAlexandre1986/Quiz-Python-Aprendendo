import speech_recognition as sr

def reconhecer_fala():
    # Cria um reconhecedor de fala
    recognizer = sr.Recognizer()
    
    # Define o microfone como fonte de entrada de áudio
    with sr.Microphone() as source:
        print("Diga alguma coisa...")
        recognizer.adjust_for_ambient_noise(source)  # Ajusta para o ruído ambiente
        audio = recognizer.listen(source)  # Escuta o áudio do microfone

    try:
        print("Reconhecendo...")
        texto = recognizer.recognize_google(audio, language='pt-BR')  # Reconhece a fala usando o Google Speech Recognition
        print("Você disse:", texto)
    except sr.UnknownValueError:
        print("Não foi possível entender a fala")
    except sr.RequestError as e:
        print("Erro ao requisitar resultados; {0}".format(e))

if __name__ == "__main__":
    
    while True:
        reconhecer_fala()