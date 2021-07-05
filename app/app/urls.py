from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import path, include
from django.views.static import serve
from rest_framework import routers, serializers, viewsets
from demo import views as demoviews
from work.models import Project
from news.models import Post
from . import views

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['title', 'description', 'technology', 'place', 'image']

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'body', 'image', 'created_on', 'last_modified', 'categories']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'posts', PostViewSet)


urlpatterns = [
    path("", views.index, name="index"),
    path("base/", views.base, name="base"),
    path("demo/", demoviews.demo, name="demo"),
    path("plot/", demoviews.plot, name="plot"),
    path('rest/', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("work/", include("work.urls")),
    path("news/", include("news.urls")),
    path("admin/", admin.site.urls)
]

if False:
	urlpatterns.append(
		path("stat/", serve, {'document_root': 'static',
							  'path': "img",
							  'show_indexes': True}))
	urlpatterns.append(
		path("cv/", serve, {'document_root': 'static/pdf',
							'path': "back-end.pdf"}))
