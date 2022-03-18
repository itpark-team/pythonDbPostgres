from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from user import User
import json
from user import DeclarativeBase

engine = create_engine('postgresql+psycopg2://puser:12345@151.248.113.116/pdb')

# DeclarativeBase.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# newUser = User(login="user10", password="user10p", name="user10name")
# session.add(newUser)
# session.commit()

for currentUser in session.query(User):
    print(json.dumps(currentUser.as_dict()))
    #print(currentUser.id, " ", currentUser.login, " ", currentUser.password, " ", currentUser.name)
