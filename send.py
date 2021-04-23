import telnyx

telnyx.api_key = "KEY0178F16E51822582E984953ECBBF48B9_1gYddzeO4FWNim7LXwVBXt"
phone_numbers = open('numbers.txt', mode='r',
                     encoding='utf-8').read().split('\n')
sms_sender = "+12182274002"
body = 'BODY TEXT GOES HERE'

for number in phone_numbers:
        
        if number == "":
            continue
        print("Sending message to {}".format(number))
        try:
            telnyx.Message.create(
            from_= sms_sender,
            to=number,
            text=body,
        )
        except Exception as e:
            print("Failed to send sms\n")
            print(str(e))

