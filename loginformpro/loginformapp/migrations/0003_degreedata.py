# Generated by Django 4.1.7 on 2023-05-05 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginformapp', '0002_hscdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='degreedata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('hallno', models.IntegerField()),
                ('bcomunication', models.IntegerField()),
                ('pm', models.IntegerField()),
                ('dbms', models.IntegerField()),
                ('clanguage', models.IntegerField()),
                ('bstatistics', models.IntegerField()),
            ],
        ),
    ]
