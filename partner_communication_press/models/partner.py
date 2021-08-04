# Copyright 2018 Rémy Taymans <remytaymans@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).


from odoo import api, models, fields


class Partner(models.Model):
    _inherit = 'res.partner'

    communication_press = fields.Boolean("Press ?")
    communication_press_type_ids = fields.Many2many(
        'res.partner.communication.press.type',
        string="Press Type"
    )

    @api.multi
    def write(self, vals):
        for rec in self:
            if 'communication_press' in vals:
                if not vals['communication_press']:
                    # Empty all communication_press_type
                    vals['communication_press_type_ids'] = [(5,)]
        return super(Partner, self).write(vals)
