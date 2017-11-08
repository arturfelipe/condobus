from django.test import TestCase

from org.models import Organization
from ..models import Bus


class BusModelTest(TestCase):

    def setUp(self):
        self.org = Organization.objects.create(
            name='Some Org',
            logo='/media/logos/some-org-logo.jpg',
            description='We are a familiar condominium',
            rules='Please check our conduct code page at https://some-url.foo'
        )
        self.bus = Bus.objects.create(
            name='Bus 1',
            organization=self.org
        )

    def test_str(self):
        self.assertEqual('Bus 1', str(self.bus))

    def test_can_create(self):
        self.assertTrue(Bus.objects.exists())
