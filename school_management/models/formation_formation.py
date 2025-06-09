# Copyright 2025 Tanatielly Serafim
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models

class FormationFormation(models.Model):
    _name = "formation.formation"

    name = fields.Char(string="Nome", required=True)
    teacher_id = fields.Many2one(comodel_name="school.teacher")
