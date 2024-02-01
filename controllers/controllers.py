# -*- coding: utf-8 -*-
# from odoo import http


# class Llibreria(http.Controller):
#     @http.route('/llibreria/llibreria', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/llibreria/llibreria/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('llibreria.listing', {
#             'root': '/llibreria/llibreria',
#             'objects': http.request.env['llibreria.llibreria'].search([]),
#         })

#     @http.route('/llibreria/llibreria/objects/<model("llibreria.llibreria"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('llibreria.object', {
#             'object': obj
#         })
