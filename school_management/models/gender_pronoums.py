# Copyright 2025 Tanatielly Serafim
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models

class GenderPronoums(models.Model):
    _name = "gender.pronoums"

    name = fields.Char(string="Nome", required=True)
    gender_id = fields.Many2one(comodel_name="gender.gender")