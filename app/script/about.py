from work.models import Project

work = {}

work[3], cr = Project.objects.get_or_create(pk = 3)
work[3].title = "page web statiques et responsive"
work[3].description = """
Un site vitrine d'un développeur d'applications. Codé en python 3 avec django web framework.

Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. SQLite is the most used database engine in the world.

Plots are created with plotly.py, an interactive, open-source, and browser-based graphing library for Python.

Le code est deployé d'abord sur google cloud après l'avoir containerisé en image docker et puis sur digitalocean.com.

Il existe plusieurs des façons à gérer le contenu de la page web. Django administration est très utile. L'accès à la base de donnée est réalisé dans un envirenment objet, on code les classes nous-même. Une autre possibilté est django rest framework. C'est un api rest, un ensemble de définitions et de protocoles qui facilite la création et l'intégration de logiciels d'applications.
"""
work[3].place = "simplon.co, Grenoble, FRANCE"
work[3].technology = "python3.8, Django-3.2.4, django rest framework 3.12.4, jupiterlab 0.1.1, SQLite 3, bootstrap/4.1.3"
work[3].save()

print(work[3])
