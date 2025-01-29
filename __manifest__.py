{
    'name': 'Claim Management',
    'version': '1.0',
    'category': 'Services',
    'summary': 'Claim management for AlMiyah Djazair',
    'description': """
        Claim management module for the AlMiyah Djazair company, offering the following features:
        - Recording claims (citizens, businesses, monitoring unit)
        - Monitoring and processing claims (commercial or technical)
        - Managing communication with claimants
        - Generating reports and indicators
    """,
    'author': '2CS SIT2 TEAM 02 - ESI 2025',
    'website': 'https://almiyah-djazair.dz',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'mail',
        'web',
        'hr',
        'project'
    ],
    'data': [
        'security/claim_security.xml',
        'security/ir.model.access.csv',
        # Data files first
        'data/claim_sequence.xml',
        'data/mail_template_data.xml',
        # Then reports
        'report/claim_acknowledgment.xml',
        # Finally views
        'views/menu_views.xml',
        'views/claim_views.xml',
        'views/claimant_views.xml',
        'views/agency_views.xml',
        'views/communication_views.xml',        
        'views/employee_views.xml',
        'views/project_views.xml',
    ],
    'demo': [
        'demo/claim_demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}