# Generated by Django 5.0.2 on 2024-02-15 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0002_alter_content_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='documents',
            field=models.FileField(upload_to='documents'),
        ),
    ]
