from utils.notifiers.notifier import Notifier

class EmailNotifier(Notifier):
    def __init__(self, email_provider):
        super().__init__()
        self.email_provider = email_provider

    def send_notification(self, recipient, message):
        print(f"Sending Email to {recipient}: {message}")
