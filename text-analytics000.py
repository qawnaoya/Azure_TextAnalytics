# %%
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
documents = [
    "iPhoneのマップやばいよ"
]

# %%
result = client.analyze_sentiment(documents)
docs = [doc for doc in result if not doc.is_error]

for idx, doc in enumerate(docs):
    print(documents[idx])
    print(doc.sentiment)
    print(doc.confidence_scores)

# %%
