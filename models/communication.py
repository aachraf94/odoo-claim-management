from odoo import models, fields, api

class CustomerCommunication(models.Model):
    _name = 'claim.communication'
    _description = 'Customer Communication'
    _order = 'date desc'

    claim_id = fields.Many2one('claim.claim', string='Claim', required=True)
    date = fields.Datetime(string='Communication Date', default=fields.Datetime.now)
    agent_id = fields.Many2one('hr.employee', string='Customer Service Agent')
    communication_type = fields.Selection([
        ('outbound', 'Outbound Call'),
        ('inbound', 'Inbound Call'),
        ('update', 'Status Update')
    ], string='Communication Type')
    notes = fields.Text(string='Communication Notes')