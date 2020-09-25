# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Deckcards(models.Model):
    id_deckcard = models.AutoField(primary_key=True)
    id_deck = models.ForeignKey('Decks', models.DO_NOTHING, db_column='id_deck', blank=True, null=True)
    card_name = models.TextField(blank=True, null=True)
    cant = models.IntegerField(blank=True, null=True)
    side = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.card_name

    class Meta:
        #managed = False
        db_table = 'deckcards'


class Decks(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    format = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    class Meta:
        #managed = False
        db_table = 'decks'

class Cards(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    set = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    rarity = models.TextField(blank=True, null=True)
    manacost = models.TextField(blank=True, null=True)
    converted_manacost = models.TextField(blank=True, null=True)
    power = models.TextField(blank=True, null=True)
    toughness = models.TextField(blank=True, null=True)
    loyalty = models.TextField(blank=True, null=True)
    ability = models.TextField(blank=True, null=True)
    flavor = models.TextField(blank=True, null=True)
    variation = models.TextField(blank=True, null=True)
    artist = models.TextField(blank=True, null=True)
    number = models.TextField(blank=True, null=True)
    rating = models.TextField(blank=True, null=True)
    ruling = models.TextField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)
    generated_mana = models.TextField(blank=True, null=True)
    pricing_eur = models.TextField(blank=True, null=True)
    pricing_usd = models.TextField(blank=True, null=True)
    pricing_tix = models.TextField(blank=True, null=True)
    back_id = models.TextField(blank=True, null=True)
    watermark = models.TextField(blank=True, null=True)
    print_number = models.TextField(blank=True, null=True)
    is_original = models.TextField(blank=True, null=True)
    color_identity = models.TextField(blank=True, null=True)
    name_cn = models.TextField(blank=True, null=True)
    name_tw = models.TextField(blank=True, null=True)
    name_fr = models.TextField(blank=True, null=True)
    name_de = models.TextField(blank=True, null=True)
    name_it = models.TextField(blank=True, null=True)
    name_jp = models.TextField(blank=True, null=True)
    name_pt = models.TextField(blank=True, null=True)
    name_ru = models.TextField(blank=True, null=True)
    name_es = models.TextField(blank=True, null=True)
    name_ko = models.TextField(blank=True, null=True)
    type_cn = models.TextField(blank=True, null=True)
    type_tw = models.TextField(blank=True, null=True)
    type_fr = models.TextField(blank=True, null=True)
    type_de = models.TextField(blank=True, null=True)
    type_it = models.TextField(blank=True, null=True)
    type_jp = models.TextField(blank=True, null=True)
    type_pt = models.TextField(blank=True, null=True)
    type_ru = models.TextField(blank=True, null=True)
    type_es = models.TextField(blank=True, null=True)
    type_ko = models.TextField(blank=True, null=True)
    ability_cn = models.TextField(blank=True, null=True)
    ability_tw = models.TextField(blank=True, null=True)
    ability_fr = models.TextField(blank=True, null=True)
    ability_de = models.TextField(blank=True, null=True)
    ability_it = models.TextField(blank=True, null=True)
    ability_jp = models.TextField(blank=True, null=True)
    ability_pt = models.TextField(blank=True, null=True)
    ability_ru = models.TextField(blank=True, null=True)
    ability_es = models.TextField(blank=True, null=True)
    ability_ko = models.TextField(blank=True, null=True)
    flavor_cn = models.TextField(blank=True, null=True)
    flavor_tw = models.TextField(blank=True, null=True)
    flavor_fr = models.TextField(blank=True, null=True)
    flavor_de = models.TextField(blank=True, null=True)
    flavor_it = models.TextField(blank=True, null=True)
    flavor_jp = models.TextField(blank=True, null=True)
    flavor_pt = models.TextField(blank=True, null=True)
    flavor_ru = models.TextField(blank=True, null=True)
    flavor_es = models.TextField(blank=True, null=True)
    flavor_ko = models.TextField(blank=True, null=True)
    legality_block = models.TextField(blank=True, null=True)
    legality_standard = models.TextField(blank=True, null=True)
    legality_pioneer = models.TextField(blank=True, null=True)
    legality_modern = models.TextField(blank=True, null=True)
    legality_legacy = models.TextField(blank=True, null=True)
    legality_vintage = models.TextField(blank=True, null=True)
    legality_highlander = models.TextField(blank=True, null=True)
    legality_duel_commander = models.TextField(blank=True, null=True)
    legality_tiny_leaders_commander = models.TextField(blank=True, null=True)
    legality_commander = models.TextField(blank=True, null=True)
    legality_peasant = models.TextField(blank=True, null=True)
    legality_pauper = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        #managed = False
        db_table = 'cards'


class Sets(models.Model):
    name = models.TextField(blank=True, null=True)
    code = models.TextField(primary_key=True)
    date = models.TextField(blank=True, null=True)
    is_promo = models.TextField(blank=True, null=True)
    boosterpack_nm = models.TextField(blank=True, null=True)
    boosterpack_nr = models.TextField(blank=True, null=True)
    boosterpack_nu = models.TextField(blank=True, null=True)
    boosterpack_nc = models.TextField(blank=True, null=True)
    boosterpack_ne = models.TextField(blank=True, null=True)
    boosterpack_pm = models.TextField(blank=True, null=True)
    boosterpack_pr = models.TextField(blank=True, null=True)
    boosterpack_typeextra1 = models.TextField(blank=True, null=True)
    boosterpack_typeextra2 = models.TextField(blank=True, null=True)
    boosterpack_listextra1 = models.TextField(blank=True, null=True)
    boosterpack_listextra2 = models.TextField(blank=True, null=True)
    boosterpack_has_foil = models.TextField(blank=True, null=True)
    boosterpack_pf = models.TextField(blank=True, null=True)
    boosterpack_hasmasterpiece = models.TextField(blank=True, null=True)
    boosterpack_ppm = models.TextField(blank=True, null=True)
    boosterpack_listpmid = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        #managed = False
        db_table = 'sets'


class Users(models.Model):
    idusr = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        #managed = False
        db_table = 'users'


class Usrcards(models.Model):
    idusrcard = models.IntegerField(primary_key=True)
    quantity = models.IntegerField(blank=True, null=True)
    idcard = models.ForeignKey(Cards, models.DO_NOTHING, db_column='idcard', blank=True, null=True)
    idusr = models.ForeignKey(Users, models.DO_NOTHING, db_column='idusr', blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'usrcards'
