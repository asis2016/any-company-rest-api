from django.test import TestCase

from .models import Testimonial


class TestimonialTest(TestCase):
    """
    The test case for Testimonial.
    """

    @classmethod
    def setUpTestData(cls):
        """ Creates initial data at the class level. """
        testimonial = Testimonial.objects.create(
            id='550e8400e29b41d4a716446655440000',
            client_name='Jane Austin',
            client_position='Author at Awesome',
            image_url='https://amaharjan.com/img1',
            testimonial='Great work!'
        )
        testimonial.save()

    def test_title(self):
        """ Test if title works. """
        data = Testimonial.objects.get(id='550e8400e29b41d4a716446655440000')
        expected_title = f'{data.client_name}'
        self.assertEqual(expected_title, 'Jane Austin')
