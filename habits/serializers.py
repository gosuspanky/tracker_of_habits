from rest_framework import serializers

from habits.models import Reward, Habit


class RewardSerializer(serializers.ModelSerializer):
    """
    Сериализатор для вознаграждения
    """

    class Meta:
        model = Reward
        fields = "__all__"


class HabitSerializer(serializers.ModelSerializer):
    """
    Сериализатор для привычки
    """

    class Meta:
        model = Habit
        fields = "__all__"
