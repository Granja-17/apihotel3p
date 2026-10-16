from flask_restful import Resource,reqparse

lista_hoteis =[
    {"hotel_id": "Fama", "nome": "Fama Hotel", "estrelas": 5.0, "diaria": 199.99, "cidade": "Famalicão"},
    {"hotel_id": "Hijo", "nome": "Hijo Hotel", "estrelas": 4.9, "diaria": 197.99, "cidade": "Argentina"},
    {"hotel_id": "Tripeiro", "nome": "Tripeiro Hotel", "estrelas": 4.7, "diaria": 183.99, "cidade": "Porto"}
 ]

class Hoteis(Resource):
    def get(self):
        return{"hoteis":lista_hoteis}

class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument("nome", type=str, required=True, help="Nome Obrigatório")
    argumentos.add_argument("estrelas", type=str, required=True, help="Estrelas Obrigatório")
    argumentos.add_argument("diaria", type=str, required=True, help="Diária Obrigatório")
    argumentos.add_argument("cidade", type=str, required=True, help="Cidade Obrigatório")

    def get(self, id_hotel):
        for hotel in lista_hoteis:
            if hotel["hotel_id"] == id_hotel:
                return hotel, 200
        return {"message": "Hotel not found"}, 404


    def post(self,id_hotel):
        dados = Hotel.argumentos.parse_args() #Dicionário
        for hotel in lista_hoteis:
            if hotel["hotel_id"] == id_hotel:
                return { "message": "Hotel with this id already exists"}
        novo_hotel = {"hotel_id": id_hotel, **dados }
        lista_hoteis.append(novo_hotel)
        return hotel,200

    def put(self,id_hotel):
        ...

    def delete(self,id_hotel):
        ...