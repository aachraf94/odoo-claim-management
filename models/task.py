from odoo import models, fields, api

class ClaimTask(models.Model):
    _inherit = 'project.task'

    assignees = fields.Many2many('hr.employee', string='Assignees')
    claim_state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('done', 'Done')
    ], string='Status', default='draft')