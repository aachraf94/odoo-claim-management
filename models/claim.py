from odoo import models, fields, api # type: ignore
from odoo.exceptions import UserError

class Claim(models.Model):
    _name = 'claim.claim'
    _description = 'Réclamation'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'date desc, id desc'

    name = fields.Char('Référence', required=True, copy=False, readonly=True, default='New')
    date = fields.Date('Date', required=True, default=fields.Date.context_today, tracking=True)
    subject = fields.Char('Objet', required=True, tracking=True)
    description = fields.Text('Description', tracking=True)
    
    claimant_id = fields.Many2one('claim.claimant', string='Réclamant', required=True)
    agency_id = fields.Many2one('claim.agency', string='Agence', required=True)
    
    origin = fields.Selection([
        ('citizen', 'Citoyen'),
        ('company', 'Entreprise'),
        ('monitoring', 'Cellule de veille')
    ], string='Origine', required=True, tracking=True)
    
    source = fields.Selection([
        ('web', 'Formulaire Web'),
        ('phone', 'Appel Téléphonique'),
        ('onsite', 'Sur Site'),
        ('monitoring', 'Cellule de veille')
    ], string='Source', required=True)
    
    type = fields.Selection([
        ('technical', 'Technique'),
        ('commercial', 'Commercial')
    ], string='Type', tracking=True)
    
    urgent = fields.Boolean('Urgente', tracking=True)
    complexity = fields.Selection([
        ('low', 'Faible'),
        ('medium', 'Moyenne'),
        ('high', 'Élevée')
    ], string='Complexité')
    
    gravity = fields.Selection([
        ('low', 'Faible'),
        ('medium', 'Moyenne'),
        ('high', 'Élevée')
    ], string='Gravité')
    
    state = fields.Selection([
        ('draft', 'Brouillon'),
        ('submitted', 'Soumise'),
        ('in_progress', 'En cours'),
        ('resolved', 'Résolue'),
        ('closed', 'Clôturée'),
        ('archived', 'Archivée')
    ], string='État', default='draft', tracking=True)
    
    customer_service_agent_id = fields.Many2one('claim.employee', string='Agent Clientèle', tracking=True)
    team_ids = fields.Many2many('claim.employee', string='Équipe d\'intervention')
    team_leader_id = fields.Many2one('claim.employee', string='Chef d\'équipe')
    
    attachment_ids = fields.Many2many('ir.attachment', string='Pièces jointes')
    
    # Champs pour le PV commercial
    commercial_pv = fields.Text('PV Commercial')
    commercial_decision = fields.Text('Décision Commerciale')
    commercial_pv_date = fields.Date('Date PV Commercial')
    
    # Champs pour les interventions techniques
    intervention_ids = fields.One2many('claim.technical.intervention', 'claim_id', string='Interventions')
    
    # Champs pour la satisfaction client
    satisfaction_score = fields.Selection([
        ('1', 'Très insatisfait'),
        ('2', 'Insatisfait'),
        ('3', 'Neutre'),
        ('4', 'Satisfait'),
        ('5', 'Très satisfait')
    ], string='Score de satisfaction')
    satisfaction_comment = fields.Text('Commentaire satisfaction')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('claim.claim') or 'New'
        return super(Claim, self).create(vals)

    def action_submit(self):
        self.write({'state': 'submitted'})

    def action_start_processing(self):
        if not self.customer_service_agent_id or not self.type:
            raise UserError('Veuillez assigner un agent clientèle et définir le type de réclamation avant de commencer le traitement.')
        self.write({'state': 'in_progress'})

    def action_resolve(self):
        self.write({'state': 'resolved'})

    def action_close(self):
        if not self.satisfaction_score:
            raise UserError('Veuillez remplir le questionnaire de satisfaction avant de clôturer la réclamation.')
        self.write({'state': 'closed'})

    def action_archive(self):
        self.write({'state': 'archived'})