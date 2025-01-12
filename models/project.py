from odoo import models, fields, api

class ClaimProject(models.Model):
    _inherit = 'project.project'

    claim_id = fields.Many2one('claim.claim', string='Related Claim')
    claim_type = fields.Selection([
        ('commercial', 'Commercial'),
        ('technical', 'Technical')
    ], string='Claim Type')
