# Generated by Django 2.1.5 on 2019-03-30 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oleaapp', '0002_auto_20190330_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='matiere',
            name='code',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='salle',
            name='situation',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
