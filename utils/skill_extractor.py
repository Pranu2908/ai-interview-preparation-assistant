def extract_skills(text):

    text = text.lower()

    skill_database = {

        "python": [
            "python"
        ],

        "java": [
            "java"
        ],

        "c++": [
            "c++"
        ],

        "javascript": [
            "javascript"
        ],

        "html": [
            "html"
        ],

        "css": [
            "css"
        ],

        "sql": [
            "sql"
        ],

        "mysql": [
            "mysql"
        ],

        "git": [
            "git"
        ],

        "github": [
            "github",
            "git"
        ],

        "aws": [
            "aws"
        ],

        "flask": [
            "flask"
        ],

        "django": [
            "django"
        ],

        "react": [
            "react"
        ],

        "machine learning": [
            "machine learning",
            "ml"
        ],

        "deep learning": [
            "deep learning"
        ],

        "nlp": [
            "nlp"
        ],

        "tensorflow": [
            "tensorflow"
        ],

        "data analysis": [
            "data analysis",
            "analytics",
            "power bi"
        ],

        "large language models": [
            "large language models",
            "llm",
            "llm workflows"
        ],

        "agentic ai": [
            "agentic ai",
            "agent systems",
            "agent-based"
        ],

        "groq": [
            "groq"
        ]
    }

    found_skills = []

    for skill, keywords in skill_database.items():

        for keyword in keywords:

            if keyword in text:

                found_skills.append(skill)

                break

    return found_skills