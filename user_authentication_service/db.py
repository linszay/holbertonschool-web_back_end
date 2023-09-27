#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """returns a user object & saves user to db"""
        """create a new user"""
        user = User(email=email, hashed_password=hashed_password)
        """add a new user to db session"""
        self._session.add(user)
        """commit changes to save user"""
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """takes in keywords and returns 1st row of users"""
        try:
            """filer user by keyword args"""
            """raise NoResultFound and InvalidRequestError if no reult found"""
            return self._session.query(User).filter_by(**kwargs).one()
        except (NoResultFound, InvalidRequestError):
            raise

    def update_user(self, user_id: int, **kwargs):
            """find user by user_id"""
            user = self.find_user_by(id=user_id)
            """check keyward args against user attr"""
            for key in kwargs:
                if not hasattr(User, key):
                    raise ValueError(f"Invalid attribute: {key}")
            """update the users attributes"""
            for key, value in kwargs.items():
                setattr(user, key, value)
            """commit changes to db"""
            self._session.commit()
