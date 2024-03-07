from django.views.generic import TemplateView
from supabase_py import create_client
from django.shortcuts import render


def fetch_supabase_data(supabase_url, supabase_key):
    return create_client(supabase_url, supabase_key)


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_data(self):
        supabase_url = 'https://ruoaxfttcbppnoyzvvur.supabase.co'
        supabase_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJ1b2F4ZnR0Y2JwcG5veXp2dnVyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDk2NzUxMzEsImV4cCI6MjAyNTI1MTEzMX0.PLg70dP9slrDuWLhEM5Z8fHiTtHkB_5j8XrddQ08oP8'
        supabase_client = fetch_supabase_data(supabase_url, supabase_key)
        data = supabase_client.table('artist').select("*").execute()
        return data.get('data', [])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = self.get_data()
        return context

def view_data(request):
    return HomePageView.as_view()(request)


class ArtistPageView(TemplateView):
    template_name = "artist.html"
    
    def get_data(self, artist_id):
        supabase_url = 'https://ruoaxfttcbppnoyzvvur.supabase.co'
        supabase_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJ1b2F4ZnR0Y2JwcG5veXp2dnVyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDk2NzUxMzEsImV4cCI6MjAyNTI1MTEzMX0.PLg70dP9slrDuWLhEM5Z8fHiTtHkB_5j8XrddQ08oP8'
        supabase_client = fetch_supabase_data(supabase_url, supabase_key)

        # Fetch artist data
        artist_response = supabase_client.table('artist').select("*").execute()
        if artist_response.get('error'):
            print(f"Error fetching artist data: {artist_response['error']}")
            return {}

        artists = {}
        artist_data = artist_response.get('data', [])
        for artist in artist_data:
            if 'artistid' in artist:
                artists[artist['artistid']] = artist

        # Fetch album data
        album_response = supabase_client.table('album').select("*").execute()
        if album_response.get('error'):
            print(f"Error fetching album data: {album_response['error']}")
            # Provide an empty list as a default value for artist_albums
            artist_albums = []
        else:
            albums = album_response.get('data', [])

            # Filter albums associated with the artist
            artist_albums = [album for album in albums if album.get('artistid') == artist_id]

        # Calculate album count
        album_count = len(artist_albums)

        return {
            'artist': artists.get(artist_id, {}),
            'albums': artist_albums,
            'album_count': album_count
        }

    def get_context_data(self, **kwargs):
        album_id = self.kwargs.get('artistid')
        context = super().get_context_data(**kwargs)
        context['data'] = self.get_data(album_id)
        context['album_count'] = context['data'].get('album_count', 0)
        return context



class AlbumPageView(TemplateView):
    template_name = "album.html"

    def get_artist_name(self, artist_id):
        supabase_url = 'https://ruoaxfttcbppnoyzvvur.supabase.co'
        supabase_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJ1b2F4ZnR0Y2JwcG5veXp2dnVyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDk2NzUxMzEsImV4cCI6MjAyNTI1MTEzMX0.PLg70dP9slrDuWLhEM5Z8fHiTtHkB_5j8XrddQ08oP8'
        supabase_client = fetch_supabase_data(supabase_url, supabase_key)

        # Fetch artist data
        artist_response = supabase_client.table('artist').select("*").execute()
        if artist_response.get('error'):
            print(f"Error fetching artist data: {artist_response['error']}")
            return None

        artists = {}
        artist_data = artist_response.get('data', [])
        for artist in artist_data:
            if 'artistid' in artist:
                artists[artist['artistid']] = artist

        # Get artist name based on artist_id
        artist_name = artists.get(artist_id, {}).get('name', None)
        return artist_name

    def get_data(self, album_id):
        supabase_url = 'https://ruoaxfttcbppnoyzvvur.supabase.co'
        supabase_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJ1b2F4ZnR0Y2JwcG5veXp2dnVyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDk2NzUxMzEsImV4cCI6MjAyNTI1MTEzMX0.PLg70dP9slrDuWLhEM5Z8fHiTtHkB_5j8XrddQ08oP8'
        supabase_client = fetch_supabase_data(supabase_url, supabase_key)

        # Fetch artist data
        album_response = supabase_client.table('album').select("*").execute()
        if album_response.get('error'):
            print(f"Error fetching artist data: {album_response['error']}")
            return {}

        albums = {}
        album_data = album_response.get('data', [])
        for album in album_data:
            if 'albumid' in album:
                albums[album['albumid']] = album

        # Fetch album data
        songs_response = supabase_client.table('song').select("*").execute()
        if songs_response.get('error'):
            print(f"Error fetching album data: {songs_response['error']}")
            # Provide an empty list as a default value for artist_albums
            album_songs = []
        else:
            songs = songs_response.get('data', [])

            # Filter albums associated with the artist
            album_songs = [song for song in songs if song.get('albumid') == album_id]

        # Calculate album count
        song_count = len(album_songs)

        # Fetch artist name based on album's artistid
        artist_id = albums.get(album_id, {}).get('artistid', None)
        artist_name = self.get_artist_name(artist_id)

        return {
            'album': albums.get(album_id, {}),
            'songs': album_songs,
            'song_count': song_count,
            'artist_name': artist_name,
        }

    def get_context_data(self, **kwargs):
        album_id = self.kwargs.get('albumid')
        context = super().get_context_data(**kwargs)
        context['data'] = self.get_data(album_id)
        context['song_count'] = context['data'].get('song_count', 0)
        return context


class AboutPageView(TemplateView):
    template_name = "about.html"
