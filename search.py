import yaml

with open("./data/search_page.yaml", "r",encoding="utf-8") as f:
  data = yaml.load(f,Loader=yaml.FullLoader)
  print(data)

