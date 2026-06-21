import re

with open('admissions.html', 'r', encoding='utf-8') as f:
    adm_content = f.read()

# Extract hero section from admissions.html
hero_match = re.search(r'(<section class="hero-section">.*?</section>)', adm_content, re.DOTALL)
if hero_match:
    adm_hero = hero_match.group(1)
    
    with open('parcours-fle.html', 'r', encoding='utf-8') as f:
        fle_content = f.read()
    
    # Extract hero section from parcours-fle.html
    fle_hero_match = re.search(r'(<section class="hero-section">.*?</section>)', fle_content, re.DOTALL)
    if fle_hero_match:
        # We want to replace the hero, BUT we need to keep FLE content!
        pass
