# -*- coding: utf-8 -*-
from odoo import api, fields, models,tools
from odoo.exceptions import UserError
from odoo.tools.translate import _
import base64
import os
import logging
import csv
from tempfile import TemporaryFile

_logger = logging.getLogger(__name__)

class StockPicking(models.Model):   
	_inherit = "stock.production.lot"
	
	origin = fields.Char()