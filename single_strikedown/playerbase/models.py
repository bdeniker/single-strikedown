from django.db import models
from django.contrib.auth.models import User, Group

class Player(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=200)
    friends = models.ManyToManyField(User, blank=True, related_name='friend_of')

class Group(models.Model):
    group = models.OneToOneField(Group, related_name='party')
    name = models.CharField(max_length=200)
    forum = models.URLField(blank=True) 
    moderators = models.ManyToManyField(User, related_name='moderating')

class Character(models.Model):

    ACTIVE = 'act'
    INACTIVE = 'ina'
    RETIRED = 'ret'

    CHARACTER_STATES = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
        (RETIRED, 'Retired'),
    )

    player = models.ForeignKey(User, related_name='characters')
    name = models.CharField(max_length=200)
    background = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    state = models.CharField(max_length=3, choices=CHARACTER_STATES)

class XP(models.Model):
    character = models.ForeignKey(Character)
    timestamp = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=500, blank=True)