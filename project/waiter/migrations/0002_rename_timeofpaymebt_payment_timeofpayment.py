# Generated by Django 4.1.5 on 2023-02-27 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('waiter', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='timeOfPaymebt',
            new_name='timeOfPayment',
        ),
    ]
