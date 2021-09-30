# Generated by Django 3.2.7 on 2021-09-27 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20210927_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='investor',
            name='status',
            field=models.CharField(choices=[('Declined', 'Declined'), ('Approved', 'Approved'), ('Pending', 'Pending')], default='Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='startup',
            name='start_month',
            field=models.CharField(choices=[('December', 'December'), ('November', 'November'), ('January', 'January'), ('April', 'April'), ('February', 'February'), ('August', 'August'), ('June', 'June'), ('May', 'May'), ('October', 'October'), ('July', 'July'), ('September', 'September'), ('March', 'March')], max_length=100),
        ),
        migrations.AlterField(
            model_name='startup',
            name='start_year',
            field=models.CharField(blank=True, choices=[('2018', '2018'), ('2020', '2020'), ('2021', '2021'), ('2019', '2019')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='startup',
            name='startup_stage',
            field=models.CharField(choices=[('paying users', 'Paying Users'), ('prototype', 'Prototype'), ('users', 'Users'), ('idea', 'Idea')], max_length=100),
        ),
        migrations.AlterField(
            model_name='startup',
            name='status',
            field=models.CharField(choices=[('Declined', 'Declined'), ('Approved', 'Approved'), ('Pending', 'Pending')], default='Pending', max_length=100),
        ),
    ]