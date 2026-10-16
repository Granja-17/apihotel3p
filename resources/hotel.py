from flask_restful import Resource

lista_hoteis =[
    {"hotel_id": "Fama", "nome": "Fama Hotel", "estrelas": 5.0, "diaria": 199.99, "cidade": "Famalicão"},
    {"hotel_id": "Hijo", "nome": "Hijo Hotel", "estrelas": 4.9, "diaria": 197.99, "cidade": "Argentina"},
    {"hotel_id": "Tripeiro", "nome": "Tripeiro Hotel", "estrelas": 4.7, "diaria": 183.99, "cidade": "Porto"}
 ]

class Hoteis(Resource):
    def get(self):
        return{"hoteis":lista_hoteis}