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

    job_description = request.form["job_description"]

    file = request.files["resume"]

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(filepath)

    resume_text = extract_text_from_pdf(
        filepath
    )

    skills = extract_skills(
        resume_text
    )

    jd_skills = extract_skills(
        job_description
    )

    missing_skills = []

    for skill in jd_skills:

        if skill not in skills:
            missing_skills.append(skill)

    matched_skills_count = len(skills)

    missing_skills_count = len(
        missing_skills
    )

    if len(jd_skills) > 0:

        match_score = round(
            (
                (len(jd_skills) - len(missing_skills))
                / len(jd_skills)
            ) * 100,
            2
        )

    else:

        match_score = 75

    readiness_score = (
        calculate_readiness_score(
            match_score,
            missing_skills_count
        )
    )

    interview_questions = (
        generate_questions(
            skills
        )
    )

    recommendations = (
        generate_recommendations(
            missing_skills
        )
    )

    if readiness_score >= 80:
        verdict = "Interview Ready"

    elif readiness_score >= 60:
        verdict = "Almost Ready"

    else:
        verdict = "Needs Preparation"

    return render_template(
        "results.html",

        skills=skills,

        missing_skills=missing_skills,

        match_score=match_score,

        readiness_score=readiness_score,

        interview_questions=interview_questions,

        recommendations=recommendations,

        verdict=verdict,

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