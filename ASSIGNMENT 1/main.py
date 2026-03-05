from fastapi import FastAPI

app = FastAPI()

# FastAPI Internship Training - Day 1 Assignment
# Name: Rahul

# Initial Products List (Total = 7)
products = [
    {"id": 1, "name": "Wireless Mouse", "price": 599, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Notebook", "price": 49, "category": "Stationery", "in_stock": True},
    {"id": 3, "name": "Pen Set", "price": 99, "category": "Stationery", "in_stock": False},
    {"id": 4, "name": "Headphones", "price": 1499, "category": "Electronics", "in_stock": True},
    
    # Added Products (IDs 5, 6, 7)
    {"id": 5, "name": "Laptop Stand", "price": 1299, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1899, "category": "Electronics", "in_stock": False},
]

# 1️⃣ Get All Products
@app.get("/products")
def get_products():
    return {
        "products": products,
        "total": len(products)
    }


# 2️⃣ Filter by Category
@app.get("/products/category/{category_name}")
def get_by_category(category_name: str):
    filtered = [p for p in products if p["category"].lower() == category_name.lower()]
    
    if not filtered:
        return {"error": "No products found in this category"}
    
    return {
        "products": filtered,
        "count": len(filtered)
    }


# 3️⃣ Show Only In-Stock Products
@app.get("/products/instock")
def get_instock_products():
    instock = [p for p in products if p["in_stock"]]
    
    return {
        "in_stock_products": instock,
        "count": len(instock)
    }


# 4️⃣ Store Summary
@app.get("/store/summary")
def store_summary():
    total = len(products)
    instock_count = len([p for p in products if p["in_stock"]])
    outstock_count = total - instock_count
    categories = list(set(p["category"] for p in products))

    return {
        "store_name": "My E-commerce Store",
        "total_products": total,
        "in_stock": instock_count,
        "out_of_stock": outstock_count,
        "categories": categories
    }


# 5️⃣ Search Products (Case-Insensitive)
@app.get("/products/search/{keyword}")
def search_products(keyword: str):
    matches = [p for p in products if keyword.lower() in p["name"].lower()]
    
    if not matches:
        return {"message": "No products matched your search"}
    
    return {
        "matched_products": matches,
        "total_matches": len(matches)
    }


# ⭐ Bonus — Cheapest & Most Expensive
@app.get("/products/deals")
def product_deals():
    cheapest = min(products, key=lambda x: x["price"])
    expensive = max(products, key=lambda x: x["price"])

    return {
        "best_deal": cheapest,
        "premium_pick": expensive
    }