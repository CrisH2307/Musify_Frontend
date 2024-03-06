from django.views.generic import TemplateView
from supabase_py import create_client
from django.shortcuts import render

class HomePageView(TemplateView):
    template_name = "home.html"

    def fetch_supabase_data(self):
        supabase_url = 'https://ruoaxfttcbppnoyzvvur.supabase.co'
        supabase_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJ1b2F4ZnR0Y2JwcG5veXp2dnVyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDk2NzUxMzEsImV4cCI6MjAyNTI1MTEzMX0.PLg70dP9slrDuWLhEM5Z8fHiTtHkB_5j8XrddQ08oP8'
        return create_client(supabase_url, supabase_key)

    def get_data(self):
        supabase_client = self.fetch_supabase_data()
        data = supabase_client.table('artist').select("*").execute()
        return data.get('data', [])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = self.get_data()
        return context

def view_data(request):
    return HomePageView.as_view()(request)


class AboutPageView(TemplateView):
    template_name = "about.html"


class ArtistPageView(TemplateView):
    template_name = "artist.html"


class AlbumPageView(TemplateView):
    template_name = "album.html"

