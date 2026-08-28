# SPDX-FileCopyrightText: 2026 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    contact_type = fields.Selection(
        [
            ("beneficiary", "Beneficiary"),
            ("volunteer", "Volunteer"),
            ("partner", "Partner"),
            ("benefactor", "Benefactor"),
            ("other", "Other"),
        ],
        default="beneficiary",
    )

    creation_date = fields.Date(
        string="File Creation Date",
        required=True,
        default=fields.Date.context_today,
    )
