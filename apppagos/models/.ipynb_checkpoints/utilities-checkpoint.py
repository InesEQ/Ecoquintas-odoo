#from odoo import models, fields, api
import requests

class utilities():
    
    def request_api():
        x = requests.get('http://181.193.143.38:5050/')
        return x.text