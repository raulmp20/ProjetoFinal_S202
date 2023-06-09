class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class ForumCLI(SimpleCLI):
    def __init__(self, forum_model):
        super().__init__()
        self.forumModel = forum_model
        self.add_command("create_user", self.create_user)
        self.add_command("create_post", self.create_post)
        self.add_command("create_forum", self.create_forum)
        self.add_command("get_users", self.get_users)
        self.add_command("get_posts", self.get_posts)
        self.add_command("get_forums", self.get_forums)
        self.add_command("update_user", self.update_user)
        self.add_command("update_post", self.update_post)
        self.add_command("update_forum", self.update_forum)
        self.add_command("delete_user", self.delete_user)
        self.add_command("delete_post", self.delete_post)
        self.add_command("delete_forum", self.delete_forum)

    def create_user(self):
        name = input("Enter the name: ")
        email = input("Enter the email: ")
        password = input("Enter the password: ")
        self.forumModel.create_user(name, email, password)

    def create_post(self):
        title = input("Enter the title: ")
        content = input("Enter the content: ")
        autor = input("Enter the author: ")
        self.forumModel.create_post(title, content, autor)

    def create_forum(self):
        name = input("Enter the name: ")
        description = input("Enter the description: ")
        post = input("Enter the post: ")
        self.forumModel.create_forum(name, description, post)

    def get_users(self):
        users = self.forumModel.get_users()
        if users:
            for user in users:
                print(f"Name: {user}")
        else:
            print("No users found.")

    def get_posts(self):
        autor = input("Enter the author name: ")
        posts = self.forumModel.get_posts(autor)
        if posts:
            for post in posts:
                print(f"Title: {post}")
        else:
            print("No posts found.")

    def get_forums(self):
        forums = self.forumModel.get_forums()
        if forums:
            for forum in forums:
                print(f"Name: {forum}")
        else:
            print("No forums found.")

    def update_user(self):
        name = input("Enter the name: ")
        new_password = input("Enter the new password: ")
        self.forumModel.update_user(name, new_password)
        print("User updated successfully.")

    def update_post(self):
        title = input("Enter the title: ")
        new_content = input("Enter the new content: ")
        self.forumModel.update_post(title, new_content)
        print("Post updated successfully.")

    def update_forum(self):
        name = input("Enter the name: ")
        new_description = input("Enter the new description: ")
        self.forumModel.update_forum(name, new_description)
        print("Forum updated successfully.")

    def delete_user(self):
        name = input("Enter the name: ")
        self.forumModel.delete_user(name)
        print("User deleted successfully.")

    def delete_post(self):
        title = input("Enter the title: ")
        self.forumModel.delete_post(title)
        print("Post deleted successfully.")

    def delete_forum(self):
        name = input("Enter the name: ")
        self.forumModel.delete_forum(name)
        print("Forum deleted successfully.")

    def run(self):
        print("Welcome to the Forum CLI!")
        print(
            "Available commands: create_user, create_post, create_forum, get_users, get_posts, get_forums, update_user, update_post, update_forum, delete_user, delete_post, delete_forum, quit")

        super().run()
