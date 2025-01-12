from odoo import models, fields, api # type: ignore

class Employee(models.Model):
    _name = 'claim.employee'
    _description = 'Employé'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Nom', required=True)
    first_name = fields.Char('Prénom')
    role = fields.Selection([
        ('customer_service', 'Agent Clientèle'),
        ('technician', 'Technicien'),
        ('commercial', 'Commercial'),
        ('manager', 'Responsable'),
        ('monitoring', 'Cellule de veille')
    ], string='Rôle', required=True)
    agency_id = fields.Many2one('claim.agency', string='Agence')
    phone = fields.Char('Téléphone')
    email = fields.Char('Email')
    active = fields.Boolean('Actif', default=True)