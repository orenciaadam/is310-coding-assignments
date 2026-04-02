import os
import json
import requests
from dotenv import load_dotenv
import pyeuropeana.apis as apis

load_dotenv()
europeana_api_key = os.getenv('EUROPEANA_API_KEY')
os.environ['EUROPEANA_API_KEY'] = europeana_api_key


print("=== DATA USA: Top 10 States by Population (2023) ===\n")

datausa_url = (
    "https://api.datausa.io/tesseract/data.jsonrecords"
    "?cube=acs_yg_total_population_5"
    "&drilldowns=State,Year"
    "&measures=Population"
    "&include=Year:2023"
    "&sort=Population.desc"
    "&limit=10,0"
)

datausa_response = requests.get(datausa_url)
datausa_data = datausa_response.json()
top_states = datausa_data["data"]

for entry in top_states:
    print(f"{entry['State']}: {entry['Population']:,}")

top_state = top_states[0]["State"]
print(f"\nChosen state for Europeana search: {top_state}")


print(f"\n=== EUROPEANA: Items related to '{top_state}' ===\n")

result = apis.search(
    query=top_state,
    qf="TYPE:IMAGE",
    media=True,
    thumbnail=True,
    rows=10,
)

print(f"Total results found in Europeana: {result['totalResults']}")

items = result.get('items', [])
print(f"\nPreview of first {min(3, len(items))} item(s):")
for item in items[:3]:
    title = item.get('title', ['No title'])[0]
    provider = item.get('dataProvider', ['Unknown'])[0]
    print(f"  Title: {title}")
    print(f"  Provider: {provider}\n")


safe_result = {k: v for k, v in result.items() if k != 'apikey'}
for item in safe_result.get('items', []):
    item.pop('apikey', None)

output = {
    "source": "Data USA + Europeana",
    "datausa_top_states_2023": top_states,
    "europeana_results_for_top_state": safe_result,
}

filename = "datausa_europeana_results.json"
with open(filename, "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

print(f"Results saved to {filename}")