from odoo import api, fields, models
from odoo.exceptions import UserError
from twilio.rest import Client

class OdooTwilioApi(models.AbstractModel):
    _name = 'twilio_odoo_messenger.api'
    _description = 'Twilio API'

    @api.model
    def _send_twilio_whatsapp(self, payload):
        ACCOUNT_SID = self.env['ir.config_parameter'].sudo().get_param('twilio_odoo_messenger.twilio_account_sid')
        ACCOUNT_TOKEN = self.env['ir.config_parameter'].sudo().get_param('twilio_odoo_messenger.twilio_auth_token')
        WHATSAPP_NUMBER = self.env['ir.config_parameter'].sudo().get_param('twilio_odoo_messenger.twilio_whatsapp_number')

        client = Client(ACCOUNT_SID, ACCOUNT_TOKEN)

        message = client.messages.create(
            from_=f'{WHATSAPP_NUMBER}',
            body=payload['message'],
            to=f"whatsapp:{payload['text_to']}"
        )
        return message.sid
