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
        'segment': 'login'
    }

    def get(self, request):
        return render(request, 'site/login/login.html')


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


class SingleProduct(View):
    context = {
        'segment': 'single_product'
    }

    def get(self, request):
        return render(request, 'site/single_product/single_product.html')


class Checkout(View):
    context = {
        'segment': 'checkout'
    }

    def get(self, request):
        return render(request, 'site/checkout/checkout.html')


class Cart(View):
    context = {
        'segment': 'cart'
    }

    def get(self, request):
        return render(request, 'site/cart/cart.html')


class Confirmation(View):
    context = {
        'segment': 'confirmation'
    }

    def get(self, request):
        return render(request, 'site/confirmation/confirmation.html')


class SingleBlog(View):
    context = {
        'segment': 'single_blog'
    }

    def get(self, request):
        return render(request, 'site/single_blog/single_blog.html')


class Login(View):
    context = {
        'segment': 'login'
    }

    def get(self, request):
        return render(request, 'site/login/login.html')


class Tracking(View):
    context = {
        'segment': 'tracking'
    }

    def get(self, request):
        return render(request, 'site/tracking/tracking.html')


class Elements(View):
    context = {
        'segment': 'elements'
    }

    def get(self, request):
        return render(request, 'site/elements/elements.html')