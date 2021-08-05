# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Wizard(models.TransientModel):
    _name = 'controlhome.wizard'



    type = fields.Many2many('controlhome.monitoring',string="Name")
    name = fields.Text(string="Name", compute='_default_monitoring')
    state = fields.Text(string="State")

    def _default_monitoring(self):
        monitoring_obj = self.env['controlhome.monitoring']
        monitoring_id = self._context.get('active_id')
        monitoring_record = session_obj.browse(monitoring_id)
        import pdb; pdb.set_trace()
        return monitoring_record

"""
    def subscribe(self):
        #for session in self.session_ids:
            session.attendee_ids |= self.attendee_ids
        return {}
    """
