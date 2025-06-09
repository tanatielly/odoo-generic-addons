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
        "data/gender_pronoums.xml",
        "data/gender_gender.xml",
        "views/school_school.xml",
        "views/school_teacher.xml",
        "views/gender_gender.xml",
        "views/formation_formation.xml",
        "views/teachers_availability.xml",
        "views/gender_pronoums.xml",
        "views/school_student.xml",
    ],
    "auto_install": False,
    "installable": True,
}