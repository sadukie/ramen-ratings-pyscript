import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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
    # do this so labels don't get cutoff
    plt.subplots_adjust(bottom=0.25)
    plt.setp(ax.get_xticklabels(),rotation=45)
    plt.title('Brands Most Reviewed')
    plt.xlabel('Brands')
    plt.ylabel('Number of Reviews')
    document.querySelector("#most_tested_graph").innerHTML=""
    display(fig,target="most_tested_graph")

def show_most_tested_seaborn(event):
    url_content = open_url("https://raw.githubusercontent.com/sadukie/ramen-ratings-pyscript/main/ramen-ratings.csv")
    df = pd.read_csv(url_content)
    # Remove the unrated entries
    df = df.drop(df[df["Stars"] == "Unrated"].index)
    # Convert to numeric to make it easier to plot
    df["Stars"] = pd.to_numeric(df["Stars"])
    fig,ax = plt.subplots()
    sns.set_theme(style="darkgrid")
    sns.boxplot(data=df,x="Style",y="Stars",palette="pastel",hue="Style").set(title="Reviews by Style")
    document.querySelector("#most_tested_seaborn").innerHTML=""
    display(fig,target="most_tested_seaborn")