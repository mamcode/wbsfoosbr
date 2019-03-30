# -*- coding: utf-8 -*-
#################################################################################
#
#    Copyright (c) 2018-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#
#################################################################################
from odoo import models, fields, api, _

class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    @api.multi
    def _create_invoice(self, order, so_line, amount):
        invocie  =  super(SaleAdvancePaymentInv, self)._create_invoice(order, so_line, amount)
        if invocie and order and order.wk_website_id:
            invocie.wk_website_id = order.wk_website_id.id
        return invocie
            