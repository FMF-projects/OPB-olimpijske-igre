# Generated by Django 2.0.9 on 2019-05-24 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('olympic_games', '0007_auto_20190524_1831'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='tekmovalec',
            unique_together={('ime', 'rojstvo')},
        ),
    ]
