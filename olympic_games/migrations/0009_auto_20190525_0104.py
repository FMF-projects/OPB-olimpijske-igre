# Generated by Django 2.0.9 on 2019-05-24 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olympic_games', '0008_auto_20190525_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drzava',
            name='ime',
            field=models.TextField(unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='rezultat',
            unique_together={('ime', 'disciplina', 'mesto', 'olimpijske_igre')},
        ),
    ]