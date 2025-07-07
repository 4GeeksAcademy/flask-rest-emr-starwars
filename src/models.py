from flask_sqlalchemy import SQLAlchemy
from typing import List
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date

db = SQLAlchemy()


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    subscription_date: Mapped[date] = mapped_column(db.Date, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    favorites = relationship("Favorite", back_populates="character", cascade="all, delete")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "subscription_date": self.subscription_date,
            "is_active": self.is_active,
        }


class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    climate: Mapped [str] = mapped_column(String(100))
    terrain: Mapped [str] = mapped_column(String(100))
    population: Mapped[int] = mapped_column()

    favorites = relationship("Favorite", back_populates="character", cascade="all, delete")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "terrain": self.terrain,
            "population": self.population,
        }


class Character(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    birth_year: Mapped [str] = mapped_column(String(20))
    gender: Mapped [str] = mapped_column(String(20))
    height: Mapped[int] = mapped_column()

    favorites = relationship("Favorite", back_populates="character", cascade="all, delete")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "height": self.height,
        }


class Favorite(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    planet_id:Mapped[int] = mapped_column(ForeignKey("planet.id"), nullable=False)
    character_id:Mapped[int] = mapped_column(ForeignKey("character.id"), nullable=False)

    user = relationship("User", back_populates="favorites")
    planet = relationship("Planter", back_populates="favorites")
    character = relationship("Character", back_populates="favorites")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
            "character_id": self.character_id,
        }
