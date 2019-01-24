# -*- coding: utf-8 -*-
# © 2017 Jérôme Guerriat
# © 2017 Niboo SPRL (https://www.niboo.be/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Archive Sale Orders',
    'category': 'Account',
    'summary': 'Merge draft invoices that share the same client',
    'license': 'AGPL-3',
    'website': 'https://www.niboo.be',
    'version': '10.0.1.0.0',
    'description': '''
This module allows the user to archive any sale order
        ''',
    'author': 'Niboo',
    'depends': [
        'sale',
    ],
    'data': [
        'views/sale_order_view.xml',
    ],
    'installable': True,
    'application': False,
}
