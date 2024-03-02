
import openai
import os
import sys

openai.api_key = os.environ['OPENAI_API_KEY']

#List all opanai models
for model in openai.models.list():
    sys.stdout.write(model.id + '\n')
