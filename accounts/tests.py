from django.test import TestCase
from django.contrib.auth.models import User


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username='longdao', password='secret12347', email='long.daohai4894@gmail.com')
        User.objects.create(username='giangnguyen', password='secret12347', email='giangnguyen347@gmail.com')

    def test_user(self):
        long = User.objects.get(username='longdao')
        kq = self.assertEqual(long.email, 'long.daohai4894@gmail.com')
