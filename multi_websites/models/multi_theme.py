# -*- coding: utf-8 -*-
#################################################################################
#
#    Copyright (c) 2017-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#    You should have received a copy of the License along with this program.
#    If not, see <https://store.webkul.com/license.html/>
#################################################################################

from odoo import api, fields, models
import logging
_logger = logging.getLogger(__name__)

class WebsiteMultiTheme(models.Model):
	
	_name = 'website.multi.theme'
	_rec_name = "multi_theme_module"
	
	def _compute_name(self):
		for record in self:
			if record.multi_theme_module:
				record.name = record.multi_theme_module.name
			else:
				record.name = 'Deleted'

	name = fields.Char(
		compute='_compute_name',
		translate=True,
		string="Theme Technical Name",
		
	)
	multi_theme_module = fields.Many2one(
		comodel_name="ir.module.module",
		string="Theme Name",
		help="Theme technical name that will be used as a multi theme",
		required=True,
		domain=[('state','=','installed')],
	)
	multi_theme_asset_ids = fields.One2many(
		comodel_name="website.multi.theme.assets",
		inverse_name="multi_theme_id",
		string="Multi Theme Assets",
	)

	@api.model
	def create(self,vals):
		res = super(WebsiteMultiTheme, self).create(vals)
		if res:
			res._set_multi_theme_assets()
		return res

	@api.multi
	def write(self,vals):
		if vals.get('multi_theme_module'):
			self._set_multi_theme_assets()
		return super(WebsiteMultiTheme,self).write(vals)

	def _set_multi_theme_assets(self):
		Assets_env = self.env["website.multi.theme.assets"]
		for record in self.filtered("multi_theme_module"):
			refs = self.env["ir.model.data"].search([ ("module", "in", [record.multi_theme_module.name]),("model", "=", "ir.ui.view")])
			existing = frozenset(record.mapped("multi_theme_asset_ids.name"))
			expected = frozenset(refs.mapped("complete_name"))
			extra = tuple(existing - expected)
			for ref in expected - existing:
				view = self.env.ref(ref, raise_if_not_found=False)
				if view and view.type != 'qweb':
					continue
				record.multi_theme_asset_ids |= Assets_env.new({"name": ref})
			if extra:
				Assets_env.search([("name", "in", extra)]).unlink()
		Assets_env._make_views_multi_website()


class WebsiteMultiThemeAsset(models.Model):
	_name = "website.multi.theme.assets"

	name = fields.Char(
		name="Reference",
		required=True,
	)
	multi_theme_id = fields.Many2one(
		comodel_name="website.multi.theme",
		string="Theme",
		required=True,
		ondelete="cascade",
	)
	view_id = fields.Many2one(
		comodel_name="ir.ui.view",
		string="Assets view",
		
	)

	@api.model
	def _make_views_multi_website(self):
		views = self.search(["|", ("view_id", "=", False), ("view_id.active", "=", True)])
		for record in views:
			try:
				record.view_id = self.env.ref(record.name)
			except ValueError:
				record.view_id = False
			else:
				if record.view_id.active:
					record.view_id.write({
						"active": False,
						"active_before": True,
					})
		self.env["ir.qweb"]._get_asset_content.clear_cache(self.env["ir.qweb"])