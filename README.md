

## Installation

You need to have docker installed on your system to run this project.

- [Install Docker](https://docs.docker.com/engine/install/) here.
- If you have not used docker in the past, please read this [introduction on docker](https://docs.docker.com/get-started/) here.

## Try it

```bash
git clone git@github.com:Nevo0/spotify-clone.git
cd spotify-clone
docker compose build web
docker compose run web python manage.py migrate
docker compose run web python manage.py createsuperuser
docker compose up -d
```

Then open http://127.0.0.1:8000 in your browser.

