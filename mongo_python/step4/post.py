
from databse import Database

class Post:
    def __init__(self, blog_id, title, content, author, date , id ):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = date
        self.id = id
        
    def save_to_mongodb(self):
        Database.insert( collection='posts',  data=self.json() )
        
    def json(self):
        return {
            'id': self.id,
            'title' : self.title,
            'blog_id' : self.blog_id,
            'content' : self.content,
            'author' : self.author,
            'created_date' : self.date
            
            }
    @staticmethod
    def from_mongo(id):
        return Database.find_one( collection='posts', query={'id': id })
    
    @staticmethod
    def from_blog(id):
        return [ post for post in Database.find( collection='posts', query={'blog_id': id })]