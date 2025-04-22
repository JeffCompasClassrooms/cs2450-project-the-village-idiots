import tinydb
from tinydb import where
 
def new_user(db, username, hashed_password, first_name, last_name, iq):
    users = db.table('users')
    User = tinydb.Query()
    if users.get(User.username == username):
        return None
    user_record = {
            'first_name': first_name,
            'last_name': last_name,
            'iq': iq,
            'username': username,
            'password': hashed_password,
            'friends': [],
            'points': 0,
            }
    return users.insert(user_record)

def get_user(db, username, hashed_password):
    user = db.table('users').get(where('username') == username and where('password') == hashed_password)
    return user

def get_user_by_name(db, username):
    return db.table('users').get(where('username') == username)

def delete_user(db, username, password):
    users = db.table('users')
    User = tinydb.Query()
    return users.remove((User.username == username) &
            (User.password == password))

def add_user_friend(db, user, friend):
    users = db.table('users')
    users.update({'friends': user['friends']}, where('username') == user['username'])

def remove_user_friend(db, user, friend):
    users = db.table('users')
    User = tinydb.Query()
    if friend in user['friends']:
        user['friends'].remove(friend)
        users.upsert(user, (User.username == user['username']) &
                (User.password == user['password']))
        return 'Friend {} successfully unfriended!'.format(friend), 'success'
    return 'You are not friends with {}.'.format(friend), 'warning'

def get_user_friends(db, user):
    users = db.table('users')
    User = tinydb.Query()
    friends = []
    for friend in user['friends']:
        friends.append(users.get(User.username == friend))
    return friends
