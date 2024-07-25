import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")

def main():
    col1, col2, col3 = st.columns([1.5, 5, 1.5])

    with col1:
        option = st.selectbox("Select an option", ["I want to be", "I am skilled in", "Chat with AI"])
    with col2:
        user_input = st.text_input("Enter your input here")
        
    with col3:
        st.markdown('<div style="height:27px;visibility:hidden;"></div>',unsafe_allow_html=True)
        st.button("Submit",use_container_width=True,type="primary")
    data=pd.read_excel("Database/Job_Roles.xlsx")

    # data_columns = data.columns
    data_columns = ['Domain', 'Level', 'Job Roles']
    list_jobs_domain=data['Domain'].to_list()
    list_jobs_Level=data['Level'].to_list()
    list_jobs_roles=data['Job Roles'].to_list()
    key=0
    for i in data_columns:
        st.title(i)
        for j in list_jobs_roles:
            key +=1
            card(j,key)


def card(name,key):
    st.button(name,use_container_width=True,key=key)

    

    

    



if __name__=="__main__":
    main()