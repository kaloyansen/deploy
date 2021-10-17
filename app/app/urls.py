import logging

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import path, re_path, include as incl
from django.views.generic import RedirectView, TemplateView
from django.views.static import serve

from rest_framework import routers, serializers, viewsets
import debug_toolbar

from work.models import Project, Visitor, Mage, ColorStyle
from news.models import Post, Comment, Category
from memo.models import Child, Prog, Parent
from memo.views import bgbgbg as memobg
from . import views

logger = logging.getLogger(__name__)

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ['url', 'username', 'email', 'is_staff']

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Project
		fields = '__all__'

class VisitorSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Visitor
		fields = '__all__'

class MageSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Mage
		fields = '__all__'

class ColorStyleSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ColorStyle
		fields = '__all__'

class PostSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Post
		fields = ['title', 'body', 'image', 'created_on', 'last_modified', 'categories']

class CommentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Comment
		fields = ['author', 'body', 'created_on', 'post']

class CategorySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Category
		fields = ['name']

class ChildSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Child
		fields = '__all__'

class ParentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Parent
		fields = '__all__'

class ProgSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Prog
		fields = ['name', 'code']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class ProjectViewSet(viewsets.ModelViewSet):
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer

class VisitorViewSet(viewsets.ModelViewSet):
	queryset = Visitor.objects.all()
	serializer_class = VisitorSerializer

class MageViewSet(viewsets.ModelViewSet):
	queryset = Mage.objects.all()
	serializer_class = MageSerializer

class ColorStyleViewSet(viewsets.ModelViewSet):
	queryset = ColorStyle.objects.all()
	serializer_class = ColorStyleSerializer

class PostViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer

class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class ChildViewSet(viewsets.ModelViewSet):
	queryset = Child.objects.all()
	serializer_class = ChildSerializer

class ParentViewSet(viewsets.ModelViewSet):
	queryset = Parent.objects.all()
	serializer_class = ParentSerializer

class ProgViewSet(viewsets.ModelViewSet):
	queryset = Prog.objects.all()
	serializer_class = ProgSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
#router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
#router.register(r'visitors', VisitorViewSet)
#router.register(r'mages', MageViewSet)
router.register(r'colorstyles', ColorStyleViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'children', ChildViewSet)
router.register(r'parents', ParentViewSet)
router.register(r'progs', ProgViewSet)

admin.autodiscover()

handler400 = 'app.views.handler400'
handler403 = 'app.views.handler403'
handler404 = 'app.views.handler404'
handler418 = 'app.views.handler418'
handler451 = 'app.views.handler451'
handler500 = 'app.views.handler500'
handler502 = 'app.views.handler502'
handler503 = 'app.views.handler503'

url_m = "https://freeshell.de/morla"
url_k = "https://kalodev.site"
url_h = "http://ka.lo"

url_patterns = [
	path('', views.index, name = 'index'),
	path('mindex/', views.mindex, name = 'mindex'),
	path('base/', views.base, name = 'base'),
	path('rest/', incl(router.urls)),
	path('i18n/', incl('django.conf.urls.i18n')),
	path('auth/', incl('rest_framework.urls', namespace = 'rest_framework')),
	re_path('^memo[/]?', incl('memo.urls')),
	re_path('^bg[/]?$', memobg, name = 'memo bg'),
	re_path('^news[/]?', incl('news.urls')),
	re_path('^work[/]?', incl('work.urls')),
	re_path('^admin[/]?', admin.site.urls),
	re_path('^face[/]?$', views.face, name = 'face'),
	re_path('^onn[n]+[/]?$', RedirectView.as_view(url = url_k), name = 'on'),
	re_path('^off[f]+[/]?$', RedirectView.as_view(url = url_h), name = 'off'),
	re_path('^morla[/]?$', RedirectView.as_view(url = url_m), name = 'morla')
]

if settings.DEBUG: url_patterns.append(path('__debug__/', incl(debug_toolbar.urls)))

parazit = ['.env', 'wp-login.php', 'owa/auth/logon.aspx', 'err', 'erreur', 'wlwmanifest.xml']
parazit_patterns = []
for url in parazit: parazit_patterns.append(re_path('{}[/]?$'.format(url),
													views.erreur,
													name = 'erreur'))

static_patterns = static(settings.STATIC_URL, document_root = settings.STATIC_ROOT, show_indexes = True) + static(settings.ENCRYPT_URL, document_root = settings.ENCRYPT_ROOT) + static(settings.ROBOTS_URL, document_root = settings.ROBOTS_ROOT) + static(settings.FAVICON_URL, document_root = settings.FAVICON_ROOT) + static(settings.CV_URL, document_root = settings.CV_ROOT)

last_patterns = [
	re_path('^bio[/]?$', views.bio, name = 'bio'),
	# re_path('^bio[/]?$', TemplateView.as_view(template_name = 'bio.html', content_type = 'text/html'), name = 'bio'),
	re_path('^model[/]?$', views.model, name = 'model'),
	# if no any corрesponding pattern found:
	#re_path('.*', RedirectView.as_view(url = '/'), name = 'mindex')
	re_path('.*', views.erreur, name = 'erreur') 
]


urlpatterns = url_patterns + parazit_patterns + static_patterns + last_patterns


# for up in urlpatterns: logger.info(up)
