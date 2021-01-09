from django.urls import path 


urlpatterns = [
    path('', home, name="home")
    path('about/', about, name="about"),
    path('images/',images),
    path('search_category/', search_category, name="search_category"),
]