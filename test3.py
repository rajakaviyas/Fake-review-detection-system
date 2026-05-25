import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/dataset'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session


# Read the files

homepage = pd.read_csv('dataset/home_page_table.csv')
payment = pd.read_csv('dataset/payment_page_table.csv')
confirmation = pd.read_csv('dataset/payment_confirmation_table.csv')
search = pd.read_csv('dataset/search_page_table.csv')
user = pd.read_csv('dataset/user_table.csv')

homepage.info()
payment.info()
confirmation.info()
search.info()
user.info()

homepage['user_id'].count()
search['user_id'].count()
payment['user_id'].count()
confirmation['user_id'].count()
user['user_id'].count()

# Create a new DataFrame 'drop_by_step'

drop_by_step = pd.DataFrame([['Homepage',homepage['user_id'].count()],['Search',search['user_id'].count()],['Payment',payment['user_id'].count()],['Confirmation',confirmation['user_id'].count()]], columns =['Step','Count'])
drop_by_step

#Visulizing the funnel. 

#reference: https://plotly.com/python/funnel-charts/

from plotly import graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Homepage","Search","Payment", "Confirmation"],
    x = [90400,45200,6030,452],
    textposition = "outside",
    textinfo = "value+percent initial"))

fig.show()

