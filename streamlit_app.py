"""CAIE Grade System Streamlit application."""
from io import StringIO
import pandas as pd
import streamlit as st

st.set_page_config(page_title="CAIE Grade System", page_icon="🎓", layout="wide")
GRADE_BANDS = [(90, "A", "Excellent"), (80, "B", "Very good"), (70, "C", "Good"), (60, "D", "Satisfactory"), (0, "E", "Needs improvement")]

def grade_for(mark):
    return next((grade, label) for minimum, grade, label in GRADE_BANDS if mark >= minimum)
    """Apply the assignment's grade conditions to one mark."""
    if mark >= 90:
        return "A", "Excellent"
    elif mark >= 80:
        return "B", "Very good"
    elif mark >= 70:
        return "C", "Good"
    elif mark >= 60:
        return "D", "Satisfactory"
    else:
        return "E", "Needs improvement"

def colour(grade):
    return {"A":"#2563eb", "B":"#0891b2", "C":"#059669", "D":"#d97706", "E":"#dc2626"}[grade]

st.markdown("""<style>.stApp{background:#f7f8fc}.hero{padding:2rem 2.2rem;border-radius:22px;color:white;background:linear-gradient(115deg,#1e3a8a,#5b21b6);margin-bottom:1.4rem}.hero h1{margin:0;font-size:2.3rem}.hero p{margin:.5rem 0 0;opacity:.9}.grade{padding:1.2rem;border-radius:18px;color:white;text-align:center}.grade h2{font-size:3rem;margin:0}.grade p{margin:.25rem}div[data-testid="stMetric"]{background:white;border:1px solid #e6e8f0;padding:.9rem;border-radius:14px}</style><div class="hero"><h1>🎓 CAIE Grade System</h1><p>Enter a student's marks to create a clear, shareable result summary.</p></div>""", unsafe_allow_html=True)

with st.sidebar:
    st.header("Student details")
    name = st.text_input("Student name", placeholder="e.g. Aisha Khan")
    st.text_input("Candidate number (optional)", placeholder="e.g. 0042")
    st.divider(); st.caption("CAIE scale used")
    for low, grade, label in GRADE_BANDS:
        high = 100 if low == 90 else low + 9
        st.write(f"**{grade}** · {low}–{high} · {label}")
    for mark_range, grade, label in [("90–100", "A", "Excellent"), ("80–89", "B", "Very good"), ("70–79", "C", "Good"), ("60–69", "D", "Satisfactory"), ("0–59", "E", "Needs improvement")]:
        st.write(f"**{grade}** · {mark_range} · {label}")

st.subheader("Assessment marks")
st.caption("Add 1–10 subjects. Every mark must be between 0 and 100.")
if "marks" not in st.session_state:
    st.session_state.marks = pd.DataFrame({"Subject":["English", "Mathematics", "Science"], "Mark":[0.0, 0.0, 0.0]})
marks = st.data_editor(st.session_state.marks, num_rows="dynamic", hide_index=True, use_container_width=True, key="editor", column_config={"Subject":st.column_config.TextColumn("Subject", required=True), "Mark":st.column_config.NumberColumn("Mark / 100", min_value=0.0, max_value=100.0, step=0.5, required=True)})

results = marks.dropna(subset=["Subject", "Mark"]).copy()
results["Subject"] = results["Subject"].astype(str).str.strip()
results = results[results["Subject"] != ""]
if results.empty:
    st.info("Add one completed subject to see a result."); st.stop()
if len(results) > 10:
    st.error("Please keep the result to a maximum of 10 subjects."); st.stop()
results["Grade"], results["Descriptor"] = zip(*results["Mark"].map(grade_for))
average = float(results["Mark"].mean())
overall, descriptor = grade_for(average)
best = results.loc[results["Mark"].idxmax()]

st.divider()
c1, c2, c3, c4 = st.columns([1,1,1,1.15])
c1.metric("Average mark", f"{average:.1f}%")
c2.metric("Subjects", len(results))
c3.metric("Highest mark", f"{best['Mark']:.1f}%", best["Subject"])
c4.markdown(f"<div class='grade' style='background:{colour(overall)}'><p>OVERALL GRADE</p><h2>{overall}</h2><p>{descriptor}</p></div>", unsafe_allow_html=True)
st.subheader("Subject breakdown")
display = results[["Subject", "Mark", "Grade", "Descriptor"]].copy()
display["Mark"] = display["Mark"].map(lambda x: f"{x:.1f}%")
st.dataframe(display, hide_index=True, use_container_width=True)
report = results[["Subject", "Mark", "Grade", "Descriptor"]].copy()
report.loc[len(report)] = ["Overall average", average, overall, descriptor]
buffer = StringIO(); report.to_csv(buffer, index=False)
filename = "_".join((name or "student").lower().split())
st.download_button("Download result as CSV", buffer.getvalue(), f"caie_result_{filename}.csv", "text/csv")