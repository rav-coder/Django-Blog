from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.contrib.auth.models import Group
from django.db.models import Sum

from django.contrib import admin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Emotion 
from .models import  Fitness, Entry, Person

UserAdmin.list_display = ('email', 'first_name', 'last_name')
UserAdmin.list_filter = []

admin.site.unregister(User)
admin.site.unregister(Group)

##################################

# admin.site.register(User, UserAdmin)

# # Register your models here.
# class EmotionAdmin(admin.ModelAdmin):
#     list_display = ['subtype', 'type']
#     list_filter = ['type']
#     search_fields = ['subtype']

#     def save_model(self, request, obj, form, change):
#         if obj.type not in ['mad', 'sad', 'scared', 'peaceful', 'powerful', 'joyful']:
#             messages.error(request, f'{obj.type} is not an allowed type of emotion.')
#             return HttpResponseRedirect(reverse('admin:diary_emotion_add'))
#         else:
#             super().save_model(request, obj, form, change)

# admin.site.register(Emotion, EmotionAdmin)

##################################

class PersonUser(admin.ModelAdmin):
    list_display = ['name', 'group_name']
    list_filter = ['group_name']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.order_by('name')
        return qs  

class FitnessUser(admin.ModelAdmin):
    
    verbose_name = "Fitness Totals"
    list_display = ['total_duration', 'total_calories_burned']
    list_per_page = 1

    def total_duration(self, obj):
        total_duration = Fitness.objects.aggregate(Sum('duration'))['duration__sum']
        return total_duration

    def total_calories_burned(self, obj):
        total_calories_burned = Fitness.objects.aggregate(Sum('calories_burned'))['calories_burned__sum']
        return total_calories_burned

    total_duration.short_description = 'Total duration'
    total_calories_burned.short_description = 'Total calories burned'

class EntryProxy(Entry):
    class Meta:
        proxy = True
        verbose_name = "Entry Date"

class EntryProxyUser(admin.ModelAdmin):
    list_display = ('hour', 'minute', 'text')
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.order_by('-dairy__date', '-hour', '-minute')
        return queryset

class EntryYogaUser(admin.ModelAdmin):
    list_display = ['hour', 'minute', 'text']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.filter(fitness__exercise_name='yoga').distinct()
        return qs
    
class EntryEmotionJoy(Entry):
    class Meta:
        proxy = True
        verbose_name = "Entry (Emotion)"

class EmotionTypeFilter(admin.SimpleListFilter):
    title = 'Emotion Type'
    parameter_name = 'etype'

    def lookups(self, request, model_admin):
        return Emotion.objects.values_list('type', 'type').distinct()

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(entryemotion__subtype__type=self.value()).distinct()

class EntryJoyUser(admin.ModelAdmin):
    list_display = ('hour', 'minute', 'text')
    list_filter = (EmotionTypeFilter,)

admin.site.register(Fitness, FitnessUser)
admin.site.register(EntryProxy, EntryProxyUser) 
admin.site.register(Entry, EntryYogaUser)
admin.site.register(EntryEmotionJoy, EntryJoyUser) 
admin.site.register(Person, PersonUser) 

