{
    'name': 'Claim Management',
    'version': '1.0',
    'category': 'Services',
    'summary': 'Gestion des réclamations pour AlMiyah Djazair',
    'description': """
        Module de gestion des réclamations permettant de :
        * Recevoir et enregistrer les réclamations
        * Suivre le traitement des réclamations
        * Gérer la communication avec les réclamants
        * Générer des rapports et indicateurs
    """,
    'depends': ['base', 'mail', 'web'],
    'data': [
        'security/claim_security.xml',
        'security/ir.model.access.csv',
        'views/claim_views.xml',
        'views/claimant_views.xml',
        'views/agency_views.xml',
        'views/employee_views.xml',
        'views/menu_views.xml',
        'report/claim_reports.xml',
        'data/claim_sequence.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
