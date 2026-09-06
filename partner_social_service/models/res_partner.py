# SPDX-FileCopyrightText: 2026 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import api, fields, models
from odoo.osv.expression import SQL_OPERATORS
from odoo.tools.sql import SQL


class ResPartner(models.Model):
    _inherit = "res.partner"

    social_type = fields.Selection(
        [
            ("social_beneficiary", "Beneficiary"),
            ("social_volunteer", "Volunteer"),
            ("social_partner", "Partner"),
            ("social_benefactor", "Benefactor"),
            ("social_other", "Other"),
        ],
        default="social_beneficiary",
    )

    social_beneficiary_ids = fields.Many2many(
        "res.partner",
        "beneficiary_partner_rel",
        "social_partner",
        "social_beneficiary",
        string="Beneficiaries",
    )
    social_partner_ids = fields.Many2many(
        "res.partner",
        "beneficiary_partner_rel",
        "social_beneficiary",
        "social_partner",
        string="Partners",
    )

    creation_date = fields.Date(
        string="File Creation Date",
        required=True,
        default=fields.Date.context_today,
    )

    # The logic on properties used here follows the one done in
    # oca/partner-contact/partner_property
    # The properties are defined on the company
    properties_company_id = fields.Many2one(
        compute="_compute_properties_company_id",
        search="_search_properties_company_id",
        comodel_name="res.company",
    )

    beneficiary_properties = fields.Properties(
        definition="properties_company_id.beneficiary_properties_definition"
    )
    volunteer_properties = fields.Properties(
        definition="properties_company_id.volunteer_properties_definition"
    )
    partner_properties = fields.Properties(
        definition="properties_company_id.partner_properties_definition"
    )
    benefactor_properties = fields.Properties(
        definition="properties_company_id.benefactor_properties_definition"
    )

    @api.depends("company_id")
    @api.depends_context("company")
    def _compute_properties_company_id(self):
        for item in self:
            item.properties_company_id = item.company_id or self.env.company

    def _search_properties_company_id(self, operator, value):
        self.flush_model(["company_id"])
        query = self._where_calc([])
        query.add_where(
            SQL(
                "%s %s %s",
                self._field_to_sql(self._table, "properties_company_id", query),
                SQL_OPERATORS[operator],
                value,
            )
        )
        return [("id", "in", query)]

    def _field_to_sql(self, alias, fname, query=None, flush: bool = True) -> SQL:
        # OVERRIDE to allow to export the properties
        if fname == "properties_company_id":
            return SQL(
                """COALESCE(%(company_column)s, %(env_company)s)""",
                company_column=SQL.identifier(alias, "company_id"),
                env_company=self.env.company.id,
            )
        return super()._field_to_sql(alias, fname, query, flush)

    # When a partner is set to the type partner he's automatically added to the
    # group_portal_social_partner group, and removed from it when set to another type
    def write(self, vals):
        res = super().write(vals)
        if "social_type" in vals:
            group = self.env.ref("partner_social_service.group_portal_social_partner")
            for partner in self:
                if partner.social_type == "social_partner":
                    partner.user_ids.sudo().write({"groups_id": [(4, group.id)]})
                else:
                    partner.user_ids.sudo().write({"groups_id": [(3, group.id)]})
        return res
