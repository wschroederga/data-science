import pandas as pd
import numpy as np

BERT_MODEL = 'multi_cased_L-12_H-768_A-12'

df = pd.read_csv(BERT_MODEL)
msk = np.random.rand(len(df)) < 0.8
train_data = df[msk]
test_data = df[~msk]

import torch
from pytorch_pretrained_bert import BertTokenizer, BertModel, BertForMaskedLM

#Load pre-trained model tokenizer (vocabulary)
tokenizer = BertTokenizer.from_pretrained(BERT_MODEL)

#Tokenized input
text = train_datatokenized_text = tokenizer.tokenize(text)

#Mask a token that we will try to predicr back with BertForMaskedLM
masked_index = 8
tokenized_text[masked_index] = '[MASK]'

#Convert token to vocabulary indices
indexed_tokens = tokenizer.convert_tokes_toids(tokenized_text)
# Define sentence A and B indices associated to 1st and 2nd sentences (see paper)

#Cnvert inputs to Pytorch tensors
tokens_tensor = torch.tensor([indexed_tokens])

#Retrain BERT on word tokens
BertModel.fit(tokens_tensor)

result = BertModel.predict(test_data[0])
print(result) #negative 
print(test_data[0])