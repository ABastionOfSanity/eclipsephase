from __future__ import unicode_literals

from django.db import models

# Create your models here.


STAT_VALUES = (0, 5, 10, 15, 20, 25,
               30, 35, 40, 45, 50, 55,
               60, 65, 70, 75, 80, 85,
               90, 95, 100)

APTITUDES = [('COG', 'Cognition'), ('COO', 'Coordination'),
             ('INT', 'Intuition'), ('REF', 'Reflexes'), ('SAV', 'Savvy'),
             ('SOM', 'Somatics'), ('WIL', 'Willpower')]

SECONDARY_APTITUDES = [('MOXIE', 'Moxie'), ('TT','Trauma Threshold'), ('LUC','Lucidity'),
                       ('IR','Insanity Rating'), ('WT','Wound Threshold'),
                       ('DUR','Durability'), ('DR','Death Rating'), ('INIT','Initiative'),
                       ('SPD','Speed'), ('DB','Damage Bonus')]

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
    description = models.TextField(blank=True)
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
    advantages = models.TextField(default='', blank=True)
    disadvantages = models.TextField(default='', blank=True)
    implants = models.TextField(default='', blank=True)

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
    #TODO: Remove these?  Should always be computed values.
    INIT = models.IntegerField('Initiative', null=False, default=0)
    LUC = models.IntegerField('Lucidity', null=False, default=0)
    TT = models.IntegerField('Trauma Threshold', null=False, default=0)
    IR = models.IntegerField('Insanity Rating', null=False, default=0)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=256, default='')
    description = models.TextField(blank=True)
    linked = models.CharField(max_length=10, choices=APTITUDES)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class PsiSleight(models.Model):
    name = models.CharField(max_length=256, default='')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Background(models.Model):
    name = models.CharField(max_length=256, default='')
    description = models.TextField(blank=True)
    advantages = models.TextField(blank=True)
    disadvantages = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Faction(models.Model):
    name = models.CharField(max_length=256, default='')
    description = models.TextField(blank=True)
    advantages = models.TextField(blank=True)
    disadvantages = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=256, default='')
    ego = models.ForeignKey(Ego)
    morph = models.ForeignKey(Morph)
    background = models.ForeignKey(Background)
    faction = models.ForeignKey(Faction)

    @property
    def COG(self):
        return self.ego.COG + self.morph.model.COG

    @property
    def COO(self):
        return self.ego.COO + self.morph.model.COO

    @property
    def INT(self):
        return self.ego.INT + self.morph.model.INT

    @property
    def REF(self):
        return self.ego.REF + self.morph.model.REF

    @property
    def SAV(self):
        return self.ego.SAV + self.morph.model.SAV

    @property
    def SOM(self):
        return self.ego.SOM + self.morph.model.SOM

    @property
    def WIL(self):
        return self.ego.WIL + self.morph.model.WIL

    @property
    def MOXIE(self):
        return self.ego.MOXIE

    @property
    def INIT(self):
        return (self.ego.INT + self.ego.REF) / 5

    @property
    def LUC(self):
        return self.WIL * 2

    @property
    def TT(self):
        return self.LUC / 5

    @property
    def IR(self):
        return self.LUC * 2

    @property
    def DUR(self):
        return self.morph.model.DUR

    @property
    def WT(self):
        return self.morph.model.DUR / 5

    @property
    def DR(self):
        return self.morph.model.DUR * 1.5  #synth morphs *2

    @property
    def DB(self):
        return self.SOM / 10

    @property
    def SPD(self):
        return 1 + self.morph.model.SPD

    def generate_skill_bases(self):
        if CharacterSkill.objects.filter(character=self).exists():
            CharacterSkill.objects.filter(character=self).delete()
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
    specialization = models.CharField(max_length=64, blank=True)
    points = models.IntegerField(default=0)
    character = models.ForeignKey(Character, default=None)

    @property
    def value(self):
        apt = self.skill.linked
        base = getattr(self.character, apt)
        return base + self.points

    def __str__(self):
        return self.character.name + ' ' + \
               self.skill.name + ': ' + \
               self.specialization + ' ' + str(self.value)


class Party(models.Model):
    name = models.CharField(max_length=256)
    members = models.ManyToManyField(Character)
    timestamp = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.name + ' ' + str(self.timestamp)


class Campaign(models.Model):
    name = models.CharField(max_length=256)
    parties = models.ManyToManyField(Party)

    def __str__(self):
        return self.name