# Generated by Django 3.2.7 on 2021-09-23 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20210923_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='investor',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='investor',
            name='investor_type',
            field=models.CharField(choices=[('Other', 'Other'), ('Venture Capitalist', 'Venture Capitalist'), ('Angel Investor', 'Angel Investor')], max_length=100),
        ),
        migrations.AlterField(
            model_name='startup',
            name='applicant_title',
            field=models.CharField(choices=[('employee', 'Employee'), ('founder', 'Founder'), ('co-founder', 'Co-founder')], max_length=100),
        ),
        migrations.AlterField(
            model_name='startup',
            name='start_month',
            field=models.CharField(choices=[('February', 'February'), ('May', 'May'), ('December', 'December'), ('September', 'September'), ('June', 'June'), ('March', 'March'), ('October', 'October'), ('July', 'July'), ('August', 'August'), ('April', 'April'), ('January', 'January'), ('November', 'November')], max_length=100),
        ),
        migrations.AlterField(
            model_name='startup',
            name='start_year',
            field=models.CharField(blank=True, choices=[('2021', '2021'), ('2018', '2018'), ('2020', '2020'), ('2019', '2019')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='startup',
            name='startup_stage',
            field=models.CharField(choices=[('prototype', 'Prototype'), ('users', 'Users'), ('paying users', 'Paying Users'), ('idea', 'Idea')], max_length=100),
        ),
    ]