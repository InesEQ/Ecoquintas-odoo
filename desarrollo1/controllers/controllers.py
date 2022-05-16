# -*- coding: utf-8 -*-
 from odoo import http


 class Desarrollo1(http.Controller):
     @http.route('/desarrollo1/desarrollo1/', auth='public')
     def index(self, **kw):
         return "Hello, world"

     @http.route('/desarrollo1/desarrollo1/objects/', auth='public')
     def list(self, **kw):
         return http.request.render('desarrollo1.listing', {
             'root': '/desarrollo1/desarrollo1',
             'objects': http.request.env['desarrollo1.desarrollo1'].search([]),
         })

     @http.route('/desarrollo1/desarrollo1/objects/<model("desarrollo1.desarrollo1"):obj>/', auth='public')
     def object(self, obj, **kw):
         return http.request.render('desarrollo1.object', {
             'object': obj
         })
