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

    @api.model
    def create(self, values):
        if 'name' in values:
            values['description'] += ' Create'
        return super(my_module, self).create(values)

    def write(self, values):
        if 'id' in values:
            values['description'] += ' Write'
        return super(my_module, self).write(values)
    
    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
            x = requests.get('http://181.193.143.38:5050/')
            record.description = x.text
            