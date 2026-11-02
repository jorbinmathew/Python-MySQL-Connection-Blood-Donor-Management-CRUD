import streamlit as st
from streamlit import text_input

from blood_donor_view import BloodDonorManager

donor_instance=BloodDonorManager()

tab1,tab2=st.tabs(["ADD" , "VIEW"])

with tab1:
    st.header("add new donor")
    Name=st.text_input("Enter Donor Name")
    Phone=st.text_input("Enter Donor contact number")
    blood_group=st.selectbox("select the blood group",["A+","B+","O+","A","B","O","A-","B-","O-"])

    city=st.text_input("Enter the city")
    last_donation=st.text_input("Last Donation")
    if st.button("Add new donor:"):
        donor_instance.post(name=Name,blood_group=blood_group,phone=Phone,city=city,last_donor=last_donation)
        st.success("new donor added successfully")

with tab2:
    st.header("view new donor")
    records=donor_instance.get()
    if records:
        st.table(records)
    else:
        st.warning("No Donor details Found...")