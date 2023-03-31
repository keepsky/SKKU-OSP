# Generated by Django 4.1.3 on 2023-03-21 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0010_alter_articleimage_created_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleFile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('file', models.FileField(default='', upload_to='file/article/')),
                ('created_user', models.CharField(max_length=150)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(max_length=20)),
                ('article_id', models.BigIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='articleimage',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='articleimage',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
