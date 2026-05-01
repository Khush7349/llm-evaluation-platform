import streamlit as st
import requests
API = "http://localhost:8000"
st.set_page_config(layout="wide", page_title="Elite LLM Eval", page_icon="🔥")
st.title("🔥 Elite LLM Evaluation Platform")
st.caption("Compare prompts across multiple inputs with automated scoring")
raw_inputs = st.text_area("Inputs (one per line)")
inputs = [i.strip() for i in raw_inputs.split("\n") if i.strip()]
col1, col2 = st.columns(2)
with col1:
    prompt1 = st.text_area("Prompt 1")
with col2:
    prompt2 = st.text_area("Prompt 2")
prompts = [p for p in [prompt1, prompt2] if p and p.strip()]
if st.button("Evaluate"):
    if not inputs:
        st.warning("Please provide at least one input.")
        st.stop()
    if not prompts:
        st.warning("Please provide at least one prompt.")
        st.stop()
    with st.spinner("Evaluating prompts..."):
        try:
            res = requests.post(
                f"{API}/evaluate",
                json={"inputs": inputs, "prompts": prompts},
                timeout=30
            )
            if res.status_code != 200:
                st.error(res.text)
                st.stop()
            payload = res.json()
            data = payload.get("data", payload)
            st.success(f"Completed in {payload.get('time_taken', 'N/A')} sec")
        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.stop()
    st.subheader("🏆 Leaderboard")
    for idx, (p, v) in enumerate(data["leaderboard"], 1):
        score = sum(v["average"].values())
        st.markdown(f"**{idx}.** `{p[:60]}...` → **{round(score, 2)}**")
    st.subheader("📊 Detailed Results")
    for p, v in data["details"].items():
        with st.expander(f"Prompt: {p[:80]}..."):
            st.write("**Average Scores:**", v["average"])
            st.write("**Failure Cases:**", v["failures"])