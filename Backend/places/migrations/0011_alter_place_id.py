# Generated by Django 4.2 on 2023-06-06 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0010_alter_place_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='id',
            field=models.UUIDField(default='<function uuid4 at 0x0000020638098E50>', editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
