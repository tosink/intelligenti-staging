# coding: utf-8
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
from odoo import api, tools, SUPERUSER_ID
from odoo.tools.safe_eval import safe_eval
_logger = logging.getLogger(__name__)


def pre_init_hook(cr):
    cr.execute('ALTER TABLE ir_cron'
               'SET active=True;')
    cr.execute('ALTER TABLE payment_acquirer'
               'SET environment="test", authorize_login="dummy", authorize_transaction_key="dummy";')
    
    env = api.Environment(cr, SUPERUSER_ID, {})
    google_drive = env['ir.module.module'].search([('name','=','google_drive_odoo'),('state','=','installed')],limit=1)
    if google_drive:
        PARAMS = (
            ('googledrive_client_id', str, ''),
            ('googledrive_client_secret', str, ''),
            ('googledrive_redirect_uri', str, 'http://localhost:8069/google_drive_token'),
            ('googleteam_drive', safe_eval, False),
            ('googledrive_drive', str, 'My Drive'),
        )
        Config = env['ir.config_parameter']
        values = {}
        for field_name, getter, default in PARAMS:
            Config.set_param(field_name, getter(default))
    
    sendgrid = env['ir.module.module'].search([('name','=','intel_mail_sendgrid'),('state','=','installed')],limit=1)
    if sendgrid:
        cr.execute('ALTER TABLE res_company'
               'SET sendgrid_email_validation_api_key="dummy", sendgrid_email_api_key="dummy", sendgrid_test_environment=True;')
    
    