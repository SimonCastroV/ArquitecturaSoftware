from django.urls import path 
from .views import homePageView, AboutPageView, ProductIndexView, ProductShowView,  ProductCreateView, TemplateView
  
urlpatterns = [ 
     path("", homePageView.as_view(), name='home'), 
     path('about/', AboutPageView.as_view(), name='about'),
     path('products/', ProductIndexView.as_view(), name='index'),
     path('products/<str:id>', ProductShowView.as_view(), name='show'),
     path('products/create/', ProductCreateView.as_view(), name='product-create'),
     path('products/created/', TemplateView.as_view(template_name='products/created.html'), name='product-created'),
]