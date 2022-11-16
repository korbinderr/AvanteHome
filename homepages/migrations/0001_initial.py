# Generated by Django 4.1.2 on 2022-11-16 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_photo', models.ImageField(upload_to='photos')),
                ('price', models.IntegerField(default=0)),
                ('square_ft', models.IntegerField(default=0)),
                ('beds', models.IntegerField(default=0)),
                ('baths', models.IntegerField(default=0)),
                ('garage_spaces', models.IntegerField(default=0)),
                ('street_address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=2)),
                ('lot_size', models.IntegerField(default=0)),
                ('year_built', models.IntegerField(default=0)),
                ('days_listed', models.IntegerField(default=0)),
            ],
        ),
    ]