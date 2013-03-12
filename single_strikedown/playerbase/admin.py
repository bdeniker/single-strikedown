from django.contrib import admin

import reversion
import models

class CharacterAdmin(reversion.VersionAdmin):
    pass

class XPAdmin(reversion.VersionAdmin):
    pass

admin.site.register(models.Character, CharacterAdmin)
admin.site.register(models.XP, XPAdmin)