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
        """Opens the related claim form view"""
        self.ensure_one()
        if not self.claim_id:
            return

        return {
            'type': 'ir.actions.act_window',
            'name': 'Claim',
            'res_model': 'claim.claim',
            'res_id': self.claim_id.id,
            'view_mode': 'form',
            'target': 'current',
        }