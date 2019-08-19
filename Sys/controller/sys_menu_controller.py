#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

route_sys_menu = Blueprint("sys_menu", __name__)


@route_sys_menu.route("/")
def index():
    print(11111111111)
    return render_template("index.html")
