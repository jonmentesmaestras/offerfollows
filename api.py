from flask import Flask, request, jsonify
from ads_number_final import get_ads_number

app = Flask(__name__)

@app.route('/getads', methods=['GET'])
def get_ads():
    query = request.args.get('query', '')
    
    # Inicializar el navegador para cada solicitud
    
    numero_anuncios = get_ads_number(query)
    
    
    print(query)

    response = {
        "message": "Success",
        "code": 200,
        "error": False,
        "status": "Ok",
        "stage": "Ending",
        "info": {},
        "data": [
            {
                "query": query,
                "totalAds": numero_anuncios
            }
        ]
    }
    return jsonify(response)
@app.route('/status', methods=['GET'])
def status():
    response = {
        "status": "OK",
        "message": "server running"
    }
    return jsonify(response)
    
if __name__ == '__main__':
    app.run(host='localhost', port=3005)