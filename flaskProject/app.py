from flask import render_template, request

from orm_db import *


@app.route('/', methods=['GET', 'POST'])
def index():  # put application's code here
    if request.method == "POST":
        name = request.form['name']
        password = request.form['password']

    mesaj = "İyi Günler Dileriz !"
    try:
        kullanici = User.query.filter(User.name == name, User.password == password).first()
        print(kullanici)
        if kullanici == None:
            mesaj = "Kullanici bulunamadı"
        else:
            mesaj = "hos geldiniz" + kullanici.name
    except:
        mesaj = " sorgu hatası"

    return render_template('index.html', mesaj=mesaj)


@app.route('/yonetici')
def yonetici():  # put application's code here
    return 'Yönetici Sayfasına Hosgeldiniz.!'


if __name__ == '__main__':
    app.run()
