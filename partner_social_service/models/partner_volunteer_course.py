# SPDX-FileCopyrightText: 2026 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import fields, models


class PartnerSocialVolunteerCourse(models.Model):
    _name = "partner.social.volunteer.course"
    _description = "Volunteer Course Line"
    _order = "date desc"

    partner_id = fields.Many2one(
        "res.partner",
        required=True,
        ondelete="cascade",
    )
    date = fields.Date()
    volunteer_type_id = fields.Many2one("partner.social.volunteer.type")
    reason = fields.Char()
