from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


class ArtistPageView(TemplateView):
    template_name = "artist.html"

