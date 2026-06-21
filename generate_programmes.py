import re
import os

with open("index.html", "r") as f:
    fr_content = f.read()

with open("index-en.html", "r") as f:
    en_content = f.read()

def generate_page(content, lang="fr"):
    # Extract Head
    head_match = re.search(r'(<head>.*?</head>)', content, re.DOTALL)
    head = head_match.group(1) if head_match else ""

    # Extract Header (including mobile menu btn and site-nav)
    header_match = re.search(r'(<header class="site-header">.*?</header>)', content, re.DOTALL)
    header = header_match.group(1) if header_match else ""

    # Update relative links in header/footer to point correctly from programs page
    # Since they are absolute in standard layouts (index.html#about etc.), make sure we sync
    header = header.replace('href="#about"', f'href="index{"-en" if lang=="en" else ""}.html#about"')
    header = header.replace('href="#academics"', f'href="index{"-en" if lang=="en" else ""}.html#academics"')
    header = header.replace('href="#contact"', f'href="index{"-en" if lang=="en" else ""}.html#contact"')
    header = header.replace('href="#formations"', f'href="programmes{"-en" if lang=="en" else ""}.html"')
    
    if lang == "en":
        header = header.replace('href="index.html" class="nav-lang"', 'href="programmes.html" class="nav-lang"')
    else:
        header = header.replace('href="index-en.html" class="nav-lang"', 'href="programmes-en.html" class="nav-lang"')

    # Extract Footer
    footer_match = re.search(r'(<footer class="site-footer">.*?</footer>)', content, re.DOTALL)
    footer = footer_match.group(1) if footer_match else ""
    # Update footer links
    footer = footer.replace('href="#about"', f'href="index{"-en" if lang=="en" else ""}.html#about"')
    footer = footer.replace('href="#academics"', f'href="index{"-en" if lang=="en" else ""}.html#academics"')
    footer = footer.replace('href="#contact"', f'href="index{"-en" if lang=="en" else ""}.html#contact"')
    footer = footer.replace('href="#formations"', f'href="programmes{"-en" if lang=="en" else ""}.html"')

    # Content pieces specific to languages
    if lang == "fr":
        hero_section = """        <section class="hero-section">
            <div class="hero-image-wrapper hero-secondary fade-up">
                <img src="./assets/hero.jpeg" alt="Campus Superia Team" class="hero-img"
                    onerror="this.src='https://images.unsplash.com/photo-1577896851231-70ef18881754?q=80&w=2070&auto=format&fit=crop'">
                <div class="hero-overlay">
                    <div class="hero-text-area">
                        <span class="overline" style="color: white; margin-bottom: 0.5rem; display: block; font-weight: bold; text-transform: uppercase;">Pour vous</span>
                        <h1 class="display-title" style="font-size: 3.5rem;">Nos Formations Linguistiques</h1>
                        <p class="hero-subtitle">Découvrez nos programmes conçus pour vous accompagner à chaque étape de votre apprentissage, du niveau élémentaire à la maîtrise parfaite. Nous cultivons vos compétences pour vous aider à communiquer avec aisance.</p>
                        <div class="hero-search-gadget">
                            <div class="gadget-select-group">
                                <label for="gadget-program">Programme</label>
                                <div class="select-wrapper">
                                    <select id="gadget-program">
                                        <option value="">Tous les programmes</option>
                                        <option value="BTS">BTS (Bac+2 alternance)</option>
                                        <option value="A2">Pré-intermédiaire - A2</option>
                                        <option value="B1">Intermédiaire - B1</option>
                                        <option value="B2">Avancé - B2</option>
                                        <option value="C1">Autonome - C1</option>
                                        <option value="C2">Maîtrise - C2</option>
                                    </select>
                                    <span class="select-arrow">
                                        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
                                    </span>
                                </div>
                            </div>
                            <div class="gadget-select-group">
                                <label for="gadget-specialization">Spécialisation</label>
                                <div class="select-wrapper">
                                    <select id="gadget-specialization">
                                        <option value="">Toutes spécialités</option>
                                        <option value="general">Français Général</option>
                                        <option value="business">Français Professionnel & Affaires</option>
                                        <option value="exam">Préparation Examens</option>
                                        <option value="eloquence">Éloquence & Leadership</option>
                                    </select>
                                    <span class="select-arrow">
                                        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
                                    </span>
                                </div>
                            </div>
                            <div class="gadget-select-group">
                                <label for="gadget-campus">Campus / Format</label>
                                <div class="select-wrapper">
                                    <select id="gadget-campus">
                                        <option value="">Tous formats</option>
                                        <option value="paris">Paris (Neuilly)</option>
                                        <option value="online">En Ligne / E-Learning</option>
                                    </select>
                                    <span class="select-arrow">
                                        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
                                    </span>
                                </div>
                            </div>
                            <button class="gadget-search-btn" id="btn-search-gadget" aria-label="Rechercher">
                                <span>Rechercher</span>
                               <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </section>"""
        
        filter_gadget = ""
        
        filter_status_bar = """            <!-- Dynamic Filter Status Bar -->
            <div class="filter-status-bar" id="filter-status-bar" style="display: none;">
                <div class="filter-status-title">Filtres actifs :</div>
                <div class="filter-status-tags" id="filter-status-tags"></div>
                <button class="filter-clear-btn" id="filter-clear-btn">Effacer les filtres</button>
            </div>"""

        cards = [
            {
                "level": "A2",
                "family": "fle",
                "title": "Niveau Pré-intermédiaire - A2 (FLE)",
                "specs": "general,exam",
                "campuses": "paris,online",
                "img": "formation-new-1.jpg",
                "points": [
                    ("point-icon-foundation", "Bases essentielles avec rigueur et méthode"),
                    ("point-icon-expression", "Première expression fiable et structurée"),
                    ("point-icon-guided", "Situations simples et encadrées")
                ]
            },
            {
                "level": "B1",
                "family": "fle",
                "title": "Niveau Intermédiaire - B1 (FLE)",
                "specs": "general,business,exam",
                "campuses": "paris,online",
                "img": "formation-new-2.jpg",
                "points": [
                    ("point-icon-communication", "Communication claire et cohérente"),
                    ("point-icon-growth", "Progression régulière des compétences"),
                    ("point-icon-professional", "Interactions en contextes variés et professionnels")
                ]
            },
            {
                "level": "B2",
                "family": "fle",
                "title": "Niveau Avancé - B2 (FLE)",
                "specs": "general,business,eloquence,exam",
                "campuses": "paris,online",
                "img": "formation-new-3.jpg",
                "points": [
                    ("point-icon-expression", "Expression fluide et structurée"),
                    ("point-icon-argument", "Argumentation persuasive et convaincante"),
                    ("point-icon-demanding", "Intégration dans des environnements exigeants")
                ]
            },
            {
                "level": "C1",
                "family": "fle",
                "title": "Niveau Autonome - C1 (FLE)",
                "specs": "general,business,eloquence,exam",
                "campuses": "paris",
                "img": "formation-new-4.jpg",
                "points": [
                    ("point-icon-expression", "Expression précise, nuancée et impactante"),
                    ("point-icon-complex", "Traitement de sujets complexes"),
                    ("point-icon-demanding", "Aisance en contextes intellectuels exigeants")
                ]
            },
            {
                "level": "C2",
                "family": "fle",
                "title": "Niveau Maîtrise - C2 (FLE)",
                "specs": "general,business,eloquence",
                "campuses": "paris",
                "img": "formation-new-5.jpg",
                "points": [
                    ("point-icon-mastery", "Maîtrise complète avec finesse et exigence"),
                    ("point-icon-communication", "Communication naturelle à haut niveau"),
                    ("point-icon-global", "Environnements internationaux compétitifs")
                ]
            },
            # Parcours anglais
            {
                "level": "A2",
                "family": "english",
                "title": "Anglais Pré-intermédiaire - A2",
                "specs": "general,exam",
                "campuses": "paris,online",
                "img": "formation-new-1.jpg",
                "points": [
                    ("point-icon-foundation", "Acquisition des bases de la communication quotidienne"),
                    ("point-icon-expression", "Vocabulaire courant et structures de phrases clés"),
                    ("point-icon-guided", "Compréhension simple et dialogues guidés")
                ]
            },
            {
                "level": "B1",
                "family": "english",
                "title": "Anglais Intermédiaire - B1",
                "specs": "general,business,exam",
                "campuses": "paris,online",
                "img": "formation-new-2.jpg",
                "points": [
                    ("point-icon-communication", "Aisance dans les conversations courantes et de voyage"),
                    ("point-icon-growth", "Rédaction d'e-mails et de textes simples"),
                    ("point-icon-professional", "Premières interactions dans un cadre professionnel")
                ]
            },
            {
                "level": "B2",
                "family": "english",
                "title": "Anglais Professionnel - B2",
                "specs": "general,business,eloquence,exam",
                "campuses": "paris,online",
                "img": "formation-new-3.jpg",
                "points": [
                    ("point-icon-expression", "Expression fluide lors de réunions et négociations"),
                    ("point-icon-argument", "Présentations orales et rédaction de rapports détaillés"),
                    ("point-icon-demanding", "Compétences clés pour l'entreprise internationale")
                ]
            },
            {
                "level": "C1",
                "family": "english",
                "title": "Anglais Avancé & Préparation IELTS / TOEFL",
                "specs": "general,business,eloquence,exam",
                "campuses": "paris,online",
                "img": "formation-new-4.jpg",
                "points": [
                    ("point-icon-expression", "Expression d'excellence, négociation et leadership"),
                    ("point-icon-complex", "Examens blancs réguliers et simulations intensives"),
                    ("point-icon-demanding", "Score ciblé garanti pour universités et grands groupes")
                ]
            },
            # BTS
            {
                "level": "BTS",
                "family": "bts",
                "title": "BTS Management Commercial Opérationnel - MCO",
                "specs": "general,business",
                "campuses": "paris,online",
                "img": "formation-new-6.jpg",
                "points": [
                    ("point-icon-professional", "Gestion opérationnelle : Stocks, budgets, indicateurs (KPI) et rentabilité"),
                    ("point-icon-communication", "Management d'équipe commerciale : Recrutement, animation et encadrement"),
                    ("point-icon-expression", "Relation client &amp; développement : Dynamisation de l'espace de vente et marketing")
                ]
            },
            {
                "level": "BTS",
                "family": "bts",
                "title": "BTS Négociation et Digitalisation de la Relation Client - NDRC",
                "specs": "business,eloquence",
                "campuses": "paris,online",
                "img": "formation-new-7.jpg",
                "points": [
                    ("point-icon-communication", "Relation client &amp; négociation : Prospection, négociation de vente et fidélisation"),
                    ("point-icon-complex", "Digitalisation omnicanale : CRM, e-commerce, réseaux sociaux et social selling"),
                    ("point-icon-global", "Animation de réseaux : Gestion des partenaires, distributeurs et vente directe")
                ]
            },
            {
                "level": "BTS",
                "family": "bts",
                "title": "BTS Gestion de la PME - GPME",
                "specs": "general,business",
                "campuses": "paris",
                "img": "formation-new-8.jpg",
                "points": [
                    ("point-icon-professional", "Gestion administrative &amp; financière : Organisation comptable et pilotage d'activité"),
                    ("point-icon-growth", "Ressources humaines (GRH) : Gestion du personnel et soutien au développement"),
                    ("point-icon-foundation", "Gestion des risques : Prévention des risques opérationnels et financiers")
                ]
            },
            {
                "level": "BTS",
                "family": "bts",
                "title": "BTS Commerce International - CI",
                "specs": "business,exam",
                "campuses": "paris,online",
                "img": "formation-new-9.jpg",
                "points": [
                    ("point-icon-expression", "Prospection &amp; négociation : Analyse de marchés et relation interculturelle"),
                    ("point-icon-global", "Gestion de l'import-export : Logistique, douane et Supply Chain"),
                    ("point-icon-mastery", "Gestion des risques globaux : Suivi de contrats, financements et devises")
                ]
            },
            # Bachelor
            {
                "level": "Bachelor",
                "family": "bachelor",
                "title": "Bachelor Marketing & Business Development",
                "specs": "general,business",
                "campuses": "paris,online",
                "img": "scroll-actual-1.jpg",
                "points": [
                    ("point-icon-foundation", "Titre RNCP Niveau 6 certifié par l'État"),
                    ("point-icon-growth", "Troisième année effectuée entièrement en alternance (financement 100%)"),
                    ("point-icon-professional", "Spécialisations : Marketing Digital, Vente, Management de projet")
                ]
            },
            {
                "level": "Bachelor",
                "family": "bachelor",
                "title": "BBA - Bachelor of Business Administration",
                "specs": "business,exam",
                "campuses": "paris,online",
                "img": "scroll-actual-2.jpg",
                "points": [
                    ("point-icon-global", "Cursus d'affaires internationales 100% bilingue"),
                    ("point-icon-communication", "Semestres d'études à l'étranger et doubles diplômes"),
                    ("point-icon-complex", "Immersion professionnelle complète en entreprise globale")
                ]
            },
            {
                "level": "Bachelor",
                "family": "bachelor",
                "title": "Master of Science (MSc) Finance & Management",
                "specs": "business,exam",
                "campuses": "paris",
                "img": "scroll-actual-3.jpg",
                "points": [
                    ("point-icon-mastery", "Cursus Bac+5 haut niveau, Titre RNCP Niveau 7"),
                    ("point-icon-demanding", "Intervenants professionnels actifs issus des plus grands groupes"),
                    ("point-icon-growth", "Réseau de 10 000 entreprises partenaires pour votre alternance")
                ]
            }
        ]
        
        btn_brochure = "Brochure"
        btn_signup = "En savoir plus"
        
        tabs_html = """            <!-- Program Families Selector Tab Bar -->
            <div class="program-families-tabs-container fade-up">
                <div class="program-families-tabs">
                    <button class="tab-btn active" data-family="all">Toutes nos formations</button>
                    <button class="tab-btn" data-family="fle">Parcours FLE</button>
                    <button class="tab-btn" data-family="english">Parcours anglais</button>
                    <button class="tab-btn" data-family="bts">BTS</button>
                    <button class="tab-btn" data-family="bachelor">Bachelor</button>
                </div>
            </div>"""
    else:
        hero_section = """        <section class="hero-section">
            <div class="hero-image-wrapper hero-secondary fade-up">
                <img src="./assets/hero.jpeg" alt="Campus Superia Team" class="hero-img"
                     onerror="this.src='https://images.unsplash.com/photo-1577896851231-70ef18881754?q=80&w=2070&auto=format&fit=crop'">
                <div class="hero-overlay">
                    <div class="hero-text-area">
                        <span class="overline" style="color: white; margin-bottom: 0.5rem; display: block; font-weight: bold; text-transform: uppercase;">Made for you</span>
                        <h1 class="display-title" style="font-size: 3.5rem;">Our Linguistic & Higher Ed Programmes</h1>
                        <p class="hero-subtitle">Discover our programs designed to support you at every stage of your learning journey, from elementary language courses to state-certified degrees. We cultivate your skills for your academic and career success.</p>
                        <div class="hero-search-gadget">
                            <div class="gadget-select-group">
                                <label for="gadget-program">Program</label>
                                <div class="select-wrapper">
                                    <select id="gadget-program">
                                        <option value="">All programs</option>
                                        <option value="BTS">BTS (Bac+2 Work-Study)</option>
                                        <option value="Bachelor">Bachelor & BBA</option>
                                        <option value="A2">Pre-intermediate - A2</option>
                                        <option value="B1">Intermediate - B1</option>
                                        <option value="B2">Advanced - B2</option>
                                        <option value="C1">Autonomous - C1</option>
                                        <option value="C2">Mastery - C2</option>
                                    </select>
                                    <span class="select-arrow">
                                        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
                                    </span>
                                </div>
                            </div>
                            <div class="gadget-select-group">
                                <label for="gadget-specialization">Specialization</label>
                                <div class="select-wrapper">
                                    <select id="gadget-specialization">
                                        <option value="">All specializations</option>
                                        <option value="general">General Studies</option>
                                        <option value="business">Professional & Business Focus</option>
                                        <option value="exam">Exam Preparation</option>
                                        <option value="eloquence">Eloquence & Leadership</option>
                                    </select>
                                    <span class="select-arrow">
                                        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
                                    </span>
                                </div>
                            </div>
                            <div class="gadget-select-group">
                                <label for="gadget-campus">Campus / Format</label>
                                <div class="select-wrapper">
                                    <select id="gadget-campus">
                                        <option value="">All formats</option>
                                        <option value="paris">Paris (Neuilly)</option>
                                        <option value="online">Online / E-Learning</option>
                                    </select>
                                    <span class="select-arrow">
                                        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
                                    </span>
                                </div>
                            </div>
                            <button class="gadget-search-btn" id="btn-search-gadget" aria-label="Search">
                                <span>Search</span>
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </section>"""
        
        filter_gadget = ""
        
        filter_status_bar = """            <!-- Dynamic Filter Status Bar -->
            <div class="filter-status-bar" id="filter-status-bar" style="display: none;">
                <div class="filter-status-title">Active Filters:</div>
                <div class="filter-status-tags" id="filter-status-tags"></div>
                <button class="filter-clear-btn" id="filter-clear-btn">Clear Filters</button>
            </div>"""

        cards = [
            {
                "level": "A2",
                "family": "fle",
                "title": "Pre-intermediate Level - A2 (FLE)",
                "specs": "general,exam",
                "campuses": "paris,online",
                "img": "formation-new-1.jpg",
                "points": [
                    ("point-icon-foundation", "Essential foundations with rigor and method"),
                    ("point-icon-expression", "First reliable and structured expression"),
                    ("point-icon-guided", "Simple, guided communication situations")
                ]
            },
            {
                "level": "B1",
                "family": "fle",
                "title": "Intermediate Level - B1 (FLE)",
                "specs": "general,business,exam",
                "campuses": "paris,online",
                "img": "formation-new-2.jpg",
                "points": [
                    ("point-icon-communication", "Clear and coherent communication"),
                    ("point-icon-growth", "Steady, progressive skill building"),
                    ("point-icon-professional", "Varied and professional interactions")
                ]
            },
            {
                "level": "B2",
                "family": "fle",
                "title": "Advanced Level - B2 (FLE)",
                "specs": "general,business,eloquence,exam",
                "campuses": "paris,online",
                "img": "formation-new-3.jpg",
                "points": [
                    ("point-icon-expression", "Fluent and structured expression"),
                    ("point-icon-argument", "Persuasive argumentation and confidence"),
                    ("point-icon-demanding", "Integration into demanding environments")
                ]
            },
            {
                "level": "C1",
                "family": "fle",
                "title": "Autonomous Level - C1 (FLE)",
                "specs": "general,business,eloquence,exam",
                "campuses": "paris",
                "img": "formation-new-4.jpg",
                "points": [
                    ("point-icon-expression", "Precise, nuanced, and impactful expression"),
                    ("point-icon-complex", "Confidence with complex subjects"),
                    ("point-icon-demanding", "Ease in intellectually demanding contexts")
                ]
            },
            {
                "level": "C2",
                "family": "fle",
                "title": "Mastery Level - C2 (FLE)",
                "specs": "general,business,eloquence",
                "campuses": "paris",
                "img": "formation-new-5.jpg",
                "points": [
                    ("point-icon-mastery", "Complete mastery with finesse and high standards"),
                    ("point-icon-communication", "Natural high-level communication"),
                    ("point-icon-global", "International and competitive environments")
                ]
            },
            # English Pathways
            {
                "level": "A2",
                "family": "english",
                "title": "Pre-Intermediate English - A2",
                "specs": "general,exam",
                "campuses": "paris,online",
                "img": "formation-new-1.jpg",
                "points": [
                    ("point-icon-foundation", "Acquire essentials of everyday English communication"),
                    ("point-icon-expression", "Common vocabulary and key sentence structures"),
                    ("point-icon-guided", "Simple listening comprehension and guided dialogues")
                ]
            },
            {
                "level": "B1",
                "family": "english",
                "title": "Intermediate English - B1",
                "specs": "general,business,exam",
                "campuses": "paris,online",
                "img": "formation-new-2.jpg",
                "points": [
                    ("point-icon-communication", "Confidence in travel and casual conversations"),
                    ("point-icon-growth", "Writing simple emails and structured texts"),
                    ("point-icon-professional", "First interactions in a professional workplace")
                ]
            },
            {
                "level": "B2",
                "family": "english",
                "title": "Professional English - B2",
                "specs": "general,business,eloquence,exam",
                "campuses": "paris,online",
                "img": "formation-new-3.jpg",
                "points": [
                    ("point-icon-expression", "Fluent expression in meetings and negotiations"),
                    ("point-icon-argument", "Deliver business presentations and draft detailed reports"),
                    ("point-icon-demanding", "Core competencies for global enterprise contexts")
                ]
            },
            {
                "level": "C1",
                "family": "english",
                "title": "Advanced English & IELTS / TOEFL Prep",
                "specs": "general,business,eloquence,exam",
                "campuses": "paris,online",
                "img": "formation-new-4.jpg",
                "points": [
                    ("point-icon-expression", "Mastery of advanced communication, negotiation and leadership"),
                    ("point-icon-complex", "Regular mock exams and intensive preparation modules"),
                    ("point-icon-demanding", "Target score guarantee for top universities and firms")
                ]
            },
            # BTS
            {
                "level": "BTS",
                "family": "bts",
                "title": "BTS Operational Commercial Management - MCO",
                "specs": "general,business",
                "campuses": "paris,online",
                "img": "formation-new-6.jpg",
                "points": [
                    ("point-icon-professional", "Operational management: Stocks, budgets, indicators (KPI), and profitability"),
                    ("point-icon-communication", "Commercial team management: Recruitment, animation, and supervision"),
                    ("point-icon-expression", "Customer relations &amp; development: Store layout dynamics and marketing")
                ]
            },
            {
                "level": "BTS",
                "family": "bts",
                "title": "BTS Negotiation and Digitalization of Customer Relations - NDRC",
                "specs": "business,eloquence",
                "campuses": "paris,online",
                "img": "formation-new-7.jpg",
                "points": [
                    ("point-icon-communication", "Customer relations &amp; negotiation: Prospecting, sales negotiation, and loyalty"),
                    ("point-icon-complex", "Omnichannel digitalization: CRM, e-commerce, social media, and social selling"),
                    ("point-icon-global", "Network animation: Managing partners, distributors, and direct sales")
                ]
            },
            {
                "level": "BTS",
                "family": "bts",
                "title": "BTS Small &amp; Medium Enterprise Management - GPME",
                "specs": "general,business",
                "campuses": "paris",
                "img": "formation-new-8.jpg",
                "points": [
                    ("point-icon-professional", "Administrative &amp; financial management: Accounting organization and activity pilot"),
                    ("point-icon-growth", "Human Resources (HRM): Personnel management and development support"),
                    ("point-icon-foundation", "Risk management: Prevention of operational and financial risks")
                ]
            },
            {
                "level": "BTS",
                "family": "bts",
                "title": "BTS International Trade - CI",
                "specs": "business,exam",
                "campuses": "paris,online",
                "img": "formation-new-9.jpg",
                "points": [
                    ("point-icon-expression", "Prospecting &amp; negotiation: Market analysis and intercultural relations"),
                    ("point-icon-global", "Import-export management: Logistics, customs, and Supply Chain"),
                    ("point-icon-mastery", "Global risk management: Contract tracking, financing, and currencies")
                ]
            },
            # Bachelor
            {
                "level": "Bachelor",
                "family": "bachelor",
                "title": "Bachelor in Marketing & Business Development",
                "specs": "general,business",
                "campuses": "paris,online",
                "img": "scroll-actual-1.jpg",
                "points": [
                    ("point-icon-foundation", "State-certified RNCP Level 6 Bachelor degree"),
                    ("point-icon-growth", "Third year fully completed in work-study (100% tuition funded)"),
                    ("point-icon-professional", "Tracks: Digital Marketing, Sales Development, Project Management")
                ]
            },
            {
                "level": "Bachelor",
                "family": "bachelor",
                "title": "BBA - Bachelor of Business Administration",
                "specs": "business,exam",
                "campuses": "paris,online",
                "img": "scroll-actual-2.jpg",
                "points": [
                    ("point-icon-global", "100% bilingual international business curriculum"),
                    ("point-icon-communication", "Study abroad semesters and double degree options"),
                    ("point-icon-complex", "Full professional immersion in multinational enterprises")
                ]
            },
            {
                "level": "Bachelor",
                "family": "bachelor",
                "title": "Master of Science (MSc) Finance & Management",
                "specs": "business,exam",
                "campuses": "paris",
                "img": "scroll-actual-3.jpg",
                "points": [
                    ("point-icon-mastery", "High-level Bac+5 curriculum, State-certified RNCP Level 7"),
                    ("point-icon-demanding", "Active industry guest speakers from top financial institutions"),
                    ("point-icon-growth", "Access to 10,000 corporate partner slots for apprenticeship placement")
                ]
            }
        ]
        
        btn_brochure = "Brochure"
        btn_signup = "Learn more"
        
        tabs_html = """            <!-- Program Families Selector Tab Bar -->
            <div class="program-families-tabs-container fade-up">
                <div class="program-families-tabs">
                    <button class="tab-btn active" data-family="all">All Programs</button>
                    <button class="tab-btn" data-family="fle">French Pathways (FLE)</button>
                    <button class="tab-btn" data-family="english">English Pathways</button>
                    <button class="tab-btn" data-family="bts">BTS (Bac+2)</button>
                    <button class="tab-btn" data-family="bachelor">Bachelor &amp; BBA</button>
                </div>
            </div>"""

    grid_html = ""
    for card in cards:
        points_html = ""
        for icon_cls, pt_text in card["points"]:
            points_html += f'                            <li><span class="point-icon {icon_cls}"></span>{pt_text}</li>\n'
        
        grid_html += f"""
                <div class="program-card-detail" data-family="{card['family']}" data-level="{card['level']}" data-specializations="{card['specs']}" data-campuses="{card['campuses']}">
                    <img src="./assets/{card['img']}" alt="{card['title']}" class="program-card-detail-img">
                    <div class="program-card-detail-body">
                        <h3>{card['title']}</h3>
                        <ul class="program-points">
{points_html}                        </ul>
                        <div class="program-card-actions">
                            <a href="index{"-en" if lang=="en" else ""}.html#contact" class="btn btn-outline-brand">{btn_brochure}</a>
                            <a href="index{"-en" if lang=="en" else ""}.html#contact" class="btn btn-brand-orange">{btn_signup}</a>
                        </div>
                    </div>
                </div>"""

    # Clean the replace logic for Title replacement to prevent dual titles/head tags
    clean_head = head.replace('<title>Campus Superia Web</title>', '<title>Campus Superia - Programmes</title>')
    clean_head = clean_head.replace('<title>Campus Superia</title>', '<title>Campus Superia - Programmes</title>')

    full_html = f"""<!DOCTYPE html>
<html lang="{lang}">
{clean_head}
<body>
    <main>
        {header}
        
{hero_section}

        <section class="programmes-grid-container">
{tabs_html}
{filter_status_bar}

            <div class="programmes-grid">
{grid_html}
            </div>
        </section>
    </main>
    {footer}
    <script src="script.js?v=10"></script>
    <script>
        document.querySelectorAll('.hero-nav a').forEach(link => {{
            link.addEventListener('click', () => {{
                document.querySelector('.hero-nav').classList.remove('active');
            }});
        }});
    </script>
</body>
</html>
"""
    return full_html

# Generate the files
with open("programmes.html", "w") as f:
    f.write(generate_page(fr_content, "fr"))

with open("programmes-en.html", "w") as f:
    f.write(generate_page(en_content, "en"))

print("Program pages generated successfully!")
