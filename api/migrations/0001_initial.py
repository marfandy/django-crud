# Generated by Django 3.2 on 2022-06-28 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Felame')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Felame')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='GrandChild',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Felame')], max_length=10)),
                ('fk_child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grandchild', to='api.child')),
            ],
        ),
        migrations.AddField(
            model_name='child',
            name='fk_parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child', to='api.parents'),
        ),
    ]