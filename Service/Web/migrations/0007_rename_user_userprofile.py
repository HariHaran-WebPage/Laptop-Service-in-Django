# Generated by Django 5.0 on 2024-01-05 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0006_user_delete_userprofile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserProfile',
        ),
    ]
