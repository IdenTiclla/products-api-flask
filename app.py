from flask import Flask, render_template, jsonify, request
from products import products

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello world"

@app.route('/ping',methods=['GET'])
def ping():
    return jsonify({"message":"pong"})

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify({"products":products})

@app.route('/products/<string:product_name>',methods=['GET'])
def get_product(product_name):
    products_found = [product for product in products if product["name"] == product_name]
    if len(products_found) > 0:
        return jsonify({"product": products_found[0]})
    else:
        return jsonify({"error":"Product not found"})

@app.route('/products',methods=['POST'])
def add_product():
    new_product = {
        "name": request.json["name"],
        "price": request.json["price"],
        "quantity": request.json["quantity"]
    }
    products.append(new_product)
    return jsonify({"message":"product added succesfully","products":products})

@app.route('/products/<string:product_name>',methods=['PUT'])
def update_product(product_name):
    products_found = [product for product in products if product["name"] == product_name]
    if len(products_found) > 0:
        products_found[0]['name'] = request.json["name"]
        products_found[0]['price'] = request.json["price"]
        products_found[0]['quantity'] = request.json["quantity"]
        return jsonify({
            "message":"product updated",
            "product":products_found[0]
        })
    else:
        return jsonify({"error":"Product not found"})

@app.route('/products/<string:product_name>',methods=['DELETE'])
def delete_product(product_name):
    products_found = [product for product in products if product["name"] == product_name]
    if len(products_found) > 0:
        products.remove(products_found[0])
        return jsonify({
            "message":"product deleted",
            "products": products
        })
    else:
        return jsonify({"error": "product not found"})

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 