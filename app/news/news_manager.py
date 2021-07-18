from django.utils import timezone
from news.models import Post, Comment, Category

deb = False
""" categories """

cat1 = Category(pk = 4,	name = 'conception d\'applications')
cat2 = Category(pk = 3,	name = 'développement')
cat3 = Category(pk = 1,	name = 'django')
cat4 = Category(pk = 2,	name = 'fun')

cat1.save()
cat2.save()
cat3.save()
cat4.save()

co = Category.objects.all()
if deb:
	for c in co:
		print(c.pk, c.name)

""" news """
post1 = Post(pk = 1,
			 title = "Serverless",
			 body = "Over the years cloud providers have started to offer more and more services, which abstract away the underlying infrastructure. The most common ones being:\n\n\
\
Storage services, i.e. a simple service where files can be stored and retrieved via an easily accessible API. Most known examples are Amazon S3, Azure Blob Storage, Google Cloud Storage, DigitalOcean Spaces…\n\
Database services in all forms, like the most common SQL databases (like PostgreSQL, Oracle, MySQL or Maria DB) and noSQL databases (like MongoDB, Cassandra, ElasticSearch, HBase… ). Typical examples being Amazon RDS, Amazon Dynamo DB, Azure SQL Database, Azure Cosmos DB, Google Cloud SQL, Google Cloud BigTable, MongoDB Atlas… .\n\
Docker container management, like running containers in a flexible, scalable and reliable way, all or not on Kubernetes. E.g. Amazon ECS, Amazon EKS, Google GKE, Azure AKS, Red Hat OpenShift Container Platform…\
Content management systems and eCommerce platforms, like Wordpress, Drupal, Magento…\n\
Identity management, like Auth0, Amazon Cognito, Azure AD…\n\
But this is just the tip of the iceberg. Every cloud provider has an offering of hundreds of managed services, making it sometimes extremely difficult to find your way in this offering.\n\n\
\
These abstractions have led to the new term of serverless. This doesn’t mean that there are no servers anymore, but rather that the underlying servers are fully abstracted away for the consumer of the service, i.e. the allocation of the infrastructure (server) is fully managed by the cloud provider.\n\n\
\
The services can be the services described above (also called managed services, managed cloud, backend-as-a-service or BaaS), but it can also be services directly offered to developers in the form of functions which can be requested to be executed via an API. This type of serverless is called \"Functions-as-a-service\" (FaaS), with the most known ambassador being AWS Lambda, which is the implementation of Amazon of this service. Of course the other cloud providers have in the meantime similar offers like Google Cloud Functions, Azure Functions or IBM OpenWhisk.",
			 created_on = timezone.now(),
			 image = "/img/serverless.png")
post1.categories.set([3, 4])

post2 = Post(pk = 2,
			 title = "Google Trends for Docker",
			 body = "In simpler words, Docker is a tool that allows developers, sys-admins etc. to easily deploy their applications in a sandbox (called containers) to run on the host operating system i.e. Linux. The key benefit of Docker is that it allows users to package an application with all of its dependencies into a standardized unit for software development. Unlike virtual machines, containers do not have high overhead and hence enable more efficient usage of the underlying system and resources.",
			 created_on = timezone.now(),
			 image = "/img/docker.png")
post2.categories.set([3, 4])

post3 = Post(pk = 3,
			 title = "Une API REST, qu'est-ce que c'est ?",
			 body = "Une API est un ensemble de définitions et de protocoles qui facilite la création et l'intégration de logiciels d'applications. Elle est parfois considérée comme un contrat entre un fournisseur d'informations et un utilisateur d'informations, qui permet de définir le contenu demandé au consommateur (l'appel) et le contenu demandé au producteur (la réponse). Par exemple, l'API conçue pour un service de météo peut demander à l'utilisateur de fournir un code postal et au producteur de renvoyer une réponse en deux parties : la première concernant la température maximale et la seconde la température minimale.\n\nREST est un ensemble de contraintes architecturales. Il ne s'agit ni d'un protocole, ni d'une norme. Les développeurs d'API peuvent mettre en œuvre REST de nombreuses manières.\n\nLorsqu'un client émet une requête par le biais d'une API RESTful, celle-ci transfère une représentation de l'état de la ressource au demandeur ou point de terminaison. Cette information, ou représentation, est fournie via le protocole HTTP dans l'un des formats suivants : JSON (JavaScript Object Notation), HTML, XLT, Python, PHP ou texte brut. Le langage de programmation le plus communément utilisé est JSON, car, contrairement à ce que son nom indique, il ne dépend pas d'un langage et peut être lu aussi bien par les humains que par les machines.",
			 created_on = timezone.now(),
			 image = "/img/api.rest.png")
post3.categories.set([3, 4])


post4 = Post(pk = 4,
			 title = "DigotalOcean: Power your application with our infrastructure",
			 body = "When you’re building a web or mobile application, you need to develop and deliver your app quickly. Equally important, your application needs to be fast for end users. That’s why you should consider DigitalOcean to power your app’s backend. We offer compute, storage, databases, and networking, through a developer-friendly interface optimized for productivity.\n\nNot only is DigitalOcean easy to operate, it’s built with best-in-class Intel processors that run your app at blazing speeds. Cloud Spectator, a renowned benchmarking firm, found that DigitalOcean delivers superior price-performance compared to Amazon and Google. With DigitalOcean, you can choose whether to run your app directly on VMs or Kubernetes.",
			 created_on = timezone.now(),
			 image = "/img/sammy-404.gif")
post4.categories.set([3, 4])

post5 = Post(pk = 5,
			 title = "Get the latest official Django==3.2.5",
			 body = "With Django, you can take Web applications from concept to launch in a matter of hours. Django takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. Django is\nfree\nopen source\nridiculously fast\nfully loaded\nreassuringly secure\nexceedingly scalable\nand incredibly versatile.",
			 created_on = timezone.now(),
			 image = "/img/django-rocket.gif")
post5.categories.set([3, 4])


post1.save()
post2.save()
post3.save()
post4.save()
post5.save()
	



po = Post.objects.all()
if deb: print(po.values_list())
for p in po:
    print(p.pk, p.title, p.categories, p.image)
