# -*- coding: utf-8 -*-

from odoo import models, fields, api
import requests

class apppagos(models.Model):
    _name = 'apppagos.apppagos'
    _description = 'apppagos.apppagos'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    
    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
            
    def consulta(self):
        var=requests.get("https://181.193.143.38:5050/")
        print(var.text)