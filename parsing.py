import yaml

with open("repeated_nodes.yaml","r") as stream :
    try :
        print(yaml.safe_load(stream))
    except yaml.YAMError as e:
        print(e)