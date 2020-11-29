from twilio.rest import Client

def msg_mom_and_dad(event=None, context=None):

    # get your sid and auth token from twilio
    twilio_sid = 'ACf95fb72cd0f797915cef66a0ef7e5768'
    auth_token = '71174d069b34e4756371e2d08c811de6'

    whatsapp_client = Client(twilio_sid, auth_token)

    # keep adding contacts to this dict to send
    # them the message
    contact_directory = {'daddy':'+919700939598'}

    for key, value in contact_directory.items():
        msg_loved_ones = whatsapp_client.messages.create(
                body = 'good evng {} !'.format(key),
                from_= 'whatsapp:+14155238886',
                to='whatsapp:' + value,

            )

        print(msg_loved_ones.sid)
