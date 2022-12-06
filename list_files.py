# Databricks notebook source
import os
cpt = [len(files) for r, d, files in os.walk("/tmp/")]
print(cpt)
