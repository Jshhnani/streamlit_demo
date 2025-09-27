import streamlit as st
# import pandas as pd


# df = pd.DataFrame({
#     "Name": ["A", "B", "C"],
#     "Score": [90, 85, 88]
# })

# st.dataframe(df)   # Interactive table
# st.table(df)       # Static table
# st.line_chart(df["Score"])

# ----

# dataset = pd.read_csv(r"C:\Users\A.JASWANTH\OneDrive\Documents\Streamlit\loan.csv")

# st.dataframe(dataset)
# st.table(dataset)

# -----
# st.title("Akshita")
# st.header("Jaswanth")
# st.subheader("I love You")
# st.markdown("Parul University")
# st.code(""" for i in range(1, 10):
#             print("Akshita I love u")
# """)

# ------
name = st.text_input("enter the name")
fname = st.text_input("enter the father name")
add = st.text_area("enter the address")
classdata = st.selectbox("select the class :", (1, 2, 3, 4, 5, 6, 7, 8, 9))

button = st.button("Done")
if button:
    st.markdown(f""" 
        
name : {name}  
fname : {fname}  
address : {add}  
Class Data : {classdata}

""")



# -------
# name = st.text_input("Enter your name:")
# age = st.slider("Select your age", 1, 100, 25)
# option = st.selectbox("Choose a color:", ["Red", "Green", "Blue"])

# st.write(f"Hello {name}, you are {age} years old and your favorite color is {option}")
