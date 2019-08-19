#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
import os


class Application(Flask):
    def __init__(self, import_name, template_folder=None, static_folder=None):
        super(Application, self).__init__(import_name, template_folder=template_folder, static_folder=static_folder)
        self.config.from_pyfile('config/base_setting.py')

        db.init_app(self)


db = SQLAlchemy()
app = Application(__name__, template_folder='../templates', static_folder='../static')


app.secret_key = os.urandom(24)
manager = Manager(app)
