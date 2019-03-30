from django.contrib import admin

from .models import *

admin.site.register(Eleve)
admin.site.register(SemestreFiliere)
admin.site.register(Matiere)
admin.site.register(Enseignant)
admin.site.register(Salle)
admin.site.register(DispenserCours)
admin.site.register(CoursSemestreFiliere)
admin.site.register(Presence)
