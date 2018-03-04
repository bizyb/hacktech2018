import requests
import json
from xml.etree import ElementTree


def get_token(sub_key):
    token_request_url = "https://api.cognitive.microsoft.com/sts/v1.0/issueToken"
    header = {"Ocp-Apim-Subscription-Key": sub_key}

    response = requests.post(token_request_url, headers=header)

    return response.text


def get_tts_audio(text):
    tts_uri = "https://speech.platform.bing.com/synthesize"

    body = ElementTree.Element('speak', version='1.0')
    body.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-us')
    voice = ElementTree.SubElement(body, 'voice')
    voice.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-US')
    voice.set('{http://www.w3.org/XML/1998/namespace}gender', 'Male')
    voice.set('name', 'Microsoft Server Speech Text to Speech Voice (en-US, BenjaminRUS)')
    voice.text = text

    token = get_token("8933078bcae341e5887899cded2f2f83")
    tts_header = {
        "X-Microsoft-OutputFormat": "audio-16khz-128kbitrate-mono-mp3", 
        "Content-Type": "application/ssml+xml", 
        "Host": "speech.platform.bing.com", 
        "Content-Length": b'197', 
        "Authorization": "Bearer {}".format(token)}

    audio_response = requests.post(tts_uri, data=ElementTree.tostring(body), headers=tts_header)

    return audio_response.content


def get_stt_text(audio_bytes):
    stt_uri = "https://speech.platform.bing.com/speech/recognition/dictation/cognitiveservices/v1?language=en-US&format=simple"

    stt_header = {
        "Ocp-Apim-Subscription-Key": "8933078bcae341e5887899cded2f2f83",
        "Content-type": "audio/mp3; codec=audio/pcm; samplerate=16000"}

    text_response = requests.post(stt_uri, data=audio_bytes, headers=stt_header)

    return json.loads(text_response.text).get('DisplayText')
