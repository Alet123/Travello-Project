# Generated by Django 3.2.15 on 2022-09-28 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staticapp', '0002_people'),
    ]

    operations = [
        migrations.RenameField(
            model_name='people',
            old_name='des',
            new_name='des1',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='im',
            new_name='img1',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='nam',
            new_name='nam1',
        ),
    ]