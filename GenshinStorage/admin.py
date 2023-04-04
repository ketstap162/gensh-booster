from django.contrib import admin

from GenshinStorage.models import Character, Post, Skill, SkillData


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Character)
class AdminCharacter(admin.ModelAdmin):
    pass


@admin.register(Skill)
class AdminSkill(admin.ModelAdmin):
    pass


@admin.register(SkillData)
class SkillDataAdmin(admin.ModelAdmin):
    pass
