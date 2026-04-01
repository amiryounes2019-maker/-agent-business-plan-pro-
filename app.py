import streamlit as st

st.title("🤖 Agent Business Plan PRO")
nom = st.text_input("Nom porteur", "MALEK KAMEL")
ca = st.number_input("CA Année 1 (€)", 1000000)

if st.button("🚀 Générer Business Plan"):
    st.success("✅ Business Plan créé !")
    st.balloons()
    
    col1, col2 = st.columns(2)
    with col1:
        st.download_button("📊 Excel", data=open("BUSINESS-PLAN-EGJ (1).xlsx","rb").read(), file_name="business_plan.xlsx")
    with col2:
        st.download_button("📄 Word", data=open("BUSINESS-PLAN-EGJ (1).docx","rb").read(), file_name="business_plan.docx")
