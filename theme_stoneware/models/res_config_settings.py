# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.addons.http_routing.models.ir_http import slugify


class website(models.Model):

    """Adds the fields for Breadcrumb."""

    _inherit = 'website'

    bread_cum_image = fields.Binary(string="Breadcrumb Image")
    is_breadcum = fields.Boolean(string="Do you want to disable Breadcrumb?")

    @api.model
    def get_category_breadcum(self,category):
        data=[]
        parent_categ=False
        if category:
            categ_data=self.env['product.public.category'].search([('id','=',int(category))])
            data.append(categ_data)
            parent_categ=categ_data
            if categ_data and categ_data.parent_id:
                parent_categ=categ_data.parent_id
                data.append(parent_categ)           
                while parent_categ.parent_id:
                    parent_categ=parent_categ.parent_id
                    data.append(parent_categ) 
            data.reverse()     
        return data

    @api.model
    def new_page(self, name=False, add_menu=False, template='website.default_page', ispage=True, namespace=None):
        res = super(website,self).new_page(name,add_menu,template,ispage=True,namespace=namespace)
        if  ispage:  
            arch = "<?xml version='1.0'?><t t-name='website."+str(name)+"'><t t-call='website.layout'> \
                    <div id='wrap' class='oe_structure oe_empty'>"

            arch=arch+'<t t-if="not website.is_breadcum">'

            arch =arch+'<t t-if="not website.bread_cum_image">'\
                '<nav class="is-breadcrumb shop-breadcrumb" role="navigation" aria-label="breadcrumbs">'\
                      '<div class="container">'\
                        '<h1><span>'+str(name)+'</span></h1>'\
                        '<ul class="breadcrumb">'\
                            '<li><a href="/page/homepage">Home</a></li>'\
                            '<li class="active"><span>'+str(name)+'</span></li>'\
                        '</ul>'\
                      '</div>'\
                '</nav>'\
                '</t>'
            arch=arch+'<t t-if="website.bread_cum_image">'\
                '<t t-set="bread_cum" t-value="website.image_url(website,'+repr('bread_cum_image')+')"/>'\
                '<nav class="is-breadcrumb shop-breadcrumb" role="navigation" aria-label="breadcrumbs" t-attf-style="background-image:url(#{bread_cum}#)">'\
                    '<div class="container">'\
                        '<h1><span>'+str(name)+'</span></h1>'\
                        '<ul class="breadcrumb">'\
                            '<li><a href="/page/homepage">Home</a></li>'\
                            '<li class="active"><span>'+str(name)+'</span></li>'\
                        '</ul>'\
                      '</div>'\
                '</nav>'\
            '</t>'
            arch =arch+'</t>'
            arch = arch+'</div><div class="oe_structure"/></t></t>'
            view_id = res['view_id']
            view = self.env['ir.ui.view'].browse(int(view_id))
            view.write({'arch':arch})
        return res


class WebsiteConfigSettings(models.TransientModel):

    """Settings for the Breadcrumb."""

    _inherit = 'res.config.settings'

    bread_cum_image = fields.Binary(
        related='website_id.bread_cum_image',
        string='Breadcrumb Image',
    )
    is_breadcum = fields.Boolean(string="Do you want to disable Breadcrumb?", related='website_id.is_breadcum')

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    hover_image = fields.Binary("Hover Image")
