from django.test import TestCase
from django.urls import reverse
from .models import Artist, Album

class HomepageTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    def test_non_existent_url(self):
        response = self.client.get("/non_existent_url/")
        self.assertEqual(response.status_code, 404)



class ArtistpageTests(TestCase):
    def setUp(self):
        self.artist = Artist.objects.create(artistid=1, name="Test Artist")

    def test_url_exists_at_correct_location(self):
        response = self.client.get(f"/{self.artist.artistid}/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("artist", kwargs={"artistid": self.artist.artistid}))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("artist", kwargs={"artistid": self.artist.artistid}))
        self.assertTemplateUsed(response, "artist.html")

    def test_artist_detail_page(self):
        response = self.client.get(reverse("artist", kwargs={"artistid": self.artist.artistid}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.artist.name)
        # Add more assertions if you have additional details to display on the artist page



class AlbumpageTests(TestCase):
    def setUp(self):
        self.artist = Artist.objects.create(name="Test Artist")
        self.album = Album.objects.create(artistid=self.artist, albumtitle="Test Album")

    def test_url_exists_at_correct_location(self):
        response = self.client.get(f"/{self.artist.artistid}/{self.album.albumid}/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("album", kwargs={"artistid": self.artist.artistid, "albumid": self.album.albumid}))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("album", kwargs={"artistid": self.artist.artistid, "albumid": self.album.albumid}))
        self.assertTemplateUsed(response, "album.html")


class AboutpageTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")
