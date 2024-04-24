## Installation

### Create an environment
```doctest
mkdir learn-flask
cd learn-flask
python -m vnev .venv
```

### Activate the environment
```doctest
. .venv/bin/activate
```

# Flask REST API Clean Architecture Practice
A Clean Architecture Practice with Flask REST API.

This is a practice project I used to learn Clean Architecture by implementing the REST API with a full Authentication/Authorization Protocols, Dependency Injection and furthermore the Swagger documentation.

## Basic Folder Structure

> application.py

The major application declaration file.

> apps

The Application Layer that defines API controller endpoint, global exceptions and also Request/Response/Presenter/Validator adapters.

> config

Application Configuration files are here.

> core

The core concept of the Clean Architecture practice. The `kernel` part is about the interface and abstract class definitions. The `core` part contains the business logic and the domains objects such as **entity**, **value object**, **use case** and also the **repository**.

> extensions

Some configuration and plugins I used, to make the application itself cleaner.

> infra

The Infrastructure Layer that provides the actual implementation of network, persistent, cache layer... etc.

> tests

Test folder, not implemented yet.

## Dependencies
* `flask`: Base Web Framework
* `werkzeug`: Utility Library under Flask
* `authlib`: OpenID Connect Provider Library
* `flask-restplus` = REST API, Swagger Library
* `flask-injector` = Dependency Injection
* `attrs` = Data Classes Utility LIbrary
* `cattrs` = Serialization / Deserialization

## Run the project
```
> pipenv sync
```

Enter Shell
```
> pipenv shell
```

Start App
```
> flask run
```