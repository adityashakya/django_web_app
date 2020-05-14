from django.shortcuts import render
from .models import Post


# posts = [
#     {
#         'author': 'Aditya Shakya',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'April 30 2020'
#     },
# {
#         'author': 'John Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'May 1 2020'
#     }
#
# ]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
# Create your views here.
