# Speech To Text (stt)

This is a simple Artificial Intelligence Application that converts audios to speech using `ibm_watson`.


#### Application capabilities
This app is capable of:
* reading an audio from `audios` folder
* converts the audio to speech using `ibm_watson SpeechToTextV1()`
* write the converted speech to an external file `speech.txt` in the `files` folder

### Getting started
##### Installation
####### First you need to install `ibm_watson`
````shell
$pip install ibm_watson
````
###### Second you need to install `pip install PyJWT==1.7.1`
```shell
$pip install PyJWT==1.7.1
```
Then you are ready to go
##### Getting an API key and service URL
To get the service URL go to [IBM WATSON](https://cloud.ibm.com/catalog/services/)
* Create an account or login if you are a member
* Go to service
* Go to AI
* Look for Speech To Text and click
* Create a new project 
* Hunt for API keys in the docs

###### Importing packages

````
from ibm_watson import SpeechToTextV1, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json
````
###### Keys Variables
```
url = "API_KEY"
api_key = "URL"

```

###### Setting the authentication
```
try:
    auth = IAMAuthenticator(api_key)
    stt = SpeechToTextV1(authenticator=auth)
    stt.set_service_url(url)
except ApiException as e:
    print(e)
```
###### Converting audio to speech
```` 
with open("audios/long.mp3", "rb") as audio:
    res = stt.recognize(audio=audio, content_type="audio/mp3", model="en-AU_NarrowbandModel", continuous=True).get_result()
````

###### Write all the speech in a text file

```
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
```

###### All the code in one file `main.py`

````

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
with open("audios/long.mp3", "rb") as audio:
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
````
##### Changes 
There are a list of models and you can change the code based on what you want to achive
* Modes URL [HERE](https://cloud.ibm.com/apidocs/speech-to-text?code=python)
* Speech To Text Docs [HERE](https://cloud.ibm.com/apidocs/speech-to-text)
#### Why this simple Application.

This program was built for practical purposes

### Credits:
* [None](https//localhost)
