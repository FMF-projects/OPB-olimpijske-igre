from django.db import models

class Disciplina(models.Model):
    id = models.AutoField(primary_key=True)
    ime = models.TextField(null=False, unique=True)


class OlimpijskeIgre(models.Model):
    leto = models.IntegerField(primary_key=True)
    mesto = models.TextField(null=False)


class Drzava(models.Model):
    kratica = models.TextField(primary_key=True)
    ime = models.TextField()

class Tekmovalec(models.Model):
    id = models.AutoField(primary_key=True)
    ime = models.TextField(null=False)
    drzava = models.ForeignKey(Drzava, on_delete=models.CASCADE)
    rojstvo = models.DateField(null=True)
    