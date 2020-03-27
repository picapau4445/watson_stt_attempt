# coding=utf-8
from watson_developer_cloud import SpeechToTextV1
import json
import traceback
import codecs
import sys

if len(sys.argv) < 2:
    print('Usage : python 3_show_word_list.py ${language_customization_id}')
    sys.exit(1)

language_customization_id = sys.argv[1]

credentials = json.load(open('credentials.json', "r"))

stt = SpeechToTextV1(
    iam_apikey=credentials["apikey"],
    url=credentials["url"])

result_json = stt.list_words(customization_id=language_customization_id, word_type=None, sort=None)
results = result_json.result["words"]
print(results)