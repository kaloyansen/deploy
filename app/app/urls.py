from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import path, include
from django.views.generic import RedirectView, TemplateView
from django.views.static import serve


from rest_framework import routers, serializers, viewsets

from work.models import Project, Visitor, Page, ColorStyle
from news.models import Post, Comment, Category
from memo.models import Child, Prog, Parent
from . import views

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

class PageSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Page
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

class PageViewSet(viewsets.ModelViewSet):
	queryset = Page.objects.all()
	serializer_class = PageSerializer

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
#router.register(r'pages', PageViewSet)
router.register(r'colorstyles', ColorStyleViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'children', ChildViewSet)
router.register(r'parents', ParentViewSet)
router.register(r'progs', ProgViewSet)

admin.autodiscover()

url_m = "https://freeshell.de/morla"
url_k = "https://kalodev.site"
url_h = "http://ka.lo"

urlpatterns = [
	path("", views.index, name = "index"),
	path("base/", views.base, name = "base"),
	path("err/", views.erreur, name = "erreur"),
	path("erreur/", views.erreur, name = "erreur"),
	path("face/", views.face, name = "face"),
	path("f/a/c/e/", views.face, name = "face"),
	path("morla/", RedirectView.as_view(url = url_m), name = "morla"),
	path("on/",	RedirectView.as_view(url = url_k), name = "on"),
	path("off/", RedirectView.as_view(url = url_h), name = "off"),
	path("rest/", include(router.urls)),
	path("auth/", include("rest_framework.urls", namespace = "rest_framework")),
	path("memo/", include("memo.urls"), name = "memo"),
	path("news/", include("news.urls")),
	path("work/", include("work.urls")),
	#path("robots.txt", TemplateView.as_view(template_name = "robots.txt", content_type = "text/plain"), name = "robots"),
	path("tv", TemplateView.as_view(template_name = "erreur.html", content_type = "text/html"), name = "tv"),
	#path("github.ico", TemplateView.as_view(template_name = "../static/ico/github.ico", content_type = "image/x-icon"), name = "github icon"),
	#path("cv", TemplateView.as_view(template_name = "pdf/back-end.pdf", content_type = "pdf"), name = "cv"),
	#path("cv/", serve, {"document_root": 'static/pdf', "path": 'back-end.pdf'}),
	path("admin/", admin.site.urls)
]


urlpatterns += static(settings.STATIC_URL,
					  document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.ENCRYPT_URL,
					  document_root = settings.ENCRYPT_ROOT)
urlpatterns += static(settings.ROBOTS_URL,
					  document_root = settings.ROBOTS_ROOT)
urlpatterns += static(settings.FAVICON_URL,
					  document_root = settings.FAVICON_ROOT)
urlpatterns += static(settings.CV_URL,
					  document_root = settings.CV_ROOT)
