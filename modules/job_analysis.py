import spacy

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")


def analyze_job_text(job_description):
    """
    Analyze a pasted job description to extract key details using semantic matching.

    Args:
        job_description (str): Job description text.

    Returns:
        dict: Extracted details (skills, responsibilities, keywords).
    """
    # Reference phrases for semantic similarity
    skill_reference = nlp("skills or qualifications")
    responsibility_reference = nlp("responsibilities or tasks")

    # Placeholder for extracted details
    extracted_details = {"skills": [], "responsibilities": [], "keywords": []}

    # Split the job description into lines
    lines = job_description.split("\n")

    for line in lines:
        line_doc = nlp(line.strip())

        # Check semantic similarity with "skills"
        if line_doc.similarity(skill_reference) > 0.75:
            extracted_details["skills"].append(line.strip())

        # Check semantic similarity with "responsibilities"
        elif line_doc.similarity(responsibility_reference) > 0.75:
            extracted_details["responsibilities"].append(line.strip())

    # Extract general keywords using NLP (focus on nouns and proper nouns)
    doc = nlp(job_description)
    for token in doc:
        if token.pos_ in ["NOUN", "PROPN"]:  # Only include relevant parts of speech
            extracted_details["keywords"].append(token.text)

    # Remove duplicates from the keywords
    extracted_details["keywords"] = list(set(extracted_details["keywords"]))

    return extracted_details
