"""
A translator service utilizing IBM Watson AI
"""

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
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

translation = language_translator.translate(
    text='Hello, how are you today?',
    model_id='en-fr').get_result()

def english_to_french(english_text):
    """
    Translate from english to french
    """
    if english_text is None:
        raise TypeError("Null input found for e2f translator")
    french_text = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    return french_text.get("translations")[0].get("translation")

def french_to_english(french_text):
    """
    Translate from french to english
    """
    if french_text is None:
        raise TypeError("Null input found for f2e translator")
    english_text = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    return english_text.get("translations")[0].get("translation")
