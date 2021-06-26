

from post import Post
from database import Database

# Lets create Blog class and call

Database.initialize()

# what do you want from blog class?

blog = Blog( author="harsha",
            title="Sample title",
            description="Sample Description" )


blog.new_post()

blog.save_to_mongo()

blog.from_mongo()

blog.get_posts()  