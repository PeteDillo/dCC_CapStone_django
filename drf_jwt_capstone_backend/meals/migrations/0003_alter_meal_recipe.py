# Generated by Django 4.0 on 2021-12-17 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0002_alter_meal_recipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='recipe',
            field=models.CharField(max_length=45),
        ),
    ]
