# Generated by Django 2.2.12 on 2022-06-14 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GithubIssues',
            fields=[
                ('owner_id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('repo_name', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('github_id', models.CharField(max_length=40)),
                ('title', models.CharField(max_length=256)),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'github_issues',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GithubPulls',
            fields=[
                ('owner_id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('repo_name', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('github_id', models.CharField(max_length=40)),
                ('title', models.CharField(max_length=256)),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'github_pulls',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GithubRepoCommits',
            fields=[
                ('github_id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('repo_name', models.CharField(max_length=100)),
                ('sha', models.CharField(max_length=40)),
                ('additions', models.IntegerField()),
                ('deletions', models.IntegerField()),
                ('author_date', models.DateTimeField()),
                ('committer_date', models.DateTimeField()),
                ('author', models.CharField(blank=True, max_length=100, null=True)),
                ('committer', models.CharField(blank=True, max_length=100, null=True)),
                ('author_github', models.CharField(blank=True, max_length=50, null=True)),
                ('committer_github', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'github_repo_commits',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GithubRepoContributor',
            fields=[
                ('github_id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('owner_id', models.CharField(max_length=40)),
                ('repo_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'github_repo_contributor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GithubRepoStats',
            fields=[
                ('github_id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('repo_name', models.CharField(max_length=100)),
                ('stargazers_count', models.IntegerField(blank=True, null=True)),
                ('forks_count', models.IntegerField(blank=True, null=True)),
                ('commits_count', models.IntegerField(blank=True, null=True)),
                ('prs_count', models.IntegerField(blank=True, null=True)),
                ('open_issue_count', models.IntegerField(blank=True, null=True)),
                ('close_issue_count', models.IntegerField(blank=True, null=True)),
                ('watchers_count', models.IntegerField(blank=True, null=True)),
                ('dependencies', models.IntegerField(blank=True, null=True)),
                ('language', models.CharField(blank=True, max_length=45, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('contributors_count', models.IntegerField(blank=True, null=True)),
                ('release_ver', models.CharField(blank=True, max_length=45, null=True)),
                ('release_count', models.IntegerField(blank=True, null=True)),
                ('readme', models.IntegerField(blank=True, null=True)),
                ('license', models.CharField(blank=True, max_length=45, null=True)),
                ('proj_short_desc', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'github_repo_stats',
                'managed': False,
            },
        ),
    ]
