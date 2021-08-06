# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Wizard(models.TransientModel):
    _name = 'controlhome.wizard'

    def _default_name(self):
        return self.env['controlhome.monitoring'].browse(self._context.get('active_ids')).name

    def _default_type(self):
        for record in self.env['controlhome.monitoring'].browse(self._context.get('active_ids')).type:
            value = record[0].name
        return value

    def _default_state(self):
        return self.env['controlhome.monitoring'].browse(self._context.get('active_ids')).state

    type = fields.Text(string="Type", readonly= 1, default=_default_type)
    name = fields.Text(string="Name", readonly= 1, default=_default_name)
    state = fields.Char(string="State", size=5, default=_default_state)

    def modify(self):
        query= "update controlhome_monitoring set state='%s' where name='%s'" %(self.state,self.name)
        cr=self.env.cr
        cr.execute(query)
        #import pdb; pdb.set_trace()
        return {}
