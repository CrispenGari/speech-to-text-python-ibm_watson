
# importing packages
from ibm_watson import SpeechToTextV1, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json

# service credentials
url = "API_KEY"
api_key = "URL"

# Setting the authentication
try:
    auth = IAMAuthenticator(api_key)
    stt = SpeechToTextV1(authenticator=auth)
    stt.set_service_url(url)
except ApiException as e:
    print(e)

# converting audio to speech
with open("audios/short.mp3", "rb") as audio:
    res = stt.recognize(audio=audio, content_type="audio/mp3", model="en-AU_NarrowbandModel", continuous=True).get_result()


""""
* We are getting a python list of number of results
* We want to loop through them and create sentences
"""

sentences = res["results"]
sentence_list = []
for sentence in sentences:
    # adding a sentence with confidence that is greater than 50%
    sentence_list.append(str(sentence["alternatives"][0]["transcript"]).strip() if sentence["alternatives"][0]["confidence"] > 0.5 else "")

# print(json.dumps(sentence_list, indent=2))

with open("files/speech.txt", "w") as writter:
    for line in sentence_list:
        if line == "%HESITATION":
            writter.write(",")
        else:
            writter.write(line+" ")

print("DONE")
