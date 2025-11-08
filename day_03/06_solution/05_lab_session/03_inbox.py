from datetime import datetime

class Email:
    def __init__(self, sender, subject, message, date=None):
        self.sender = sender
        self.subject = subject
        self.message = message
        self.date = date or datetime.now()
        self.read_status = False
        self.archive_status = False

    def read(self):
        self.read_status = True

    def unread(self):
        self.read_status = False

    def archive(self):
        self.archive_status = True

    def unarchive(self):
        self.archive_status = False

    def __repr__(self):
        status = "Read" if self.read_status else "Unread"
        archived = "Archived" if self.archive_status else "Inbox"
        return f"[{status} | {archived}] From: {self.sender}, Subject: {self.subject}, Date: {self.date.strftime('%Y-%m-%d %H:%M')}"


class Inbox:
    def __init__(self):
        self.emails = []

    def add(self, email: Email):
        self.emails.append(email)

    def show(self, index):
        try:
            return self.emails[index]
        except IndexError:
            print("No email at that index.")

    def delete(self, index):
        try:
            return self.emails.pop(index)
        except IndexError:
            print("No email to delete at that index.")

    def search(self, keyword):
        result = [email for email in self.emails
                  if keyword.lower() in email.subject.lower() or keyword.lower() in email.message.lower()]
        return result

    def __add__(self, other):
        new_inbox = Inbox()
        new_inbox.emails = self.emails + other.emails
        return new_inbox

    def __repr__(self):
        return "\n".join(f"{i}: {email}" for i, email in enumerate(self.emails))


class WorkInbox(Inbox):
    @property
    def archived(self):
        return [email for email in self.emails if email.archive_status]

    @property
    def read(self):
        return [email for email in self.emails if email.read_status]

    @property
    def unread(self):
        return [email for email in self.emails if not email.read_status]
