from odoo import api, fields, models, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    twilio_account_sid = fields.Char(string='Twilio Account SID')
    twilio_auth_token = fields.Char(string='Twilio Auth Token')
    twilio_whatsapp_number = fields.Char(string='Twilio Whatsapp Number')
    twilio_phone_number = fields.Char(string='Twilio Phone Number')

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res.update(
            twilio_account_sid=self.env['ir.config_parameter'].sudo().get_param('twilio_odoo_messenger'
                                                                                '.twilio_account_sid'),
            twilio_auth_token=self.env['ir.config_parameter'].sudo().get_param('twilio_odoo_messenger'
                                                                               '.twilio_auth_token'),
            twilio_whatsapp_number=self.env['ir.config_parameter'].sudo().get_param('twilio_odoo_messenger'
                                                                                    '.twilio_whatsapp_number'),
            twilio_phone_number=self.env['ir.config_parameter'].sudo().get_param('twilio_odoo_messenger'
                                                                                 '.twilio_phone_number')
        )
        return res

    @api.multi
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('twilio_odoo_messenger.twilio_account_sid',
                                                         self.twilio_account_sid)
        self.env['ir.config_parameter'].sudo().set_param('twilio_odoo_messenger.twilio_auth_token',
                                                         self.twilio_auth_token)
        self.env['ir.config_parameter'].sudo().set_param('twilio_odoo_messenger.twilio_whatsapp_number',
                                                         self.twilio_whatsapp_number)
        self.env['ir.config_parameter'].sudo().set_param('twilio_odoo_messenger.twilio_phone_number',
                                                         self.twilio_phone_number)
