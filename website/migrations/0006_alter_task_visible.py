# Generated by Django 4.0.3 on 2022-04-06 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_task_visible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='visible',
            field=models.BooleanField(default=False),
        ),
    ]
