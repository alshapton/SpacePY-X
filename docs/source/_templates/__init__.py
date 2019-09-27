from os import path


def get_html_theme_path():
    """Return list of HTML theme paths."""
    cur_dir = path.abspath(path.dirname(path.dirname(__file__)))
    return cur_dir


def setup(app):
    app.add_html_theme('stsci_rtd_theme', get_html_theme_path())
