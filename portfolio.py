#!/usr/local/bin/python3
import cgi
form = cgi.FieldStorage()



#cgi-bin ordner erstellen, wo die .py datei drin ist
#Zugriffsrechte: um auf die Datei zugreifen zu können muss ich chmod 777 cgi-bin/color_check.py ins Terminal eingeben. (777 = read, write,...)
#wenn ich das Programm laufen lassen will muss ich den Local Host im terminal starten: python3 -m http.server --cgi 8000
#im Browser: http://localhost:8000 eingeben


#GITHUB:
#$ git init
#$ git add .
#$ git commit -m "First commit"
#$ git push