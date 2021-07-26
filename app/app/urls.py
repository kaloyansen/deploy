from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import path, include
from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers, serializers, viewsets

from work.models import Project, Visitor, Page
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
		#fields = ['title', 'description', 'technology', 'place', 'image']

class VisitorSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Visitor
		fields = ['ip_address', 'page_visited', 'event_date']

class PageSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Page
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
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'visitors', VisitorViewSet)
router.register(r'pages', PageViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'children', ChildViewSet)
router.register(r'parents', ParentViewSet)
router.register(r'progs', ProgViewSet)

admin.autodiscover()

urlpatterns = [
	path("", views.index, name="index"),
	path("base/", views.base, name="base"),
	path('rest/', include(router.urls)),
	path('auth/', include('rest_framework.urls', namespace='rest_framework')),
	path("memo/", include("memo.urls")),
	path("news/", include("news.urls")),
	path("work/", include("work.urls")),
	#path("mded/", include('mdeditor.urls')),
	path("admin/", admin.site.urls)
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if False:
	urlpatterns.append(
		path("stat/", serve, {'document_root': 'static',
							  'path': "img",
							  'show_indexes': True}))
	urlpatterns.append(
		path("cv/", serve, {'document_root': 'static/pdf',
							'path': "back-end.pdf"}))
