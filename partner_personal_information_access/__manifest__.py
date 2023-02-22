# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Personal Information Access",
    "summary": "This module restricts access to personal "
    "fields to users of group 'Access to Private Addresses'.",
    "version": "12.0.1.0.0",
    "category": "Customer Relationship Management",
    "website": "https://github.com/coopiteasy/cie-partner-contact",
    "author": "Coop IT Easy SC",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "base",
        "mail",
    ],
    "data": [
        "views/res_partner_forms.xml",
        "views/res_partner_kanbans.xml",
        "views/res_partner_trees.xml",
    ],
}
