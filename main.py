import re
import streamlit as st

from services.resume_service import extract_text_from_pdf
from services.voice_service import record_voice
from agents.supervisor import InterviewSupervisor
from agents.evaluation_agent import evaluate_answer

# ---------------- Load CSS ----------------

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🤖 AI Interview Assistant")

# ---------------- Session State ----------------

if "candidate_profile" not in st.session_state:
    st.session_state.candidate_profile = None

if "generated_questions" not in st.session_state:
    st.session_state.generated_questions = []

if "questions" not in st.session_state:
    st.session_state.questions = []

if "answers" not in st.session_state:
    st.session_state.answers = {}

if "current" not in st.session_state:
    st.session_state.current = 0

# ---------------- Upload Resume ----------------

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    resume_text = extract_text_from_pdf(uploaded_file)

    # Run supervisor only once
    if st.session_state.candidate_profile is None:

        supervisor = InterviewSupervisor()

        result = supervisor.start_interview(resume_text)

        if isinstance(result["questions"], str) and result["questions"].startswith("ERROR"):
            st.error(result["questions"])
            st.stop()

        st.session_state.candidate_profile = result["profile"]
        st.session_state.ats_report = result["ats"]
        st.session_state.generated_questions = result["questions"]

    st.subheader("📄 Candidate Profile")
    st.json(st.session_state.candidate_profile)

    st.divider()

    st.subheader("📊 ATS Resume Analysis")

    ats = st.session_state.ats_report
    

    ats_score = re.search(r"ATS Score:\s*(.*)", ats)
    skills_match = re.search(r"Skills Match:\s*(.*)", ats)

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "⭐ ATS Score",
            ats_score.group(1) if ats_score else "-"
    )

    with col2:
        st.metric(
            "📈 Skills Match",
            skills_match.group(1) if skills_match else "-"
    )

    missing = re.search(
        r"Missing Keywords:\s*(.*?)\s*Strengths:",
        ats,
        re.DOTALL
    )

    strengths = re.search(
        r"Strengths:\s*(.*?)\s*Weaknesses:",
        ats,
        re.DOTALL
    )


    weaknesses = re.search(
        r"Weaknesses:\s*(.*?)\s*Suggestions:",
        ats,
        re.DOTALL
    )

    suggestions = re.search(
        r"Suggestions:\s*(.*)",
        ats,
        re.DOTALL
    )

    st.divider()

    st.subheader("❌ Missing Keywords")

    if missing:
        st.markdown(missing.group(1).strip())
    else:
        st.info("No missing keywords.")

        st.subheader("💪 Strengths")

    if strengths:
        st.markdown(strengths.group(1).strip())
    else:
        st.info("No strengths found.")

        st.subheader("⚠ Weaknesses")

    if weaknesses:
        st.markdown(weaknesses.group(1).strip())
    else:
        st.info("No weaknesses found.")

        st.subheader("💡 Suggestions")

    if suggestions:
        st.markdown(suggestions.group(1).strip())
    else:
        st.info("No suggestions found.")

        st.divider()

    # ---------------- Generate Questions ----------------

    if st.button("Generate Questions"):

        questions = st.session_state.generated_questions

        lines = questions.split("\n")

        clean_questions = []

        for line in lines:

            line = line.strip()

            if not line:
                continue

            if line.lower().startswith("here are"):
                continue

            line = re.sub(r"^\d+\.\s*", "", line)

            clean_questions.append(line)

        st.session_state.questions = clean_questions
        st.session_state.answers = {}
        st.session_state.current = 0

        st.rerun()

    # ---------------- Interview Screen ----------------

    if st.session_state.questions:

        total = len(st.session_state.questions)
        current = st.session_state.current

        st.progress((current + 1) / total)

        st.subheader(f"Question {current + 1} of {total}")

        st.write(st.session_state.questions[current])
# ---------- Voice Input ----------

        # ---------- Voice Input ----------

        st.write("🎤 Speak your answer or type below.")

        voice_answer = record_voice()

# If speech is recognized, save it and rerun
        if voice_answer:
            st.session_state.answers[current] = voice_answer
            st.session_state[f"text_{current}"] = voice_answer
            st.rerun()

# Initialize text box
        if f"text_{current}" not in st.session_state:
            st.session_state[f"text_{current}"] = st.session_state.answers.get(current, "")

# Text Area
        answer = st.text_area(
            "Your Answer",
            key=f"text_{current}",
            height=200
        )

# Save manual edits
        st.session_state.answers[current] = answer

        col1, col2 = st.columns(2)

        with col1:

            if current > 0:

                if st.button("⬅ Previous"):

                    st.session_state.answers[current] = answer
                    st.session_state.current -= 1
                    st.rerun()

        with col2:

            if current < total - 1:

                if st.button("Next ➡"):

                    st.session_state.answers[current] = answer
                    st.session_state.current += 1
                    st.rerun()

        if current == total - 1:

            if st.button("Submit Interview"):

                st.session_state.answers[current] = answer

                answers = []

                for i in range(total):
                    answers.append(st.session_state.answers.get(i, ""))

                st.write("DEBUG ANSWERS")
                st.write(answers)

                feedback = evaluate_answer(
                    st.session_state.questions,
                    answers
                )

                if feedback.startswith("ERROR"):
                    st.error(feedback)
                    st.stop()

                st.success("✅ Interview Completed Successfully!")

                st.divider()

                st.header("📊 AI Interview Report")
                                # ---------------- Scores ----------------

                overall = re.search(r"Overall Score:\s*(.*)", feedback)
                technical = re.search(r"Technical Knowledge:\s*(.*)", feedback)
                communication = re.search(r"Communication Skills:\s*(.*)", feedback)
                problem = re.search(r"Problem Solving:\s*(.*)", feedback)
                confidence = re.search(r"Confidence Level:\s*(.*)", feedback)

                col1, col2 = st.columns(2)

                with col1:
                    st.metric(
                        "⭐ Overall Score",
                        overall.group(1) if overall else "-"
                    )

                with col2:
                    st.metric(
                        "💻 Technical Knowledge",
                        technical.group(1) if technical else "-"
                    )

                col3, col4 = st.columns(2)

                with col3:
                    st.metric(
                        "🗣 Communication",
                        communication.group(1) if communication else "-"
                    )

                with col4:
                    st.metric(
                        "🧠 Problem Solving",
                        problem.group(1) if problem else "-"
                    )

                st.metric(
                    "😊 Confidence Level",
                    confidence.group(1) if confidence else "-"
                )

                st.divider()

                strengths = re.search(
                    r"Strengths:(.*?)Weaknesses:",
                    feedback,
                    re.S
                )

                weaknesses = re.search(
                    r"Weaknesses:(.*?)Suggestions:",
                    feedback,
                    re.S
                )

                suggestions = re.search(
                    r"Suggestions:(.*?)Hiring Recommendation:",
                    feedback,
                    re.S
                )

                recommendation = re.search(
                    r"Hiring Recommendation:\s*(.*)",
                    feedback,
                    re.S
                )
                                # ---------------- Strengths ----------------

                st.subheader("💪 Strengths")

                if strengths:
                    st.markdown(strengths.group(1).strip())
                else:
                    st.info("No strengths available.")

                # ---------------- Weaknesses ----------------

                st.subheader("⚠ Weaknesses")

                if weaknesses:
                    st.markdown(weaknesses.group(1).strip())
                else:
                    st.info("No weaknesses available.")

                # ---------------- Suggestions ----------------

                st.subheader("💡 Suggestions")

                if suggestions:
                    st.markdown(suggestions.group(1).strip())
                else:
                    st.info("No suggestions available.")

                # ---------------- Hiring Recommendation ----------------

                st.subheader("🎯 Hiring Recommendation")

                if recommendation:

                    rec = recommendation.group(1).strip().lower()

                    if "selected" in rec and "not" not in rec:
                        st.success("🟢 Selected")

                    elif "maybe" in rec:
                        st.warning("🟡 Maybe Selected")

                    else:
                        st.error("🔴 Not Selected")