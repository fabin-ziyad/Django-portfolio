from django.urls import path,include
from . import views
app_name='main'
urlpatterns = [
    path('',views.home_page,name="main_home" ),
    path('Portfolio/',views.Portfolio,name='portfolio'),
    path('Contact/',views.Contact,name='contact')
]