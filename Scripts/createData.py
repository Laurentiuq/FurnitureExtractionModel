import random
import json
def create_data():
    with open("furniture_products.txt") as fp:
        product_list = [line.strip() for line in fp]
    with open("materials.txt") as fm:
        materials_list = [line.strip() for line in fm]
    with open("names.txt") as fn:
        names_list = [line.strip() for line in fn]
    
    ln_product = len(product_list)
    ln_materials = len(materials_list)
    ln_names = len(names_list)

    new_data_f = open("data1.jsonl", 'a')
    
    json_line = dict()
    for i in range(1000):
        rand_product = random.randint(0,ln_product-1)
        rand_material = random.randint(0,ln_materials-1)
        rand_name = random.randint(0,ln_names-1)
        
        new_product =  names_list[rand_name] + " " + product_list[rand_product]
        new_other = ''
        if random.randint(0,1):
            new_other += ' -'
        if random.randint(0,1):
            new_other += ' ' + materials_list[rand_material] + ' '
        if random.randint(0,1):
           
            rand_price = random.randrange(0, 10000, 10) - 1
            new_other += f'  {rand_price}'
            if random.randint(0,1):
                new_other += '0.99'
        if new_other:
            label_list = [[0, len(new_product), "PRODUCT"], [len(new_product), len(new_product) + len(new_other), "OTHER"]]
        else:
            label_list = [[0, len(new_product), "PRODUCT"]]
        json_line["text"] = new_product + new_other
        json_line["label"] = label_list
        json.dump(json_line, new_data_f)
        new_data_f.write("\n")


create_data()