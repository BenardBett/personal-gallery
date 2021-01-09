from django.urls import path 
from gallery.views import images,about,home,search_category

urlpatterns = [
    path('', home, name="home")
    path('about/', about, name="about"),
    path('images/',images),
    path('search_category/', search_category, name="search_category"),
]