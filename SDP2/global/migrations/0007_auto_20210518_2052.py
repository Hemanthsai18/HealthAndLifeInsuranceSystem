# Generated by Django 3.1.6 on 2021-05-18 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('global', '0006_user_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='User_Own',
        ),
    ]