# Generated by Django 4.0.5 on 2022-07-18 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0005_rename_target_account_teaminvitemessage_account_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TeamRecruitArticle',
        ),
    ]
