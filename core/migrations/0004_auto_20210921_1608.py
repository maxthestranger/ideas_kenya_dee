# Generated by Django 3.2.7 on 2021-09-21 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_startup_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='application_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='startup',
            name='pending',
            field=models.BooleanField(default=True),
        ),
    ]