from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo import tools, _
from twilio.rest import Client


class OdooTwilioApi(models.AbstractModel):
    _name = 'twilio_odoo_messenger.api'
    _description = 'Twilio API'

    @api.model
    def _twilio_messaging(self, payload):
        """

        :param payload: Expects a dict payload with keys:
        'message' - for the message to be sent
        'text_to' - the phone number to text/whatsapp,
        'api_type' - the type of api to use, sms or whatsapp.
        :return: Returns twilio.http_client Post response with status, and info dict.
        Call this method as:
         - First set payload.

        payload = {'message': 'message body here', 'text_to': 'To phone', 'api_type': 'sms type here'}

         - Call Abstract Model 'twilio_odoo_messenger.api' to access method _twilio_messaging and pass
         payload as parameter.

        response = self.env['twilio_odoo_messenger.api']._twilio_messaging(payload)

        response contains status code and info dict which can be examined further.
        """
        if not payload:
            raise Exception(_('payload argument missing.'))
        if 'message' not in payload.keys():
            raise Exception(_('message key missing in payload'))
        if 'text_to' not in payload.keys():
            raise Exception(_('text_to key missing in payload'))
        if 'api_type' not in payload.keys():
            raise Exception(_('api_type key missing in payload'))

        ACCOUNT_SID = self.env['ir.config_parameter'].sudo().get_param('twilio_odoo_messenger.twilio_account_sid')
        ACCOUNT_TOKEN = self.env['ir.config_parameter'].sudo().get_param('twilio_odoo_messenger.twilio_auth_token')

        if not ACCOUNT_SID:
            raise UserError(_('Please set your Twilio Account SID in Settings.'))
        if not ACCOUNT_TOKEN:
            raise UserError(_('Please set your Twilio Account Token in Settings.'))

        if payload['api_type'] == 'whatsapp':
            WHATSAPP_NUMBER = self.env['ir.config_parameter'].sudo().get_param(
                'twilio_odoo_messenger.twilio_whatsapp_number')
            if not WHATSAPP_NUMBER:
                raise UserError(_('Please set your Whatsapp Number in Settings.'))
            phone_from = WHATSAPP_NUMBER
            phone_to = f"whatsapp:{payload['text_to']}"
        elif payload['api_type'] == 'sms':
            PHONE_NUMBER = self.env['ir.config_parameter'].sudo().get_param('twilio_odoo_messenger.twilio_phone_number')
            if not PHONE_NUMBER:
                raise UserError(_('Please set your Whatsapp Number in Settings.'))
            phone_from = PHONE_NUMBER
            phone_to = f"{payload['text_to']}"
        else:
            raise Exception(_('The api_type sent {0} is not supported, supported types are whatsapp and sms.'.
                              format(payload['api_type'])))

        client = Client(ACCOUNT_SID, ACCOUNT_TOKEN)
        message = client.messages.create(
            from_=f'{phone_from}',
            body=payload['message'],
            to=phone_to
        )
        return message.sid

#  Methods below have been combined into one method _twilio_messaging.
# You can still call them to perform their actions.

    @api.model
    def _send_twilio_whatsapp(self, payload):
        ACCOUNT_SID = self.env['ir.config_parameter'].sudo().get_param('twilio_odoo_messenger.twilio_account_sid')
        ACCOUNT_TOKEN = self.env['ir.config_parameter'].sudo().get_param('twilio_odoo_messenger.twilio_auth_token')
        WHATSAPP_NUMBER = self.env['ir.config_parameter'].sudo().get_param(
            'twilio_odoo_messenger.twilio_whatsapp_number')

        client = Client(ACCOUNT_SID, ACCOUNT_TOKEN)

        message = client.messages.create(
            from_=f'{WHATSAPP_NUMBER}',
            body=payload['message'],
            to=f"whatsapp:{payload['text_to']}"
        )
        return message.sid

    @api.model
    def _send_twilio_sms(self, payload):
        ACCOUNT_SID = self.env['ir.config_parameter'].sudo().get_param('twilio_odoo_messenger.twilio_account_sid')
        ACCOUNT_TOKEN = self.env['ir.config_parameter'].sudo().get_param('twilio_odoo_messenger.twilio_auth_token')
        PHONE_NUMBER = self.env['ir.config_parameter'].sudo().get_param('twilio_odoo_messenger.twilio_phone_number')

        client = Client(ACCOUNT_SID, ACCOUNT_TOKEN)
        message = client.messages.create(
            from_=PHONE_NUMBER,
            to=payload['text_to'],
            body=payload['message']
        )
        return message.sid
