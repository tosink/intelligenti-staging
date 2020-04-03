# coding: utf-8
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
from odoo import api, tools, SUPERUSER_ID
from odoo.tools.safe_eval import safe_eval
_logger = logging.getLogger(__name__)


def pre_init_hook(cr):
    cr.execute('UPDATE ir_cron '
               'SET active=False;')
    cr.execute("UPDATE res_users "
               "SET password='admin';")
        
    env = api.Environment(cr, SUPERUSER_ID, {})
    payment = env['ir.module.module'].search([('name','=','payment'),('state','=','installed')],limit=1)
    if payment:
        cr.execute("UPDATE payment_acquirer "
               "SET environment='test', authorize_login='dummy', authorize_transaction_key='dummy';")
    google_drive = env['ir.module.module'].search([('name','=','google_drive_odoo'),('state','=','installed')],limit=1)
    if google_drive:
        PARAMS = (
            ('googledrive_client_id', str, ''),
            ('googledrive_client_secret', str, ''),
            ('googledrive_redirect_uri', str, 'http://localhost:8069/google_drive_token'),
            ('googleteam_drive', str, ''),
            ('googledrive_drive', str, 'My Drive'),
        )
        Config = env['ir.config_parameter']
        values = {}
        for field_name, getter, default in PARAMS:
            Config.set_param(field_name, getter(default))
    
    sendgrid = env['ir.module.module'].search([('name','=','intel_mail_sendgrid'),('state','=','installed')],limit=1)
    if sendgrid:
        cr.execute("UPDATE res_company "
               "SET sendgrid_email_validation_api_key='dummy', sendgrid_email_api_key='dummy', sendgrid_test_environment=True;")
    
