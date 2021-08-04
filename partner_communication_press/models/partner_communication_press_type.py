# Copyright 2018 Rémy Taymans <remytaymans@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).


from odoo import models, fields


class PartnerCommunicationPressType(models.Model):
    _name = 'res.partner.communication.press.type'
    _description = "Partner Communication Press Type"
    _order = 'name'

    name = fields.Char("Name", required=True)
    partner_ids = fields.Many2many('res.partner',
                                   string="Partners")
    active = fields.Boolean("Active", default=True)
