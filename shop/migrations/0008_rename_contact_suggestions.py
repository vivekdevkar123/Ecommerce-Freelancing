# Generated by Django 3.2.12 on 2023-07-13 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_orderupdate_order_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='Suggestions',
        ),
    ]
