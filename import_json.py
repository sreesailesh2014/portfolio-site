import streamlit as st
import json

# Title
st.title("CIBIL Report Analyzer")

# Upload JSON file
uploaded_file = st.file_uploader("Upload CIBIL JSON", type="json")

if uploaded_file is not None:
    # Load JSON
    data = json.load(uploaded_file)

    # Display summary
    st.subheader("📊 Report Summary")
    st.write(f"Report Date: {data['cibilReport']['reportDate']}")
    st.write(f"CIBIL Score: {data['cibilReport']['score']}")
    st.write(f"Name: {data['cibilReport']['personalInfo']['name']}")
    st.write(f"DOB: {data['cibilReport']['personalInfo']['dob']}")
    st.write(f"PAN: {data['cibilReport']['personalInfo']['pan']}")

    # Tradeline search
    st.subheader("🔍 Search Tradelines")
    search_term = st.text_input("Enter Account Number or Institution")
    tradelines = data['cibilReport']['tradelines']

    if search_term:
        results = [t for t in tradelines if search_term.lower() in t['accountNumber'].lower() 
                   or search_term.lower() in t['institution'].lower()]
        st.write("Search Results:", results)

    # Show all tradelines
    st.subheader("📂 All Tradelines")
    for t in tradelines:
        st.json(t)

    # Recommendation logic
    st.subheader("💡 Recommendations")
    score = data['cibilReport']['score']

    if score >= 750:
        st.success("Excellent score! You are eligible for most loans and credit cards.")
    elif 650 <= score < 750:
        st.warning("Fair score. Improve repayment history to boost eligibility.")
    else:
        st.error("Low score. Focus on clearing overdue accounts and reducing DPD.")

    # Check overdue / write-off / DPD
    for t in tradelines:
        if "DPD" in "".join(t.get("paymentHistory", [])):
            st.warning(f"Tradeline {t['accountNumber']} has DPD issues.")
        if t.get("status") == "Write-off":
            st.error(f"Tradeline {t['accountNumber']} is written off.")
        if t.get("currentBalance", 0) > t.get("sanctionedAmount", 0):
            st.error(f"Tradeline {t['accountNumber']} shows overdue balance.")
            

            
