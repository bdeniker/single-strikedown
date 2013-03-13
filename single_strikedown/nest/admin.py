from django.contrib import admin

import reversion
import models

class NestCharacterAdmin(reversion.VersionAdmin):
    list_display = ('name', 'player', 'state')
    list_filter = ('player', 'state')
    search_fields = ('player__name', 'player__user__username',
                     'background', 'notes')

admin.site.register(models.NestCharacter, NestCharacterAdmin)
admin.site.register(models.Skill)
admin.site.register(models.Virtue)
admin.site.register(models.Flaw)
admin.site.register(models.PostMasterTweak)
admin.site.register(models.Item)