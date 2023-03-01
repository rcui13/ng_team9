import plotly
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def make_pie_chart(dict):
    # num_real = 0
    # num_fake = 0
    # for i in range(0, len(dict)):
    #     if (dict[str(i)]['is_real'] == True):
    #         num_real += 1
    #     else:
    #         num_fake += 1
    labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
    values = [4500, 2500, 1053, 500]
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

    # fig = go.pie(data=[go.Pie(values=[num_fake, num_real])])
    fig.show()