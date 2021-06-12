from django.test import TestCase

from .models import Brand


class BrandTest(TestCase):
    """
    The test case for Brand.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Creates initial data at the class level.
        """
        brand = Brand.objects.create(
            id='550e8400e29b41d4a716446655440000',
            title='Brand Instagram',
            image_url='intagram.com/insta.png'
        )
        brand.save()

    def test_title(self):
        """
        Test if title works.
        """
        brand = Brand.objects.get(id='550e8400e29b41d4a716446655440000')
        expected_title = f'{brand.title}'
        self.assertEqual(expected_title, 'Brand Instagram')

    def test_image_url(self):
        """
        Test if image_url works.
        """
        brand = Brand.objects.get(id='550e8400e29b41d4a716446655440000')
        expected_image_url = brand.image_url
        self.assertEqual(expected_image_url, 'intagram.com/insta.png')
