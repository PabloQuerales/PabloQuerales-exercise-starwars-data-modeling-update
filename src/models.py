import os
import sys
from typing import List
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import create_engine, ForeignKey
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    password: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    favorites: Mapped[List["Favorites"]] = relationship()

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    climate: Mapped[str] = mapped_column(nullable=False)
    diameter: Mapped[str] = mapped_column(nullable=False)
    gravity: Mapped[str] = mapped_column(nullable=False)
    favorites: Mapped[List["Favorites"]] = relationship()

class Persons(Base):
    __tablename__ = 'persons'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    eyes_color: Mapped[str] = mapped_column(nullable=False)
    hair_color: Mapped[str] = mapped_column(nullable=False)
    heigth: Mapped[str] = mapped_column(nullable=False)
    favorites: Mapped[List["Favorites"]] = relationship()

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    person_id: Mapped[int] = mapped_column(ForeignKey("persons.id"))
    planet_id: Mapped[int] = mapped_column(ForeignKey("planets.id"))

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
