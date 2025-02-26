from core.post.models import Post
from core.user.models import User

def test_create_post():
    post = Post(title="My first post", content="this is my post")
    assert post.title == "My first post"
    assert post.content == "this is my post"


def test_user_posts_relationship():
    user = User(username = "user", email="user@email.com", hashed_password="password")
    post = Post(title="My first post", content="this is my post", author=user)
    assert post.author == user
    assert user.posts == [post]
