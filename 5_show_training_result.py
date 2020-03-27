# coding=utf-8
from watson_developer_cloud import SpeechToTextV1
import json
import traceback
import codecs
import sys

if len(sys.argv) < 2:
    print('Usage : python 5_show_training_result.py ${language_customization_id}')
    sys.exit(1)

language_customization_id = sys.argv[1]

credentials = json.load(open('credentials.json', "r"))

stt = SpeechToTextV1(
    iam_apikey=credentials["apikey"],
    url=credentials["url"])

result_json = stt.get_language_model(language_customization_id)
results = result_json.result["status"]
print(results)