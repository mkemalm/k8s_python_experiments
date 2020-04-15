import yaml

with open('test.yml') as f:
    
    data = yaml.load_all(f, Loader=yaml.FullLoader)
    for doc in data:
        for k, v in doc.items():
            print(k, "->", v)