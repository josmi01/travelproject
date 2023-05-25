from . import views
from django.urls import path



urlpatterns = [
    path('',views.demo,name='demo'),

    # path('home/',views.home,name='home'),
    # path('about/',views.about,name='about'),
    # path('contact/',views.contact,name='contact'),
    # path('details/',views.details,name='details'),
    # path('thanks/',views.thanks,name='thanks'),

    # path('equ/',views.equations,name='equations')
]