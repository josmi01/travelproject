# Generated by Django 4.1.7 on 2023-03-23 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nurseryapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pics')),
                ('name', models.CharField(max_length=250)),
                ('desc', models.TextField()),
            ],
        ),
    ]
