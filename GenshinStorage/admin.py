from django import forms
from django.contrib import admin
from django.utils.html import format_html
from GenshinStorage.models import Character, Post, Skill, SkillData, Element, Weapon, Location


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = '__all__'
        widgets = {
            'big_image': forms.FileInput(attrs={'required': False}),
            'small_image': forms.FileInput(attrs={'required': False}),
        }


class CharacterAdmin(admin.ModelAdmin):
    form = CharacterForm
    list_display = ('full_name', 'title',  'element',  'display_image')  # 'location', 'weapon',

    def display_image(self, obj):
        if obj.big_image:
            return format_html('<img src="{}" width="50"/>'.format(obj.big_image.url))
        else:
            return '-'

    display_image.short_description = 'Image'


admin.site.register(Character, CharacterAdmin)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Skill)
class AdminSkill(admin.ModelAdmin):
    pass


@admin.register(SkillData)
class SkillDataAdmin(admin.ModelAdmin):
    pass


@admin.register(Element)
class SkillDataAdmin(admin.ModelAdmin):
    pass


@admin.register(Weapon)
class SkillDataAdmin(admin.ModelAdmin):
    pass


@admin.register(Location)
class SkillDataAdmin(admin.ModelAdmin):
    pass
