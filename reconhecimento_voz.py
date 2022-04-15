import pyaudio
import speech_recognition as sr  #Importação da bibioteca de reconhecimento de voz

reconhecimento = sr.Recognizer()

with sr.Microphone() as microfone:  #Caso queira escolher um microfone específico vc precisa passar por parâmetro qual o índice do microfone
    reconhecimento.adjust_for_ambient_noise(microfone) #Ajuste dos ruídos... (ignora ruídos que não sejam a fala)
    print("\033[1;33mEstou ouvindo...\033[m")
    audio = reconhecimento.listen(microfone) #Código para ouvir o áudio
    texto = reconhecimento.recognize_google(audio, language="PT-BR") #Reconhecimento de idioma
    print("Você disse: {}".format(texto)) #Escreve na tela o que o usuário falou

#OBS: A Estrutura "with" inicializa a função do microfone e quando sai dessa "estrutura" ele fecha o microfone automaticamente.



















