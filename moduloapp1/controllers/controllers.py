# -*- coding: utf-8 -*-
# from odoo import http


# class ../user/moduloapp1(http.Controller):
#     @http.route('/../user/moduloapp1/../user/moduloapp1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/../user/moduloapp1/../user/moduloapp1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('../user/moduloapp1.listing', {
#             'root': '/../user/moduloapp1/../user/moduloapp1',
#             'objects': http.request.env['../user/moduloapp1.../user/moduloapp1'].search([]),
#         })

#     @http.route('/../user/moduloapp1/../user/moduloapp1/objects/<model("../user/moduloapp1.../user/moduloapp1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('../user/moduloapp1.object', {
#             'object': obj
#         })
