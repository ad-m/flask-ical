# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import (Blueprint, request, render_template, flash, url_for,
                    redirect, session)

from .forms import CalendarForm
from .utils import url2html
blueprint = Blueprint('public', __name__, static_folder="../static")


@blueprint.route("/", methods=["GET"])
def home():
    context = {}
    form = CalendarForm(request.args, csrf_enabled=False)
    context['form'] = form
    if form.validate():
        context['calendar'] = url2html(form.data['url'], 2015, 7)
        return render_template("public/calendar.html", **context)
    return render_template("public/home.html", **context)
