# Generated by Django 2.2.1 on 2020-11-03 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20201102_1620'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['Surname']},
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=25, unique=True, verbose_name='ISBN'),
        ),
    ]
