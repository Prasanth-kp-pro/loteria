
# Register your models here.
from django.contrib import admin
from .models import LotteryEntry

class LotteryEntryAdmin(admin.ModelAdmin):
    list_display = ('name', 'referral_code', 'mobile_number', 'winning_number')
    search_fields = ('name', 'referral_code', 'mobile_number', 'winning_number')

admin.site.register(LotteryEntry, LotteryEntryAdmin)
from django.contrib import admin
from .models import Participant

import pandas as pd
from django.contrib import admin
from django.http import HttpResponse
from .models import Participant

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'phonenumber', 'winnings')
    actions = ['import_participants']

    def import_participants(self, request, queryset):
        selected = queryset
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="participants.csv"'
        df = pd.DataFrame(selected.values())
        df.to_csv(response, index=False)
        return response

admin.site.register(Participant, ParticipantAdmin)
