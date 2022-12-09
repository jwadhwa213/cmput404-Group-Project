# Generated by Django 4.1.2 on 2022-11-29 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='origin',
            field=models.URLField(default='https://cmput404team18-backend.herokuapp.com/', max_length=255),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='source',
            field=models.URLField(default='https://cmput404team18-backend.herokuapp.com/', max_length=255),
        ),
        migrations.AlterField(
            model_name='users',
            name='host',
            field=models.CharField(blank=True, default='https://cmput404team18-backend.herokuapp.com/backendapi/', max_length=200),
        ),
        migrations.AlterField(
            model_name='users',
            name='url',
            field=models.CharField(default='https://cmput404team18-backend.herokuapp.com/backendapi/authors/<django.db.models.fields.UUIDField>', max_length=225),
        ),
    ]
