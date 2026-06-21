#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os

def sync_page(source_file, target_file, lang="en"):
    print(f"Syncing header from {source_file} to {target_file}...")
    with open(source_file, "r", encoding="utf-8") as f:
        source_content = f.read()
    
    with open(target_file, "r", encoding="utf-8") as f:
        target_content = f.read()

    # Extract header from source
    header_match = re.search(r'(<header class="site-header.*?">.*?</header>)', source_content, re.DOTALL)
    if not header_match:
        print(f"Error: Could not find header in {source_file}")
        return
    
    header = header_match.group(1)

    # Get the class of the header in target to preserve it (e.g. site-header scrolled vs site-header)
    target_header_match = re.search(r'<header class="(site-header[^"]*)"', target_content)
    if target_header_match:
        target_class = target_header_match.group(1)
        header = re.sub(r'class="site-header[^"]*"', f'class="{target_class}"', header)

    # Make absolute link adjustments for non-index pages
    home_file = "index-en.html" if lang == "en" else "index.html"
    header = header.replace('href="#about"', f'href="{home_file}#about"')
    header = header.replace('href="#academics"', f'href="{home_file}#academics"')
    header = header.replace('href="#contact"', f'href="{home_file}#contact"')
    header = header.replace('href="#formations"', f'href="programmes{"-en" if lang=="en" else ""}.html"')

    # Adjust language link based on target page
    target_basename = os.path.basename(target_file)
    if lang == "en":
        # English target page, language switcher should point to French counterpart
        fr_counterpart = target_basename.replace("-en.html", ".html")
        header = re.sub(r'href="index\.html"\s+class="nav-lang"', f'href="{fr_counterpart}" class="nav-lang"', header)
        header = re.sub(r'href=\'index\.html\'\s+class="nav-lang"', f'href="{fr_counterpart}" class="nav-lang"', header)
    else:
        # French target page, language switcher should point to English counterpart
        en_counterpart = target_basename.replace(".html", "-en.html")
        header = re.sub(r'href="index-en\.html"\s+class="nav-lang"', f'href="{en_counterpart}" class="nav-lang"', header)
        header = re.sub(r'href=\'index-en\.html\'\s+class="nav-lang"', f'href="{en_counterpart}" class="nav-lang"', header)

    # Adjust active class for dropdown triggers based on target page
    # 1. Pre-evaluation
    if "test" in target_basename or "analyse" in target_basename:
        # Make Pre-evaluation trigger active
        test_file = "test-en.html" if lang == "en" else "test.html"
        header = header.replace(f'href="{test_file}" class="dropdown-trigger"', f'href="{test_file}" class="dropdown-trigger active"')
        # Ensure Admissions trigger is NOT active
        adm_file = "admissions-en.html" if lang == "en" else "admissions.html"
        header = header.replace(f'href="{adm_file}" class="dropdown-trigger active"', f'href="{adm_file}" class="dropdown-trigger"')
    
    # 2. Admissions
    elif "admissions" in target_basename:
        # Make Admissions trigger active
        adm_file = "admissions-en.html" if lang == "en" else "admissions.html"
        header = header.replace(f'href="{adm_file}" class="dropdown-trigger"', f'href="{adm_file}" class="dropdown-trigger active"')
        # Ensure Pre-evaluation trigger is NOT active
        test_file = "test-en.html" if lang == "en" else "test.html"
        header = header.replace(f'href="{test_file}" class="dropdown-trigger active"', f'href="{test_file}" class="dropdown-trigger"')

    # 3. Partenariats
    elif "partenariats" in target_basename:
        # Make Partenariats active
        part_file = "partenariats-en.html" if lang == "en" else "partenariats.html"
        header = header.replace(f'href="{part_file}"', f'href="{part_file}" class="active"')
        # Ensure Admissions trigger is NOT active
        adm_file = "admissions-en.html" if lang == "en" else "admissions.html"
        header = header.replace(f'href="{adm_file}" class="dropdown-trigger active"', f'href="{adm_file}" class="dropdown-trigger"')
        # Ensure Pre-evaluation trigger is NOT active
        test_file = "test-en.html" if lang == "en" else "test.html"
        header = header.replace(f'href="{test_file}" class="dropdown-trigger active"', f'href="{test_file}" class="dropdown-trigger"')

    # Replace header in target content
    new_target_content = re.sub(r'(<header class="site-header.*?">.*?</header>)', header, target_content, flags=re.DOTALL)
    
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(new_target_content)
    print(f"Successfully synced {target_file}!")

if __name__ == "__main__":
    # Sync English pages
    sync_page("index-en.html", "test-en.html", "en")
    sync_page("index-en.html", "analyse-en.html", "en")
    sync_page("index-en.html", "admissions-en.html", "en")
    sync_page("index-en.html", "admissions-bts-en.html", "en")
    sync_page("index-en.html", "admissions-bachelor-en.html", "en")
    sync_page("index-en.html", "admissions-bba-en.html", "en")
    sync_page("index-en.html", "admissions-msc-en.html", "en")
    sync_page("index-en.html", "partenariats-en.html", "en")

    # Sync French pages (to ensure all are up-to-date and consistent)
    sync_page("index.html", "test.html", "fr")
    sync_page("index.html", "analyse.html", "fr")
    sync_page("index.html", "admissions.html", "fr")
    sync_page("index.html", "admissions-comment-candidater.html", "fr")
    sync_page("index.html", "admissions-bts.html", "fr")
    sync_page("index.html", "admissions-bachelor.html", "fr")
    sync_page("index.html", "admissions-bba.html", "fr")
    sync_page("index.html", "admissions-msc.html", "fr")
    sync_page("index.html", "partenariats.html", "fr")
