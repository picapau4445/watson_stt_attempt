# coding=utf-8
from watson_developer_cloud import SpeechToTextV1
import json
import traceback
import codecs
import sys

if len(sys.argv) < 3:
    print('Usage : python 6_tained_stt.py ${mp3_file_path} ${language_customization_id}')
    sys.exit(1)

mp3_file_path = sys.argv[1]
language_customization_id = sys.argv[2]

credentials = json.load(open('credentials.json', "r"))

stt = SpeechToTextV1(
    iam_apikey=credentials["apikey"],
    url=credentials["url"])

def recognizeWithLangModel(audio_file):
    with open(audio_file,'rb') as audio_file:
        return stt.recognize(
            audio=audio_file,
            content_type= "audio/mp3",
            model= "ja-JP_BroadbandModel",
            language_customization_id=language_customization_id,
            acoustic_customization_id=None,
            base_model_version=None,
            customization_weight=None,
            inactivity_timeout=None,
            keywords=None,
            keywords_threshold=None,
            max_alternatives=None,
            word_alternatives_threshold=None,
            word_confidence=None,
            timestamps=None,
            profanity_filter=None,
            smart_formatting=None,
            speaker_labels=None,
            customization_id=None,
            grammar_name=None,
            redaction=None)

try:
    result_json = recognizeWithLangModel(mp3_file_path)
    result = json.dumps(result_json.result, indent=2)
    f = open("trained_stt.json", "w")
    f.write(result)
    f.close()

    results = result_json.result["results"]
    for res in results:
        print(res["alternatives"][0]["transcript"])

except Exception as e:
    traceback.print_exc()