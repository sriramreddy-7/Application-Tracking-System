# Generated by Django 4.2.1 on 2024-05-08 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_userjobapplication_posted_on_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecommendedWebsite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('url', models.URLField()),
            ],
        ),
    ]