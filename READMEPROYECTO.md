
# Pre-requirements
- Install Ubuntu 18.04 64bit
- Posgresql, python 3.6.9, virtualenv

# Manual install (developers)
- `git clone git@gitlab.prod.uci.cu:fortes/ak-mined-arch-test.git`
- `cd ak-mined-arch-test`
- `virtualenv venv -p python3`
- `source ./venv/bin/activate`
- `pip install -r server/requirements/dev.txt`
- Uncompress the **db.zip**: `unzip db.zip` 
- `psql -h localhost -U postgres arch_test < db.sql`
- `python server/manage.py migrate`
- `python server/manage.py runserver`


# OLD - Manual install
- sudo apt install redis-server
- git clone git@gitlab.prod.uci.cu:fortes/ak-mined-arch-test.git
- cd ak-mined-arch-test
- virtualenv venv -p python3
- source ./venv/bin/activate
- pip install -r server/requirements/dev.txt
- python server/manage.py makemigrations
- python server/manage.py migrate
- python server/manage.py loaddata province
- python server/manage.py loaddata data
- python server/manage.py loaddata type
- python server/manage.py loaddata users
- python server/manage.py createsuperuser
- python server/manage.py loaddata structure
- python server/manage.py loaddata study_plan
- python server/manage.py loaddata summary_daily_attendance
- python server/manage.py loaddata teaching_group
- python server/manage.py loaddata person
- python server/manage.py runserver


# With Docker
- Fallow this steps: - [Docker UCI](./docs/docker_images_uci_conf.md)
- `git clone git@gitlab.prod.uci.cu:fortes/ak-mined-arch-test.git` 
- `cd ak-mined-arch-test`
- Uncompress the **db.zip**: `unzip db.zip` 
- `docker-compose up -d`

The <b>client</b> will be running here: http://localhost:4201

The <b>server</b> will be running here: http://localhost:8585

# (Skip this if you did above steps) - Data load
- `docker-compose run --rm ak-web ./manage.py loaddata users`
- `docker-compose run --rm ak-web ./manage.py createsuperuser`
- `docker-compose run --rm ak-web ./manage.py loaddata data`
- `docker-compose run --rm ak-web ./manage.py loaddata type`
- `docker-compose run --rm ak-web ./manage.py loaddata province`
- `docker-compose run --rm ak-web ./manage.py loaddata structure`
- `docker-compose run --rm ak-web ./manage.py loaddata study_plan`
- `docker-compose run --rm ak-web ./manage.py loaddata summary_daily_attendance`
- `docker-compose run --rm ak-web ./manage.py loaddata teaching_group`

The <b>client</b> will be running here: http://localhost:4201

The <b>server</b> will be running here: http://localhost:8585

#For testing purposes
You need to re-build this docker service (<b>ak_nginx_prod</b>)
- `cd ak-mined-arch-test`
- `docker-compose up --build ak_nginx_prod`

Then you can access the client: http://localhost:8282

# Updating docker image

1 - Type: `docker run -it --name="test_python" ak-mined-base /bin/bash`

If you are at UCI you can skip steps 2 and 4

2 - Type: `mv /root/.pip/pip.conf /root/.pip/Apip.conf`

3 - Type: `pip install [your library]`

4 - Type: `mv /root/.pip/Apip.conf /root/.pip/pip.conf`

5 - Type: `exit`

6 - Type: `docker ps -a`

After executing the above command look for the CONTAINER_ID of the container named "test_python", in my case it was a number like this "_549526bca5b3_" yours will be different

7 - Type: `docker commit [CONTAINER_ID] ak-mined-base`

8 - Type: `docker rm [CONTAINER_ID]`

Done

# Proof of concepts



# Project docs
- [Developers guidelines](./docs/developers-guidelines.md)
- [Redis](./docs/redis.md)
- [Celery](./docs/celery.md)
- [Sentry](./docs/sentry.md)
- [Open Street Map](./docs/openstreet-map-server.md)
- [HAproxy](./docs/HAproxy.md)
- [Postgres Master-Slave](./docs/postgres-mater-slave.md)
- [Docker UCI](./docs/docker_images_uci_conf.md)
- [Kubernets](./docs/Kubernets.md)
- [Architecture Image](./docs/WorkInProgress.png)
- [System design](https://github.com/donnemartin/system-design-primer#system-design-topics-start-here)


# i18n
The default language for programming will be English, with the labels:

- For HTML: `{ % trans 'message' %}`
- For javascript: `gettext('message')`
- For modeling: `_('message')`

Generate  traslations message: 
- Command to HTML and Python: `python manage.py makemessages -l es`
- Command to Javascript: `python manage.py makemessages -d djangojs -l es`

Compile message: 
- Command: `python manage.py compilemessages`

Other types of translations are available at: https://docs.djangoproject.com/en/3.0/topics/i18n/translation/

GUNICORN

gunicorn base.wsgi:application --bind 127.0.0.1:8000 --workers=2