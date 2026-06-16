import yaml

def read_yml(filename):
    with open("manual_build/" + filename, 'r') as f:
        infos = yaml.safe_load(f)
        return infos