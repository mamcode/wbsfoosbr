# -*- coding: utf-8 -*-
#################################################################################
# Author      : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2015-Present Webkul Software Pvt. Ltd.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://store.webkul.com/license.html/>
#################################################################################
{
  "name"                 :  "Odoo Multi Website",
  "summary"              :  "Set Multi-Company, Multi-Warehouse, Multi-Theme, Multi-ecommerce in a single database",
  "description"          :  "Set Multi-Company, Multi-Warehouse, Multi-Theme, Multi-ecommerce in a single database",
  "category"             :  "website",
  "version"              :  "1.0.0",
  "author"               :  "Webkul Software Pvt. Ltd.",
  "website"              :  "https://store.webkul.com/",
  "license"              :  "Other proprietary",
  "live_test_url"        :  "http://odoodemo.webkul.com/?module=multi_websites&version=11.0",
  "depends"              :  ['website_sale_delivery'],
  "data"                 :   [
                              'security/security.xml',
                              'views/website_views.xml',
                              'views/templates.xml',
                              'views/res_partner_view.xml',
                              'views/multi_theme_view.xml',
                              'views/sale_order_view.xml',
                              'views/sale_stock_view.xml',
                              'views/invoice_view.xml',
                              'reports/sale_report_view.xml',
                              'security/ir.model.access.csv',
                            ],
  'qweb': ['static/src/xml/*.xml'],
  "images"               :  ['static/description/Banner.png'],
  "application"          :  True,
  "installable"          :  True,
  "auto_install"         :  False,
  "price"                :  199,
  "currency"             :  "EUR",
  "pre_init_hook"        :  "pre_init_check",
}
