# -*- encoding: utf-8 -*-
##############################################################################
#
#    Brazillian Human Resources Payroll module for OpenERP
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{  # pylint: disable=C8101,C8103
    'name': 'Folha de Pagamento Brasil',
    'summary': """Permite gerar o cálculo automático do pagamento a seus
        funcionários""",
    'description': 'Folha de Pagamento Brasil',
    'category': 'Localization',
    'author': 'Udoo',
    'license': 'AGPL-3',
    'maintainer': 'Udoo',
    'website': 'http://www.udoo.com.br',
    'version': '11.0.1.0.0',
    'depends': ['hr_payroll', 'hr_contract', 'br_hr'],
    'data': [
        'data/br_hr_payroll_data.xml',
        'view/hr_contract_view.xml',
        'view/hr_employee.xml'
    ],
    'installable': True,
    'application': True,
}
