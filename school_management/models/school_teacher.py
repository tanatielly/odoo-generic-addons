# Copyright 2025 Tanatielly Serafim
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class SchoolTeacher(models.Model):
    _name = "school.teacher"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string="Nome", required=True, tracking=True)
    teacher_id = fields.Many2one(comodel_name="res.partner", string="Profissional")
    birth_date = fields.Date(string="Data de Nascimento")
    cnpj_cpf = fields.Char(string="Documentos")
    gender_ids = fields.Many2many(comodel_name="gender.gender", string="Gênero")
    formation_ids = fields.One2many(comodel_name="formation.formation", inverse_name="teacher_id", string="Formação Acadêmica")
    availability_ids = fields.One2many(comodel_name="teachers.availability", inverse_name="teacher_id", string="Disponibilidade")
