import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from millify import millify
from plotly.subplots import make_subplots
from streamlit_extras.colored_header import colored_header

# st.cache_data.clear()

st.set_page_config(
    page_title="Uniswap Tokens",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": None,
        "Report a bug": "https://twitter.com/sageOlamide",
        "About": None
    }
)

st.markdown(f'<h1 style="color:#434346;font-size:60px;text-align:center;">Uniswap Tokens</h1>', unsafe_allow_html=True)

text_1 = """
<p style="font-family:sans-serif; color:#4d372c; font-size: 20px;">
This dashboard offers an in-depth analysis of token activity on Uniswap, focusing on trends across multiple chains and Uniswap versions. 
It addresses key questions such as the growth of unique tokens over time, shifts in popular token pairs, and differences in token activity across chains. 
The analysis covers the following blockchains: Arbitrum, Avalanche, Base, Binance Smart Chain (BSC), Ethereum, Optimism, and Polygon, with data sourced for Uniswap V2 and V3 via 
FlipsideCrypto's <a href="https://flipsidecrypto.github.io/crosschain-models/#!/model/model.crosschain_models.defi__ez_dex_swaps"><code>crosschain.defi.ez_dex_swaps</code></a> table.
</p>
"""
st.markdown(text_1, unsafe_allow_html=True)

###################################
############ CACHE DATA ###########
###################################

url1 = "https://flipsidecrypto.xyz/studio/queries/1987171e-2579-4977-8985-df4bb995cf25"
@st.cache_data
def load_df1():
    df1 = pd.read_csv('data/df1.csv')
    return df1

url2 = "https://flipsidecrypto.xyz/studio/queries/1b22a97f-496e-4639-81e2-f2a1c115fcce"
@st.cache_data
def load_df2():
    df2 = pd.read_csv('data/df2.csv')
    return df2

url3 = "https://flipsidecrypto.xyz/studio/queries/7e7a5581-8df6-4ff5-a152-2948bc1e85c6"
@st.cache_data
def load_df3():
    df3 = pd.read_csv('data/df3.csv')
    return df3

url4 = "https://flipsidecrypto.xyz/studio/queries/1dcd34f1-8ad0-4341-9893-48aa64247ad4"
@st.cache_data
def load_df4():
    df4 = pd.read_csv('data/df4.csv')
    return df4

url5 = "https://flipsidecrypto.xyz/studio/queries/1682e5b8-e9ea-4412-a96c-54263bc00a19"
@st.cache_data
def load_df5():
    df5 = pd.read_csv('data/df5.csv')
    return df5

url6 = "https://flipsidecrypto.xyz/studio/queries/4af0a8c8-6d57-45c7-8d6a-8318bf81c851"
@st.cache_data
def load_df6():
    df6 = pd.read_csv('data/df6.csv')
    return df6

url7 = "https://flipsidecrypto.xyz/studio/queries/9bfd0108-8dcd-4e28-95d4-a1afa111955a"
@st.cache_data
def load_df7():
    df7 = pd.read_csv('data/df7.csv')
    return df7

url8 = "https://flipsidecrypto.xyz/studio/queries/e5353e90-57a8-43e1-bf62-0222e720ebb3"
@st.cache_data
def load_df8():
    df8 = pd.read_csv('data/df8.csv')
    return df8

url9 = "https://flipsidecrypto.xyz/studio/queries/cc17010f-bfbb-47d2-b975-6fb6a7929585"
@st.cache_data
def load_df9():
    df9 = pd.read_csv('data/df9.csv')
    return df9

url10 = "https://flipsidecrypto.xyz/studio/queries/52a70ad6-8110-4487-b671-316b27794c5d"
@st.cache_data
def load_df10():
    df10 = pd.read_csv('data/df10.csv')
    return df10

url11 = "https://flipsidecrypto.xyz/studio/queries/fb3f38cb-f61f-4b8e-ba37-fb3ce3ea9230"
@st.cache_data
def load_df11():
    df11 = pd.read_csv('data/df11.csv')
    return df11

url12 = "https://flipsidecrypto.xyz/studio/queries/f6e0b575-33f0-4202-baf9-1aaf36511172"
@st.cache_data
def load_df12():
    df12 = pd.read_csv('data/df12.csv')
    return df12

url13 = "https://flipsidecrypto.xyz/studio/queries/0fc93148-788b-4468-8172-41e117b4ee85"
@st.cache_data
def load_df13():
    df13 = pd.read_csv('data/df13.csv')
    return df13

url14 = "https://flipsidecrypto.xyz/studio/queries/a9e721c4-d36c-4a0a-ab3a-5801aaf14d5a"
@st.cache_data
def load_df14():
    df14 = pd.read_csv('data/df14.csv')
    return df14

url15 = "https://flipsidecrypto.xyz/studio/queries/69d6aa20-0164-4180-8cc0-86b0485536be"
@st.cache_data
def load_df15():
    df15 = pd.read_csv('data/df15.csv')
    return df15

url16 = "https://flipsidecrypto.xyz/studio/queries/c0f1b7dd-5706-404c-859a-050e59c3e372"
@st.cache_data
def load_df16():
    df16 = pd.read_csv('data/df16.csv')
    return df16

url17 = "https://flipsidecrypto.xyz/studio/queries/70a4d4e8-94a2-4b67-9242-2f27d64dd20a"
@st.cache_data
def load_df17():
    df17 = pd.read_csv('data/df17.csv')
    return df17

url18 = "https://flipsidecrypto.xyz/studio/queries/2ed2287f-09f1-480d-9da3-e01e910e23fc"
@st.cache_data
def load_df18():
    df18 = pd.read_csv('data/df18.csv')
    return df18

url19 = "https://flipsidecrypto.xyz/studio/queries/88cf4f44-80e8-41e6-b262-7f1fff37a637"
@st.cache_data
def load_df19():
    df19 = pd.read_csv('data/df19.csv')
    return df19

url20 = "https://flipsidecrypto.xyz/studio/queries/54e82ad5-1263-43d5-93db-a8deee59e6e0"
@st.cache_data
def load_df20():
    df20 = pd.read_csv('data/df20.csv')
    return df20

url21 = "https://flipsidecrypto.xyz/studio/queries/3feffd60-815b-46c8-8204-8a0656c43903"
@st.cache_data
def load_df21():
    df21 = pd.read_csv('data/df21.csv')
    return df21

url22 = "https://flipsidecrypto.xyz/studio/queries/b3dc5178-ffea-4477-b575-1a2b75abfd93"
@st.cache_data
def load_df22():
    df22 = pd.read_csv('data/df22.csv')
    return df22

url23 = "https://flipsidecrypto.xyz/studio/queries/9d2de927-8dc4-4187-ad27-9ec902cee75d"
@st.cache_data
def load_df23():
    df23 = pd.read_csv('data/df23.csv')
    return df23

url24 = "https://flipsidecrypto.xyz/studio/queries/514c228c-b34a-4f58-bc51-055b045ddf85"
@st.cache_data
def load_df24():
    df24 = pd.read_csv('data/df24.csv')
    return df24

url25 = "https://flipsidecrypto.xyz/studio/queries/3f77b6cb-6eca-46b6-b63a-d77978a8023d"
@st.cache_data
def load_df25():
    df25 = pd.read_csv('data/df25.csv')
    return df25

url26 = "https://flipsidecrypto.xyz/studio/queries/b296fc7c-b06e-4a45-9430-d1decbe7cd07"
@st.cache_data
def load_df26():
    df26 = pd.read_csv('data/df26.csv')
    return df26

url27 = "https://flipsidecrypto.xyz/studio/queries/18346568-b0a5-4e48-9d2d-6b8706039b23"
@st.cache_data
def load_df27():
    df27 = pd.read_csv('data/df27.csv')
    return df27

url28 = "https://flipsidecrypto.xyz/studio/queries/632b4a11-518a-45e5-a01d-689345e574ed"
@st.cache_data
def load_df28():
    df28 = pd.read_csv('data/df28.csv')
    return df28

###################################
############ LOAD DATA ############
###################################

df1 = load_df1()
df2 = load_df2()
df3 = load_df3()
df4 = load_df4()
df5 = load_df5()
df6 = load_df6()
df7 = load_df7()
df8 = load_df8()
df9 = load_df9()
df10 = load_df10()
df11 = load_df11()
df12 = load_df12()
df13 = load_df13()
df14 = load_df14()
# df15 = load_df15()
# df16 = load_df16()
df17 = load_df17()
df18 = load_df18()
df19 = load_df19()
df20 = load_df20()
df21 = load_df21()
df22 = load_df22()
df23 = load_df23()
df24 = load_df24()
df25 = load_df25()
df26 = load_df26()
df27 = load_df27()
df28 = load_df28()

###################################
########### PLOT CHARTS ###########
###################################


##################### DF1 #####################
################ FIG1 START ###################
df1_fig1 = px.area(df1, x='WEEK', y='UNIQUE_TOKEN_COUNT', title='Unique Tokens Traded per Week')
df1_fig1.update_layout(hovermode="x unified")
################# FIG1 END ####################

##################### DF2 #####################
################ FIG1 START ###################
df2_fig1 = px.line(df2, x='WEEK', y='UNIQUE_TOKEN_COUNT', color='BLOCKCHAIN', title='Unique Tokens Traded per Week by Blockchain')
df2_fig1.update_layout(hovermode="x unified")
################# FIG1 END ####################

##################### DF3 #####################
################ FIG1 START ###################
################ FIG1 START ###################
df3_fig1 = px.line(df3, x='WEEK', y=['V2', 'V3'], title='Unique Tokens Traded per Week by Uniswap Version')
df3_fig1.update_layout(hovermode="x unified", yaxis_title="UNIQUE_TOKEN_COUNT", legend_title="Uniswap Version")
################# FIG1 END ####################

##################### DF4 #####################
################ FIG1 START ###################
df4_fig1 = px.area(df4, x='WEEK', y='UNIQUE_TOKEN_PAIRS', title='Unique Token Pairs per Week')
df4_fig1.update_layout(hovermode="x unified")
################# FIG1 END ####################

##################### DF5 #####################
################ FIG1 START ###################
df5_fig1 = px.line(df5, x='TRADING_WEEK', y='UNIQUE_TOKEN_PAIRS', color='BLOCKCHAIN', title='Unique Token Pairs per Week by Blockchain')
df5_fig1.update_layout(hovermode="x unified")
################# FIG1 END ####################

##################### DF6 #####################
################ FIG1 START ###################
df6_fig1 = px.line(df6, x='WEEK', y='NEW_TOKENS', title='New Tokens per Week')
df6_fig1.update_layout(hovermode="x unified", yaxis2=dict(title='Cumulative New Tokens', overlaying='y', side='right'))
df6_fig1.add_trace(go.Scatter(x=df6['WEEK'], y=df6['CUMU_NEW_TOKENS'], mode='lines', name='Cumulative New Tokens', yaxis='y2'))
################# FIG1 END ####################

##################### DF7 #####################
################ FIG1 START ###################
df7_fig1 = px.line(df7, x='WEEK', y='NEW_TOKENS', color='BLOCKCHAIN', title='New Tokens per Week by Blockchain')
df7_fig1.update_layout(hovermode="x unified")
################# FIG1 END ####################

##################### DF8 #####################
################ FIG1 START ###################
df8_fig1 = px.bar(df8, x='BLOCKCHAIN', y=['ACTIVE_PERCENTAGE', 'INACTIVE_PERCENTAGE'], title='Active and Inactive Token Percentage by Blockchain', color_discrete_map={'ACTIVE_PERCENTAGE': 'green', 'INACTIVE_PERCENTAGE': 'red'})
df8_fig1.update_layout(barmode='stack', hovermode='x unified', yaxis_title="PERCENTAGE")
################# FIG1 END ####################
###############################################
################ FIG2 START ###################
df8_fig2 = px.bar(df8.sort_values(by='UNIQUE_TOKENS', ascending=False), x='BLOCKCHAIN', y='UNIQUE_TOKENS',
                  title='Unique Tokens by Blockchain')
df8_fig2.update_layout(hovermode='x unified')
################# FIG2 END ####################

##################### DF9 #####################
################ FIG1 START ###################
df9_fig1 = px.bar(df9.sort_values(by='AVG_LIFESPAN_DAYS', ascending=False), x='BLOCKCHAIN', y='AVG_LIFESPAN_DAYS', title='Average Token Lifespan (Days) by Blockchain')
df9_fig1.update_layout(hovermode="x unified")
################# FIG1 END ####################

##################### DF10 #####################
################ FIG1 START ###################
df10_fig1 = px.bar(df10, x='BLOCKCHAIN', y='PERCENTAGE', title='Token Lifespan Distribution by Blockchain', color='CATEGORY', color_discrete_sequence=px.colors.qualitative.Set1)
df10_fig1.update_layout(barmode='stack', hovermode='x unified')

##################### DF11 #####################
################ FIG1 START ###################
df11_fig1 = px.pie(df11, names='CATEGORY', values='PERCENTAGE', title='Percentage of Tokens by Lifespan Category')
################# FIG1 END ####################

##################### DF12 #####################
################ FIG1 START ###################
df12_fig1 = px.line(df12, x='DATE', y='UNIQUE_TOKEN_COUNT', title='Daily Unique Tokens vs Average Transaction Fee USD')
df12_fig1.update_layout(hovermode="x unified", yaxis2=dict(title='Avg Txn Fee USD', overlaying='y', side='right'))
df12_fig1.add_trace(go.Scatter(x=df12['DATE'], y=df12['AVG_TX_FEE_USD'], mode='lines', name='Avg Txn Fee USD', yaxis='y2'))
################# FIG1 END ####################

##################### DF13 #####################
################ FIG1 START ###################
df13_fig1 = px.scatter(df13,
     x="HOUR",
     y="DAY",
     size="TOKEN",
     size_max=10,
     color="TOKEN",
     hover_data={'TOKEN':True,
                 'DAY':True,
                 'HOUR':True
                },
     title="Distribution of Unique Tokens Traded by Weekday & Hour")
################# FIG1 END ####################

##################### DF14 #####################
################ FIG1 START ###################
df14_fig1 = px.scatter(df14,
     x="HOUR",
     y="DAY",
     size="NEW_TOKENS",
     size_max=10,
     color="NEW_TOKENS",
     hover_data={'NEW_TOKENS':True,
                 'DAY':True,
                 'HOUR':True
                },
     title="Distribution of New Tokens by Weekday & Hour")
################# FIG1 END ####################

##################### DF17 #####################
################ FIG1 START ###################
# Aggregate by blockchain to get total swaps per blockchain
df17_sorted = df17.groupby('BLOCKCHAIN', as_index=False)['NUMBER_OF_SWAPS'].sum().sort_values(by='NUMBER_OF_SWAPS', ascending=False)

# Merge back with the original dataframe to maintain the color information
df17_sorted_full = df17.merge(df17_sorted[['BLOCKCHAIN']], on='BLOCKCHAIN', how='right')

# Create the bar plot, sorting by total NUMBER_OF_SWAPS per blockchain
df17_fig1 = px.bar(df17_sorted_full, x='BLOCKCHAIN', y='NUMBER_OF_SWAPS', color='TOKEN', 
                   title='Top 10 Tokens Swapped to by Number of Swaps per Blockchain', 
                   barmode='stack', hover_data={'BLOCKCHAIN': False})

df17_fig1.update_layout(hovermode="x unified")
################# FIG1 END ####################

##################### DF18 #####################
################ FIG1 START ###################
# Aggregate by blockchain to get total swaps per blockchain
df18_sorted = df18.groupby('BLOCKCHAIN', as_index=False)['NUMBER_OF_SWAPS'].sum().sort_values(by='NUMBER_OF_SWAPS', ascending=False)

# Merge back with the original dataframe to maintain the color information (TOKEN)
df18_sorted_full = df18.merge(df18_sorted[['BLOCKCHAIN']], on='BLOCKCHAIN', how='right')

# Create the bar plot, sorting by total NUMBER_OF_SWAPS per blockchain
df18_fig1 = px.bar(df18_sorted_full, x='BLOCKCHAIN', y='NUMBER_OF_SWAPS', color='TOKEN', 
                   title='Top 10 Tokens Swapped from by Number of Swaps per Blockchain', 
                   barmode='stack', hover_data={'BLOCKCHAIN': False})

df18_fig1.update_layout(hovermode="x unified")
################# FIG1 END ####################

##################### DF19 #####################
################ FIG1 START ###################
# Aggregate by blockchain to get total unique traders per blockchain
df19_sorted = df19.groupby('BLOCKCHAIN', as_index=False)['UNIQUE_TRADERS'].sum().sort_values(by='UNIQUE_TRADERS', ascending=False)

# Merge back with the original dataframe to maintain the color information (TOKEN)
df19_sorted_full = df19.merge(df19_sorted[['BLOCKCHAIN']], on='BLOCKCHAIN', how='right')

# Create the bar plot, sorting by total UNIQUE_TRADERS per blockchain
df19_fig1 = px.bar(df19_sorted_full, x='BLOCKCHAIN', y='UNIQUE_TRADERS', color='TOKEN', 
                   title='Top 10 Tokens Swapped to by Unique Traders per Blockchain', 
                   barmode='stack', hover_data={'BLOCKCHAIN': False})

df19_fig1.update_layout(hovermode="x unified")
################# FIG1 END ####################

##################### DF20 #####################
################ FIG1 START ###################
# Aggregate by blockchain to get total unique traders per blockchain
df20_sorted = df20.groupby('BLOCKCHAIN', as_index=False)['UNIQUE_TRADERS'].sum().sort_values(by='UNIQUE_TRADERS', ascending=False)

# Merge back with the original dataframe to maintain the color information (TOKEN)
df20_sorted_full = df20.merge(df20_sorted[['BLOCKCHAIN']], on='BLOCKCHAIN', how='right')

# Create the bar plot, sorting by total UNIQUE_TRADERS per blockchain
df20_fig1 = px.bar(df20_sorted_full, x='BLOCKCHAIN', y='UNIQUE_TRADERS', color='TOKEN', 
                   title='Top 10 Tokens Swapped from by Unique Traders per Blockchain', 
                   barmode='stack', hover_data={'BLOCKCHAIN': False})

df20_fig1.update_layout(hovermode="x unified")
################# FIG1 END ####################

##################### DF21 #####################
################ FIG1 START ###################
# Aggregate by blockchain to get total swap volume (USD) per blockchain
df21_sorted = df21.groupby('BLOCKCHAIN', as_index=False)['TOTAL_SWAP_VOLUME_USD'].sum().sort_values(by='TOTAL_SWAP_VOLUME_USD', ascending=False)

# Merge back with the original dataframe to maintain the color information (TOKEN_PAIR)
df21_sorted_full = df21.merge(df21_sorted[['BLOCKCHAIN']], on='BLOCKCHAIN', how='right')

# Create the bar plot, sorting by total TOTAL_SWAP_VOLUME_USD per blockchain
df21_fig1 = px.bar(df21_sorted_full, x='BLOCKCHAIN', y='TOTAL_SWAP_VOLUME_USD', color='TOKEN_PAIR', 
                   title='Top 10 Token Pairs by USD Volume per Blockchain [logarithmic scale]', 
                   barmode='stack', hover_data={'BLOCKCHAIN': False})

# Set hover mode and apply logarithmic scale to the y-axis
df21_fig1.update_layout(hovermode="x unified")
df21_fig1.update_yaxes(type="log", secondary_y=False)
################# FIG1 END ####################

##################### DF22 #####################
################ FIG1 START ###################
# Aggregate by blockchain to get total swap count per blockchain
df22_sorted = df22.groupby('BLOCKCHAIN', as_index=False)['TOTAL_SWAP_COUNT'].sum().sort_values(by='TOTAL_SWAP_COUNT', ascending=False)

# Merge back with the original dataframe to maintain the color information (TOKEN_PAIR)
df22_sorted_full = df22.merge(df22_sorted[['BLOCKCHAIN']], on='BLOCKCHAIN', how='right')

# Create the bar plot, sorting by total TOTAL_SWAP_COUNT per blockchain
df22_fig1 = px.bar(df22_sorted_full, x='BLOCKCHAIN', y='TOTAL_SWAP_COUNT', color='TOKEN_PAIR', 
                   title='Top 10 Token Pairs by Number of Swaps per Blockchain', 
                   barmode='stack', hover_data={'BLOCKCHAIN': False})

df22_fig1.update_layout(hovermode="x unified")
################# FIG1 END ####################

##################### DF23 #####################
################ FIG1 START ###################
# Aggregate by blockchain to get total unique trader count per blockchain
df23_sorted = df23.groupby('BLOCKCHAIN', as_index=False)['UNIQUE_TRADER_COUNT'].sum().sort_values(by='UNIQUE_TRADER_COUNT', ascending=False)

# Merge back with the original dataframe to maintain the color information (TOKEN_PAIR)
df23_sorted_full = df23.merge(df23_sorted[['BLOCKCHAIN']], on='BLOCKCHAIN', how='right')

# Create the bar plot, sorting by total UNIQUE_TRADER_COUNT per blockchain
df23_fig1 = px.bar(df23_sorted_full, x='BLOCKCHAIN', y='UNIQUE_TRADER_COUNT', color='TOKEN_PAIR', 
                   title='Top 10 Token Pairs by Unique Traders per Blockchain', 
                   barmode='stack', hover_data={'BLOCKCHAIN': False})

df23_fig1.update_layout(hovermode="x unified")
################# FIG1 END ####################

##################### DF24 #####################
################ FIG1 START ###################
df24_fig1 = px.bar(df24, x='EXPANSION_PATH', y='TOKEN_COUNT', title='Token Expansion Across Blockchains: From First to Second Chain (Tokens on Multiple Chains Only)')
df24_fig1.update_layout(hovermode="x unified")
################# FIG1 END ####################

##################### DF25 #####################
################ FIG1 START ###################
df25_fig1 = px.pie(df25, names='NUMBER_OF_CHAINS', values='TOKEN_COUNT', title='Distribution of Tokens by Number of Active Chains')
################# FIG1 END ####################

colored_header(
    label="",
    description="",
    color_name="gray-70",
)

col_1a, col_1b, col_1c = st.columns(3)
with col_1a:
    st.metric("Unique Tokens", millify(df28['TOTAL_TOKENS'][0], precision=1))
    st.link_button("View SQL", f"{url28}")
with col_1b:
    st.metric("Unique Pairs", millify(df26['TOTAL_UNIQUE_PAIRS'][0], precision=1))
    st.link_button("View SQL", f"{url26}")
with col_1c:
    st.metric("Avg Token Lifespan (Days)", df27['AVG_LIFESPAN_DAYS'][0])
    st.link_button("View SQL", f"{url27}")

col_2a, col_2b = st.columns(2)
with col_2a:
    st.plotly_chart(df1_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url1}")
with col_2b:
    st.plotly_chart(df2_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url2}")

col_3a, col_3b = st.columns(2)
with col_3a:
    st.plotly_chart(df4_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url4}")
with col_3b:
    st.plotly_chart(df5_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url5}")

st.plotly_chart(df12_fig1, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url12}")

insight_1 = '''<p style='font-family:sans-serif; color:#4d372c; font-size: 18px;'>There has been a consistent rise in unique tokens and token pairs traded on Uniswap, with Ethereum maintaining its dominant position. This growth surged notably in 2023, culminating in a dramatic peak in late July 2024. During this period, the Base blockchain led with a significant contribution, accounting for 86% of the unique tokens and 79% of the token pairs traded, with overall totals across all blockchains reaching 43,000 and 48,000, respectively.</p>

<p style='font-family:sans-serif; color:#4d372c; font-size: 18px;'>The recent activity surge on Base can be attributed to several factors. The Dencun upgrade made L2s like Base much cheaper to transact on, which is evident from the inverse relationship between transaction fees and unique token counts. Higher fees often correlate with temporary dips in token activity. Additionally, the memecoin craze further spurred Base's activity, even surpassing Ethereum at its peak.</p><p style='font-family:sans-serif; color:#4d372c; font-size: 18px;'>While chains like Arbitrum, Optimism, Polygon, BSC, and Avalanche exhibit lower activity, the overall trend reflects a significant market-wide increase in Uniswap tokens trading activity.</p>'''
st.markdown(insight_1, unsafe_allow_html=True)

col_4a, col_4b = st.columns(2)
with col_4a:
    st.plotly_chart(df3_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url3}")
with col_4b:
    st.plotly_chart(df8_fig2, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url8}")

insight_2 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">There is a clear upward trend in the number of unique tokens traded on both Uniswap V2 and V3, with V2 consistently leading in unique tokens. A notable surge occurred in V2 towards the end of July 2024, reaching over 41,000 unique tokens traded in a single week, predominantly on the Base blockchain.</p><p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">In terms of token distribution across different blockchains, Ethereum stands out with over 120,000 unique tokens, while Base, despite being the newest blockchain, follows with around 55,000 unique tokens. Other blockchains such as Polygon, Arbitrum, BSC, Optimism, and Avalanche have significantly fewer unique tokens, each below 10,000. This distribution underscores Ethereum\'s central role in Uniswap\'s ecosystem and highlights the emerging significance of L2s like Base.</p>'
st.markdown(insight_2, unsafe_allow_html=True)

col_5a, col_5b = st.columns(2)
with col_5a:
    st.plotly_chart(df6_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url6}")
with col_5b:
    st.plotly_chart(df7_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url7}")

insight_3 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">New tokens have been in a steady upward trajectory over time, punctuated by occasional spikes in activity. By 2024, the cumulative count of new tokens has surpassed 150,000, with a particularly notable surge in early 2024 where weekly new token counts exceed 3,000.</p><p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">By blockchain, Ethereum consistently leads in new token launches, underscoring its role as the primary platform for token launches. However, the most striking observation is the dramatic surge on Base in April 2024. Other blockchains like Arbitrum, Optimism, Polygon, BSC, and Avalanche display lower but steady levels of new token creation.</p>'
st.markdown(insight_3, unsafe_allow_html=True) 

col_6a, col_6b = st.columns(2)
with col_6a:
    st.plotly_chart(df9_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url9}")
with col_6b:
    st.plotly_chart(df10_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url10}")

insight_4 = '''<p style="font-family:sans-serif;color:#4d372c;font-size:18px;">
Optimism leads with the longest average token lifespan of over 236 days, followed by Polygon and Ethereum. This suggests that tokens on these chains tend to have more longevity and potentially more stability. In contrast, Base has the shortest average lifespan at around 50 days.
</p>
'''
st.markdown(insight_4, unsafe_allow_html=True)

insight_4_1 = '''<p style="font-family:sans-serif;color:#4d372c;font-size:18px;">
When we break down the token lifespan distribution into three categories: long-lived (more than 30 days), medium-lived (7 to 30 days), and short-lived (less than 7 days), we observe the following

1. Base and BSC have the highest proportion of long-lived tokens, suggesting more established or sustainable projects on these platforms.
2. Arbitrum shows a more balanced distribution across all three categories, indicating a diverse ecosystem with both new and established tokens.
3. Ethereum, despite its prominence, has a surprisingly high percentage of short-lived tokens. This could reflect its role as an incubator for new projects, many of which may not survive long-term.
</p>
'''
st.markdown(insight_4_1, unsafe_allow_html=True)

col_7a, col_7b = st.columns(2)
with col_7a:
    st.plotly_chart(df11_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url11}")
with col_7b:
    st.plotly_chart(df8_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url8}")

insight_5_1 = '''<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">
Long-lived tokens (more than 30 days) make up the largest segment at 47.3%, closely followed by short-lived tokens (less than 7 days) at 44.8%. Medium-lived tokens (7 to 30 days) represent a much smaller portion at 7.85%. This distribution suggests a polarized token ecosystem on Uniswap where most tokens either establish themselves for the long term or fail quickly, with relatively few occupying the middle ground.
</p>'''

insight_5_2 = '''<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">
Observing the percentage of active and inactive tokens across blockchains, notably, all blockchains show a significantly higher percentage of inactive tokens compared to active ones. BSC (Binance Smart Chain), Optimism and Avalanche have the highest proportion of active tokens - 35% each. Ethereum, despite being the most established blockchain, has the lowest percentages of active tokens, with less than 14% active tokens. Base has the second lowest active token percentage, at about 16%.
</p>'''

insight_5_3 = '''<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">
The Uniswap token ecosystem is characterized by extremes, with most tokens either surviving past the 30-day mark or failing within a week. This indicates a challenging environment where tokens must quickly prove their value or face obsolescence.
</p>'''

insight_5_4 = '''<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">
Across all blockchains, inactive tokens far outnumber active ones. This suggests a high rate of token abandonment or failure, which is consistent with the high percentage of short-lived tokens shown in the token lifespan pie chart.
</p>'''

insight_5_5 = '''<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">
Ethereum's low percentage of active tokens, despite its prominence, might reflect its maturity as a platform. It could have accumulated a large number of inactive tokens over time, while still maintaining a significant number of active tokens in absolute terms.
</p>'''
st.markdown(insight_5_1, unsafe_allow_html=True)
st.markdown(insight_5_2, unsafe_allow_html=True)
st.markdown(insight_5_3, unsafe_allow_html=True)
st.markdown(insight_5_4, unsafe_allow_html=True)
st.markdown(insight_5_5, unsafe_allow_html=True)

col_8a, col_8b = st.columns(2)
with col_8a:
    st.plotly_chart(df13_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url13}")
with col_8b:
    st.plotly_chart(df14_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url14}")

insight_6 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">The highest number of unique tokens are traded between 09:00 UTC and 14:00 UTC on Saturdays.<br>New token launches are fairly evenly spread throughout the week, but they peak between 17:00 UTC and 21:00 UTC, marking this timeframe the most popular for new token releases.</p>'
st.markdown(insight_6, unsafe_allow_html=True)

col_9a, col_9b = st.columns(2)
with col_9a:
    st.plotly_chart(df17_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url17}")
with col_9b:
    st.plotly_chart(df18_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url18}")

col_10a, col_10b = st.columns(2)
with col_10a:
    st.plotly_chart(df19_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url19}")
with col_10b:
    st.plotly_chart(df20_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url20}")

insight_7 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">Ethereum and stablecoins dominate the number of swaps on Uniswap, but when looking at unique traders across chains, especially on Base, the significant presence of memecoins stands out. This highlights the substantial role memecoins play in driving user acquisition for Uniswap.</p>'
st.markdown(insight_7, unsafe_allow_html=True)

col_11a, col_11b = st.columns(2)
with col_11a:
    st.plotly_chart(df22_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url22}")
with col_11b:
    st.plotly_chart(df23_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url23}")

col_12a, col_12b = st.columns(2)
with col_12a:
    st.plotly_chart(df21_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url21}")
with col_12b:
    st.plotly_chart(df25_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url25}")

st.plotly_chart(df24_fig1, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url24}")

insight_8 = '<p style=\"font-family:sans-serif; color:#4d372c; font-size: 18px;\">\nExamining token expansions from their original chain to a secondary chain reveals that the \"Ethereum → Base\" path is by far the most prevalent, with around 16,000 tokens taking this route—more than all other expansion paths combined. The next most popular paths are \"Ethereum → Polygon\" and \"Ethereum → Arbitrum,\" with 2,800 and 1,800 tokens, respectively.</p>'
st.markdown(insight_8, unsafe_allow_html=True)

insight_8_1 = '<p style=\"font-family:sans-serif; color:#4d372c; font-size: 18px;\">There are relatively low token counts for expansions between chains that don\'t involve Ethereum. This suggests that direct token migrations between alternative chains are less common, with most cross-chain activity centering around Ethereum.</p>'
st.markdown(insight_8_1, unsafe_allow_html=True)

colored_header(
    label="",
    description="",
    color_name="gray-70",
)
st.markdown(f'<h1 style="color:#434346;font-size:40px;text-align:center;">Final Thoughts</h1>', unsafe_allow_html=True)
colored_header(
    label="",
    description="",
    color_name="gray-70",
)
conclusion = '''<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">
Uniswap’s token ecosystem is evolving fast, marked by big shifts and surprises. The rise of unique tokens and pairs has been nothing short of remarkable, with Ethereum leading the charge, as expected, but the recent explosion on Base turned heads. Late July 2024 was a game-changer—Base accounted for a staggering 86% of unique tokens and 79% of pairs traded, driven by low fees and a memecoin frenzy that briefly saw Base outpace Ethereum itself.</p>

<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">Token creation is also booming. It took three years to hit 75,000 tokens, but just one more to double that to 150,000. Ethereum still sets the pace, but Base’s early 2024 surge, with nearly 5,000 new tokens in a week, signals a fresh wave of innovation.</p>

<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">We’ve seen it all in token lifespans too—Optimism and Polygon have some of the longest-lasting tokens, while on Base, it’s more of a sink-or-swim scenario, with many tokens not making it past 50 days. It’s a tough market out there; nearly half of all tokens don’t survive their first week, highlighting Uniswap’s nature as a proving ground where success isn’t guaranteed.</p>

<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">Meanwhile, swap activity tells its own story. Ethereum and stablecoins still dominate, but it’s the memecoins, especially on Base, that are drawing in traders. This just goes to show the unexpected power of these fun, speculative assets in driving user engagement.</p>

<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">And as for token expansion, it’s clear: Ethereum remains the heart of the network. The “Ethereum to Base” path is the most popular, dwarfing other routes, with thousands of tokens using Ethereum as a launchpad for cross-chain growth.</p>

<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">Uniswap’s landscape is a mix of stability, innovation, and a touch of chaos. The trends we’re seeing now—rising token diversity, rapid expansion, and the constant ebb and flow of new and old players—paint a picture of a DeFi world that’s anything but predictable. There’s more ahead, and it’s going to be exciting to see where Uniswap goes next.</p>'''
st.markdown(conclusion, unsafe_allow_html=True)
