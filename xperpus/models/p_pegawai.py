from odoo import api, fields, models


class Pegawai (models.Model):
    _name = 'perpus.pegawai'
    _description = 'Pegawai perpustakaan'

    name = fields.Char(
        string='Name')
    alamat = fields.Char(
        string='Alamat')
    no_tlp = fields.Char(
        string='Telepon/HP')