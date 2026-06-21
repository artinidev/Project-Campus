#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

HEADER_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
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
        <div class="logo-container"><a href="index-en.html"><img src="./assets/logo-full.png" alt="Campus Superia Logo"></a></div>
        <button class="mobile-menu-btn" aria-label="Toggle menu" onclick="document.querySelector('.site-nav').classList.toggle('active')"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg></button>
        <nav class="site-nav">
            <a href="index-en.html#about">About</a>
            <a href="index-en.html#academics">Mission</a>
            <a href="programmes-en.html">Program</a>
            <div class="nav-dropdown-wrapper">
                <a href="test-en.html" class="dropdown-trigger"><span>Pre-evaluation</span><svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="chevron-icon"><polyline points="6 9 12 15 18 9"></polyline></svg></a>
                <div class="nav-dropdown">
                    <div class="dropdown-links-col">
                        <div class="dropdown-item opt-analyse"><a href="analyse-en.html"><span class="item-title">Personalized Project Analysis</span><span class="item-desc">To support you in choosing your training, complete this short questionnaire so our team can understand your background and goals.</span></a></div>
                        <div class="dropdown-item opt-test"><a href="test-en.html"><span class="item-title">Pre-evaluation</span><span class="item-desc">CAMPUS SUPERIA proposes a French placement test to evaluate your current level, identify your needs, and guide you towards the right path.</span></a></div>
                    </div>
                    <div class="dropdown-preview-col"><div class="preview-img-container"><img src="./assets/hero.jpeg" class="preview-img img-default" alt="Campus Default"><img src="./assets/scroll-actual-2.jpg" class="preview-img img-analyse" alt="Analyse"><img src="./assets/scroll-actual-1.jpg" class="preview-img img-test" alt="Test"></div></div>
                </div>
            </div>
            <div class="nav-dropdown-wrapper">
                <a href="admissions-en.html" class="dropdown-trigger">
                    <span>Admissions</span>
                    <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="chevron-icon"><polyline points="6 9 12 15 18 9"></polyline></svg>
                </a>
                <div class="nav-dropdown admissions-mega">
                    <!-- Col 1: Main Category Cards -->
                    <div class="adm-column adm-col-main">
                        <div class="dropdown-col-header">Admission</div>
                        <div class="adm-cards-container">
                            <div class="adm-card-btn active" data-target="candidature">
                                <div class="adm-card-icon">
                                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>
                                </div>
                                <div class="adm-card-text"><span class="adm-card-title">Apply to CAMPUS SUPERIA</span></div>
                                <div class="adm-card-arrow">
                                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                                </div>
                            </div>
                            
                            <div class="adm-card-btn" data-target="financement">
                                <div class="adm-card-icon">
                                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>
                                </div>
                                <div class="adm-card-text"><span class="adm-card-title">Studies Financing</span></div>
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
                            <div class="dropdown-col-header">Apply to Campus Superia</div>
                            <div class="adm-cards-container">
                                <div class="adm-card-btn active" data-target="rentree-septembre">
                                    <div class="adm-card-icon">
                                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
                                    </div>
                                    <div class="adm-card-text"><span class="adm-card-title">Start in September</span></div>
                                    <div class="adm-card-arrow">
                                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                                    </div>
                                </div>
                                <div class="adm-card-btn" data-target="rentree-fevrier">
                                    <div class="adm-card-icon">
                                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
                                    </div>
                                    <div class="adm-card-text"><span class="adm-card-title">Start in February</span></div>
                                    <div class="adm-card-arrow">
                                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                                    </div>
                                </div>
                                <div class="adm-card-btn" data-target="procedure-internationale">
                                    <div class="adm-card-icon">
                                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
                                    </div>
                                    <div class="adm-card-text"><span class="adm-card-title">International Procedure</span></div>
                                    <div class="adm-card-arrow">
                                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                        <!-- Sub-panel for Financement -->
                        <div class="adm-sub-panel" id="sub-panel-financement">
                            <div class="dropdown-col-header">Studies Financing</div>
                            <div class="adm-cards-container">
                                <div class="adm-card-btn" data-target="financement-options">
                                    <div class="adm-card-icon">
                                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"></rect><line x1="12" y1="10" x2="12" y2="10"></line><line x1="12" y1="14" x2="12" y2="14"></line></svg>
                                    </div>
                                    <div class="adm-card-text"><span class="adm-card-title">Financing Options</span></div>
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
                            <div class="dropdown-col-header">Start in September</div>
                            <ul class="adm-detail-links">
                                <li><a href="admissions-bts-en.html">BTS Procedure</a></li>
                                <li><a href="admissions-bachelor-en.html">Bachelor Procedure</a></li>
                                <li><a href="admissions-bba-en.html">BBA Procedure</a></li>
                                <li><a href="admissions-msc-en.html">Master of Science Procedure</a></li>
                            </ul>
                        </div>
                        <div class="adm-links-panel" id="links-panel-rentree-fevrier">
                            <div class="dropdown-col-header">Start in February</div>
                            <ul class="adm-detail-links">
                                <li><a href="admissions-bachelor-en.html?rentree=fevrier">Bachelor Procedure</a></li>
                                <li><a href="admissions-bba-en.html?rentree=fevrier">BBA Procedure</a></li>
                                <li><a href="admissions-msc-en.html?rentree=fevrier">Master of Science Procedure</a></li>
                            </ul>
                        </div>
                        <div class="adm-links-panel" id="links-panel-procedure-internationale">
                            <div class="dropdown-col-header">International Procedure</div>
                            <ul class="adm-detail-links">
                                <li><a href="admissions-international-en.html">International Admission Bachelor</a></li>
                                <li><a href="admissions-international-en.html">International Admission BBA</a></li>
                                <li><a href="admissions-international-en.html">International Admission MSc</a></li>
                                <li><a href="admissions-international-en.html#visa">Student Visa</a></li>
                                <li><a href="admissions-international-en.html#visa">Student Housing</a></li>
                            </ul>
                        </div>
                        <div class="adm-links-panel" id="links-panel-financement-options">
                            <div class="dropdown-col-header">Studies Financing</div>
                            <ul class="adm-detail-links">
                                <li><a href="admissions-frais-en.html">Tuition fees</a></li>
                                <li><a href="admissions-bourses-en.html">Scholarships</a></li>
                                <li><a href="admissions-bourses-en.html#cpf">Financing</a></li>
                                <li><a href="admissions-frais-en.html#options">Installment Plan</a></li>
                                <li><a href="admissions-bourses-en.html#alternance">Work-Study</a></li>
                            </ul>
                        </div>
                    </div>
                    
                    <!-- Col 4: Preview Card -->
                    <div class="adm-column adm-col-preview">
                        <div class="adm-preview-container">
                            <div class="adm-preview-card active" data-preview="rentree-septembre">
                                <img src="./assets/adm-preview-september.png" alt="September Intake">
                            </div>
                            <div class="adm-preview-card" data-preview="rentree-fevrier">
                                <img src="./assets/adm-preview-september.png" alt="February Intake">
                            </div>
                            <div class="adm-preview-card" data-preview="procedure-internationale">
                                <img src="./assets/adm-preview-international.png" alt="International Procedure">
                            </div>
                            <div class="adm-preview-card" data-preview="financement-options">
                                <img src="./assets/adm-preview-scholarship.png" alt="Studies Financing">
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <a href="partenariats-en.html">Partnerships</a>
            <a href="index.html" class="nav-lang" aria-label="Switch language to French"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg><span>FR</span></a>
            <a href="#contact" class="nav-cta">Contact Us</a>
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
                            <a href="#contact" class="btn btn-brand-orange" style="border-radius:4px;">Apply Now →</a>
                            <a href="admissions-en.html" class="btn btn-outline-light" style="border-radius:4px;">Overview</a>
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
            <div class="header-left"><h2>Ready to<br>join us?</h2></div>
            <div class="header-right">
                <p>Submit your application today. Our team will contact you within 72 hours.</p>
                <div class="header-actions">
                    <a href="#contact" class="btn btn-brand-orange">Apply Now ↗</a>
                    <a href="tel:+33781547503" class="btn btn-outline-light">+33 781 547 503</a>
                </div>
            </div>
        </div>
        <div class="form-container fade-up">
            <div class="form-card">
                <div class="form-card-left"><h3>Your Application in 3 Steps</h3><p>Simple, fast and without commitment. Your advisor will guide you within 72 hours.</p><div class="card-features"><span class="feature-tag">Free</span><span class="feature-tag">Fast</span><span class="feature-tag">Dedicated</span></div></div>
                <div class="form-card-right">
                    <form action="#" class="campus-form-card" id="multi-step-form">
                        <div class="form-progress"><span class="progress-text">Step <span id="current-step">1</span> of 3</span><div class="progress-bar-bg"><div class="progress-bar-fill" id="progress-fill"></div></div></div>
                        <div class="form-step form-step-active" data-step="1">
                            <div class="form-group">
                                <label for="nom">Last Name <span class="text-brand-orange">*</span></label>
                                <input type="text" id="nom" name="nom" placeholder="Your last name" required>
                            </div>
                            <div class="form-group">
                                <label for="prenom">First Name <span class="text-brand-orange">*</span></label>
                                <input type="text" id="prenom" name="prenom" placeholder="Your first name" required>
                            </div>
                            <div class="form-group">
                                <label for="naissance">Date of Birth <span class="text-brand-orange">*</span></label>
                                <input type="date" id="naissance" name="naissance" required>
                            </div>
                            <div class="form-group">
                                <label for="email">Email <span class="text-brand-orange">*</span></label>
                                <input type="email" id="email" name="email" placeholder="example@email.com" required>
                            </div>
                            <div class="form-group">
                                <label for="telephone">Phone <span class="text-brand-orange">*</span></label>
                                <input type="tel" id="telephone" name="telephone" placeholder="+33 6 XX XX XX XX" required>
                            </div>
                            <div class="form-group">
                                <label for="ville">City of Residence <span class="text-brand-orange">*</span></label>
                                <input type="text" id="ville" name="ville" placeholder="E.g.: Paris, Lyon..." required>
                            </div>
                            <div class="form-actions form-actions-right">
                                <button type="button" class="btn btn-brand-orange-full btn-next">Next</button>
                            </div>
                        </div>
                        <div class="form-step" data-step="2">
                            <div class="form-group">
                                <label for="formation_souhaitee">Desired Program <span class="text-brand-orange">*</span></label>
                                <select id="formation_souhaitee" name="formation_souhaitee" required>
                                    <option value="" disabled selected>Select a program</option>
                                    <option value="BTS">BTS</option>
                                    <option value="Bachelor">Bachelor</option>
                                    <option value="Master">Master</option>
                                    <option value="Vocational Training">Vocational Training</option>
                                    <option value="Other">Other</option>
                                </select>
                            </div>
                            <div class="form-group">
                                <label for="formation_visee">Target Program Name <span class="text-brand-orange">*</span></label>
                                <input type="text" id="formation_visee" name="formation_visee" placeholder="E.g.: BTS MCO, Bachelor Marketing..." required>
                            </div>
                            <div class="form-group">
                                <label for="niveau_actuel">Current Education Level (Last degree obtained / current level) <span class="text-brand-orange">*</span></label>
                                <input type="text" id="niveau_actuel" name="niveau_actuel" placeholder="E.g.: High School Diploma, Bachelor's Degree..." required>
                            </div>
                            <div class="form-group">
                                <label for="situation_actuelle">Current Situation <span class="text-brand-orange">*</span></label>
                                <select id="situation_actuelle" name="situation_actuelle" required>
                                    <option value="" disabled selected>Select your situation</option>
                                    <option value="Student">Student</option>
                                    <option value="Employee">Employee</option>
                                    <option value="Job Seeker">Job Seeker</option>
                                    <option value="Career Transition">Career Transition</option>
                                    <option value="Other">Other</option>
                                </select>
                            </div>
                            <div class="form-actions">
                                <button type="button" class="btn btn-outline-dark btn-prev">Previous</button>
                                <button type="button" class="btn btn-brand-orange-full btn-next">Next</button>
                            </div>
                        </div>
                        <div class="form-step" data-step="3">
                            <div class="form-group">
                                <label for="rythme_souhaite">Desired Pace <span class="text-brand-orange">*</span></label>
                                <select id="rythme_souhaite" name="rythme_souhaite" required>
                                    <option value="" disabled selected>Select desired pace</option>
                                    <option value="Initial">Initial</option>
                                    <option value="Alternance">Work-study (Alternance)</option>
                                    <option value="Formation continue">Continuing Education</option>
                                    <option value="À distance / Hybride">Online / Hybrid</option>
                                </select>
                            </div>
                            <div class="form-group">
                                <label for="motivation">Candidate Motivation <span class="text-brand-orange">*</span></label>
                                <textarea id="motivation" name="motivation" placeholder="Briefly describe your project and objectives..." rows="4" required></textarea>
                            </div>
                            <div class="form-group checkbox-group">
                                <label class="custom-checkbox">
                                    <input type="checkbox" id="rgpd" name="rgpd" required>
                                    <span class="checkmark"></span>
                                    <span class="checkbox-text">I consent to Campus Superia collecting and using my data. <a href="#">[Privacy Policy]</a> <span class="text-brand-orange">*</span></span>
                                </label>
                            </div>
                            <div class="form-actions">
                                <button type="button" class="btn btn-outline-dark btn-prev">Previous</button>
                                <button type="submit" class="btn btn-brand-orange-full">Submit Application</button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </section>
</main>
<footer class="site-footer">
    <div class="footer-container">
        <div class="footer-col brand-col"><h3 class="footer-brand">Campus Superia</h3><div class="footer-bottom-brand"><img src="./assets/logo-icon.png" alt="Logo" class="footer-badge-img" style="height:30px;width:auto;"><p class="copyright">&copy; 2026, Campus Superia</p></div></div>
        <div class="footer-col"><h4 class="footer-heading">Admissions</h4><ul class="footer-links"><li><a href="admissions-en.html">Overview</a></li><li><a href="admissions-comment-candidater-en.html">How to Apply</a></li><li><a href="admissions-conditions-en.html">Requirements</a></li><li><a href="admissions-frais-en.html">Tuition &amp; Fees</a></li><li><a href="admissions-faq-en.html">FAQ</a></li></ul></div>
        <div class="footer-col"><h4 class="footer-heading">Follow Us</h4><ul class="footer-links"><li><a href="https://www.instagram.com/campus_superia" target="_blank">Instagram ↗</a></li><li><a href="https://www.tiktok.com/@campussuperia?_r=1&_t=ZN-96ISLCCJ6s2" target="_blank">TikTok ↗</a></li></ul></div>
        <div class="footer-col contact-col"><h4 class="footer-heading">Contact Us</h4><ul class="footer-links"><li><a href="mailto:contact@campussuperia.com">contact@campussuperia.com</a></li><li><a href="mailto:campussuperia@gmail.com">campussuperia@gmail.com</a></li><li><a href="tel:+33781547503">+33 781 547 503</a></li></ul><a href="#contact" class="btn btn-brand-orange-full footer-btn">Apply Now</a></div>
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
    fr_filename = filename.replace('-en.html', '.html')
    content = HEADER_TEMPLATE.format(
        title=title, meta_desc=meta, h1=h1, subtitle=subtitle,
        hero_img=hero_img, breadcrumb=bc(breadcrumb), body=body
    )
    content = content.replace('href="index.html" class="nav-lang"', f'href="{fr_filename}" class="nav-lang"')
    
    if 'partenariats' in filename:
        content = content.replace('Apply Now \u2192', 'Become a Partner \u2192')
        content = content.replace('href="admissions-en.html" class="btn btn-outline-light" style="border-radius:4px;">Overview</a>', 'href="mailto:contact@campussuperia.com" class="btn btn-outline-light" style="border-radius:4px;">Contact Us</a>')
        content = content.replace('<h2>Ready to<br>join us?</h2>', '<h2>Let&apos;s build<br>the future together</h2>')
        content = content.replace('Submit your application today. Our team will contact you within 72 hours.', 'Submit your partnership request today. Our team will contact you within 72 hours.')
        content = content.replace('Apply Now \u2197</a>', 'Become a Partner \u2197</a>')
        
        # Replace the admission form with the partnership form
        partenariats_form = """<form action="#" class="campus-form-card" id="multi-step-form">
                        <div class="form-progress"><span class="progress-text">Step <span id="current-step">1</span> of 3</span><div class="progress-bar-bg"><div class="progress-bar-fill" id="progress-fill"></div></div></div>
                        
                        <!-- Step 1: Organization & Contact -->
                        <div class="form-step form-step-active" data-step="1">
                            <div class="form-group">
                                <label for="structure">Organization name (Company / Association / Institution) <span class="text-brand-orange">*</span></label>
                                <input type="text" id="structure" name="structure" placeholder="E.g.: Company Ltd..." required>
                            </div>
                            <div class="form-group">
                                <label for="contact_nom">Key contact name, first name and job title <span class="text-brand-orange">*</span></label>
                                <input type="text" id="contact_nom" name="contact_nom" placeholder="E.g.: John Doe, HR Manager" required>
                            </div>
                            <div class="form-actions form-actions-right">
                                <button type="button" class="btn btn-brand-orange-full btn-next">Next</button>
                            </div>
                        </div>
                        
                        <!-- Step 2: Contact Details & Partnership Type -->
                        <div class="form-step" data-step="2">
                            <div class="form-group">
                                <label for="email">Email <span class="text-brand-orange">*</span></label>
                                <input type="email" id="email" name="email" placeholder="contact@company.com" required>
                            </div>
                            <div class="form-group">
                                <label for="telephone">Phone <span class="text-brand-orange">*</span></label>
                                <input type="tel" id="telephone" name="telephone" placeholder="+33 6 XX XX XX XX" required>
                            </div>
                            <div class="form-group">
                                <label>Type of partnership desired <span class="text-brand-orange">*</span></label>
                                <div class="checkbox-grid" style="display: grid; grid-template-columns: 1fr; gap: 0.75rem; margin-top: 0.5rem;">
                                    <label class="custom-checkbox">
                                        <input type="checkbox" name="type_partenariat" value="Training">
                                        <span class="checkmark"></span>
                                        <span class="checkbox-text">Training</span>
                                    </label>
                                    <label class="custom-checkbox">
                                        <input type="checkbox" name="type_partenariat" value="Exams / certifications">
                                        <span class="checkmark"></span>
                                        <span class="checkbox-text">Exams / certifications</span>
                                    </label>
                                    <label class="custom-checkbox">
                                        <input type="checkbox" name="type_partenariat" value="Work-study (Alternance)">
                                        <span class="checkmark"></span>
                                        <span class="checkbox-text">Work-study (Alternance)</span>
                                    </label>
                                    <label class="custom-checkbox">
                                        <input type="checkbox" name="type_partenariat" value="Public orientation">
                                        <span class="checkmark"></span>
                                        <span class="checkbox-text">Public orientation</span>
                                    </label>
                                    <label class="custom-checkbox">
                                        <input type="checkbox" name="type_partenariat" value="Events / lectures">
                                        <span class="checkmark"></span>
                                        <span class="checkbox-text">Events / lectures</span>
                                    </label>
                                    <label class="custom-checkbox">
                                        <input type="checkbox" name="type_partenariat" value="Other">
                                        <span class="checkmark"></span>
                                        <span class="checkbox-text">Other</span>
                                    </label>
                                </div>
                            </div>
                            <div class="form-actions">
                                <button type="button" class="btn btn-outline-dark btn-prev">Previous</button>
                                <button type="button" class="btn btn-brand-orange-full btn-next">Next</button>
                            </div>
                        </div>
                        
                        <!-- Step 3: Your Request & Availability -->
                        <div class="form-step" data-step="3">
                            <div class="form-group">
                                <label for="demande">Your request (Briefly describe the purpose of the desired partnership) <span class="text-brand-orange">*</span></label>
                                <textarea id="demande" name="demande" placeholder="Describe your partnership project..." rows="3" required></textarea>
                            </div>
                            <div class="form-group">
                                <label for="disponibilites">Availability for a discussion <span class="text-brand-orange">*</span></label>
                                <input type="text" id="disponibilites" name="disponibilites" placeholder="E.g.: Monday afternoon, Tuesday morning..." required>
                            </div>
                            <div class="form-group checkbox-group">
                                <label class="custom-checkbox">
                                    <input type="checkbox" id="rgpd" name="rgpd" required>
                                    <span class="checkmark"></span>
                                    <span class="checkbox-text">I consent to Campus Superia collecting and using my data. <a href="#">[Privacy Policy]</a> <span class="text-brand-orange">*</span></span>
                                </label>
                            </div>
                            <div class="form-actions">
                                <button type="button" class="btn btn-outline-dark btn-prev">Previous</button>
                                <button type="submit" class="btn btn-brand-orange-full">Submit Request</button>
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

base_bc = [('Home','index-en.html'), ('Admissions','admissions-en.html')]

# ── conditions ──────────────────────────────────────────────────────────────
make('admissions-conditions-en.html',
    "Admission Requirements",
    "Discover the prerequisites and accepted profiles to join Campus Superia's programs.",
    "Admission<br>Requirements",
    "Every profile is welcome. Discover the specific requirements for each program.",
    base_bc + [("Requirements", '')],
    './assets/scroll-actual-2.jpg',
    """
    <section class="requirements-section">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up">
                <span class="tag"><span class="dot"></span> Prerequisites</span>
                <h2 class="section-title">Requirements by Program</h2>
                <p class="section-subtitle" style="margin:.75rem auto 0;">Whether you are a beginner or an advanced learner, there is a program adapted to your profile.</p>
            </div>
            <div class="requirements-grid">
                <div class="req-card fade-up" style="--delay:0.1s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg></div><h3>FLE Programs (A2 to C1)</h3></div>
                    <ul class="req-list"><li>Be at least 16 years old at registration</li><li>Valid identity document</li><li>No minimum level — placement test included</li><li>Motivation and availability for classes</li><li>Access to a computer/tablet for online classes</li></ul>
                </div>
                <div class="req-card fade-up" style="--delay:0.2s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg></div><h3>BTS Program (Bac+2)</h3></div>
                    <ul class="req-list"><li>High school diploma or equivalent</li><li>Minimum B1 level in French</li><li>Motivation letter</li><li>Availability for work-study classes (3 days/week)</li><li>Valid residence permit or student visa</li></ul>
                </div>
                <div class="req-card fade-up" style="--delay:0.3s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg></div><h3>International Students</h3></div>
                    <ul class="req-list"><li>Student visa or valid residence permit (in-person)</li><li>Certified translation if necessary</li><li>Minimum A2 level recommended</li><li>Proof of resources or financial guarantor</li><li>Visa support on request</li></ul>
                </div>
                <div class="req-card fade-up" style="--delay:0.4s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg></div><h3>Online Classes (E-Learning)</h3></div>
                    <ul class="req-list"><li>Stable internet connection (5 Mbps minimum)</li><li>Recent computer, tablet or smartphone</li><li>Microphone and camera for live sessions</li><li>Active email address</li><li>Accessible worldwide</li></ul>
                </div>
            </div>
        </div>
    </section>
    <section class="admission-steps-section">
        <div class="container">
            <div class="section-header text-center fade-up"><span class="tag"><span class="dot"></span> Evaluation</span><h2 class="section-title">How we evaluate your application</h2></div>
            <div class="admission-steps-grid">
                <div class="step-card fade-up" style="--delay:0.1s"><div class="step-num">1</div><h3>Placement Test</h3><p>A 30-minute adaptive test covering reading comprehension, grammar and expression.</p></div>
                <div class="step-card fade-up" style="--delay:0.2s"><div class="step-num">2</div><h3>File Analysis</h3><p>Review of your diplomas, background and stated objectives.</p></div>
                <div class="step-card fade-up" style="--delay:0.3s"><div class="step-num">3</div><h3>Validation Interview</h3><p>A 20-minute call to confirm your oral level and finalize the program.</p></div>
                <div class="step-card fade-up" style="--delay:0.4s"><div class="step-num">4</div><h3>Decision and Integration</h3><p>Personalized admission letter with program, calendar and practical info.</p></div>
            </div>
        </div>
    </section>
    <section class="faq-section section-padding"><div class="container"><div class="section-header text-center mb-5 fade-up"><h2 class="section-title">Questions about requirements</h2></div><div class="faq-accordion"><div class="faq-item"><button class="faq-question">Can I apply without a high school diploma?<span class="faq-icon"></span></button><div class="faq-answer"><div class="faq-answer-content">For FLE programs, no diploma is required. A high school diploma is required only for BTS.</div></div></div><div class="faq-item"><button class="faq-question">Is there a minimum age?<span class="faq-icon"></span></button><div class="faq-answer"><div class="faq-answer-content">The minimum age is 16. For minors, signed parental consent is required.</div></div></div></div></div></section>
""")

# ── calendrier ──────────────────────────────────────────────────────────────
make('admissions-calendrier-en.html',
    "Application Calendar",
    "Check the key dates of the admission and intake sessions at Campus Superia.",
    "Application<br>Calendar",
    "Do not miss any deadline. View all admission sessions and plan your integration.",
    base_bc + [("Calendar", '')],
    './assets/scroll-actual-1.jpg',
    """
    <section class="timeline-events-section">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up">
                <span class="tag"><span class="dot"></span> Sessions 2025–2026</span>
                <h2 class="section-title">Key dates for applications</h2>
                <p class="section-subtitle" style="margin:.75rem auto 0;">Three entry sessions per year to integrate the program at the best time.</p>
            </div>
            <div class="timeline-events">
                <div class="timeline-event fade-up"><div class="event-date">June 15<br>2025</div><div class="event-info"><h3>Opening of applications — September 2025 Session</h3><p>Access to FLE (A2-C1) and work-study BTS programs.</p><span class="event-badge">Main session</span></div></div>
                <div class="timeline-event fade-up"><div class="event-date">August 31<br>2025</div><div class="event-info"><h3>Deadline — September 2025 Applications</h3><p>Last delay to submit a complete file.</p><span class="event-badge">Deadline</span></div></div>
                <div class="timeline-event fade-up"><div class="event-date">Sept. 8<br>2025</div><div class="event-info"><h3>September 2025 Intake</h3><p>Start of classes for all FLE and BTS programs.</p><span class="event-badge">Official intake</span></div></div>
                <div class="timeline-event fade-up"><div class="event-date">Nov. 1<br>2025</div><div class="event-info"><h3>Opening of applications — January 2026 Session</h3><p>Ideal session for candidates who could not apply in September.</p><span class="event-badge">New session</span></div></div>
                <div class="timeline-event fade-up"><div class="event-date">Dec. 20<br>2025</div><div class="event-info"><h3>Deadline — January 2026 Applications</h3><p>Last delay for the January intake.</p><span class="event-badge">Deadline</span></div></div>
                <div class="timeline-event fade-up"><div class="event-date">January 12<br>2026</div><div class="event-info"><h3>January 2026 Intake</h3><p>Start of classes for FLE programs (January session).</p><span class="event-badge">Intake</span></div></div>
                <div class="timeline-event fade-up"><div class="event-date">Feb. 21<br>2026</div><div class="event-info"><h3>Open Day — Neuilly Campus</h3><p>Come to meet the team and discover the programs for the April session.</p><span class="event-badge">Open Day</span></div></div>
                <div class="timeline-event fade-up"><div class="event-date">March 28<br>2026</div><div class="event-info"><h3>Deadline — April 2026 Applications</h3><p>Last submission delay for the April 2026 session.</p><span class="event-badge">Deadline</span></div></div>
            </div>
        </div>
    </section>
    <section class="admission-steps-section"><div class="container"><div class="section-header text-center fade-up"><span class="tag"><span class="dot"></span> Advice</span><h2 class="section-title">To apply in the best conditions</h2></div><div class="admission-steps-grid"><div class="step-card fade-up" style="--delay:0.1s"><div class="step-num">✓</div><h3>Anticipate your submission</h3><p>Submit your file at least 3 weeks before the deadline to complete any missing documents.</p></div><div class="step-card fade-up" style="--delay:0.2s"><div class="step-num">✓</div><h3>Take the test in advance</h3><p>The placement test can be taken as soon as the applications open.</p></div><div class="step-card fade-up" style="--delay:0.3s"><div class="step-num">✓</div><h3>Prepare your documents</h3><p>Scan in advance identity document, diploma and level certificates.</p></div><div class="step-card fade-up" style="--delay:0.4s"><div class="step-num">✓</div><h3>Contact us in case of doubt</h3><p>Our team answers your questions before you submit your file.</p></div></div></div></section>
""")

# ── frais ────────────────────────────────────────────────────────────────────
make('admissions-frais-en.html',
    "Tuition Fees",
    "Consulte tuition fees at Campus Superia: FLE, BTS, intensive courses and e-learning.",
    "Tuition<br>Fees",
    "Transparent pricing, no hidden fees. Discover the cost of each program.",
    base_bc + [("Tuition & Fees", '')],
    './assets/form-bg.jpg',
    """
    <section class="fees-section">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up"><span class="tag"><span class="dot"></span> Pricing</span><h2 class="section-title">Our rates by program</h2><p class="section-subtitle" style="margin:.75rem auto 0;">All fees shown are included in the price — no unexpected extra charges.</p></div>
            <div class="fees-table-wrap">
                <table class="fees-table">
                    <thead><tr><th>Program</th><th>Duration</th><th>Format</th><th>Rate</th><th>Included</th></tr></thead>
                    <tbody>
                        <tr><td><strong>General French A2–B1</strong></td><td>3 months</td><td>In-person / Online</td><td><strong>890 €</strong></td><td>Classes, materials, final test</td></tr>
                        <tr><td><strong>Advanced French B2–C1</strong></td><td>3 months</td><td>In-person / Online</td><td><strong>990 €</strong></td><td>Classes, materials, final test, progress interview</td></tr>
                        <tr><td><strong>Professional &amp; Business French</strong></td><td>2 months</td><td>Online</td><td><strong>750 €</strong></td><td>Classes, case studies, partial certification</td></tr>
                        <tr><td><strong>TEF / DELF Preparation</strong></td><td>6 weeks</td><td>In-person / Online</td><td><strong>590 €</strong></td><td>Intensive classes, past papers, exam simulation</td></tr>
                        <tr><td><strong>Eloquence &amp; Leadership</strong></td><td>6 weeks</td><td>Online</td><td><strong>650 €</strong></td><td>Workshops, individual coaching, recordings</td></tr>
                        <tr><td><strong>BTS — Work-Study (Bac+2)</strong></td><td>2 years</td><td>In-person</td><td><strong>On quote</strong></td><td>Classes, individual follow-up, assistance with company search</td></tr>
                        <tr><td><strong>Intensive Course (4 weeks)</strong></td><td>4 weeks</td><td>In-person / Online</td><td><strong>480 €</strong></td><td>20h/week, digital materials included</td></tr>
                    </tbody>
                </table>
            </div>
        </div>
    </section>
    <section class="features-section" style="padding-bottom:6rem;"><div class="section-header fade-up"><span class="tag"><span class="dot"></span> Included in the rate</span><h2 class="section-title">What is included<br>in each training</h2></div><div class="features-grid"><div class="feature-card fade-up" style="--delay:.1s"><div class="icon-placeholder"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg></div><h3>Pedagogical<br>materials</h3><p>Access to all digital course materials included, at no extra cost.</p></div><div class="feature-card fade-up" style="--delay:.2s"><div class="icon-placeholder"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div><h3>Individual<br>follow-up</h3><p>Mid-term assessment with your teacher to adjust the pace.</p></div><div class="feature-card fade-up" style="--delay:.3s"><div class="icon-placeholder"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 11 12 14 22 4"/></svg></div><h3>Access to the<br>platform</h3><p>E-learning platform available 24/7 to review and practice.</p></div><div class="feature-card fade-up" style="--delay:.4s"><div class="icon-placeholder"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg></div><h3>Placement<br>test</h3><p>Initial test and final test included to measure your progress.</p></div><div class="feature-card fade-up" style="--delay:.5s"><div class="icon-placeholder"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2"/></svg></div><h3>Live<br>lessons</h3><p>Live sessions with a teacher, in-person or video conference — included.</p></div><div class="feature-card fade-up" style="--delay:.6s"><div class="icon-placeholder"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg></div><h3>Training<br>certificate</h3><p>Official certificate given to each learner who has completed their program.</p></div></div></section>
    <section class="testimonial-banner split-50"><div class="testimonial-text"><p>"« The rates are honest and with no surprises. Everything was included as advertised. »"</p><span class="author">Lina D. — TEF Preparation Student</span></div><div class="banner-cta split-50"><a href="admissions-bourses-en.html" class="cta-block cta-orange">View scholarships</a><a href="admissions-comment-candidater-en.html" class="cta-block cta-beige">Apply</a></div></section>
""")

# ── bourses ──────────────────────────────────────────────────────────────────
make('admissions-bourses-en.html',
    "Scholarships & Financial Aid",
    "Discover scholarships and financing options available to finance your training at Campus Superia.",
    "Scholarships &<br>Financial Aid",
    "Campus Superia is committed to making training accessible to all. Discover our financial aid schemes.",
    base_bc + [("Scholarships & Aid", '')],
    './assets/scroll-actual-3.jpg',
    """
    <section class="scholarships-section">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up"><span class="tag"><span class="dot"></span> Financing</span><h2 class="section-title">Our financial aid schemes</h2><p class="section-subtitle" style="margin:.75rem auto 0;">Three types of support to make your training accessible, whatever your budget.</p></div>
            <div class="scholarship-cards-grid">
                <div class="scholarship-card fade-up" style="--delay:0.1s"><div class="sc-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg></div><span class="scholarship-badge">Merit</span><h3>Excellence Scholarship</h3><p>Awarded to candidates who demonstrated an exceptional level on the placement test. 20% to 30% reduction on fees.</p></div>
                <div class="scholarship-card fade-up" style="--delay:0.2s"><div class="sc-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div><span class="scholarship-badge">Social</span><h3>Need-based Scholarship</h3><p>Financial aid for candidates with limited resources. On file with proof of income.</p></div>
                <div class="scholarship-card fade-up" style="--delay:0.3s"><div class="sc-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg></div><span class="scholarship-badge">International</span><h3>International Aid</h3><p>Specific scheme for international candidates: reduction on fees and administrative support.</p></div>
            </div>
        </div>
    </section>
    <section class="admission-steps-section"><div class="container"><div class="section-header text-center fade-up"><span class="tag"><span class="dot"></span> How to apply</span><h2 class="section-title">How to obtain a scholarship</h2></div><div class="admission-steps-grid"><div class="step-card fade-up" style="--delay:0.1s"><div class="step-num">1</div><h3>Apply to the training</h3><p>First submit your application to the desired program and take the placement test.</p></div><div class="step-card fade-up" style="--delay:0.2s"><div class="step-num">2</div><h3>Request aid</h3><p>During your interview, mention your request for financial aid and the type of scholarship targeted.</p></div><div class="step-card fade-up" style="--delay:0.3s"><div class="step-num">3</div><h3>Submit the scholarship file</h3><p>Provide the necessary supporting documents within 15 days of your admission.</p></div><div class="step-card fade-up" style="--delay:0.4s"><div class="step-num">4</div><h3>Decision within 7 days</h3><p>The pedagogical committee evaluates your file and notifies you of the amount granted.</p></div></div></div></section>
    <section class="requirements-section"><div class="container"><div class="section-header text-center mb-5 fade-up"><h2 class="section-title">Flexible payment options</h2></div><div class="requirements-grid"><div class="req-card fade-up"><div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg></div><h3>Payment in installments</h3></div><ul class="req-list"><li>Payment in 2, 3 or 6 monthly installments at no extra cost</li><li>Available for training courses longer than 6 weeks</li><li>Secure automatic debit</li></ul></div><div class="req-card fade-up"><div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg></div><h3>CPF &amp; OPCO financing</h3></div><ul class="req-list"><li>Some programs eligible for the Compte Personnel de Formation (CPF)</li><li>Support possible by your OPCO</li><li>Our team supports you in the steps</li></ul></div></div></div></section>
""")

# ── international ─────────────────────────────────────────────────────────────
make('admissions-international-en.html',
    "International Students",
    "Specific information for foreign candidates wishing to join Campus Superia.",
    "International<br>Students",
    "Campus Superia welcomes learners from all over the world. We support you in every administrative step.",
    base_bc + [("International Students", '')],
    './assets/scroll-actual-3.jpg',
    """
    <section class="international-section">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up"><span class="tag"><span class="dot"></span> International welcome</span><h2 class="section-title">Your step-by-step support</h2><p class="section-subtitle" style="margin:.75rem auto 0;">From application to your first day of class, we guide you at every step.</p></div>
            <div class="international-grid">
                <div class="international-card fade-up" style="--delay:0.1s"><div class="ic-icon"><svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg></div><h3>Admission letter for visa</h3><p>We issue an official admission letter as soon as your application is validated, usable for your student visa application.</p></div>
                <div class="international-card fade-up" style="--delay:0.2s"><div class="ic-icon"><svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg></div><h3>Help with administrative steps</h3><p>Our team guides you for the long-stay visa application file: document list, deadlines and organizations.</p></div>
                <div class="international-card fade-up" style="--delay:0.3s"><div class="ic-icon"><svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg></div><h3>Housing advice</h3><p>List of reliable resources to find housing in Paris and Neuilly-sur-Seine: residences, agencies, platforms.</p></div>
                <div class="international-card fade-up" style="--delay:0.4s"><div class="ic-icon"><svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg></div><h3>Online courses available</h3><p>If your visa takes time, start your training online from your country of origin.</p></div>
                <div class="international-card fade-up" style="--delay:0.5s"><div class="ic-icon"><svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div><h3>Multicultural community</h3><p>Integrate a community of learners from more than 12 nationalities.</p></div>
                <div class="international-card fade-up" style="--delay:0.6s"><div class="ic-icon"><svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg></div><h3>International scholarship</h3><p>Specific financial aid scheme for international students. Inquire during your interview.</p></div>
            </div>
        </div>
    </section>
    <section class="requirements-section"><div class="container"><div class="section-header text-center mb-5 fade-up"><h2 class="section-title">Documents specific to foreign candidates</h2></div><div class="requirements-grid"><div class="req-card fade-up"><div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"/></svg></div><h3>For all non-EU candidates</h3></div><ul class="req-list"><li>Valid passport (minimum 6 months after the entry date)</li><li>Valid student visa or residence permit</li><li>Proof of resources (last 3 months or guarantor)</li><li>Certified translation of diplomas if requested</li><li>International health insurance or student Social Security</li></ul></div><div class="req-card fade-up"><div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/></svg></div><h3>For EU/EEA nationals</h3></div><ul class="req-list"><li>National identity card or valid passport</li><li>No visa required to reside and study in France</li><li>Registration at the town hall recommended</li><li>European health insurance card advised</li><li>Same admission conditions as French candidates</li></ul></div></div></div></section>
    <section class="stats-banner"><div class="container"><div class="stats-banner-grid"><div class="stat-item fade-up"><span class="stat-number">12+</span><span class="stat-label">Nationalities represented</span></div><div class="stat-item fade-up" style="--delay:.1s"><span class="stat-number">100%</span><span class="stat-label">Online processed applications</span></div><div class="stat-item fade-up" style="--delay:.2s"><span class="stat-number">5 days</span><span class="stat-label">Admission letter delay</span></div><div class="stat-item fade-up" style="--delay:.3s"><span class="stat-number">2 languages</span><span class="stat-label">French and English support</span></div></div></div></section>
""")

# ── transfert ─────────────────────────────────────────────────────────────────
make('admissions-transfert-en.html',
    "Admission by Transfer",
    "Join Campus Superia mid-course thanks to our simplified transfer procedure.",
    "Admission<br>by Transfer",
    "Already enrolled elsewhere or having started training? Join Campus Superia via our transfer procedure.",
    base_bc + [("Transfer", '')],
    './assets/scroll-actual-2.jpg',
    """
    <section class="section-padding" style="width:100%; background:var(--clr-white);">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up"><span class="tag"><span class="dot"></span> Transfer</span><h2 class="section-title">Join Campus Superia<br>mid-course</h2></div>
            <div class="transfer-content-grid">
                <div class="transfer-text">
                    <h3>Why choose Campus Superia by transfer?</h3>
                    <p>Do you want to change school, benefit from more personalized teaching or simply change environment? Our procedure is designed to minimize disruptions in your journey.</p>
                    <p>We evaluate your current level, recognize your achievements and integrate you into the most suitable class, without wasting time.</p>
                    <h3 style="margin-top:2rem;">Who can benefit from the transfer?</h3>
                    <p>Any learner who has followed at least 4 weeks of French lessons elsewhere can apply for admission by transfer. An individual evaluation is carried out.</p>
                </div>
                <div>
                    <ul class="transfer-checklist">
                        <li><span class="check-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></span>You have followed courses elsewhere and wish to change environment</li>
                        <li><span class="check-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></span>You have stopped training and wish to resume where you left off</li>
                        <li><span class="check-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></span>You are moving to France and have a certified level in your country</li>
                        <li><span class="check-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></span>You are moving from e-learning to in-person or vice versa</li>
                        <li><span class="check-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg></span>You wish to add a specialization to your current path</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>
    <section class="admission-steps-section"><div class="container"><div class="section-header text-center fade-up"><h2 class="section-title">Simplified transfer procedure</h2></div><div class="admission-steps-grid"><div class="step-card fade-up" style="--delay:0.1s"><div class="step-num">1</div><h3>Transfer request</h3><p>Contact our team indicating your current level and previous school.</p></div><div class="step-card fade-up" style="--delay:0.2s"><div class="step-num">2</div><h3>Evaluation of achievements</h3><p>Take our placement test. Provide any training report or level certificate.</p></div><div class="step-card fade-up" style="--delay:0.3s"><div class="step-num">3</div><h3>Integration proposal</h3><p>We propose a class and a calendar adapted to your validated level.</p></div><div class="step-card fade-up" style="--delay:0.4s"><div class="step-num">4</div><h3>Finalization and start</h3><p>Sign your contract and join your group. A tutor welcomes you during the first sessions.</p></div></div></div></section>
""")

# ── portes ouvertes ──────────────────────────────────────────────────────────
make('admissions-portes-ouvertes-en.html',
    "Open Days",
    "Participate in the open days of Campus Superia: visit our campus, meet the team.",
    "Open<br>Days",
    "Meet our teachers, visit our spaces and discover our programs in person. Free and open to all.",
    base_bc + [("Open Days", '')],
    './assets/scroll-actual-1.jpg',
    """
    <section class="events-section">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up"><span class="tag"><span class="dot"></span> Agenda 2025–2026</span><h2 class="section-title">Next Open Days</h2></div>
            <div class="events-cards-grid">
                <div class="event-card fade-up" style="--delay:0.1s">
                    <div class="event-card-header"><div class="event-date-block"><span class="event-day">14</span><span class="event-month">June</span></div><span class="event-card-title">Open Day — Neuilly Campus</span></div>
                    <div class="event-card-body"><p>Discover our classrooms, meet teachers and attend a mini demonstration session. Full program on site.</p><div class="event-meta"><span class="event-tag">Neuilly-sur-Seine</span><span class="event-tag">10am–5pm</span><span class="event-tag">Free</span></div></div>
                    <div class="event-card-footer"><a href="#contact">Register →</a></div>
                </div>
                <div class="event-card fade-up" style="--delay:0.2s">
                    <div class="event-card-header"><div class="event-date-block"><span class="event-day">18</span><span class="event-month">Oct.</span></div><span class="event-card-title">Virtual Open Day — E-Learning</span></div>
                    <div class="event-card-body"><p>Presentation of e-learning tools, live Q&A with teachers and demonstration of the platform.</p><div class="event-meta"><span class="event-tag">Online</span><span class="event-tag">2pm–4pm</span><span class="event-tag">Free</span></div></div>
                    <div class="event-card-footer"><a href="#contact">Register →</a></div>
                </div>
                <div class="event-card fade-up" style="--delay:0.3s">
                    <div class="event-card-header"><div class="event-date-block"><span class="event-day">21</span><span class="event-month">Feb.</span></div><span class="event-card-title">Open Day — Neuilly Campus</span></div>
                    <div class="event-card-body"><p>Meet current students and ask all your questions to our pedagogical team.</p><div class="event-meta"><span class="event-tag">Neuilly-sur-Seine</span><span class="event-tag">10am–4pm</span><span class="event-tag">Free</span></div></div>
                    <div class="event-card-footer"><a href="#contact">Register →</a></div>
                </div>
            </div>
        </div>
    </section>
    <section class="features-section" style="padding-bottom:6rem;"><div class="section-header fade-up"><span class="tag"><span class="dot"></span> On the program</span><h2 class="section-title">What awaits you<br>during an open day</h2></div><div class="features-grid"><div class="feature-card fade-up" style="--delay:.1s"><div class="icon-placeholder"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg></div><h3>Visits of premises</h3><p>Guided tour of our classrooms, collaborative spaces and work areas.</p></div><div class="feature-card fade-up" style="--delay:.2s"><div class="icon-placeholder"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div><h3>Meeting with<br>teachers</h3><p>Discuss directly methods and programs.</p></div><div class="feature-card fade-up" style="--delay:.3s"><div class="icon-placeholder"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2"/></svg></div><h3>Live course demo</h3><p>Free mini-session to discover our pedagogy in action.</p></div><div class="feature-card fade-up" style="--delay:.4s"><div class="icon-placeholder"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg></div><h3>Free placement test</h3><p>Take your level test on site and receive your result immediately.</p></div><div class="feature-card fade-up" style="--delay:.5s"><div class="icon-placeholder"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/></svg></div><h3>Brochures and<br>information</h3><p>Leave with all the details on programs, rates and intake dates.</p></div><div class="feature-card fade-up" style="--delay:.6s"><div class="icon-placeholder"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg></div><h3>Priority<br>registration</h3><p>Submit your application on site for priority processing of your file.</p></div></div></section>
""")

# ── campus ────────────────────────────────────────────────────────────────────
make('admissions-campus-en.html',
    "Our Campuses & Learning Formats",
    "Discover the campuses and formats available at Campus Superia: in-person at Paris Neuilly and 100% online.",
    "Our Campuses<br>&amp; Formats",
    "Two formats adapted to your lifestyle: a physical campus in Neuilly-sur-Seine and a global e-learning program.",
    base_bc + [("Campuses & Formats", '')],
    './assets/scroll-actual-3.jpg',
    """
    <section class="campus-cards-section">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up"><span class="tag"><span class="dot"></span> Our locations</span><h2 class="section-title">Choose your format</h2><p class="section-subtitle" style="margin:.75rem auto 0;">Two learning environments to adapt to your personal and professional constraints.</p></div>
            <div class="campus-cards-grid">
                <div class="campus-card fade-up" style="--delay:0.1s">
                    <div class="campus-card-img"><img src="./assets/scroll-actual-1.jpg" alt="Neuilly-sur-Seine Campus" onerror="this.src='./assets/hero.jpeg'"></div>
                    <div class="campus-card-body">
                        <h3>Neuilly-sur-Seine Campus</h3>
                        <span class="campus-location"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>99 Avenue Achille Peretti, 92200 Neuilly-sur-Seine</span>
                        <p>Our main campus in one of the most dynamic areas of the Paris region. Modern rooms, collaborative space and warm atmosphere.</p>
                        <div class="campus-facilities"><span class="facility-tag">Modern rooms</span><span class="facility-tag">High-speed Wi-Fi</span><span class="facility-tag">Collaborative space</span><span class="facility-tag">RER C access</span><span class="facility-tag">Library</span></div>
                    </div>
                </div>
                <div class="campus-card fade-up" style="--delay:0.2s">
                    <div class="campus-card-img"><img src="./assets/scroll-actual-3.jpg" alt="Online training" onerror="this.src='./assets/hero.jpeg'"></div>
                    <div class="campus-card-body">
                        <h3>E-Learning Training</h3>
                        <span class="campus-location"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>Accessible worldwide</span>
                        <p>Modern e-learning platform for live lessons, 24/7 access to materials and progression at your own pace.</p>
                        <div class="campus-facilities"><span class="facility-tag">Live lessons</span><span class="facility-tag">24/7 access</span><span class="facility-tag">Dedicated platform</span><span class="facility-tag">Technical support</span><span class="facility-tag">Unlimited resources</span></div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <section class="location-section section-padding" id="location" style="width:100%; background:var(--clr-bg-main);"><div class="container"><div class="section-header text-center mb-5 fade-up"><h2 class="section-title">Find <span>us</span></h2><p class="section-subtitle" style="margin:.75rem auto 0;">Our main campus is located in Neuilly-sur-Seine, 5 minutes from the RER C.</p></div><div class="map-container"><iframe src="https://www.google.com/maps?q=99+Avenue+Achille+Peretti,+92200+Neuilly-sur-Seine&hl=en&z=15&output=embed" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div></div></section>
""")

# ── témoignages ───────────────────────────────────────────────────────────────
make('admissions-temoignages-en.html',
    "Student Testimonials",
    "Discover the paths and testimonials of students who have joined and succeeded at Campus Superia.",
    "Student<br>Testimonials",
    "They chose Campus Superia and transformed their relationship with the French language. Discover their paths.",
    base_bc + [("Testimonials", '')],
    './assets/scroll-actual-2.jpg',
    """
    <section class="testimonials-section">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up"><span class="tag"><span class="dot"></span> Our learners testify</span><h2 class="section-title">They succeeded with<br>Campus Superia</h2></div>
            <div class="testimonial-cards-grid">
                <div class="testimonial-card fade-up" style="--delay:0.1s"><div class="testimonial-quote">Campus Superia allowed me to obtain my naturalization certificate after 6 months of intensive training. The personalized approach changed everything.</div><div class="testimonial-author"><div class="testimonial-avatar">A</div><div class="testimonial-author-info"><span class="author-name">Amina K.</span><span class="author-role">B2 Program → Naturalization</span></div></div></div>
                <div class="testimonial-card fade-up" style="--delay:0.2s"><div class="testimonial-quote">I was working full-time. Thanks to the online format, I was able to reconcile work and training without compromise.</div><div class="testimonial-author"><div class="testimonial-avatar">M</div><div class="testimonial-author-info"><span class="author-name">Mehdi T.</span><span class="author-role">Professional French</span></div></div></div>
                <div class="testimonial-card fade-up" style="--delay:0.3s"><div class="testimonial-quote">The teachers are very patient and professional. The classes are lively and interactive. I progressed from A2 to B2 in less than a year.</div><div class="testimonial-author"><div class="testimonial-avatar">S</div><div class="testimonial-author-info"><span class="author-name">Sofia L.</span><span class="author-role">General French B1/B2</span></div></div></div>
                <div class="testimonial-card fade-up" style="--delay:0.4s"><div class="testimonial-quote">An excellent school. The administrative support for my student visa was perfect. I highly recommend!</div><div class="testimonial-author"><div class="testimonial-avatar">A</div><div class="testimonial-author-info"><span class="author-name">Ali R.</span><span class="author-role">International Student</span></div></div></div>
            </div>
        </div>
    </section>
    <section class="stats-banner"><div class="container"><div class="stats-banner-grid"><div class="stat-item fade-up"><span class="stat-number">98%</span><span class="stat-label">Satisfaction rate</span></div><div class="stat-item fade-up" style="--delay:.1s"><span class="stat-number">1 800+</span><span class="stat-label">Graduates since opening</span></div><div class="stat-item fade-up" style="--delay:.2s"><span class="stat-number">87%</span><span class="stat-label">Progress by at least 2 levels</span></div><div class="stat-item fade-up" style="--delay:.3s"><span class="stat-number">92%</span><span class="stat-label">Recommend Campus Superia</span></div></div></div></section>
""")

# ── FAQ ───────────────────────────────────────────────────────────────────────
make('admissions-faq-en.html',
    "Admissions FAQ",
    "All the answers to your questions on admissions, programs, fees and life at Campus Superia.",
    "Admissions<br>FAQ",
    "Find here the answers to the most frequent questions about our admission process and our programs.",
    base_bc + [("FAQ", '')],
    './assets/scroll-actual-1.jpg',
    """
    <section class="faq-section section-padding" style="width:100%;"><div class="container"><div class="section-header text-center mb-5 fade-up"><span class="tag"><span class="dot"></span> Application</span><h2 class="section-title">Questions on application</h2></div><div class="faq-accordion"><div class="faq-item"><button class="faq-question">Are there fees to submit an application?<span class="faq-icon"></span></button><div class="faq-answer"><div class="faq-answer-content">No. The application is entirely free. No fees are requested before your formal admission.</div></div></div><div class="faq-item"><button class="faq-question">How long does it take to get a reply?<span class="faq-icon"></span></button><div class="faq-answer"><div class="faq-answer-content">We commit to answer within 72 business hours after receiving your complete file.</div></div></div><div class="faq-item"><button class="faq-question">What happens if my file is incomplete?<span class="faq-icon"></span></button><div class="faq-answer"><div class="faq-answer-content">Our team will contact you. You will have 15 days to complete your file without losing your place.</div></div></div></div></div></section>
    <section class="faq-section section-padding" style="width:100%; background:var(--clr-white);"><div class="container"><div class="section-header text-center mb-5 fade-up"><span class="tag"><span class="dot"></span> Programs</span><h2 class="section-title">Questions on programs</h2></div><div class="faq-accordion"><div class="faq-item"><button class="faq-question">What is the duration of a typical training?<span class="faq-icon"></span></button><div class="faq-answer"><div class="faq-answer-content">FLE programs generally last 3 months. Intensive formats last 4 to 6 weeks. BTS is a 2-year work-study training.</div></div></div><div class="faq-item"><button class="faq-question">How many hours of class per week?<span class="faq-icon"></span></button><div class="faq-answer"><div class="faq-answer-content">Standard programs include 8 to 12 hours per week. Intensive formats reach 20 hours per week.</div></div></div><div class="faq-item"><button class="faq-question">Are classes available in replay?<span class="faq-icon"></span></button><div class="faq-answer"><div class="faq-answer-content">Online classes are recorded and available in replay for 30 days.</div></div></div></div></div></section>
    <section class="faq-section section-padding" style="width:100%;"><div class="container"><div class="section-header text-center mb-5 fade-up"><span class="tag"><span class="dot"></span> Finances</span><h2 class="section-title">Questions on fees and financing</h2></div><div class="faq-accordion"><div class="faq-item"><button class="faq-question">Can we pay in installments?<span class="faq-icon"></span></button><div class="faq-answer"><div class="faq-answer-content">Yes. Payment in 2, 3 or 6 monthly installments at no extra cost for training courses longer than 6 weeks.</div></div></div><div class="faq-item"><button class="faq-question">Are training courses eligible for CPF?<span class="faq-icon"></span></button><div class="faq-answer"><div class="faq-answer-content">Some programs are eligible for CPF. Contact us to verify the eligibility of your training.</div></div></div><div class="faq-item"><button class="faq-question">What do the tuition fees cover?<span class="faq-icon"></span></button><div class="faq-answer"><div class="faq-answer-content">Fees include: classes, access to the e-learning platform, digital pedagogical materials, tests and training certificate.</div></div></div></div></div></section>
    <div style="text-align:center; padding:3rem 1rem; background:var(--clr-white);"><p style="font-size:1.1rem;color:var(--clr-text-mid);margin-bottom:1.5rem;">Haven't found your answer?</p><a href="admissions-contact-en.html" class="btn btn-brand-orange" style="border-radius:4px;display:inline-flex;">Contact our team →</a></div>
""")

# ── contact ───────────────────────────────────────────────────────────────────
make('admissions-contact-en.html',
    "Contact Admissions",
    "Contact the admissions team of Campus Superia. Phone, email, form — we reply within 72 hours.",
    "Contact<br>our team",
    "A question about your application? Our team is at your disposal by phone, email or form.",
    base_bc + [("Contact", '')],
    './assets/scroll-actual-2.jpg',
    """
    <section class="contact-info-section">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up"><span class="tag"><span class="dot"></span> Coordinates</span><h2 class="section-title">Our contact details</h2><p class="section-subtitle" style="margin:.75rem auto 0;">Several ways to reach us according to your preferences.</p></div>
            <div class="contact-info-grid">
                <div class="contact-info-card fade-up" style="--delay:0.1s"><div class="contact-info-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 13a19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 3.6 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg></div><h4>Phone</h4><a href="tel:+33781547503">+33 781 547 503</a><p>Mon–Fri : 9am–6pm</p></div>
                <div class="contact-info-card fade-up" style="--delay:0.2s"><div class="contact-info-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg></div><h4>Email</h4><a href="mailto:contact@campussuperia.com">contact@campussuperia.com</a><br><a href="mailto:campussuperia@gmail.com">campussuperia@gmail.com</a><p>Response within 72h</p></div>
                <div class="contact-info-card fade-up" style="--delay:0.3s"><div class="contact-info-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></div><h4>Campus</h4><p>99 Avenue Achille Peretti<br>92200 Neuilly-sur-Seine</p></div>
                <div class="contact-info-card fade-up" style="--delay:0.4s"><div class="contact-info-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg></div><h4>Working Hours</h4><p>Mon–Fri : 9am–6pm<br>Sat : 10am–1pm<br>Sun : Closed</p></div>
            </div>
        </div>
    </section>
    <section class="location-section section-padding" id="location" style="width:100%; background:var(--clr-white);"><div class="container"><div class="section-header text-center mb-5 fade-up"><h2 class="section-title">Find <span>us</span></h2></div><div class="map-container"><iframe src="https://www.google.com/maps?q=99+Avenue+Achille+Peretti,+92200+Neuilly-sur-Seine&hl=en&z=15&output=embed" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div></div></section>
""")

# ── comment candidater ────────────────────────────────────────────────────────
make('admissions-comment-candidater-en.html',
    "How to Apply",
    "Discover all the steps to submit your application to Campus Superia and integrate our programs.",
    "How to<br>Apply?",
    "A clear, step-by-step process. From your first inquiry to your first class session.",
    base_bc + [("How to Apply", '')],
    './assets/scroll-actual-1.jpg',
    """
    <section class="section-padding" style="width:100%; background:var(--clr-bg-main);">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up">
                <span class="tag"><span class="dot"></span> Your Journey</span>
                <h2 class="section-title">Your application in 5 steps</h2>
                <p class="section-subtitle" style="margin:.75rem auto 0;">Each step is designed to be simple, fast, and entirely doable from home.</p>
            </div>
            <div class="story-timeline">
                <div class="timeline-line-bg"></div>
                <div class="timeline-line-fill" id="timeline-fill"></div>
                <div class="story-step left">
                    <div class="step-number">1</div>
                    <div class="step-content">
                        <h3>Fill out the online form</h3>
                        <p>Access our secure application form, fill in your personal details, your current level, and your training goals. It takes less than 5 minutes.</p>
                    </div>
                </div>
                <div class="story-step right">
                    <div class="step-number">2</div>
                    <div class="step-content">
                        <h3>Attach your documents</h3>
                        <p>Upload your supporting documents: copy of ID, latest diploma, and language certificate if available. All documents can be scanned or photographed.</p>
                    </div>
                </div>
                <div class="story-step left">
                    <div class="step-number">3</div>
                    <div class="step-content">
                        <h3>Take the placement test</h3>
                        <p>A link will be sent to you by email to take our online placement test. This 30-minute test helps us validate your level and guide you to the most suitable program.</p>
                    </div>
                </div>
                <div class="story-step right">
                    <div class="step-number">4</div>
                    <div class="step-content">
                        <h3>Interview with an advisor</h3>
                        <p>A pedagogical advisor will contact you within 72 hours for a 20-minute interview to validate your project, answer questions, and confirm your program.</p>
                    </div>
                </div>
                <div class="story-step left">
                    <div class="step-number">5</div>
                    <div class="step-content">
                        <h3>Confirmation and integration</h3>
                        <p>You receive your admission letter by email. Finalize registration, select payment options, and prepare for intake. An integration kit will be sent before start.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <section class="requirements-section">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up">
                <span class="tag"><span class="dot"></span> Complete File</span>
                <h2 class="section-title">Required Documents to Apply</h2>
            </div>
            <div class="requirements-grid">
                <div class="req-card fade-up" style="--delay:0.1s">
                    <div class="req-card-header">
                        <div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg></div>
                        <h3>Mandatory Documents</h3>
                    </div>
                    <ul class="req-list">
                        <li>Copy (front/back) of your ID (passport or national ID card)</li>
                        <li>Latest diploma or school certificate</li>
                        <li>Recent passport-sized photo (digital format accepted)</li>
                        <li>Completed application form</li>
                        <li>Parental consent for minors under 18 years old</li>
                    </ul>
                </div>
                <div class="req-card fade-up" style="--delay:0.2s">
                    <div class="req-card-header">
                        <div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg></div>
                        <h3>Supporting Documents (optional)</h3>
                    </div>
                    <ul class="req-list">
                        <li>Language level certificate (DELF, TEF, Alliance Française, etc.)</li>
                        <li>CV or summary of professional experience</li>
                        <li>Cover letter (recommended for BTS applications)</li>
                        <li>Any proof of current professional activity</li>
                        <li>For internationals: valid visa or residence permit</li>
                    </ul>
                </div>
                <div class="req-card fade-up" style="--delay:0.3s">
                    <div class="req-card-header">
                        <div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg></div>
                        <h3>What we do NOT ask for</h3>
                    </div>
                    <ul class="req-list">
                        <li>No application or registration file fees</li>
                        <li>No selective or eliminatory entry exams</li>
                        <li>No mandatory recommendation letters</li>
                        <li>No nationality restrictions</li>
                        <li>No minimum entry level required (except for BTS)</li>
                    </ul>
                </div>
                <div class="req-card fade-up" style="--delay:0.4s">
                    <div class="req-card-header">
                        <div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg></div>
                        <h3>Accepted Formats</h3>
                    </div>
                    <ul class="req-list">
                        <li>PDF (recommended), JPG, PNG for scans and photos</li>
                        <li>Files up to 5 MB per document</li>
                        <li>Documents in French, English or Arabic accepted</li>
                        <li>Certified translation required for some countries (contact us)</li>
                        <li>100% online submission, no postal mail required</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>
    <section class="testimonial-banner split-50"><div class="testimonial-text"><p>« I completed my application in 10 minutes from my phone. A week later, I had my admission letter. »</p><span class="author">Mehdi T. — Student in French B1</span></div><div class="banner-cta split-50"><a href="#contact" class="cta-block cta-orange">Apply Now</a><a href="admissions-conditions-en.html" class="cta-block cta-beige">View Requirements</a></div></section>
""")

# ── admissions BTS ───────────────────────────────────────────────────────────
make('admissions-bts-en.html',
    "BTS Admission",
    "Discover the admission procedure for the BTS work-study program at Campus Superia. Enrollment, selection, and company placement.",
    "BTS Admission<br>Procedure (Bac+2)",
    "Join a 100% work-study state-certified program. Fully funded with personalized placement coaching.",
    base_bc + [("BTS", '')],
    './assets/scroll-actual-2.jpg',
    """
    <section class="requirements-section">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up">
                <span class="tag"><span class="dot"></span> Key Points</span>
                <h2 class="section-title">Why Choose the BTS Work-Study Program?</h2>
                <p class="section-subtitle" style="margin:.75rem auto 0;">A highly professionalizing program to quickly enter the workforce with solid hands-on experience.</p>
            </div>
            <div class="requirements-grid">
                <div class="req-card fade-up" style="--delay:0.1s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg></div><h3>State-Certified Degree</h3></div>
                    <ul class="req-list">
                        <li>RNCP Level 5 Certification</li>
                        <li>100% recognized by the State and corporate recruiters</li>
                        <li>Continuous assessment and a national final exam</li>
                    </ul>
                </div>
                <div class="req-card fade-up" style="--delay:0.2s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg></div><h3>100% Funded Tuition</h3></div>
                    <ul class="req-list">
                        <li>Zero cost for the student</li>
                        <li>Tuition fees are entirely funded by the host company's OPCO</li>
                        <li>Earn a regular monthly salary (based on a percentage of the SMIC)</li>
                    </ul>
                </div>
                <div class="req-card fade-up" style="--delay:0.3s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div><h3>Guaranteed Placement Support</h3></div>
                    <ul class="req-list">
                        <li>Personalized resume workshops and mock interview coaching</li>
                        <li>Direct connection to our exclusive network of partner companies</li>
                        <li>Dedicated guidance until you sign your contract</li>
                    </ul>
                </div>
                <div class="req-card fade-up" style="--delay:0.4s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a10 10 0 0 0-7.38 16.75L12 22l7.38-5.25A10 10 0 0 0 12 2z"/></svg></div><h3>Flexible Work-Study Pace</h3></div>
                    <ul class="req-list">
                        <li>2 days of theoretical classes on campus</li>
                        <li>3 days of professional practice within the company</li>
                        <li>Perfect balance to build real-world skills</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <section class="admission-steps-section">
        <div class="container">
            <div class="section-header text-center fade-up">
                <span class="tag"><span class="dot"></span> Steps</span>
                <h2 class="section-title">Our 4-Step Admission Process</h2>
            </div>
            <div class="admission-steps-grid">
                <div class="step-card fade-up" style="--delay:0.1s"><div class="step-num">1</div><h3>Online Application</h3><p>Complete the online application form with your transcripts, CV, and cover letter.</p></div>
                <div class="step-card fade-up" style="--delay:0.2s"><div class="step-num">2</div><h3>Interview</h3><p>Attend a 20-minute individual motivation interview to evaluate your professional goals.</p></div>
                <div class="step-card fade-up" style="--delay:0.3s"><div class="step-num">3</div><h3>Admissibility</h3><p>Get the admission committee's decision regarding your eligibility within 48 hours.</p></div>
                <div class="step-card fade-up" style="--delay:0.4s"><div class="step-num">4</div><h3>Placement Match</h3><p>Access our customized coaching to secure your work-study contract with a company.</p></div>
            </div>
        </div>
    </section>

    <section class="faq-section section-padding" style="width:100%; background:var(--clr-white);">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up">
                <h2 class="section-title">Frequently Asked Questions</h2>
            </div>
            <div class="faq-accordion">
                <div class="faq-item">
                    <button class="faq-question">Who pays for my BTS tuition fees?<span class="faq-icon"></span></button>
                    <div class="faq-answer"><div class="faq-answer-content">Your tuition fees are 100% covered by the funding body (OPCO) of your host company. You do not have to pay any application or tuition fees yourself.</div></div>
                </div>
                <div class="faq-item">
                    <button class="faq-question">What are the prerequisites to enroll?<span class="faq-icon"></span></button>
                    <div class="faq-answer"><div class="faq-answer-content">You must hold a high school diploma (Baccalauréat or equivalent) and have a sufficient level of French (minimum B1) to follow the classes.</div></div>
                </div>
            </div>
        </div>
    </section>

    <section class="stats-banner">
        <div class="container">
            <div class="stats-banner-grid">
                <div class="stat-item fade-up"><span class="stat-number">98%</span><span class="stat-label">Student satisfaction</span></div>
                <div class="stat-item fade-up" style="--delay:.1s"><span class="stat-number">100%</span><span class="stat-label">Tuition funded</span></div>
                <div class="stat-item fade-up" style="--delay:.2s"><span class="stat-number">48h</span><span class="stat-label">Jury response time</span></div>
                <div class="stat-item fade-up" style="--delay:.3s"><span class="stat-number">2 years</span><span class="stat-label">Program duration</span></div>
            </div>
        </div>
    </section>
    """
)

# ── admissions Bachelor ──────────────────────────────────────────────────────
make('admissions-bachelor-en.html',
    "Bachelor Admission",
    "Admission procedure for the Bachelor programs at Campus Superia. State-certified 3-year curriculum with multiple specializations.",
    "Bachelor Admission<br>Procedure (Bac+3)",
    "State-certified 3-year program. Shape your professional future with our specialized tracks and work-study options.",
    base_bc + [("Bachelor", '')],
    './assets/scroll-actual-1.jpg',
    """
    <section class="requirements-section">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up">
                <span class="tag"><span class="dot"></span> Key Points</span>
                <h2 class="section-title">Why Choose the Bachelor Program?</h2>
                <p class="section-subtitle" style="margin:.75rem auto 0;">A professionalizing program with global opportunities, blending academic excellence with real-world business experience.</p>
            </div>
            <div class="requirements-grid">
                <div class="req-card fade-up" style="--delay:0.1s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg></div><h3>RNCP Recognition</h3></div>
                    <ul class="req-list">
                        <li>State-certified Level 6 degree</li>
                        <li>Structured 3-year path (post-high school, entry in 2nd or 3rd year)</li>
                        <li>ECTS credits awarded for further study or international mobility</li>
                    </ul>
                </div>
                <div class="req-card fade-up" style="--delay:0.2s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg></div><h3>3rd Year Work-Study</h3></div>
                    <ul class="req-list">
                        <li>First two years under student status to master core fundamentals</li>
                        <li>Third year in a work-study format for quick professional entry</li>
                        <li>Full tuition funding and support for your 3rd year placement</li>
                    </ul>
                </div>
                <div class="req-card fade-up" style="--delay:0.3s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg></div><h3>Specialized Tracks</h3></div>
                    <ul class="req-list">
                        <li>Targeted fields: Marketing, Communication, Business Development, Management</li>
                        <li>Practical teaching tailored to actual company requirements</li>
                        <li>Real-world corporate projects and team challenges</li>
                    </ul>
                </div>
                <div class="req-card fade-up" style="--delay:0.4s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div><h3>High Employment Rate</h3></div>
                    <ul class="req-list">
                        <li>90% of graduates employed within 6 months of graduation</li>
                        <li>Active alumni network and strong corporate partnerships</li>
                        <li>Individualized career guidance and coaching for every student</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <section class="admission-steps-section">
        <div class="container">
            <div class="section-header text-center fade-up">
                <span class="tag"><span class="dot"></span> Steps</span>
                <h2 class="section-title">Our 4-Step Bachelor Admission Process</h2>
            </div>
            <div class="admission-steps-grid">
                <div class="step-card fade-up" style="--delay:0.1s"><div class="step-num">1</div><h3>Online Submission</h3><p>Submit your academic records, CV, and motivation letter through our online portal.</p></div>
                <div class="step-card fade-up" style="--delay:0.2s"><div class="step-num">2</div><h3>Jury Review</h3><p>Our academic board carefully evaluates your transcripts, recommendations, and achievements.</p></div>
                <div class="step-card fade-up" style="--delay:0.3s"><div class="step-num">3</div><h3>Evaluations</h3><p>Complete a short written test (English and general knowledge) and a 20-minute motivation interview.</p></div>
                <div class="step-card fade-up" style="--delay:0.4s"><div class="step-num">4</div><h3>Final Results</h3><p>The final admission decision is sent directly to you within 5 working days.</p></div>
            </div>
        </div>
    </section>

    <section class="faq-section section-padding" style="width:100%; background:var(--clr-white);">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up">
                <h2 class="section-title">Frequently Asked Questions</h2>
            </div>
            <div class="faq-accordion">
                <div class="faq-item">
                    <button class="faq-question">Can I enter directly into the 2nd or 3rd year?<span class="faq-icon"></span></button>
                    <div class="faq-answer"><div class="faq-answer-content">Yes. We accept parallel applications: entry into the 2nd year after 1 year of higher education, or entry into the 3rd year after a validated Bac+2 degree (BTS, DUT, or 120 equivalent ECTS credits).</div></div>
                </div>
                <div class="faq-item">
                    <button class="faq-question">How does the 3rd year work-study pace work?<span class="faq-icon"></span></button>
                    <div class="faq-answer"><div class="faq-answer-content">The schedule generally consists of 1 week of classes on campus per month, and the other 3 weeks working at your host company.</div></div>
                </div>
            </div>
        </div>
    </section>

    <section class="stats-banner">
        <div class="container">
            <div class="stats-banner-grid">
                <div class="stat-item fade-up"><span class="stat-number">90%</span><span class="stat-label">Employed within 6 months</span></div>
                <div class="stat-item fade-up" style="--delay:.1s"><span class="stat-number">3 years</span><span class="stat-label">Program duration</span></div>
                <div class="stat-item fade-up" style="--delay:.2s"><span class="stat-number">5 days</span><span class="stat-label">Jury decision delay</span></div>
                <div class="stat-item fade-up" style="--delay:.3s"><span class="stat-number">RNCP 6</span><span class="stat-label">State-certified degree</span></div>
            </div>
        </div>
    </section>
    """
)

# ── admissions BBA ───────────────────────────────────────────────────────────
make('admissions-bba-en.html',
    "BBA Admission",
    "Discover the admission procedure for the Bachelor of Business Administration (BBA) at Campus Superia. A 4-year bilingual program.",
    "BBA Admission<br>Procedure (Bac+4)",
    "Bachelor of Business Administration (Bac+4). Go global with a bilingual business curriculum and study abroad semesters.",
    base_bc + [("BBA", '')],
    './assets/scroll-actual-3.jpg',
    """
    <section class="requirements-section">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up">
                <span class="tag"><span class="dot"></span> Global Curriculum</span>
                <h2 class="section-title">Why Choose the BBA Program?</h2>
                <p class="section-subtitle" style="margin:.75rem auto 0;">An elite 4-year bilingual program focused on global commerce, financial markets, and academic mobility.</p>
            </div>
            <div class="requirements-grid">
                <div class="req-card fade-up" style="--delay:0.1s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg></div><h3>Bilingual Path</h3></div>
                    <ul class="req-list">
                        <li>50% to 100% of courses taught in English depending on the year</li>
                        <li>Total language immersion preparing you for global corporate careers</li>
                        <li>International faculty composed of industry leaders and researchers</li>
                    </ul>
                </div>
                <div class="req-card fade-up" style="--delay:0.2s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg></div><h3>International Mobility</h3></div>
                    <ul class="req-list">
                        <li>Study abroad semesters at one of our partner universities</li>
                        <li>Opportunities for annual international corporate internships</li>
                        <li>Dual-degree options with top-ranked global universities</li>
                    </ul>
                </div>
                <div class="req-card fade-up" style="--delay:0.3s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/></svg></div><h3>Bac+4 Standard</h3></div>
                    <ul class="req-list">
                        <li>RNCP Level 6 State Certified Degree</li>
                        <li>Direct path to prestigious Master or MSc programs worldwide</li>
                        <li>240 ECTS credits earned throughout the program</li>
                    </ul>
                </div>
                <div class="req-card fade-up" style="--delay:0.4s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg></div><h3>Specialization Majors</h3></div>
                    <ul class="req-list">
                        <li>Choose a major in International Finance or Global Project Management</li>
                        <li>Curriculum focused on entrepreneurship and global data analytics</li>
                        <li>Final year corporate immersion to launch your career</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <section class="admission-steps-section">
        <div class="container">
            <div class="section-header text-center fade-up">
                <span class="tag"><span class="dot"></span> Two Tracks</span>
                <h2 class="section-title">Two Admission Routes</h2>
            </div>
            <div class="admission-steps-grid">
                <div class="step-card fade-up" style="--delay:0.1s"><div class="step-num">1</div><h3>Post-High School</h3><p>For current high school seniors, submit wishes through Parcoursup, followed by written and oral tests.</p></div>
                <div class="step-card fade-up" style="--delay:0.2s"><div class="step-num">2</div><h3>Parallel Admission</h3><p>For students with 1 or 2 years of higher education, apply directly on transcripts and attend a bilingual interview.</p></div>
                <div class="step-card fade-up" style="--delay:0.3s"><div class="step-num">3</div><h3>Interview</h3><p>Pass a 30-minute bilingual oral evaluation to test motivation and English proficiency.</p></div>
                <div class="step-card fade-up" style="--delay:0.4s"><div class="step-num">4</div><h3>Enrollment</h3><p>Finalize registration upon submission of your high school diploma or previous transcripts.</p></div>
            </div>
        </div>
    </section>

    <section class="faq-section section-padding" style="width:100%; background:var(--clr-white);">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up">
                <h2 class="section-title">Frequently Asked Questions</h2>
            </div>
            <div class="faq-accordion">
                <div class="faq-item">
                    <button class="faq-question">Do I need to be completely bilingual to apply?<span class="faq-icon"></span></button>
                    <div class="faq-answer"><div class="faq-answer-content">No. Although many classes are taught in English, we accept candidates with intermediate skills (minimum B2 level is recommended). Support classes are provided to help you improve.</div></div>
                </div>
                <div class="faq-item">
                    <button class="faq-question">Which countries can I go to for my semesters abroad?<span class="faq-icon"></span></button>
                    <div class="faq-answer"><div class="faq-answer-content">We have university partnerships across Europe, North America (USA, Canada), and Asia. Our international office will help you plan your travel and coursework.</div></div>
                </div>
            </div>
        </div>
    </section>

    <section class="stats-banner">
        <div class="container">
            <div class="stats-banner-grid">
                <div class="stat-item fade-up"><span class="stat-number">4 years</span><span class="stat-label">Program duration</span></div>
                <div class="stat-item fade-up" style="--delay:.1s"><span class="stat-number">50%+</span><span class="stat-label">Courses in English</span></div>
                <div class="stat-item fade-up" style="--delay:.2s"><span class="stat-number">240</span><span class="stat-label">ECTS credits awarded</span></div>
                <div class="stat-item fade-up" style="--delay:.3s"><span class="stat-number">100%</span><span class="stat-label">Online applications</span></div>
            </div>
        </div>
    </section>
    """
)

# ── admissions MSc ───────────────────────────────────────────────────────────
make('admissions-msc-en.html',
    "MSc Admission",
    "Discover the admission procedure for the Master of Science (MSc) programs at Campus Superia. A high-level 5-year work-study degree.",
    "MSc Admission<br>Procedure (Bac+5)",
    "Master of Science (Bac+5) of excellence. Build high-level industry expertise, access our corporate network, and study in a work-study format.",
    base_bc + [("MSc", '')],
    './assets/hero.jpeg',
    """
    <section class="requirements-section">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up">
                <span class="tag"><span class="dot"></span> Master Level</span>
                <h2 class="section-title">Why Choose the Master of Science Program?</h2>
                <p class="section-subtitle" style="margin:.75rem auto 0;">An elite specialized curriculum designed with industry experts to prepare you for direct entry into management roles.</p>
            </div>
            <div class="requirements-grid">
                <div class="req-card fade-up" style="--delay:0.1s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg></div><h3>Expertise &amp; VAE</h3></div>
                    <ul class="req-list">
                        <li>State-certified Level 7 Degree (Bac+5 equivalence)</li>
                        <li>Specializations tailored to match market needs: Corporate Finance, Digital Marketing &amp; AI, HR</li>
                        <li>Also accessible via VAE (Validation of Acquired Experience)</li>
                    </ul>
                </div>
                <div class="req-card fade-up" style="--delay:0.2s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg></div><h3>Work-Study Format</h3></div>
                    <ul class="req-list">
                        <li>Can be completed entirely as a work-study (Apprentissage)</li>
                        <li>Optimized schedule designed for maximum integration in companies</li>
                        <li>100% of tuition is covered by the company; student receives a salary</li>
                    </ul>
                </div>
                <div class="req-card fade-up" style="--delay:0.3s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg></div><h3>Partner Corporate Network</h3></div>
                    <ul class="req-list">
                        <li>Exclusive access to partner companies for placement and hiring</li>
                        <li>Regular hiring forums and job events hosted directly on campus</li>
                        <li>Outstanding employment rate for graduating work-study students</li>
                    </ul>
                </div>
                <div class="req-card fade-up" style="--delay:0.4s">
                    <div class="req-card-header"><div class="req-card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div><h3>Professional Lecturers</h3></div>
                    <ul class="req-list">
                        <li>Classes taught by active industry executives and department heads</li>
                        <li>Active pedagogy: real-world case studies, simulations, and business games</li>
                        <li>High average starting salary for cadres/management-level graduates</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <section class="admission-steps-section">
        <div class="container">
            <div class="section-header text-center fade-up">
                <span class="tag"><span class="dot"></span> 5 Steps</span>
                <h2 class="section-title">MSc Recruitment Steps</h2>
            </div>
            <div class="admission-steps-grid">
                <div class="step-card fade-up" style="--delay:0.1s"><div class="step-num">1</div><h3>Application</h3><p>Submit your full academic record (validated Bac+3/4), CV, and chosen specialization online.</p></div>
                <div class="step-card fade-up" style="--delay:0.2s"><div class="step-num">2</div><h3>Jury Review</h3><p>The pedagogical jury evaluates your file and validates admissibility within 48 hours.</p></div>
                <div class="step-card fade-up" style="--delay:0.3s"><div class="step-num">3</div><h3>Oral Exam</h3><p>Participate in a 20-minute individual motivation interview focused on your career goals.</p></div>
                <div class="step-card fade-up" style="--delay:0.4s"><div class="step-num">4</div><h3>Decision</h3><p>Get the final admission decision within 5 working days.</p></div>
                <div class="step-card fade-up" style="--delay:0.5s"><div class="step-num">5</div><h3>Placement</h3><p>Gain access to our job workshops and partner job offers to secure your work-study contract.</p></div>
            </div>
        </div>
    </section>

    <section class="faq-section section-padding" style="width:100%; background:var(--clr-white);">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up">
                <h2 class="section-title">Frequently Asked Questions</h2>
            </div>
            <div class="faq-accordion">
                <div class="faq-item">
                    <button class="faq-question">Who is eligible to apply for the MSc?<span class="faq-icon"></span></button>
                    <div class="faq-answer"><div class="faq-answer-content">MSc programs are open to students holding a Bac+3 degree (Bachelor, Licence, or 180 ECTS credits) for entry into MSc year 1, or a Bac+4 degree (Master 1 or 240 ECTS credits) for direct entry into MSc year 2.</div></div>
                </div>
                <div class="faq-item">
                    <button class="faq-question">What are the job opportunities after the MSc?<span class="faq-icon"></span></button>
                    <div class="faq-answer"><div class="faq-answer-content">Our graduates step into management roles across sectors: Corporate Controller, Financial Analyst, Digital Project Manager, Marketing Manager, HR Director, and more.</div></div>
                </div>
            </div>
        </div>
    </section>

    <section class="stats-banner">
        <div class="container">
            <div class="stats-banner-grid">
                <div class="stat-item fade-up"><span class="stat-number">97%</span><span class="stat-label">Employed within 6 months</span></div>
                <div class="stat-item fade-up" style="--delay:.1s"><span class="stat-number">10 000</span><span class="stat-label">Partner companies</span></div>
                <div class="stat-item fade-up" style="--delay:.2s"><span class="stat-number">5 days</span><span class="stat-label">Jury decision delay</span></div>
                <div class="stat-item fade-up" style="--delay:.3s"><span class="stat-number">Bac+5</span><span class="stat-label">RNCP Level 7 Degree</span></div>
            </div>
        </div>
    </section>
    """
)

PARTNERSHIPS_BODY = """
    <!-- Why become a partner -->
    <section class="why-partner-section section-padding">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up">
                <span class="tag"><span class="dot"></span> Why Collaborate</span>
                <h2 class="section-title">Why Become a Partner?</h2>
                <p class="section-subtitle" style="margin:.75rem auto 0; max-width:600px;">Associate your organization with Campus Superia to boost your projects, recruit top-tier profiles, and shape tomorrow's education.</p>
            </div>
            <div class="why-partner-grid">
                <div class="why-card fade-up" style="--delay: 0.1s">
                    <div class="why-card-icon">
                        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="8.5" cy="7" r="4"></circle><line x1="20" y1="8" x2="20" y2="14"></line><line x1="23" y1="11" x2="17" y2="11"></line></svg>
                    </div>
                    <h3>Recruit Our Talents</h3>
                    <p>Gain priority access to our qualified students seeking internships, work-study programs, or their first job.</p>
                </div>
                <div class="why-card fade-up" style="--delay: 0.2s">
                    <div class="why-card-icon">
                        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"></path><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path></svg>
                    </div>
                    <h3>Co-build Programs</h3>
                    <p>Participate in updating our academic programs to adapt them directly to your industry requirements.</p>
                </div>
                <div class="why-card fade-up" style="--delay: 0.3s">
                    <div class="why-card-icon">
                        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 10a6 6 0 0 0-12 0c0 7 3 9 3 9h6s3-2 3-9"></path><line x1="12" y1="22" x2="12" y2="23"></line><path d="M9 22h6"></path></svg>
                    </div>
                    <h3>Drive Innovation</h3>
                    <p>Collaborate on hackathons, student projects, or applied research to solve your complex challenges.</p>
                </div>
                <div class="why-card fade-up" style="--delay: 0.4s">
                    <div class="why-card-icon">
                        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="7"></circle><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline></svg>
                    </div>
                    <h3>Promote Your Brand</h3>
                    <p>Strengthen your employer brand and associate your image with a modern, innovative academic hub.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Partnership categories -->
    <section class="partner-categories-section section-padding">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up">
                <span class="tag"><span class="dot"></span> Categories</span>
                <h2 class="section-title">Partnership Categories</h2>
                <p class="section-subtitle" style="margin:.75rem auto 0; max-width:600px;">Tailored collaboration formats matching your organization's profile and goals.</p>
            </div>
            <div class="categories-grid">
                <div class="category-card fade-up" style="--delay: 0.1s">
                    <h3>Companies</h3>
                    <p>From start-ups to multinational corporations, integrate our students into your teams and share your business expertise during our regular events.</p>
                    <ul class="category-list">
                        <li>Internship & work-study offers</li>
                        <li>Recruitment forums</li>
                        <li>Professional masterclasses</li>
                        <li>Real-world study projects</li>
                    </ul>
                </div>
                <div class="category-card fade-up" style="--delay: 0.2s">
                    <h3>Academic Institutions</h3>
                    <p>National or international higher education institutions, let's develop student exchange pathways, dual degrees, and joint research.</p>
                    <ul class="category-list">
                        <li>Dual-degrees & pathways</li>
                        <li>International exchanges</li>
                        <li>Applied research projects</li>
                        <li>Research seminars</li>
                    </ul>
                </div>
                <div class="category-card fade-up" style="--delay: 0.3s">
                    <h3>Public & Private Organizations</h3>
                    <p>Communities, government bodies, foundations, or associations, let's co-design high social and economic impact collective initiatives.</p>
                    <ul class="category-list">
                        <li>Event sponsoring</li>
                        <li>Thematic conferences</li>
                        <li>Inclusion programs</li>
                        <li>Public utility hackathons</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- Collaboration process -->
    <section class="collab-timeline-section section-padding">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up">
                <span class="tag"><span class="dot"></span> Process</span>
                <h2 class="section-title">The Collaboration Process</h2>
                <p class="section-subtitle" style="margin:.75rem auto 0; max-width:600px;">A structured 4-step approach for a high-performing and sustainable partnership.</p>
            </div>
            <div class="timeline-container">
                <div class="timeline-step fade-up" style="--delay: 0.1s">
                    <div class="timeline-node">1</div>
                    <h3>First Exchange</h3>
                    <p>Initial meeting to identify your objectives, recruitment needs, and define the ideal scope.</p>
                </div>
                <div class="timeline-step fade-up" style="--delay: 0.2s">
                    <div class="timeline-node">2</div>
                    <h3>Co-build Partnership</h3>
                    <p>Design a customized action plan defining terms, schedule, resources, and performance metrics.</p>
                </div>
                <div class="timeline-step fade-up" style="--delay: 0.3s">
                    <div class="timeline-node">3</div>
                    <h3>Implementation</h3>
                    <p>Launch initiatives: publishing job offers, scheduling workshops, welcoming students, or starting projects.</p>
                </div>
                <div class="timeline-step fade-up" style="--delay: 0.4s">
                    <div class="timeline-node">4</div>
                    <h3>Monitoring & Evolution</h3>
                    <p>Regular reviews, impact assessment, and annual adjustments to support your growth over the long term.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Collaboration opportunities -->
    <section class="opportunities-section section-padding">
        <div class="container">
            <div class="section-header text-center mb-5 fade-up">
                <span class="tag"><span class="dot"></span> Opportunities</span>
                <h2 class="section-title">Our Collaboration Opportunities</h2>
                <p class="section-subtitle" style="margin:.75rem auto 0; max-width:600px;">Explore the various action points to actively engage with our community.</p>
            </div>
            <div class="opp-grid">
                <div class="opp-card fade-up" style="--delay: 0.05s">
                    <div class="opp-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
                    </div>
                    <h3>Recruitment</h3>
                    <p>Gain priority access to our graduating students.</p>
                </div>
                <div class="opp-card fade-up" style="--delay: 0.1s">
                    <div class="opp-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>
                    </div>
                    <h3>Internships</h3>
                    <p>Host our students for 2 to 6-month missions.</p>
                </div>
                <div class="opp-card fade-up" style="--delay: 0.15s">
                    <div class="opp-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>
                    </div>
                    <h3>Work-study</h3>
                    <p>Integrate students throughout the year in apprenticeship contracts.</p>
                </div>
                <div class="opp-card fade-up" style="--delay: 0.2s">
                    <div class="opp-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
                    </div>
                    <h3>Conferences</h3>
                    <p>Present on key industry and topical subjects.</p>
                </div>
                <div class="opp-card fade-up" style="--delay: 0.25s">
                    <div class="opp-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
                    </div>
                    <h3>Masterclass</h3>
                    <p>Lead technical workshops or interactive training sessions.</p>
                </div>
                <div class="opp-card fade-up" style="--delay: 0.3s">
                    <div class="opp-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
                    </div>
                    <h3>Mentoring</h3>
                    <p>Personally support a student in their professional project.</p>
                </div>
                <div class="opp-card fade-up" style="--delay: 0.35s">
                    <div class="opp-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg>
                    </div>
                    <h3>Student Projects</h3>
                    <p>Submit a concrete challenge to be solved by our students.</p>
                </div>
                <div class="opp-card fade-up" style="--delay: 0.4s">
                    <div class="opp-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
                    </div>
                    <h3>Research</h3>
                    <p>Co-develop innovations through thesis work or research projects.</p>
                </div>
                <div class="opp-card fade-up" style="--delay: 0.45s">
                    <div class="opp-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="4 17 10 11 4 5"></polyline><line x1="12" y1="19" x2="20" y2="19"></line></svg>
                    </div>
                    <h3>Hackathons</h3>
                    <p>Propose and sponsor a 48h innovation marathon.</p>
                </div>
                <div class="opp-card fade-up" style="--delay: 0.5s">
                    <div class="opp-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
                    </div>
                    <h3>Sponsorship</h3>
                    <p>Support our events of excellence or student scholarships.</p>
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
                    <span class="stat-label">Active partners</span>
                </div>
                <div class="stat-item fade-up" style="--delay:.1s">
                    <span class="stat-number stat-number-anim" data-target="95" data-suffix="%">0%</span>
                    <span class="stat-label">Employment rate</span>
                </div>
                <div class="stat-item fade-up" style="--delay:.2s">
                    <span class="stat-number stat-number-anim" data-target="300" data-suffix="+">0+</span>
                    <span class="stat-label">Internship & work-study offers / yr</span>
                </div>
                <div class="stat-item fade-up" style="--delay:.3s">
                    <span class="stat-number stat-number-anim" data-target="15" data-suffix="+">0+</span>
                    <span class="stat-label">Student projects completed</span>
                </div>
            </div>
        </div>
    </section>

    <!-- Partners section -->
    <section class="logo-carousel-container">
        <div class="section-header text-center mb-5 fade-up">
            <span class="tag"><span class="dot"></span> Network</span>
            <h2 class="section-title">They Trust Us</h2>
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
                <h2 class="section-title">Frequently Asked Questions on Partnerships</h2>
            </div>
            <div class="faq-accordion">
                <div class="faq-item">
                    <button class="faq-question">How can my organization become a partner of Campus Superia?<span class="faq-icon"></span></button>
                    <div class="faq-answer"><div class="faq-answer-content">For any information request, we invite you to fill out the form below or to contact us directly by email. An orientation advisor or a corporate relations representative will contact you shortly to arrange an initial personalized discussion.</div></div>
                </div>
                <div class="faq-item">
                    <button class="faq-question">What are the costs associated with a partnership?<span class="faq-icon"></span></button>
                    <div class="faq-answer"><div class="faq-answer-content">Signing a partnership framework agreement is free. However, certain specific projects, such as customized hackathons, dedicated research actions, or sponsorship operations, may be subject to specific funding.</div></div>
                </div>
                <div class="faq-item">
                    <button class="faq-question">Can I post internship or work-study job offers?<span class="faq-icon"></span></button>
                    <div class="faq-answer"><div class="faq-answer-content">Absolutely. Our students preparing for a BTS, a Bachelor, or an MSc regularly seek internships as well as work-study contracts. We make our internal platform available to you in order to distribute your offers to our candidates.</div></div>
                </div>
                <div class="faq-item">
                    <button class="faq-question">How are student group projects monitored?<span class="faq-icon"></span></button>
                    <div class="faq-answer"><div class="faq-answer-content">Each student project, whether a group project or a hackathon, is supervised by a tutor-teacher from Campus Superia as well as a representative within your organization, to guarantee the quality of the deliverables.</div></div>
                </div>
            </div>
        </div>
    </section>
"""

make('partenariats-en.html',
    "Become a Partner",
    "Discover partnership opportunities with Campus Superia. Recruit our talents, co-construct training programs, and drive innovation.",
    "Building the future<br>together",
    "Join Campus Superia's partner network and collaborate with a committed institution to train tomorrow's leaders.",
    [('Home', 'index-en.html'), ('Partnerships', '')],
    './assets/scroll-actual-3.jpg',
    PARTNERSHIPS_BODY
)

print("\n✅ All 17 English pages generated successfully!")

