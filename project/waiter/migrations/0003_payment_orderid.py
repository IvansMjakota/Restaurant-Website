# Generated by Django 4.1.5 on 2023-02-27 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('waiter', '0002_rename_timeofpaymebt_payment_timeofpayment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='orderID',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='project.order'),
            preserve_default=False,
        ),
    ]