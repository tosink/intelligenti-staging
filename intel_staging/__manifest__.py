# -*- coding: utf-8 -*-
{
    'name': "Intel Staging",

    'summary': """
        Remove Production Sensitive Data and only use on Dummy Data
    """,

    'description': """
         Remove Production Sensitive Data and only use on Dummy Data
    """,

    'author': "Intelligenti.io",
    'website': "http://www.intelligenti.io",

    'category': 'Tools',
    'version': '1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    "pre_init_hook": "pre_init_hook",
}