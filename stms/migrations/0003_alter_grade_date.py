# Generated by Django 5.1.4 on 2024-12-08 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stms', '0002_alter_class_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='date',
            field=models.DateField(),
        ),
    ]