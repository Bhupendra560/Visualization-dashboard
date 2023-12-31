# Generated by Django 4.2 on 2023-11-20 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_newsarticle_end_year_alter_newsarticle_impact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='added',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='end_year',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='impact',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='insight',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='intensity',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='likelihood',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='published',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='relevance',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='start_year',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='url',
            field=models.CharField(max_length=255),
        ),
    ]
