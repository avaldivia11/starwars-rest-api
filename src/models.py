from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(200),unique=True)
    password = db.Column(db.String(300))
    favorites = db.relationship('Favorite', cascade="all,delete",backref="user")

    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "password": self.password
        }
    
    def serialize_whit_favorite(self):
        return{
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "password": self.password,
            "favorites": self.get_favorites()
        }

    def get_favorites(self):
        return list(map(lambda favorite:favorite.serialize(),self.favorites))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Favorite(db.Model):
    __tablename__='favorites'
    id = db.Column(db.Integer, primary_key=True)
    name_favorite = db.Column(db.String(200))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    
    
    def serialize(self):
        return {
            "id": self.id,
            "name_favorite":self.name_favorite
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Character(db.Model):
    __tablename__='characters'
    id = db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    height= db.Column(db.Integer)
    mass = db.Column(db.Integer)
    hair_color = db.Column(db.String(100))
    skin_color = db.Column(db.String(100))
    eye_color = db.Column(db.String(100))
    birth_year = db.Column(db.Integer)
    gender = db.Column(db.String(100))

    def serialize(self):
        return {
            "id":self.id,
            "name":self.name,
            "height":self.height,
            "mass":self.mass,
            "hair_color":self.hair_color,
            "skin_color":self.skin_color,
            "eye_color":self.eye_color,
            "birth_year":self.birth_year,
            "gender": self.gender
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Planet(db.Model):
    __tablename__='planets'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    diameter = db.Column(db.Integer)
    rotation_period = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    gravity = db.Column(db.Integer)
    population = db.Column(db.Integer)
    climate = db.Column(db.String)

    def serialize(self):
        return {
            "id":self.id,
            "name":self.name,
            "diameter":self.diameter,
            "rotation_period":self.rotation_period,
            "orbital_period":self.orbital_period,
            "gravity":self.gravity,
            "population":self.population,
            "climate":self.climate
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit

class Vehicle(db.Model):
    __tablename__='vehicles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    model = db.Column(db.String(100))
    vehicle_class = db.Column(db.String(100))
    cargo_capacity = db.Column(db.Integer)
    passenger = db.Column(db.Integer)

    def serialize(self):
        return {
            "id":self.id,
            "name":self.name,
            "model":self.model,
            "vehicle_class":self.vehicle_class,
            "cargo_capacity":self.cargo_capacity,
            "passenger":self.passenger
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()