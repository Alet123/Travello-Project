# Generated by Django 3.2.15 on 2022-09-28 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staticapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nam', models.CharField(max_length=250)),
                ('im', models.ImageField(upload_to='pics')),
                ('des', models.TextField()),
            ],
        ),
    ]
