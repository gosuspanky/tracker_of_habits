from rest_framework import viewsets, generics

from habits.models import Reward
from habits.serializers import RewardSerializer, HabitSerializer


class RewardViewSet(viewsets.ModelViewSet):
    serializer_class = RewardSerializer
    queryset = Reward.objects.all()


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Reward.objects.all()


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Reward.objects.all()


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Reward.objects.all()


class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = Reward.objects.all()
