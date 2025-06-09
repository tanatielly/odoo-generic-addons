# Copyright 2025 Tanatielly Serafim
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models

#TODO boletim, laudo?, 

class SchoolStudent(models.Model):
    _name = "school.student"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string="Nome", required=True, tracking=True)
    student_id = fields.Many2one(comodel_name="res.partner", string="Estudante")
    student_intern_register = fields.Char(string="RA")
    birth_date= fields.Date(string="Data de nascimento")
    cnpj_cpf = fields.Char(string="Documentos")
    gender_ids = fields.Many2many(comodel_name="gender.gender", string="Genero")
    mother_id = fields.Many2one(comodel_name="res.partner", string="Nome da mae")
    mother_contact_info = fields.Char(string="Numero de contato", related="mother_id.phone")
    father_id = fields.Many2one(comodel_name="res.partner", string="Nome do pai")
    father_contact_info = fields.Char(string="Numero de contato", related="father_id.phone")