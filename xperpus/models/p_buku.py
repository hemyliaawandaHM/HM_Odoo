from odoo import api, fields, models


class Buku(models.Model):
    _name = 'perpus.buku'
    _description = 'Berbagai macam buku'

    judul = fields.Char(
        string='Judul Buku')
    pengarang = fields.Char(
        string='Nama Pengarang')
    kota = fields.Char(
        string='Kota Buku')
    status = fields.Selection(
        string='Status Buku', 
        selection=[('dipinjam','Tersedia'),('tersedia','Dipinjam')])
    tahun = fields.Datetime(
        string='Tahun Buku',
        default=fields.Datetime.now())
    jumlah = fields.Integer(
        string='Jumlah Buku')
    klasifikasi = fields.Many2one(
        comodel_name='perpus.kelompok', 
        string='Kelompok Buku')
    