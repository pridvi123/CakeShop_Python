from django.urls import path
from views import views 
urlpatterns=[
    path('', views.user_login, name='user_login'),
    path('signup/',views.signup, name='signup'),
    path('dash/',views.dash ,name='dash'),
    path('list/',views.list ,name='list'),
    path('cakes/',views.cakes,name='cakes'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.cakeup,name='cakeup'),
    path('customeradd/',views.customeradd,name='customeradd'), 
    path('showviews/',views.showviews,name='showviews'),
    path('customerdelete/<int:id>/',views.customerdelete,name='customerdelete'),
    path('customerupdate/<int:id>/', views.customerupdate, name='customerupdate'),
    path('customer_order/',views.customer_order, name='customer_order'),
    path('orderfield/',views.orderfield, name='orderfield'),
    path('totalamount/',views.TotalAmount, name='TotalAmount'),
    path('delete_order/<int:id>/',views.delete_order, name='delete_order'),
    path('orderdetails/',views.orderdetails, name='orderdetails'),
    path('viewsorder/<int:pk>/', views.viewsorder, name='viewsorder'),
    path('customerviews/', views.customerviews, name='customerviews'),
    path('cutomerup/<int:id>/',views.cutomerup, name='cutomerup'),

]