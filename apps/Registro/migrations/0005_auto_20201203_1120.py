# Generated by Django 3.1.2 on 2020-12-03 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0004_auto_20201110_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imgcategoria'),
        ),
    ]