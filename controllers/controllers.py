# -*- coding: utf-8 -*-
from odoo import http

# class TwilioOdooMessenger(http.Controller):
#     @http.route('/twilio_odoo_messenger/twilio_odoo_messenger/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/twilio_odoo_messenger/twilio_odoo_messenger/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('twilio_odoo_messenger.listing', {
#             'root': '/twilio_odoo_messenger/twilio_odoo_messenger',
#             'objects': http.request.env['twilio_odoo_messenger.twilio_odoo_messenger'].search([]),
#         })

#     @http.route('/twilio_odoo_messenger/twilio_odoo_messenger/objects/<model("twilio_odoo_messenger.twilio_odoo_messenger"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('twilio_odoo_messenger.object', {
#             'object': obj
#         })