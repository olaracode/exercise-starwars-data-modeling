import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
## Son las importaciones de lo necesario para trabajar SQLALCHEMY

# Base es la Clase base de sqlalchemy de donde vamos a hacer las tablas
Base = declarative_base() # CLASE

### Es la configuracion del proyecto. NO VAMOS A TOCAR NADA ARRIBA DE PERSON!


# El esquema de twitter User | Tweets

# Tabla de Usuario
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)

    # Propiedades
    name = Column(String, nullable=False)
    username = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(300), nullable=False)
    # Relaciones
    tweets = relationship("Tweet", back_populates="user")
    likes = relationship("Like", back_populates="user")
    comments = relationship("Comment", back_populates="user")

class Tweet(Base):
    ## Dunders(Double Underscore)
    __tablename__ = "tweet"
    id = Column(Integer, primary_key=True)

    ## Propiedades:
    content = Column(String(144), nullable=False)
    
    # Declaramos la clave foranea
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    # Relaciones ()
    likes = relationship("Like", back_populates="tweet")
    comments = relationship("Comment", back_populates="tweet")

class Comment(Base):
    # Genericos
    __tablename__ = "comment"
    id = Column(Integer, primary_key = True)

    ## Propiedades
    content = Column(String(144), nullable=False)

    # Claves foraneas
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    tweet_id = Column(Integer, ForeignKey("tweet.id"), nullable=False)

    # Relaciones
    likes = relationship("Like", back_populates="comment")

class Like(Base):
    # Genericos
    __tablename__ = "like"
    id = Column(Integer, primary_key=True)

    ## Clave Foranea
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    # O comment_id es True O tweet_id es True
    comment_id = Column(Integer, ForeignKey("comment.id"), nullable=True)
    tweet_id = Column(Integer, ForeignKey("tweet.id"), nullable=True)




## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
