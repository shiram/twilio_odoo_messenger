# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo import tools, _
from odoo.exceptions import ValidationError, AccessError
import phonenumbers


class Partner(models.Model):
    _inherit = ['res.partner']

    @api.constrains('whatsapp_phone_number')
    def _check_whatsapp_phone_number(self):
        for record in self:
            phone = phonenumbers.parse(record.whatsapp_phone_number, None)
            if not phonenumbers.is_valid_number(phone):
                raise ValidationError(_('Could not validate whatsapp phone number, format +256 XXX XXX XXX.'))

    whatsapp_phone_number = fields.Char(string='Whatsapp Number')

    @api.one
    def send_whatsapp_message(self):
        print("Send whatsapp method logic")


class SendWhatsappWizard(models.TransientModel):
    _name = 'twilio_odoo_messenger.send_whatsapp_wizard'
    _description = 'Send Whatsapp Wizard'

    TEMPLATE_LIST = [
        ('auth_template', 'Authentication Template'),
        ('appointment_template', 'Appointment Template'),
        ('order_template', 'Order Template'),
    ]

    DEFAULT_TEMPLATE = 'auth_template'

    twilio_template = fields.Selection(selection=TEMPLATE_LIST, default=DEFAULT_TEMPLATE, string='Template')
    message_detail = fields.Char(string='Authentication Detail')
    auth_code = fields.Char(string='Authentication Code')
    message_date = fields.Datetime(string='On Date')
    order_detail = fields.Char(string='Order Detail')
    order_url = fields.Char(string='Order Url')

    @api.one
    def action_send_whatsapp(self):
        payload = False
        model = self.env.context['active_model']
        active_id = self.env.context['active_id']
        record = self.env[model].sudo().browse(active_id)
        if not record:
            raise AccessError(_('No Partner Record Found'))
        if not record.whatsapp_phone_number:
            raise ValidationError(_('Partner does not have a valid whatsapp number set.'))
        if self.twilio_template == 'auth_template':
            message = "Your {0} code is {1}".format(self.message_detail, self.auth_code)
            payload = {'message': message, 'text_to': record.whatsapp_phone_number}
        elif self.twilio_template == 'appointment_template':
            message = "Your {0} appointment is comming up on {1}".format(self.message_detail, self.message_date)
            payload = {'message': message, 'text_to': record.whatsapp_phone_number}
        elif self.twilio_template == 'order_template':
            message = "Your {0} order of {1} has been shipped and should be delivered on {2}. Details: {3}".format(
                self.message_detail, self.order_detail, self.message_date, self.order_url
            )
            payload = {'message': message, 'text_to': record.whatsapp_phone_number}

        response = self.env['twilio_odoo_messenger.api']._send_twilio_whatsapp(payload)
        print(response)


