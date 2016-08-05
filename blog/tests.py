from django.test import TestCase
from .models import Post
# Create your tests here.

class PostTests(TestCase):
    def test_str(self):
        test_title = Post(title='My latest blog post')
        self.assertEquals(
                str(test_title),
                'My latest blog post')
