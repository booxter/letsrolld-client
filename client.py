from letsrolld_api_client import Client
from letsrolld_api_client.api.default import get_directors


client = Client(base_url="https://api.example.com")

with client as client:
    directors = get_directors.sync(client=client)
    print(directors)
