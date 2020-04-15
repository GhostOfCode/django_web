from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Article
from django.urls import reverse


def index(requst):
    latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    return render(requst, 'articles/list.html', {'latest_articles_list': latest_articles_list})


def detail(requst, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404('No article found!')

    latest_comments = a.comment_set.order_by('-id')[:10]

    return render(requst, 'articles/detail.html', {'article': a, 'latest_comments': latest_comments})


def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404('No article found!')

    a.comment_set.create(comment_author=request.POST['name'], comment_text=request.POST['text'])

    return HttpResponseRedirect(reverse('articles:detail', args=(a.id,)))
