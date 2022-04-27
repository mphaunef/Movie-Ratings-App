'''ALL CRUD'''
from model import db, User, Movie, Rating, connect_to_db

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)
    return user

def create_movie(title, overview, release_date, poster_path):
    movie = Movie(title=title,
    overview=overview,
    release_date=release_date,
    poster_path = poster_path)
    return movie

def create_rating(user, movie, score):
    '''Pass in returned values of create_user and create_movie'''

    rating = Rating(user=user, movie=movie, score=score)
    # print(rating)
    # print(type(rating))
    return rating

    
if __name__ == '__main__':
    from server import app
    connect_to_db(app)
