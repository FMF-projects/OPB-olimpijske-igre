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
    drzava = models.ForeignKey(Drzava, null=True, on_delete=models.CASCADE)
    rojstvo = models.DateField(null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['drzava', 'ime', 'rojstvo'], name='tekmovalec')
        ]

    def __str__(self):
        return str(self.id) + ":" + self.ime

class Rezultat(models.Model):
    id = models.AutoField(primary_key=True)
    ime = models.ForeignKey(Tekmovalec, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    mesto = models.IntegerField(null=True)
    rezultat = models.TextField(null=True)
    olimpijske_igre = models.ForeignKey(OlimpijskeIgre, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['olimpijske_igre', 'disciplina', 'ime', 'mesto'], name='rezultat')
        ]