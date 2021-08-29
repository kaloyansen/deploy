from work.models import Project

work = {}

work[3], cr = Project.objects.get_or_create(pk = 3)
work[3].title = "page web statiques et responsive"
work[3].description = """
Un logiciel opérationnel est la principale mesure d’avancement.

https://kalodev.site
http://142.93.171.130

Un site vitrine d'un développeur d'applications. Codé en python 3 avec Django web framework. Le site est bilangue anglais/français et il s'adapte à la taille de n'importe quel écran sur lequel il s'affiche. Le site est entièrement crypté.

Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. SQLite is the most used database engine in the world.

Plots are created with plotly.py, an interactive, open-source, and browser-based graphing library for Python.

Le code est deployé d'abord sur google cloud après l'avoir containerisé en image docker et puis sur digitalocean.com.

Il existe plusieurs des façons à gérer le contenu de la page web. Django administration est très utile. L'accès à la base de donnée est réalisé dans un envirenment objet, on code les classes nous-même. Une autre possibilté est django rest framework. C'est un api rest, un ensemble de définitions et de protocoles qui facilite la création et l'intégration de logiciels d'applications.
"""
work[3].place = "simplon.co, Grenoble, FRANCE"
work[3].technology = "python3.8, Django-3.2.4, django rest framework 3.12.4, jupiterlab 0.1.1, SQLite 3, bootstrap/4.1.3, Docker version 20.10.6-ce, nginx/1.18.0, gunicorn (version 20.0.4), certbot 0.40.0, git version 2.32.0, git repository: https://github.com/kaloyansen/deploy"
work[3].save()

print(work[3])

work[8], cr = Project.objects.get_or_create(pk = 8)
work[8].description = """
Madame, Monsieur,


Je suis à la recherche d’une entreprise pouvant m’accueillir dans le cadre d’un contrat en alternance
(contrat d’apprentissage) pour la formation de concepteur développeur d’applications.

Cette formation a commencé le 10 mai 2021 et dure 12 mois. L’alternance est d’une semaine de formation en centre puis trois semaines en entreprise. Des tests techniques et un entretien individuel de motivation ont été effectués avec le responsable d’école simplon et ma candidature a été validée.

Les compétences visées sont maquetter une application, développer une interface utilisateur de type desktop, développer des composants d’accès aux données, développer la partie front-end d’une interface utilisateur web, développer la partie back-end d’une interface utilisateur web, concevoir une base de données, mettre en place une base de données, développer des composants dans le langage d’une base de données, collaborer à la gestion d’un projet informatique et à l’organisation de l’environnement de développement, concevoir une application, développer des composants métier, construire une application organisée en couches, développer une application mobile, préparer et exécuter les plans de tests d’une application, préparer et exécuter le déploiement d’une application.

Le développeur de logiciel a un rôle important dans une entreprise et plus largement dans le cadre de l’évolution de la société. Ce rôle me correspond car je suis responsable et organisé, j’aime le contact avec les gens et je suis efficace dans les missions qui me sont confiées. Je sais apprendre et trouver des solutions aux problèmes complexes. Je suis capable de travailler en autonomie ou en équipe. Je parle, je lis et j’écris l’anglais et le français ainsi que ma langue maternelle, le bulgare.

Mon parcours me permet d’avoir les compétences de bases pour ce métier mais j’ai à cœur de continuer à me former afin d’être parfaitement opérationnel dans la fonction visée. C’est pourquoi j’espère pouvoir trouver une entreprise qui pourra m’accueillir et à laquelle je pourrais proposer mes connaissances et mon investissement en échange.

Je souhaiterais un entretien afin de vous convaincre de ma motivation et je reste à votre disposition
pour tout renseignement complémentaire.


Veuillez agréer, Madame, Monsieur, l’expression de mes salutations distinguées.
"""
