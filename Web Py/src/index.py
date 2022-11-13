from flask import Flask, render_template

app = Flask (__name__)


#Inicio#
@app.route ('/')
def home ():
    return render_template ('home.html')

#Acerca de la pagina#
@app.route ('/about')
def about ():
    return render_template ('about.html')






if __name__ == '__main__':
    app.run(debug=True)

