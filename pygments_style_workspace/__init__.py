# -*- coding: utf-8 -*-
"""
    workspace
    ~~~~~~

    Port of the workspace color scheme.

    :copyright: Copyright 2019 Bilel Omrani
    :license: MIT, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import (
    Comment,
    Error,
    Generic,
    Keyword,
    Literal,
    Name,
    Number,
    Operator,
    Other,
    String,
    Text,
    Whitespace,
)


class WorkspaceStyle(Style):
    """
    Port of the workspace color scheme.
    """

    orange = "#f25000"
    magenta = "#b50059"
    purple = "#7d15c3"
    blue = "#0087bd"
    deepblue = "#232692"
    grey = "#969896"
    black = "#333333"

    default_style = black

    styles = {
        Comment: grey,
        Comment.Preproc: grey,
        Comment.Special: grey,
        Keyword: "bold " + magenta,
        Keyword.Declaration: magenta,
        Keyword.Constant: magenta,
        Keyword.Pseudo: magenta,
        Keyword.Reserved: magenta,
        Keyword.Namespace: magenta,
        Keyword.Type: "italic " + magenta,
        Keyword.Other: magenta,
        Other: magenta,
        Operator: magenta,
        Operator.Word: magenta,
        Name.Attribute: magenta,
        Name.Builtin: magenta,
        Name.Builtin.Pseudo: magenta,
        Name.Class: purple,
        Name.Constant: black,
        Name.Decorator: magenta,
        Name.Entity: purple,
        Name.Exception: orange,
        Name.Function: purple,
        Name.Label: black,
        Name.Namespace: black,
        Name.Tag: black,
        Name.Variable: black,
        Generic.Heading: "bold " + deepblue,
        Generic.Subheading: "italic " + deepblue,
        Generic.Deleted: orange,
        Generic.Inserted: black,
        Generic.Error: orange,
        Generic.Emph: "italic",
        Generic.Strong: "bold",
        Generic.Prompt: "bold " + deepblue,
        Generic.Output: black,
        Generic.Traceback: orange,
        String: deepblue,
        String.Escape: deepblue,
        String.Interpol: deepblue,
        String.Regex: deepblue,
        String.Doc: "italic " + deepblue,
        String.Symbol: deepblue,
        String.Other: deepblue,
        Number: blue,
        Error: "bg:#F00",
    }
