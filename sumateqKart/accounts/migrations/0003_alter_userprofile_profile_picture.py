# Generated by Django 4.2.6 on 2023-11-26 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='default/download.png', upload_to='userprofile'),
        ),
    ]
