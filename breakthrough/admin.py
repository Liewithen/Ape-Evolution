from django.contrib import admin
from breakthrough.models import *


class userAdmin(admin.ModelAdmin):
    list_display = ('p_id', 'p_name', 'p_alive', 'p_key', 'p_class', 'p_count', 'score1', 'score2', 'score3', 'sum_score',)


class dataAdmin(admin.ModelAdmin):
    list_display = ('q_class', 'q_id', 'answer', 'content', 'option1', 'option2', 'option3', 'option4',)

admin.site.register(Participant, userAdmin)
admin.site.register(DataBank1, dataAdmin)
admin.site.register(DataBank2, dataAdmin)
admin.site.register(DataBank3, dataAdmin)
