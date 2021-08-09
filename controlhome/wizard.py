# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Wizard(models.TransientModel):
    _name = 'controlhome.wizard'

    def _default_name(self):
        return self.env['controlhome.monitoring'].browse(self._context.get('active_ids')).name

    def _default_type(self):
        if len(self.env.context.get('active_ids')) >= 2:
           raise ValidationError("Only can select one item")

        value = self.env['controlhome.monitoring'].browse(self._context.get('active_ids')).type
        return value[0].name


    def _default_state(self):
        return self.env['controlhome.monitoring'].browse(self._context.get('active_ids')).state

    type = fields.Text(string="Type", readonly= 1, default=_default_type)
    name = fields.Text(string="Name", readonly= 1, default=_default_name)
    state = fields.Char(string="State", size=5, readonly= 1, default=_default_state)


    def modify(self):
        if self.state == "On":
            value = "Off"
        elif self.state == "Off":
            value =  "On"
        self.env['controlhome.monitoring'].browse(self._context.get('active_ids')).state = value
        """ *** This a way to do by SQL ***
        query= "update controlhome_monitoring set state='%s' where name='%s'" %(value,self.name)
        cr=self.env.cr
        cr.execute(query) """
        return {}
