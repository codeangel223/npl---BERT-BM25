# type: ignore
# import torch
# from transformers import BertTokenizer, BertModel
from sentence_transformers import SentenceTransformer

sentence_transformer_model = SentenceTransformer(
    "distiluse-base-multilingual-cased")
