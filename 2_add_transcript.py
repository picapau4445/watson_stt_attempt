# coding=utf-8
from watson_developer_cloud import SpeechToTextV1
import json
import traceback
import codecs
import sys

if len(sys.argv) < 2:
    print('Usage : python 2_add_transcript.py ${language_customization_id}')
    sys.exit(1)

language_customization_id = sys.argv[1]

credentials = json.load(open('credentials.json', "r"))

stt = SpeechToTextV1(
    iam_apikey=credentials["apikey"],
    url=credentials["url"])

TRANSCRIPT_JSON="transcript_sample.json"

with codecs.open(TRANSCRIPT_JSON,'r','utf-8') as f:
    custom_words = json.load(f)["words"]
    result_json = stt.add_words(
        customization_id=language_customization_id,
        words=custom_words).get_result()
