import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia

wikipedia.set_lang('pt')
engine = pyttsx3.init()

# Converte texto em fala usando pyttsx3
def falar(texto):
    engine.say(texto)
    engine.runAndWait()

# Captura áudio do microfone e converte para texto
def ouvir_microfone():    
    reconhecedor = sr.Recognizer()
    with sr.Microphone() as fonte:
        reconhecedor.adjust_for_ambient_noise(fonte)
        print("Diga algo...")
        audio = reconhecedor.listen(fonte)
    
    try:
        comando = reconhecedor.recognize_google(audio, language='pt-BR').lower()
        print(f"Você disse: {comando}")
        return comando
    except sr.UnknownValueError:
        print("Não entendi o áudio.")
        return ""
    except sr.RequestError as e:
        print(f"Erro no serviço de reconhecimento: {e}")
        return ""

# Processa o comando de voz e executa ações correspondentes
def pocessar_comando(comando):
    if 'youtube' in comando:
        webbrowser.open('https://www.youtube.com')
        falar("Abrindo o YouTube.")
        return False
    
    elif 'wikipédia' in comando:
        try:
            termo = comando.split('por')[-1].strip()
            resumo = wikipedia.summary(termo, sentences=2)
            falar(resumo)
        except:
            falar("Não encontrei informações sobre isso na Wikipedia.")
        return False
    
    elif 'farmácia' in comando or 'farmacia' in comando:
        webbrowser.open('https://www.google.com/maps/search/farmácia+próxima')
        falar("Mostrando farmácias próximas no mapa.")
        return False
    
    elif 'sair' in comando or 'parar' in comando:
        falar("Encerrando o assistente. Até mais!")
        return True
    
    else:
        falar("Comando não reconhecido. Tente novamente.")
        return False

if __name__ == "__main__":
    falar("Assistente ativado. Como posso ajudar?")
    
    while True:
        comando = ouvir_microfone()
        if comando:
            encerrar = processar_comando(comando)
            if encerrar:
                break