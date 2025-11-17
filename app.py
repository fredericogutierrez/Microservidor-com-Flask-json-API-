from flask import Flask, request, jsonify  # Importações essenciais do Flask
import os  

# Criação da aplicação Flask
app = Flask(__name__)

# Nome da pasta onde os arquivos .txt serão armazenados
STORAGE_FOLDER = "storage_txt"

if not os.path.exists(STORAGE_FOLDER):
    os.makedirs(STORAGE_FOLDER)

def get_file_path(filename):
    return os.path.join(STORAGE_FOLDER, filename)

@app.route('/files', methods=['POST'])
def create_file():
    data = request.get_json()  

    filename = data.get("filename")
    content = data.get("content", "")  

    if not filename:
        return jsonify({"error": "filename é obrigatório"}), 400

    file_path = get_file_path(filename)

    if os.path.exists(file_path):
        return jsonify({"error": "arquivo já existe"}), 400

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

    return jsonify({
        "message": "arquivo criado",
        "filename": filename
    }), 201


@app.route('/files/<filename>', methods=['GET'])
def read_file(filename):
    file_path = get_file_path(filename)

    if not os.path.exists(file_path):
        return jsonify({"error": "arquivo não encontrado"}), 404

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    return jsonify({
        "filename": filename,
        "content": content
    }), 200


@app.route('/files/<filename>', methods=['PUT'])
def update_file(filename):
    data = request.get_json()
    new_content = data.get("content", "")

    file_path = get_file_path(filename)

    if not os.path.exists(file_path):
        return jsonify({"error": "arquivo não encontrado"}), 404

    with open(file_path, "a", encoding="utf-8") as file:
        file.write(new_content + "\n")

    with open(file_path, "r", encoding="utf-8") as file:
        updated_content = file.read()

    return jsonify({
        "message": "arquivo atualizado (append)",
        "filename": filename,
        "content": updated_content
    }), 200


@app.route('/files/<filename>', methods=['DELETE'])
def delete_file(filename):
    file_path = get_file_path(filename)

    if not os.path.exists(file_path):
        return jsonify({"error": "arquivo não encontrado"}), 404

    os.remove(file_path)

    return jsonify({
        "message": "arquivo deletado",
        "filename": filename
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
