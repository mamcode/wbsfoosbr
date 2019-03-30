# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import Warning
import datetime


class sale_order(models.Model):
    _inherit = 'sale.order'

    order_type = fields.Selection([('sale','Sale'),('con_order','SOC'),
    ('con_sale','Sale SOC')], string = "Type of Sale", default='sale', required=True)
    
    @api.onchange('order_type', 'partner_id')
    def onchange_order_type_partner(self):
        print("##### onchange_order_type_partner [START] #####")
        result = {}
        count = 0
        for each_line in self.order_line:
            count += 1
        
        if count > 0:
            result['warning'] = {'title': "Aviso!",'message': "Changes to the Customer or Type of Sale / Request after inserting a product may cause inconsistency."}
        print("##### onchange_order_type_partner [END] #####")
        return result
    
    @api.onchange('order_type')
    def onchange_order_type(self):
        print("##### onchange_order_type [START] #####")
        result = {}
        
        if self.order_type and self.order_type != 'sale':
            result['domain'] = {'partner_id':[('allow_consignment','=',True),('customer','=',True)]}
            if self.partner_id:
                partner = self.env['res.partner'].search([('id','=',self.partner_id.id)])
                if not partner['allow_consignment']:
                    result['value'] = {'partner_id':False}
                    result['warning'] = {'title': "Warning!",'message': "This Client does not allow consignment operations."}
                    
        elif self.order_type and self.order_type == 'sale':
            result['domain'] = {'partner_id':[('customer','=',True)]}
        print("##### onchange_order_type [END] #####")
        return result

    @api.multi
    def action_confirm(self):
        if self.order_type == 'con_sale':
            self = self.with_context(consig_op_type='sale')
            if len(self.order_line) < 1:
                raise Warning("Add one or more products to confirm the Settlement of Consignment.")
                return False
            else:
                estoque = self.env['stock.quant'].search([('location_id.id', '=', self.partner_id.consignee_location_id.id)])
                
                flag = False
                excluir = []
                log = ""
                for item in self.order_line:
                    print(item.product_id.id)
                    for produto in estoque:
                        if item.product_id == produto.product_id:
                            qtde_estoque = produto.quantity
                            qtde_acerto = item.product_uom_qty
                            qtde_atual = qtde_estoque - qtde_acerto
                            
                            if qtde_atual >= 0:
                                produto.sudo().write({'quantity': qtde_atual})
                            else:
                                log = log + "Produto: %s - Qtde: %d<br>" % (produto.product_id.name, int(qtde_atual))
                                excluir.append(produto)
                                flag = True

                if bool(excluir): 
                    for registro in excluir:
                        registro.unlink()

                if flag:
                    self.create_message(log)                            
                self.write({'state':'sale', 'confirmation_date':datetime.datetime.now()})
                return True
        else:
            if len(self.order_line) < 1:
                raise Warning("Adicione um ou mais produtos para confirmar o Acerto de Consignação.")
            else:
                self = self.with_context(order_type=self.order_type)
                return super(sale_order, self).action_confirm()
    
    @api.multi
    def action_view_sale_consignment_products(self):
        imd = self.env['ir.model.data']
        
        list_view_id = imd.xmlid_to_res_id('stock.view_stock_quant_tree')        
        form_view_id = imd.xmlid_to_res_id('stock.view_stock_quant_form')        
        action = self.env.ref('soc.consignee_open_quants').read()[0]        
        action['views'] = [[list_view_id, 'tree'], [form_view_id, 'form']]        
        action['context'] = {'search_default_internal_loc': 1, 'search_default_productgroup': 1}                
        action['domain'] = "[('location_id','=',%s)]" % self.partner_id.consignee_location_id.id        
        action['target'] = "new"

        return action

    #Opção 2 caso o envio da mensagem pelo canal dê errado
    @api.multi
    def teste_email(self):
        print("Teste")
        email = self.env['mail.mail'].create(
            {'subject' : 'Notice! Settlement of Consignment x negatived the stock',
             'email_from' : 'contato@udoo.com.br',
             'email_to' : 'contao@udoo.com.br',
             'body_html' : 'Here is the warning that the negative stock for the hit x',
             'message_type' : 'email'
            }
        )
        print(email.id)
        email.send()

    @api.multi
    def create_channel(self):
        mail_channel = self.env['mail.channel'].create(
                {'name' : 'Errors of SOC',
                 'public' : 'public'
                }
            )
        self.env['mail.channel.partner'].create(
                {'partner_id' : self.env.user.partner_id.id,
                 'channel_id' : mail_channel.id
                }
            )

        return mail_channel

    @api.multi
    def create_message(self, log):
        record_name = 'Errors of SOC'
        channel =  self.env['mail.channel'].search([('name', '=', record_name)])
        print(channel, bool(channel))

        if not bool(channel):
            print("Creating a channel")
            channel = self.create_channel()
            print(channel)
            
        date = datetime.datetime.now()
        email_from = self.env.user.partner_id.email
        author_id = self.env.user.partner_id.id
        model = 'mail.channel'
        res_id = channel.id
        message_type = 'comment'

        body = 'The Sale of SOC Adjustment %s generated negative inventory for the (s) Following(s) product(s):<br>' % self.name + log

        vals = {'date' : date, 
                'email_from' : email_from, 
                'author_id' : author_id, 
                'record_name' : record_name,
                'model' : model,
                'res_id' : res_id,
                'message_type' : message_type,
                'channel_ids' : [(4, res_id)],
                'body' : body
               }

        message = self.env['mail.message'].create(vals)
        if message:
            print("Message successfully sent to channel -", message)
        
class sale_order_line(models.Model):
    _inherit = 'sale.order.line'

    consignment_stock = fields.Float(string='SOC', compute='_compute_consignment_stock', store=True)
    
    @api.one
    @api.depends('product_id')
    def _compute_consignment_stock(self):
        print ("##### _compute_consignment_stock [START] #####")
        if not self.product_id:
            return
        
        consignent_location = self.order_id.partner_id.consignee_location_id
        if not consignent_location:
            return False
        
        consignment_quants = self.env['stock.quant'].search([('location_id','=',consignent_location.id),
            ('product_id','=', self.product_id.id)])
        product_qty = 0
        for each_quant in consignment_quants:
            product_qty += each_quant.quantity
        self.consignment_stock = product_qty

    @api.onchange('product_id')
    def onchange_product(self):
        if self.product_id:
            if self.order_id.order_type != 'sale' and self.product_id.product_tmpl_id.type != 'product':
                result = {}
        
                result['value'] = {'product_id':False, 'name':False, 'product_uom_qty':1, 'price_unit':False, 'tax_id':False, 'price_subtotal':False}
                
                result['warning'] = {'title': "Aviso!",'message': "This Product Type is not allowed in consignment operations."}
                
                return result
            
            consignment_quants = self.env['stock.quant'].search([('location_id','=',self.order_id.partner_id.consignee_location_id.id),
                ('product_id','=', self.product_id.id)])
            
            product_qty = 0
            
            for each_quant in consignment_quants:
                product_qty += each_quant.quantity

            consignment_stock = product_qty
            
            self.consignment_stock = consignment_stock
    
    @api.onchange('product_uom_qty', 'product_id')
    def _onchange_consignment_stock(self):
        if self.product_id and self.order_id.order_type == 'con_sale':
            consignment_quants = self.env['stock.quant'].search([('location_id','=',self.order_id.partner_id.consignee_location_id.id),
                ('product_id','=', self.product_id.id)])
            product_qty = 0
            for each_quant in consignment_quants:
                product_qty += each_quant.quantity

            consignment_stock = product_qty
            if self.product_uom_qty > consignment_stock:
                return {
                    'warning': {
                        'title': "Warning!",
                        'message': "This Consignment Sale will negatively affect the consignment stock of this product.",
                    },
                }
        
