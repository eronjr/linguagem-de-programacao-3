from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField, StringField
from wtforms.validators import InputRequired, Length, ValidationError
from models.User import Users

class RegisterForm(FlaskForm):
	
	username = StringField(validators=[InputRequired(), Length(min=4, max=120)],render_kw={"placeholder": "Usuário"})

	email = EmailField(validators=[InputRequired(), Length(min=4, max=120)],render_kw={"placeholder": "Email"})

	password = PasswordField(validators=[InputRequired(), Length(min=4, max=120)],render_kw={"placeholder": "Senha"})

	submit = SubmitField("Cadastrar")
	
	def validate_email(self, email):
		existing_email = Users.query.filter_by(email=email.data).first()
		if existing_email:
			raise ValidationError("Email já cadastrado")

class LoginForm(FlaskForm):
	email = EmailField(
		validators=[InputRequired(), Length(min=4, max=120)],
		render_kw={"placeholder": "Email"}
	)

	password = PasswordField(
		validators=[InputRequired(), Length(min=4, max=120)],
		render_kw={"placeholder": "Senha"}
	)

	submit = SubmitField("Login")
