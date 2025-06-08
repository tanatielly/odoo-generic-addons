# Copyright 2025 Tanatielly Serafim
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "School Management",
    "version": "14.0.1.0.0",
    "author": "Tanatielly Serafim",
    "license": "AGPL-3",
    "website": "https://github.com/tanatielly/odoo-generic-addons",
    "depends": ["contacts"],
    "data": [
        "security/ir.model.access.csv",
        "views/school_school.xml",
        "views/school_teacher.xml",
    ],
    "auto_install": False,
    "installable": True,
}