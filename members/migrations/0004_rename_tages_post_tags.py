# Generated by Django 4.2.2 on 2023-06-23 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0003_reply_comment_post_comments"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="tages",
            new_name="tags",
        ),
    ]
