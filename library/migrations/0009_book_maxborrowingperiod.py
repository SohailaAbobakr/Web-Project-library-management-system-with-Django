# Generated by Django 3.2.5 on 2021-07-20 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_delete_borrower'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='maxborrowingPeriod',
            field=models.IntegerField(default=0),
        ),
    ]
