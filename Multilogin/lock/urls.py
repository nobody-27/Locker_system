from django.urls import path
from lock import views
urlpatterns = [
    path('login/',views.login_data,name="login"),
    path('',views.home,name="home"),
    path('logout/',views.logout_of_site,name="logout"),
    path('my_phontos/',views.my_phontos,name="my_phontos"),

    path('pin/',views.add_pin,name="pin")
    
]
