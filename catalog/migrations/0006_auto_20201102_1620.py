# Generated by Django 2.2.1 on 2020-11-02 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20201030_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='YearEdition',
            field=models.CharField(blank=True, max_length=4),
        ),
    ]
