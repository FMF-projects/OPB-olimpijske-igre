# Generated by Django 2.2.1 on 2019-05-18 18:38

from django.db import migrations, models
import django.db.models.deletion


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
        migrations.CreateModel(
            name='Rezultat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mesto', models.IntegerField(null=True)),
                ('rezultat', models.IntegerField(null=True)),
                ('ime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='olympic_games.Tekmovalec')),
                ('olimpijske_igre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='olympic_games.OlimpijskeIgre')),
            ],
        ),
    ]
