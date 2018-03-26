# app/models.py

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

    # Ensures table will be named in plural and not in singular
    # as is the name of the model

class Validation(db.Model):

    __tablename__ = 'validations'
    id_chd = db.Column(db.Integer, primary_key=True)
    val_flag = db.Column(db.Boolean, default=False)

class User(db.Model):

    __tablename__ = 'users'
    id_usr = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    is_providers = db.Column(db.Boolean, default=False)
    is_resident = db.Column(db.Boolean, default=False)
    resident_fk = db.relationship('Resident_Registry', backref='user',
                                lazy='dynamic')
    administrator_fk = db.relationship('Administrator_Registry', backref='user',
                                lazy='dynamic')
    provider_fk = db.relationship('Provider_Registry', backref='user',
                                lazy='dynamic')


class Resident_Registry(db.Model):
    """
    Crea una tabella anagrafica condomini
    """

    __tablename__ = 'residents_registry'
    id_resident = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    surname = db.Column(db.String(40), nullable=False)
    cf = db.Column(db.String(16), nullable=False)
    sex = db.Column(db.Boolean, default='M')
    birthdate = db.Column(db.Date, nullable=False)
    birthplace = db.Column(db.String(20), nullable=False)
    identity_card = db.Column(db.String(8), nullable=False)
    address = db.Column(db.String(40), nullable=False)
    residence = db.Column(db.String(40), nullable=False)
    phone_home = db.Column(db.String(20), nullable=False)
    phone_mobile = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    flat = db.Column(db.String(2), nullable=False)
    thousandths = db.Column(db.Float, nullable=False)
    id_usr = db.Column(db.Integer, db.ForeignKey('users.id_usr'))


class Administrator_Registry(db.Model):

    __tablename__ = 'administrators_registry'
    id_admin = db.Column(db.Integer, primary_key=True)
    license_n = db.Column(db.String(20), nullable=False)
    p_iva = db.Column(db.String(13), nullable=False)
    condo_own_n = db.Column(db.Integer, nullable=False)
    id_usr = db.Column(db.Integer, db.ForeignKey('users.id_usr'))

    condo_fk = db.relationship('Condo', backref='administrators_registry',
                                lazy='dynamic')


class Provider_Registry(db.Model):

    __tablename__ = 'providers_registry'

    id_provider = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(40), nullable=False)
    pi_cf = db.Column(db.String(16), nullable=False)
    city = db.Column(db.String(40), nullable=False)
    district = db.Column(db.String(40), nullable=False)
    manager = db.Column(db.String(30))
    phone_home = db.Column(db.String(20), nullable=False)
    phone_mobile = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    site = db.Column(db.String(40))
    category = db.Column(db.Integer, nullable=False)
    id_usr = db.Column(db.Integer, db.ForeignKey('users.id_usr'))

    provider_fk = db.relationship('Provider_Category', backref='providers_registry',
                                lazy='dynamic')


class Provider_Category(db.Model):

    __tablename__ = 'providers_category'

    id_provider = db.Column(db.Integer, db.ForeignKey('providers_registry.id_provider'),  primary_key=True)
    boiler = db.Column(db.Integer, nullable=False)
    lifter = db.Column(db.Integer, nullable=False)
    extinguisher = db.Column(db.Integer, nullable=False)
    gas = db.Column(db.Integer, nullable=False)
    light = db.Column(db.Integer, nullable=False)
    cleaning = db.Column(db.Integer, nullable=False)
    electrician = db.Column(db.Integer, nullable=False)
    plumber = db.Column(db.Integer, nullable=False)
    lawyer = db.Column(db.Integer, nullable=False)
    achitect = db.Column(db.Integer, nullable=False)
    antenna = db.Column(db.Integer, nullable=False)
    sewer = db.Column(db.Integer, nullable=False)
    business_consultant = db.Column(db.Integer, nullable=False)
    exterminator = db.Column(db.Integer, nullable=False)
    bricklayer = db.Column(db.Integer, nullable=False)
    gardeners = db.Column(db.Integer, nullable=False)


class Condo(db.Model):

    __tablename__ = 'condos'
    id_condo = db.Column(db.Integer, primary_key=True)

    condo_name = db.Column(db.String(30), nullable=False)
    id_admin = db.Column(db.Integer, db.ForeignKey('administrators_registry.id_admin'))

    condo_data_fk = db.relationship('Condo', backref='condo',
                                lazy='dynamic')


class Condos_Data(db.Model):

    __tablename__ = 'condos_data'
    condo_name = db.Column(db.String(30))
    condo_age = db.Column(db.Date, nullable=False)
    cf_c = db.Column(db.String(16), nullable=False)
    city = db.Column(db.String(20), nullable=False)
    district = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(30), nullable=False)
    house_n = db.Column(db.Integer)
    condo_n = db.Column(db.Integer)
    stair_n = db.Column(db.Integer)
    flat_n = db.Column(db.Integer)
    cap = db.Column(db.Integer)
    id_condo = db.Column(db.Integer, db.ForeignKey('condos.id_condo'), primary_key=True)


    @property
    def password(self):

        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):

        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):

        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<USER: {}>'.format(self.username)

#inizio debug


class Employee(UserMixin, db.Model):

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Employee: {}>'.format(self.username)

# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(int(user_id))

class Department(db.Model):

    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    employees = db.relationship('Employee', backref='department',
                                lazy='dynamic')

    def __repr__(self):
        return '<Department: {}>'.format(self.name)

class Role(db.Model):

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    employees = db.relationship('Employee', backref='role',
                                lazy='dynamic')

    def __repr__(self):
        return '<Role: {}>'.format(self.name)
