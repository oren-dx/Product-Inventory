from django.urls import path
from product_app.views import*

urlpatterns = [
    path('', register, name='register'),
    path('login-page', login_page, name='login_page'),
    path('logout-page/',logout_page,name='logout_page'),

    path('home-page/', home_view, name='home_view'),
    path('product-list/', product_list, name='product_list'),
    path('add-product/',add_product, name='add_product'),
    
    path('products/<int:id>/',product_detail,name='product_detail'),
    path('product_update/<str:p_id>/',product_update, name='product_update'),
    path('product_delete/<str:p_id>/',product_delete, name='product_delete'),
]
