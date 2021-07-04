from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

from stats import views


routerv1 = DefaultRouter()
routerv1.register('matchs', views.MatchList, basename='match')
routerv1.register('deliveries', views.DeliveriesList, basename='deliveries')
routerv1.register('top_winning_teams', views.TopWinningTeamList,
                  basename='top-winning-teams')
routerv1.register('top_tosses_winning_teams', views.TopTossesWinningTeamList,
                  basename='top-tosses-winning-teams')
routerv1.register('top_player_of_matchs', views.MaxPlayerOfMatchList,
                  basename='top-player-of-matchs')
routerv1.register('top_team_max_win_locations', views.MaxWinLocationList,
                  basename='top-team-max-win-locations')
routerv1.register('max_match_locations', views.MaxMatchLocationList,
                  basename='max-match-locations')
routerv1.register('toss_percent', views.TossPercentList,
                  basename='toss-percent')
routerv1.register('top_win_by_runs', views.TopWinByRunsList,
                  basename='top-win-by-runs')
routerv1.register('top_win_by_wickets', views.TopWinByWicketsList,
                  basename='top-win-by-wickets')
routerv1.register('top_win_by_wickets', views.TopWinByWicketsList,
                  basename='top-win-by-wickets')
routerv1.register('won_toss_and_match_count', views.WonMatchAndTossList,
                  basename='won-toss-and-match-count')
routerv1.register('most_runs_by_batsman', views.MostRunsByBatsmanList,
                  basename='most-runs-by-batsman')
routerv1.register('most_catches_by_fielder', views.MostCatchesByFielderList,
                  basename='most-catches-by-fielder')


urlpatterns = [
    path('v1/', include(routerv1.urls)),
    path('', views.IndexView.as_view())
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
