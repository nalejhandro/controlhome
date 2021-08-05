# -*- coding: utf-8 -*-
# from odoo import http


# class Controlhome(http.Controller):
#     @http.route('/controlhome/controlhome/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/controlhome/controlhome/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('controlhome.listing', {
#             'root': '/controlhome/controlhome',
#             'objects': http.request.env['controlhome.controlhome'].search([]),
#         })

#     @http.route('/controlhome/controlhome/objects/<model("controlhome.controlhome"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('controlhome.object', {
#             'object': obj
#         })
