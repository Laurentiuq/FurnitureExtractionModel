# Parse a jsonl file and assign the label "[0, len(text), "OTHER"]" for the text that is not labeled
import json


def assign_label(jsonl_file_path):
    """
    Parse a jsonl file and assign the label "OTHER" for the text that is not labeled
    :param jsonl_file_path:
    :return:
    """
    # open the jsonl file
    with open(jsonl_file_path, 'r') as file:
        # read the file line by line
        for line in file:
            json_line = json.loads(line)
            text = json_line['text']
            label = json_line['label']
            # if the label is empty, assign the label "OTHER"
            if not label:
                json_line['label'] = [[0,len(text),"OTHER"]]
            # write the data in a new jsonl file

            with open(jsonl_file_path.rsplit(".", 1)[0] + "mod.jsonl",
                      'a', encoding="utf-8") as new_file:
                json.dump(json_line, new_file)
                # print(json_line)

                new_file.write("\n")


# assign_label("C:/Users/Laurentiu/PycharmProjects/FurnitureStoresExtraction/admin.jsonl")

assign_label("unlabeled/data6.jsonl")

# with open("C:/Users/Laurentiu/PycharmProjects/FurnitureStoresExtraction/admin_label.jsonl", 'r', encoding='utf-8') as file:
#     for line in file:
#         json_line = json.loads(line)
#         label = json_line['label']
#         print(type(label))