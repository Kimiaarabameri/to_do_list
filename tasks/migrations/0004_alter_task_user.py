# Generated by Django 4.1 on 2024-09-09 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
        ("tasks", "0003_remove_task_complated_task_completed"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="accounts.account"
            ),
        ),
    ]
