def generate_questions(skills):

    questions = []

    skill_questions = {

        "python":
        "Explain decorators in Python and where you have used them.",

        "sql":
        "What is the difference between INNER JOIN and LEFT JOIN?",

        "flask":
        "Explain Flask routing and request handling.",

        "machine learning":
        "What is overfitting and how can it be prevented?",

        "deep learning":
        "What is the difference between CNN and RNN?",

        "javascript":
        "Explain the difference between let, var and const.",

        "html":
        "What is semantic HTML?",

        "css":
        "What is Flexbox and when would you use it?",

        "react":
        "Explain React component lifecycle.",

        "aws":
        "What are EC2 and S3 services?",

        "git":
        "Explain git pull, git fetch and git merge.",

        "data analysis":
        "Describe a data analysis project you worked on.",

        "large language models":
        "How do LLMs generate responses?",

        "agentic ai":
        "What is an AI agent and how is it different from a chatbot?"
    }

    for skill in skills:

        if skill in skill_questions:
            questions.append(
                skill_questions[skill]
            )

    return questions