import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(engText):
    """
    Takes english text as inpute and outputs fench text
    """
    translation = language_translator.translate(text=engText, model_id='en-fr').get_result()
    return translation['translations'][0]['translation']

def french_to_english(frText):
    """
    Takes english text as inpute and outputs fench text
    """
    translation = language_translator.translate(text=frText, model_id='fr-en').get_result()
    return translation['translations'][0]['translation']