from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Page
from .models import Post
from django.http import HttpResponse


def index(request):
    #html='<html><body><h4 style="color: green; front-size: 40px; font-style: italic;">PythonHelpUAguid</h4></body></html>'
    return render(request, 'MainPage/index.html')


def home(request):
    return render(request, 'MainPage/main.html')


def category(request):
    return render(request, 'MainPage/category.html')


def news(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'MainPage/news.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post)


def search(request):
    query = request.GET.get('q')
    if query:
        results = Page.objects.filter(title__icontains=query) | Page.objects.filter(content__icontains=query)
    else:
        results = Page.objects.all()
    return render(request, 'MainPage/search.html', {'results': results})


#def category1(request):
    #return render(request, 'MainPage/category1.html')


def category1(request):
    category1_pages = Page.objects.filter(category='cat1')
    context = {'category1_pages': category1_pages}
    return render(request, 'MainPage/category1.html', context)


def category2(request):
    category1_pages = Page.objects.filter(category='cat2')
    context = {'category1_pages': category1_pages}
    return render(request, 'MainPage/category2.html', context)


def category3(request):
    category1_pages = Page.objects.filter(category='cat3')
    context = {'category1_pages': category1_pages}
    return render(request, 'MainPage/category3.html', context)


def category4(request):
    category1_pages = Page.objects.filter(category='cat4')
    context = {'category1_pages': category1_pages}
    return render(request, 'MainPage/category4.html', context)


def category5(request):
    category1_pages = Page.objects.filter(category='cat5')
    context = {'category1_pages': category1_pages}
    return render(request, 'MainPage/category5.html', context)


def category6(request):
    category1_pages = Page.objects.filter(category='cat6')
    context = {'category1_pages': category1_pages}
    return render(request, 'MainPage/category6.html', context)


def category7(request):
    category1_pages = Page.objects.filter(category='cat7')
    context = {'category1_pages': category1_pages}
    return render(request, 'MainPage/category7.html', context)


def category8(request):
    category1_pages = Page.objects.filter(category='cat8')
    context = {'category1_pages': category1_pages}
    return render(request, 'MainPage/category8.html', context)


def category9(request):
    category1_pages = Page.objects.filter(category='cat9')
    context = {'category1_pages': category1_pages}
    return render(request, 'MainPage/category9.html', context)


