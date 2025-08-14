import requests
from googletrans import Translator
import google.generativeai as genai
from app.config import API_KEY_GOOGLE,URL_GOOGLE

genai.configure(api_key="AIzaSyAGS8qY4QfchdgwahpUg-1OTpcwIav_nyk")


def verificar_noticia_google(manchete):

    params = {
        "query": manchete,
        "key": API_KEY_GOOGLE,
        "languageCode": "en-US"
    }

    resposta = requests.get(URL_GOOGLE, params=params)
    data = resposta.json()

    msg_p = 'Não foi possível determinar se a notícia é Falsa ou Verdadeira'
    cont_true = 0
    cont_false = 0

    if "claims" in data:
        for claim in data.get('claims',[]):
            #print('Título:', claim['text'])
            for review in claim['claimReview']:
                #print('Fonte:', review['publisher']['name'])
                #print('Classificação:', review['textualRating'])
                
                cont_true += review['textualRating'].lower() == 'true'
                cont_false += review['textualRating'].lower() == 'false'

                #print('Link:', review['url']+'\n')


        return 'Verdadeira' if cont_true > cont_false else "Falsa" if cont_false > cont_true else msg_p
        
    else:
        print("Nenhuma checagem encontrada.")
    
    return msg_p


def verificar_noticia_ia(text):
    modelo = genai.GenerativeModel("gemini-1.5-flash")

    prompt = (
        f"Classifique a seguinte notícia como VERDADEIRA ou FALSA. "
        f"Responda apenas com VERDADEIRA ou FALSA, sem explicações:\n\n{text}"
    )

    resposta = modelo.generate_content(prompt)
    classificacao = resposta.text.strip().upper() 

    if "VERDADEIRA" in classificacao:
        return "Verdadeira"
    else:
        return "Falsa" 


def verificar_noticia(msg):

    # Falta fazer a organização do texto vindo.

    translator = Translator()
    traducao = translator.translate(msg, dest='en')
    traducao_texto = traducao.text

    if verificar_noticia_google(traducao_texto) != 'Não foi possível determinar se a notícia é Falsa ou Verdadeira':
        return verificar_noticia_google(traducao_texto) 
    
    else: 
        return verificar_noticia_ia(msg)


    