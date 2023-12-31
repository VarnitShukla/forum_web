# Generated by Django 4.2.2 on 2023-06-22 11:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("taggit", "0005_auto_20220424_2025"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("slug", models.SlugField(blank=True, max_length=400, unique=True)),
            ],
            options={
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("slug", models.SlugField(blank=True, max_length=400, unique=True)),
                ("content", models.TextField()),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("approved", models.BooleanField(default=False)),
                ("categories", models.ManyToManyField(to="members.category")),
                (
                    "tages",
                    taggit.managers.TaggableManager(
                        help_text="A comma-separated list of tags.",
                        through="taggit.TaggedItem",
                        to="taggit.Tag",
                        verbose_name="Tags",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fullname", models.CharField(blank=True, max_length=40, null=True)),
                ("slug", models.SlugField(blank=True, max_length=400, unique=True)),
                ("bio", models.TextField(blank=True, null=True)),
                ("points", models.IntegerField(default=0)),
                (
                    "profile_pic",
                    django_resized.forms.ResizedImageField(
                        crop=None,
                        default=None,
                        force_format=None,
                        keep_meta=True,
                        null=True,
                        quality=100,
                        scale=None,
                        size=[50, 80],
                        upload_to="authors",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
