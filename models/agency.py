from odoo import models, fields, api # type: ignore

class Agency(models.Model):
    _name = 'claim.agency'
    _description = 'Agence'

    name = fields.Char('Nom', required=True)
    code = fields.Char('Code', required=True)
    address = fields.Text('Adresse')
    city = fields.Char('Commune')
    phone = fields.Char('Téléphone')
    manager_id = fields.Many2one('claim.employee', string='Responsable')
    employee_ids = fields.One2many('claim.employee', 'agency_id', string='Employés')
    active = fields.Boolean('Active', default=True)