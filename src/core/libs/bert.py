# type: ignore
import torch
from transformers import BertTokenizer, BertModel
from sentence_transformers import SentenceTransformer

tokenizer: BertTokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model: BertModel = BertModel.from_pretrained("bert-base-uncased")
