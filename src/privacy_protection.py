```python
from src.database.user_db import UserDB

class PrivacyProtection:
    def __init__(self):
        self.user_db = UserDB()

    def protectPrivacy(self, user_id):
        """
        Function to anonymize user data for privacy protection.
        """
        user_data = self.user_db.get_user(user_id)
        if user_data:
            anonymized_data = self.anonymize_data(user_data)
            self.user_db.update_user(user_id, anonymized_data)
            return True
        return False

    def anonymize_data(self, user_data):
        """
        Function to anonymize user data.
        """
        anonymized_data = {}
        for key in user_data.keys():
            if key not in ['username', 'email']:
                anonymized_data[key] = None
        return anonymized_data

    def delete_user_data(self, user_id):
        """
        Function to delete user data upon request.
        """
        return self.user_db.delete_user(user_id)
```