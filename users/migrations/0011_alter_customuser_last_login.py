# Generated by Django 5.1.7 on 2025-04-09 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0010_alter_payments_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="last_login",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
