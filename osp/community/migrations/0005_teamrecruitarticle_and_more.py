# Generated by Django 4.0.5 on 2022-07-18 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0006_delete_teamrecruitarticle'),
        ('community', '0004_auto_20220715_1036'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamRecruitArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.article')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.team')),
            ],
        ),
        migrations.AddConstraint(
            model_name='teamrecruitarticle',
            constraint=models.UniqueConstraint(fields=('team', 'article'), name='unique_team_article'),
        ),
    ]