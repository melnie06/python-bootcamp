class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def display_info(self):
        return f"User: {self.username} Email: {self.email}"

class Writer(User):
    def __init__(self, username, email):
        super().__init__(username, email)
        self.articles = []

    def write_article(self, title):
        print(f"{self.username} is writing '{title}'...")
        self.articles.append(title)

writer = Writer("JohnyTest", "johny.test@gmail.com")
writer.display_info()

writer.write_article("Java")
writer.write_article("Python")
print(writer.articles)

