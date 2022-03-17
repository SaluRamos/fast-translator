import os
import pyperclip
from dependencies.google_trans_new.google_trans_new import google_translator

os.system("cls")
translator = google_translator()
print("Criado por .: Salu Conteratto Ramos")
phrase = str(input("Digite algo para ser traduzido: "))
from_language = "pt"
spacing_symbol = ";"
traduction = f"{phrase}{spacing_symbol}"
#total de 22 línguas (incluindo português)
#ingles (en)
#mandarim tradicional (zh-tw)
#mandarim simplificado (zh-cn)
#espanhol (es)
#frances (fr)
#russo (ru)
#hindi (hi)
#arabe (ar)
#japones (ja)
#bengali (bn)
#indonesio (id)
#coreano (ko)
#javanes (jw)
#alemão (de)
#telugo (te)
#marati (mr)
#turco (tr)
#vietnamita (vi)
#italiano (it)
#polaco (pl)
#holandes (nl)
languages = ["en", "zh-tw", "zh-cn", "es", "fr", "ru", "hi", "ar", "ja", "bn", "id", "ko", "jw", "de", "te", "mr", "tr", "vi", "it", "pl", "nl"]
for index, i in enumerate(languages):
    print(f"TRADUZINDO {index + 1} DE {len(languages)} ('{i}')")
    new_traduction = (translator.translate(phrase, lang_src = from_language, lang_tgt = i))[:-1]
    if index == len(languages)- 1:
        traduction = f"{traduction}{new_traduction}"
    else:
        traduction = f"{traduction}{new_traduction}{spacing_symbol}"
pyperclip.copy(traduction)
print("TEXTO COPIADO PARA A ÁREA DE TRANSFÊRENCIA!")