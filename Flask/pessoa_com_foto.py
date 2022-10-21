from Flask import bd
import os
from flask import Flask, render_template, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'C:\\pycharm_projects\\Flask\\static\\images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def menu():
    return render_template('menu.html')


@app.route('/upImgs')
def up_imgs():
    return render_template('up_imgs.html')


@app.route('/getImgs', methods=['POST'])
def get_imgs():
    global msg
    if request.method == 'POST':
        # check if the post request has the file part
        print(request.files)
        if 'pImagem' not in request.files:
            msg = "Não existem arquivos no formulário"
        else:
            arq = request.files['pImagem']
            if arq.filename == '':
                msg = "Arquivo não selecionado no formulário"
            else:
                if arq and allowed_file(arq.filename):
                    arqname = secure_filename(arq.filename)
                    arq.save(os.path.join(app.config['UPLOAD_FOLDER'], arqname))
                    nome = request.form['pNome']
                    end = request.form['pEndereco']
                    tel = request.form['pTelefone']
                    dsc = "/static/images/" + arqname

                    # Incluindo dados na tabela
                    mysql = bd.SQL("root", "uniceub", "tb_pessoa")
                    comando = "INSERT INTO tb_pessoa(nme_pessoa, end_pessoa, tel_pessoa," \
                              " dsc_path_imagem) VALUES (%s, %s, %s, %s);"

                    if mysql.executar(comando, [nome, end, tel, dsc]):
                        msg = arqname + " armazenado com sucessso!!!"
                    else:
                        msg = "Falha na inclusão de imagem."

    return render_template('get_imgs.html', msg=msg)


@app.route('/listImgs')
def list_imgs():
    # Consultando dados na tabela
    mysql = bd.SQL("root", "uniceub", "tb_pessoa")
    comando = "SELECT * FROM tb_pessoa;"
    imagens = ""
    cs = mysql.consultar(comando, [])
    for (idt, nme, end, tel, dsc) in cs:
        imagens += "<TR>\n"
        imagens += "<TD>" + nme + "</TD>\n"
        imagens += "<TD>" + str(end) + "</TD>\n"
        imagens += "<TD>" + str(tel) + "</TD>\n"
        imagens += "<TD><IMG SRC='" + dsc + "'></TD>\n"
        imagens += "</TR>\n"

    return render_template('list_imgs.html', imagens=imagens)


app.run(debug=True)
