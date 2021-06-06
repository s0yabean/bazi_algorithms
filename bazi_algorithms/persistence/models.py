"""Database models."""
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from .. import db

# class Sessions_table(db.Model):
# 	"""sessions"""

# 	__tablename__ = 'natal_chart'
# 	__table_args__ = {'extend_existing': True} 

# 	id = db.Column(
# 		db.Integer,
# 		nullable=False
# 	)
# 	session_id = db.Column(
# 		db.String(255),
# 		nullable=False
# 	)
# 	data = db.Column(
# 		db.blob,
# 	)
# 	expiry = db.Column(
# 		db.DateTime,
# 	)

class User(UserMixin, db.Model):
	"""User account model."""

	__tablename__ = 'user'
	id = db.Column(
		db.Integer,
		primary_key=True
	)
	name = db.Column(
		db.String(100),
		nullable=False,
		unique=False
	)
	email = db.Column(
		db.String(40),
		unique=True,
		nullable=False
	)
	password = db.Column(
		db.String(200),
		primary_key=False,
		unique=False,
		nullable=False
	)
	natal_chart_id = db.Column(
		db.Integer,
		#db.ForeignKey('natal_chart.id'), if uncomment, cannot edit directly in UI
		unique=True,
		nullable=True
	)
	created_on = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=True
    )
	last_login = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=True
    )

	def set_password(self, password):
		"""Create hashed password."""
		self.password = generate_password_hash(password, method='sha256')

	def check_password(self, password):
		"""Check hashed password."""
		return check_password_hash(self.password, password)

	def __repr__(self):
		return '<User {}>'.format(self.username)

class NatalChart(db.Model):
	"""Natal Charts"""

	__tablename__ = 'natal_chart'
	id = db.Column(
		db.Integer,
		primary_key=True,
		unique=True
	)
	user_id = db.Column(
		db.Integer,
		db.ForeignKey('user.id'),
		nullable=False,
		unique=False,
	)
	contact_name = db.Column(
		db.String(100),
		unique=False,
		nullable=False
	)
	hour_s = db.Column(
		db.String(10),
		unique=False,
		nullable=True
	)
	hour_e = db.Column(
		db.String(10),
		unique=False,
		nullable=True
	)
	day_s = db.Column(
		db.String(10),
		unique=False,
		nullable=False
	)
	day_e = db.Column(
		db.String(10),
		unique=False,
		nullable=False
	)
	month_s = db.Column(
		db.String(10),
		unique=False,
		nullable=False
	)
	month_e = db.Column(
		db.String(10),
		unique=False,
		nullable=False
	)
	year_s = db.Column(
		db.String(10),
		unique=False,
		nullable=False
	)
	year_e = db.Column(
		db.String(10),
		unique=False,
		nullable=False
	)

class ExternalPillars(db.Model):
	"""External Charts"""

	__tablename__ = 'external_pillars'
	id = db.Column(
		db.Integer,
		primary_key=True
	)
	date = db.Column(
		db.String(20),
		nullable=False,
		unique=True
	)
	day_pillar = db.Column(
		db.String(20),
		unique=False,
		nullable=False
	)
	month_pillar = db.Column(
		db.String(20),
		unique=False,
		nullable=False
	)
	year_pillar = db.Column(
		db.String(20),
		unique=False,
		nullable=False
	)

