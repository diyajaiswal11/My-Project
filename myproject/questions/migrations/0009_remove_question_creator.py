# Generated by Django 3.0.4 on 2020-03-30 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0008_auto_20200331_0033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='creator',
        ),
    ]