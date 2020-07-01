from django.urls import path
from .import views


urlpatterns = [
   path('', views.home, name="HomePage"),
   path('about_page', views.about, name="about_page"),
   path('menu_page' , views.menu, name="menu_page"),
   path('blog_page', views.blog, name="blog_page" ),
   path('reservation/', views.reservation, name="reservation"),
   path('newsletter/', views.newsLetter, name="newsLetter")
]
