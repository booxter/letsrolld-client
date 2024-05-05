from letsrolld_api_client import Client
from letsrolld_api_client.api.default import get_directors


def report_film(film):
    print(f"Film: {film.title} ({film.year})")


def report_director(director):
    print(f"Director: {director.name}")
    for film in director.films:
        report_film(film)


def run():
    client = Client(base_url="http://localhost:8000")
    with client as client:
        for director in get_directors.sync(client=client):
            report_director(director)


if __name__ == "__main__":
    run()
