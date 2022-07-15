# -*- coding: utf-8 -*-

from odoo import models, fields, api


class eco_libs(models.Model):
    _name = 'eco_libs.eco_libs'
    _description = 'eco_libs.eco_libs'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

    def consulta(self, data):
        url = "http://181.193.143.38:5050/odoo/test"
        headers = {"Content-Type": "application/json; charset=utf-8", "token": '3e26b17c-3e96-40d6-91fa-7f355bf2c570'}
        response = requests.post(url, headers=headers, json=data)
        return response.status_code
