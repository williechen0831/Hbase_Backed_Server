from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired
from sanic_wtf import SanicForm

class PosForm(SanicForm):
    time = StringField('time', validators=[DataRequired()])
    car = StringField('car', validators=[DataRequired()])
    x_value = StringField('x_value', validators=[DataRequired()])
    y_value = StringField('y_value', validators=[DataRequired()])
    vector_value = StringField('vector_value', validators=[DataRequired()])
    submit = SubmitField('Get in')

class LedForm(SanicForm):
    time = StringField('time', validators=[DataRequired()])
    main = StringField('main', validators=[DataRequired()])
    nums = StringField('nums', validators=[DataRequired()])
    first = StringField('first', validators=[DataRequired()])
    second = StringField('second', validators=[DataRequired()])
    third = StringField('third', validators=[DataRequired()])
    fourth =StringField('fourth', validators=[DataRequired()])
    fifth =StringField('fifth', validators=[DataRequired()])
    sixth =StringField('sixth', validators=[DataRequired()])
    submit = SubmitField('Get in')
