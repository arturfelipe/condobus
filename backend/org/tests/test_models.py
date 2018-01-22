from django.test import TestCase

from ..models import Organization


class OrganizationModelTest(TestCase):

    def setUp(self):
        self.org = Organization.objects.create(
            name='Some Org',
            logo='/media/logos/some-org-logo.jpg',
            description='We are a familiar condominium',
            rules='Please check our conduct code page at https://some-url.foo'
        )

    def test_str(self):
        self.assertEqual('Some Org', str(self.org))

    def test_can_create(self):
        self.assertTrue(Organization.objects.exists())
