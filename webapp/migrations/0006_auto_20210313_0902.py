# Generated by Django 3.1.5 on 2021-03-13 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20210309_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertydetails',
            name='district',
            field=models.CharField(default='Kathmandu', max_length=100),
        ),
        migrations.AlterField(
            model_name='propertydetails',
            name='Province',
            field=models.CharField(choices=[('1', 'Province1'), ('2', 'Province2'), ('3', 'Bagmati(3)'), ('4', 'Gandaki(4)'), ('5', 'Lumbini(5)'), ('6', 'Karnali(6)'), ('7', 'Sudurpashchim(7)')], default='Bagmati(3)', max_length=15),
        ),
        migrations.AlterField(
            model_name='propertydetails',
            name='address',
            field=models.CharField(default='Koteshwor', max_length=100),
        ),
    ]
