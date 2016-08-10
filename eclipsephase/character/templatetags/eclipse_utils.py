__author__ = 'michael'
from django.template.defaulttags import register
from eclipsephase.character import models

@register.filter(name='model_attr')
def model_attr(model, key):
    if hasattr(model, key):
        return getattr(model, key)
    else:
        return 'N/A'


@register.filter(name='dict_var_key')
def dict_var_key(dic, key):
    return dic.get(key, None)


@register.inclusion_tag('character/character.html')
def character_include(character):
    context = {}
    context['character'] = character
    context['aptitudes'] = models.APTITUDES
    context['secondaries'] = models.SECONDARY_APTITUDES
    char_skills = models.CharacterSkill.objects.filter(character=character).order_by('skill__name')
    context['skills'] = {}
    context['skills'][character.id] = char_skills
    return context