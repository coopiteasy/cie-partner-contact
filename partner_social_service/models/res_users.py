from odoo import api, models


class ResUsers(models.Model):
    _inherit = "res.users"

    @api.model_create_multi
    def create(self, vals_list):
        users = super().create(vals_list)
        group = self.env.ref("partner_social_service.group_portal_social_partner")
        for user in users:
            if user.partner_id.social_type == "social_partner":
                user.sudo().write({"groups_id": [(4, group.id)]})
        return users
