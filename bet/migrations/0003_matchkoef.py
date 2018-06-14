# Generated by Django 2.0.3 on 2018-06-11 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bet', '0002_auto_20180608_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchKoef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match', models.IntegerField()),
                ('bet_team', models.IntegerField()),
                ('perc', models.IntegerField()),
                ('koef', models.FloatField()),
            ],
            options={
                'db_table': 'match_koef',
                'managed': False,
            },
        ),
    ]
