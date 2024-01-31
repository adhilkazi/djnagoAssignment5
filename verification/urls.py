from.import views
from django.urls import path
urlpatterns=[
path('',views.insert,name="singnup"),#insert
path('views',views.views,name="views"),#views
path("delete/<str:pk>",views.delete,name='delete'),#delete
path('dview/<str:pk>',views.detials_view,name='dview'),#dviews
path('update/<str:pk>',views.update,name="update"),#update


#login

path('login/',views.login,name="login"),#login views
path('userloge/',views.userlog,name="userloge"),#userlogin
path('welcome/',views.welcome,name="welcome"), #welcom

#login page show
# path('loginclick/',views.loginclick,name="loginclick"),

]