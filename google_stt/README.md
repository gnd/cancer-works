## About: 
Speech-to-text script based on Google's STT [python sample](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/speech/microphone). 

## Usage: 

- `apt-get install portaudio19-dev`
- `python3 -m pip install -r requirements.txt`
- Potential [bugfix](https://stackoverflow.com/questions/53790531/problem-with-import-google-cloud-speech-to-text-recognition): `pip install -U protobuf` 
- Export [GCloud authentication](https://cloud.google.com/docs/authentication/production#auth-cloud-explicit-python) token with enabled Speech service.
- Run `python ./transcribe_streaming_indefinite.py [--lang <langCode> --realtime <True|False>]`

