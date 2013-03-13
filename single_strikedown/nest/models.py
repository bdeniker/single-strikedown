from django.db import models
from single_strikedown.playerbase.models import Character

class NestCharacter(Character):
    strength = models.IntegerField()
    endurance = models.IntegerField()
    aura = models.IntegerField()

    virtues = models.ManyToManyField('Virtue', blank=True, null=True,
                                     related_name='characters')
    flaws = models.ManyToManyField('Flaw', blank=True, null=True,
                                   related_name='characters')
    skills = models.ManyToManyField('Skill', through='HasSkill',
                                    blank=True, null=True)
    post_master_tweaks = models.ManyToManyField('PostMasterTweak',
                                                blank=True, null=True,
                                                related_name='characters')
    items = models.ManyToManyField('Item', blank=True, null=True,
                                   related_name='characters')


class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

class HasSkill(models.Model):
    PROFICIENT = 1
    EXPERT = 2
    MASTER = 4
    SKILL_LEVEL = (
        (PROFICIENT, 'Proficient'),
        (EXPERT, 'Expert'),
        (MASTER, 'Master'),
    )

    character = models.ForeignKey(NestCharacter)
    skill = models.ForeignKey(Skill, related_name='characters')
    level = models.IntegerField(choices=SKILL_LEVEL)

    def __unicode__(self):
        return (self.character + ': ' + self.skill)


class Quality(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    level = models.IntegerField()
    broadcast = models.BooleanField()

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name


class Virtue(Quality):
    @property
    def cost():
        return -self.level

class Flaw(Quality):
    @property
    def cost():
        return self.level

class PostMasterTweak(Quality):
    skill = models.ForeignKey(Skill, related_name='postmasters')

    @property
    def cost():
        return -self.level

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.name
