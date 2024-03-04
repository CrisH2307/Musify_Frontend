from django.urls import path
from .views import HomePageView, AboutPageView, ArtistPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("artist/", ArtistPageView.as_view(), name="artist")
]