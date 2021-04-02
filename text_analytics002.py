# %%
import codecs
import configparser
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

# %%
config = configparser.ConfigParser()
config.read('azure.config')

endpoint = config['AZURE']['azure_endpoint']
key = config['AZURE']['azure_ai_key']

# %%
client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# %%
ifs = codecs.open('N4830BU-1.txt', 'r', 'utf-8')

# %%
lines = ifs.readlines()

documents = [''.join(lines)]

# %%
response = client.recognize_entities(documents, language = "ja")

result = [doc for doc in response if not doc.is_error]

# %%
for doc in result:
    for entity in doc.entities:
        print(entity.text, entity.category)

# %%
ifs.close()

# %%