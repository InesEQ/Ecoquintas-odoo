# -*- coding: utf-8 -*-
from odoo import http


class EcoLibs(http.Controller):
    @http.route('/eco_libs/eco_libs/', auth='public')
    
    def index(self, **kw):
        return "Hello, world"
    @http.route('/eco_libs/eco_libs/objects/', auth='public')
    
    def list(self, **kw):
        return http.request.render('eco_libs.listing', {
            'root': '/eco_libs/eco_libs',
            'objects': http.request.env['eco_libs.eco_libs'].search([]),
        })
    @http.route('/eco_libs/eco_libs/objects/<model("eco_libs.eco_libs"):obj>/', auth='public')

    def object(self, obj, **kw):
        return http.request.render('eco_libs.object', {
            'object': obj
        })
