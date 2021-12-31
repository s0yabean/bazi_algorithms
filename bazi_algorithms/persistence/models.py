"""Database models."""
from flask_login import UserMixin
from stripe.api_resources import plan
from werkzeug.security import check_password_hash, generate_password_hash
from .. import db
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import os

class StripeCustomer(db.Model):
	__tablename__ = 'stripe_customer'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	email = db.Column(db.String(40), unique=False, nullable=True)
	payment_status = db.Column(db.String(40), unique=False, nullable=False)
	amount_subtotal = db.Column(db.Numeric, unique=False, nullable=False)
	amount_total = db.Column(db.Numeric, unique=False, nullable=False)
	currency = db.Column(db.String(40), unique=False, nullable=False)
	date = db.Column(db.BigInteger)
	stripe_session_id = db.Column(db.String(255), nullable=False)
	stripe_customer_id = db.Column(db.String(255), nullable=False)
	stripe_subscription_id = db.Column(db.String(255), nullable=True)

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
	plan = db.Column(
		db.String(40),
		primary_key=False,
		unique=False,
		nullable=False
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

	def get_reset_token(self, expires_sec=3600):
		s = Serializer(os.getenv('SECRET_KEY'), expires_sec)
		return s.dumps({'user_id': self.id}).decode('utf-8')

	

	@staticmethod
	def verify_reset_token(token):
		s = Serializer(os.getenv('SECRET_KEY'))
		try:
			user_id = s.loads(token)['user_id']
		except:
			return None
		return User.query.filter_by(id = user_id).first()  
class NatalChart(db.Model):
	"""Natal Charts"""

	__tablename__ = 'natal_chart'
	id = db.Column(
		db.Integer,
		primary_key=True,
		autoincrement=True
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
	gender = db.Column(
		db.String(10)
	)
	self_chart = db.Column(
		db.Boolean
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

