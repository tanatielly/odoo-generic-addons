# Copyright 2025 Tanatielly Serafim
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models

class GenderGender(models.Model):
    _name = "gender.gender"

    name = fields.Char(string="Nome", required=True)
    
    is_non_binary = fields.Boolean(string="Não binário?")
    pronoums_ids = fields.One2many(comodel_name="gender.pronoums", inverse_name="gender_id", string="Pronomes")