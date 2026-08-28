# SPDX-FileCopyrightText: 2026 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    beneficiary_properties_definition = fields.PropertiesDefinition("beneficiary")
    volunteer_properties_definition = fields.PropertiesDefinition("volunteer")
    partner_properties_definition = fields.PropertiesDefinition("partner")
    benefactor_properties_definition = fields.PropertiesDefinition("benefactor")
