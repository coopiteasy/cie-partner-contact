# SPDX-FileCopyrightText: 2026 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    social_type = fields.Selection(
        [
            ("accompagner", "Accompagner"),
            ("beneficiary", "Beneficiary"),
            ("partner", "Partner"),
        ],
        default="beneficiary",
    )

    is_social_benefactor = fields.Boolean("Benefactor")
    is_social_employee = fields.Boolean("Employee")
    is_social_volunteer = fields.Boolean("Volunteer")
