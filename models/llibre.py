# -*- coding: utf-8 -*-

from odoo import models, fields, api


class llibre(models.Model):
    _name = 'llibreria.llibre'
    _description = 'llibreria.llibre'

    nom = fields.Char(required=True)
    preu = fields.Float()
    exemplars = fields.Integer()
    rotura_estoc = fields.Boolean(compute="_compute_rotura", store=True)
    data = fields.Date()
    segonama = fields.Boolean()
    estat = fields.Selection(
        'Bo',
        'Regular',
        'Dolent',
        default='Bo'
    )

    @api.depends('rotura_estoc')
    def _compute_rotura(self):
        for record in self:
            record.rotura_estoc = record.exemplars < 10
