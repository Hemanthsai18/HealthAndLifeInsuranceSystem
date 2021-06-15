# Generated by Django 3.1.6 on 2021-05-17 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('global', '0003_life_insurance'),
    ]

    operations = [
        migrations.AddField(
            model_name='health_insurance',
            name='pdf',
            field=models.FileField(default='settings.MEDIA/pdfs/TERM INSURANCE.pdf', upload_to='pdfs'),
        ),
        migrations.AddField(
            model_name='life_insurance',
            name='pdf',
            field=models.FileField(default='settings.MEDIA/pdfs/TERM INSURANCE.pdf', upload_to='pdfs'),
        ),
    ]
