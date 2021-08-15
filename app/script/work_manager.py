from work.models import Project

work = {}


work[4], cr = Project.objects.get_or_create(pk = 4)
work[4].title = "visualisation en-ligne des données expérimentales de H1 detector à HERA"
work[4].place = "DESY, Hamburg, ALLEMAGNE"
work[4].description = "les données sont stoquées d'abord dans la base de donnée oracle à l'aide de sql*loader, puis la visualisation est faite après la demande du client et selon cette demande à l'aide de gnuplpot"
work[4].technology = "perl, oracle, sql*loader, gnuplot, zsh"
work[4].image = "img/h1.png"


work[2], cr = Project.objects.get_or_create(pk = 2)
work[2].title = "Jets in Photoproduction at HERA, analyse scientifique des données experimentales de H1 détecteur à HERA"
work[2].place = "doctorat en physique des particles, hamburg univercity"
work[2].description = """
H1 est une expérience de physique localisée sur l'accélérateur HERA du centre de recherche DESY à Hambourg (Allemagne). Son objectif scientifique principal est l'étude de la structure du proton. Ses mesures concernent également l'étude des interactions élémentaires et la physique au-delà du modèle standard. L'expérience H1 a été en service entre 1991 et 2007 (fermeture de l'accélérateur HERA).
"""
work[2].technology = "C++, RooT"
work[2].image = "img/h1.old.png"


work[5], cr = Project.objects.get_or_create(pk = 5)
work[5].title = "H1 central trigger expert"
work[5].place = "DESY, Hamburg, ALLEMAGNE"
work[5].description = """
The H1 Trigger System is divided into four levels. The first and second level systems (L1 and L2) are phase-locked to the HERA accelerator clock of 10.4 MHz.

The L1 system provides a trigger decision for each bunch crossing after 2.3 µ sec. without causing dead time. A subset of the subdetector system data is used by most systems to generate fast informations concerning the general properties of the event. This is encoded in Boolean decisions (Trigger Elements).

The L2 system decision is presently derived from a combination of two independent hardware systems within 20 µs of the preceding L1 Keep signal, allowing sufficient time for transmission of trigger information and computation of the L2 trigger response.
"""
work[5].technology = "c, java"
work[5].image = "img/trigger.png"


work[6], cr = Project.objects.get_or_create(pk = 6)
work[6].title = "CALICE calorimètre électromagnétique prototype physique R&D"
work[6].place = "CNRS, IN2P3, Grenoble, FRANCE, l'étude d'un prototype de calorimètre électromagnétique y compris la reconstruction et la digitalisation du prototype"
work[6].description = "The CALICE collaboration (Calorimeter for Linear Collider Experiment) is undertaking a major program of R&D into calorimetry for the ILC, directed towards the design of an ILC calorimeter optimised for both performance and cost. It now has over 200 members from 41 institutes worldwide including all three major ILC regions, and is by far the largest group studying calorimetry for the ILC. New groups continue to join CALICE and these have recently included institutes in India, Canada and Spain."
work[6].technology = "The main direction of the collaboration R&D is to study particle flow (PFA) calorimetry, software compensation and individual particle reconstruction. As such, the studies are concentrating on fine granularity calorimeters with a high degree of longitudinal segmentation. These studies include comparison of simulation models with data to measure their degree of agreement, the technical issues of building a detector optimised for PFA calorimetry, and development of algorithms for software compensation and particle flow reconstruction."
work[6].image = "img/calice.png"


work[1], cr = Project.objects.get_or_create(pk = 1)
work[1].title = "concepteur développeur d'applications"
work[1].place = "simplon.co, Grenoble, FRANCE"
work[1].description = """
Le concepteur développeur d'applications conçoit et développe des services numériques à destination des utilisateurs en respectant les normes et standards reconnus par la profession et en suivant l'état de l'art de la sécurité informatique à toutes les étapes. La connaissance du métier du client pour lequel il réalise l'application peut être demandée.

Il prend en compte les contraintes économiques, en termes de coûts et de délais, les exigences de sécurité propres à son domaine d'intervention. Il peut aussi être amené, à la demande du client, à intégrer les principes liés à la conception responsable de services numériques. Pour concevoir et développer les interfaces utilisateur de type desktop ou web, il élabore une maquette avec les enchaînements d'écrans, qu'il fait valider à l'utilisateur.

Il code les formulaires de saisie et de résultats, ainsi que les états, en programmant de manière sécurisée les événements utilisateur et en accédant aux données stockées dans une base. Pour concevoir et mettre en œuvre la persistance des données, il analyse un cahier des charges fonctionnel ou une demande utilisateur afin de modéliser et de créer une base de données de type relationnel ou NoSQL (Not only SQL) ou d'adapter une base existante en l'optimisant ou en ajoutant des éléments et en veillant à ne pas introduire de vulnérabilité dans le système d'informations. Pour concevoir et développer une application multicouche répartie, il analyse la demande en s'appuyant sur une démarche permettant de construire les services numériques en plusieurs couches correspondant aux couches présentation, métier et persistance.

Il s'adapte en continu aux évolutions technologiques et réglementaires de la filière études et développement. Pour assurer cette veille, l'usage de la langue anglaise est souvent requis pour la lecture et la compréhension de documentations techniques ainsi que pour assurer des échanges techniques au moyen de textes courts avec des développeurs distants pouvant être de nationalités différentes.
"""
work[1].technology = "javascript, php, REST"
work[1].image = "img/web.png"


deb = False
pro = Project.objects.all()

print('dans le fichier:')
for w in work.values():
	print(w.id, w.title, w.image, w.description, w.technology)
	if deb:	x = 0
	else: w.save()


print('{} slides detected'.format(pro.count()))
#print(pro.values_list())


