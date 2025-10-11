# 5. Assume india wants to export to Australia the products with the following registration no. 
# 147,263,645,789,791,795,796,797 ,798,799.
# Australia is already importing many product from other countries also with regi no..
# Like 
# 105,263,646,789,793,795,796,797 ,798,799,855,882,886.
# so which are the product that india should remove from the export list.

# Find common registration numbers and print them (these should be removed)

india_exports = [147,263,645,789,791,795,796,797,798,799]
australia_imports = [105,263,646,789,793,795,796,797,798,799,855,882,886]

if __name__ == '__main__':
    to_remove = [x for x in india_exports if x in australia_imports]
    print('Products India should remove from export list (common items):')
    print(to_remove)
