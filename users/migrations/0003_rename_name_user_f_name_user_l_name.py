# Generated by Django 4.2.3 on 2023-07-26 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='f_name',
        ),
        migrations.AddField(
            model_name='user',
            name='l_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
