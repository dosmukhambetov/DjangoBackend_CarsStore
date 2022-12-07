from django.shortcuts import render
from django.views.generic.base import View
from Menu.models import ClientContact


# Create your views here.
class HomeView(View):
    """Home Page"""
    context = {
        'segment': 'home'
    }

    def get(self, request):
        return render(request, 'site/home/index.html')


class ShopCategoryView(View):
    """Shop Page"""
    context = {
        'segment': 'shop_category'
    }

    def get(self, request):
        return render(request, 'site/shop_category/shopcategory.html')


class BlogView(View):
    """Blog Page"""
    context = {
        'segment': 'blog'
    }

    def get(self, request):
        return render(request, 'site/blog/blog.html')


class PagesView(View):
    """Pages Page"""
    context = {
        'segment': 'pages'
    }

    def get(self, request):
        return render(request, 'site/pages/pages.html')


class ContactView(View):
    """Contact Page"""
    context = {
        'segment': 'contact'
    }

    def get(self, request):
        return render(request, 'site/contact/contact.html')

    def post(self, request):
        email = request.POST['email']
        name = request.POST['name']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = ClientContact(email=email, name=name, subject=subject, message=message)
        contact.save()

        return render(request, 'site/contact/contact.html')