"""__version__: 1.0
__since__: 13-02-2025
__author__: MG
__copyright__: MG
"""

from bottle import Bottle, request
from bottle import route, run
from tuto01 import Personne
from datetime import date

personne = Personne("Mohamet","Gueye",date(2000,4,22),"77 123 45 67","Dakar")


@route("/")
def index():
    return f"personne: {personne.prenom} {personne.nom}"


run(host="localhost",port=8080,debug=True, reloader=True)