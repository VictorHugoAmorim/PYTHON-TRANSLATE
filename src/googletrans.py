import speech_recognition as sr
import pyaudio
import time
from googletrans import Translator
#from translate import Translator

#Função para ouvir e reconhecer a fala
def ouvir_microfone():
    #Habilita o microfone do usuário
    microfone = sr.Recognizer()
    
    #usando o microfone
    with sr.Microphone() as source:
        
        #Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)
        
        #Frase para o usuario dizer algo
        print("Aguardando...")
        
        #Armazena o que foi dito numa variavel
        audio = microfone.listen(source)
        
    try:
        
        #Passa a variável para o algoritmo reconhecedor de padroes
        frase = microfone.recognize_google(audio,language='pt-BR')
        
        #Retorna a frase pronunciada
        print("Você disse: " + frase)
        
    #Se nao reconheceu o padrao de fala, exibe a mensagem
    except sr.UnknownValueError:
        print("Não entendi")

        
    return frase


print('Ola, sou sua Tradutora Virtual!\nDiga "OK" para iniciarmos')

frase=ouvir_microfone()
start = 'ok'

while start.upper() != frase.upper():
    print('comando não reconhecido, favor repetir')
    frase=ouvir_microfone()
if start.upper() == frase.upper():
    pass
    while True:
        #Gerando tradução
        ''' s = Translator(from_lang="Portuguese", to_lang="english")
        frase=ouvir_microfone()
        res= s.translate(frase)'''
        trad = Translator()
        frase=ouvir_microfone()
        res = trad.translate(str(frase), dest="en").text
        print(f'Português: "{frase.upper()}"\nInglês: "{res}"')
        if "Encerrar".upper() in frase.upper():
            print('Até logo')
            break


    

