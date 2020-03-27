# coding=utf-8
from watson_developer_cloud import SpeechToTextV1
import json
import traceback
import codecs

credentials = json.load(open('credentials.json', "r"))

stt = SpeechToTextV1(
    iam_apikey=credentials["apikey"],
    url=credentials["url"])

result = stt.create_language_model(
      name="MyLanguageModel",
      base_model_name="ja-JP_BroadbandModel",
      dialect=None,
      description="MyLanguageModel")

language_customization_id = result.get_result()["customization_id"]
print("language_customization_id:", language_customization_id)
