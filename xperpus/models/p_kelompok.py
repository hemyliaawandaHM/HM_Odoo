from unicodedata import name
from odoo import api, fields, models

class Kelompok(models.Model):
    _name = 'perpus.kelompok'
    _description = 'Pengelompokan Koleksi Perpustakaan'

    name = fields.Char(
        string='Jenis Buku'
        )
    deskripsi = fields.Char(
        string='Deskripsi ',
        )
    

    
