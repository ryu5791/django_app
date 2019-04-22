# Generated by Django 2.1.7 on 2019-04-16 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tblMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playerID', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=20)),
                ('dispName', models.CharField(max_length=20)),
                ('inputName1', models.CharField(max_length=20)),
                ('inputName2', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='tblScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('gameNo', models.PositiveIntegerField()),
                ('gamePt', models.PositiveIntegerField()),
                ('playerID', models.PositiveIntegerField()),
                ('pairID', models.PositiveIntegerField()),
                ('row', models.PositiveIntegerField()),
                ('serve1st', models.BooleanField()),
                ('serve2nd', models.BooleanField()),
                ('serveTurn', models.PositiveIntegerField()),
                ('updateDate', models.DateTimeField()),
            ],
        ),
    ]
