# Generated by Django 4.0 on 2021-12-22 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favmeals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='favmeal',
            name='label',
            field=models.CharField(default='beef tacos', max_length=300),
            preserve_default=False,
        ),
    ]