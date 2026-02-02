from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(team='Alpha')
        self.assertEqual(user.team, 'Alpha')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create()
        self.assertIsNotNone(team)

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user='test', activity_type='run')
        self.assertEqual(activity.activity_type, 'run')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(team='Alpha')
        self.assertEqual(leaderboard.team, 'Alpha')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create()
        self.assertIsNotNone(workout)
