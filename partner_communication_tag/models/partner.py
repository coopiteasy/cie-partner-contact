# Copyright 2018 Rémy Taymans <remytaymans@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).


from odoo import fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    communication_tag_ids = fields.Many2many(
        "res.partner.communication.tag", string="Communication"
    )
