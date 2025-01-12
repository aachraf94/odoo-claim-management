# models/claim.py
from odoo import models, fields, api
from odoo.exceptions import UserError

class Claim(models.Model):
    _name = 'claim.claim'
    _description = 'Claim'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'date desc, id desc'

    name = fields.Char('Reference', required=True, copy=False, readonly=True, default='New')
    date = fields.Date('Date', required=True, default=fields.Date.context_today, tracking=True)
    subject = fields.Char('Subject', required=True, tracking=True)
    description = fields.Text('Description', tracking=True)
    
    claimant_id = fields.Many2one('claim.claimant', string='Claimant', required=True)
    agency_id = fields.Many2one('claim.agency', string='Agency', required=True)
    project_id = fields.Many2one('project.project', string='Related Project')
    
    origin = fields.Selection([
        ('citizen', 'Citizen'),
        ('company', 'Company'),
        ('monitoring', 'Watch Cell')
    ], string='Origin', required=True, tracking=True)
    
    source = fields.Selection([
        ('web', 'Web Form'),
        ('phone', 'Phone Call'),
        ('onsite', 'On Site'),
        ('monitoring', 'Watch Cell')
    ], string='Source', required=True)
    
    type = fields.Selection([
        ('technical', 'Technical'),
        ('commercial', 'Commercial')
    ], string='Type', tracking=True)
    
    urgent = fields.Boolean('Urgent', tracking=True)
    complexity = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ], string='Complexity')
    
    gravity = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ], string='Gravity')
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
        ('archived', 'Archived')
    ], string='Status', default='draft', tracking=True)
    
    customer_service_agent_id = fields.Many2one('hr.employee', string='Customer Service Agent', tracking=True)
    
    attachment_ids = fields.Many2many('ir.attachment', string='Attachments')
    
    # Commercial PV fields
    commercial_pv = fields.Text('Commercial PV')
    commercial_decision = fields.Text('Commercial Decision')
    commercial_pv_date = fields.Date('Commercial PV Date')
    
    # Customer satisfaction fields
    satisfaction_score = fields.Selection([
        ('1', 'Very Unsatisfied'),
        ('2', 'Unsatisfied'),
        ('3', 'Neutral'),
        ('4', 'Satisfied'),
        ('5', 'Very Satisfied')
    ], string='Satisfaction Score')
    satisfaction_comment = fields.Text('Satisfaction Comment')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('claim.claim') or 'New'
        return super(Claim, self).create(vals)

    def action_submit(self):
        self.write({'state': 'submitted'})

    def action_start_processing(self):
        if not self.customer_service_agent_id or not self.type:
            raise UserError('Please assign a customer service agent and define the claim type before starting processing.')
        self.write({'state': 'in_progress'})

    def action_resolve(self):
        self.write({'state': 'resolved'})

    def action_close(self):
        if not self.satisfaction_score:
            raise UserError('Please fill in the satisfaction survey before closing the claim.')
        self.write({'state': 'closed'})

    def action_archive(self):
        self.write({'state': 'archived'})
        
    def action_view_communications(self):
        self.ensure_one()
        return {
            'name': 'Communications',
            'type': 'ir.actions.act_window',
            'res_model': 'claim.communication',
            'view_mode': 'tree,form',
            'domain': [('claim_id', '=', self.id)],
            'context': {'default_claim_id': self.id},
        }