from django.db import models


class Match(models.Model):
    result_choices = (
        ('tie', 'Tie'),
        ('normal', 'Normal'),
        (None, 'No result'))
    city = models.CharField(max_length=25)
    date = models.DateField()
    team1 = models.CharField(max_length=50)
    team2 = models.CharField(max_length=50)
    toss_winner = models.CharField(max_length=50)
    toss_decision = models.CharField(max_length=10)
    result = models.CharField(
        max_length=10, choices=result_choices, default=None)
    dl_applied = models.BooleanField()
    winner = models.CharField(max_length=50)
    win_by_runs = models.SmallIntegerField(default=0)
    win_by_wickets = models.SmallIntegerField(default=0)
    player_of_match = models.CharField(max_length=50)
    venue = models.CharField(max_length=150, null=True)
    umpire1 = models.CharField(max_length=50, null=True, blank=True)
    umpire2 = models.CharField(max_length=50, null=True, blank=True)
    umpire3 = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return '%s: %s %s' % (self.date, self.team1, self.team2)


class Deliveries(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    inning = models.SmallIntegerField()
    batting_team = models.CharField(max_length=50)
    bowling_team = models.CharField(max_length=50)
    over = models.SmallIntegerField(default=0)
    ball = models.SmallIntegerField(default=0)
    batsman = models.CharField(max_length=50)
    non_striker = models.CharField(max_length=50)
    bowler = models.CharField(max_length=50)
    is_super_over = models.BooleanField(default=False)
    wide_runs = models.SmallIntegerField(default=0)
    bye_runs = models.SmallIntegerField(default=0)
    legbye_runs = models.SmallIntegerField(default=0)
    noball_runs = models.SmallIntegerField(default=0)
    penalty_runs = models.SmallIntegerField(default=0)
    batsman_runs = models.SmallIntegerField(default=0)
    extra_runs = models.SmallIntegerField(default=0)
    total_runs = models.SmallIntegerField(default=0)
    player_dismissed = models.CharField(max_length=50, null=True, blank=True)
    dismissal_kind = models.CharField(max_length=50, null=True, blank=True)
    fielder = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.match, self.inning)
