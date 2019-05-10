from django.db import models

class Disciplina(models.Model):
    id = models.AutoField(primary_key=True)
    ime = models.TextField(null=False)


class OlimpijskeIgre(models.Model):
    leto = models.IntegerField(primary_key=True)
    mesto = models.TextField(null=False)


class Drzava(models.Model):
    kratica = models.TextField(primary_key=True)
    ime = models.TextField(null=False)

class Tekmovalec(models.Model):
    id = models.AutoField(primary_key=True)
    ime = models.TextField(null=False)
    drzava = models.ForeignKey(Drzava)
    rojstvo = models.DateField(null=True)
    mesto = models.IntegerField(null=True)
    rezultat = models.IntegerField(null=True)
    olimpijske_igre = models.ForeignKey(OlimpijskeIgre)
