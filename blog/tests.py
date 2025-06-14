```python
  from django.test import TestCase
  from .models import Post

  class PostModelTest(TestCase):
      def setUp(self):
          Post.objects.create(title="Test Post", content="This is a test post", category="Test")

      def test_post_str(self):
          post = Post.objects.get(title="Test Post")
          self.assertEqual(str(post), "Test Post")
  ```