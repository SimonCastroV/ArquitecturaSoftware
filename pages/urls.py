from django.urls import path 
from .views import homePageView, AboutPageView, ProductIndexView, ProductShowView,  ProductCreateView, TemplateView, CartView, CartRemoveAllView
  
urlpatterns = [ 
     path("", homePageView.as_view(), name='home'), 
     path('about/', AboutPageView.as_view(), name='about'),
     path('products/', ProductIndexView.as_view(), name='index'),
     path('products/<str:id>', ProductShowView.as_view(), name='show'),
     path('products/create/', ProductCreateView.as_view(), name='product-create'),
     path('products/created/', TemplateView.as_view(template_name='products/created.html'), name='product-created'),
     path('cart/', CartView.as_view(), name='cart_index'),
     path('cart/add/<str:product_id>', CartView.as_view(), name='cart_add'),
     path('cart/removeAll', CartRemoveAllView.as_view(), name='cart_removeAll'),

]