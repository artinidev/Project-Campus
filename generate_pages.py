#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

HEADER_TEMPLATE = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>{title} — Campus Superia</title>
    <meta name="description" content="{meta_desc}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto+Serif:opsz,wght@8..144,300..700&family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css?v=14">
</head>
<body>
<main>
    <header class="site-header">
        <div class="logo-container"><a href="index.html"><img src="./assets/logo-full.png" alt="Campus Superia Logo"></a></div>
        <button class="mobile-menu-btn" aria-label="Toggle menu" onclick="document.querySelector('.site-nav').classList.toggle('active')"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg></button>
        <nav class="site-nav">
            <a href="index.html#about">\u00c0 propos</a>
            <a href="index.html#academics">Mission</a>
            <a href="programmes.html">Programme</a>
            <div class="nav-dropdown-wrapper">
                <a href="test.html" class="dropdown-trigger"><span>Pr\u00e9-\u00e9valuation</span><svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="chevron-icon"><polyline points="6 9 12 15 18 9"></polyline></svg></a>
                <div class="nav-dropdown">
                    <div class="dropdown-links-col">
                        <div class="dropdown-item opt-analyse"><a href="analyse.html"><span class="item-title">Analyse personnalis\u00e9e de votre projet</span><span class="item-desc">Questionnaire pour orienter le choix de votre formation.</span></a></div>
                        <div class="dropdown-item opt-test"><a href="test.html"><span class="item-title">Pr\u00e9-\u00e9valuation</span><span class="item-desc">Test de positionnement en fran\u00e7ais pour \u00e9valuer votre niveau.</span></a></div>
                    </div>
                    <div class="dropdown-preview-col"><div class="preview-img-container"><img src="./assets/hero.jpeg" class="preview-img img-default" alt="Campus Default"><img src="./assets/scroll-actual-2.jpg" class="preview-img img-analyse" alt="Analyse"><img src="./assets/scroll-actual-1.jpg" class="preview-img img-test" alt="Test"></div></div>
                </div>
            </div>
            <div class="nav-dropdown-wrapper">
                <a href="admissions.html" class="dropdown-trigger">
                    <span>Admissions</span>
                    <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="chevron-icon"><polyline points="6 9 12 15 18 9"></polyline></svg>
                </a>
                <div class="nav-dropdown admissions-mega">
                    <!-- Col 1: Main Category Cards -->
                    <div class="adm-column adm-col-main">
                        <div class="dropdown-col-header">Intégrer Campus Supéria</div>
                        <div class="adm-cards-container">
                            <div class="adm-card-btn active" data-target="candidature">
                                <div class="adm-card-icon">
                                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>
                                </div>
                                <div class="adm-card-text"><span class="adm-card-title">Déposer ma candidature</span></div>
                                <div class="adm-card-arrow">
                                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                                </div>
                            </div>
                            
                            <div class="adm-card-btn" data-target="financement">
                                <div class="adm-card-icon">
                                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>
                                </div>
                                <div class="adm-card-text"><span class="adm-card-title">Financer ma formation</span></div>
                                <div class="adm-card-arrow">
                                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Col 2: Sub-category Cards -->
                    <div class="adm-column adm-col-sub">
                        <!-- Sub-panel for Candidature -->
                        <div class="adm-sub-panel active" id="sub-panel-candidature">
                            <div class="dropdown-col-header">Choisir sa rentrée</div>
                            <div class="adm-cards-container">
                                <div class="adm-card-btn active" data-target="rentree-septembre">
                                    <div class="adm-card-icon">
                                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
                                    </div>
                                    <div class="adm-card-text"><span class="adm-card-title">Rentrée de septembre</span></div>
                                    <div class="adm-card-arrow">
                                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                                    </div>
                                </div>
                                <div class="adm-card-btn" data-target="rentree-fevrier">
                                    <div class="adm-card-icon">
                                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
                                    </div>
                                    <div class="adm-card-text"><span class="adm-card-title">Rentrée de février</span></div>
                                    <div class="adm-card-arrow">
                                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                                    </div>
                                </div>
                                <div class="adm-card-btn" data-target="procedure-internationale">
                                    <div class="adm-card-icon">
                                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
                                    </div>
                                    <div class="adm-card-text"><span class="adm-card-title">Candidats internationaux</span></div>
                                    <div class="adm-card-arrow">
                                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                        <!-- Sub-panel for Financement -->
                        <div class="adm-sub-panel" id="sub-panel-financement">
                            <div class="dropdown-col-header">Le financement des études</div>
                            <div class="adm-cards-container">
                                <div class="adm-card-btn" data-target="financement-options">
                                    <div class="adm-card-icon">
                                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"></rect><line x1="12" y1="10" x2="12" y2="10"></line><line x1="12" y1="14" x2="12" y2="14"></line></svg>
                                    </div>
                                    <div class="adm-card-text"><span class="adm-card-title">Options de financement</span></div>
                                    <div class="adm-card-arrow">
                                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Col 3: Direct Link Lists -->
                    <div class="adm-column adm-col-links">
                        <div class="adm-links-panel active" id="links-panel-rentree-septembre">
                            <div class="dropdown-col-header">Procédures par programme</div>
                            <ul class="adm-detail-links">
                                <li><a href="admissions-bts.html">Admission BTS</a></li>
                                <li><a href="admissions-bachelor.html">Admission Bachelor</a></li>
                                <li><a href="admissions-bba.html">Admission BBA</a></li>
                                <li><a href="admissions-msc.html">Admission MSc</a></li>
                            </ul>
                        </div>
                        <div class="adm-links-panel" id="links-panel-rentree-fevrier">
                            <div class="dropdown-col-header">Faire sa rentrée en Février</div>
                            <ul class="adm-detail-links">
                                <li><a href="admissions-bachelor.html?rentree=fevrier">Admission Bachelor</a></li>
                                <li><a href="admissions-bba.html?rentree=fevrier">Admission BBA</a></li>
                                <li><a href="admissions-msc.html?rentree=fevrier">Admission MSc</a></li>
                            </ul>
                        </div>
                        <div class="adm-links-panel" id="links-panel-procedure-internationale">
                            <div class="dropdown-col-header">Procédure Internationale</div>
                            <ul class="adm-detail-links">
                                <li><a href="admissions-international.html">Admission Internationale Bachelor</a></li>
                                <li><a href="admissions-international.html">Admission Internationale BBA</a></li>
                                <li><a href="admissions-international.html">Admission Internationale MSc</a></li>
                                <li><a href="admissions-international.html#visa">Visa Étudiant</a></li>
                                <li><a href="admissions-international.html#visa">Logement Étudiant</a></li>
                            </ul>
                        </div>
                        <div class="adm-links-panel" id="links-panel-financement-options">
                            <div class="dropdown-col-header">Le financement des études</div>
                            <ul class="adm-detail-links">
                                <li><a href="admissions-frais.html">Frais de scolarité</a></li>
                                <li><a href="admissions-bourses.html">Bourses</a></li>
                                <li><a href="admissions-bourses.html#cpf">Financement</a></li>
                                <li><a href="admissions-frais.html#options">Paiement échelonné</a></li>
                                <li><a href="admissions-bourses.html#alternance">Alternance</a></li>
                            </ul>
                        </div>
                    </div>
                    
                    <!-- Col 4: Preview Card -->
                    <div class="adm-column adm-col-preview">
                        <div class="adm-preview-container">
                            <div class="adm-preview-card active" data-preview="rentree-septembre">
                                <img src="./assets/adm-preview-september.png" alt="Rentrée de Septembre">
                            </div>
                            <div class="adm-preview-card" data-preview="rentree-fevrier">
                                <img src="./assets/adm-preview-september.png" alt="Rentrée de Février">
                            </div>
                            <div class="adm-preview-card" data-preview="procedure-internationale">
                                <img src="./assets/adm-preview-international.png" alt="Procédure Internationale">
                            </div>
                            <div class="adm-preview-card" data-preview="financement-options">
                                <img src="./assets/adm-preview-scholarship.png" alt="Le financement des études">
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <a href="partenariats.html">Partenariats</a>
            <a href="index-en.html" class="nav-lang" aria-label="Switch to English"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg><span>EN</span></a>
            <a href="#contact" class="nav-cta">Contactez-nous</a>
        </nav>
    </header>

    <section class="hero-section">
        <div class="hero-image-wrapper hero-secondary fade-up">
            <img src="{hero_img}" alt="{title}" class="hero-img">
            <div class="hero-overlay">
                <div class="hero-layout">
                    <div class="hero-text-area">
                        <span class="tag" style="color:rgba(255,255,255,0.8);border-color:rgba(255,255,255,0.25);margin-bottom:1.5rem;"><span class="dot" style="background:#fca33d;"></span> Campus Superia</span>
                        <h1 class="display-title">{h1}</h1>
                        <p class="hero-subtitle">{subtitle}</p>
                        <div style="display:flex;gap:1rem;margin-top:2rem;flex-wrap:wrap;">
                            <a href="#contact" class="btn btn-brand-orange" style="border-radius:4px;">Candidater maintenant \u2192</a>
                            <a href="admissions.html" class="btn btn-outline-light" style="border-radius:4px;">Vue d&apos;ensemble</a>
                        </div>
                    </div>
                </div>
                <nav class="page-breadcrumb">{breadcrumb}</nav>
            </div>
        </div>
    </section>
{body}
    <section id="contact" class="form-section card-variant">
        <div class="form-section-header fade-up">
            <div class="header-left"><h2>Pr\u00eat \u00e0 nous<br>rejoindre ?</h2></div>
            <div class="header-right">
                <p>D\u00e9posez votre candidature maintenant. Notre \u00e9quipe vous recontactera sous 72 heures.</p>
                <div class="header-actions">
                    <a href="#contact" class="btn btn-brand-orange">Candidater \u2197</a>
                    <a href="tel:+33781547503" class="btn btn-outline-light">+33 781 547 503</a>
                </div>
            </div>
        </div>
        <div class="form-container fade-up">
            <div class="form-card">
                <div class="form-card-left"><h3>Votre demande en 3 \u00e9tapes</h3><p>Simple, rapide et sans engagement. Votre conseiller d\u00e9di\u00e9 prendra le relais sous 72h.</p><div class="card-features"><span class="feature-tag">Gratuit</span><span class="feature-tag">Rapide</span><span class="feature-tag">D\u00e9di\u00e9</span></div></div>
                <div class="form-card-right">
                    <form action="#" class="campus-form-card" id="multi-step-form">
                        <div class="form-progress"><span class="progress-text">Étape <span id="current-step">1</span> sur 3</span><div class="progress-bar-bg"><div class="progress-bar-fill" id="progress-fill"></div></div></div>
                        <div class="form-step form-step-active" data-step="1">
                            <div class="form-group">
                                <label for="nom">Nom <span class="text-brand-orange">*</span></label>
                                <input type="text" id="nom" name="nom" placeholder="Votre nom" required>
                            </div>
                            <div class="form-group">
                                <label for="prenom">Prénom <span class="text-brand-orange">*</span></label>
                                <input type="text" id="prenom" name="prenom" placeholder="Votre prénom" required>
                            </div>
                            <div class="form-group">
                                <label for="naissance">Date de naissance <span class="text-brand-orange">*</span></label>
                                <input type="date" id="naissance" name="naissance" required>
                            </div>
                            <div class="form-group">
                                <label for="email">Email <span class="text-brand-orange">*</span></label>
                                <input type="email" id="email" name="email" placeholder="exemple@email.com" required>
                            </div>
                            <div class="form-group">
                                <label for="telephone">Téléphone <span class="text-brand-orange">*</span></label>
                                <input type="tel" id="telephone" name="telephone" placeholder="+33 6 XX XX XX XX" required>
                            </div>
                            <div class="form-group">
                                <label for="ville">Ville de résidence <span class="text-brand-orange">*</span></label>
                                <input type="text" id="ville" name="ville" placeholder="Ex: Paris, Lyon..." required>
                            </div>
                            <div class="form-actions form-actions-right">
                                <button type="button" class="btn btn-brand-orange-full btn-next">Suivant</button>
                            </div>
                        </div>
                        <div class="form-step" data-step="2">
                            <div class="form-group">
                                <label for="formation_souhaitee">Formation souhaitée <span class="text-brand-orange">*</span></label>
                                <select id="formation_souhaitee" name="formation_souhaitee" required>
                                    <option value="" disabled selected>Sélectionnez une formation</option>
                                    <option value="BTS">BTS</option>
                                    <option value="Bachelor">Bachelor</option>
                                    <option value="Master">Master</option>
                                    <option value="Formation professionnelle">Formation professionnelle</option>
                                    <option value="Autre">Autre</option>
                                </select>
                            </div>
                            <div class="form-group">
                                <label for="formation_visee">Intitulé de la formation visée <span class="text-brand-orange">*</span></label>
                                <input type="text" id="formation_visee" name="formation_visee" placeholder="Ex: BTS MCO, Bachelor Marketing..." required>
                            </div>
                            <div class="form-group">
                                <label for="niveau_actuel">Niveau d'études actuel (Dernier diplôme / en cours) <span class="text-brand-orange">*</span></label>
                                <input type="text" id="niveau_actuel" name="niveau_actuel" placeholder="Ex: Baccalauréat, Licence..." required>
                            </div>
                            <div class="form-group">
                                <label for="situation_actuelle">Situation actuelle <span class="text-brand-orange">*</span></label>
                                <select id="situation_actuelle" name="situation_actuelle" required>
                                    <option value="" disabled selected>Sélectionnez votre situation</option>
                                    <option value="Étudiant">Étudiant</option>
                                    <option value="Salarié">Salarié</option>
                                    <option value="Demandeur d'emploi">Demandeur d'emploi</option>
                                    <option value="En reconversion">En reconversion</option>
                                    <option value="Autre">Autre</option>
                                </select>
                            </div>
                            <div class="form-actions">
                                <button type="button" class="btn btn-outline-dark btn-prev">Précédent</button>
                                <button type="button" class="btn btn-brand-orange-full btn-next">Suivant</button>
                            </div>
                        </div>
                        <div class="form-step" data-step="3">
                            <div class="form-group">
                                <label for="rythme_souhaite">Rythme souhaité <span class="text-brand-orange">*</span></label>
                                <select id="rythme_souhaite" name="rythme_souhaite" required>
                                    <option value="" disabled selected>Sélectionnez le rythme</option>
                                    <option value="Initial">Initial</option>
                                    <option value="Alternance">Alternance</option>
                                    <option value="Formation continue">Formation continue</option>
                                    <option value="À distance / Hybride">À distance / Hybride</option>
                                </select>
                            </div>
                            <div class="form-group">
                                <label for="motivation">Motivation du candidat <span class="text-brand-orange">*</span></label>
                                <textarea id="motivation" name="motivation" placeholder="Décrivez brièvement votre projet et vos objectifs..." rows="4" required></textarea>
                            </div>
                            <div class="form-group checkbox-group">
                                <label class="custom-checkbox">
                                    <input type="checkbox" id="rgpd" name="rgpd" required>
                                    <span class="checkmark"></span>
                                    <span class="checkbox-text">J'accepte la collecte de mes données par Campus Superia. <a href="#">[Politique de confidentialité]</a> <span class="text-brand-orange">*</span></span>
                                </label>
                            </div>
                            <div class="form-actions">
                                <button type="button" class="btn btn-outline-dark btn-prev">Précédent</button>
                                <button type="submit" class="btn btn-brand-orange-full">Envoyer ma demande</button>
                            </div>
                        </div>
                    </form>                </div>
            </div>
        </div>
    </section>
</main>
<footer class="site-footer">
    <div class="footer-container">
        <div class="footer-col brand-col"><h3 class="footer-brand">Campus Superia</h3><div class="footer-bottom-brand"><img src="./assets/logo-icon.png" alt="Logo" class="footer-badge-img" style="height:30px;width:auto;"><p class="copyright">&copy; 2026, Campus Superia</p></div></div>
        <div class="footer-col"><h4 class="footer-heading">Admissions</h4><ul class="footer-links"><li><a href="admissions.html">Vue d&apos;ensemble</a></li><li><a href="admissions-comment-candidater.html">Comment candidater</a></li><li><a href="admissions-conditions.html">Conditions</a></li><li><a href="admissions-frais.html">Frais</a></li><li><a href="admissions-faq.html">FAQ</a></li></ul></div>
        <div class="footer-col"><h4 class="footer-heading">Suivez-nous</h4><ul class="footer-links"><li><a href="https://www.instagram.com/campus_superia" target="_blank">Instagram \u2197</a></li><li><a href="https://www.tiktok.com/@campussuperia?_r=1&_t=ZN-96ISLCCJ6s2" target="_blank">TikTok \u2197</a></li></ul></div>
        <div class="footer-col contact-col"><h4 class="footer-heading">Contactez-nous</h4><ul class="footer-links"><li><a href="mailto:contact@campussuperia.com">contact@campussuperia.com</a></li><li><a href="mailto:campussuperia@gmail.com">campussuperia@gmail.com</a></li><li><a href="tel:+33781547503">+33 781 547 503</a></li></ul><a href="#contact" class="btn btn-brand-orange-full footer-btn">Candidater</a></div>
    </div>
</footer>
<script src="script.js?v=10"></script>
<script>document.querySelectorAll('.site-nav a').forEach(l=>l.addEventListener('click',()=>{{const n=document.querySelector('.site-nav');if(n)n.classList.remove('active');}}))</script>
</body>
</html>"""

def bc(items):
    parts = []
    for i, (label, url) in enumerate(items):
        if url:
            parts.append(f'<a href="{url}">{label}</a><span class="bc-sep">/</span>')
        else:
            parts.append(f'<span class="bc-current">{label}</span>')
    return ' '.join(parts)

def make(filename, title, meta, h1, subtitle, breadcrumb, hero_img, body):
    en_filename = filename.replace('.html', '-en.html')
    content = HEADER_TEMPLATE.format(
        title=title, meta_desc=meta, h1=h1, subtitle=subtitle,
        hero_img=hero_img, breadcrumb=bc(breadcrumb), body=body
    )
    content = content.replace('href="index-en.html" class="nav-lang"', f'href="{en_filename}" class="nav-lang"')
    
    if 'partenariats' in filename:
        content = content.replace('Candidater maintenant \u2192', 'Devenir partenaire \u2192')
        content = content.replace('href="admissions.html" class="btn btn-outline-light" style="border-radius:4px;">Vue d&apos;ensemble</a>', 'href="mailto:contact@campussuperia.com" class="btn btn-outline-light" style="border-radius:4px;">Nous contacter</a>')
        content = content.replace('<h2>Pr\u00eat \u00e0 nous<br>rejoindre ?</h2>', '<h2>Collaborons<br>ensemble</h2>')
        content = content.replace('D\u00e9posez votre candidature maintenant. Notre \u00e9quipe vous recontactera sous 72 heures.', 'D\u00e9posez votre demande de partenariat. Notre \u00e9quipe vous recontactera sous 72 heures.')
        content = content.replace('Candidater \u2197</a>', 'Devenir partenaire \u2197</a>')
        
        # Replace the admission form with the partnership form
        partenariats_form = """<form action="#" class="campus-form-card" id="multi-step-form">
                        <div class="form-progress"><span class="progress-text">Étape <span id="current-step">1</span> sur 3</span><div class="progress-bar-bg"><div class="progress-bar-fill" id="progress-fill"></div></div></div>
                        <div class="form-step form-step-active" data-step="1">
                            <div class="form-group">
                                <label for="structure">Nom de l’entreprise / association / établissement <span class="text-brand-orange">*</span></label>
                                <input type="text" id="structure" name="structure" placeholder="Ex: Entreprise SAS..." required>
                            </div>
                            <div class="form-group">
                                <label for="contact_nom">Nom, prénom et fonction du contact référent <span class="text-brand-orange">*</span></label>
                                <input type="text" id="contact_nom" name="contact_nom" placeholder="Ex: Dupont Jean, Responsable RH" required>
                            </div>
                            <div class="form-actions form-actions-right">
                                <button type="button" class="btn btn-brand-orange-full btn-next">Suivant</button>
                            </div>
                        </div>
                        <div class="form-step" data-step="2">
                            <div class="form-group">
                                <label for="email">Email <span class="text-brand-orange">*</span></label>
                                <input type="email" id="email" name="email" placeholder="contact@entreprise.com" required>
                            </div>
                            <div class="form-group">
                                <label for="telephone">Téléphone <span class="text-brand-orange">*</span></label>
                                <input type="tel" id="telephone" name="telephone" placeholder="+33 6 XX XX XX XX" required>
                            </div>
                            <div class="form-group">
                                <label>Type de partenariat souhaité <span class="text-brand-orange">*</span></label>
                                <div class="checkbox-grid" style="display: grid; grid-template-columns: 1fr; gap: 0.75rem; margin-top: 0.5rem;">
                                    <label class="custom-checkbox">
                                        <input type="checkbox" name="type_partenariat" value="Formation">
                                        <span class="checkmark"></span>
                                        <span class="checkbox-text">Formation</span>
                                    </label>
                                    <label class="custom-checkbox">
                                        <input type="checkbox" name="type_partenariat" value="Examen / certifications">
                                        <span class="checkmark"></span>
                                        <span class="checkbox-text">Examen / certifications</span>
                                    </label>
                                    <label class="custom-checkbox">
                                        <input type="checkbox" name="type_partenariat" value="Alternance">
                                        <span class="checkmark"></span>
                                        <span class="checkbox-text">Alternance</span>
                                    </label>
                                    <label class="custom-checkbox">
                                        <input type="checkbox" name="type_partenariat" value="Orientation de publics">
                                        <span class="checkmark"></span>
                                        <span class="checkbox-text">Orientation de publics</span>
                                    </label>
                                    <label class="custom-checkbox">
                                        <input type="checkbox" name="type_partenariat" value="Événement / intervention">
                                        <span class="checkmark"></span>
                                        <span class="checkbox-text">Événement / intervention</span>
                                    </label>
                                    <label class="custom-checkbox">
                                        <input type="checkbox" name="type_partenariat" value="Autre">
                                        <span class="checkmark"></span>
                                        <span class="checkbox-text">Autre</span>
                                    </label>
                                </div>
                            </div>
                            <div class="form-actions">
                                <button type="button" class="btn btn-outline-dark btn-prev">Précédent</button>
                                <button type="button" class="btn btn-brand-orange-full btn-next">Suivant</button>
                            </div>
                        </div>
                        <div class="form-step" data-step="3">
                            <div class="form-group">
                                <label for="demande">Votre demande (Décrivez brièvement l’objet du partenariat souhaité) <span class="text-brand-orange">*</span></label>
                                <textarea id="demande" name="demande" placeholder="Décrivez votre projet de partenariat..." rows="3" required></textarea>
                            </div>
                            <div class="form-group">
                                <label for="disponibilites">Disponibilités pour un échange <span class="text-brand-orange">*</span></label>
                                <input type="text" id="disponibilites" name="disponibilites" placeholder="Ex: Lundi après-midi, Mardi matin..." required>
                            </div>
                            <div class="form-group checkbox-group">
                                <label class="custom-checkbox">
                                    <input type="checkbox" id="rgpd" name="rgpd" required>
                                    <span class="checkmark"></span>
                                    <span class="checkbox-text">J'accepte la collecte de mes données par Campus Superia. <a href="#">[Politique de confidentialité]</a> <span class="text-brand-orange">*</span></span>
                                </label>
                            </div>
                            <div class="form-actions">
                                <button type="button" class="btn btn-outline-dark btn-prev">Précédent</button>
                                <button type="submit" class="btn btn-brand-orange-full">Envoyer ma demande</button>
                            </div>
                        </div>
                    </form>"""
        form_start = content.find('<form action="#" class="campus-form-card" id="multi-step-form">')
        if form_start != -1:
            form_end = content.find('</form>', form_start)
            if form_end != -1:
                content = content[:form_start] + partenariats_form + content[form_end + len('</form>'):]

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"\u2713 {filename}")

base_bc = [('Accueil','index.html'), ('Admissions','admissions.html')]

# ── conditions ──────────────────────────────────────────────────────────────
make('admissions-conditions.html',
    "Conditions d'admission",
    "D\u00e9couvrez les pr\u00e9requis et profils accept\u00e9s pour rejoindre les programmes de Campus Superia.",
    "Conditions<br>d'admission",
    "Chaque profil est le bienvenu. D\u00e9couvrez les pr\u00e9requis sp\u00e9cifiques \u00e0 chaque programme.",
    base_bc + [("Conditions d'admission", '')],
    './assets/scroll-actual-2.jpg',
    """
    <section class="requirements-section">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up">
                <span class="tag"><span class="dot"></span> Pr\u00e9requis</span>
                <h2 class="section-title">Conditions par programme</h2>
                <p class="section-subtitle" style="margin:.75rem auto 0;">Que vous soyez d\u00e9butant ou apprenant avanc\u00e9, il existe un programme adapt\u00e9 \u00e0 votre profil.</p>
            </div>
            <div class="requirements-grid">
                <div class="req-card fade-up" style="--delay:0.1s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg></div><h3>Programmes FLE (A2 \u00e0 C1)</h3></div>
                    <ul class="req-list"><li>Avoir au moins 16 ans \u00e0 l'inscription</li><li>Pi\u00e8ce d'identit\u00e9 valide</li><li>Aucun niveau minimum \u2014 positionnement inclus</li><li>Motivation et disponibilit\u00e9 pour les cours</li><li>Acc\u00e8s \u00e0 un ordinateur/tablette pour les cours en ligne</li></ul>
                </div>
                <div class="req-card fade-up" style="--delay:0.2s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg></div><h3>Programme BTS (Bac+2)</h3></div>
                    <ul class="req-list"><li>Titre du baccalaur\u00e9at ou \u00e9quivalent</li><li>Niveau minimum B1 en fran\u00e7ais</li><li>Lettre de motivation</li><li>Disponibilit\u00e9 pour les cours en alternance (3j/sem)</li><li>Titre de s\u00e9jour valide ou visa \u00e9tudiant</li></ul>
                </div>
                <div class="req-card fade-up" style="--delay:0.3s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg></div><h3>\u00c9tudiants internationaux</h3></div>
                    <ul class="req-list"><li>Visa \u00e9tudiant ou titre de s\u00e9jour valide (pr\u00e9sentiel)</li><li>Traduction asserment\u00e9e si n\u00e9cessaire</li><li>Niveau A2 minimum recommand\u00e9</li><li>Justificatif de ressources ou garant financier</li><li>Accompagnement visa sur demande</li></ul>
                </div>
                <div class="req-card fade-up" style="--delay:0.4s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg></div><h3>Cours en ligne (E-Learning)</h3></div>
                    <ul class="req-list"><li>Connexion internet stable (5 Mbps minimum)</li><li>Ordinateur, tablette ou smartphone r\u00e9cent</li><li>Microphone et cam\u00e9ra pour les sessions en direct</li><li>Adresse email active</li><li>Accessible depuis le monde entier</li></ul>
                </div>
            </div>
        </div>
    </section>
    <section class="admission-steps-section">
        <div class="container">
            <div class="section-header text-center fade-up"><span class="tag"><span class="dot"></span> \u00c9valuation</span><h2 class="section-title">Comment nous \u00e9valuons votre candidature</h2></div>
            <div class="admission-steps-grid">
                <div class="step-card fade-up" style="--delay:0.1s"><div class="step-num">1</div><h3>Test de positionnement</h3><p>Un test adaptatif de 30 minutes couvrant compr\u00e9hension \u00e9crite, grammaire et expression.</p></div>
                <div class="step-card fade-up" style="--delay:0.2s"><div class="step-num">2</div><h3>Analyse du dossier</h3><p>R\u00e9vision de vos dipl\u00f4mes, de votre parcours et de vos objectifs d\u00e9clar\u00e9s.</p></div>
                <div class="step-card fade-up" style="--delay:0.3s"><div class="step-num">3</div><h3>Entretien de validation</h3><p>Un appel de 20 minutes pour confirmer votre niveau \u00e0 l'oral et finaliser le programme.</p></div>
                <div class="step-card fade-up" style="--delay:0.4s"><div class="step-num">4</div><h3>D\u00e9cision et int\u00e9gration</h3><p>Lettre d'admission personnalis\u00e9e avec programme, calendrier et informations pratiques.</p></div>
            </div>
        </div>
    </section>
    <section class="faq-section section-padding"><div class="container"><div class="section-header text-center mb-5 fade-up"><h2 class="section-title">Questions sur les conditions</h2></div><div class="faq-accordion"><div class="faq-item"><button class="faq-question">Puis-je candidater sans dipl\u00f4me de baccalaur\u00e9at ?<span class="faq-icon"></span></button><div class="faq-answer"><div class="faq-answer-content">Pour les programmes FLE, aucun niveau de dipl\u00f4me n'est requis. Le baccalaur\u00e9at est requis uniquement pour le BTS.</div></div></div><div class="faq-item"><button class="faq-question">Y a-t-il un \u00e2ge minimum ?<span class="faq-icon"></span></button><div class="faq-answer"><div class="faq-answer-content">L'\u00e2ge minimum est de 16 ans. Pour les mineurs, un accord parental sign\u00e9 est requis.</div></div></div></div></div></section>
""")

# ── calendrier ──────────────────────────────────────────────────────────────
make('admissions-calendrier.html',
    "Calendrier des candidatures",
    "Consultez les dates cl\u00e9s des sessions d'admission et de rentr\u00e9e \u00e0 Campus Superia.",
    "Calendrier des<br>candidatures",
    "Ne manquez aucune date limite. Consultez toutes les sessions d'admission et planifiez votre int\u00e9gration.",
    base_bc + [("Calendrier", '')],
    './assets/scroll-actual-1.jpg',
    """
    <section class="timeline-events-section">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up">
                <span class="tag"><span class="dot"></span> Sessions 2025\u20132026</span>
                <h2 class="section-title">Dates cl\u00e9s des candidatures</h2>
                <p class="section-subtitle" style="margin:.75rem auto 0;">Trois sessions d'entr\u00e9e par an pour int\u00e9grer le programme au meilleur moment.</p>
            </div>
            <div class="timeline-events">
                <div class="timeline-event fade-up"><div class="event-date">15 Juin<br>2025</div><div class="event-info"><h3>Ouverture des candidatures \u2014 Session Septembre 2025</h3><p>Acc\u00e8s aux programmes FLE (A2\u2013C1) et BTS en alternance.</p><span class="event-badge">Session principale</span></div></div>
                <div class="timeline-event fade-up"><div class="event-date">31 Ao\u00fbt<br>2025</div><div class="event-info"><h3>Date limite \u2014 Candidatures Septembre 2025</h3><p>Dernier d\u00e9lai pour soumettre un dossier complet.</p><span class="event-badge">Date limite</span></div></div>
                <div class="timeline-event fade-up"><div class="event-date">8 Sep.<br>2025</div><div class="event-info"><h3>Rentr\u00e9e de Septembre 2025</h3><p>D\u00e9but des cours pour tous les programmes FLE et BTS.</p><span class="event-badge">Rentrée officielle</span></div></div>
                <div class="timeline-event fade-up"><div class="event-date">1er Nov.<br>2025</div><div class="event-info"><h3>Ouverture des candidatures \u2014 Session Janvier 2026</h3><p>Session id\u00e9ale pour les candidats n'ayant pas pu postuler en septembre.</p><span class="event-badge">Nouvelle session</span></div></div>
                <div class="timeline-event fade-up"><div class="event-date">20 D\u00e9c.<br>2025</div><div class="event-info"><h3>Date limite \u2014 Candidatures Janvier 2026</h3><p>Dernier d\u00e9lai pour la rentr\u00e9e de janvier.</p><span class="event-badge">Date limite</span></div></div>
                <div class="timeline-event fade-up"><div class="event-date">12 Jan.<br>2026</div><div class="event-info"><h3>Rentr\u00e9e de Janvier 2026</h3><p>D\u00e9but des cours pour les programmes FLE (session janvier).</p><span class="event-badge">Rentrée</span></div></div>
                <div class="timeline-event fade-up"><div class="event-date">21 F\u00e9v.<br>2026</div><div class="event-info"><h3>Journ\u00e9e Portes Ouvertes \u2014 Campus Neuilly</h3><p>Venue pour rencontrer l'\u00e9quipe et d\u00e9couvrir les programmes de la session d'avril.</p><span class="event-badge">Portes ouvertes</span></div></div>
                <div class="timeline-event fade-up"><div class="event-date">28 Mars<br>2026</div><div class="event-info"><h3>Date limite \u2014 Candidatures Avril 2026</h3><p>Dernier d\u00e9lai de d\u00e9p\u00f4t pour la session d'avril 2026.</p><span class="event-badge">Date limite</span></div></div>
            </div>
        </div>
    </section>
    <section class="admission-steps-section"><div class="container"><div class="section-header text-center fade-up"><span class="tag"><span class="dot"></span> Conseils</span><h2 class="section-title">Pour candidater dans les meilleures conditions</h2></div><div class="admission-steps-grid"><div class="step-card fade-up" style="--delay:0.1s"><div class="step-num">\u2713</div><h3>Anticipez votre d\u00e9p\u00f4t</h3><p>Soumettez votre dossier au moins 3 semaines avant la date limite pour compl\u00e9ter les documents manquants.</p></div><div class="step-card fade-up" style="--delay:0.2s"><div class="step-num">\u2713</div><h3>Passez le test en avance</h3><p>Le test de positionnement peut \u00eatre pass\u00e9 d\u00e8s l'ouverture des candidatures.</p></div><div class="step-card fade-up" style="--delay:0.3s"><div class="step-num">\u2713</div><h3>Pr\u00e9parez vos documents</h3><p>Scannez \u00e0 l'avance pi\u00e8ce d'identit\u00e9, dipl\u00f4me et attestations de niveau.</p></div><div class="step-card fade-up" style="--delay:0.4s"><div class="step-num">\u2713</div><h3>Contactez-nous en cas de doute</h3><p>Notre \u00e9quipe r\u00e9pond \u00e0 vos questions avant que vous soumettiez votre dossier.</p></div></div></div></section>
""")

# ── frais ────────────────────────────────────────────────────────────────────
make('admissions-frais.html',
    "Frais de formation",
    "Consultez les tarifs d\u00e9taill\u00e9s des formations \u00e0 Campus Superia : FLE, BTS, cours intensifs et e-learning.",
    "Frais de<br>formation",
    "Une tarification transparente, sans frais cach\u00e9s. D\u00e9couvrez le co\u00fbt de chaque programme.",
    base_bc + [("Frais de formation", '')],
    './assets/form-bg.jpg',
    """
    <section class="fees-section">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up"><span class="tag"><span class="dot"></span> Tarification</span><h2 class="section-title">Nos tarifs par programme</h2><p class="section-subtitle" style="margin:.75rem auto 0;">Tous les frais indiqu\u00e9s sont inclus dans le tarif \u2014 aucun suppl\u00e9ment inattendu.</p></div>
            <div class="fees-table-wrap">
                <table class="fees-table">
                    <thead><tr><th>Programme</th><th>Dur\u00e9e</th><th>Format</th><th>Tarif</th><th>Inclus</th></tr></thead>
                    <tbody>
                        <tr><td><strong>Fran\u00e7ais G\u00e9n\u00e9ral A2\u2013B1</strong></td><td>3 mois</td><td>Pr\u00e9sentiel / En ligne</td><td><strong>890 \u20ac</strong></td><td>Cours, supports, test final</td></tr>
                        <tr><td><strong>Fran\u00e7ais Avanc\u00e9 B2\u2013C1</strong></td><td>3 mois</td><td>Pr\u00e9sentiel / En ligne</td><td><strong>990 \u20ac</strong></td><td>Cours, supports, test final, entretien bilan</td></tr>
                        <tr><td><strong>Fran\u00e7ais Professionnel &amp; Affaires</strong></td><td>2 mois</td><td>En ligne</td><td><strong>750 \u20ac</strong></td><td>Cours, \u00e9tudes de cas, certification partielle</td></tr>
                        <tr><td><strong>Pr\u00e9paration TEF / DELF</strong></td><td>6 semaines</td><td>Pr\u00e9sentiel / En ligne</td><td><strong>590 \u20ac</strong></td><td>Cours intensifs, annales, simulation d'examen</td></tr>
                        <tr><td><strong>\u00c9loquence &amp; Leadership</strong></td><td>6 semaines</td><td>En ligne</td><td><strong>650 \u20ac</strong></td><td>Ateliers, coaching individuel, enregistrements</td></tr>
                        <tr><td><strong>BTS \u2014 Alternance (Bac+2)</strong></td><td>2 ans</td><td>Pr\u00e9sentiel</td><td><strong>Sur devis</strong></td><td>Cours, suivi individuel, aide recherche entreprise</td></tr>
                        <tr><td><strong>Cours intensif (4 semaines)</strong></td><td>4 semaines</td><td>Pr\u00e9sentiel / En ligne</td><td><strong>480 \u20ac</strong></td><td>20h/semaine, supports num\u00e9riques inclus</td></tr>
                    </tbody>
                </table>
            </div>
        </div>
    </section>
    <section class="features-section" style="padding-bottom:6rem;"><div class="section-header fade-up"><span class="tag"><span class="dot"></span> Inclus dans le tarif</span><h2 class="section-title">Ce qui est inclus<br>dans chaque formation</h2></div><div class="features-grid"><div class="feature-card fade-up" style="--delay:.1s"><div class="icon-placeholder"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg></div><h3>Supports<br>p\u00e9dagogiques</h3><p>Acc\u00e8s \u00e0 tous les supports de cours num\u00e9riques inclus, sans surco\u00fbt.</p></div><div class="feature-card fade-up" style="--delay:.2s"><div class="icon-placeholder"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div><h3>Suivi<br>individuel</h3><p>Bilan de mi-parcours avec votre enseignant pour ajuster le rythme.</p></div><div class="feature-card fade-up" style="--delay:.3s"><div class="icon-placeholder"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 11 12 14 22 4"/></svg></div><h3>Acc\u00e8s \u00e0 la<br>plateforme</h3><p>Plateforme e-learning disponible 24h/24 pour r\u00e9viser et s'exercer.</p></div><div class="feature-card fade-up" style="--delay:.4s"><div class="icon-placeholder"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg></div><h3>Test de<br>positionnement</h3><p>Test initial et test final inclus pour mesurer votre progression.</p></div><div class="feature-card fade-up" style="--delay:.5s"><div class="icon-placeholder"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2"/></svg></div><h3>Cours<br>en direct</h3><p>Sessions en direct avec un enseignant, pr\u00e9sentiel ou visio \u2014 incluses.</p></div><div class="feature-card fade-up" style="--delay:.6s"><div class="icon-placeholder"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg></div><h3>Attestation<br>de formation</h3><p>Attestation officielle remise \u00e0 chaque apprenant ayant compl\u00e9t\u00e9 son programme.</p></div></div></section>
    <section class="testimonial-banner split-50"><div class="testimonial-text"><p>"\u00ab Les tarifs sont honn\u00eates et sans surprise. Tout \u00e9tait inclus comme annonc\u00e9. \u00bb"</p><span class="author">Lina D. \u2014 \u00c9tudiante en Pr\u00e9paration TEF</span></div><div class="banner-cta split-50"><a href="admissions-bourses.html" class="cta-block cta-orange">Voir les bourses</a><a href="admissions-comment-candidater.html" class="cta-block cta-beige">Candidater</a></div></section>
""")

# ── bourses ──────────────────────────────────────────────────────────────────
make('admissions-bourses.html',
    "Bourses & aides financi\u00e8res",
    "D\u00e9couvrez les bourses et solutions de financement disponibles pour financer votre formation \u00e0 Campus Superia.",
    "Bourses &<br>aides financi\u00e8res",
    "Campus Superia s'engage \u00e0 rendre la formation accessible \u00e0 tous. D\u00e9couvrez nos dispositifs d'aide financière.",
    base_bc + [("Bourses &amp; aides", '')],
    './assets/scroll-actual-3.jpg',
    """
    <section class="scholarships-section">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up"><span class="tag"><span class="dot"></span> Financement</span><h2 class="section-title">Nos dispositifs d'aide financi\u00e8re</h2><p class="section-subtitle" style="margin:.75rem auto 0;">Trois types de soutien pour rendre votre formation accessible, quel que soit votre budget.</p></div>
            <div class="scholarship-cards-grid">
                <div class="scholarship-card fade-up" style="--delay:0.1s"><div class="sc-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg></div><span class="scholarship-badge">M\u00e9rite</span><h3>Bourse d'excellence</h3><p>Accord\u00e9e aux candidats ayant d\u00e9montr\u00e9 un niveau exceptionnel au test de positionnement. R\u00e9duction de 20\u00e0 30% sur les frais.</p></div>
                <div class="scholarship-card fade-up" style="--delay:0.2s"><div class="sc-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div><span class="scholarship-badge">Social</span><h3>Bourse sur crit\u00e8res sociaux</h3><p>Aide financi\u00e8re pour les candidats \u00e0 ressources limit\u00e9es. Sur dossier avec justificatifs de revenus.</p></div>
                <div class="scholarship-card fade-up" style="--delay:0.3s"><div class="sc-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg></div><span class="scholarship-badge">International</span><h3>Aide internationale</h3><p>Dispositif sp\u00e9cifique pour les candidats internationaux : r\u00e9duction sur les frais et accompagnement administratif.</p></div>
            </div>
        </div>
    </section>
    <section class="admission-steps-section"><div class="container"><div class="section-header text-center fade-up"><span class="tag"><span class="dot"></span> Comment postuler</span><h2 class="section-title">Comment obtenir une bourse</h2></div><div class="admission-steps-grid"><div class="step-card fade-up" style="--delay:0.1s"><div class="step-num">1</div><h3>Candidatez \u00e0 la formation</h3><p>Soumettez d'abord votre candidature au programme souhait\u00e9 et passez le test de positionnement.</p></div><div class="step-card fade-up" style="--delay:0.2s"><div class="step-num">2</div><h3>Demandez une aide</h3><p>Lors de votre entretien, signalez votre demande d'aide financi\u00e8re et le type de bourse vis\u00e9.</p></div><div class="step-card fade-up" style="--delay:0.3s"><div class="step-num">3</div><h3>Soumettez le dossier bourse</h3><p>Fournissez les justificatifs n\u00e9cessaires dans les 15 jours suivant votre admission.</p></div><div class="step-card fade-up" style="--delay:0.4s"><div class="step-num">4</div><h3>D\u00e9cision sous 7 jours</h3><p>Le comit\u00e9 p\u00e9dagogique \u00e9value votre dossier et vous notifie du montant accord\u00e9.</p></div></div></div></section>
    <section class="requirements-section"><div class="container"><div class="section-header text-center mb-5 fade-up"><h2 class="section-title">Options de paiement flexibles</h2></div><div class="requirements-grid"><div class="req-card fade-up"><div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg></div><h3>Paiement en plusieurs fois</h3></div><ul class="req-list"><li>R\u00e8glement en 2, 3 ou 6 mensualit\u00e9s sans frais suppl\u00e9mentaires</li><li>Disponible pour les formations sup\u00e9rieures \u00e0 6 semaines</li><li>Pr\u00e9l\u00e8vement automatique s\u00e9curis\u00e9</li></ul></div><div class="req-card fade-up"><div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg></div><h3>Prise en charge CPF &amp; OPCO</h3></div><ul class="req-list"><li>Certains programmes \u00e9ligibles au Compte Personnel de Formation</li><li>Prise en charge possible par votre OPCO</li><li>Notre \u00e9quipe vous accompagne dans les d\u00e9marches</li></ul></div></div></div></section>
""")

# ── international ─────────────────────────────────────────────────────────────
make('admissions-international.html',
    "\u00c9tudiants internationaux",
    "Informations sp\u00e9cifiques pour les candidats \u00e9trangers souhaitant rejoindre Campus Superia.",
    "\u00c9tudiants<br>internationaux",
    "Campus Superia accueille des apprenants du monde entier. Nous vous accompagnons dans chaque \u00e9tape administrative.",
    base_bc + [("\u00c9tudiants internationaux", '')],
    './assets/scroll-actual-3.jpg',
    """
    <section class="international-section">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up"><span class="tag"><span class="dot"></span> Accueil international</span><h2 class="section-title">Votre accompagnement pas \u00e0 pas</h2><p class="section-subtitle" style="margin:.75rem auto 0;">De la candidature \u00e0 votre premi\u00e8re journ\u00e9e de cours, nous vous guidons \u00e0 chaque \u00e9tape.</p></div>
            <div class="international-grid">
                <div class="international-card fade-up" style="--delay:0.1s"><div class="ic-icon"><svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg></div><h3>Lettre d'admission pour visa</h3><p>Nous \u00e9mettons une lettre d'admission officielle d\u00e8s validation de votre candidature, utilisable pour votre demande de visa \u00e9tudiant.</p></div>
                <div class="international-card fade-up" style="--delay:0.2s"><div class="ic-icon"><svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg></div><h3>Aide aux d\u00e9marches administratives</h3><p>Notre \u00e9quipe vous guide pour le dossier de demande de visa long s\u00e9jour : liste des documents, d\u00e9lais et organismes.</p></div>
                <div class="international-card fade-up" style="--delay:0.3s"><div class="ic-icon"><svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg></div><h3>Conseils logement</h3><p>Liste de ressources fiables pour trouver un logement \u00e0 Paris et Neuilly-sur-Seine : r\u00e9sidences, agences, plateformes.</p></div>
                <div class="international-card fade-up" style="--delay:0.4s"><div class="ic-icon"><svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg></div><h3>Cours en ligne disponibles</h3><p>Si votre visa prend du temps, d\u00e9marrez votre formation en ligne depuis votre pays d'origine.</p></div>
                <div class="international-card fade-up" style="--delay:0.5s"><div class="ic-icon"><svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div><h3>Communaut\u00e9 multiculturelle</h3><p>Int\u00e9grez une communaut\u00e9 d'apprenants de plus de 12 nationalit\u00e9s.</p></div>
                <div class="international-card fade-up" style="--delay:0.6s"><div class="ic-icon"><svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg></div><h3>Bourse internationale</h3><p>Dispositif d'aide financi\u00e8re sp\u00e9cifique pour les \u00e9tudiants internationaux. Renseignez-vous lors de votre entretien.</p></div>
            </div>
        </div>
    </section>
    <section class="requirements-section"><div class="container"><div class="section-header text-center mb-5 fade-up"><h2 class="section-title">Documents sp\u00e9cifiques aux candidats \u00e9trangers</h2></div><div class="requirements-grid"><div class="req-card fade-up"><div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"/></svg></div><h3>Pour tous les candidats non-UE</h3></div><ul class="req-list"><li>Passeport valide (minimum 6 mois apr\u00e8s la date de rentr\u00e9e)</li><li>Visa \u00e9tudiant ou titre de s\u00e9jour valide</li><li>Justificatif de ressources (3 derniers mois ou garant)</li><li>Traduction asserment\u00e9e des dipl\u00f4mes si demand\u00e9e</li><li>Assurance sant\u00e9 internationale ou S\u00e9curit\u00e9 Sociale \u00e9tudiante</li></ul></div><div class="req-card fade-up"><div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/></svg></div><h3>Pour les ressortissants UE/EEE</h3></div><ul class="req-list"><li>Carte nationale d'identit\u00e9 ou passeport valide</li><li>Aucun visa requis pour r\u00e9sider et \u00e9tudier en France</li><li>Enregistrement en mairie recommand\u00e9</li><li>Carte europ\u00e9enne d'assurance maladie conseill\u00e9e</li><li>M\u00eames conditions d'admission que les candidats fran\u00e7ais</li></ul></div></div></div></section>
    <section class="stats-banner"><div class="container"><div class="stats-banner-grid"><div class="stat-item fade-up"><span class="stat-number">12+</span><span class="stat-label">Nationalit\u00e9s repr\u00e9sent\u00e9es</span></div><div class="stat-item fade-up" style="--delay:.1s"><span class="stat-number">100%</span><span class="stat-label">Candidatures trait\u00e9es en ligne</span></div><div class="stat-item fade-up" style="--delay:.2s"><span class="stat-number">5 jours</span><span class="stat-label">D\u00e9lai lettre d'admission</span></div><div class="stat-item fade-up" style="--delay:.3s"><span class="stat-number">2 langues</span><span class="stat-label">Support fran\u00e7ais et anglais</span></div></div></div></section>
""")

# ── transfert ─────────────────────────────────────────────────────────────────
make('admissions-transfert.html',
    "Admission par transfert",
    "Rejoignez Campus Superia en cours de parcours gr\u00e2ce \u00e0 notre proc\u00e9dure de transfert simplifi\u00e9e.",
    "Admission<br>par transfert",
    "D\u00e9j\u00e0 inscrit ailleurs ou ayant commenc\u00e9 une formation ? Rejoignez Campus Superia via notre proc\u00e9dure de transfert.",
    base_bc + [("Transfert", '')],
    './assets/scroll-actual-2.jpg',
    """
    <section class="section-padding" style="width:100%; background:var(--clr-white);">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up"><span class="tag"><span class="dot"></span> Transfert</span><h2 class="section-title">Rejoindre Campus Superia<br>en cours de parcours</h2></div>
            <div class="transfer-content-grid">
                <div class="transfer-text">
                    <h3>Pourquoi choisir Campus Superia par transfert ?</h3>
                    <p>Vous souhaitez changer d'\u00e9tablissement, b\u00e9n\u00e9ficier d'un enseignement plus personnalis\u00e9 ou simplement changer de cadre ? Notre proc\u00e9dure est con\u00e7ue pour minimiser les perturbations dans votre parcours.</p>
                    <p>Nous \u00e9valuons votre niveau actuel, reconnaissons vos acquis et vous int\u00e9grons dans la classe la plus adapt\u00e9e, sans perte de temps.</p>
                    <h3 style="margin-top:2rem;">Qui peut b\u00e9n\u00e9ficier du transfert ?</h3>
                    <p>Tout apprenant ayant suivi au moins 4 semaines de cours de fran\u00e7ais peut pr\u00e9tendre \u00e0 une admission par transfert. Une \u00e9valuation individuelle est r\u00e9alis\u00e9e.</p>
                </div>
                <div>
                    <ul class="transfer-checklist">
                        <li><span class="check-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></span>Vous avez suivi des cours ailleurs et souhaitez changer d'environnement</li>
                        <li><span class="check-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></span>Vous avez arr\u00eat\u00e9 une formation et souhaitez reprendre l\u00e0 o\u00f9 vous en \u00e9tiez</li>
                        <li><span class="check-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></span>Vous d\u00e9m\u00e9nagez en France et avez un niveau att\u00e9st\u00e9 dans votre pays</li>
                        <li><span class="check-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></span>Vous passez du e-learning au pr\u00e9sentiel ou inversement</li>
                        <li><span class="check-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></span>Vous souhaitez ajouter une sp\u00e9cialisation \u00e0 votre parcours actuel</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>
    <section class="admission-steps-section"><div class="container"><div class="section-header text-center fade-up"><h2 class="section-title">Proc\u00e9dure de transfert simplifi\u00e9e</h2></div><div class="admission-steps-grid"><div class="step-card fade-up" style="--delay:0.1s"><div class="step-num">1</div><h3>Demande de transfert</h3><p>Contactez notre \u00e9quipe en indiquant votre niveau actuel et votre \u00e9tablissement pr\u00e9c\u00e9dent.</p></div><div class="step-card fade-up" style="--delay:0.2s"><div class="step-num">2</div><h3>\u00c9valuation des acquis</h3><p>Passez notre test de positionnement. Fournissez tout relevé de formation ou attestation de niveau.</p></div><div class="step-card fade-up" style="--delay:0.3s"><div class="step-num">3</div><h3>Proposition d'int\u00e9gration</h3><p>Nous vous proposons une classe et un calendrier adapt\u00e9s \u00e0 votre niveau valid\u00e9.</p></div><div class="step-card fade-up" style="--delay:0.4s"><div class="step-num">4</div><h3>Finalisation et d\u00e9marrage</h3><p>Signez votre contrat et rejoignez votre groupe. Un tuteur vous accueille lors des premi\u00e8res s\u00e9ances.</p></div></div></div></section>
""")

# ── portes ouvertes ──────────────────────────────────────────────────────────
make('admissions-portes-ouvertes.html',
    "Portes ouvertes",
    "Participez aux journ\u00e9es portes ouvertes de Campus Superia : visitez nos campus, rencontrez les \u00e9quipes.",
    "Portes<br>ouvertes",
    "Rencontrez nos enseignants, visitez nos espaces et d\u00e9couvrez nos programmes de visu. Gratuit et ouvert \u00e0 tous.",
    base_bc + [("Portes ouvertes", '')],
    './assets/scroll-actual-1.jpg',
    """
    <section class="events-section">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up"><span class="tag"><span class="dot"></span> Agenda 2025\u20132026</span><h2 class="section-title">Prochaines journ\u00e9es portes ouvertes</h2></div>
            <div class="events-cards-grid">
                <div class="event-card fade-up" style="--delay:0.1s">
                    <div class="event-card-header"><div class="event-date-block"><span class="event-day">14</span><span class="event-month">Juin</span></div><span class="event-card-title">Journ\u00e9e Portes Ouvertes \u2014 Campus Neuilly</span></div>
                    <div class="event-card-body"><p>D\u00e9couvrez nos salles de cours, rencontrez les enseignants et assistez \u00e0 une mini-session de d\u00e9monstration. Programme complet sur place.</p><div class="event-meta"><span class="event-tag">Neuilly-sur-Seine</span><span class="event-tag">10h\u201317h</span><span class="event-tag">Gratuit</span></div></div>
                    <div class="event-card-footer"><a href="#contact">Je m'inscris \u2192</a></div>
                </div>
                <div class="event-card fade-up" style="--delay:0.2s">
                    <div class="event-card-header"><div class="event-date-block"><span class="event-day">18</span><span class="event-month">Oct.</span></div><span class="event-card-title">Portes Ouvertes Virtuelles \u2014 E-Learning</span></div>
                    <div class="event-card-body"><p>Pr\u00e9sentation des outils e-learning, Q&amp;R en direct avec les enseignants et d\u00e9monstration de la plateforme.</p><div class="event-meta"><span class="event-tag">En ligne</span><span class="event-tag">14h\u201316h</span><span class="event-tag">Gratuit</span></div></div>
                    <div class="event-card-footer"><a href="#contact">Je m'inscris \u2192</a></div>
                </div>
                <div class="event-card fade-up" style="--delay:0.3s">
                    <div class="event-card-header"><div class="event-date-block"><span class="event-day">21</span><span class="event-month">F\u00e9v.</span></div><span class="event-card-title">Journ\u00e9e Portes Ouvertes \u2014 Campus Neuilly</span></div>
                    <div class="event-card-body"><p>Rencontrez les \u00e9tudiants actuels et posez toutes vos questions \u00e0 notre \u00e9quipe p\u00e9dagogique.</p><div class="event-meta"><span class="event-tag">Neuilly-sur-Seine</span><span class="event-tag">10h\u201316h</span><span class="event-tag">Gratuit</span></div></div>
                    <div class="event-card-footer"><a href="#contact">Je m'inscris \u2192</a></div>
                </div>
            </div>
        </div>
    </section>
    <section class="features-section" style="padding-bottom:6rem;"><div class="section-header fade-up"><span class="tag"><span class="dot"></span> Au programme</span><h2 class="section-title">Ce qui vous attend<br>lors d'une porte ouverte</h2></div><div class="features-grid"><div class="feature-card fade-up" style="--delay:.1s"><div class="icon-placeholder"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg></div><h3>Visite des locaux</h3><p>Tour guid\u00e9 de nos salles, espaces collaboratifs et zones de travail.</p></div><div class="feature-card fade-up" style="--delay:.2s"><div class="icon-placeholder"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div><h3>Rencontre avec<br>les enseignants</h3><p>\u00c9changez directement sur les m\u00e9thodes et programmes.</p></div><div class="feature-card fade-up" style="--delay:.3s"><div class="icon-placeholder"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2"/></svg></div><h3>D\u00e9mo de cours<br>en direct</h3><p>Mini-session gratuite pour d\u00e9couvrir notre p\u00e9dagogie en action.</p></div><div class="feature-card fade-up" style="--delay:.4s"><div class="icon-placeholder"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg></div><h3>Test de positionnement<br>gratuit</h3><p>Passez votre test de niveau sur place et recevez votre r\u00e9sultat imm\u00e9diatement.</p></div><div class="feature-card fade-up" style="--delay:.5s"><div class="icon-placeholder"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/></svg></div><h3>Brochures et<br>informations</h3><p>Repartez avec tous les d\u00e9tails sur programmes, tarifs et dates de rentr\u00e9e.</p></div><div class="feature-card fade-up" style="--delay:.6s"><div class="icon-placeholder"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg></div><h3>Inscription<br>prioritaire</h3><p>D\u00e9posez votre candidature sur place pour un traitement prioritaire de votre dossier.</p></div></div></section>
""")

# ── campus ────────────────────────────────────────────────────────────────────
make('admissions-campus.html',
    "Nos campus & formats de formation",
    "D\u00e9couvrez les campus et formats disponibles \u00e0 Campus Superia : pr\u00e9sentiel \u00e0 Paris Neuilly et 100% en ligne.",
    "Nos campus<br>&amp; formats",
    "Deux formats adapt\u00e9s \u00e0 votre style de vie : un campus physique \u00e0 Neuilly-sur-Seine et un programme e-learning mondial.",
    base_bc + [("Campus &amp; formats", '')],
    './assets/scroll-actual-3.jpg',
    """
    <section class="campus-cards-section">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up"><span class="tag"><span class="dot"></span> Nos lieux</span><h2 class="section-title">Choisissez votre format</h2><p class="section-subtitle" style="margin:.75rem auto 0;">Deux environnements d'apprentissage pour s'adapter \u00e0 vos contraintes personnelles et professionnelles.</p></div>
            <div class="campus-cards-grid">
                <div class="campus-card fade-up" style="--delay:0.1s">
                    <div class="campus-card-img"><img src="./assets/scroll-actual-1.jpg" alt="Campus Neuilly-sur-Seine" onerror="this.src='./assets/hero.jpeg'"></div>
                    <div class="campus-card-body">
                        <h3>Campus Neuilly-sur-Seine</h3>
                        <span class="campus-location"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>99 Avenue Achille Peretti, 92200 Neuilly-sur-Seine</span>
                        <p>Notre campus principal dans l'un des quartiers les plus dynamiques de la r\u00e9gion parisienne. Salles modernes, espace collaboratif et ambiance chaleureuse.</p>
                        <div class="campus-facilities"><span class="facility-tag">Salles modernes</span><span class="facility-tag">Wi-Fi haut d\u00e9bit</span><span class="facility-tag">Espace collaboratif</span><span class="facility-tag">Acc\u00e8s RER C</span><span class="facility-tag">Biblioth\u00e8que</span></div>
                    </div>
                </div>
                <div class="campus-card fade-up" style="--delay:0.2s">
                    <div class="campus-card-img"><img src="./assets/scroll-actual-3.jpg" alt="Formation en ligne" onerror="this.src='./assets/hero.jpeg'"></div>
                    <div class="campus-card-body">
                        <h3>Formation E-Learning</h3>
                        <span class="campus-location"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>Accessible depuis le monde entier</span>
                        <p>Plateforme e-learning moderne pour cours en direct, acc\u00e8s aux supports 24h/24 et progression \u00e0 votre rythme.</p>
                        <div class="campus-facilities"><span class="facility-tag">Cours en direct</span><span class="facility-tag">Acc\u00e8s 24h/24</span><span class="facility-tag">Plateforme d\u00e9di\u00e9e</span><span class="facility-tag">Support technique</span><span class="facility-tag">Ressources illimit\u00e9es</span></div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <section class="location-section section-padding" id="location" style="width:100%; background:var(--clr-bg-main);"><div class="container"><div class="section-header text-center mb-5 fade-up"><h2 class="section-title">Trouvez-<span>nous</span></h2><p class="section-subtitle" style="margin:.75rem auto 0;">Notre campus principal est situ\u00e9 \u00e0 Neuilly-sur-Seine, \u00e0 5 minutes du RER C.</p></div><div class="map-container"><iframe src="https://www.google.com/maps?q=99+Avenue+Achille+Peretti,+92200+Neuilly-sur-Seine&hl=fr&z=15&output=embed" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div></div></section>
""")

# ── témoignages ───────────────────────────────────────────────────────────────
make('admissions-temoignages.html',
    "T\u00e9moignages \u00e9tudiants",
    "D\u00e9couvrez les parcours et t\u00e9moignages d'\u00e9tudiants ayant int\u00e9gr\u00e9 et r\u00e9ussi leurs formations \u00e0 Campus Superia.",
    "T\u00e9moignages<br>\u00e9tudiants",
    "Ils ont choisi Campus Superia et transform\u00e9 leur rapport \u00e0 la langue fran\u00e7aise. D\u00e9couvrez leurs parcours.",
    base_bc + [("T\u00e9moignages", '')],
    './assets/scroll-actual-2.jpg',
    """
    <section class="testimonials-section">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up"><span class="tag"><span class="dot"></span> Nos apprenants t\u00e9moignent</span><h2 class="section-title">Ils ont r\u00e9ussi avec<br>Campus Superia</h2></div>
            <div class="testimonial-cards-grid">
                <div class="testimonial-card fade-up" style="--delay:0.1s"><div class="testimonial-quote">Campus Superia m'a permis d'obtenir mon attestation de naturalisation apr\u00e8s 6 mois de formation intensive. L'approche personnalis\u00e9e a tout chang\u00e9.</div><div class="testimonial-author"><div class="testimonial-avatar">A</div><div class="testimonial-author-info"><span class="author-name">Amina K.</span><span class="author-role">Programme B2 \u2192 Naturalisation</span></div></div></div>
                <div class="testimonial-card fade-up" style="--delay:0.2s"><div class="testimonial-quote">Je travaillais \u00e0 temps plein. Gr\u00e2ce au format en ligne, j'ai pu concilier emploi et formation sans compromis.</div><div class="testimonial-author"><div class="testimonial-avatar">M</div><div class="testimonial-author-info"><span class="author-name">Mehdi T.</span><span class="author-role">Fran\u00e7ais Professionnel \u2014 E-Learning</span></div></div></div>
                <div class="testimonial-card fade-up" style="--delay:0.3s"><div class="testimonial-quote">Mon test DELF \u00e9tait dans 8 semaines. Le programme m'a donn\u00e9 exactement les outils n\u00e9cessaires. J'ai obtenu B2 du premier coup.</div><div class="testimonial-author"><div class="testimonial-avatar">S</div><div class="testimonial-author-info"><span class="author-name">Sarah B.</span><span class="author-role">Pr\u00e9paration DELF B2</span></div></div></div>
                <div class="testimonial-card fade-up" style="--delay:0.4s"><div class="testimonial-quote">En tant qu'\u00e9tudiant international, Campus Superia m'a accompagn\u00e9 pour le visa, le logement et l'int\u00e9gration.</div><div class="testimonial-author"><div class="testimonial-avatar">Y</div><div class="testimonial-author-info"><span class="author-name">Youssef A.</span><span class="author-role">\u00c9tudiant marocain \u2014 BTS alternance</span></div></div></div>
                <div class="testimonial-card fade-up" style="--delay:0.5s"><div class="testimonial-quote">La bourse sur crit\u00e8res sociaux m'a permis de financer ma formation sans m'endetter. L'\u00e9quipe \u00e9tait transparente et rapide.</div><div class="testimonial-author"><div class="testimonial-avatar">F</div><div class="testimonial-author-info"><span class="author-name">Fatou M.</span><span class="author-role">Programme A2 \u2192 B2 en 12 mois</span></div></div></div>
                <div class="testimonial-card fade-up" style="--delay:0.6s"><div class="testimonial-quote">Le programme d'\u00e9loquence a compl\u00e8tement chang\u00e9 ma prise de parole en public. Extraordinaire en 6 semaines.</div><div class="testimonial-author"><div class="testimonial-avatar">P</div><div class="testimonial-author-info"><span class="author-name">Priya S.</span><span class="author-role">\u00c9loquence &amp; Leadership C1</span></div></div></div>
            </div>
        </div>
    </section>
    <section class="stats-banner"><div class="container"><div class="stats-banner-grid"><div class="stat-item fade-up"><span class="stat-number">98%</span><span class="stat-label">Taux de satisfaction</span></div><div class="stat-item fade-up" style="--delay:.1s"><span class="stat-number">1 800+</span><span class="stat-label">Dipl\u00f4m\u00e9s depuis l'ouverture</span></div><div class="stat-item fade-up" style="--delay:.2s"><span class="stat-number">87%</span><span class="stat-label">Progressent de 2 niveaux minimum</span></div><div class="stat-item fade-up" style="--delay:.3s"><span class="stat-number">92%</span><span class="stat-label">Recommandent Campus Superia</span></div></div></div></section>
""")

# ── FAQ ───────────────────────────────────────────────────────────────────────
make('admissions-faq.html',
    "FAQ Admissions",
    "Toutes les r\u00e9ponses \u00e0 vos questions sur les admissions, les programmes, les frais et la vie \u00e0 Campus Superia.",
    "FAQ<br>Admissions",
    "Trouvez ici les r\u00e9ponses aux questions les plus fr\u00e9quentes sur notre processus d'admission et nos programmes.",
    base_bc + [("FAQ", '')],
    './assets/scroll-actual-1.jpg',
    """
    <section class="faq-section section-padding" style="width:100%;"><div class="container"><div class="section-header text-center mb-5 fade-up"><span class="tag"><span class="dot"></span> Candidature</span><h2 class="section-title">Questions sur la candidature</h2></div><div class="faq-accordion"><div class="faq-item"><button class="faq-question">Y a-t-il des frais pour d\u00e9poser une candidature ?<span class="faq-icon"></span></button><div class="faq-answer"><div class="faq-answer-content">Non. La candidature est enti\u00e8rement gratuite. Aucun frais n'est demand\u00e9 avant votre admission formelle.</div></div></div><div class="faq-item"><button class="faq-question">Combien de temps pour recevoir une r\u00e9ponse ?<span class="faq-icon"></span></button><div class="faq-answer"><div class="faq-answer-content">Nous nous engageons \u00e0 r\u00e9pondre sous 72 heures ouvr\u00e9es apr\u00e8s r\u00e9ception de votre dossier complet.</div></div></div><div class="faq-item"><button class="faq-question">Que se passe-t-il si mon dossier est incomplet ?<span class="faq-icon"></span></button><div class="faq-answer"><div class="faq-answer-content">Notre \u00e9quipe vous contactera. Vous disposerez de 15 jours pour compl\u00e9ter votre dossier sans perdre votre place.</div></div></div></div></div></section>
    <section class="faq-section section-padding" style="width:100%; background:var(--clr-white);"><div class="container"><div class="section-header text-center mb-5 fade-up"><span class="tag"><span class="dot"></span> Programmes</span><h2 class="section-title">Questions sur les programmes</h2></div><div class="faq-accordion"><div class="faq-item"><button class="faq-question">Quelle est la dur\u00e9e d'une formation type ?<span class="faq-icon"></span></button><div class="faq-answer"><div class="faq-answer-content">Les programmes FLE durent g\u00e9n\u00e9ralement 3 mois. Les formats intensifs durent 4 \u00e0 6 semaines. Le BTS est une formation de 2 ans en alternance.</div></div></div><div class="faq-item"><button class="faq-question">Combien d'heures de cours par semaine ?<span class="faq-icon"></span></button><div class="faq-answer"><div class="faq-answer-content">Les programmes standards incluent 8 \u00e0 12 heures par semaine. Les formats intensifs atteignent 20 heures par semaine.</div></div></div><div class="faq-item"><button class="faq-question">Les cours sont-ils disponibles en replay ?<span class="faq-icon"></span></button><div class="faq-answer"><div class="faq-answer-content">Les cours en ligne sont enregistr\u00e9s et disponibles en replay pendant 30 jours.</div></div></div></div></div></section>
    <section class="faq-section section-padding" style="width:100%;"><div class="container"><div class="section-header text-center mb-5 fade-up"><span class="tag"><span class="dot"></span> Finances</span><h2 class="section-title">Questions sur les frais et le financement</h2></div><div class="faq-accordion"><div class="faq-item"><button class="faq-question">Peut-on payer en plusieurs fois ?<span class="faq-icon"></span></button><div class="faq-answer"><div class="faq-answer-content">Oui. Paiement en 2, 3 ou 6 mensualit\u00e9s sans frais suppl\u00e9mentaires pour les formations de plus de 6 semaines.</div></div></div><div class="faq-item"><button class="faq-question">Les formations sont-elles \u00e9ligibles au CPF ?<span class="faq-icon"></span></button><div class="faq-answer"><div class="faq-answer-content">Certains programmes sont \u00e9ligibles au CPF. Contactez-nous pour v\u00e9rifier l'\u00e9ligibilit\u00e9 de votre formation.</div></div></div><div class="faq-item"><button class="faq-question">Que couvrent les frais de formation ?<span class="faq-icon"></span></button><div class="faq-answer"><div class="faq-answer-content">Les frais incluent : cours, acc\u00e8s \u00e0 la plateforme e-learning, supports p\u00e9dagogiques num\u00e9riques, tests et attestation de fin de formation.</div></div></div></div></div></section>
    <div style="text-align:center; padding:3rem 1rem; background:var(--clr-white);"><p style="font-size:1.1rem;color:var(--clr-text-mid);margin-bottom:1.5rem;">Vous n'avez pas trouv\u00e9 votre r\u00e9ponse ?</p><a href="admissions-contact.html" class="btn btn-brand-orange" style="border-radius:4px;display:inline-flex;">Contactez notre \u00e9quipe \u2192</a></div>
""")

# ── contact ───────────────────────────────────────────────────────────────────
make('admissions-contact.html',
    "Contact Admissions",
    "Contactez l'\u00e9quipe admissions de Campus Superia. T\u00e9l\u00e9phone, email, formulaire \u2014 nous r\u00e9pondons sous 72 heures.",
    "Contactez<br>notre \u00e9quipe",
    "Une question sur votre candidature ? Notre \u00e9quipe est \u00e0 votre \u00e9coute par t\u00e9l\u00e9phone, email ou formulaire.",
    base_bc + [("Contact", '')],
    './assets/scroll-actual-2.jpg',
    """
    <section class="contact-info-section">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up"><span class="tag"><span class="dot"></span> Coordonn\u00e9es</span><h2 class="section-title">Nos coordonn\u00e9es</h2><p class="section-subtitle" style="margin:.75rem auto 0;">Plusieurs fa\u00e7ons de nous joindre selon vos pr\u00e9f\u00e9rences.</p></div>
            <div class="contact-info-grid">
                <div class="contact-info-card fade-up" style="--delay:0.1s"><div class="contact-info-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 13a19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 3.6 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg></div><h4>T\u00e9l\u00e9phone</h4><a href="tel:+33781547503">+33 781 547 503</a><p>Lun\u2013Ven : 9h\u201318h</p></div>
                <div class="contact-info-card fade-up" style="--delay:0.2s"><div class="contact-info-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg></div><h4>Email</h4><a href="mailto:contact@campussuperia.com">contact@campussuperia.com</a><br><a href="mailto:campussuperia@gmail.com">campussuperia@gmail.com</a><p>R\u00e9ponse sous 72h</p></div>
                <div class="contact-info-card fade-up" style="--delay:0.3s"><div class="contact-info-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></div><h4>Campus</h4><p>99 Avenue Achille Peretti<br>92200 Neuilly-sur-Seine</p></div>
                <div class="contact-info-card fade-up" style="--delay:0.4s"><div class="contact-info-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg></div><h4>Horaires</h4><p>Lun\u2013Ven : 9h\u201318h<br>Sam : 10h\u201313h<br>Dim : Ferm\u00e9</p></div>
            </div>
        </div>
    </section>
    <section class="location-section section-padding" id="location" style="width:100%; background:var(--clr-white);"><div class="container"><div class="section-header text-center mb-5 fade-up"><h2 class="section-title">Trouvez-<span>nous</span></h2></div><div class="map-container"><iframe src="https://www.google.com/maps?q=99+Avenue+Achille+Peretti,+92200+Neuilly-sur-Seine&hl=fr&z=15&output=embed" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div></div></section>
""")

# ── comment candidater ────────────────────────────────────────────────────────
make('admissions-comment-candidater.html',
    "Comment candidater",
    "Découvrez toutes les étapes pour déposer votre candidature à Campus Superia et intégrer nos programmes.",
    "Comment<br>candidater ?",
    "Un processus clair, étape par étape. De votre première démarche à votre première session de cours.",
    base_bc + [("Comment candidater", '')],
    './assets/scroll-actual-1.jpg',
    """
    <section class="section-padding" style="width:100%; background:var(--clr-bg-main);">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up">
                <span class="tag"><span class="dot"></span> Votre parcours</span>
                <h2 class="section-title">Votre candidature en 5 étapes</h2>
                <p class="section-subtitle" style="margin:.75rem auto 0;">Chaque étape est conçue pour être simple, rapide et entièrement réalisable depuis chez vous.</p>
            </div>
            <div class="story-timeline">
                <div class="timeline-line-bg"></div>
                <div class="timeline-line-fill" id="timeline-fill"></div>
                <div class="story-step left">
                    <div class="step-number">1</div>
                    <div class="step-content">
                        <h3>Remplissez le formulaire en ligne</h3>
                        <p>Accédez à notre formulaire de candidature sécurisé, renseignez vos informations personnelles, votre niveau actuel et votre objectif de formation. L'opération prend moins de 5 minutes.</p>
                    </div>
                </div>
                <div class="story-step right">
                    <div class="step-number">2</div>
                    <div class="step-content">
                        <h3>Joignez vos documents</h3>
                        <p>Téléchargez vos pièces justificatives : copie de pièce d'identité, dernier diplôme obtenu, et si disponible, toute attestation de langue. Tous les documents peuvent être scannés ou photographiés.</p>
                    </div>
                </div>
                <div class="story-step left">
                    <div class="step-number">3</div>
                    <div class="step-content">
                        <h3>Passez le test de positionnement</h3>
                        <p>Un lien vous sera envoyé par email pour passer notre test de positionnement en ligne. Ce test (30 minutes) nous permet de valider votre niveau et de vous orienter vers le programme le plus adapté.</p>
                    </div>
                </div>
                <div class="story-step right">
                    <div class="step-number">4</div>
                    <div class="step-content">
                        <h3>Entretien avec un conseiller</h3>
                        <p>Un conseiller pédagogique vous contacte sous 72h pour un entretien de 20 minutes. Cet échange permet de valider votre projet, répondre à vos questions et confirmer votre orientation de formation.</p>
                    </div>
                </div>
                <div class="story-step left">
                    <div class="step-number">5</div>
                    <div class="step-content">
                        <h3>Confirmation et intégration</h3>
                        <p>Vous recevez votre lettre d'admission par email. Finalisez votre inscription, réglez les modalités de paiement et préparez votre rentrée. Un kit d'intégration vous sera envoyé avant le démarrage.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <section class="requirements-section">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up">
                <span class="tag"><span class="dot"></span> Dossier complet</span>
                <h2 class="section-title">Documents requis pour candidater</h2>
            </div>
            <div class="requirements-grid">
                <div class="req-card fade-up" style="--delay:0.1s">
                    <div class="req-card-header">
                        <div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg></div>
                        <h3>Documents obligatoires</h3>
                    </div>
                    <ul class="req-list">
                        <li>Copie recto/verso de votre pièce d'identité (passeport ou carte nationale)</li>
                        <li>Dernier diplôme ou attestation de scolarité</li>
                        <li>Photo d'identité récente (format numérique accepté)</li>
                        <li>Formulaire de candidature complété</li>
                        <li>Accord parental pour les mineurs de moins de 18 ans</li>
                    </ul>
                </div>
                <div class="req-card fade-up" style="--delay:0.2s">
                    <div class="req-card-header">
                        <div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg></div>
                        <h3>Documents complémentaires (si disponibles)</h3>
                    </div>
                    <ul class="req-list">
                        <li>Attestation de niveau de langue (DELF, TEF, Alliance Française, etc.)</li>
                        <li>CV ou résumé de parcours professionnel</li>
                        <li>Lettre de motivation (recommandée pour les candidatures BTS)</li>
                        <li>Tout justificatif d'activité professionnelle actuelle</li>
                        <li>Pour les internationaux : visa en cours de validité ou titre de séjour</li>
                    </ul>
                </div>
                <div class="req-card fade-up" style="--delay:0.3s">
                    <div class="req-card-header">
                        <div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg></div>
                        <h3>Ce que nous ne demandons PAS</h3>
                    </div>
                    <ul class="req-list">
                        <li>Aucun frais de dossier</li>
                        <li>Aucun test d'entrée éliminatoire</li>
                        <li>Aucune lettre de recommandation obligatoire</li>
                        <li>Aucune condition de nationalité</li>
                        <li>Aucun niveau minimum requis (sauf pour le BTS)</li>
                    </ul>
                </div>
                <div class="req-card fade-up" style="--delay:0.4s">
                    <div class="req-card-header">
                        <div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg></div>
                        <h3>Formats acceptés</h3>
                    </div>
                    <ul class="req-list">
                        <li>PDF (recommandé), JPG, PNG pour les scans et photos</li>
                        <li>Fichiers jusqu'à 5 Mo par document</li>
                        <li>Documents en français, anglais ou arabe acceptés</li>
                        <li>Traduction assermentée requise pour certains pays (nous contacter)</li>
                        <li>Dépôt 100% en ligne, aucun envoi postal requis</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>
    <section class="testimonial-banner split-50"><div class="testimonial-text"><p>« J'ai complété ma candidature en 10 minutes depuis mon téléphone. Une semaine plus tard, j'avais ma lettre d'admission. »</p><span class="author">Mehdi T. — Étudiant en Français B1</span></div><div class="banner-cta split-50"><a href="#contact" class="cta-block cta-orange">Candidater maintenant</a><a href="admissions-conditions.html" class="cta-block cta-beige">Voir les conditions</a></div></section>
    """
)

# ── admissions BTS ───────────────────────────────────────────────────────────
make('admissions-bts.html',
    "Admission BTS",
    "Découvrez la procédure d'admission pour le programme BTS en alternance chez Campus Superia. Inscription, sélection et placement en entreprise.",
    "Admission<br>BTS (Bac+2)",
    "Intégrez une formation d'État à 100% en alternance. Financement complet et coaching de recherche d'entreprise.",
    base_bc + [("BTS", '')],
    './assets/scroll-actual-2.jpg',
    """
    <section class="requirements-section">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up">
                <span class="tag"><span class="dot"></span> Points Clés</span>
                <h2 class="section-title">Pourquoi choisir le BTS en alternance ?</h2>
                <p class="section-subtitle" style="margin:.75rem auto 0;">Une formation professionnalisante pour entrer rapidement dans la vie active avec une expérience solide.</p>
            </div>
            <div class="requirements-grid">
                <div class="req-card fade-up" style="--delay:0.1s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg></div><h3>Diplôme d'État</h3></div>
                    <ul class="req-list">
                        <li>Titre RNCP de Niveau 5</li>
                        <li>Reconnu à 100% par l'État et les recruteurs</li>
                        <li>Contrôle continu et examen final national</li>
                    </ul>
                </div>
                <div class="req-card fade-up" style="--delay:0.2s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg></div><h3>Financement 100% Pris en Charge</h3></div>
                    <ul class="req-list">
                        <li>Zéro reste à charge pour l'étudiant</li>
                        <li>Frais de formation financés par l'OPCO de l'entreprise</li>
                        <li>Perception d'un salaire mensuel (pourcentage du SMIC)</li>
                    </ul>
                </div>
                <div class="req-card fade-up" style="--delay:0.3s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div><h3>Placement Garanti</h3></div>
                    <ul class="req-list">
                        <li>Ateliers de coaching CV et préparation aux entretiens</li>
                        <li>Mise en relation directe avec notre réseau d'entreprises</li>
                        <li>Accompagnement jusqu'à la signature du contrat</li>
                    </ul>
                </div>
                <div class="req-card fade-up" style="--delay:0.4s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a10 10 0 0 0-7.38 16.75L12 22l7.38-5.25A10 10 0 0 0 12 2z"/></svg></div><h3>Rythme Flexible</h3></div>
                    <ul class="req-list">
                        <li>2 jours de cours théoriques sur le campus</li>
                        <li>3 jours de pratique professionnelle en entreprise</li>
                        <li>Une immersion parfaite pour développer vos compétences</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <section class="admission-steps-section">
        <div class="container">
            <div class="section-header text-center fade-up">
                <span class="tag"><span class="dot"></span> Procédure</span>
                <h2 class="section-title">Les 4 étapes de votre admission</h2>
            </div>
            <div class="admission-steps-grid">
                <div class="step-card fade-up" style="--delay:0.1s"><div class="step-num">1</div><h3>Candidature</h3><p>Complétez le dossier de candidature en ligne avec vos bulletins scolaires de Première/Terminale et votre CV.</p></div>
                <div class="step-card fade-up" style="--delay:0.2s"><div class="step-num">2</div><h3>Entretien</h3><p>Passez un entretien de motivation individuel de 20 minutes pour évaluer l'adéquation de votre profil avec l'alternance.</p></div>
                <div class="step-card fade-up" style="--delay:0.3s"><div class="step-num">3</div><h3>Admissibilité</h3><p>Recevez la décision du jury pédagogique sous 48 heures concernant la validation de votre dossier.</p></div>
                <div class="step-card fade-up" style="--delay:0.4s"><div class="step-num">4</div><h3>Placement</h3><p>Bénéficiez de notre coaching personnalisé pour décrocher votre contrat de professionnalisation ou d'apprentissage.</p></div>
            </div>
        </div>
    </section>

    <section class="faq-section section-padding" style="width:100%; background:var(--clr-white);">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up">
                <h2 class="section-title">Questions fréquentes sur le BTS</h2>
            </div>
            <div class="faq-accordion">
                <div class="faq-item">
                    <button class="faq-question">Qui finance ma formation en BTS ?<span class="faq-icon"></span></button>
                    <div class="faq-answer"><div class="faq-answer-content">La scolarité est intégralement prise en charge par l'organisme financeur (OPCO) de votre entreprise d'accueil. Vous n'avez aucun frais d'inscription ni de frais de scolarité à régler.</div></div>
                </div>
                <div class="faq-item">
                    <button class="faq-question">Quels sont les prérequis pour s'inscrire ?<span class="faq-icon"></span></button>
                    <div class="faq-answer"><div class="faq-answer-content">Il est nécessaire d'être titulaire du baccalauréat (général, technologique ou professionnel) ou d'un diplôme équivalent de niveau 4, et de posséder un niveau de français suffisant (B1 minimum) pour suivre les enseignements.</div></div>
                </div>
            </div>
        </div>
    </section>

    <section class="stats-banner">
        <div class="container">
            <div class="stats-banner-grid">
                <div class="stat-item fade-up"><span class="stat-number">98%</span><span class="stat-label">Satisfaction étudiant</span></div>
                <div class="stat-item fade-up" style="--delay:.1s"><span class="stat-number">100%</span><span class="stat-label">Frais financés</span></div>
                <div class="stat-item fade-up" style="--delay:.2s"><span class="stat-number">48h</span><span class="stat-label">Délai de réponse jury</span></div>
                <div class="stat-item fade-up" style="--delay:.3s"><span class="stat-number">2 ans</span><span class="stat-label">Durée d'études</span></div>
            </div>
        </div>
    </section>
    """
)

# ── admissions Bachelor ──────────────────────────────────────────────────────
make('admissions-bachelor.html',
    "Admission Bachelor",
    "Procédure d'admission pour les programmes Bachelor de Campus Superia. Cursus Bac+3 certifié par l'État avec spécialisations multiples.",
    "Admission<br>Bachelor (Bac+3)",
    "Cursus Bac+3 certifié par l'État. Construisez votre avenir professionnel avec nos spécialisations et l'alternance.",
    base_bc + [("Bachelor", '')],
    './assets/scroll-actual-1.jpg',
    """
    <section class="requirements-section">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up">
                <span class="tag"><span class="dot"></span> Points Clés</span>
                <h2 class="section-title">Pourquoi choisir le Bachelor ?</h2>
                <p class="section-subtitle" style="margin:.75rem auto 0;">Un diplôme professionnalisant et ouvert sur l'international, combinant socle académique et immersion professionnelle.</p>
            </div>
            <div class="requirements-grid">
                <div class="req-card fade-up" style="--delay:0.1s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg></div><h3>Reconnaissance RNCP</h3></div>
                    <ul class="req-list">
                        <li>Titre certifié par l'État de Niveau 6</li>
                        <li>Cursus structuré en 3 ans (post-bac, post-bac+1 ou post-bac+2)</li>
                        <li>Crédits ECTS délivrés pour poursuite d'études ou mobilité internationale</li>
                    </ul>
                </div>
                <div class="req-card fade-up" style="--delay:0.2s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg></div><h3>Alternance en 3ème année</h3></div>
                    <ul class="req-list">
                        <li>Deux premières années sous statut d'étudiant pour acquérir les bases</li>
                        <li>Troisième année en alternance pour une insertion professionnelle rapide</li>
                        <li>Prise en charge financière totale des frais en 3ème année</li>
                    </ul>
                </div>
                <div class="req-card fade-up" style="--delay:0.3s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg></div><h3>Domaines Spécialisés</h3></div>
                    <ul class="req-list">
                        <li>Filières ciblées : Marketing, Communication, Business Development, Management</li>
                        <li>Enseignement pratique axé sur les besoins réels des entreprises</li>
                        <li>Projets réels et challenges par équipe</li>
                    </ul>
                </div>
                <div class="req-card fade-up" style="--delay:0.4s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div><h3>Excellent Taux d'Insertion</h3></div>
                    <ul class="req-list">
                        <li>90% des diplômés en poste dans les 6 mois après le diplôme</li>
                        <li>Réseau d'alumni actif et partenariats corporatifs solides</li>
                        <li>Suivi de carrière individualisé pour chaque étudiant</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <section class="admission-steps-section">
        <div class="container">
            <div class="section-header text-center fade-up">
                <span class="tag"><span class="dot"></span> Procédure</span>
                <h2 class="section-title">Les 4 étapes de l'admission Bachelor</h2>
            </div>
            <div class="admission-steps-grid">
                <div class="step-card fade-up" style="--delay:0.1s"><div class="step-num">1</div><h3>Dossier en ligne</h3><p>Soumettez vos bulletins scolaires, CV, lettre de motivation et pièces justificatives via notre portail en ligne.</p></div>
                <div class="step-card fade-up" style="--delay:0.2s"><div class="step-num">2</div><h3>Examen du jury</h3><p>Notre jury académique étudie votre dossier scolaire, votre comportement et votre parcours personnel.</p></div>
                <div class="step-card fade-up" style="--delay:0.3s"><div class="step-num">3</div><h3>Évaluations</h3><p>Réalisez un court test écrit (anglais et culture générale) suivi d'un entretien oral de motivation de 20 minutes.</p></div>
                <div class="step-card fade-up" style="--delay:0.4s"><div class="step-num">4</div><h3>Résultats</h3><p>La décision finale d'admissibilité ou d'admission vous est envoyée sous 5 jours ouvrés.</p></div>
            </div>
        </div>
    </section>

    <section class="faq-section section-padding" style="width:100%; background:var(--clr-white);">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up">
                <h2 class="section-title">Questions fréquentes sur le Bachelor</h2>
            </div>
            <div class="faq-accordion">
                <div class="faq-item">
                    <button class="faq-question">Puis-je intégrer le Bachelor directement en 2ème ou 3ème année ?<span class="faq-icon"></span></button>
                    <div class="faq-answer"><div class="faq-answer-content">Oui. Nous acceptons les admissions parallèles : entrée en 2ème année après une année validée de licence/classe prépa, ou entrée en 3ème année après un Bac+2 validé (BTS, DUT, ou 120 crédits ECTS équivalents).</div></div>
                </div>
                <div class="faq-item">
                    <button class="faq-question">Comment fonctionne le rythme de l'alternance en 3ème année ?<span class="faq-icon"></span></button>
                    <div class="faq-answer"><div class="faq-answer-content">Le rythme est généralement d'une semaine de cours par mois ou de quelques jours par semaine en cours et le reste en entreprise, permettant une intégration complète en milieu professionnel.</div></div>
                </div>
            </div>
        </div>
    </section>

    <section class="stats-banner">
        <div class="container">
            <div class="stats-banner-grid">
                <div class="stat-item fade-up"><span class="stat-number">90%</span><span class="stat-label">Insertion pro sous 6 mois</span></div>
                <div class="stat-item fade-up" style="--delay:.1s"><span class="stat-number">3 ans</span><span class="stat-label">Durée totale cursus</span></div>
                <div class="stat-item fade-up" style="--delay:.2s"><span class="stat-number">5 jours</span><span class="stat-label">Délai résultats d'admission</span></div>
                <div class="stat-item fade-up" style="--delay:.3s"><span class="stat-number">RNCP 6</span><span class="stat-label">Titre certifié d'État</span></div>
            </div>
        </div>
    </section>
    """
)

# ── admissions BBA ───────────────────────────────────────────────────────────
make('admissions-bba.html',
    "Admission BBA",
    "Découvrez la procédure d'admission pour le Bachelor of Business Administration (BBA) de Campus Superia. Cursus bilingue Bac+4 axé international.",
    "Admission<br>BBA (Bac+4)",
    "Bachelor of Business Administration (Bac+4). Ouvrez-vous à l'international avec un cursus bilingue, des semestres d'études à l'étranger.",
    base_bc + [("BBA", '')],
    './assets/scroll-actual-3.jpg',
    """
    <section class="requirements-section">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up">
                <span class="tag"><span class="dot"></span> Cursus Global</span>
                <h2 class="section-title">Pourquoi choisir le BBA ?</h2>
                <p class="section-subtitle" style="margin:.75rem auto 0;">Un programme d'excellence bilingue en 4 ans axé sur le commerce international et la mobilité académique.</p>
            </div>
            <div class="requirements-grid">
                <div class="req-card fade-up" style="--delay:0.1s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg></div><h3>Cursus Bilingue</h3></div>
                    <ul class="req-list">
                        <li>Cours dispensés de 50% à 100% en anglais selon les années</li>
                        <li>Immersion linguistique totale et préparation aux carrières globales</li>
                        <li>Corps professoral international composé de spécialistes du domaine</li>
                    </ul>
                </div>
                <div class="req-card fade-up" style="--delay:0.2s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg></div><h3>Mobilité Internationale</h3></div>
                    <ul class="req-list">
                        <li>Semestres d'études à l'étranger dans nos universités partenaires</li>
                        <li>Stages en entreprise à l'international possibles chaque année</li>
                        <li>Possibilité de double-diplôme international avec des universités reconnues</li>
                    </ul>
                </div>
                <div class="req-card fade-up" style="--delay:0.3s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/></svg></div><h3>Format Bac+4</h3></div>
                    <ul class="req-list">
                        <li>Diplôme de niveau Bac+4 visé par l'État (Titre RNCP Niveau 6)</li>
                        <li>Accès facilité aux programmes de Master et MSc en France et à l'étranger</li>
                        <li>240 crédits ECTS capitalisés sur la durée de la formation</li>
                    </ul>
                </div>
                <div class="req-card fade-up" style="--delay:0.4s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg></div><h3>Majeures de Spécialisation</h3></div>
                    <ul class="req-list">
                        <li>Choix de spécialisation en Finance Internationale ou Management de projet global</li>
                        <li>Approche basée sur l'entreprenariat et l'analyse de données globales</li>
                        <li>Immersion professionnelle en fin de cursus</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <section class="admission-steps-section">
        <div class="container">
            <div class="section-header text-center fade-up">
                <span class="tag"><span class="dot"></span> Double Voie</span>
                <h2 class="section-title">Deux voies d'admission possibles</h2>
            </div>
            <div class="admission-steps-grid">
                <div class="step-card fade-up" style="--delay:0.1s"><div class="step-num">1</div><h3>Voie Post-Bac</h3><p>Pour les élèves de Terminale, formulation des vœux via Parcoursup, suivi d'évaluations écrites et orales.</p></div>
                <div class="step-card fade-up" style="--delay:0.2s"><div class="step-num">2</div><h3>Voie Parallèle</h3><p>Pour les étudiants en Bac+1 ou Bac+2, candidature directe sur dossier scolaire et entretien bilingue.</p></div>
                <div class="step-card fade-up" style="--delay:0.3s"><div class="step-num">3</div><h3>Entretien</h3><p>Passage d'un oral individuel bilingue de 30 minutes avec analyse de la motivation globale et du niveau d'anglais.</p></div>
                <div class="step-card fade-up" style="--delay:0.4s"><div class="step-num">4</div><h3>Intégration</h3><p>Dossier finalisé et processus d'inscription validé à réception de l'attestation de scolarité ou du diplôme précédent.</p></div>
            </div>
        </div>
    </section>

    <section class="faq-section section-padding" style="width:100%; background:var(--clr-white);">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up">
                <h2 class="section-title">Questions fréquentes sur le BBA</h2>
            </div>
            <div class="faq-accordion">
                <div class="faq-item">
                    <button class="faq-question">Un niveau d'anglais bilingue est-il requis pour postuler ?<span class="faq-icon"></span></button>
                    <div class="faq-answer"><div class="faq-answer-content">Non. Bien que les cours soient dispensés partiellement en anglais, nous acceptons les candidats de niveau intermédiaire (B2 conseillé). Les cours de soutien et l'immersion progressive permettent de rapidement perfectionner votre niveau.</div></div>
                </div>
                <div class="faq-item">
                    <button class="faq-question">Quels sont les pays d'accueil pour la mobilité internationale ?<span class="faq-icon"></span></button>
                    <div class="faq-answer"><div class="faq-answer-content">Nous disposons de nombreux partenariats universitaires en Europe, en Amérique du Nord (USA, Canada) et en Asie. Notre bureau international vous aide à organiser votre départ.</div></div>
                </div>
            </div>
        </div>
    </section>

    <section class="stats-banner">
        <div class="container">
            <div class="stats-banner-grid">
                <div class="stat-item fade-up"><span class="stat-number">4 ans</span><span class="stat-label">Durée du cursus</span></div>
                <div class="stat-item fade-up" style="--delay:.1s"><span class="stat-number">50%+</span><span class="stat-label">Cours en anglais</span></div>
                <div class="stat-item fade-up" style="--delay:.2s"><span class="stat-number">240</span><span class="stat-label">Crédits ECTS délivrés</span></div>
                <div class="stat-item fade-up" style="--delay:.3s"><span class="stat-number">100%</span><span class="stat-label">Candidatures en ligne</span></div>
            </div>
        </div>
    </section>
    """
)

# ── admissions MSc ───────────────────────────────────────────────────────────
make('admissions-msc.html',
    "Admission Master of Science",
    "Découvrez la procédure d'admission pour les programmes Master of Science (MSc) de Campus Superia. Cursus d'excellence Bac+5 en alternance.",
    "Admission<br>MSc (Bac+5)",
    "Programme Bac+5 d'excellence (Titre RNCP Niveau 7). Développez une expertise métier de haut niveau et accédez à un large réseau d'entreprises.",
    base_bc + [("MSc", '')],
    './assets/hero.jpeg',
    """
    <section class="requirements-section">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up">
                <span class="tag"><span class="dot"></span> Niveau Master</span>
                <h2 class="section-title">Pourquoi choisir le Master of Science ?</h2>
                <p class="section-subtitle" style="margin:.75rem auto 0;">Un programme d'études spécialisé de haut niveau, conçu avec des professionnels du secteur pour une insertion directe au niveau cadre.</p>
            </div>
            <div class="requirements-grid">
                <div class="req-card fade-up" style="--delay:0.1s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg></div><h3>Expertise Métier &amp; VAE</h3></div>
                    <ul class="req-list">
                        <li>Titre certifié par l'État de Niveau 7 (Bac+5)</li>
                        <li>Spécialisations adaptées aux réalités du marché : Finance d'entreprise, Marketing Digital &amp; IA, Ressources Humaines</li>
                        <li>Disponible également en Validation des Acquis de l'Expérience (VAE)</li>
                    </ul>
                </div>
                <div class="req-card fade-up" style="--delay:0.2s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg></div><h3>Alternance Privilégiée</h3></div>
                    <ul class="req-list">
                        <li>Cursus réalisable entièrement en alternance (apprentissage ou professionnalisation)</li>
                        <li>Rythme de formation optimisé pour une présence maximale en entreprise</li>
                        <li>Prise en charge à 100% des frais par l'entreprise et salaire garanti</li>
                    </ul>
                </div>
                <div class="req-card fade-up" style="--delay:0.3s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg></div><h3>Réseau Partenaires</h3></div>
                    <ul class="req-list">
                        <li>Accès privilégié à un large réseau d'entreprises nationales et internationales</li>
                        <li>Rencontres recruteurs et forums de recrutement exclusifs sur le campus</li>
                        <li>Taux de placement exceptionnel des alternants diplômés</li>
                    </ul>
                </div>
                <div class="req-card fade-up" style="--delay:0.4s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div><h3>Cadres &amp; Intervenants</h3></div>
                    <ul class="req-list">
                        <li>Enseignements dirigés par des experts en activité et directeurs de départements</li>
                        <li>Pédagogie active : études de cas réelles, simulations et business games</li>
                        <li>Rémunération moyenne de sortie élevée (jeunes diplômés cadres)</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <section class="admission-steps-section">
        <div class="container">
            <div class="section-header text-center fade-up">
                <span class="tag"><span class="dot"></span> Les 5 étapes</span>
                <h2 class="section-title">Processus de recrutement MSc</h2>
            </div>
            <div class="admission-steps-grid">
                <div class="step-card fade-up" style="--delay:0.1s"><div class="step-num">1</div><h3>Dossier</h3><p>Soumettez votre dossier académique complet (Bac+3/4 validé), CV et votre projet de spécialisation.</p></div>
                <div class="step-card fade-up" style="--delay:0.2s"><div class="step-num">2</div><h3>Jury</h3><p>Notre jury pédagogique examine votre dossier et valide l'admissibilité sous 48h.</p></div>
                <div class="step-card fade-up" style="--delay:0.3s"><div class="step-num">3</div><h3>Oral</h3><p>Passez un entretien individuel de 20 minutes portant sur votre parcours professionnel et vos motivations.</p></div>
                <div class="step-card fade-up" style="--delay:0.4s"><div class="step-num">4</div><h3>Résultats</h3><p>La décision finale concernant votre admission est rendue sous un délai maximum de 5 jours ouvrés.</p></div>
                <div class="step-card fade-up" style="--delay:0.5s"><div class="step-num">5</div><h3>Placement</h3><p>Accès immédiat à nos ateliers de placement et offres partenaires pour dénicher votre alternance.</p></div>
            </div>
        </div>
    </section>

    <section class="faq-section section-padding" style="width:100%; background:var(--clr-white);">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up">
                <h2 class="section-title">Questions fréquentes sur le MSc</h2>
            </div>
            <div class="faq-accordion">
                <div class="faq-item">
                    <button class="faq-question">Qui peut s'inscrire en MSc (Master of Science) ?<span class="faq-icon"></span></button>
                    <div class="faq-answer"><div class="faq-answer-content">Les programmes MSc sont accessibles aux titulaires d'un diplôme de niveau Bac+3 (Bachelor, Licence, 180 crédits ECTS) pour une intégration en 1ère année (MSc 1), ou d'un niveau Bac+4 (Master 1, Master of Science 1ère année, ou 240 crédits ECTS) pour une entrée directe en 2ème année (MSc 2).</div></div>
                </div>
                <div class="faq-item">
                    <button class="faq-question">Quels sont les débouchés après un MSc ?<span class="faq-icon"></span></button>
                    <div class="faq-answer"><div class="faq-answer-content">Les débouchés sont axés sur les postes de cadres et managers dans nos diverses filières : Contrôleur de gestion, Business Analyst, Chef de projet digital, Responsable Marketing, Consultant ou Directeur RH.</div></div>
                </div>
            </div>
        </div>
    <section class="stats-banner">
        <div class="container">
            <div class="stats-banner-grid">
                <div class="stat-item fade-up"><span class="stat-number">97%</span><span class="stat-label">Insertion pro sous 6 mois</span></div>
                <div class="stat-item fade-up" style="--delay:.1s"><span class="stat-number">10 000</span><span class="stat-label">Entreprises partenaires</span></div>
                <div class="stat-item fade-up" style="--delay:.2s"><span class="stat-number">5 jours</span><span class="stat-label">Délai d'admissibilité</span></div>
                <div class="stat-item fade-up" style="--delay:.3s"><span class="stat-number">Bac+5</span><span class="stat-label">Titre RNCP de Niveau 7</span></div>
            </div>
        </div>
    </section>
    """
)

PARTENARIATS_BODY = """
    <!-- Why become a partner -->
    <section class="why-partner-section section-padding">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up">
                <span class="tag"><span class="dot"></span> Pourquoi collaborer</span>
                <h2 class="section-title">Pourquoi devenir partenaire ?</h2>
                <p class="section-subtitle" style="margin:.75rem auto 0; max-width:600px;">Associez votre organisation à Campus Superia pour dynamiser vos projets, recruter des profils d'excellence et impacter l'éducation de demain.</p>
            </div>
            <div class="why-partner-grid">
                <div class="why-card fade-up" style="--delay: 0.1s">
                    <div class="why-card-icon">
                        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="8.5" cy="7" r="4"></circle><line x1="20" y1="8" x2="20" y2="14"></line><line x1="23" y1="11" x2="17" y2="11"></line></svg>
                    </div>
                    <h3>Recruter nos talents</h3>
                    <p>Accédez en priorité à nos étudiants qualifiés en recherche de stages, d'alternance ou de premier emploi.</p>
                </div>
                <div class="why-card fade-up" style="--delay: 0.2s">
                    <div class="why-card-icon">
                        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"></path><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path></svg>
                    </div>
                    <h3>Co-construire les formations</h3>
                    <p>Participez à la mise à jour de nos programmes pédagogiques pour les adapter directement à vos besoins terrain.</p>
                </div>
                <div class="why-card fade-up" style="--delay: 0.3s">
                    <div class="why-card-icon">
                        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 10a6 6 0 0 0-12 0c0 7 3 9 3 9h6s3-2 3-9"></path><line x1="12" y1="22" x2="12" y2="23"></line><path d="M9 22h6"></path></svg>
                    </div>
                    <h3>Développer l’innovation</h3>
                    <p>Collaborez sur des hackathons, des projets d'étudiants ou de la recherche appliquée pour relever vos défis complexes.</p>
                </div>
                <div class="why-card fade-up" style="--delay: 0.4s">
                    <div class="why-card-icon">
                        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="7"></circle><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline></svg>
                    </div>
                    <h3>Valoriser votre marque</h3>
                    <p>Renforcez votre marque employeur et associez votre image à un pôle académique moderne et innovant.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Partnership categories -->
    <section class="partner-categories-section section-padding">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up">
                <span class="tag"><span class="dot"></span> Profils concernés</span>
                <h2 class="section-title">Catégories de partenariat</h2>
                <p class="section-subtitle" style="margin:.75rem auto 0; max-width:600px;">Des formats de collaboration adaptés au profil et aux objectifs de votre organisation.</p>
            </div>
            <div class="categories-grid">
                <div class="category-card fade-up" style="--delay: 0.1s">
                    <h3>Entreprises</h3>
                    <p>De la start-up au grand groupe, intégrez nos étudiants au sein de vos équipes et partagez votre expertise métier lors de nos rendez-vous réguliers.</p>
                    <ul class="category-list">
                        <li>Offres de stage & alternance</li>
                        <li>Forums de recrutement</li>
                        <li>Masterclasses professionnelles</li>
                        <li>Projets d'études réels</li>
                    </ul>
                </div>
                <div class="category-card fade-up" style="--delay: 0.2s">
                    <h3>Institutions académiques</h3>
                    <p>Établissements d'enseignement supérieur nationaux ou internationaux, construisons des passerelles d'études et des projets conjoints.</p>
                    <ul class="category-list">
                        <li>Double-diplômes & passerelles</li>
                        <li>Échanges internationaux</li>
                        <li>Projets de recherche appliquée</li>
                        <li>Séminaires de recherche</li>
                    </ul>
                </div>
                <div class="category-card fade-up" style="--delay: 0.3s">
                    <h3>Organisations publiques & privées</h3>
                    <p>Collectivités, ministères, fondations ou associations, développons des initiatives collectives à fort impact social et économique.</p>
                    <ul class="category-list">
                        <li>Sponsoring d'événements</li>
                        <li>Conférences thématiques</li>
                        <li>Programmes d'inclusion</li>
                        <li>Hackathons d'utilité publique</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- Collaboration process -->
    <section class="collab-timeline-section section-padding">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up">
                <span class="tag"><span class="dot"></span> Parcours</span>
                <h2 class="section-title">Le processus de collaboration</h2>
                <p class="section-subtitle" style="margin:.75rem auto 0; max-width:600px;">Une approche structurée en 4 étapes pour un partenariat performant et durable.</p>
            </div>
            <div class="timeline-container">
                <div class="timeline-step fade-up" style="--delay: 0.1s">
                    <div class="timeline-node">1</div>
                    <h3>Premier échange</h3>
                    <p>Rencontre d'évaluation pour identifier vos objectifs, vos besoins en talents et définir le périmètre idéal.</p>
                </div>
                <div class="timeline-step fade-up" style="--delay: 0.2s">
                    <div class="timeline-node">2</div>
                    <h3>Construction du partenariat</h3>
                    <p>Co-conception d'un programme d'action personnalisé (modalités, calendrier, ressources et objectifs chiffrés).</p>
                </div>
                <div class="timeline-step fade-up" style="--delay: 0.3s">
                    <div class="timeline-node">3</div>
                    <h3>Mise en œuvre</h3>
                    <p>Lancement des initiatives : publication d'offres, programmation d'ateliers, accueil d'étudiants ou lancement de projet.</p>
                </div>
                <div class="timeline-step fade-up" style="--delay: 0.4s">
                    <div class="timeline-node">4</div>
                    <h3>Suivi et évolution</h3>
                    <p>Bilan régulier des actions menées, mesure d'impact et ajustement annuel pour accompagner votre croissance.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Collaboration opportunities -->
    <section class="opportunities-section section-padding">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up">
                <span class="tag"><span class="dot"></span> Opportunités</span>
                <h2 class="section-title">Nos opportunités de collaboration</h2>
                <p class="section-subtitle" style="margin:.75rem auto 0; max-width:600px;">Explorez les différents leviers d'action pour vous impliquer concrètement auprès de notre communauté.</p>
            </div>
            <div class="opp-grid">
                <div class="opp-card fade-up" style="--delay: 0.05s">
                    <div class="opp-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
                    </div>
                    <h3>Recrutement</h3>
                    <p>Accédez en priorité à nos profils diplômés.</p>
                </div>
                <div class="opp-card fade-up" style="--delay: 0.1s">
                    <div class="opp-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>
                    </div>
                    <h3>Stages</h3>
                    <p>Accueillez nos étudiants pour des missions de 2 à 6 mois.</p>
                </div>
                <div class="opp-card fade-up" style="--delay: 0.15s">
                    <div class="opp-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>
                    </div>
                    <h3>Alternance</h3>
                    <p>Intégrez des talents à l'année en contrat d'apprentissage.</p>
                </div>
                <div class="opp-card fade-up" style="--delay: 0.2s">
                    <div class="opp-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
                    </div>
                    <h3>Conférences</h3>
                    <p>Intervenez sur des sujets sectoriels et d'actualité.</p>
                </div>
                <div class="opp-card fade-up" style="--delay: 0.25s">
                    <div class="opp-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
                    </div>
                    <h3>Masterclass</h3>
                    <p>Animez des ateliers techniques ou des sessions interactives.</p>
                </div>
                <div class="opp-card fade-up" style="--delay: 0.3s">
                    <div class="opp-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
                    </div>
                    <h3>Mentorat</h3>
                    <p>Accompagnez personnellement un étudiant dans son projet.</p>
                </div>
                <div class="opp-card fade-up" style="--delay: 0.35s">
                    <div class="opp-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg>
                    </div>
                    <h3>Projets étudiants</h3>
                    <p>Soumettez un défi concret à la résolution de nos étudiants.</p>
                </div>
                <div class="opp-card fade-up" style="--delay: 0.4s">
                    <div class="opp-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
                    </div>
                    <h3>Recherche</h3>
                    <p>Co-développez des innovations via des thèses ou de la recherche.</p>
                </div>
                <div class="opp-card fade-up" style="--delay: 0.45s">
                    <div class="opp-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="4 17 10 11 4 5"></polyline><line x1="12" y1="19" x2="20" y2="19"></line></svg>
                    </div>
                    <h3>Hackathons</h3>
                    <p>Proposez et sponsorisez un marathon d'innovation de 48h.</p>
                </div>
                <div class="opp-card fade-up" style="--delay: 0.5s">
                    <div class="opp-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
                    </div>
                    <h3>Sponsoring</h3>
                    <p>Soutenez nos événements d'excellence ou bourses d'études.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Statistics Section -->
    <section class="stats-banner">
        <div class="container">
            <div class="stats-banner-grid">
                <div class="stat-item fade-up">
                    <span class="stat-number stat-number-anim" data-target="50" data-suffix="+">0+</span>
                    <span class="stat-label">Partenaires actifs</span>
                </div>
                <div class="stat-item fade-up" style="--delay:.1s">
                    <span class="stat-number stat-number-anim" data-target="95" data-suffix="%">0%</span>
                    <span class="stat-label">Insertion professionnelle</span>
                </div>
                <div class="stat-item fade-up" style="--delay:.2s">
                    <span class="stat-number stat-number-anim" data-target="300" data-suffix="+">0+</span>
                    <span class="stat-label">Offres de stages & alternances / an</span>
                </div>
                <div class="stat-item fade-up" style="--delay:.3s">
                    <span class="stat-number stat-number-anim" data-target="15" data-suffix="+">0+</span>
                    <span class="stat-label">Projets étudiants réalisés</span>
                </div>
            </div>
        </div>
    </section>

    <!-- Partners section -->
    <section class="logo-carousel-container">
        <div class="section-header text-center mb-5 fade-up">
            <span class="tag"><span class="dot"></span> Réseau</span>
            <h2 class="section-title">Ils nous font confiance</h2>
        </div>
        <div class="logo-carousel-track">
            <!-- Logo 1: Google -->
            <div class="logo-item">
                <svg viewBox="0 0 24 24" width="36" height="36"><path d="M12.24 10.285V14.4h6.887c-.648 2.41-2.519 4.114-5.136 4.114A5.79 5.79 0 0 1 8.2 12.725a5.79 5.79 0 0 1 5.79-5.79c2.518 0 4.114 1.547 4.114 1.547l3.056-3.056C21.16 5.42 17.844 3 13.99 3 8.358 3 3.99 7.368 3.99 13s4.368 10 10 10c6.046 0 9.873-4.258 9.873-10 0-.682-.068-1.285-.236-1.715h-11.39Z"/></svg>
            </div>
            <!-- Logo 2: Microsoft -->
            <div class="logo-item">
                <svg viewBox="0 0 23 23" width="36" height="36"><path d="M0 0h11v11H0z" fill="#F25022"/><path d="M12 0h11v11H12z" fill="#7FBA00"/><path d="M0 12h11v11H0z" fill="#00A4EF"/><path d="M12 12h11v11H12z" fill="#FFB900"/></svg>
            </div>
            <!-- Logo 3: Orange -->
            <div class="logo-item">
                <svg viewBox="0 0 24 24" width="36" height="36"><rect width="24" height="24" fill="#FF7900"/><path d="M3 17h18v4H3z" fill="#FFF"/></svg>
            </div>
            <!-- Logo 4: Capgemini -->
            <div class="logo-item">
                <svg viewBox="0 0 24 24" width="36" height="36"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2Zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93Zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.66 0 3 1.34 3 3v1.41c1.39.7 2.3 2.11 2.3 3.7 0 .93-.33 1.79-.9 2.48Z"/></svg>
            </div>
            <!-- Logo 5: Société Générale -->
            <div class="logo-item">
                <svg viewBox="0 0 24 24" width="36" height="36"><rect width="24" height="11" fill="#FF0000"/><rect y="13" width="24" height="11" fill="#000000"/><rect y="11" width="24" height="2" fill="#FFFFFF"/></svg>
            </div>
            <!-- Logo 6: Decathlon -->
            <div class="logo-item">
                <svg viewBox="0 0 24 24" width="36" height="36"><path d="M2 4h6a8 8 0 0 1 8 8 8 8 0 0 1-8 8H2V4Zm6 12a4 4 0 0 0 4-4 4 4 0 0 0-4-4H6v8h2Z"/></svg>
            </div>
            <!-- Logo 7: L'Oréal -->
            <div class="logo-item">
                <svg viewBox="0 0 24 24" width="36" height="36"><path d="M12 2C6.47 2 2 6.5 2 12a10 10 0 0 0 10 10c1.82 0 3.53-.5 5-1.35l-2.43-2.43A6.62 6.62 0 0 1 12 16.63c-2.56 0-4.63-2.07-4.63-4.63S9.44 7.37 12 7.37s4.63 2.07 4.63 4.63c0 .87-.24 1.68-.66 2.37l2.43 2.43A9.93 9.93 0 0 0 22 12c0-5.5-4.47-10-10-10Z"/></svg>
            </div>
            
            <!-- Duplicated for Infinite Loop -->
            <div class="logo-item">
                <svg viewBox="0 0 24 24" width="36" height="36"><path d="M12.24 10.285V14.4h6.887c-.648 2.41-2.519 4.114-5.136 4.114A5.79 5.79 0 0 1 8.2 12.725a5.79 5.79 0 0 1 5.79-5.79c2.518 0 4.114 1.547 4.114 1.547l3.056-3.056C21.16 5.42 17.844 3 13.99 3 8.358 3 3.99 7.368 3.99 13s4.368 10 10 10c6.046 0 9.873-4.258 9.873-10 0-.682-.068-1.285-.236-1.715h-11.39Z"/></svg>
            </div>
            <div class="logo-item">
                <svg viewBox="0 0 23 23" width="36" height="36"><path d="M0 0h11v11H0z" fill="#F25022"/><path d="M12 0h11v11H12z" fill="#7FBA00"/><path d="M0 12h11v11H0z" fill="#00A4EF"/><path d="M12 12h11v11H12z" fill="#FFB900"/></svg>
            </div>
            <div class="logo-item">
                <svg viewBox="0 0 24 24" width="36" height="36"><rect width="24" height="24" fill="#FF7900"/><path d="M3 17h18v4H3z" fill="#FFF"/></svg>
            </div>
            <div class="logo-item">
                <svg viewBox="0 0 24 24" width="36" height="36"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2Zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93Zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.66 0 3 1.34 3 3v1.41c1.39.7 2.3 2.11 2.3 3.7 0 .93-.33 1.79-.9 2.48Z"/></svg>
            </div>
            <div class="logo-item">
                <svg viewBox="0 0 24 24" width="36" height="36"><rect width="24" height="11" fill="#FF0000"/><rect y="13" width="24" height="11" fill="#000000"/><rect y="11" width="24" height="2" fill="#FFFFFF"/></svg>
            </div>
            <div class="logo-item">
                <svg viewBox="0 0 24 24" width="36" height="36"><path d="M2 4h6a8 8 0 0 1 8 8 8 8 0 0 1-8 8H2V4Zm6 12a4 4 0 0 0 4-4 4 4 0 0 0-4-4H6v8h2Z"/></svg>
            </div>
            <div class="logo-item">
                <svg viewBox="0 0 24 24" width="36" height="36"><path d="M12 2C6.47 2 2 6.5 2 12a10 10 0 0 0 10 10c1.82 0 3.53-.5 5-1.35l-2.43-2.43A6.62 6.62 0 0 1 12 16.63c-2.56 0-4.63-2.07-4.63-4.63S9.44 7.37 12 7.37s4.63 2.07 4.63 4.63c0 .87-.24 1.68-.66 2.37l2.43 2.43A9.93 9.93 0 0 0 22 12c0-5.5-4.47-10-10-10Z"/></svg>
            </div>
        </div>
    </section>

    <!-- FAQ Section -->
    <section class="faq-section section-padding" style="width:100%; background:var(--clr-bg-main);">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up">
                <span class="tag"><span class="dot"></span> FAQ</span>
                <h2 class="section-title">Questions fréquentes sur les partenariats</h2>
            </div>
            <div class="faq-accordion">
                <div class="faq-item">
                    <button class="faq-question">Comment devenir partenaire de Campus Superia ?<span class="faq-icon"></span></button>
                    <div class="faq-answer"><div class="faq-answer-content">Pour toute demande d’information, nous vous invitons à remplir le formulaire ci-dessous ou à nous contacter directement par e-mail. Un conseiller en orientation ou un chargé des relations entreprises prendra ensuite contact avec vous afin d’organiser un premier échange personnalisé.</div></div>
                </div>
                <div class="faq-item">
                    <button class="faq-question">Quels sont les coûts associés à un partenariat ?<span class="faq-icon"></span></button>
                    <div class="faq-answer"><div class="faq-answer-content">La signature d’un accord-cadre de partenariat est gratuite. Toutefois, certains projets spécifiques, tels que des hackathons personnalisés, des actions de recherche dédiées ou des opérations de sponsoring, peuvent faire l’objet d’un financement spécifique.</div></div>
                </div>
                <div class="faq-item">
                    <button class="faq-question">Puis-je proposer des offres d'alternance ou de stage ?<span class="faq-icon"></span></button>
                    <div class="faq-answer"><div class="faq-answer-content">Absolument. Nos étudiants préparant un BTS, un Bachelor ou un MSc recherchent régulièrement des stages ainsi que des contrats d’alternance. Nous mettons à votre disposition notre plateforme interne afin de diffuser vos offres auprès de nos candidats.</div></div>
                </div>
                <div class="faq-item">
                    <button class="faq-question">Comment se déroule le suivi des projets étudiants ?<span class="faq-icon"></span></button>
                    <div class="faq-answer"><div class="faq-answer-content">Chaque projet étudiant, qu’il s’agisse d’un projet de groupe ou d’un hackathon, est encadré par un enseignant-tuteur de Campus Supéria ainsi que par un référent au sein de votre organisation, afin de garantir la qualité des livrables.</div></div>
                </div>
            </div>
        </div>
    </section>
"""

make('partenariats.html',
    "Devenir Partenaire",
    "Découvrez les opportunités de partenariat avec Campus Superia. Recrutez nos talents, co-construisez nos formations et développez l'innovation.",
    "Construisons l’avenir<br>ensemble",
    "Rejoignez le réseau de partenaires de Campus Superia et collaborez avec une institution engagée pour former les leaders de demain.",
    [('Accueil', 'index.html'), ('Partenariats', '')],
    './assets/scroll-actual-3.jpg',
    PARTENARIATS_BODY
)

print("\n✅ All 16 pages generated successfully!")

