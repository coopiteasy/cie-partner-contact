# SPDX-FileCopyrightText: 2026 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

{
    "name": "Partner Social Service",
    "summary": "Extensions for partner useful for social services",
    "version": "18.0.1.0.0",
    "category": "Customer Relationship Management",
    "website": "https://github.com/coopiteasy/cie-partner-contact",
    "author": "Coop IT Easy SC",
    "maintainers": ["mihien"],
    "license": "AGPL-3",
    "depends": [
        "base",
        "contacts",
    ],
    "data": [
        "security/ir.model.access.csv",
        "security/partner_social_service_security.xml",
        "views/partner_social_configuration_views.xml",
        "views/res_partner_views.xml",
    ],
}
