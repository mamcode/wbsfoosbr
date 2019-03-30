# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.addons.payment.models.payment_acquirer import ValidationError
from odoo.tools.float_utils import float_compare
from pagseguro import PagSeguro
import logging
import pprint

_logger = logging.getLogger(__name__)


class PagseguroPaymentAcquirer(models.Model):
    _inherit = 'payment.acquirer'

    provider = fields.Selection(
        selection_add=[('pagseguro', 'Pagseguro')], default='pagseguro')
    pagseguro_email_account = fields.Char(
        'Pagseguro Email', required_if_provider='pagseguro', groups='base.group_user')
    pagseguro_token = fields.Char(
        'Pagseguro Token', groups='base.group_user',
        help='The Pagseguro Token is used to ensure communications coming from Pagseguro are valid and secured.')

    @api.multi
    def pagseguro_form_generate_values(self, values):
        pagseguro_tx_values = dict(values)
        pagseguro_tx_values.update({
            'pagseguro_email': self.pagseguro_email_account,
            'pagseguro_token': self.pagseguro_token,
            'amount': format(values['amount'], '.2f')
        })
        if self.environment == 'prod':
            config = {'sandbox': False}
        else:
            config = {'sandbox': True}
        pg = PagSeguro(email=self.pagseguro_email_account,
                       token=self.pagseguro_token, config=config)
        pg.reference_prefix = None
        pg.reference = pagseguro_tx_values['reference']
        pg.items = [
            {"id": "0001", "description": pagseguro_tx_values['reference'],
                "amount": pagseguro_tx_values['amount'], "quantity": 1},
        ]
        base_url = self.env['ir.config_parameter'].sudo(
        ).get_param('web.base.url')
        pg.redirect_url = base_url + pagseguro_tx_values['return_url']
        _logger.info("Redirect Url: %s" % (pg.redirect_url))
        pg.notification_url = base_url + "/payment/pagseguro/feedback"
        response = pg.checkout()
        _logger.info("Response Errors: %s" % (response.errors))
        pagseguro_tx_values.update({
            'payment_url': response.payment_url
        })
        # _logger.info(values['reference'])
        _logger.info("Transaction Values: %s" % (pagseguro_tx_values))
        return pagseguro_tx_values


class PagseguroPaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    @api.model
    def _pagseguro_form_get_tx_from_data(self, data):
        aqr = self.env['payment.acquirer'].search([('name', '=', 'Pagseguro')])
        if aqr.environment == 'prod':
            config = {'sandbox': False}
        else:
            config = {'sandbox': True}
        pg = PagSeguro(email=aqr.pagseguro_email_account,
                       token=aqr.pagseguro_token, config=config)
        notif = pg.check_notification(data.get('notificationCode'))
        reference, amount, currency = notif.reference, notif.grossAmount, 'BRL'
        tx = self.search([('reference', '=', reference)])
        if not tx or len(tx) > 1:
            error_msg = _('received data for reference %s') % (
                pprint.pformat(reference))
            if not tx:
                error_msg += _('; no order found')
            else:
                error_msg += _('; multiple order found')
            _logger.info(error_msg)
            raise ValidationError(error_msg)

        return tx

    # def _pagseguro_form_get_invalid_parameters(self, data):
        # invalid_parameters = [

        # if float_compare(float(data.get('amount', '0.0')), self.amount, 2) != 0:
        # invalid_parameters.append(('amount', data.get('amount'), '%.2f' % self.amount))
        # if data.get('currency') != self.currency_id.name:
        # invalid_parameters.append(('currency', data.get('currency'), self.currency_id.name))

        # return invalid_parameters

    def _pagseguro_form_validate(self, data):

        STATUS_CODE = {

            '1': 'Aguardando Pagamento',
            '2': 'Em análise',
            '3': 'Paga',
            '4': 'Disponível',
            '5': 'Em disputa',
            '6': 'Devolvida',
            '7': 'Cancelada',
            '8': 'Debitada',
            '9': 'Retenção temporária'
        }

        aqr = self.env['payment.acquirer'].search([('name', '=', 'Pagseguro')])
        if aqr.environment == 'prod':
            config = {'sandbox': False}
        else:
            config = {'sandbox': True}
        pg = PagSeguro(email=aqr.pagseguro_email_account,
                       token=aqr.pagseguro_token, config=config)
        notif = pg.check_notification(data.get('notificationCode'))
        status = notif.status
        res = {
            'acquirer_reference': notif.code,
        }
        # TODO confirmation date
        if status == '1':
            _logger.info(
                'Validated Pagseguro payment for tx %s: set as pending' % (self.reference))
            res.update(state='pending')
            return self.write(res)
        elif status == '3':
            _logger.info(
                'Validated Pagseguro payment for tx %s: set as done' % (self.reference))
            res.update(state='done')
            return self.write(res)
        else:
            _logger.info(
                'Error on Pagseguro payment for tx %s: set as error' % (self.reference))
            res.update(state='error')
            return self.write(res)
