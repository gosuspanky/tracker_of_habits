from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Reward, Habit
from habits.paginations import CustomPagination
from habits.serializers import RewardSerializer, HabitSerializer

from users.permissions import IsOwner


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
    pagination_class = CustomPagination

    def get_queryset(self, *args, **kwargs):
        """
        Метод получения уроков с фильтрацией по владельцу
        """
        queryset = super().get_queryset()
        queryset = queryset.filter(is_public=True)
        return queryset


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (
        IsAuthenticated,
        IsOwner,
    )


class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = (
        IsAuthenticated,
        IsOwner,
    )
