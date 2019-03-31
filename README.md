This cookiecutter creates a scaffold for a Django REST/Vue.js web app.

# Quick Start

1. Install <a href="https://github.com/audreyr/cookiecutter">cookiecutter</a>
2. Scaffold your project by running `cookiecutter gh:vpolisky/vpolisky/cookiecutter-django-vuejs`
3. Enter your project's name when you are asked for it

You also need _Vue CLI_ for building the client app and _docker-compose_.

# Project structure

The project has a typical Django project structure. The client app code is in the _webapp_ directory within the 
Django project.

Building the client app creates a _webapp/dist_ folder with the client app bundle. Its _index.html_ is
server via a Django template view from this folder. Other static assets are served by _Whitenoise_ also
from this folder.

# docker-compose

In the docker-compose, there are 3 services: _postgres_, _<project-name>-local_, _<project-name>_:

+ _<project-name>-local_:

    runs code from the project's directory
    
+ _<project-name>_:

    runs code from the container
    