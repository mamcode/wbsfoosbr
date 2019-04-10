# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class MRP(models.Model):
  _inherit = 'mrp.production'
  
  @api.model
  def read_group(self, domain, fields, groupby, offset=0, limit=None, orderby=False, lazy=True):
      if groupby and groupby[0] == "state":
        states = [
            ('confirmed', 'Confirmed'),
            ('planned', 'Planned'),
            ('progress', 'In Progress'),
            ('done', 'Done'),
            ('cancel', 'Cancelled')
        ]
        read_group_all_states = [{
            '__context': {'group_by': groupby[1:]},
            '__domain': domain + [('state', '=', state_value)],
            'state': state_value,
            'state_count': 0,
        } for state_value, state_name in states]
        # Get standard results
        read_group_res = super(MRP, self).read_group(domain, fields, groupby, offset=offset, limit=limit, orderby=orderby)
        # Update standard results with default results
        result = []
        for state_value, state_name in states:
            res = []
            for i in read_group_res:
                if i['state'] == state_value:
                    res.append(i)
            if not res:
                for i in read_group_all_states:
                    if i['state'] == state_value:
                        res.append(i)
            res[0]['state'] = state_value#[state_value, state_name]
            result.append(res[0])
        return result
      else:
        return super(MRP, self).read_group(domain, fields, groupby, offset=offset, limit=limit, orderby=orderby)