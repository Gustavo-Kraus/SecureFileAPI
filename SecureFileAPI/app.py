from flask import Flask, jsonify, send_file, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
import os
import urllib.parse
from datetime import timedelta
from asgiref.wsgi import WsgiToAsgi
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

app = Flask(__name__)

# Configuração para token
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY", "chave_padrao_insegura")
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=10)
jwt = JWTManager(app)

# Converte o flask app para ASGI
asgi_app = WsgiToAsgi(app)

# Função para gerar o token
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    valid_user = os.getenv("APP_USERNAME")
    valid_pass = os.getenv("APP_PASSWORD")

    if username == valid_user and password == valid_pass:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"erro": "Credenciais inválidas"}), 401

# Endpoint para baixar o arquivo
@app.route('/baixar_arquivo', methods=['GET'])
@jwt_required()
def baixar_arquivo():
    caminho_arquivo = request.args.get('file_path')

    if not caminho_arquivo:
        return jsonify({"erro": "Caminho do arquivo não fornecido!"}), 400

    arquivo = urllib.parse.unquote(caminho_arquivo)

    if not os.path.exists(arquivo) or not os.path.isfile(arquivo):
        return jsonify({"erro": "Arquivo não encontrado!"}), 404

    return send_file(arquivo, as_attachment=True)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(asgi_app, host='0.0.0.0', port=5000, workers=4)
