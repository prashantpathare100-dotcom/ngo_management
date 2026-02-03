# from django.contrib import admin
# from .models import Donation, Volunteer, Event
# from .models import (
#     ContactHero,
#     ContactInfo,
#     ContactMap,
#     ContactTeam,
#     ContactMessage
# )

# admin.site.register(Donation)
# admin.site.register(Volunteer)
# admin.site.register(Event)

# @admin.register(ContactHero)
# class ContactHeroAdmin(admin.ModelAdmin):
#     list_display = ('title', 'is_active')
#     list_editable = ('is_active',)
#     search_fields = ('title',)


# @admin.register(ContactInfo)
# class ContactInfoAdmin(admin.ModelAdmin):
#     list_display = ('email1', 'phone1')


# @admin.register(ContactMap)
# class ContactMapAdmin(admin.ModelAdmin):
#     list_display = ('id',)


# @admin.register(ContactTeam)
# class ContactTeamAdmin(admin.ModelAdmin):
#     list_display = ('name', 'designation', 'is_active')
#     list_editable = ('is_active',)


# @admin.register(ContactMessage)
# class ContactMessageAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'subject', 'created_at')