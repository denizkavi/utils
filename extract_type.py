import pandas as pd 
import os
import json

"""
df = pd.read_csv("230321_5_YcjN Full Network default node.csv")
df.to_excel("230321_5_YcjN Full Network default node.xlsx")
"""

res = {}
encoded_res = {}

encode = {"Other":0,
        "Signal Peptide (Sec/SPI)":1,
        "Lipoprotein signal peptide (Sec/SPII)":2,
        "TAT signal peptide (Tat/SPI)":3,
        "TAT Lipoprotein signal peptide (Tat/SPII)":4,
        "Pilin-like signal peptide (Sec/SPIII)":5}

for folder in os.listdir("out"):
    if "output.json" in os.listdir(f"out/{folder}"):
        with open(f"out/{folder}/output.json") as f:
            j = dict(json.load(f))

        res[folder] = j["SEQUENCES"][list(j["SEQUENCES"].keys())[0]]["Prediction"]
        encoded_res[folder] = encode[res[folder]]

    else:
        res[folder] = "?"
        encoded_res[folder] = "?"

id_ = [key for key in res]
lipoprotein = [res[key] for key in res]
encoded = [encoded_res[key] for key in res]

df = pd.DataFrame({"Id": id_, "Lipoprotein": lipoprotein, "Encoded":encoded})
df.to_excel("signalp_results.xlsx")
#add sending to user with email, also confirmation earlier that we recieved the query