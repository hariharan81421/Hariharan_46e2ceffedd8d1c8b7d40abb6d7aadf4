def linear_search_product(products, target_product):
    indices = []
    for index, product in enumerate(products):
        if product == target_product:
            indices.append(index)
    return indices

# Example usage:
products = ["Apple", "Banana", "Apple", "Orange", "Apple"]
target_product = "Apple"
result = linear_search_product(products, target_product)
print(f"Indices of '{target_product}': {result}")
