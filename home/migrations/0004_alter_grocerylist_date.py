# Generated by Django 3.2.7 on 2021-09-06 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_grocerylist_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocerylist',
            name='date',
            field=models.DateField(max_length=50),
        ),
    ]
