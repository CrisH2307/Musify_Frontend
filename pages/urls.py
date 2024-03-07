from django.urls import path
from .views import HomePageView, AboutPageView, ArtistPageView, AlbumPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("<int:artistid>/", ArtistPageView.as_view(), name="artist"),
    path("<int:artistid>/<int:albumid>/", AlbumPageView.as_view(), name="album")
]