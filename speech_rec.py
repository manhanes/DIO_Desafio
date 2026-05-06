import speech_recognition as sr
import os
import webbrowser

def ouvir_comando():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Ajustando ruído de fundo... Aguarde.")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Pode falar! Estou ouvindo...")
        
        try:
            audio = recognizer.listen(source, timeout=5)
            comando = recognizer.recognize_google(audio, language='pt-BR')
            print(f"Você disse: {comando}")
            return comando.lower()
        except sr.UnknownValueError:
            print("Não entendi o que você disse.")
            return ""
        except sr.RequestError:
            print("Erro no serviço de reconhecimento de voz.")
            return ""

def executar_comando(comando):
    if 'abrir youtube' in comando:
        print("Abrindo YouTube...")
        # Abre o browser padrão do Windows
        webbrowser.open("https://www.youtube.com")
        
    elif 'abrir calculadora' in comando:
        print("Abrindo Calculadora...")
        os.system("cmd.exe /c calc.exe")
        
    elif 'bloco de notas' in comando:
        os.system("cmd.exe /c notepad.exe")

    elif 'encerrar' in comando:
        print("Desligando...")
        return False
    
    return True

if __name__ == "__main__":
    executando = True
    while executando:
        frase = ouvir_comando()
        if frase:
            executando = executar_comando(frase)
