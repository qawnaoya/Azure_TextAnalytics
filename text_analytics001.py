# %%
import configparser
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
import seaborn as sns
import pandas as pd

# %%
sns.set_style('white')

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

doc = docs[0]

# %%
confidience_scores = {key:value for key, value in doc.confidence_scores.items()}

# %%
sentiment = pd.Series(confidience_scores)

# %%
sentiment


# %%
sentiment.plot.bar()

# %%
