# Generated by Django 5.1.7 on 2025-04-09 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0010_rename_courses_subscription_course_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="updated_ad",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name="lesson",
            name="updated_ad",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
