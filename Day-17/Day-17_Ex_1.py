class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.following = 0
        self.followers = 0

    def follow(self,user):
        user.followers += 1
        self.following += 1


user1 = User("001", "Neil")
user2 = User("069", "Niramay")

user1.follow(user2)

print(user1.following)
print(user2.followers)

