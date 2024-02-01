# -*- coding: utf-8 -*-

from odoo import models, fields, api


class categoria(models.Model):
    _name = 'llibreria.categoria'
    _description = 'llibreria.llibreria'

    name = fields.Char(required=True, help="Introduïx el nom de la categoria")
    description = fields.Text()
