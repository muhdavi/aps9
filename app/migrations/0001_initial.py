# Generated by Django 3.1.3 on 2021-08-21 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Program_studi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_program_studi', models.CharField(max_length=100)),
                ('jenis_program', models.CharField(max_length=100)),
                ('akreditasi_program_studi', models.CharField(max_length=20)),
                ('nomor_sk_banpt', models.CharField(max_length=50)),
                ('tanggal_kadaluarsa', models.DateField()),
                ('nama_unit_pengelola', models.CharField(max_length=100)),
                ('nama_perguruan_tinggi', models.CharField(max_length=100)),
                ('alamat', models.TextField()),
                ('kota', models.CharField(max_length=50)),
                ('kodepos', models.CharField(max_length=10)),
                ('nomor_telepon', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
                ('ts', models.CharField(max_length=10)),
                ('nama_pengusul', models.CharField(max_length=100)),
                ('tanggal_usulan', models.DateField()),
            ],
            options={
                'verbose_name': 'Program Studi',
                'verbose_name_plural': 'Program Studi',
            },
        ),
    ]
