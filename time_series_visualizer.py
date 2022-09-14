import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')

# Clean data
df = df[(df.value > np.percentile(df.value, 2.5)) & (df.value < np.percentile(df.value, 97.5))] 



def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize = (20,7))
    plt.plot(df.date, df.value, color = 'red')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    
    df_bar = df.copy()
    # turning date column to datetime type
    df_bar['date'] = pd.to_datetime(df_bar.date)
    
    # creting months column 
    df_bar['month'] = df_bar.date.dt.month_name()
    
    # creting years column 
    df_bar['year'] = df_bar.date.dt.year
    # Draw bar plot
    fig = plt.figure(figsize = (10,7))
    months_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    main_color = sns.color_palette("Dark2", 12)
    sns.barplot(x = df_bar.year, y= df_bar.value, hue=df_bar.month, ci=None, hue_order = months_order, palette= main_color)
    plt.xlabel('Years')
    plt.ylabel('Average Page Views');
    plt.legend(loc = 2, title="Months")




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    # df_box.reset_index(inplace=True)
    # df_box['year'] = [d.year for d in df_box.date]
    # df_box['month'] = [d.strftime('%b') for d in df_box.date]
  
    # turning date column to datetime type
    df_box['date'] = pd.to_datetime(df_box.date)
    
    # creting months column 
    df_box['month'] = df_box.date.dt.month_name()
    
    # creting years column 
    df_box['year'] = df_box.date.dt.year
    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(nrows =1 , ncols=2, figsize = (27,13))

    months_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    sns.boxplot(x = df_box.year, y=df_box.value, ax= ax[0] )
    ax[0].set_ylabel('Page Views')
    ax[0].set_xlabel('Year')
    ax[0].set_title('Year-wise Box Plot (Trend)')
    
    sns.boxplot(x = df_box.month, y=df_box.value, ax= ax[1], order= months_order )
    ax[1].set_ylabel('Page Views')
    ax[1].set_xlabel('Month')
    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    ax[1].set_xticklabels([i[0:3] for i in months_order]);




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
