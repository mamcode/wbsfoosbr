# -*- coding: utf-8 -*-
import logging
import pprint
import werkzeug

from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)


class PagseguroController(http.Controller):
    _accept_url = '/payment/pagseguro/feedback'

    @http.route([
        '/payment/pagseguro/feedback',
    ], type='http', auth='none', csrf=False)
    def pagseguro_form_feedback(self, **post):
        _logger.info('Beginning form_feedback with post data %s', pprint.pformat(post))  # debug
        request.env['payment.transaction'].sudo().form_feedback(post, 'pagseguro')
        return werkzeug.utils.redirect(post.pop('return_url', '/'))
