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
            ("accompagner", "Accompagner"),
            ("beneficiary", "Beneficiary"),
            ("partner", "Partner"),
            ("other", "Other"),
        ],
        default="beneficiary",
    )
    is_social_benefactor = fields.Boolean("Benefactor")
    is_social_employee = fields.Boolean("Employee")
    is_social_volunteer = fields.Boolean("Volunteer")

    social_beneficiary_ids = fields.Many2many(
        "res.partner",
        "beneficiary_partner_rel",
        "social_partner",
        "social_beneficiary",
        string="Beneficiaries",
        domain=[("social_type", "=", "beneficiary")],
    )
    social_partner_ids = fields.Many2many(
        "res.partner",
        "beneficiary_partner_rel",
        "social_beneficiary",
        "social_partner",
        string="Partners",
        domain=[("social_type", "=", "partner")],
    )

    social_file_creation_date = fields.Date(
        string="File Creation Date",
        required=True,
        default=fields.Date.context_today,
    )

    # The logic on properties used here follows the one done in
    # oca/partner-contact/partner_property
    # The properties are defined on the company
    social_properties_company_id = fields.Many2one(
        compute="_compute_social_properties_company_id",
        search="_search_social_properties_company_id",
        comodel_name="res.company",
    )

    social_beneficiary_properties = fields.Properties(
        definition="social_properties_company_id.partner_properties_definition_social_beneficiary"
    )
    social_volunteer_properties = fields.Properties(
        definition="social_properties_company_id.partner_properties_definition_social_volunteer"
    )
    social_partner_properties = fields.Properties(
        definition="social_properties_company_id.partner_properties_definition_social_partner"
    )
    social_benefactor_properties = fields.Properties(
        definition="social_properties_company_id.partner_properties_definition_social_benefactor"
    )

    @api.depends("company_id")
    @api.depends_context("company")
    def _compute_social_properties_company_id(self):
        for item in self:
            item.social_properties_company_id = item.company_id or self.env.company

    def _search_social_properties_company_id(self, operator, value):
        self.flush_model(["company_id"])
        query = self._where_calc([])
        query.add_where(
            SQL(
                "%s %s %s",
                self._field_to_sql(self._table, "social_properties_company_id", query),
                SQL_OPERATORS[operator],
                value,
            )
        )
        return [("id", "in", query)]

    def _field_to_sql(self, alias, fname, query=None, flush: bool = True) -> SQL:
        # OVERRIDE to allow to export the properties
        if fname == "social_properties_company_id":
            return SQL(
                """COALESCE(%(company_column)s, %(env_company)s)""",
                company_column=SQL.identifier(alias, "company_id"),
                env_company=self.env.company.id,
            )
        return super()._field_to_sql(alias, fname, query, flush)

    def write(self, vals):
        res = super().write(vals)
        if "social_type" in vals:
            group = self.env.ref("partner_social_service.group_portal_social_partner")
            for partner in self:
                if partner.social_type == "partner":
                    partner.user_ids.sudo().write({"groups_id": [(4, group.id)]})
                else:
                    partner.user_ids.sudo().write({"groups_id": [(3, group.id)]})
        return res
