from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)


# Return a welcome message as JSON.
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Product Catalog API!"})


# Return all products, or filter by the requested category.
@app.route("/products", methods=["GET"])
def get_products():
    category = request.args.get("category")

    if category is not None:
        filtered_products = [
            product for product in products
            if product["category"].lower() == category.lower()
        ]
        return jsonify(filtered_products)

    return jsonify(products)


# Return the matching product, or a 404 response if it does not exist.
@app.route("/products/<int:id>", methods=["GET"])
def get_product_by_id(id):
    for product in products:
        if product["id"] == id:
            return jsonify(product)

    return jsonify({"error": "Product not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)