# Generated by Django 4.1 on 2023-02-01 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
