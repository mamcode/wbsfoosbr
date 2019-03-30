# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
from odoo.addons.website_blog.controllers.main import WebsiteBlog

class WebsiteBlog(WebsiteBlog):

	@http.route(['/blog/get_blog_content'], type='http', auth='public', website=True)
	def get_blog_content_data(self, **post):
		value={}
		if post.get('blog_config_id')!='false':
			collection_data=request.env['blog.configure'].browse(int(post.get('blog_config_id')))
			value.update({'blog_slider':collection_data})
		return request.render("theme_stoneware.blog_slider_content", value)

