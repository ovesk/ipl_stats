from django.http import Http404
from django.db.models import Count, F, Sum
from django.views.generic import TemplateView
from rest_framework import viewsets

from stats.models import Match, Deliveries
from stats.serializers import *


class MatchList(viewsets.ReadOnlyModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class DeliveriesList(viewsets.ReadOnlyModelViewSet):
    queryset = Deliveries.objects.all()
    serializer_class = DeliveriesSerializer


class TopWinningTeamList(viewsets.ReadOnlyModelViewSet):
    queryset = Match.objects.all()
    serializer_class = TopWinningTeamSerializer

    def get_queryset(self):
        top = self.request.query_params.get('top', None)
        season = self.request.query_params.get('season', None)
        if top is None:
            top = 1
        if season is not None:
            sliced_queryset = self.queryset.filter(
                date__year=season).values('winner').annotate(
                wins=Count('winner')).order_by('-wins')[:int(top)]
            return sliced_queryset
        raise Http404


class TopTossesWinningTeamList(viewsets.ReadOnlyModelViewSet):
    queryset = Match.objects.all()
    serializer_class = TopTossesWinningTeamSerializer

    def get_queryset(self):
        top = self.request.query_params.get('top', None)
        season = self.request.query_params.get('season', None)
        if top is None:
            top = 1
        if season is not None:
            sliced_queryset = self.queryset.filter(
                date__year=season).values('toss_winner').annotate(
                wins=Count('toss_winner')).order_by('-wins')[:int(top)]
            return sliced_queryset
        raise Http404


class MaxPlayerOfMatchList(viewsets.ReadOnlyModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MaxPlayerOfMatchSerializer

    def get_queryset(self):
        top = self.request.query_params.get('top', None)
        season = self.request.query_params.get('season', None)
        if top is None:
            top = 1
        if season is not None:
            sliced_queryset = self.queryset.filter(
                date__year=season).values('player_of_match').annotate(
                wins=Count('player_of_match')).order_by(
                '-wins')[:int(top)]
            return sliced_queryset
        raise Http404


class MaxWinLocationList(viewsets.ReadOnlyModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MaxWinLocationSerializer

    def get_queryset(self):
        season = self.request.query_params.get('season', None)
        if season is not None:
            winner_name = None
            winner_name_qry = self.queryset.filter(
                date__year=season).values('winner').annotate(
                wins=Count('winner')).order_by('-wins')
            if winner_name_qry.exists():
                winner_name = winner_name_qry[0]['winner']
            sliced_queryset = self.queryset.filter(
                winner=winner_name, date__year=season).values(
                'city', 'winner').annotate(
                wins=Count('city')).order_by('-wins')[:1]
            return sliced_queryset
        raise Http404


class MaxMatchLocationList(viewsets.ReadOnlyModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MaxMatchLocationSerializer

    def get_queryset(self):
        season = self.request.query_params.get('season', None)
        top = self.request.query_params.get('top', None)
        if top is None:
            top = 1
        if season is not None:
            sliced_queryset = self.queryset.filter(
                date__year=season).values('city').annotate(
                count=Count('city')).order_by('-count')[:int(top)]
            return sliced_queryset
        raise Http404


class TossPercentList(viewsets.ReadOnlyModelViewSet):
    queryset = Match.objects.all()
    serializer_class = TossPercentSerializer

    def get_queryset(self):
        season = self.request.query_params.get('season', None)
        decision_param = self.request.query_params.get('decision', None)
        if season is not None and decision_param is not None:
            season_matches = self.queryset.filter(
                date__year=season)
            total_matches = season_matches.count()
            bat_field_count = season_matches.filter(
                toss_decision=decision_param).count()
            resp = [
                {'count': bat_field_count,
                 'total_match': total_matches,
                 'decision': decision_param}]
            return resp
        raise Http404


class TopWinByRunsList(viewsets.ReadOnlyModelViewSet):
    queryset = Match.objects.all()
    serializer_class = TopWinByRunsSerializer

    def get_queryset(self):
        season = self.request.query_params.get('season', None)
        top = self.request.query_params.get('top', None)
        if top is None:
            top = 1
        if season is not None:
            sliced_queryset = self.queryset.filter(
                date__year=season).values(
                'win_by_runs', 'winner').order_by(
                '-win_by_runs')[:int(top)]
            return sliced_queryset
        raise Http404


class TopWinByWicketsList(viewsets.ReadOnlyModelViewSet):
    queryset = Match.objects.all()
    serializer_class = TopWinByWicketsSerializer

    def get_queryset(self):
        season = self.request.query_params.get('season', None)
        top = self.request.query_params.get('top', None)
        if top is None:
            top = 1
        if season is not None:
            sliced_queryset = self.queryset.filter(
                date__year=season).values(
                'win_by_wickets', 'winner').order_by(
                '-win_by_wickets')[:int(top)]
            return sliced_queryset
        raise Http404


class WonMatchAndTossList(viewsets.ReadOnlyModelViewSet):
    queryset = Match.objects.all()
    serializer_class = WonTossAndMatchSerializer

    def get_queryset(self):
        season = self.request.query_params.get('season', None)
        if season is not None:
            season_qry = self.queryset.filter(
                date__year=season)
            total_matches = season_qry.count()
            toss_and_match = season_qry.filter(
                winner=F('toss_winner')).count()
            resp = [{
                'count': toss_and_match,
                'total_match': total_matches,
                'season': season}]
            return resp
        raise Http404


class MostRunsByBatsmanList(viewsets.ReadOnlyModelViewSet):
    queryset = Deliveries.objects.all()
    serializer_class = MostRunsByBatsmanSerializer

    def get_queryset(self):
        season = self.request.query_params.get('season', None)
        top = self.request.query_params.get('top', None)
        if top is None:
            top = 1
        if season is not None:
            sliced_queryset = self.queryset.filter(
                match__date__year=season).values(
                'batsman', 'match__date__year').annotate(
                runs=Sum('batsman_runs'),
                season=F('match__date__year')).order_by(
                '-runs')[:int(top)]
            return sliced_queryset
        raise Http404


class MostCatchesByFielderList(viewsets.ReadOnlyModelViewSet):
    queryset = Deliveries.objects.all()
    serializer_class = MostCatchesByFielderSerializer

    def get_queryset(self):
        season = self.request.query_params.get('season', None)
        top = self.request.query_params.get('top', None)
        if top is None:
            top = 1
        if season is not None:
            sliced_queryset = self.queryset.filter(
                match__date__year=season, dismissal_kind='caught').values(
                'fielder', 'match__date__year').annotate(
                catches=Count('fielder'),
                season=F('match__date__year')).order_by(
                '-catches')[:int(top)]
            return sliced_queryset
        raise Http404


class IndexView(TemplateView):
    template_name = "index.html"
