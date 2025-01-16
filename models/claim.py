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
    
    # Make these fields not required by default
    claimant_id = fields.Many2one('claim.claimant', string='Claimant', tracking=True)
    agency_id = fields.Many2one('claim.agency', string='Agency', tracking=True)
    project_id = fields.Many2one('project.project', string='Related Project')
    
    origin = fields.Selection([
        ('citizen', 'Citizen'),
        ('company', 'Company'),
        ('monitoring', 'Watch Cell')
    ], string='Origin', tracking=True, default='citizen')
    
    source = fields.Selection([
        ('web', 'Web Form'),
        ('phone', 'Phone Call'),
        ('onsite', 'On Site'),
        ('monitoring', 'Watch Cell')
    ], string='Source', default='web')
    
    type = fields.Selection([
        ('technical', 'Technical'),
        ('commercial', 'Commercial')
    ], string='Type', tracking=True, default='technical')
    
    priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ], string='Priority', default='medium', tracking=True) 
    
    urgent = fields.Boolean('Urgent', tracking=True, default=False)
    complexity = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ], string='Complexity', default='medium')
    
    gravity = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ], string='Gravity', default='medium')
    
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
    
    commercial_pv = fields.Text('Commercial PV')
    commercial_decision = fields.Text('Commercial Decision')
    commercial_pv_date = fields.Date('Commercial PV Date')
    
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
        for record in self:
            if not record.claimant_id or not record.agency_id:
                raise UserError('Please fill in the Claimant and Agency fields before submitting.')
            record.write({'state': 'submitted'})

    def action_start_processing(self):
        for record in self:
            if not record.customer_service_agent_id or not record.type:
                raise UserError('Please assign a customer service agent and define the claim type before starting processing.')
            record.write({'state': 'in_progress'})

    def action_resolve(self):
        self.write({'state': 'resolved'})

    def action_close(self):
        for record in self:
            if not record.satisfaction_score:
                raise UserError('Please fill in the satisfaction survey before closing the claim.')
            record.write({'state': 'closed'})

    def action_archive(self):
        self.write({'state': 'archived'})

    @api.onchange('type')
    def _onchange_type(self):
        # Clear commercial fields if type is not commercial
        if self.type != 'commercial':
            self.commercial_pv = False
            self.commercial_decision = False
            self.commercial_pv_date = False