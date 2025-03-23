from streamlit import session_state as ss
import streamlit as st
from streamlit_msal import Msal

# This MSAL implementation based on the code published at the following GitHub repo:
# https://github.com/WilianZilv/streamlit_msal
# In this app the folder streamlit_msal contains a fork of this Github 
# repo with some modifications to the embedded React.js Code

client_id = "(App Registration Client ID)"
authority = "https://login.microsoftonline.com/(Entra Tenant ID)"

auth_data = Msal.initialize(
    client_id=client_id,
    authority=authority,
    scopes=["User.Read"],  # Ask for a basic profile user info claim
)

if st.button("Sign in"):
    Msal.sign_in() # Show popup to select account

if st.button("Sign out"):
    Msal.sign_out() # Clears auth_data

if st.button("Refresh Token"):
    Msal.revalidate() # refresh the accessToken

if not auth_data:
    st.write("You are not signed in")
else:
    # Getting usefull information
    access_token = auth_data["accessToken"]

    account = auth_data["account"]
    name = account["name"]
    username = account["username"]
    account_id = account["localAccountId"]


    # Display information
    st.write(f"Hello {name}!")
    st.write(f"Your username is: {username}")
    st.write(f"Your account id is: {account_id}")
    st.write("Your access token is:")
    st.code(access_token)

    st.write("Auth data:")
    st.json(auth_data)
