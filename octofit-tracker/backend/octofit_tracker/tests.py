from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        self.assertEqual(user.name, 'Test User')
        self.assertEqual(user.team.name, 'Test Team')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Marvel')
        self.assertEqual(team.name, 'Marvel')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        team = Team.objects.create(name='DC')
        user = User.objects.create(name='Batman', email='batman@dc.com', team=team)
        activity = Activity.objects.create(user=user, type='Running', duration=30, date='2023-01-01')
        self.assertEqual(activity.type, 'Running')
        self.assertEqual(activity.user.name, 'Batman')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', description='Upper body', difficulty='Easy')
        self.assertEqual(workout.name, 'Pushups')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Avengers')
        user = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=team)
        leaderboard = Leaderboard.objects.create(user=user, score=100, rank=1)
        self.assertEqual(leaderboard.rank, 1)
        self.assertEqual(leaderboard.user.name, 'Iron Man')
