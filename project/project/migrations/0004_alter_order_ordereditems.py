# Generated by Django 4.1.5 on 2023-03-07 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_alter_menuitem_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderedItems',
            field=models.JSONField(default={}),
            preserve_default=False,
        ),
    ]
