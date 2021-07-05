from work.models import Project

pindex = Project(
    pk = 3,
    title = 'page web statiques et responsive',
    description = 'un site vitrine d\'un développeur d\'applications à servir comme CV en-ligne',
    place='simplon.co, Grenoble, FRANCE, https://freshell.de/morla',
    technology = 'python3.8, Django-3.2.4, bootstrap/4.1.3',
    image = 'img/django.png'
)

ph1gas = Project(
    pk = 4,
    title='visualisation en-ligne des données expérimentales de H1 detector à HERA',
    description='les données sont stoquées d\'abord dans la base de donnée oracle à l\'aide de sql*loader, puis la visualisation est faite après la demande du client et selon cette demande à l\'aide de gnuplpot',
    place='DESY, Hamburg, ALLEMAGNE',
    technology='perl, oracle, sql*loader, gnuplot, zsh',
    image='img/h1.png'
)

ph1ana = Project(
    pk = 2,
    title='Jets in Photoproduction at HERA, analyse scientifique des données experimentales de H1 détecteur à HERA',
    description='doctorat en physique des particles',
    place='H1 est une expérience de physique localisée sur l\'accélérateur HERA du centre de recherche DESY à Hambourg (Allemagne). Son objectif scientifique principal est l\'étude de la structure du proton. Ses mesures concernent également l\'étude des interactions élémentaires et la physique au-delà du modèle standard. L\'expérience H1 a été en service entre 1991 et 2007 (fermeture de l\'accélérateur HERA).',
    technology='C++, RooT',
    image='img/h1.old.png'
)

ph1trg = Project(
    pk = 5,
    title='H1 central trigger expert',
    description='le H1 central trigger à la recherche des HERA électron - proton collisions à enrégistrer',
    place='DESY, Hamburg, ALLEMAGNE',
    technology='The H1 Trigger System is divided into four levels. The first and second level systems (L1 and L2) are phase-locked to the HERA accelerator clock of 10.4 MHz. The L1 system provides a trigger decision for each bunch crossing after 2.3 µ sec. without causing dead time. A subset of the subdetector system data is used by most systems to generate fast informations concerning the general properties of the event. This is encoded in Boolean decisions (Trigger Elements). The L2 system decision is presently derived from a combination of two independent hardware systems within 20 µs of the preceding L1 Keep signal, allowing sufficient time for transmission of trigger information and computation of the L2 trigger response.',
    image='img/trigger.png'
)

pin2p3 = Project(
    pk = 6,
    title='CALICE calorimètre électromagnétique prototype physique R&D',
    description='The CALICE collaboration (Calorimeter for Linear Collider Experiment) is undertaking a major program of R&D into calorimetry for the ILC, directed towards the design of an ILC calorimeter optimised for both performance and cost. It now has over 200 members from 41 institutes worldwide including all three major ILC regions, and is by far the largest group studying calorimetry for the ILC. New groups continue to join CALICE and these have recently included institutes in India, Canada and Spain.',
    place='CNRS, IN2P3, Grenoble, FRANCE, l\'étude d\'un prototype de calorimètre électromagnétique y compris la reconstruction et la digitalisation du prototype',
    technology='The main direction of the collaboration R&D is to study particle flow (PFA) calorimetry, software compensation and individual particle reconstruction. As such, the studies are concentrating on fine granularity calorimeters with a high degree of longitudinal segmentation. These studies include comparison of simulation models with data to measure their degree of agreement, the technical issues of building a detector optimised for PFA calorimetry, and development of algorithms for software compensation and particle flow reconstruction.',
    image='img/calice.png'
)

lehoul = Project(
    pk = 7,
    title='Le Houl Association web site',
    description='le site web d\'une association des artist, surtout des musiciens, avec des utils des adhérantes et des adhérants, des enregistrements à écouter et les évenments de l\'association',
    place='Le Houl Association, Grenoble, FRANCE',
    technology='perl, python, CGI',
    image='img/houl.png'
)

simplo = Project(
    pk = 1,
    title='concepteur développeur d\'applications',
    place='Le·la concepteur·trice développeur·se d\'applications conçoit et développe des services numériques à destination des utilisateurs en respectant les normes et standards reconnus par la profession et en suivant l\'état de l\'art de la sécurité informatique à toutes les étapes. La connaissance du métier du client pour lequel il·elle réalise l\'application peut être demandée. Il·elle prend en compte les contraintes économiques, en termes de coûts et de délais, les exigences de sécurité propres à son domaine d\'intervention. Il·elle peut aussi être amené, à la demande du client, à intégrer les principes liés à la conception responsable de services numériques. Pour concevoir et développer les interfaces utilisateur de type desktop ou web, il·elle élabore une maquette avec les enchaînements d\'écrans, qu\'il·elle fait valider à l\'utilisateur. Il·elle code les formulaires de saisie et de résultats, ainsi que les états, en programmant de manière sécurisée les événements utilisateur et en accédant aux données stockées dans une base. Pour concevoir et mettre en œuvre la persistance des données, il·elle analyse un cahier des charges fonctionnel ou une demande utilisateur afin de modéliser et de créer une base de données de type relationnel ou NoSQL (Not only SQL) ou d\'adapter une base existante en l\'optimisant ou en ajoutant des éléments et en veillant à ne pas introduire de vulnérabilité dans le système d\'informations. Pour concevoir et développer une application multicouche répartie, il·elle analyse la demande en s\'appuyant sur une démarche permettant de construire les services numériques en plusieurs couches correspondant aux couches présentation, métier et persistance. Il·elle s\'adapte en continu aux évolutions technologiques et réglementaires de la filière Etudes et développement. Pour assurer cette veille, l\'usage de la langue anglaise est souvent requis pour la lecture et la compréhension de documentations techniques ainsi que pour assurer des échanges techniques au moyen de textes courts avec des développeurs distants pouvant être de nationalités différentes.',
    description='simplon.co, Grenoble, FRANCE',
    technology='javascript, php, REST',
    image='img/web.png'
)


pro = Project.objects.all()
for p in pro:
    print(p.id) #p.title, p.image, p.description, p.technology)
    p.delete()
pro.delete()

pindex.save()
ph1gas.save()
ph1ana.save()
ph1trg.save()
pin2p3.save()
lehoul.save()
simplo.save()

print('{} slides detected'.format(pro.count()))
print(pro.values_list())


# exit('à toute à l\'heure')
