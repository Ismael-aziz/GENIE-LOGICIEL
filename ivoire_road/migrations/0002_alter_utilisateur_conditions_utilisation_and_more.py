# Generated by Django 5.0.1 on 2024-02-05 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ivoire_road', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='conditions_utilisation',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='mot_de_passe',
            field=models.CharField(max_length=256),
        ),
    ]
