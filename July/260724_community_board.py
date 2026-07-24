import hashlib

class Member:
    def __init__(self, name: str, username: str, password: str):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print("Name: " + self.name)
        print("Username: " + self.username)

class Post:
    def __init__(self, title: str, content: str, author: str):
        self.title = title
        self.content = content
        self.author = author

# make member with input()
def make_member():
    name = input("Enter name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    return Member(name, username, password)

# make post with input()
def make_post(members):
    title = input("Enter title: ")
    content = input("Enter content: ")
    name = input("Who is the author: ")

    found = False
    for member in members:
        if member.username == name:
            author = member
            found = True

    if not found:
        print("Author does not exist.")
        return None

    return Member(title, content, author)

#password hashing
def password_hash(password):
    return hashlib.sha256(password.encode('utf-8'))

if __name__ == "__main__":
    members = []

    a = Member("a", "aa", "aaa")
    b = Member("b", "bb", "bbb")
    c = Member("c", "cc", "ccc")

    members.append(a)
    members.append(b)
    members.append(c)

    print("----------------------Member for loop----------------------")

    for member in members:
        member.display()

    posts = []

    a_first = Post("a_first", "Hello I am a. I like icecream.", "aa")
    a_second = Post("a_second", "I like playing video games.", "aa") 
    a_third = Post("a_third", "Icecream is the best.", "aa") 

    b_first = Post("b_first", "Hello I am b. I like tomato.", "bb")
    b_second = Post("b_second", "I do not like icecream.", "bb") 
    b_third = Post("b_third", "But perhaps tomato icecream is good.", "bb") 

    c_first = Post("c_first", "Hello I am c. I like coffee.", "cc")
    c_second = Post("c_second", "I like coffee jelly.", "cc") 
    c_third = Post("c_third", "I like coffee milkshake.", "cc") 

    posts.append(a_first)
    posts.append(a_second)
    posts.append(a_third)
    
    posts.append(b_first)
    posts.append(b_second)
    posts.append(b_third)
    
    posts.append(c_first)
    posts.append(c_second)
    posts.append(c_third)

    #특정 유저: b
    print("----------------------특정유저 for loop----------------------")

    for post in posts:
        if post.author == "bb":
            print("Title: " + post.title)


    #특정 단어: icecream
    print("----------------------특정단어 for loop----------------------")

    for post in posts:
        words = post.content.strip(".").lower().split()
        if "icecream" in words:
            print("Title: " + post.title)


    print(password_hash(a.password))