from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # create user
        testuser = User.objects.create_user(
            username='testuser',
            password='abc123'
        )
        testuser.save()

        # create a blog post
        testpost = Post.objects.create(
            author=testuser,
            title='Blog title',
            body='Blog content...'
        )
        testpost.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)

        self.assertEqual(f'{post.title}', 'Blog title')
        self.assertEqual(f'{post.body}', 'Blog content...')
        self.assertEqual(f'{post.author}', 'testuser')