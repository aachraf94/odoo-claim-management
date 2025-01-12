from odoo import models, fields, api

class Employee(models.Model):
    _inherit = 'hr.employee'

    agency_id = fields.Many2one('claim.agency', string='Agency')
    role = fields.Selection([
        ('customer_service', 'Customer Service Agent'),
        ('technician', 'Technician'),
        ('commercial', 'Commercial'),
        ('manager', 'Manager'),
        ('monitoring', 'Watch Cell')
    ], string='Role')