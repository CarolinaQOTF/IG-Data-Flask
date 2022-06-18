import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Usuario (Base):
    __tablename__ = 'Usuario'
    id = Column(Integer, primary_key= True)
    nombre = Column (String(50))
    Apellido = Column (String(50))
    Tlf = Column(Integer)
    e_mail = Column (String (50))
class Publicaciones (Base):
    __tablename__ = "Publicaciones"
    id = Column (Integer, primary_key=True)
    ubicación = Column (String(50))
    reseña = Column (String, ForeignKey("Usuario"))
    comentarios = Column (String, ForeignKey("Seguidores"))
    id_Seguidores = Column (String(50))
class Otras_Redes (Base):
    __tablename__= "Redes Sociales"
    id = Column(Integer, primary_key=True)
    twitter = Column (String)
    Facebook = Column (String, ForeignKey("Publicaciones"))
    Tumblr = Column (String)

class Seguidores (Base):
    __tablename__ = "Seguidores"
    id = Column (Integer, primary_key=True)
    id_user = Column (String)
    name = Column (String(50), ForeignKey("Usuario"))

class Siguiendo (Base):
    __tablename__ = "Siguiendo"
    id = Column (Integer, primary_key=True)
    id_users = Column (String(50), ForeignKey("Usuario"))
    


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e