# twilio_odoo_messenger
Odoo Integration with Twilio Messaging

1. Send Whatsapp/SMS Message to Partner. Introduces dropdown action to send partner whatsapp message/SMS.
2. Has 3 inbuilt templates corresponding to twilio whatsapp templates. Choose template while sending message. Available templates
   are Authentication template, Appointment template and Order template.
3. Can be used in any module that depends on this module.

#Steps
1. Add this module to depends list in your manifest python file.
   ```python
        'depends': ['twilio_odoo_messager']
   ```
2. Create a method in your model to send sms/whatsapp. Generate payload and send to api.
```python
        payload = {'message': 'message body here', 'text_to': 'To phone', 'api_type': 'sms type here'}
        response = self.env['twilio_odoo_messenger.api']._twilio_messaging(payload)
```
3. Examine the response which contains status code and info dict.


