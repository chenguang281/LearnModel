#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Sys.controller.sys_menu_controller import route_sys_menu
from templates import app
from flask import make_response

"""
蓝图配置
"""
"""
sys模块路由
"""
app.register_blueprint(route_sys_menu, url_prefix="/")  # 注入sys角色模块蓝图管理


@app.errorhandler(404)
def error_404(e):
    response = make_response(
        "<script>alert('页面不存在');window.opener=null;window.open('','_self');window.close();</script>")
    return response
