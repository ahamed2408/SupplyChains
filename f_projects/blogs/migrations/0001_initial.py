# Generated by Django 3.2 on 2021-05-22 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desii',
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
                ('shipment', models.IntegerField()),
                ('weight', models.CharField(blank=True, max_length=100, null=True)),
                ('mes', models.TextField()),
                ('rej', models.IntegerField()),
                ('cost', models.IntegerField()),
                ('con_e', models.IntegerField()),
                ('con_f', models.IntegerField()),
                ('con_s', models.IntegerField()),
            ],
        ),
    ]
