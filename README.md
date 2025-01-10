# **Job Application Customizer**
A Python-based tool for automating the job application process by analyzing job descriptions (via URL or text input), dynamically generating tailored responses using pre-provided personal documents, and preparing high-quality application materials.

## 🚧 **Project Status: In Progress** 🚧
This project is currently under development. The focus has shifted to prioritize modules that take a job application (via URL or pasted text) and generate highly customized resumes, cover letters, and responses, making the tool immediately useful.

---

## **Features (Planned and In Progress)**

### ✅ **Phase 1: Job Analysis and Customization (Current Priority)**
- Input job applications via URL or pasted text.
- Extract key details like required skills, responsibilities, and keywords.
- Generate customized resumes, cover letters, and responses using pre-provided templates.

### 🛠️ **Phase 2: Document Customization**
- Dynamically match user-provided documents to job requirements.
- Rephrase and tailor content for maximum relevance.

### 🛠️ **Phase 3: Automated Application Submission**
- Automate the filling out and submission of applications on job boards and company websites.
- Handle uploads, form submissions, and confirmations.

### 🛠️ **Phase 4: Job Discovery**
- Scrape major job boards and company career sections to identify relevant roles.
- Dynamically detect career sections on company websites.

### 🛠️ **Phase 5: Scheduling and Automation**
- Automate periodic analysis of job applications and responses.
- Schedule recurring tasks like job discovery and document customization.

---

## **Getting Started**

### **Prerequisites**
1. **Install Python 3.10+** on your system.
2. **Set up a virtual environment** (recommended).
3. **Install required libraries:**
   ```bash
   pip install playwright beautifulsoup4 requests sqlite3 spacy jinja2
   playwright install
   python -m spacy download en_core_web_sm
   ```

---

### **Running the Project**
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/job-application-customizer.git
   cd job-application-customizer
   ```

2. Activate your virtual environment:
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```
   - **Windows:**
     ```cmd
     venv\Scripts\activate
     ```

3. Run the test script:
   ```bash
   python main.py
   ```

---

## **Directory Structure**
```
job-application-customizer/
│
├── data/                     # Data storage
│   ├── personal_documents/   # Pre-provided resumes, essays, cover letters
│   ├── output/               # Generated responses
│
├── modules/                  # Core functionality
│   ├── job_analysis.py       # Analyze job application text or URL
│   ├── document_customizer.py # Generate tailored documents
│   ├── utils.py              # Helper functions
│
├── notebooks/                # Interactive testing
│   ├── test_job_analysis.ipynb  # For testing job analysis functionality
│
├── requirements.txt          # Dependencies
└── main.py                   # Entry point for running the program
```

---

## **Roadmap**
- [x] Set up environment and basic file structure.
- [x] Define the project scope and updated priorities.
- [ ] Develop **Job Analysis Module** to process job descriptions.
- [ ] Build **Document Customization Module** to generate tailored responses.
- [ ] Integrate submission automation for streamlined applications.
- [ ] Add job discovery and tracking capabilities.

---

## **Contributions**
This project is a personal endeavor, and external contributions are not currently being accepted. Feel free to fork the repository if you'd like to experiment or build on it.

---

## **License**
This project is under the [MIT License](LICENSE).

---

## **Acknowledgments**
- [Playwright](https://playwright.dev/) for browser automation.
- [spaCy](https://spacy.io/) for natural language processing.
- [Jinja2](https://jinja.palletsprojects.com/) for dynamic document templates.
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) for HTML parsing.