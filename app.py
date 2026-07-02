import streamlit as st 

st.title('Ticket Tatkal')

col1,col2 = st.columns(2)

with col1:
    st.image('image.png')

with col2:
    st.write('You can book Tatkal tickets for a maximum of only 4 passengers per PNR. Book tickets through your IRCTC login ID online on ixigo.' \
    ' Check Tatkal quota seat availability for your train and ticket confirmation probability/prediction.')

st.write('hey nikhil')