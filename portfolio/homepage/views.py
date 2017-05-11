from django.template.response import TemplateResponse
from django import forms
from django import http
import datetime
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from homepage.forms import EmailForm
from homepage.models import Blog, Post

class NameForm(forms.Form):
    your_name = forms.CharField(label = "Your Name", max_length = 100)



def homepage(request):
    context = {
        'page_title': 'Test Home Page'
    }
    return TemplateResponse(request, 'homepage.html', context)

def profile(request):
    return TemplateResponse(request, 'index.html', {})

def hello(request):
    form = NameForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            print(form.cleaned_data['your_name'])
            return http.HttpResponseRedirect('/')

    context = {
        'form': form
    }
    return TemplateResponse(request, 'hello.html', context)


def contact_me(request):
    form = EmailForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            send_mail(
                form.cleaned_data['your_name'],
                form.cleaned_data['your_email'] + "\n" + form.cleaned_data['your_question'],
                'some.email@sokhunseng.com',
                ['some.email@sokhunseng.com'],
                fail_silently=False,
            )
            return http.HttpResponseRedirect('/')

    context = {
        'form': form
    }
    return TemplateResponse(request, 'contact_me.html', context)


def blog_index (request, blog_slug):
    blog = get_object_or_404(Blog, slug=blog_slug)
    posts = Post.objects.filter(blog=blog)
    context = {
      'blog': blog,
      'posts': posts,
    }
    return TemplateResponse(request, 'blog.html', context)

def blog_post (request, blog_slug, post_slug):
    context = {
        
       'post': get_object_or_404(Post, slug=post_slug, blog__slug=blog_slug)
    }
    return TemplateResponse(request, 'post.html', context)


