# Generated by Django 4.1.3 on 2022-11-15 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advocate',
            old_name='name',
            new_name='username',
        ),
    ]