# Generated by Django 4.2.2 on 2023-06-23 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0004_rename_tages_post_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="approved",
            field=models.BooleanField(default=True),
        ),
    ]
