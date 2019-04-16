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
    path('customeragent_view',customer_views.customeragent_view,name="customeragent_view"),
    path('customeragent_delete/<int:pk>',customer_views.customeragent_delete,name="customeragent_delete"),
    path('customeragent_edit/<int:pk>',customer_views.customeragent_edit,name="customeragent_edit"),
    path('sales',sale_views.sale,name="sales"),
    path('estimate',sale_views.estimate,name="estimate"),
    path('category',product_views.category,name="category"),
    path('category_status_changed/<int:pk>',product_views.category_status_changed,name="category_status_changed"),
    path('category_delete/<int:pk>',product_views.category_delete,name="category_delete"),
    path('category_edit/<int:pk>',product_views.category_edit,name="category_edit"),
    path('subcategory',product_views.subcategory,name="subcategory"),
    path('get_sub_category',product_views.get_sub_category,name="get_sub_category"),
    path('subcategory_delete/<int:pk>',product_views.subcategory_delete,name="subcategory_delete"),
    path('subcategory_status_changed/<int:pk>',product_views.subcategory_status_changed,name="subcategory_status_changed"),
    path('subcategory_edit/<int:pk>',product_views.subcategory_edit,name="subcategory_edit"),
    path('item',product_views.item,name="item"),
    path('item_delete/<int:pk>',product_views.item_delete,name="item_delete"),
    path('item_update/<int:pk>',product_views.item_update,name="item_update"),
    path('status',product_views.status,name="status"),
    path('expense',expense_contract_views.expense,name="expense"),
    path('contract',expense_contract_views.contract,name="contract")
]
