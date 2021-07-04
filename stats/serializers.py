from rest_framework import serializers

from stats.models import Match, Deliveries


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'


class DeliveriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deliveries
        fields = '__all__'


class TopWinningTeamSerializer(serializers.Serializer):
    wins = serializers.IntegerField()
    winner = serializers.CharField()


class TopTossesWinningTeamSerializer(serializers.Serializer):
    wins = serializers.IntegerField()
    toss_winner = serializers.CharField()


class MaxPlayerOfMatchSerializer(serializers.Serializer):
    wins = serializers.IntegerField()
    player_of_match = serializers.CharField()


class MaxWinLocationSerializer(serializers.Serializer):
    wins = serializers.IntegerField()
    winner = serializers.CharField()
    city = serializers.CharField()


class MaxMatchLocationSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    city = serializers.CharField()


class TossPercentSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    total_match = serializers.IntegerField()
    decision = serializers.CharField()


class TopWinByRunsSerializer(serializers.Serializer):
    win_by_runs = serializers.IntegerField()
    winner = serializers.CharField()


class TopWinByWicketsSerializer(serializers.Serializer):
    win_by_wickets = serializers.IntegerField()
    winner = serializers.CharField()


class WonTossAndMatchSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    total_match = serializers.IntegerField()
    season = serializers.CharField()


class MostRunsByBatsmanSerializer(serializers.Serializer):
    runs = serializers.IntegerField()
    season = serializers.CharField()
    batsman = serializers.CharField()


class MostCatchesByFielderSerializer(serializers.Serializer):
    catches = serializers.IntegerField()
    season = serializers.CharField()
    fielder = serializers.CharField()
