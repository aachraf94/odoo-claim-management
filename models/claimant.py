from odoo import models, fields, api # type: ignore

class Claimant(models.Model):
    _name = 'claim.claimant'
    _description = 'Réclamant'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Nom', required=True)
    first_name = fields.Char('Prénom')
    company_name = fields.Char('Raison sociale')
    address = fields.Text('Adresse')
    city = fields.Char('Commune')
    phone = fields.Char('Téléphone')
    email = fields.Char('Email')
    type = fields.Selection([
        ('citizen', 'Citoyen'),
        ('company', 'Entreprise')
    ], string='Type', required=True)
    claim_ids = fields.One2many('claim.claim', 'claimant_id', string='Réclamations')
    active = fields.Boolean('Actif', default=True)