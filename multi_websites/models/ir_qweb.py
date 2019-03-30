# -*- coding: utf-8 -*-
#################################################################################
#
#    Copyright (c) 2017-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#    You should have received a copy of the License along with this program.
#    If not, see <https://store.webkul.com/license.html/>
#################################################################################
from odoo import models
from .website import MULTI_ASSETS
import logging
_logger = logging.getLogger(__name__)
class IrQweb(models.AbstractModel):
    _inherit = 'ir.qweb'

    def _get_asset(self, xmlid, *args, **kwargs):
        website_id = self.env.context.get("website_id")
        if xmlid == "web.assets_frontend" and website_id:
            alt_xmlid = MULTI_ASSETS % website_id
            if self.env.ref(alt_xmlid, False):
                xmlid = alt_xmlid
        return super(IrQweb, self)._get_asset(xmlid, *args, **kwargs)
