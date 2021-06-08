from django.test import TestCase

from .models import Gallery


class GalleryTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """ Initial data creation at the class level. """
        Gallery.objects.create(
            id='550e8400e29b41d4a716446655440000',
            title='first image',
            image_url='http://goo.gl/img',
            caption='first image'
        )

    def test_title(self):
        """ Test if title works. """
        image = Gallery.objects.get(id='550e8400e29b41d4a716446655440000')
        expected_object_name = f'{image.title}'
        self.assertEquals(expected_object_name, 'first image')

    def test_image_url(self):
        """ Test if image_url works. """
        image = Gallery.objects.get(id='550e8400e29b41d4a716446655440000')
        expected_object_name = f'{image.image_url}'
        self.assertEquals(expected_object_name, 'http://goo.gl/img')
