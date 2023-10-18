#!/bin/bash

python app.py \
--epochs=500 \
--lr=0.05 \
--model="RandomForest" \
--square=200

#python app.py \
#-e=1000 \
#-l=0.01 \
#-m="NLP" \
#-s=200

#python partition.py \
#--n_parties=100 \
#--partition=noniid-labeldir \
#--beta=0.9 \
#--datadir="/Users/tsiameh/Desktop/RodDemo/data.csv" \
#--outputdir="/Users/tsiameh/Desktop/RodDemo/creditcard/" \
#--init_seed=0