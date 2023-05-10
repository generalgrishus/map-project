# Generated by Django 4.2 on 2023-05-10 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='emo_text',
            field=models.TextField(blank=True, verbose_name='emotion_text'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]