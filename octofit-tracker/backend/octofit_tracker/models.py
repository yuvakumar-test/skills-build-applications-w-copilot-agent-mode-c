
from djongo import models
from bson import ObjectId

class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    class Meta:
        db_table = 'teams'
    def __str__(self):
        return self.name

class User(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='members', db_column='team_id', to_field='_id')
    is_superhero = models.BooleanField(default=False)
    class Meta:
        db_table = 'users'
    def __str__(self):
        return self.name

class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities', db_column='user_id', to_field='_id')
    type = models.CharField(max_length=100)
    duration = models.PositiveIntegerField(help_text='Duration in minutes')
    calories = models.PositiveIntegerField(help_text='Calories burned', default=0)
    date = models.DateField(auto_now_add=True)
    class Meta:
        db_table = 'activities'
    def __str__(self):
        return f"{self.user.name} - {self.type}"

class Workout(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    duration = models.PositiveIntegerField(help_text='Duration in minutes', default=0)
    difficulty = models.CharField(max_length=50, blank=True)
    class Meta:
        db_table = 'workouts'
    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leaderboard_entries', db_column='user_id', to_field='_id')
    points = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    class Meta:
        db_table = 'leaderboard'
    def __str__(self):
        return f"{self.user.name} - {self.rank}"
