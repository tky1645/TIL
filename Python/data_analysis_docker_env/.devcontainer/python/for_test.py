import random
import glob
import json
from tqdm import tqdm

import torch
from torch.utils.data import DataLoader
from transformers import BertJapaneseTokenizer, BertModel
import pytorch_lightning as pl

# pytorch
import torch
import torchvision
import torchvision.transforms as transforms
# Utilities
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import List

# 日本語の事前学習モデル
MODEL_NAME = 'cl-tohoku/bert-base-japanese-whole-word-masking'

class BertForSequenceClassificationMultiLabel(torch.nn.Module):
    
    def __init__(self, model_name, num_labels):
        super().__init__()
        # BertModelのロード
        self.bert = BertModel.from_pretrained(model_name) 
        # 線形変換を初期化しておく
        self.linear = torch.nn.Linear(
            self.bert.config.hidden_size, num_labels
        ) 

    def forward(
        self, 
        input_ids=None, 
        attention_mask=None, 
        token_type_ids=None, 
        labels=None
    ):
        # データを入力しBERTの最終層の出力を得る。
        bert_output = self.bert(
            input_ids=input_ids,
            attention_mask=attention_mask,
            token_type_ids=token_type_ids)
        last_hidden_state = bert_output.last_hidden_state
        
        # [PAD]以外のトークンで隠れ状態の平均をとる
        averaged_hidden_state = \
            (last_hidden_state*attention_mask.unsqueeze(-1)).sum(1) \
            / attention_mask.sum(1, keepdim=True)
        
        # 線形変換
        scores = self.linear(averaged_hidden_state) 
        
        # 出力の形式を整える。
        output = {'logits': scores}

        # labelsが入力に含まれていたら、損失を計算し出力する。
        if labels is not None: 
            loss = torch.nn.BCEWithLogitsLoss()(scores, labels.float())
            output['loss'] = loss
            
        # 属性でアクセスできるようにする。
        output = type('bert_output', (object,), output) 

        return output

# tokenizerとモデルのロード
tokenizer = BertJapaneseTokenizer.from_pretrained(MODEL_NAME)
bert_scml = BertForSequenceClassificationMultiLabel(
    MODEL_NAME, num_labels=2
)

# 
text_list = [
    '今日の仕事はうまくいったが、体調があまり良くない。',
    '昨日は楽しかった。'
]

labels_list = [
    [1, 1],
    [0, 1]
]

# データの符号化
encoding = tokenizer(
    text_list, 
    padding='longest',  
    return_tensors='pt'
)
encoding = { k: v for k, v in encoding.items() }
labels = torch.tensor(labels_list)

# BERTへデータを入力し分類スコアを得る。
with torch.no_grad():
    output = bert_scml(**encoding)
scores = output.logits

# スコアが正ならば、そのカテゴリーを選択する。
labels_predicted = ( scores > 0 ).int()

# 精度の計算
num_correct = ( labels_predicted == labels ).all(-1).sum().item()
accuracy = num_correct/labels.size(0)
print(accuracy)
