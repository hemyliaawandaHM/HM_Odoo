# -*- coding: utf-8 -*-
# from odoo import http


# class Xperpus(http.Controller):
#     @http.route('/xperpus/xperpus/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/xperpus/xperpus/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('xperpus.listing', {
#             'root': '/xperpus/xperpus',
#             'objects': http.request.env['xperpus.xperpus'].search([]),
#         })

#     @http.route('/xperpus/xperpus/objects/<model("xperpus.xperpus"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('xperpus.object', {
#             'object': obj
#         })
