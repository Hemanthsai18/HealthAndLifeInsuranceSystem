# Generated by Django 3.1.6 on 2021-05-18 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('global', '0008_auto_20210518_2055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('age', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('year', models.IntegerField()),
                ('typo', models.IntegerField()),
                ('total', models.IntegerField()),
                ('month', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='user_own',
            name='age',
        ),
        migrations.RemoveField(
            model_name='user_own',
            name='health_data',
        ),
        migrations.RemoveField(
            model_name='user_own',
            name='life_data',
        ),
        migrations.AddField(
            model_name='user_own',
            name='details',
            field=models.ManyToManyField(to='global.Details'),
        ),
    ]