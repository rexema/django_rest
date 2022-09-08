# Generated by Django 3.2.15 on 2022-09-08 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('link', models.URLField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=120)),
                ('date_of_creation', models.DateField()),
                ('date_of_update', models.DateField()),
                ('is_accomplished', models.BooleanField(default=False)),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='todo.project')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='todo.user')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ManyToManyField(to='todo.User'),
        ),
    ]
