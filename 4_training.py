# coding=utf-8
from watson_developer_cloud import SpeechToTextV1
import json
import traceback
import codecs
import sys

if len(sys.argv) < 2:
    print('Usage : python 4_training.py ${language_customization_id}')
    sys.exit(1)

language_customization_id = sys.argv[1]

credentials = json.load(open('credentials.json', "r"))

stt = SpeechToTextV1(
    iam_apikey=credentials["apikey"],
    url=credentials["url"])

stt.train_language_model(
    customization_id=language_customization_id,
    word_type_to_add=None,
    customization_weight=None).get_result()
