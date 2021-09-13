from django.shortcuts import render
from django.utils.translation import ugettext as _
from news.models import Post, Comment
from .forms import CommentForm

def news_index(request):
    posts = Post.objects.all().order_by('pk')
    
    return render(request, 'news_index.html', {'posts': posts,
											   'slide': '/img/slideshow.gif'})


def news_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    
    if posts.count() < 1: category = '<<{}>> {}'.format(category, _('NotFound'))
    return render(request, 'news_category.html', {'category': category,
												  'posts': posts})

def news_detail(request, pk):
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post
            )
            comment.save()
            # post_comment(request, comment)
    comments = Comment.objects.filter(post=post)    

    return render(request, 'news_detail.html', {'post': post,
												'comments': comments,
												'form': form})

def post_comment(request, new_comment):
    if request.session.get('has_commented', False):
        return HttpResponse('you have already commented')
    comments = Comment.objects.filter(post=post)
    c = comments.Comment(comment=new_comment)
    c.save()
    request.session['has_commented'] = True
    return HttpResponse('thanks for your comment')
