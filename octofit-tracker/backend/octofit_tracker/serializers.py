from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout

class UserSerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField()
    team = serializers.PrimaryKeyRelatedField(read_only=True)
    def get__id(self, obj):
        return str(obj._id) if hasattr(obj, '_id') else None
    class Meta:
        model = User
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField()
    def get__id(self, obj):
        return str(obj._id) if hasattr(obj, '_id') else None
    class Meta:
        model = Team
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField()
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    def get__id(self, obj):
        return str(obj._id) if hasattr(obj, '_id') else None
    class Meta:
        model = Activity
        fields = '__all__'

class LeaderboardSerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField()
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    def get__id(self, obj):
        return str(obj._id) if hasattr(obj, '_id') else None
    class Meta:
        model = Leaderboard
        fields = '__all__'

class WorkoutSerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField()
    def get__id(self, obj):
        return str(obj._id) if hasattr(obj, '_id') else None
    class Meta:
        model = Workout
        fields = '__all__'
