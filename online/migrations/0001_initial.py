# Generated by Django 3.2.6 on 2021-09-27 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registermodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('firstname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('gender', models.CharField(max_length=30)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('phone', models.BigIntegerField(unique=True)),
                ('address', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
