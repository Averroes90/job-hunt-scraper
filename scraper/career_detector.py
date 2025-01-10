# Keywords to identify career-related links
CAREER_KEYWORDS = [
    "careers",
    "jobs",
    "opportunities",
    "join us",
    "work with us",
    "employment",
    "vacancies",
]
from playwright.sync_api import sync_playwright
from urllib.parse import urljoin


def extract_links_from_homepage(homepage_url):
    """
    Extracts all links from a homepage.
    Args:
        homepage_url (str): URL of the homepage to scrape.
    Returns:
        List of tuples (link_text, href).
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to the homepage
        page.goto(homepage_url)
        print(f"Loaded {homepage_url}")

        # Extract all <a> elements
        links = page.query_selector_all("a")
        extracted_links = []

        for link in links:
            href = link.get_attribute("href")
            text = link.inner_text().strip() if link.inner_text() else ""
            if href:
                extracted_links.append((text, href))

        browser.close()
        return extracted_links


def filter_career_links(links, base_url):
    """
    Filters links to find career-related ones based on keywords.
    Args:
        links (list): List of tuples (link_text, href).
        base_url (str): Base URL for resolving relative links.
    Returns:
        List of full URLs for career-related links.
    """
    career_links = []
    for text, href in links:
        lower_text = text.lower()
        lower_href = href.lower()

        # Check if any keyword is in the text or href
        if any(keyword in lower_text for keyword in CAREER_KEYWORDS) or any(
            keyword in lower_href for keyword in CAREER_KEYWORDS
        ):
            # Resolve relative URLs to absolute
            full_url = urljoin(base_url, href)
            career_links.append(full_url)

    return career_links


def find_career_section(homepage_url):
    """
    Finds career-related links from a given homepage URL.
    Args:
        homepage_url (str): URL of the homepage to scrape.
    Returns:
        List of career-related links (absolute URLs).
    """
    links = extract_links_from_homepage(homepage_url)
    career_links = filter_career_links(links, homepage_url)

    if career_links:
        print(f"Found {len(career_links)} potential career links.")
    else:
        print("No career-related links found.")
    return career_links
