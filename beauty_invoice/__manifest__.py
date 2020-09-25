# -*- encoding: UTF-8 -*-

{
    'name': 'Invoice BEAUTY STORE',
    'summary': """Invoice in PDF""",
    'version': '',
    'description': """Is a module for printing invoice """,
    'author': '',
    'maintainer': '',
    'website': '',
    'category': 'account',
    'depends': ['account'],
    'license': 'AGPL-3',
    'data': [
            'reports/sale_invoice.xml',
            'reports/account_pdf_menu.xml'
             ],
    'demo': [],
    'sequence': 1,
    'installable': True,
    'auto_install': False,
    'application': True,

}
