"""
Summary: Dynaconf and Flask with configuration reload
"""
from dynaconf import Dynaconf
from flask import Flask, redirect, url_for

app = Flask(__name__)
settings = Dynaconf(
    settings_file="settings.yaml",
)


@app.get("/")
def index():
    """Return the `main` configuration object."""
    return str(settings.get("MAIN"))


@app.get("/reload")
def reload():
    """Endpoint for reloading the configuration file. Redirects to the index page."""
    settings.reload()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()
