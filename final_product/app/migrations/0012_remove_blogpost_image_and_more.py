# Generated by Django 5.1.2 on 2024-11-24 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_admin_referrallink_referral_link_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='image',
        ),
        migrations.AlterField(
            model_name='admin_referrallink',
            name='referral_link',
            field=models.CharField(default='277ec21ca07a49b0a86c13ad14328975', max_length=255, unique=True),
        ),
    ]
