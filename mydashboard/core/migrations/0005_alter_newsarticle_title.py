# Generated by Django 4.2 on 2023-11-20 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_newsarticle_added_alter_newsarticle_end_year_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='title',
            field=models.CharField(max_length=512),
        ),
    ]
