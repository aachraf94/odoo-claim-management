from odoo import models, fields, api

class ClaimProject(models.Model):
    _inherit = 'project.project'

    claim_id = fields.Many2one('claim.claim', string='Related Claim')
    members = fields.Many2many('hr.employee', string='Members')
    claim_type = fields.Selection([
        ('commercial', 'Commercial'),
        ('technical', 'Technical')
    ], string='Claim Type')

    def action_view_claim(self):
        self.ensure_one()
        return {
            'name': 'Claim',
            'type': 'ir.actions.act_window',
            'res_model': 'claim.claim',
            'view_mode': 'form',
            'res_id': self.claim_id.id,
            'target': 'current',
        }