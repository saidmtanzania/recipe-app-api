# recipe-app-api
This repository is a RESTful API for managing recipe data, developed using the Django framework. With this API, users can easily retrieve, add, modify, and delete recipe information, all using standardized RESTful protocols. The API is designed to be scalable and easily integrated into existing applications or services, making it an ideal choice for anyone looking to build recipe management functionality into their own software. Whether you're building a cooking app, a meal planning service, or anything else that involves recipe data, this API has everything you need to get started.

## Contents

- [Requirements](#requirements)
- [Tools](#tools)
- [Installation](#installation)
- [Development](#development)
- [Production](#production)

## Requirements

- Python >=```3.9```
- Docker
- Git

## Tools

- ```Django>=3.0```
- ```djangorestframework>=3.12.4```
- ```psycopg2>=2.8.6```
- ```drf-spectacular>=0.15.1```
- ```Pillow>=8.2.0```
- ```uwsgi>=2.0.19```
- ```flake8>=3.9.2```


## Installation
- Perform installation in the following category

    ## Development
    1.Clone this repository

    ```
    https://github.com/saidmtanzania/recipe-app-api.git
    ```

    2.Change directory.

    ```
    cd recipe-app-api
    ```

    3.Create .env file.

    ```
    .env.sample file for references
    ```

    4.Run the command to build image
    ```
    docker compose build OR docker-compose build
    ```
    5.Run command to run api instance
    ```
    docker compose up OR docker-compose up
    ```

    ###### note: create superuser while container is running.
    ```
    docker compose run --rm app sh -c "python manage.py createsuperuser"
    ```
    ###### note: perform testing.
    ```
    docker compose run --rm app sh -c "python manage.py test"
    ```
    ###### note:access api documentation interface.
    ```
    127.0.0.1/api/docs/
    ```
    ###### note:access api admin interface.
    ```
    127.0.0.1/admin/
    ```

    ## Production

    1.Clone this repository

    ```
    https://github.com/saidmtanzania/recipe-app-api.git
    ```

    2.Change directory.

    ```
    cd recipe-app-api
    ```

    3.Create .env file.

    ```
    .env.sample file for references
    ```

    4.Run the command to build image

    ```
    docker-compose -f docker-compose-deploy.yml build
    ```

    5.Run command to run api instance

    ```
    docker-compose -f docker-compose-deploy run -d
    ```

    ###### note: create superuser while container is running

    ```
    docker-compose -f docker-compose-deploy run --rm app sh -c "python manage.py createsuperuser"
    ```

    ###### note:access api documentation interface

    ```
    clous_instance_url/api/docs/
    ```

    ###### note:access api admin interface

    ```
    cloud_instance_url/admin/
    ```


