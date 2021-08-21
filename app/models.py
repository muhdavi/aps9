from django.db import models


class Program_studi(models.Model):
    nama_program_studi = models.CharField(max_length=100)
    jenis_program = models.CharField(max_length=100)
    akreditasi_program_studi = models.CharField(max_length=20)
    nomor_sk_banpt = models.CharField(max_length=50)
    tanggal_kadaluarsa = models.DateField()
    nama_unit_pengelola = models.CharField(max_length=100)
    nama_perguruan_tinggi = models.CharField(max_length=100)
    alamat = models.TextField()
    kota = models.CharField(max_length=50)
    kodepos = models.CharField(max_length=10)
    nomor_telepon = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField()
    ts = models.CharField(max_length=10)
    nama_pengusul = models.CharField(max_length=100)
    tanggal_usulan = models.DateField()

    def __str__(self):
        return self.nama_program_studi

    class Meta:
        verbose_name = 'Program Studi'
        verbose_name_plural = 'Program Studi'


class Kriteria1_kerjasama(models.Model):
    TINGKATAN = (
        ('I', 'Internasional'),
        ('N', 'Nasional'),
        ('L', 'Lokal'),
    )
    lembaga_mitra = models.CharField(max_length=100)
    tingkat = models.CharField(max_length=2, choices=TINGKATAN)
    judul_kegiatan = models.CharField(max_length=200)
    waktu = models.DateField()
    durasi = models.CharField(max_length=10)
    bukti = models.CharField(max_length=100)
    tahun_berakhirnya = models.DateField()

    def __str__(self):
        return self.judul_kegiatan

    class Meta:
        verbose_name = 'Kriteria-1 Kerjasama'
        verbose_name_plural = 'Kriteria-1 Kerjasama'


class Kriteria2_Seleksimahasiswabaru(models.Model):
    tahun_akademik = models.CharField(max_length=10)
    daya_tampung = models.CharField(max_length=10)
    jumlah_calon_pendaftar = models.IntegerField(verbose_name='Jumlah Pendaftar Calon Mahasiswa')
    jumlah_calon_lulus = models.IntegerField(verbose_name='Jumlah Lulus Seleksi Calon Mahasiswa')
    jumlah_baru_reguler = models.IntegerField(verbose_name='Jumlah Mahasiswa Baru Reguler')
    jumlah_baru_transfer = models.IntegerField(verbose_name='Jumlah Mahasiswa Baru Transfer')
    jumlah_aktif_reguler = models.IntegerField(verbose_name='Jumlah Mahasiswa Aktif Baru')
    jumlah_aktif_transfer = models.IntegerField(verbose_name='Jumlah Mahasiswa Aktif Transfer')

    def __str__(self):
        return self.tahun_akademik

    class Meta:
        verbose_name = 'Kriteria-2 Seleksi Mahasiswa Baru'
        verbose_name_plural = 'Kriteria-2 Seleksi Mahasiswa Baru'


class Kriteria2_Mahasiswaasing(models.Model):
    program_studi = models.ForeignKey(Program_studi, null=True, on_delete=models.CASCADE)
    jumlah_aktif_ts0 = models.IntegerField()
    jumlah_aktif_ts1 = models.IntegerField()
    jumlah_aktif_ts2 = models.IntegerField()
    jumlah_asing_penuh_ts0 = models.IntegerField()
    jumlah_asing_penuh_ts1 = models.IntegerField()
    jumlah_asing_penuh_ts2 = models.IntegerField()
    jumlah_asing_paruh_ts0 = models.IntegerField()
    jumlah_asing_paruh_ts1 = models.IntegerField()
    jumlah_asing_paruh_ts2 = models.IntegerField()

    def __str__(self):
        return self.program_studi

    class Meta:
        verbose_name = 'Kriteria-2 Mahasiswa Asing'
        verbose_name_plural = 'Kriteria-2 Mahasiswa Asing'

