# Generated by Django 4.1.7 on 2023-04-23 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='subscribers',
            field=models.TextField(blank=True, null=True),
        ),
    ]