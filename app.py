from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def catalogo():
    items = [
        {
            "name": "Libreta",
            "price": "$23",
            "description": "Libreta profesional Scribe cuadro grande",
            "image": "./img/Libreta.jpg"
        },
        {
            "name": "Barra de plastilina",
            "price": "$11",
            "description": "Barra de plastilina color rojo",
            "image": "./img/Plastilina.jpg"
        },
        {
            "name": "Resistol en barra",
            "price": "$16",
            "description": "Resistol en barra chico",
            "image": "./img/Pritt.jpg"
        },
        {
            "name": "Lápices de colores",
            "price": "$60",
            "description": "Colores 24 piezas + 3 incluye color oro, plata y cobre",
            "image": "./img/ColoresVividel.jpg"
        },
        {
            "name": "Lapicero Bic",
            "price": "$6",
            "description": "Lapicero Bic de color rojo, azul y negro, se venden por separado",
            "image": "./img/lapicerosBic.png"
        },
        {
            "name": "Lapiz Duo",
            "price": "$6",
            "description": "Lápiz Duo Dixon",
            "image": "./img/lapizDuo.jpg"
        }
        # Puedes agregar más elementos aquí
    ]
    return render_template('catalogo.html', items=items)

if __name__ == '__main__':
    app.run()
