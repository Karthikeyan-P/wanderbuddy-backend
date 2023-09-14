# Generated by Django 4.2.5 on 2023-09-11 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tripmgmt', '0002_delete_trip'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('phone', models.IntegerField()),
                ('emergencyContact', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('location', models.CharField(max_length=100)),
                ('organizer', models.CharField(max_length=200)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tripmgmt.user')),
                ('participants', models.ManyToManyField(blank=True, related_name='trips', to='tripmgmt.user')),
            ],
        ),
    ]
