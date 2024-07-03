from django.urls import reverse

from rest_framework import status

from rest_framework.test import APITestCase
from rest_framework.test import APIClient

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            email="test@email.com", password="123", chat_id="255450278"
        )
        self.habit = Habit.objects.create(
            owner=self.user,
            activity="Test",
            place="Home",
            time="10:00",
            periodicity="DAILY",
            duration=120,
            is_pleasant=False,
        )
        self.client.force_authenticate(user=self.user)

    def test_send_tg_messages(self):
        pass
