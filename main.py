import os
import pyperclip
from google_trans_new import google_translator

def Core ():
    #input
    translator = google_translator()
    print("Criado por .: Salu Conteratto Ramos")
    print("Digite algo para ser traduzido: ", end = "")
    #total de 22 línguas (incluindo português)
    phrase = input()
    ingles = translator.translate(phrase, lang_src = 'pt', lang_tgt = 'en')
    ingles = ingles[:-1]
    mandarim_tradicional = translator.translate(phrase, lang_src = 'pt', lang_tgt = 'zh-tw')
    mandarim_tradicional = mandarim_tradicional[:-1]
    mandarim_simplificado = translator.translate(phrase, lang_src = 'pt', lang_tgt = 'zh-cn')
    mandarim_simplificado = mandarim_simplificado[:-1]
    espanhol = translator.translate(phrase, lang_src = 'pt', lang_tgt = 'es')
    espanhol = espanhol[:-1]
    frances = translator.translate(phrase, lang_src = 'pt', lang_tgt = 'fr')
    frances = frances[:-1]
    russo = translator.translate(phrase, lang_src = 'pt', lang_tgt = 'ru')
    russo = russo[:-1]
    hindi = translator.translate(phrase, lang_src = 'pt', lang_tgt = 'hi')
    hindi = hindi[:-1]
    arabe = translator.translate(phrase, lang_src = 'pt', lang_tgt = 'ar')
    arabe = arabe[:-1]
    japones = translator.translate(phrase, lang_src = 'pt', lang_tgt = 'ja')
    japones = japones[:-1]
    bengali = translator.translate(phrase, lang_src = 'pt', lang_tgt = 'bn')
    bengali = bengali[:-1]
    indonesio = translator.translate(phrase, lang_src = 'pt', lang_tgt = 'id')
    indonesio = indonesio[:-1]
    coreano = translator.translate(phrase, lang_src = 'pt', lang_tgt = 'ko')
    coreano = coreano[:-1]
    javanes = translator.translate(phrase, lang_src = 'pt', lang_tgt = 'jw')
    javanes = javanes[:-1]
    alemao = translator.translate(phrase, lang_src = 'pt', lang_tgt = 'de')
    alemao = alemao[:-1]
    telugo = translator.translate(phrase, lang_src = 'pt', lang_tgt = 'te')
    telugo = telugo[:-1]
    marati = translator.translate(phrase, lang_src = 'pt', lang_tgt = 'mr')
    marati = marati[:-1]
    turco = translator.translate(phrase, lang_src = 'pt', lang_tgt = 'tr')
    turco = turco[:-1]
    vietnamita = translator.translate(phrase, lang_src = 'pt', lang_tgt = 'vi')
    vietnamita = vietnamita[:-1]
    italiano = translator.translate(phrase, lang_src = 'pt', lang_tgt = 'it')
    italiano = italiano[:-1]
    polaco = translator.translate(phrase, lang_src = 'pt', lang_tgt = 'pl')
    polaco = polaco[:-1]
    holandes = translator.translate(phrase, lang_src = 'pt', lang_tgt = 'nl')
    holandes = holandes[:-1]
    #copiar tudo para o copyboard
    sp = ";"
    to_copyboard = phrase + sp + mandarim_tradicional + sp + mandarim_simplificado + sp + espanhol + sp + frances + sp + russo + sp + ingles + sp + hindi + sp + arabe + sp + japones + sp + bengali + sp + indonesio + sp + coreano + sp + javanes + sp + alemao + sp + telugo + sp + marati + sp + turco + sp + vietnamita + sp + italiano + sp + polaco + sp + holandes
    pyperclip.copy(to_copyboard)
    print("\nTEXTO COPIADO PARA A ÁREA DE TRANSFÊRENCIA!")

os.system("cls")
Core()