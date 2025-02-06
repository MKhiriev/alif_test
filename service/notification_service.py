class NotificationService:
    def __init__(self, sms_notifier, email_notifier, user_service):
        self.sms_notifier = sms_notifier
        self.email_notifier = email_notifier
        self.user_service = user_service

    def notify_user(self, user_id, message):
        contact_info = self.user_service.get_contact_info_by_user_id(user_id)
        self.send_sms(contact_info.telephone, message)
        self.send_email(contact_info.email, message)

    def send_sms(self, telephone, message):
        self.sms_notifier.send_notification(telephone, message)

    def send_email(self, email, message):
        self.email_notifier.send_notification(email, message)