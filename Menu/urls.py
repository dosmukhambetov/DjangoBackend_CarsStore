from django.urls import path
from Menu import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('shop/', views.ShopCategoryView.as_view(), name='shop'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('pages/', views.PagesView.as_view(), name='pages'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]