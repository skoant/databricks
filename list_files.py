# Databricks notebook source
import os
cpt = sum([len(files) for r, d, files in os.walk("/tmp/persist_data.parquet/")])
print(cpt)
#edit from DB 
