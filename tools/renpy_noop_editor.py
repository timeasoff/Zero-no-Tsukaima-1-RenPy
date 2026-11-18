#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
No-op редактор для Ren'Py SDK.

При ошибке скрипта Ren'Py пишет traceback.txt и пытается открыть его в редакторе
(`renpy.editor.launch_editor`). В headless-контейнере редактора нет, а `xdg-open`
отсутствует — в лог летит FileNotFoundError. `RENPY_EDIT_PY` (его читает
`renpy.editor.init()`) указывает SDK на этот файл, и «редактор» ничего не делает:
traceback.txt по-прежнему пишется, но вывода про редактор больше нет.

Файл существует только как цель для переменной окружения RENPY_EDIT_PY.
"""


class Editor(object):
    def begin(self, new_window=False, **kwargs):
        pass

    def end(self, **kwargs):
        pass

    def open(self, filename, line=None, **kwargs):
        pass

    def open_project(self, directory):
        pass
