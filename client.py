from letsrolld_api_client import Client
from letsrolld_api_client.api.default import get_directors
from letsrolld_api_client.api.default import get_directors_id
from letsrolld_api_client.api.default import get_films
from letsrolld_api_client.api.default import get_films_id


def report_film(film):
    print(f"Film: {film.title} ({film.year})")


def report_director(director):
    print(f"Director: {director.name}")
    for film in director.films:
        report_film(film)


def run():
    client = Client(base_url="http://localhost:8000")
    with client as client:
        # multiple directors
        for director in get_directors.sync(client=client):
            report_director(director)

        # director by id
        director = get_directors_id.sync(id=10, client=client)
        report_director(director)

        # multiple films
        for film in get_films.sync(client=client):
            report_film(film)

        # film by id
        film = get_films_id.sync(id=10, client=client)
        report_film(film)


if __name__ == "__main__":
    run()
