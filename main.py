import pandas as pd
import os


def add_values_in_dict(sample_dict, key, list_of_values):
    if key not in sample_dict:
        sample_dict[key] = list()
    sample_dict[key].append(list_of_values)
    return sample_dict


def print_values_in_dict(parent_dict, child_dict):
    for key in parent_dict:
        parent = parent_dict.get(key)
        print(parent)
        print_values_in_child(parent.id, child_dict)


def print_values_in_child(parent_id, child_dict):
    child_nodes = child_dict.get(parent_id)
    if child_nodes:
        for child in child_nodes:
            print(child)
            print_values_in_child(child.id, child_dict)


if __name__ == "__main__":
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'entries.csv'))

    list_of_comments = {}
    list_of_blogs = {}

    for d in df.iterrows():
        if d[1].type == "BLOG":
            list_of_blogs[d[1].id] = d[1]
        elif d[1].type == "COMMENT":
            add_values_in_dict(list_of_comments, d[1].parent_id, d[1])

    print_values_in_dict(list_of_blogs, list_of_comments)

