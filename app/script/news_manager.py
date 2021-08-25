from time import sleep as dormir
from django.utils import timezone
from news.models import Post, Category

deb = False
""" categories """

cat = {}

cat[1], cr = Category.objects.get_or_create(pk = 4)
cat[1].name = "conception d'applications"

cat[2], cr = Category.objects.get_or_create(pk = 3)
cat[2].name = "développement"

cat[3], cr = Category.objects.get_or_create(pk = 1)
cat[3].name = "django"

cat[4], cr = Category.objects.get_or_create(pk = 2)
cat[4].name = "fun"

print('category           ================> in this file')
for c in cat.values():    #
	print(c.pk, c.name)   #
	if deb: x = 0         #
	else: c.save() ########


""" news """

post = {} # as posts appear ordered by 'pk':
# you will just need to edit 'pk' if you wish to change the order

post[1], cr = Post.objects.get_or_create(pk = 4)
post[1].title = "Serverless"
post[1].image = "/img/serverless.png"
post[1].categories.set([3, 4])

post[2], cr = Post.objects.get_or_create(pk = 3)
post[2].title = "Google Trends for Docker"
post[2].image = "/img/docker.png"
post[2].categories.set([3, 4])

post[3], cr = Post.objects.get_or_create(pk = 6)
post[3].title = "Une API REST, qu'est-ce que c'est ?"
post[3].image = "/img/api.rest.png"
post[3].categories.set([3, 4])

post[4], cr = Post.objects.get_or_create(pk = 2)
post[4].title = "Power your application with DigitalOcean"
post[4].image = "/img/sammy.gif"
post[4].categories.set([3, 4])

post[5], cr = Post.objects.get_or_create(pk = 5)
post[5].title = "Understanding Django’s Apps and AppConfig"
post[5].image = "/img/django-rocket.gif"
post[5].categories.set([3, 4])

post[6], cr = Post.objects.get_or_create(pk = 1)
post[6].title = "RSA Public Key Cryptography"
post[6].image = "/img/rsa.png"
post[6].categories.set([3])

post[7], cr = Post.objects.get_or_create(pk = 7)
post[7].title = "How To Secure Nginx with Let's Encrypt"
post[7].image = "/img/ssl.png"
post[7].categories.set([2])



















































post[1].body = """
Over the years cloud providers have started to offer more and more services, which abstract away the underlying infrastructure. The most common ones being:

Storage services, i.e. a simple service where files can be stored and retrieved via an easily accessible API. Most known examples are Amazon S3, Azure Blob Storage, Google Cloud Storage, DigitalOcean Spaces, ...

Database services in all forms, like the most common SQL databases (like PostgreSQL, Oracle, MySQL or Maria DB) and noSQL databases (like MongoDB, Cassandra, ElasticSearch, HBase, ... ). Typical examples being Amazon RDS, Amazon Dynamo DB, Azure SQL Database, Azure Cosmos DB, Google Cloud SQL, Google Cloud BigTable, MongoDB Atlas, ...

Docker container management, like running containers in a flexible, scalable and reliable way, all or not on Kubernetes. E.g. Amazon ECS, Amazon EKS, Google GKE, Azure AKS, Red Hat OpenShift Container Platform, ...

Content management systems and eCommerce platforms, like Wordpress, Drupal, Magento, ...

Identity management, like Auth0, Amazon Cognito, Azure AD, ...

But this is just the tip of the iceberg. Every cloud provider has an offering of hundreds of managed services, making it sometimes extremely difficult to find your way in this offering.

These abstractions have led to the new term of serverless. This doesn’t mean that there are no servers anymore, but rather that the underlying servers are fully abstracted away for the consumer of the service, i.e. the allocation of the infrastructure (server) is fully managed by the cloud provider.

The services can be the services described above (also called managed services, managed cloud, backend-as-a-service or BaaS), but it can also be services directly offered to developers in the form of functions which can be requested to be executed via an API. This type of serverless is called "Functions-as-a-service" (FaaS), with the most known ambassador being AWS Lambda, which is the implementation of Amazon of this service. Of course the other cloud providers have in the meantime similar offers like Google Cloud Functions, Azure Functions or IBM OpenWhisk.
"""
			   




post[2].body = "In simpler words, Docker is a tool that allows developers, sys-admins etc. to easily deploy their applications in a sandbox (called containers) to run on the host operating system i.e. Linux. The key benefit of Docker is that it allows users to package an application with all of its dependencies into a standardized unit for software development. Unlike virtual machines, containers do not have high overhead and hence enable more efficient usage of the underlying system and resources."



post[3].body = """
Une API est un ensemble de définitions et de protocoles qui facilite la création et l'intégration de logiciels d'applications. Elle est parfois considérée comme un contrat entre un fournisseur d'informations et un utilisateur d'informations, qui permet de définir le contenu demandé au consommateur (l'appel) et le contenu demandé au producteur (la réponse). Par exemple, l'API conçue pour un service de météo peut demander à l'utilisateur de fournir un code postal et au producteur de renvoyer une réponse en deux parties : la première concernant la température maximale et la seconde la température minimale.

REST est un ensemble de contraintes architecturales. Il ne s'agit ni d'un protocole, ni d'une norme. Les développeurs d'API peuvent mettre en œuvre REST de nombreuses manières.

Lorsqu'un client émet une requête par le biais d'une API RESTful, celle-ci transfère une représentation de l'état de la ressource au demandeur ou point de terminaison. Cette information, ou représentation, est fournie via le protocole HTTP dans l'un des formats suivants : JSON (JavaScript Object Notation), HTML, XLT, Python, PHP ou texte brut. Le langage de programmation le plus communément utilisé est JSON, car, contrairement à ce que son nom indique, il ne dépend pas d'un langage et peut être lu aussi bien par les humains que par les machines.
"""



post[4].body = """
When building a web or mobile application, we need to develop and deliver the app quickly. Equally important, the application needs to be fast for end users. That’s why you should consider DigitalOcean to power your app’s backend. It offers compute, storage, databases, and networking, through a developer-friendly interface optimized for productivity.

Not only is DigitalOcean easy to operate, it’s built with best-in-class Intel processors that run your app at blazing speeds. Cloud Spectator, a renowned benchmarking firm, found that DigitalOcean delivers superior price-performance compared to Amazon and Google. With DigitalOcean, one can choose whether to run the app directly on VMs or Kubernetes.
"""



post[5].body = """
With Django, you can take Web applications from concept to launch in a matter of hours. Django takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. Django is free, open source, fast, fully loaded, secure, scalable and versatile.

Introduction
=========================
A Django project is a collection of apps that work together to deliver a set of functions. This collection consists of apps provided by Django, ourselves and other developers. In a project, the full set of apps belonging to a project is found in the projects settings.py , declared as the INSTALLED_APPS variable.


Apps and AppConfig creation
===============================
When the application server starts (django-dev server or uwsgiserver), it loads the settings defined for the project to configure the site. The variable DJANGO_SETTINGS_MODULE defines the correct settings for the environment where your app is running i-e development or production. The loading process involves the loading of the URL configurations defined by each app and creating the URL tree structure. But before it does this and any of the other settingstasks, it needs to know about all the apps in the project. Hence as part of loading the project settings, the application server takes the INSTALLED_APPS and loads or generates an AppConfig object for each app. This collection of AppConfig objects are then stored in an instance of theApps class. This instance of the Apps class is called the master registry. This master registry is the registry for the entire Django project that is being run by this application server.


Interaction with Apps and AppConfig
=======================================
Using Django shell we can interact with this master registry for our project and get the AppConfig object for any of the installed apps.

The AppConfig objects have two very important attributes, name and label. The attribute name is exclusively set. The attribute label is however derived from this name attribute. Therefore when creating a custom AppConfig class it is compulsory to set the name attribute. The difference between the two will be clarified in the following code that was run in the Django shell.


>>> from django.apps import apps as proj_apps
>>> shop_app = proj_apps.get_app_config('shop')
>>> shop_app.name
'shop'
>>> shop_app.label
'shop'
>>> auth_app = proj_apps.get_app_config('auth')
>>> auth_app.label
'auth'
>>> auth_app.name
'django.contrib.auth'


From the above code, we learn that the name attribute is the Python import path to the app from the project’s base. To import, shop we only need to use import shop but for Django’s auth app we need to use django.contrib.auth. The label can be exclusively declared in the AppConfig class just like name but if not will be generated from the name attribute.

The instance of AppConfig for an app can also be used to access all the models in that application. The AppConfig class provides two methods for this purpose, get_models() and get_model(model_name) the functionality of each method is evident from the method names.


Defining custom AppConfig class
==================================
Custom AppConfig classes need to be defined in <app>/apps.py file. This file is generated for us by Django when we run the startapp management command. Anytime we create a custom AppConfig class in an app we need to inform Django about its existence. This is done by setting the variable default_app_config in the __init__.py file for that app. So if I wanted to define a custom AppConfig class in my shop app, I will have to update the __init__.py file of the shop app as follows.

default_app_config = 'shop.apps.<custom_config_class_name>'

The key reason to define a custom AppConfig class is to implement the ready() method, that has been declared in django.apps.Appconfig class. When Django loads the project and its apps, the ready() method is called on the AppConfig instnace of each app. Hence we can use the ready() method to change any of our app’s existing setup or to add to it. This method is mainly used to tell Django about signalhandlers in an app so that Django knows about their existence. Apart from signal handlers, we can inform Django about any tool that can’t be integrated with views templates or models.


Conclusion
======================
Apps and AppConfig are powerful tools. Understanding them clarifies in our mind how the Django project is loaded and how the server running the project accesses each part of our application and also how to add and register new tools in our apps. However, we need to be very careful when defining new tools and registering them with Django through AppConfig.ready(). The ready() method is called when an instance of the AppConfig class for that app is created. The URL configuration and translation systems are created only after each AppConfig instance has been created and added to the Apps class (as mentioned above in the Apps and AppConfig creation section). Attempts to access URLs before all the apps have been loaded will generate some funny errors. This is why the lazy versions of some tools exist such as reverse_lazy() and ugettext_lazy().


=============================
Written by Mohammad Asim Ayub
=============================
"""




post[6].body = """
Here are the basic steps to create an RSA public/private key pair. The cryptography depends on four integer numbers ;


* two prime numbers, p and q and their product n = pq

* a public exponent e, that does not divide evenly (p-1)(q-1)

* a private exponent d, such as the quotient (ed-1)/[(p-1)(q-1)] is an integer


The public key is the number pair (n, e). To encrypt a message M with that public key, one creates the encrypted message C, using the equation 1. To decrypt C the private key owner uses the equation 2.


C = M**e % n (eq. 1)

M = C**d % n (eq. 2)
"""



post[7].body = """
Introduction
==================
Let’s Encrypt is a Certificate Authority (CA) that provides an easy way to obtain and install free TLS/SSL certificates, thereby enabling encrypted HTTPS on web servers. It simplifies the process by providing a software client, Certbot, that attempts to automate most (if not all) of the required steps. Currently, the entire process of obtaining and installing a certificate is fully automated on both Apache and Nginx.

In this tutorial, you will use Certbot to obtain a free SSL certificate for Nginx on Ubuntu 16.04 and set up your certificate to renew automatically.

This tutorial uses the default Nginx configuration file instead of a separate server block file. We recommend creating new Nginx server block files for each domain because it helps to avoid some common mistakes and maintains the default files as a fallback configuration as intended. If you want to set up SSL using server blocks instead, you can follow this Nginx server blocks with Let’s Encrypt tutorial.



Prerequisites
======================
To follow this tutorial, you will need:


- One Ubuntu 16.04 server set up by following this initial server setup for Ubuntu 16.04 tutorial, including a sudo non-root user and a firewall.


- A fully registered domain name. This tutorial will use example.com throughout. You can purchase a domain name on Namecheap, get one for free on Freenom, or use the domain registrar of your choice.


- Both of the following DNS records set up for your server. You can follow this hostname tutorial for details on how to add them.

-- An A record with example.com pointing to your server’s public IP address.
-- An A record with www.example.com pointing to your server’s public IP address.


- Nginx installed by following How To Install Nginx on Ubuntu 16.04.



Step 1 — Installing Certbot
=============================================

The first step to using Let’s Encrypt to obtain an SSL certificate is to install the Certbot software on your server.

Certbot is in very active development, so the Certbot packages provided by Ubuntu tend to be outdated. However, the Certbot developers maintain a Ubuntu software repository with up-to-date versions, so we’ll use that repository instead.


Step 2 — Setting up Nginx
=============================================

Certbot can automatically configure SSL for Nginx, but it needs to be able to find the correct server block in your config. It does this by looking for a server_name directive that matches the domain you’re requesting a certificate for.


Step 3 — Allowing HTTPS Through the Firewall
=============================================

If you have the ufw firewall enabled, as recommended by the prerequisite guides, you’ll need to adjust the settings to allow for HTTPS traffic. Luckily, Nginx registers a few profiles with ufw upon installation.

Step 4 — Obtaining an SSL Certificate
=============================================

Certbot provides a variety of ways to obtain SSL certificates, through various plugins. The Nginx plugin will take care of reconfiguring Nginx and reloading the config whenever necessary.


Step 5 — Verifying Certbot Auto-Renewal
=============================================

Let’s Encrypt’s certificates are only valid for ninety days. This is to encourage users to automate their certificate renewal process. The certbot package we installed takes care of this for us by running ‘certbot renew’ twice a day via a systemd timer. On non-systemd distributions this functionality is provided by a script placed in /etc/cron.d. This task runs twice a day and will renew any certificate that’s within thirty days of expiration.


================================================
Written by Mitchell Anicas
================================================
"""


print('post                         =====================> in this file')
for p in post.values():             #
	p.created_on = timezone.now()   #
	if deb: x = 0                   #
	else: p.save() ##################


print('post                                        ===> in the database')
for ppp in Post.objects.all():                     #
	dormir(0.4)                                    #
	print(ppp.pk, ppp.title, ppp.image)            #
	################################################


