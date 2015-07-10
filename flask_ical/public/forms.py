# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired, URL


class CalendarForm(Form):
    url = TextField('URL', validators=[DataRequired(), URL()])
