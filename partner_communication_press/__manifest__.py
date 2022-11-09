# Copyright 2018 Rémy Taymans <remytaymans@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Partner Communication Press",
    "summary": """
    Add information in your contacts to know if you need to send
    advertising to your contacts and which type of advertising.
    """,
    "author": "Coop IT Easy SCRLfs",
    "license": "AGPL-3",
    "version": "12.0.1.0.0",
    "website": "https://github.com/coopiteasy/cie-partner-contact",
    "category": "Partner Management",
    "depends": [
        "base",
        "contacts",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/partner.xml",
        "views/partner_communication_press.xml",
    ],
}
