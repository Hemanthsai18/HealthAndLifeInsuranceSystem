# Generated by Django 3.1.6 on 2021-05-07 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('global', '0002_auto_20210507_1505'),
    ]

    operations = [
        migrations.CreateModel(
            name='Life_Insurance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
