from utils.notifiers.notifier import Notifier

class SmsNotifier(Notifier):
    def __init__(self, sms_provider):
        super().__init__()
        self.sms_provider = sms_provider

    def send_notification(self, recipient, message):
        print(f"Sending SMS to {recipient}: {message}")
