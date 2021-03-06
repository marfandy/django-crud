# Generated by Django 3.2 on 2022-06-28 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10),
        ),
        migrations.AlterField(
            model_name='grandchild',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10),
        ),
        migrations.AlterField(
            model_name='parents',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10),
        ),
    ]
