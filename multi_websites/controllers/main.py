# -*- coding: utf-8 -*-
#################################################################################
#
#    Copyright (c) 2017-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#    You should have received a copy of the License along with this program.
#    If not, see <https://store.webkul.com/license.html/>
#################################################################################
from odoo import http
from odoo.tools.translate import _
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.addons.web.controllers.main import ensure_db, Home

import logging
_logger = logging.getLogger(__name__)
class WebsiteSale(WebsiteSale):

	@http.route(['/shop/payment'], type='http', auth="public", website=True)
	def payment(self, **post):
		res = super(WebsiteSale, self).payment(**post)
		acquirers = res.qcontext.get('form_acquirers',[])
		deliveries = res.qcontext.get('deliveries',[])
		errors =res.qcontext.get('errors',[])
		website_acquirers = request.website.acquirer_ids
		website_deliveries = request.website.carrier_ids
		res.qcontext['form_acquirers'] =list(filter(lambda ac:ac in website_acquirers,acquirers))
		res.qcontext['deliveries'] =list(filter(lambda dl:dl in website_deliveries,deliveries))
		return res

class AuthSignupHome(Home):

	def do_signup(self, qcontext):
		""" Shared helper that creates a res.partner out of a token """
		values = { key: qcontext.get(key) for key in ('login', 'name', 'password') }
		if not values:
			raise UserError(_("The form was not properly filled in."))
		if values.get('password') != qcontext.get('confirm_password'):
			raise UserError(_("Passwords do not match; please retype them."))
		supported_langs = [lang['code'] for lang in request.env['res.lang'].sudo().search_read([], ['code'])]
		if request.lang in supported_langs:
			values['lang'] = request.lang
		if request.website:
			values['website_ids'] = [(4, request.website.id)]
			values['default_website'] =  request.website.id
			values['company_ids'] =  [(4, request.website.company_id.id)]
			values['company_id'] =  request.website.company_id.id
		self._signup_with_values(qcontext.get('token'), values)
		request.env.cr.commit()
	
	@http.route('/web/login', type='http', auth="none", sitemap=False)
	def web_login(self, redirect=None, **kw):
		response = super(AuthSignupHome, self).web_login(redirect=redirect, **kw)
		if request.website:
			if request.uid:
				user_id = request.env['res.users'].sudo().browse(request.uid)
				user_id.partner_id.website_ids = [(4, request.website.id)]
		return response