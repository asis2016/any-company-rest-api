from django.test import TestCase

from .models import Project


class ProjectTest(TestCase):
    """
    The test case for project.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Creates initial project data at the class level.
        """
        project = Project.objects.create(
            id='550e8400e29b41d4a716446655440000',
            title='abc',
            description='description...',
            content='content...',
            image_url='a.png'
        )
        project.save()

    def test_title(self):
        """
        Test if title works.
        """
        project = Project.objects.get(id='550e8400e29b41d4a716446655440000')
        expected_title = f'{project.title}'
        self.assertEqual(expected_title, 'abc')
