from django.db import models
from django.contrib.auth.models import User, Group
from model_utils.managers import InheritanceManager

class Player(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=200)
    friends = models.ManyToManyField(User, blank=True, null=True,
                                     related_name='friend_of')

    def __unicode__(self):
        if self.name == '':
            return self.user.username
        else:
            return self.name

class Group(models.Model):
    group = models.OneToOneField(Group, related_name='party')
    name = models.CharField(max_length=200)
    forum = models.URLField(blank=True) 
    moderators = models.ManyToManyField(User, related_name='moderating')
    characters = models.ManyToManyField('Character', related_name='parties',
                                        blank=True, null=True)

    def __unicode__(self):
        return self.name

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

    objects = InheritanceManager()

    def __unicode__(self):
        return self.name

class XP(models.Model):
    character = models.OneToOneField(Character)
    amount = models.IntegerField()  # New/total amount of XP (NOT difference)

    class Meta:
        verbose_name='XP'
        verbose_name_plural='XP'

    def __unicode__(self):
        return self.character