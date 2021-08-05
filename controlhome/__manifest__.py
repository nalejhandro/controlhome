# -*- coding: utf-8 -*-
{
    'name': "Control Home",

    'summary': """
        System to control the different equipment of a house
        Proposal like testing""",

    'description': """
        Long description of module's purpose
    """,

    'author': "nalejhandro/Vauxoo",
    'website': "http://www.vauxoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/controlhome.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
