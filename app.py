import streamlit as st 

st.title('Ticket Tatkal')

col1,col2 = st.columns(2)

with col1:
    st.image('image.png')

with col2:
    st.write('You can book Tatkal tickets for a maximum of only 4 passengers per PNR. Book tickets through your IRCTC login ID online on ixigo.' \
    ' Check Tatkal quota seat availability for your train and ticket confirmation probability/prediction.')

st.write('hey nikhil can u get me the ticket ')
st.write('need the confiremed ticket ')
st.write('u will get the conformed ticket if not u get 3x')



st.markdown("---")

st.markdown("""
### 🚆 Ticket Tatkal

📞 **Customer Care:** 1800-123-4567  
📧 **Email:** support@tickettatkal.com  
📍 **Contact Us:** Mumbai, India  

© 2026 Ticket Tatkal | All Rights Reserved
""")

st.sidebar.title("Sidebar")
st.sidebar.write("Home")
st.sidebar.write("Courses")
st.sidebar.write("Carrer")
st.sidebar.write("Contact")

