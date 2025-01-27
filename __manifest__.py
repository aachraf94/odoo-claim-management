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
    'depends': ['base', 'mail', 'web', 'hr', 'project'],
    'data': [
        'security/claim_security.xml',
        'security/ir.model.access.csv',
        'views/menu_views.xml',
        'views/claim_views.xml',
        'views/claimant_views.xml',
        'views/agency_views.xml',
        'views/communication_views.xml',        
        'views/employee_views.xml',
        'views/project_views.xml',
        # 'report/claim_reports.xml',
        # 'report/claim_report_template.xml',
        'data/claim_sequence.xml',        
    ],
    'demo': [
        'demo/claim_demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'maintainer': '2CS SIT2 TEAM 02 - ESI 2025',
}
