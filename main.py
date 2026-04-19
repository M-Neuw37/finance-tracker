#TODO add a graph that shows the amount invested and the value of the stock portfolio over time

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_csv('CSV FILE')

# Sum the columns to be displyed on the dashboard
NatInsurance = df['NI'].sum()
BasicPay = df['Basic.Pay'].sum()
Tax = df['Tax'].sum()
TakeHome = df['Take.Home'].sum()
TotalDeducts = df['Total.Deducts'].sum()
Invested = df['Invested'].sum()
Kept = df['Kept'].sum()
Saved = df['Saved'].sum()
PKCPension = df['PKC.Pension'].sum()

# Streamlit UI

st.set_page_config(page_title = "Personal Finance Tracker")

if 'current_page' not in st.session_state:
    st.session_state.current_page = "Dashboard"

# Sidebar with large "Title" style buttons
st.sidebar.title("Navigation")

# Navigation buttons on the sidebar
if st.sidebar.button("DASHBOARD", use_container_width=True):
    st.session_state.current_page = "Dashboard"

if st.sidebar.button("CUMULATIVE GRAPHS", use_container_width=True):
    st.session_state.current_page = "Cumulative Graphs"

if st.session_state.current_page == "Dashboard":
    st.title("Personal finance tracker monthly dashboard")
    st.subheader("Payroll summary")
    # filter to set the tax year 
    year_type = st.radio("Select View:", ["Calendar Year", "Tax Year (Apr 1st-Mar 31st)"], horizontal=True)
    
    if year_type == "Calendar Year":
        # Get unique years from 'Year' column
        year_list = sorted(df['Year'].unique(), reverse=True)
        selected_year = st.selectbox("Select Year:", year_list)
        filtered_df = df[df['Year'] == selected_year]
    else:
        tax_year_list = sorted(df['Tax.Year'].unique(), reverse=True)
        selected_tax_year = st.selectbox("Select Tax Year:", tax_year_list)
        filtered_df = df[df['Tax.Year'] == selected_tax_year]
        
    BasicPay = filtered_df['Basic.Pay'].sum()
    Tax = filtered_df['Tax'].sum()
    NatInsurance = filtered_df['NI'].sum()
    PKCPension = filtered_df['PKC.Pension'].sum()
    TakeHome = filtered_df['Take.Home'].sum()
    Invested = filtered_df['Invested'].sum()
    Saved = filtered_df['Saved'].sum()
    Kept = filtered_df['Kept'].sum()
    
    # create columns
    
    col1, col2, col3, col4 = st.columns(4)
    col5, col6, col7, col8 = st.columns(4)
    
    with col1:
        st.metric("Gross Basic Pay:", f"£{BasicPay:,.2f}")
        
    with col2:
        st.metric("Tax Paid:", f"£{Tax:,.2f}")
        
    with col3:
        st.metric("National Insurance:", f"£{NatInsurance:,.2f}")
        
    with col4:
        st.metric("Pension Contributions:", f"£{PKCPension:,.2f}")
        
    with col5:
        st.metric("Bottom line:", f"£{TakeHome:,.2f}")
        
    with col6:
        st.metric("Invested:", f"£{Invested:,.2f}")
        
    with col7:
        st.metric("Saved:", f"£{Saved:,.2f}")
        
    with col8:
        st.metric("Kept:", f"£{Kept:,.2f}")
        
    if st.checkbox("Show CSV file"):
        st.write(df)
        
    #st.pyplot(fig)
    
    #Interactive chart
    # TODO fix x axis as it is in the order of feb, jan, march
    
    #st.line_chart(df, x='Month', y=['Basic.Pay', 'Take.Home', 'Saved'])
    # st.line_chart(filtered_df, x='Month', y=['Basic.Pay', 'Take.Home', 'Saved'])
    
    st.divider()
    
    
    st.subheader("Monthly Breakdown")
    month_choice = st.selectbox("Select a month:", df['Month'].unique())
    
    
    month_row = df[df['Month'] == month_choice].iloc[0]
    
    # Display a simple table or specific metrics for that month
    st.write(f"Showing data for: **{month_choice}**")
    st.dataframe(month_row.to_frame().T)
    
    st.divider()

#TODO new page using a side bar to show all of the cumulative charts with the totals above them. 

elif st.session_state.current_page == "Cumulative Graphs":
    st.title("Cumulative Analysis")
    st.subheader("Cumulative Charts")
    
    #Cumulative Tax 
    chart_dataTAX = df.copy()
    chart_dataTAX['Cumulative_Tax'] = chart_dataTAX['Tax'].cumsum()
    
    fig1, ax1 = plt.subplots(figsize=(10, 4))
    
    ax1.plot(chart_dataTAX['Month'], chart_dataTAX['Cumulative_Tax'], color="green", marker='o', linewidth=2, label="Cumulative Tax")
    ax1.set_title("Cumulative Tax Paid")
    st.metric("Total Tax Paid", f"£{df['Tax'].sum():,.2f}")
    st.pyplot(fig1)
    
    # Cumulative Invested
    chart_dataINV = df.copy()
    chart_dataINV['Cumulative_Invsted'] = chart_dataINV['Invested'].cumsum()
    
    fig2, ax2 = plt.subplots(figsize=(10, 4))
    
    ax2.plot(chart_dataINV['Month'], chart_dataINV['Cumulative_Invsted'], color="k", marker='o', linewidth=2, label="Cumulative Invested")
    ax2.set_title("Total Invested")
    st.metric("Total Tax Paid", f"£{df['Invested'].sum():,.2f}")
    st.pyplot(fig2)
    
    # Cumulative Basic Pay
    chart_dataBP = df.copy()
    chart_dataBP['Cumulative_BP'] = chart_dataBP['Basic.Pay'].cumsum()
    
    fig3, ax3 = plt.subplots(figsize=(10, 4))
    
    ax3.plot(chart_dataBP['Month'], chart_dataBP['Cumulative_BP'], color="red", marker='o', linewidth=2, label="Cumulative Invested")
    ax3.set_title("Total Pay")
    st.metric("Total Tax Paid", f"£{df['Basic.Pay'].sum():,.2f}")
    st.pyplot(fig3)
    
    # Cumulative Take home
    chart_dataTH = df.copy()
    chart_dataTH['Cumulative_TH'] = chart_dataBP['Take.Home'].cumsum()
    
    fig4, ax4 = plt.subplots(figsize=(10, 4))
    
    ax4.plot(chart_dataBP['Month'], chart_dataTH['Cumulative_TH'], color="blue", marker='o', linewidth=2, label="Cumulative Invested")
    ax4.set_title("Total Take Home")
    st.metric("Total Tax Paid", f"£{df['Take.Home'].sum():,.2f}")
    st.pyplot(fig3)
