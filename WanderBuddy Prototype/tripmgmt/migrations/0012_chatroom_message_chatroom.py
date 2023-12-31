# Generated by Django 4.2.5 on 2023-09-27 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tripmgmt', '0011_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chatroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participants', models.ManyToManyField(blank=True, null=True, related_name='participants', to='tripmgmt.participant')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='tripmgmt.trip')),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='chatroom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tripmgmt.chatroom'),
        ),
    ]
