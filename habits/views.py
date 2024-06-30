from rest_framework import viewsets, generics

from habits.models import Reward, Habit
from habits.serializers import RewardSerializer, HabitSerializer


class RewardViewSet(viewsets.ModelViewSet):
    serializer_class = RewardSerializer
    queryset = Reward.objects.all()

    def perform_create(self, serializer):
        """
        Метод получения владельца курса
        :param serializer: на вход получаем сериализатор
        """
        reward = serializer.save()
        reward.owner = self.request.user
        reward.save()


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        """
        Метод получения владельца курса
        :param serializer: на вход получаем сериализатор
        """
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
