def extract_skills(text):

    skill_database = [

        "python",
        "java",
        "c",
        "c++",
        "javascript",
        "html",
        "css",

        "sql",
        "mysql",
        "mongodb",

        "machine learning",
        "deep learning",
        "artificial intelligence",
        "nlp",

        "tensorflow",
        "keras",
        "pytorch",
        "scikit-learn",

        "flask",
        "django",
        "react",

        "git",
        "github",

        "aws",
        "azure",

        "data analysis",
        "power bi",

        "large language models",
        "llm",
        "agentic ai",
        "groq"
    ]

    found_skills = []

    text = text.lower()

    for skill in skill_database:

        if skill in text:
            found_skills.append(skill)

    return found_skills