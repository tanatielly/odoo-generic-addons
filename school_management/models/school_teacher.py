# Copyright 2025 Tanatielly Serafim
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class SchoolTeacher(models.Model):
    _name = "school.teacher"

    name = fields.Char(string="Nome")
    teacher_id = fields.Many2one(comodel_name="res.partner", string="Profissional")
    birth_date = fields.Date(string="Data de Nascimento")
    cnpj_cpf = fields.Char(string="Documentos")


#   gender_id = fields.One2many(string="Genero")
#   formation = fields.One2many(string="Formacao")
#   availability = fields.One2many(string="Disponibilidade")
