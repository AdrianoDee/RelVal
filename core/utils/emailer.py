"""
Module that handles all email notifications
"""
from core_lib.utils.emailer import Emailer as BaseEmailer


class Emailer(BaseEmailer):
    """
    Emailer sends email notifications to users
    """

    def send(self, subject, body, recipients):
        body = body.strip()  + '\n\nSincerely,\nRelVal Machine'
        subject = f'[RelVal] {subject}'
        super().send(subject, body, recipients)
