# Copyright 2018 Robin Keunen <robin@keunen.net>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).


from odoo import fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    is_bilingual = fields.Boolean(string="Bilingual", default=False)
