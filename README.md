# Job Hunt Scraper

A Python-based tool for automating job application processes by dynamically scraping job listings from major career websites and company career pages, intelligently matching job postings to user preferences, and automating the application process with personalized documents.

## 🚧 Project Status: In Progress 🚧
This project is currently under development. Core functionalities are being built incrementally, with a focus on modularity and reusability.

---

## Features (Planned and In Progress)

### ✅ Phase 1: Scraping and Career Section Detection
- Dynamically detect career sections on company websites.
- Handle dynamic content with Playwright.
- Extract relevant job postings and save them locally.

### 🛠️ Phase 2: Job Matching
- Match job postings to user-defined preferences (e.g., keywords, location).
- Use NLP techniques for semantic matching.

### 🛠️ Phase 3: Document Generation
- Generate personalized resumes, cover letters, and answers based on user-provided templates.

### 🛠️ Phase 4: Automated Application Submission
- Automate job application processes for major job boards.
- Handle form submissions, uploads, and confirmations dynamically.

### 🛠️ Phase 5: Scheduling and Automation
- Schedule periodic scraping, matching, and application tasks.

---

## Getting Started

### Prerequisites
1. **Install Python 3.10+** on your system.
2. **Set up a virtual environment** (recommended).
3. **Install required libraries:**
   ```bash
   pip install playwright beautifulsoup4 requests sqlite3 spacy
   playwright install
   python -m spacy download en_core_web_sm
   ```

### Running the Project
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/job-hunt-scraper.git
   cd job-hunt-scraper
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

## Directory Structure
```
job-hunt-scraper/
│
├── data/                   # For SQLite database and logs
│   ├── jobs.db             # SQLite database (to be generated)
│   └── logs/               # Logs for tracking issues
│
├── scraper/                # Core scraper logic
│   ├── career_detector.py  # Detect and navigate to career sections
│   ├── search_handler.py   # Handle search inputs and filters
│   ├── data_extractor.py   # Extract job details
│   ├── utils.py            # Utility functions
│   └── __init__.py         # Makes this a Python package
│
├── notebooks/              # Interactive testing
│   ├── test_scraper.ipynb  # For testing career section detection
│
└── main.py                 # Entry point for running the scraper
```

---

## Roadmap
- [x] Set up environment and basic file structure.
- [ ] Develop **Career Section Detection**.
- [ ] Build **Search Handler** for dynamic search and filtering.
- [ ] Implement **Data Extraction** to parse job details.
- [ ] Create **Job Matching Module** using NLP.
- [ ] Integrate document generation and submission modules.

---

## Contributions
Since this is a personal project, external contributions are not currently being accepted. Feel free to fork the repository if you'd like to experiment or build on it.

---

## License
This project is under the [MIT License](LICENSE).

---

## Acknowledgments
- [Playwright](https://playwright.dev/) for browser automation.
- [spaCy](https://spacy.io/) for natural language processing.
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) for HTML parsing.