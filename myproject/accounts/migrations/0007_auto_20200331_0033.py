# Generated by Django 3.0.4 on 2020-03-30 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200330_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>.', null=True),
        ),
    ]
