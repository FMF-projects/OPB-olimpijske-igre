# Generated by Django 2.0.9 on 2019-05-18 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('olympic_games', '0003_auto_20190517_2330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tekmovalec',
            name='mesto',
        ),
        migrations.RemoveField(
            model_name='tekmovalec',
            name='olimpijske_igre',
        ),
        migrations.RemoveField(
            model_name='tekmovalec',
            name='rezultat',
        ),
    ]
