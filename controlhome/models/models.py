# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)

class TypeElements(models.Model):
    _name = 'controlhome.typeelements'
    _description = 'Table for the type of elements to controlling'

    name = fields.Text()

class Monitoring(models.Model):
    _name = 'controlhome.monitoring'
    _description = 'Show the status of the equipment on home'

    name = fields.Char(string="Name", size=10, required=True)
    type = fields.Many2one('controlhome.typeelements', string="Type")
    state = fields.Char(string="State (On/Off)", size=3, required=True, default="Off")
    color = fields.Float()#variable for Kanban view


    _sql_constraints = [
            ('name_unique',
                'UNIQUE(name)',
               _("This name was used by other equipment") ),
            ]


    def modify_state(self):
        if self.state == "On":
            value = "Off"
        elif self.state == "Off":
            value =  "On"
        self.state = value

    @api.constrains('state')
    def _check_type(self):
        if self.state != 'On' and self.state != 'Off':
            raise ValidationError("The value of State only can be On or Off")
