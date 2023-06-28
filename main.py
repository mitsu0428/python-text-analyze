import csv
import json
from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.tokenfilter import TokenCountFilter, POSKeepFilter

TOKENIZER = Tokenizer()
token_filters = [
    # POSKeepFilter(['名詞']),
    TokenCountFilter(),
]
analyzer = Analyzer(token_filters=token_filters)

input_csv_name = "file.csv"
output_json_name = "output.json"

json_key_list = []
target_analyze_text_list = []
with open(input_csv_name) as f:
    csv_reader = csv.reader(f)
    csv_reader.__next__()

    for row in list(csv_reader):
        # 0列目をKEYに、1列目の分析をVALUEにした辞書を作成
        json_key_list.append(row[0])
        target_analyze_text_list.append(row[1])

dict_list = []
loop_count = 0
for sentence in target_analyze_text_list:
    count_information_dict = analyzer.analyze(sentence)
    tmp_key = json_key_list[loop_count]

    target_dict = {}
    target_dict[tmp_key] = dict(count_information_dict)
    dict_list.append(target_dict)
    loop_count += 1


output_dict = {}
output_dict["output"] = dict_list

with open(output_json_name, "w") as file:
    json.dump(output_dict, file, indent=4, ensure_ascii=False)
