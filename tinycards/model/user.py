class User(object):
    """Data class for a Tinycards user entity.

    Args:
        creation_date (int): Timestamp of when the user's account was created.
        email (string): Email address the user's account is registered to.
        fullname (string): The full name of the user.
        user_id (int): The user ID generated by Tinycards/Duolingo.
        learning_language (str): Language code of the language the user has
            be learning last (e.g., 'fr' for French).
        picture_url (str): Link to the user's profile picture.
        subscribed (bool): ??
        subscriber_count (int): Number of other users that have subscribed to
            the current user.
        subscription_count (int): Number of other users the current user has
            subscribed to.
        ui_language (str): Language code of the language the user has selected
            for the Tinycards user interface (e.g., 'en' for English).
        username (str): The user's unique username used by Tinycards/Duolingo.
    """

    def __init__(self,
                 creation_date,
                 email,
                 fullname,
                 user_id,
                 learning_language,
                 picture_url,
                 subscribed,
                 subscriber_count,
                 subscription_count,
                 ui_language,
                 username):
        """Initialize a new instance of the User class."""
        self.creation_date = creation_date
        self.email = email
        self.fullname = fullname
        self.id = user_id
        self.learning_language = learning_language
        self.picture_url = picture_url
        self.subscribed = subscribed
        self.subscriber_count = subscriber_count
        self.subscription_count = subscription_count
        self.ui_language = ui_language
        self.username = username
