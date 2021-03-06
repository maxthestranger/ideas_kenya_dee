# Generated by Django 3.2.7 on 2021-10-09 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20211004_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='investor',
            name='status',
            field=models.CharField(choices=[('Declined', 'Declined'), ('Approved', 'Approved'), ('Pending', 'Pending')], default='Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='startup',
            name='applicant_role',
            field=models.CharField(choices=[('employee', 'Employee'), ('founder', 'Founder'), ('co-founder', 'Co-founder')], max_length=100),
        ),
        migrations.AlterField(
            model_name='startup',
            name='start_month',
            field=models.CharField(choices=[('October', 'October'), ('June', 'June'), ('November', 'November'), ('January', 'January'), ('July', 'July'), ('May', 'May'), ('February', 'February'), ('March', 'March'), ('September', 'September'), ('April', 'April'), ('August', 'August'), ('December', 'December')], max_length=100),
        ),
        migrations.AlterField(
            model_name='startup',
            name='start_year',
            field=models.CharField(blank=True, choices=[('2007', '2007'), ('2020', '2020'), ('2010', '2010'), ('2003', '2003'), ('2009', '2009'), ('2016', '2016'), ('2015', '2015'), ('2021', '2021'), ('2005', '2005'), ('2008', '2008'), ('2012', '2012'), ('2018', '2018'), ('2013', '2013'), ('2006', '2006'), ('2011', '2011'), ('2017', '2017'), ('2004', '2004'), ('2019', '2019'), ('2014', '2014')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='startup',
            name='startup_stage',
            field=models.CharField(choices=[('prototype', 'Prototype'), ('paying users', 'Paying Users'), ('users', 'Users'), ('idea', 'Idea')], max_length=100),
        ),
        migrations.AlterField(
            model_name='startup',
            name='status',
            field=models.CharField(choices=[('Declined', 'Declined'), ('Approved', 'Approved'), ('Pending', 'Pending')], default='Pending', max_length=100),
        ),
    ]
