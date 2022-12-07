from django.urls import path
from Menu import views
from django.conf import settings

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('shop_category/', views.ShopCategoryView.as_view(), name='shop_category'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('login/', views.PagesView.as_view(), name='login'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('single_product/', views.SingleProduct.as_view(), name='single_product'),
    path('checkout/', views.Checkout.as_view(), name='checkout'),
    path('cart/', views.Cart.as_view(), name='cart'),
    path('confirmation/', views.Confirmation.as_view(), name='confirmation'),
    path('single_blog/', views.SingleBlog.as_view(), name='single_blog'),
    path('login/', views.Login.as_view(), name='login'),
    path('tracking/', views.Tracking.as_view(), name='tracking'),
    path('elements/', views.Elements.as_view(), name='elements'),
]