import pandas as pd
import unicodedata
import re

tests = pd.read_csv("data/test_names.csv")
recognized = pd.read_csv("data/recognized_names.csv")

suffixes = {"inc", "ltd", "limited", "corp", "llp", "ltee", "limitee"}

#normalization function
def normalize(name):
    lowercase = name.lower()
    insert_ands = lowercase.replace("&", " and ")
    accents = unicodedata.normalize("NFKD", insert_ands)
    drop_accents = accents.encode("ascii", "ignore").decode()
    remove_punctuation = re.sub(r"[^a-z0-9 ]", " ", drop_accents)
    words = remove_punctuation.split()
    words_kept = [w for w in words if w not in suffixes]
    joined_together = " ".join(words_kept)
    return joined_together

print(normalize("Bell Textron Canada Ltée"))
print(normalize("I.B.M."))