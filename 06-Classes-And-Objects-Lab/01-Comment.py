class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes

# in judge submit only the code upto here, lines below are additional checks
comment = Comment('user1', 'I like this')
print(comment.username)
print(comment.content)