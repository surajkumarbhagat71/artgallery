from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path('public_product/',views.p_product,name="p_product"),

    ######################################### Oner #############################################
    path('oner/login',views.login, name="oner_login"),
    path('oner/dashabord/',views.oner_dashabord,name="oner_dashabord"),
    path('oner/profile',views.oner_profile,name="profile"),
    path('oner/all_order',views.all_order,name="all_order"),
    path('oner/all_painting',views.all_painting,name="all_painting"),
    path('oner/add_panting',views.add_panting,name="add_panting"),
    path('oner_logout/',views.oner_logout,name="oner_logout"),
    path('oner/about',views.about,name="about"),
    path('oner/edit_product/<int:pro_id>', views.edit, name="edit_panting"),
    path('delete_product/<int:id>',views.delete_product,name="delete_product"),


    ############################  user ##################################################

    path('user/my_order',views.my_order,name="my_order"),
    path('user/profile',views.profile,name="user_profile"),
    path('user/signup',views.signup,name="signup"),
    path('user/edit_profile/<int:id>',views.edit_profile,name="edit_profile"),
    path('user/ulogin',views.ulogin,name="user_login"),
    path('user/product',views.product,name="product"),
    path('order/<int:id>/',views.order,name="order"),
    path('delete_order/<int:id>',views.delete_order,name="delete_order"),
    path('logout',views.logout,name="logout")

]