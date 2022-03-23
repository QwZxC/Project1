from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Arcticle
from django.urls import reverse

def index(request):
    latest_arcticles_list = Arcticle.objects.order_by('-pub_date')[:5]
    return render(request,'rabotai/list.html',{'latest_arcticles_list':latest_arcticles_list})

def detail(request, article_id):
    try:
        a = Arcticle.objects.get(id = article_id)
    except:
        raise Http404("Статья не найдена")

    latest_comments_list = a.comment_set.order_by('-id')[:10]

    return render(request, 'rabotai/detail.html',{"article":a,'latest_comments_list':latest_comments_list})

def leave_comment(request, article_id):
    try:
        a = Arcticle.objects.get(id=article_id)
    except:
        raise Http404("Статья не найдена")
    a.comment_set.create(author_name = request.POST['name'],comment_text =request.POST['text'])

    return HttpResponseRedirect(reverse('rabotai:detail',args = (a.id,)))