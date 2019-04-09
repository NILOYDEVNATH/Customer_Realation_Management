from django.urls import path
from .import views
from customer import views as customer_views
from sales import views as sale_views
from products import views as product_views
from expense_contract import views as expense_contract_views

urlpatterns = [
    path('',views.home,name="home"),
    path('login',views.dashboard_login,name="login"),
    path('logout',views.dashboard_logout,name="logout"),
    path('customer_details',customer_views.customer_details,name="customer_details"),
    path('customer_agent',customer_views.customer_agent,name="customer_agent"),
    path('sales',sale_views.sale,name="sales"),
    path('estimate',sale_views.estimate,name="estimate"),
    path('category',product_views.category,name="category"),
    path('subcategory',product_views.subcategory,name="subcategory"),
    path('item',product_views.item,name="item"),
    path('status',product_views.status,name="status"),
    path('expense',expense_contract_views.expense,name="expense"),
    path('contract',expense_contract_views.contract,name="contract")
]
