'''
5. Assume india wants to export to Australia the products with the following registration no. 
147,263,645,789,791,795,796,797 ,798,799.
Australia is already importing many product from other countries also with regi no..
Like 
105,263,646,789,793,795,796,797 ,798,799,855,882,886.
so which are the product that india should remove from the export list.
'''
ind_products = {147, 263, 645, 789, 791, 795, 796, 797, 798, 799}
aus_products = {105, 263, 646, 789, 793, 795, 796, 797, 798, 799, 855, 882, 886}
prods_to_remove = ind_products.intersection(aus_products)
print("Products that should be removed: ", prods_to_remove)


