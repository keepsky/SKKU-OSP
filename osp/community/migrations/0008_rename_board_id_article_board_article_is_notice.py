# Generated by Django 4.1.3 on 2023-02-20 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0007_auto_20220727_1504'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='board_id',
            new_name='board',
        ),
        migrations.AddField(
            model_name='article',
            name='is_notice',
            field=models.BooleanField(default=False),
        ),
    ]