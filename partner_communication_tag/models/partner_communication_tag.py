# Copyright 2018 Rémy Taymans <remytaymans@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).


from odoo import models, fields


class PartnerCommunicationTag(models.Model):
    _name = 'res.partner.communication.tag'
    _description = "Partner Communication Tag"
    _order = 'name'

    name = fields.Char("Name", required=True)
    description = fields.Text("Description")
    partner_ids = fields.Many2many('res.partner', string="Partners")
    active = fields.Boolean("Active", default=True)
