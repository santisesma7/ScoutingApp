"""
Simple test to verify session state persists across Streamlit pages.
Run: streamlit run test_session_state.py
"""

import streamlit as st

st.set_page_config(page_title="Session State Test", layout="wide")

st.markdown("# Session State Persistence Test")

# Initialize session state
if "test_value" not in st.session_state:
    st.session_state.test_value = "not set"

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

st.markdown(f"**Current session state:**")
st.json({
    "authenticated": st.session_state.authenticated,
    "test_value": st.session_state.test_value
})

st.markdown("---")

# Simple login form
st.markdown("### Set Session Value")
input_val = st.text_input("Enter a value:", value=st.session_state.test_value)

if st.button("Set Value"):
    st.session_state.test_value = input_val
    st.session_state.authenticated = True
    st.success(f"Session value set to: {input_val}")
    st.success(f"Authenticated: True")

st.markdown("---")

# Show instructions
st.markdown("""
**To test persistence:**
1. Enter a value above and click "Set Value"
2. Use the navigation to go to another page (if available)
3. Come back to this page
4. Your value should still be here!

If using multi-page app:
- Create pages/ folder with test pages that check st.session_state["test_value"]
- Navigate between pages to see if session state persists
""")
