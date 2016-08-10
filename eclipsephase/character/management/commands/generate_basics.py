__author__ = 'michael'
import codecs
from django.core.management.base import BaseCommand, CommandError
from eclipsephase.character.models import *


class Command(BaseCommand):
    help = 'Reset and generate basic skills and abilities'

    def handle(self, *args, **options):
        try:
            CharacterSkill.objects.all().delete()
            Skill.objects.all().delete()

            for (skill, linked) in ACTIVE_SKILLS:
                Skill.objects.create(name=skill, active=True, linked=linked)

            for (skill, linked) in KNOWLEDGE_SKILLS:
                Skill.objects.create(name=skill, active=False, linked=linked)

        except Exception, ex:
            raise CommandError(ex)
