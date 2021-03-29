from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Player(TimeStampedModel):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class MLBPlayerStats(TimeStampedModel):
    player = models.ForeignKey('Player', blank=True, null=True, on_delete=models.CASCADE)
    games_played = models.PositiveSmallIntegerField(max_length=30)
    at_bats = models.PositiveSmallIntegerField(blank=True, null=True)
    runs = models.PositiveSmallIntegerField(blank=True, null=True)
    hits = models.PositiveSmallIntegerField(blank=True, null=True)
    doubles = models.PositiveSmallIntegerField(blank=True, null=True)
    triples = models.PositiveSmallIntegerField(blank=True, null=True)
    home_runs = models.PositiveSmallIntegerField(blank=True, null=True)
    rbis = models.PositiveSmallIntegerField(blank=True, null=True)
    walks = models.PositiveSmallIntegerField(blank=True, null=True)
    strikeouts = models.PositiveSmallIntegerField(blank=True, null=True)
    stolen_bases = models.PositiveSmallIntegerField(blank=True, null=True)
    caught_stealing = models.PositiveSmallIntegerField(blank=True, null=True)
    batting_average = models.DecimalField(max_digits=3, decimal_places=3)
