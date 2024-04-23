!pip install sentence-transformers

import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-mpnet-base-v2')

dataset_path = ''

embeddings_commercial_name_path = ''
embeddings_short_description_path = ''
embeddings_description_path = ''

loaded_embeddings_commercial_name = np.load(embeddings_commercial_name_path)
loaded_embeddings_short_description = np.load(embeddings_short_description_path)
loaded_embeddings_description = np.load(embeddings_description_path)

data = pd.DataFrame(pd.read_csv(dataset_path))

#! Commercial name - cred

def round_1(company_name):
    sen = [company_name]
    sen_embeddings = model.encode(sen)

    results = cosine_similarity(
        [sen_embeddings[0]],
        loaded_embeddings_commercial_name[0:]
    )
    sim_value = results.max() # value
    label = data.iloc[results.argmax()]['naics_label'] # label
    return label

#! Short description

def round_3(short_description):
    sen = [short_description]
    sen_embeddings = model.encode(sen)

    results = cosine_similarity(
        [sen_embeddings[0]],
        loaded_embeddings_short_description[0:]
    )
    sim_value = results.max()
    label = data.iloc[results.argmax()]['naics_label']
    return label

#! Description

def round_5(description):
    sen = [description]
    sen_embeddings = model.encode(sen)

    results = cosine_similarity(
        [sen_embeddings[0]],
        loaded_embeddings_description[0:]
    )
    sim_value = results.max()
    label = data.iloc[results.argmax()]['naics_label']
    return label