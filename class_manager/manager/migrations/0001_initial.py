# Generated by Django 4.2 on 2024-04-15 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('osis', models.IntegerField(unique=True)),
                ('grade', models.SmallIntegerField()),
                ('gpa', models.FloatField(max_length=10)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('teacher', models.CharField(max_length=200)),
                ('students', models.ManyToManyField(to='manager.student')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
