from odoo import models, fields, api

class Claimant(models.Model):
    _name = 'claim.claimant'
    _description = 'Claimant'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Name', required=True)
    first_name = fields.Char('First Name')
    company_name = fields.Char('Company Name')
    address = fields.Text('Address')
    city = fields.Char('City')
    phone = fields.Char('Phone')
    email = fields.Char('Email')
    type = fields.Selection([
        ('citizen', 'Citizen'),
        ('company', 'Company')
    ], string='Type', required=True)
    claim_ids = fields.One2many('claim.claim', 'claimant_id', string='Claims')
    active = fields.Boolean('Active', default=True)
    additional_info = fields.Text('Additional Information')