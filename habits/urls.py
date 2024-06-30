from django.urls import path

from rest_framework.routers import DefaultRouter

from habits.apps import HabitsConfig
from habits.views import (
    RewardViewSet,
    HabitCreateAPIView,
    HabitListAPIView,
    HabitRetrieveAPIView,
    HabitUpdateAPIView,
    HabitDestroyAPIView,
)

app_name = HabitsConfig.name

router = DefaultRouter()
router.register(r"rewards", RewardViewSet, basename="reward")

urlpatterns = [
    path("habits/create/", HabitCreateAPIView.as_view(), name="habit_create"),
    path("habits/", HabitListAPIView.as_view(), name="habit_list"),
    path(
        "habits/<int:pk>/",
        HabitRetrieveAPIView.as_view(),
        name="habit_retrieve",
    ),
    path("habits/update/<int:pk>/", HabitUpdateAPIView.as_view(), name="habit_update"),
    path("habits/delete/<int:pk>/", HabitDestroyAPIView.as_view(), name="habit_delete"),
] + router.urls
