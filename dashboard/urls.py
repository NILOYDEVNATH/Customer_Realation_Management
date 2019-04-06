from django.urls import path
from .import views
from customer import views as customer_views
from sales import views as sale_views

urlpatterns = [
    path('',views.home,name="home"),
    path('login',views.dashboard_login,name="login"),
    path('logout',views.dashboard_logout,name="logout"),
    path('customer_details',customer_views.customer_details,name="customer_details"),
    path('customer_agent',customer_views.customer_agent,name="customer_agent"),
    path('sales',sale_views.sale,name="sales")
]
