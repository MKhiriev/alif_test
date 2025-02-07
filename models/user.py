class User:
    def __init__(self, user_id, name, email, telephone):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.telephone = telephone

    def get_contact_info(self):
        """
        Return contact information of the user

        :return: tuple with telephone and email
        """
        return {'telephone': self.telephone, 'email': self.email}

    def __str__(self):
        return f"ID: {self.user_id}. {self.name} Contacts: {self.email} {self.telephone}"
