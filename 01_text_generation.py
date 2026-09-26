import sys
from common import create_client, model_name
prompt = "Explain what an AI aent is in three sentences"
client=create_client()
response=client.models.generate_content(model=model_name(),contents=prompt)
print(response.text)
