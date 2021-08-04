# Copyright 2018 Rémy Taymans <remytaymans@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Partner Communication Tag',

    'summary': """
    Let you add tags to a contact to manage your communication
    strategies.
    """,
    'description': """
    """,

    'author': 'Coop IT Easy, Rémy Taymans',
    'license': 'AGPL-3',
    'version': '12.0.1.0',
    'website': "https://coopiteasy.be",

    'category': 'Partner Management',

    'depends': [
        'base',
        'contacts',
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/partner.xml',
        'views/partner_communication_tag.xml',
    ]
}
