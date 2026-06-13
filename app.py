from flask import Flask, render_template, request
from utils.pdf_extractor import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.interview_questions import generate_questions
from utils.readiness_score import calculate_readiness_score
from utils.recommendations import generate_recommendations
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    # Get form data
    job_description = request.form.get("job_description", "")

    file = request.files.get("resume")

    if not file:
        return "No resume uploaded"

    # Save uploaded file
    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(filepath)

    # Extract text
    resume_text = extract_text_from_pdf(filepath)

    # Extract skills
    resume_skills = extract_skills(resume_text)

    # Extract JD skills
    jd_skills = extract_skills(job_description)

    # Missing skills
    missing_skills = []

    for skill in jd_skills:
        if skill not in resume_skills:
            missing_skills.append(skill)

    # Match Score
    if len(jd_skills) > 0:

        matched_skills = len(jd_skills) - len(missing_skills)

        match_score = round(
            (matched_skills / len(jd_skills)) * 100,
            2
        )

    else:

        match_score = 0

    # Readiness Score
    readiness_score = calculate_readiness_score(
        match_score,
        len(missing_skills)
    )

    # Verdict
    if readiness_score >= 80:

        verdict = "Interview Ready"

    elif readiness_score >= 60:

        verdict = "Almost Ready"

    else:

        verdict = "Needs Preparation"

    # Interview Questions
    interview_questions = generate_questions(
        resume_skills
    )

    # Recommendations
    recommendations = generate_recommendations(
        missing_skills
    )

    # Analytics
    matched_skills_count = len(resume_skills)

    missing_skills_count = len(missing_skills)

    return render_template(
        "results.html",

        skills=resume_skills,

        missing_skills=missing_skills,

        match_score=match_score,

        readiness_score=readiness_score,

        verdict=verdict,

        interview_questions=interview_questions,

        recommendations=recommendations,

        resume_text=resume_text,

        matched_skills_count=matched_skills_count,

        missing_skills_count=missing_skills_count
    )


if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=8000,
        debug=True
    )