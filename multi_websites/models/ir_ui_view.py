# -*- coding: utf-8 -*-
#################################################################################
#
#    Copyright (c) 2017-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#    You should have received a copy of the License along with this program.
#    If not, see <https://store.webkul.com/license.html/>
#################################################################################

from odoo import fields, models

class IrUiView(models.Model):
	_inherit = 'ir.ui.view'

	multi_theme_created = fields.Boolean(
		name="Generated from multi theme module",
		string="Created Multi View",
		readonly=True,
	)
	active_before = fields.Boolean(
		string="View Active Before"
	)
