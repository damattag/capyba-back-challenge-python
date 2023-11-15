# Generated by Django 4.2.7 on 2023-11-15 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_verification_token',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email_verification_token_expiry',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
    ]