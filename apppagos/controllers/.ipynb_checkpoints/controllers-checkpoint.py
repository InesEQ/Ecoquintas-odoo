# -*- coding: utf-8 -*-
from odoo import http


class Apppagos(http.Controller):
    @http.route('/apppagos/apppagos/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/apppagos/apppagos/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('apppagos.listing', {
            'root': '/apppagos/apppagos',
            'objects': http.request.env['apppagos.apppagos'].search([]),
         })

    @http.route('/apppagos/apppagos/objects/<model("apppagos.apppagos"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('apppagos.object', {
            'object': obj
        })
