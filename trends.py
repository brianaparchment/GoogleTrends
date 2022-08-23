#The program uses Pytrends to find trends for search terms
#InterestByRegion output is saved to intr_byRegion.png
#RelatedQueries output is saved to ai.csv and facial_rec.csv
import pandas as pd
from pytrends.request import TrendReq
import matplotlib
import matplotlib.pyplot as plt
import requests

pytrends = TrendReq(hl='en-US', timeout=5) #connect to google