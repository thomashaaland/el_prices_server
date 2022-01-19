#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fastapi import FastAPI
from fastapi import Request

from fastapi.templating import Jinja2Templates

import eldb.eldb as eldb

# Create app variable (FastAPI instance)
app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home():
    """Root route for the web app.
    This will return a the last date it was updated with..
    """

    message = eldb.get_most_recent_date()
    return message


def main():
    """Called when run as a script.

    Launches the web app.
    """
    import uvicorn
    uvicorn.run("el_app:app", debug = True, host="192.168.100.6", port=5000, log_level="info")

if __name__ == "__main__":
    main()
