# Generated by Django 2.0.1 on 2018-01-04 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0002_chat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='message',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
