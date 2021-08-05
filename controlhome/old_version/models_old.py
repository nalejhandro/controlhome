# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class TypeElements(models.Model):
    _name = 'controlhome.typeelements'
    _description = 'Table for the type of elements to controlling'

    name = fields.Text()
    #qty =  fields.Text(string="Qty", compute='_type_qty', domain=[('qty','>','0')])


    def _type_qty(self):
        for record in self:
            query= "select count(type) from controlhome_monitoring where type=%s" % record.id
            cr=self.env.cr
            cr.execute(query)
            Data = cr.fetchone()
            record.qty = int(Data[0])

class Monitoring(models.Model):
    _name = 'controlhome.monitoring'
    _description = 'Show the status of the equipment on home'

    #element_types = fields.Text(string="Equipments in Control", compute='_select_type')

    name = fields.Text(string="Name", required=True)
    type = fields.Many2one('controlhome.typeelements', string="Type")
    state = fields.Text(string="State (True/False)", required=True)

    """
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
