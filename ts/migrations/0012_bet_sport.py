# Generated by Django 2.0.2 on 2018-02-19 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ts', '0011_sport'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet',
            name='sport',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='ts.Sport'),
        ),
    ]
