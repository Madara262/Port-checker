# Python Reconnaissance & Security Scanner

A modular Python toolkit designed for quick network reconnaissance, service enumeration, and basic web vulnerability assessments.

## Features

- **DNS Reconnaissance:** Resolves domain A records using Scapy packets.
- **Socket Port Scanner:** Scans common TCP ports (`21`, `22`, `23`, `25`, `53`, `80`, `110`, `443`, `993`, `995`) and extracts service banners.
- **Web Scraping & Analysis:** Inspects HTTP status codes, security headers, redirects, and content fingerprints using `requests` and `BeautifulSoup`.
- **Vulnerability Checks:** Performs quick payload testing for basic SQL injection, code injection, and LDAP bypass vectors.

## Installation & Setup

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
   cd YOUR_REPOSITORY_NAME