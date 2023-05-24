# Generated by Django 4.2.1 on 2023-05-24 12:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("pages", models.PositiveIntegerField()),
                ("age_limit", models.PositiveIntegerField()),
                ("published_at", models.DateField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "books",
            },
        ),
        migrations.CreateModel(
            name="BookPublisher",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=500)),
            ],
            options={
                "db_table": "publisher",
            },
        ),
        migrations.CreateModel(
            name="Library",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("IN PROGRESS", "in progress"),
                            ("DONE", "done"),
                            ("PLANNED", "planned"),
                        ],
                        default="PLANNED",
                        max_length=11,
                        verbose_name="Status user book",
                    ),
                ),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="elibrary.book"
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
            options={
                "db_table": "library",
            },
        ),
        migrations.AddField(
            model_name="book",
            name="publisher",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="elibrary.bookpublisher",
            ),
        ),
    ]