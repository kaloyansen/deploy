from news.models import Post, Comment

po = Post.objects.all()
print(po.values_list())
for p in po:
    print(p.pk, p.title, p.image)
