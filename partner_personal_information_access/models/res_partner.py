# Copyright 2023 Coop IT Easy SC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def get_private_fields(self):
        if not self.env.user.has_group("base.group_private_addresses"):
            fields = [
                "email",
                "mobile",
                "phone",
                "street",
                "street2",
                "city",
                "state_id",
                "zip",
                "country_id",
            ]
        else:
            fields = []
        return fields

    @api.model
    def fields_get(self, allfields=None, attributes=None):
        res = super(ResPartner, self).fields_get()
        fields_to_hide = self.get_private_fields()
        for field in fields_to_hide:
            # hide from custom search
            res[field]["searchable"] = False
            # hide from group by selection
            res[field]["sortable"] = False
        return res
