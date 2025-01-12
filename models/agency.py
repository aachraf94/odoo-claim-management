from odoo import models, fields, api

class Agency(models.Model):
    _name = 'claim.agency'
    _description = 'Agency'

    name = fields.Char('Name', required=True)
    code = fields.Char('Code', required=True)
    address = fields.Text('Address')
    city = fields.Char('City')
    phone = fields.Char('Phone')
    manager_id = fields.Many2one('hr.employee', string='Agency Manager')
    employee_ids = fields.One2many('hr.employee', 'agency_id', string='Employees')
    active = fields.Boolean('Active', default=True)