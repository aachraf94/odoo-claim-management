from odoo import models, fields, api # type: ignore

#  ----------------------> changement : to delete and use projet and tasks from project module

class TechnicalIntervention(models.Model):
    _name = 'claim.technical.intervention'
    _description = 'Intervention Technique'
    _order = 'date desc'

    claim_id = fields.Many2one('claim.claim', string='Réclamation', required=True)
    date = fields.Date('Date', required=True, default=fields.Date.context_today)
    description = fields.Text('Description des actions réalisées', required=True)
    team_member_ids = fields.Many2many('claim.employee', string='Membres de l\'équipe')
    location = fields.Char('Lieu d\'intervention')
    duration = fields.Float('Durée (heures)')
    state = fields.Selection([
        ('planned', 'Planifiée'),
        ('in_progress', 'En cours'),
        ('done', 'Terminée')
    ], string='État', default='planned')
