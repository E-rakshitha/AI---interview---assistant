from agents.resume_agent import analyze_resume
from agents.question_agent import generate_questions
from agents.ats_agent import ats_score


class InterviewSupervisor:

    def start_interview(self, resume_text):

        # Resume Analysis
        candidate_profile = analyze_resume(resume_text)

        # ATS Analysis
        ats = ats_score(resume_text)

        # Interview Questions
        questions = generate_questions(candidate_profile)

        return {
            "profile": candidate_profile,
            "ats": ats,
            "questions": questions
        }