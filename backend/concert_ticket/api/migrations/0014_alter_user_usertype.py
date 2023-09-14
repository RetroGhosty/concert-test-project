# Generated by Django 4.2.2 on 2023-07-29 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_user_usertype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userType',
            field=models.CharField(choices=[('organizer', 'Organizer'), ('normal user', 'Normal User')], default='normal user', max_length=100),
        ),
    ]