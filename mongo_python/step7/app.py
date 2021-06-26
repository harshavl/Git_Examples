

from post import Post
from database import Database

# verifying that all post Methods work

Database.initialize()

'''
post = Post(" Post1 title", "Post1 content", "Post1 author " )
post2 = Post(" Post2 title", "Post2 content", "Post2 author " )

post2.content = "Some different"

print( post.content)
print( post2.content)
'''

'''
post = Post( blog_id='12',
            title='Another great post',
            content='THis is some sample content',
            author='Jose')

'''

# comment after insert
#post.save_to_mongodb()

# creates posts collections an insert above json files
#
# verify in the mongodb 
# db.posts.find({}).pretty()


posts = Post.from_blog('12')
print( posts )

#for post in posts:
#   print(post)