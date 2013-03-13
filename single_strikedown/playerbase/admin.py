from django.contrib import admin

import reversion
import models

class CharacterAdmin(reversion.VersionAdmin):
    list_display = ('name', 'player', 'state')
    list_filter = ('player', 'state')
    search_fields = ('player__name', 'player__user__username',
                     'background', 'notes')

class XPAdmin(reversion.VersionAdmin):
    list_display = ('character', 'amount')
    list_filter = ('character',)

admin.site.register(models.Character, CharacterAdmin)
admin.site.register(models.XP, XPAdmin)

admin.site.register(models.Player)
admin.site.register(models.Group)