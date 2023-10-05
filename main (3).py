def linear_search_product(product_list, target_product):
    indices = []
    
    # Iterate through the list and check if each product matches the target
    for i, product in enumerate(product_list):
        if product == target_product:
            indices.append(i)
    
    return indices