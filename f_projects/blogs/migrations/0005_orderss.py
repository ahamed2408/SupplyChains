# Generated by Django 3.2 on 2021-06-03 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='orderss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sen_name', models.CharField(blank=True, max_length=100, null=True)),
                ('sen_add', models.TextField()),
                ('sen_ph', models.CharField(blank=True, max_length=100, null=True)),
                ('rec_name', models.CharField(blank=True, max_length=100, null=True)),
                ('rec_add', models.TextField()),
                ('rec_ph', models.CharField(blank=True, max_length=100, null=True)),
                ('t_g', models.CharField(blank=True, max_length=100, null=True)),
                ('orgin', models.CharField(blank=True, max_length=100, null=True)),
                ('dest', models.CharField(blank=True, max_length=100, null=True)),
                ('pri', models.CharField(blank=True, max_length=100, null=True)),
                ('nodays', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('rej', models.IntegerField()),
                ('cost', models.IntegerField()),
                ('shipid', models.IntegerField()),
                ('dd', models.CharField(blank=True, max_length=100, null=True)),
                ('dm', models.CharField(blank=True, max_length=100, null=True)),
                ('dy', models.CharField(blank=True, max_length=100, null=True)),
                ('ddd', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]