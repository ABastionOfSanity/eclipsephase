from __future__ import unicode_literals

from django.db import models

# Create your models here.


STAT_VALUES = (0, 5, 10, 15, 20, 25,
               30, 35, 40, 45, 50, 55,
               60, 65, 70, 75, 80, 85,
               90, 95, 100)

APTITUDES = [('MOXIE', 'Moxie'), ('COG', 'Cognition'), ('COO', 'Coordination'),
             ('INT', 'Intuition'), ('REF', 'Reflexes'), ('SAV', 'Savvy'),
             ('SOM', 'Somatics'), ('WIL', 'Willpower')]

ACTIVE_SKILLS = [('Animal Handling', 'SAV'), ('Beam Weapon', 'COO'),
                 ('Blades', 'SOM'), ('Climbing', 'SOM'), ('Clubs', 'SOM'),
                 ('Control', 'WIL'), ('Deception', 'SAV'), ('Demolition', 'COG'),
                 ('Disguise', 'INT'), ('Exotic Melee', 'SOM'), ('Exotic Ranged', 'SOM'),
                 ('Flight', 'SOM'), ('Fray', 'REF'), ('Free Fall', 'REF'), ('Freerunning', 'SOM'),
                 ('Gunnery', 'INT'), ('Hardware', 'COG'), ('Impersonation', 'SAV'),
                 ('Infiltration', 'COO'), ('Infosec', 'COG'), ('Interfacing', 'COG'),
                 ('Intimidation', 'SAV'), ('Investigation', 'INT'), ('Kinesics', 'SAV'),
                 ('Kinetic Weapons', 'COO'), ('Medicine', 'COG'), ('Navigation', 'INT'),
                 ('Networking', 'SAV'), ('Palming', 'COO'), ('Perception', 'INT'), ('Persuasion', 'SAV'),
                 ('Pilot', 'REF'), ('Programming', 'COG'), ('Protocol', 'SAV'),
                 ('Psi Assault', 'WIL'), ('Psychosurgery', 'INT'), ('Research', 'COG'),
                 ('Scrounging', 'INT'), ('Spray Weapons', 'COO'), ('Swimming', 'SOM'),
                 ('Throwing Weapons', 'COO'), ('Unarmed Combat', 'SOM')
          ]

KNOWLEDGE_SKILLS = [('Academics', 'COG'), ('Art', 'INT'), ('Interest', 'COG'),
                    ('Language', 'INT'), ('Profession', 'COG')]


class MorphModel(models.Model):
    name = models.CharField(max_length=256, default='')
    description = models.TextField()
    COG = models.IntegerField(null=False, default=0)
    COO = models.IntegerField(null=False, default=0)
    INT = models.IntegerField(null=False, default=0)
    REF = models.IntegerField(null=False, default=0)
    SAV = models.IntegerField(null=False, default=0)
    SOM = models.IntegerField(null=False, default=0)
    WIL = models.IntegerField(null=False, default=0)

    DUR = models.IntegerField(null=False, default=0)
    WT = models.IntegerField(null=False, default=0)
    DR = models.IntegerField(null=False, default=0)
    DB = models.IntegerField(null=False, default=0)
    SPD = models.IntegerField(null=False, default=0)
    apt_max = models.IntegerField(null=False, default=0)
    advantages = models.TextField(default='')
    disadvantages = models.TextField(default='')
    implants = models.TextField(default='')

    def __str__(self):
        return self.name


class Morph(models.Model):
    model = models.ForeignKey(MorphModel, null=False)
    effects = models.TextField(null=True, default='', blank=True)

    def __str__(self):
        return self.model.name + ' ' + str(self.model.id)


class Ego(models.Model):
    name = models.CharField(max_length=256, default='')
    COG = models.IntegerField('Cognition', null=False, default=0)
    COO = models.IntegerField('Coordination', null=False, default=0)
    INT = models.IntegerField('Intuition', null=False, default=0)
    REF = models.IntegerField('Reflexes', null=False, default=0)
    SAV = models.IntegerField('Savvy', null=False, default=0)
    SOM = models.IntegerField('Somatics', null=False, default=0)
    WIL = models.IntegerField('Willpower', null=False, default=0)

    MOXIE = models.IntegerField('Moxie', null=False, default=0)
    INIT = models.IntegerField('Initiative', null=False, default=0)
    LUC = models.IntegerField('Lucidity', null=False, default=0)
    TT = models.IntegerField('Trauma Threshold', null=False, default=0)
    IR = models.IntegerField('Insanity Rating', null=False, default=0)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=256, default='')
    description = models.TextField()
    linked = models.CharField(max_length=10, choices=APTITUDES)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class PsiSleight(models.Model):
    name = models.CharField(max_length=256, default='')
    description = models.TextField()

    def __str__(self):
        return self.name


class Background(models.Model):
    name = models.CharField(max_length=256, default='')
    description = models.TextField()
    advantages = models.TextField()
    disadvantages = models.TextField()

    def __str__(self):
        return self.name


class Faction(models.Model):
    name = models.CharField(max_length=256, default='')
    description = models.TextField()
    advantages = models.TextField()
    disadvantages = models.TextField()

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=256, default='')
    ego = models.ForeignKey(Ego)
    morph = models.ForeignKey(Morph)
    background = models.ForeignKey(Background)
    faction = models.ForeignKey(Faction)

    def generate_skill_bases(self):
        for (active_skill, linked) in ACTIVE_SKILLS:
            skill = Skill.objects.get(name=active_skill, active=True)
            char_skill = CharacterSkill.objects.create(skill=skill, character=self)
            char_skill.save()

        for (knowledge_skill, linked) in KNOWLEDGE_SKILLS:
            skill = Skill.objects.get(name=knowledge_skill, active=False)
            char_skill = CharacterSkill.objects.create(skill=skill, character=self)
            char_skill.save()

    def resleeve(self):
        pass

    def __str__(self):
        return self.name


class CharacterSkill(models.Model):
    skill = models.ForeignKey(Skill, null=False)
    specialization = models.CharField(max_length=64)
    points = models.IntegerField(default=0)
    character = models.ForeignKey(Character, default=None)

    def __str__(self):
        return self.character.name + ' ' + self.skill.name + ': ' + self.specialization


