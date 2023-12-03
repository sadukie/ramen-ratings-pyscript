import pandas as pd
import matplotlib.pyplot as plt
from pyodide.http import open_url
from pyscript import document, display

def show_most_tested_list(event):
    url_content = open_url("https://raw.githubusercontent.com/sadukie/ramen-ratings-pyscript/main/ramen-ratings.csv")
    output = document.querySelector("#most_tested_list")
    df = pd.read_csv(url_content)
    most_tested = df.Brand.value_counts().nlargest(10).to_frame()
    output.innerHTML = most_tested.to_html() 
    #display(,target="most_tested_list")

def show_most_tested_graph(event):
    url_content = open_url("https://raw.githubusercontent.com/sadukie/ramen-ratings-pyscript/main/ramen-ratings.csv")
    df = pd.read_csv(url_content)
    most_tested = df.Brand.value_counts().nlargest(10).to_frame()        
    fig, ax = plt.subplots()
    ax.bar(most_tested.index,most_tested.Brand)
    plt.setp(ax.get_xticklabels(),rotation=45)
    plt.title('Brands Most Reviewed')
    plt.xlabel('Brands')
    plt.ylabel('Number of Reviews')
    display(fig,target="most_tested_graph")