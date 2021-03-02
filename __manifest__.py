# -*- coding: utf-8 -*-
{
    'name': "twilio_odoo_messenger",

    'summary': """
        Twilio Odoo Integration""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Edward Shirambere",
    'website': "https://www.coderain.tech",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'base_setup', 'mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/res_config_settings.xml',
        'views/wizard_views.xml',
        'views/res_partners.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}