from django.shortcuts import render, Http404, HttpResponseRedirect
import models


def character_sheet(request, character_id):
    context = {}
    try:
        character = models.Character.objects.get(id=character_id)
        context['character'] = character
        context['aptitudes'] = models.APTITUDES
        context['secondaries'] = models.SECONDARY_APTITUDES
        # char_skills = models.CharacterSkill.objects.filter(character=character).order_by('skill__name')
        # context['skills'] = {}
        # context['skills'][character.id] = char_skills
        return render(request, 'character/sheet.html', context=context)
    except models.Character.DoesNotExist, dne:
        return Http404


def reset_character(request, character_id):
    context = {}
    try:
        character = models.Character.objects.get(id=character_id)
        character.generate_skill_bases()
        context['character'] = character
        context['aptitudes'] = models.APTITUDES
        context['secondaries'] = models.SECONDARY_APTITUDES
        # char_skills = models.CharacterSkill.objects.filter(character=character).order_by('skill__name')
        # context['skills'] = {}
        # context['skills'][character.id] = char_skills
        return render(request, 'character/sheet.html', context=context)
    except models.Character.DoesNotExist, dne:
        return Http404

def party(request, party_id):
    context = {}
    try:
        party = models.Party.objects.get(id=party_id)
        context['aptitudes'] = models.APTITUDES
        context['secondaries'] = models.SECONDARY_APTITUDES
        context['members'] = []
        context['skills'] = {}
        for character in party.members.all():
            context['members'].append(character)
            # char_skills = models.CharacterSkill.objects.filter(character=character).order_by('skill__name')
            # context['skills'][character.id] = char_skills
        return render(request, 'character/party.html', context=context)
    except models.Character.DoesNotExist, dne:
        return Http404