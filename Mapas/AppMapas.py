from util import bd
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/simples')
def simples():
    sql = bd.SQL('root', 'uniceub', 'bd_mapas')
    cmd = 'SELECT idt_ponto, lat_ponto, lng_ponto FROM tb_ponto'
    cs = sql.consultar(cmd, [])
    marcadores = ''
    icon = '{icon: greenIcon}'
    for idt, lat, lng in cs:
        marcadores += f'var mk_{idt} = L.marker([{lat}, {lng}], {icon}).addTo(m);\n'
    cs.close()
    return render_template('simples.html', marcadores=marcadores)


@app.route('/dialogos')
def dialogos():
    sql = bd.SQL('root', 'uniceub', 'bd_mapas')
    cmd = 'SELECT idt_ponto, lat_ponto, lng_ponto, nme_ponto FROM tb_ponto'
    cs = sql.consultar(cmd, [])
    marcadores = ''
    popups = ''
    for idt, lat, lng, nme in cs:
        marcadores += f'var mk_{idt} = L.marker([{lat}, {lng}]).addTo(m);\n'
    cs.close()
    return render_template('dialogos.html', marcadores=marcadores, popups=popups)


@app.route('/figuras')
def figuras():
    sql = bd.SQL('root', 'uniceub', 'bd_mapas')
    cmd = 'SELECT idt_ponto, lat_ponto, lng_ponto, nme_ponto FROM tb_ponto'
    cs = sql.consultar(cmd, [])
    figs = ''
    popups = ''
    for idt, lat, lng, nme in cs:
        if nme != 'Represa Santa Maria':
            figs += 'var circle_' + str(idt) + \
                    ' = L.circle([' + str(lat) + \
                    ', ' + str(lng) + '], {\n ' + \
                    'color: "blue", \n' + \
                    'fillColor: "blue",\n' + \
                    'fillOpacity: 0.5,\n' + \
                    'radius: 600\n' + \
                    ' }).addTo(m);\n'
            popups += 'circle_{}.bindPopup("{}");'.format(idt, nme)
        else:
            figs += 'var poly = L.polygon([\n' + \
                    '[' + str(lat) + ', ' + str(lng) + '- 0.05],' + \
                    '[' + str(lat) + ', ' + str(lng) + ' + 0.05],' + \
                    '[' + str(lat) + ' + 0.04, ' + str(lng) + ' + 0.05],' + \
                    '[' + str(lat) + ' + 0.04, ' + str(lng) + ' - 0.05]' + \
                    ']).addTo(m);'
            popups += 'poly.bindPopup("{}");'.format(nme)

    cs.close()
    return render_template('figuras.html', figs=figs, popups=popups)


app.run(debug=True)
