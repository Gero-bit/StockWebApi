from numpy import imag
from pandas.io.formats import style
import streamlit as st
import pandas as pd
from PIL import Image

st.write("""
# Stock Market Web Application
**Visually** show data on a Stock! Date range from Apr 9, 2020 - Apr 09, 2021
""")

image = Image.open("F:/.Programing/wallstreat.jpg")
st.image(image, use_column_width=True)

st.sidebar.header('User Input')

# Create a funtion to get the users input
def get_input():
    start_date = st.sidebar.text_input("Start Date", "2007-08-10")
    end_date = st.sidebar.text_input("End Date", "2021-04-09")
    stock_symbol = st.sidebar.text_input("Stock Symbol", "AMZN")
    return start_date, end_date, stock_symbol

# Create a funtion to get the company name
def get_company_name(symbol):
    if symbol == 'AMZN':
        return 'Amazon'
    elif symbol == 'MELI':
        return 'MercadoLibre'
    elif symbol == 'BABA':
        return 'Alibaba'
    else:
        'None'

# Create a Funtion to get the proper company data and the proper time frame from the user start date to ther users end date
def get_data(symbol, start, end):

    # Load the data
    if symbol.upper() == 'AMZN':
        df = pd.read_csv("F:/.Programing/AMZN.csv")
    elif symbol.upper() == 'MELI':
        df = pd.read_csv("F:/.Programing/MELI.csv")
    elif symbol.upper() == 'BABA':
        df = pd.read_csv("F:/.Programing/BABA.csv")
    else:
        df = pd.DataFrame(
            columns=['Date', 'Close', 'Open', 'Volume', 'Adj Close', 'High', 'Low'])

    # Get the date range
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)

    # Set the start and end index rows both to 0
    stat_row = 0
    end_row = 0

    # Start the date from the top of the data set and go down to see if the usuers start date is less than or equal to the dataset
    for i in range(0, len(df)):
        if start <= pd.to_datetime(df['Date'][i]):
            start_row = i
            break

    # Start from the bottom of the data set and go up to see if the users end date is greather than or equal
    for j in range(0, len(df)):
        if end >= pd.to_datetime(df['Date'][len(df)-1-j]):
            end_row = len(df) - 1 - j
            break

    # Set the index to be the date
    df = df.set_index(pd.DatetimeIndex(df['Date'].values))

    return df.iloc[start_row:end_row + 1, :]


# Get the users input
start, end, symbol = get_input()

# Get the data
df = get_data(symbol, start, end)

# Get the company name
company_name = get_company_name(symbol.upper())

# Display the close price
st.header(company_name+" Close Price\n")
st.line_chart(df['Close'])

# Display the Volume price
st.header(company_name+" Volume Price\n")
st.line_chart(df['Volume'])

# Get statistics on the data
st.header('Data Statistics')
st.write(df.describe())
