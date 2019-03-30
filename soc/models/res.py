# -*- coding: utf-8 -*-

import io
from odoo import models, fields, api
import base64
import datetime
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning
import csv

class res_partner(models.Model):
    _inherit = 'res.partner'

    allow_consignment = fields.Boolean("Allows SOC")
    # is_author = fields.Boolean("Autor", default=False)
    consignee_location_id = fields.Many2one('stock.location','Location SOC')
    report_attachment_ids = fields.One2many('ir.attachment','consignment_partner_id',string='Report SOC')
    send_auto_email = fields.Boolean("Submit Auto Report")

    @api.multi
    def create_consignee_location(self):
        location_obj = self.env['stock.location']
        if self.customer:
            consignent_op_type = 'sale'
        if not self.env['stock.location'].search([('name','=', 'Consignado'),('usage','=','internal')]):
            print('\nentrou no if consigando')
            default_vals = location_obj.default_get(location_obj.fields_get())

            location_vals = {   'usage':'internal',
                                'name': 'Consignado',
                                'is_consignment': True,
                                'consignment_operation_type': consignent_op_type
                            }
            default_vals.update(location_vals)
            location_id = location_obj.create(default_vals)
        
        consignado_id = self.env['stock.location'].search([('name','=', 'Consignado')]).id
        print(consignado_id)
        default_vals = location_obj.default_get(location_obj.fields_get())

        location_vals = {   'usage':'internal',
                            'name': self.name,
                            'location_id': consignado_id,
                            'consignee_id': self.id,
                            'is_consignment': True,
                            'consignment_operation_type': consignent_op_type
                        }
        default_vals.update(location_vals)
        
        location_id = location_obj.create(default_vals)
        if location_id and self.supplier:
            rule_obj = self.env['stock.rule']
            route_obj = self.env['stock.location.route']
            picking_type_id = self.env['stock.picking.type'].search([('warehouse_id.company_id', '=', self.company_id.id), ('code', '=', 'outgoing')], limit=1)
            Route = route_obj.search([('name', '=', 'PurchaseConsignment')], limit=1)
            if not Route:
                Route = route_obj.create({'name': 'PurchaseConsignment'})
            default_val = rule_obj.default_get(rule_obj.fields_get())
            
            default_val.update({
                'name': self.name,
                'action': 'pull',
                'route_id': Route.id,
                'location_src_id': location_id.id,
                'picking_type_id': picking_type_id.id,
                'location_id': self.property_stock_customer.id,
                })
            rul = rule_obj.create(default_val)

        self.consignee_location_id = location_id.id

    @api.model
    def create(self, vals):
        partner = super(res_partner, self).create(vals)
        if vals.get('allow_consignment'):
            print (partner.create_consignee_location())
        return partner


    @api.multi
    def write(self, vals):
        if vals.get('allow_consignment') is not None:
            # Create consignent location for this customer if not present.
            if vals.get('allow_consignment'):
                print("===================aaaa===========")
                con_loc_exists = self.env['stock.location'].search([('consignee_id','=', self.id),('usage','=','internal')], limit=1)

                if not con_loc_exists:
                    self.create_consignee_location()
            
            elif self.env['stock.quant'].search_count([('location_id','=', self.consignee_location_id.id)]) > 0:               
                raise UserError('It was not possible to file the Consigned Inventory, it has products in it')

            # else:
            #     self.env['stock.location'].search([('consignee_id','=', self.id),('usage','=','internal')]).unlink()
            #     self.consignee_location_id = None

        partner = super(res_partner, self).write(vals)

        return partner

    @api.multi
    def action_view_consignment_products(self):
        self.ensure_one()
        estoque = self.env['stock.quant'].search([('location_id.id', '=', self.consignee_location_id.id)])
        
        if len(estoque) > 0:
            imd = self.env['ir.model.data']
            list_view_id = imd.xmlid_to_res_id('stock.view_stock_quant_tree')
            form_view_id = imd.xmlid_to_res_id('stock.view_stock_quant_form')
            action = self.env.ref('soc.consignee_open_quants').read()[0]
            action['domain'] = "[('consig_op_type', 'in', ['sale', False]),('location_id','=',%s)]" % self.consignee_location_id.id
            action['context'] = {'search_default_internal_loc': 1, 'search_default_productgroup': 1}
            action['views'] = [[list_view_id, 'tree'], [form_view_id, 'form']]
            return action
        else:
            raise Warning('This customer has no consignment products.')

    @api.multi
    def create_xls_consignment_report(self):
        estoque = self.env['stock.quant'].search([('location_id.id', '=', self.consignee_location_id.id)])

        if len(estoque) > 0:            
            cabecalho = "Mapa de Consignação Editora Hedra\ncomercial@hedra.com.br\n11-3097-8304\n\n"
            empresa = self.name + "\n"
            data = datetime.datetime.now().strftime('%d-%m-%Y')
            campos = "\n\nISBN,Titulo,Quantidade,Valor de Custo,Valor de Venda,Valor Total,Acerto,Reposição\n"

            arquivo = cabecalho + empresa + data + campos

            for produto in estoque:
                isbn = produto.product_id.ean13
                titulo = produto.product_id.name
                quantidade = produto.quantity
                val_custo = produto.product_id.standard_price
                val_venda = produto.product_id.list_price
                total = val_custo * quantidade

                linha = "%s,%s,%d,%.2f,%.2f,%.2f\n" % (isbn, titulo, int(quantidade), val_custo, val_venda, total)

                arquivo = arquivo + linha

            mode = 'manual'
            if self._context.get('mode') and self._context.get('mode') == 'auto':
                mode = 'auto'
            
            attach = self.env['ir.attachment'].create({
                    'name': u'RelatorioConsignacao.xlsx',
                    'datas': base64.b64encode(arquivo.encode()),
                    'datas_fname': "RelatorioConsignacao.xlsx",
                    'res_model': 'mail.compose.message',
                    'res_id': 0,
                    'consignment_partner_id': self.id,
                    'consignment_mode': mode
                })

            return attach.id
        else:
            return False
    
    @api.model
    def consignment_report_cron(self):
        print ("##### consignment_report_cron [START] #####")
        customers = self.search([('send_auto_email','=',True)])
        template_id = self.env['ir.model.data'].get_object_reference('soc',
                                                                     'email_template_partner_consignment_report')[1]
        for each_cst in customers:
            attachment_id = each_cst.with_context({'mode':'auto'}).create_xls_consignment_report()
            self.env['mail.template'].browse(template_id).send_mail(each_cst.id)
        print ("##### consignment_report_cron [END] #####")

    @api.one
    def _compute_sale_order_count(self):
        super(res_partner, self)._compute_sale_order_count()
        sale_data = self.env['sale.order'].read_group(domain=[('partner_id', 'child_of', self.ids)],
                                                     fields=['partner_id'], groupby=['partner_id'])
        cons_count = self.env['sale.order'].search_count([('partner_id','=', self.id),('order_type','=','con_order')])
        partner_child_ids = self.read(['child_ids'])
        mapped_data = dict([(m['partner_id'][0], m['partner_id_count']) for m in sale_data])
        for partner in self:
           # let's obtain the partner id and all its child ids from the read up there
            item = next(p for p in partner_child_ids if p['id'] == partner.id)
            partner_ids = [partner.id] + item.get('child_ids')
            # then we can sum for all the partner's child
            partner.sale_order_count = sum(mapped_data.get(child, 0) for child in partner_ids)
        self.sale_order_count -= cons_count

class mail_compose_message(models.TransientModel):
    _inherit = 'mail.compose.message'

    @api.multi
    def cancel_send_email(self):
        self.env['ir.attachment'].search([('id', '=', self.attachment_ids.id)]).unlink()

    @api.model
    def default_get(self, fields):
        result = super(mail_compose_message, self).default_get(fields)
        consignment_template = self.env.ref("soc.email_template_partner_consignment_report")
        if result.get('template_id') and result.get('template_id') == consignment_template.id:
            if self._context and self._context.get('active_id'):
                attachment_id = self.env['res.partner'].browse(self._context.get('active_id')).create_xls_consignment_report()
                if attachment_id:
                    result['attachment_ids'] = [attachment_id]
        return result

class ir_attachment(models.Model):
    _inherit = 'ir.attachment'

    consignment_partner_id = fields.Many2one('res.partner','Relatório para:', readonly=True)
    consignment_mode = fields.Selection([('auto','Automatic'),('manual','Manual')], string="Modo de Criação")
    
    @api.model
    def create(self, vals):
        attach = super(ir_attachment, self).create(vals)
        return attach
