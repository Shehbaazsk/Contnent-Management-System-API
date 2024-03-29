# Generated by Django 5.0.2 on 2024-02-14 17:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('body', models.TextField(max_length=300)),
                ('summary', models.CharField(max_length=60)),
                ('documents', models.FileField(upload_to='media')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_contents', to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(blank=True, null=True, related_name='category_contents', to='contents.contentcategory')),
            ],
        ),
    ]
