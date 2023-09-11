import os
import re
import csv

# 特定のワード・記号を削除する関数を定義
def clean_text(text):
    # @から始まる部分を削除
    cleaned_text = re.sub(r'@\w+\s*', '', text)
    
    # "RT"を削除
    cleaned_text = re.sub(r'RT', '', cleaned_text)
    
    # 絵文字や記号を削除
    cleaned_text = re.sub(r'[^\w\s]', '', cleaned_text)
    
    # URLを削除
    cleaned_text = re.sub(r'http\S+', '', cleaned_text)
    
    return cleaned_text

input_folder = 'input_folder'  # 入力ファイルが含まれるフォルダのパス
output_folder = 'output_folder'  # 出力ファイルを保存するフォルダのパス

# 出力フォルダが存在しない場合は作成
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith('.csv'):
        input_filepath = os.path.join(input_folder, filename)
        output_filepath = os.path.join(output_folder, filename)
        
        # CSVファイルを読み込み、新しいCSVファイルを書き込む
        with open(input_filepath, 'r', encoding='utf-8') as input_file, open(output_filepath, 'w', newline='', encoding='utf-8') as output_file:
            csv_reader = csv.reader(input_file)
            csv_writer = csv.writer(output_file)
            
            for row_num, row in enumerate(csv_reader):
                if 1 <= row_num <= 202:  # セルB2からセルB201までの行のテキストをクリーニング
                    cleaned_text = clean_text(row[1])  # セルBのテキストをクリーニング
                    row[1] = cleaned_text  # クリーニングしたテキストをセルBに設定
                csv_writer.writerow(row)  # 行を新しいCSVファイルに書き込む
