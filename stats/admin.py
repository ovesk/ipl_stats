from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from stats.models import Match, Deliveries


class BaseAdmin(ImportExportModelAdmin):
    list_per_page = 50


@admin.register(Match)
class MatchAdmin(BaseAdmin):
    search_fields = ('id', 'date', 'team1', 'team2', 'city')
    list_display = ('date', 'team1', 'team2', 'city')


@admin.register(Deliveries)
class DeliveriesAdmin(BaseAdmin):
    search_fields = (
        'id', 'match__id', 'match__year',
        'batting_team', 'bowling_team', 'inning')
    list_display = ('match', 'batting_team', 'bowling_team', 'inning')
