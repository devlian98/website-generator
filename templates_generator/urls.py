from django.urls import path
from . import views
from .views import UserCreate

#from templates_generator.views import generate_text


urlpatterns = [
    #path('', views.newHome, name='newHome'),
    path('', views.home, name='home'),
    path('signup/', UserCreate.as_view(), name='signup'),

    path('generate/restaurant_template/index.html', views.index_view, name='index'),
    path('generate/restaurant_template/menu.html', views.menu_view, name='menu'),
    path('generate/restaurant_template/about.html', views.about_view, name='about'),
    path('generate/restaurant_template/book.html', views.book_view, name='book'),

    path('generate/', views.generate_template, name='generate_template'),
    #path('generate-text/',views.generate_text, name='generate_text'),
    #path('generate-text/', generate_text, name='generate_text'),
]


