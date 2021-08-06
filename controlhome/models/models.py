# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class TypeElements(models.Model):
    _name = 'controlhome.typeelements'
    _description = 'Table for the type of elements to controlling'

    name = fields.Text()

class Monitoring(models.Model):
    _name = 'controlhome.monitoring'
    _description = 'Show the status of the equipment on home'

    name = fields.Text(string="Name", required=True)
    type = fields.Many2one('controlhome.typeelements', string="Type")
    state = fields.Text(string="State (True/False)", required=True, default="False")
    color = fields.Float()#variable for Kanban view

"""
    @api.onchange('type')
    def _verify_valid_type(self):
        if self.type == " ":
            self.type ="Alarm"
        elif self.type.name != "Alarm" or self.type.name !=  "Device" or self.type.name != "Light" or self.type.name != "Door":
            return {
                    'warning':{
                        'title': "Incorrect TYPE",
                        'message': "The TYPE of the equipments only can be Alarm, Device, Door or Light",
                        }
                    }


    def _select_type(self):
        query= "select distinct type from controlhome_monitoring"
        cr=self.env.cr
        cr.execute(query)
        Data = cr.fetchall()
        for record in Data:
            value = str(record[0])
            #import pdb; pdb.set_trace()
            self.element_types = value
    """
