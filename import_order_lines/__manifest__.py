# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Import Sale Order Lines from Excel or CSV File',
    'version': '11.0.1.2',
    'summary': 'Easy to Import multiple sales order lines on Odoo by Using CSV/XLS file',
    'category': 'Sales',
    "price": 25,
    "currency": 'EUR',
    'description': """
	BrowseInfo developed a new odoo/OpenERP module apps.
	This module use for import bulk Sales Order lines from Excel file. Import Sales order lines from CSV or Excel file.
	Import Sales, Import Sale order line, Import Sale lines, Import SO Line. Sale Import, Add SO from Excel.Add Excel Sale order lines.Add CSV file.Import Sale data. Import excel file


Este módulo usa para importar linhas de Pedidos de Vendas a granel a partir do arquivo do Excel. Importar linhas de pedidos de vendas a partir do arquivo CSV ou Excel.Importar vendas, linha de pedidos de importação de importação, linhas de importação de vendas, importar SO Line. Importação de vendas, Adicione SO de Excel. Adicione as linhas de ordem de venda do Excel. Adicione arquivos CSV. Dados de venda de importação. Importar arquivo excel Este módulo usa para importar leads em massa do arquivo Excel. Importar liderar do arquivo CSV ou Excel.Importe os dados do chumbo, Adicione o lead do excel. Importar arquivo excel

تستخدم هذه الوحدة لخطوط استيراد أمر المبيعات بالجملة من ملف Excel. استيراد أسطر أمر المبيعات من ملف CSV أو Excel.استيراد المبيعات ، استيراد سطر أمر البيع ، استيراد خطوط البيع ، استيراد SO Line. بيع استيراد ، إضافة SO من Excel.Add Excel Sale order lines.Add CSV file.Import بيع البيانات. استيراد ملف excel تستخدم هذه الوحدة النمطية لاستيراد العملاء السائبة من ملف Excel. استيراد الرصاص من ملف CSV أو Excel.استيراد البيانات الرصاص ، إضافة الرصاص من التفوق. استيراد ملف اكسل

Ce module est utilisé pour importer des lignes de commande client en vrac à partir du fichier Excel. Importer des lignes de commande client à partir d'un fichier CSV ou Excel.
Importer des ventes, Importer une ligne de commande de vente, Importer des lignes de vente, Importer une ligne SO. Vente Import, Ajouter SO à partir de Excel.Add Excel Vente lignes de commande.Ajouter fichier CSV.Import données de vente. Importer un fichier Excel Ce module permet d'importer des prospects en masse à partir d'un fichier Excel. Importer le plomb à partir d'un fichier CSV ou Excel.
Importer des données de prospects, ajouter des pistes depuis Excel. Importer un fichier Excel

Este módulo se utiliza para importar líneas de pedidos de ventas a granel desde el archivo de Excel. Importar líneas de orden de venta desde CSV o archivo de Excel.
Importar ventas, Línea de orden de venta de importación, Importar líneas de venta, Importar línea SO. Importación de venta, agregue SO de Excel. Agregue líneas de orden de venta de Excel. Agregue archivo CSV. Importe de datos de venta. Importar archivo de Excel Este módulo se utiliza para importar clientes potenciales a granel del archivo de Excel. Importar plomo desde CSV o archivo de Excel.
Importar datos de clientes potenciales, agregar clientes potenciales de excel. Importar archivo de Excel
	-
    """,
    'author': 'BrowseInfo',
    'website': 'http://www.browseinfo.in',
    
    'depends': ['base','sale'],
    'data': [
    		  'import_order_lines_view.xml',
            ],
    'demo': [],
    'test': [],
    'installable':True,
    'auto_install':False,
    'application':True,
    "images":['static/description/Banner.png'],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
