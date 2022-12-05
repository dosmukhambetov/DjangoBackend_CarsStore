from django.urls import path
from Menu import views
from django.conf import settings

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('shop_category/', views.ShopCategoryView.as_view(), name='shop_category'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('pages/', views.PagesView.as_view(), name='pages'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]