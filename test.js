/**
 * test.js - Logic for the Campus Superia Test de Positionnement
 */

document.addEventListener('DOMContentLoaded', () => {

    // --- State & DOM Elements ---
    let currentMainStep = 'intro'; // intro, active, result
    let currentQuizSection = 1;
    const totalQuizSections = 3;

    const introStep = document.getElementById('test-intro-step');
    const activeStep = document.getElementById('test-active-step');
    const resultStep = document.getElementById('test-result-step');

    const candidatForm = document.getElementById('candidat-form');
    const progressBar = document.getElementById('main-progress-bar');
    const progressText = document.getElementById('progress-percentage');
    const sectionNameText = document.getElementById('current-section-name');

    // --- Grammar Quiz Data (Partie 2) ---
    const grammarQuestions = [
        { q: "1. Je ______ au centre tous les matins.", options: ["viens", "vient", "venir"] },
        { q: "2. Hier, nous ______ votre dossier.", options: ["reçoit", "avons reçu", "recevrons"] },
        { q: "3. Pouvez-vous ______ ce formulaire, s'il vous plaît ?", options: ["compléter", "complétez", "complété"] },
        { q: "4. Si vous avez une question, vous pouvez ______ par e-mail.", options: ["nous contacter", "contactons", "contacté"] },
        { q: "5. Le rendez-vous est confirmé, ______ le candidat doit être présent à 9 h 50.", options: ["car", "donc", "mais"] },
        { q: "6. Je travaille à Campus Superia ______ deux mois.", options: ["depuis", "pendant", "dans"] },
        { q: "7. ______ possible de reporter le rendez-vous ?", options: ["Est-il", "A-t-il", "Fait-il"] },
        { q: "8. Nous vous remercions ______ votre retour.", options: ["pour", "à", "dans"] },
        { q: "9. Le candidat est arrivé en retard, ______ il a pu passer le test.", options: ["mais", "parce que", "puisque"] },
        { q: "10. Je voudrais ______ des informations sur la formation.", options: ["avoir", "eu", "avais"] }
    ];

    const grammarTransformations = [
        "11. Transformez en question polie : “Envoyez-moi le programme.”",
        "12. Complétez : “Je me permets de vous écrire ______ obtenir des renseignements.”",
        "13. Reformulez dans un registre professionnel : “J’ai pas compris.”",
        "14. Complétez : “Nous restons à votre disposition ______ toute information complémentaire.”",
        "15. Écrivez une phrase avec “cependant” dans un contexte professionnel."
    ];

    // --- 1. Form Submission (Start Test) ---
    if (candidatForm) {
        candidatForm.addEventListener('submit', (e) => {
            e.preventDefault();
            // In a real app, save candidate info here
            
            // Transition to Test Active Step
            introStep.classList.remove('active');
            document.body.classList.add('test-in-progress');
            setTimeout(() => {
                introStep.style.display = 'none';
                activeStep.style.display = 'block';
                // Small delay to allow display:block to apply before adding opacity class
                setTimeout(() => {
                    activeStep.classList.add('active');
                    updateProgress();
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                }, 50);
            }, 500); // Wait for fade out
        });
    }

    // Scroll directly to form when clicking top "Commencer le test"
    const startBtn = document.getElementById('start-btn');
    if (startBtn) {
        startBtn.addEventListener('click', () => {
            document.querySelector('.test-form-card').scrollIntoView({ behavior: 'smooth' });
        });
    }

    // --- 2. Render Grammar Section (Partie 2) ---
    const mcqContainer = document.getElementById('mcq-container');
    if (mcqContainer) {
        // Render MCQs
        grammarQuestions.forEach((item, index) => {
            const mcqHtml = `
                <div class="mcq-item">
                    <div class="mcq-question">${item.q}</div>
                    <div class="mcq-options">
                        ${item.options.map((opt, i) => `
                            <label class="mcq-option" data-qindex="${index}" data-optindex="${i}">
                                <input type="radio" name="g_q${index}" value="${opt}">
                                <span>${opt}</span>
                            </label>
                        `).join('')}
                    </div>
                </div>
            `;
            mcqContainer.insertAdjacentHTML('beforeend', mcqHtml);
        });

        // Render Transform questions
        grammarTransformations.forEach((q, index) => {
            const transHtml = `
                <div class="q-item">
                    <label>${q}</label>
                    <input type="text" class="q-input" name="t_q${index}" placeholder="Votre réponse...">
                </div>
            `;
            mcqContainer.insertAdjacentHTML('beforeend', transHtml);
        });

        // Add interactive class toggling for radio cards
        document.querySelectorAll('.mcq-option').forEach(option => {
            option.addEventListener('click', function() {
                // Remove selected from siblings
                const siblings = this.parentElement.querySelectorAll('.mcq-option');
                siblings.forEach(s => s.classList.remove('selected'));
                // Add selected to this
                this.classList.add('selected');
                // The actual radio input will be checked automatically because of the label wrapping
            });
        });
    }

    // --- 3. Navigation Between Quiz Sections ---
    const updateProgress = () => {
        const percentage = ((currentQuizSection - 1) / totalQuizSections) * 100;
        progressBar.style.width = `${percentage}%`;
        progressText.textContent = `${Math.round(percentage)}%`;

        const sectionNames = [
            "1. Compréhension écrite et lexique",
            "2. Grammaire et structures",
            "3. Production écrite"
        ];
        sectionNameText.textContent = sectionNames[currentQuizSection - 1];
    };

    const navigateSection = (direction) => {
        const currentSectionEl = document.getElementById(`quiz-section-${currentQuizSection}`);
        currentSectionEl.classList.remove('active');
        
        setTimeout(() => {
            currentSectionEl.style.display = 'none';
            currentQuizSection += direction;
            
            const nextSectionEl = document.getElementById(`quiz-section-${currentQuizSection}`);
            nextSectionEl.style.display = 'block';
            
            setTimeout(() => {
                nextSectionEl.classList.add('active');
                updateProgress();
                window.scrollTo({ top: 0, behavior: 'smooth' });
            }, 50);
        }, 300); // Wait for fade out
    };

    document.querySelectorAll('.next-section-btn').forEach(btn => {
        btn.addEventListener('click', () => navigateSection(1));
    });

    document.querySelectorAll('.prev-section-btn').forEach(btn => {
        btn.addEventListener('click', () => navigateSection(-1));
    });

    // --- 4. Production Écrite (Word Counter) ---
    const editor = document.getElementById('writing-editor');
    const wordCountSpan = document.getElementById('word-count');
    const lineCountSpan = document.getElementById('line-count');
    const autoSaveStatus = document.querySelector('.auto-save-status');
    let autoSaveTimer;

    if (editor) {
        editor.addEventListener('input', () => {
            const text = editor.value;
            // Word count
            const words = text.trim() ? text.trim().split(/\s+/).length : 0;
            wordCountSpan.textContent = words;
            // Line count (approximated by newlines)
            const lines = text ? text.split(/\r\n|\r|\n/).length : 0;
            lineCountSpan.textContent = lines;

            // Simulate auto-save
            autoSaveStatus.textContent = "Enregistrement...";
            clearTimeout(autoSaveTimer);
            autoSaveTimer = setTimeout(() => {
                autoSaveStatus.textContent = "Enregistré à l'instant";
            }, 1000);
        });
    }

    // --- 5. Interaction Orale (Removed) ---

    // --- 6. Final Submission (Dashboard Transition) ---
    // --- 6. Dynamic Scoring & Diagnostic Dashboard Submission ---
    const submitBtn = document.getElementById('submit-test-btn');
    if (submitBtn) {
        submitBtn.addEventListener('click', () => {
            // Fill final progress bar
            progressBar.style.width = `100%`;
            progressText.textContent = `100%`;

            // --- Dynamic Grading Logic ---
            
            // Partie 1 : Compréhension écrite (20 pts)
            // 9 open-text questions (q1-q9). Length > 3 chars gets 2 pts. Max 18.
            // +2 bonus points if all questions are answered substantially.
            let part1Score = 0;
            let allPart1Answered = true;
            for (let i = 1; i <= 9; i++) {
                const qInput = document.querySelector(`input[name="q${i}"]`);
                const val = qInput ? qInput.value.trim() : '';
                if (val.length > 3) {
                    part1Score += 2;
                } else {
                    allPart1Answered = false;
                }
            }
            if (allPart1Answered && part1Score === 18) {
                part1Score = 20;
            }

            // Partie 2 : Grammaire et structures (20 pts)
            // MCQ (10 pts)
            const mcqAnswers = ["viens", "avons reçu", "compléter", "nous contacter", "donc", "depuis", "Est-il", "pour", "mais", "avoir"];
            let mcqScore = 0;
            mcqAnswers.forEach((ans, idx) => {
                const checkedRadio = document.querySelector(`input[name="g_q${idx}"]:checked`);
                if (checkedRadio && checkedRadio.value === ans) {
                    mcqScore += 1;
                }
            });

            // transformations (10 pts) - 2 pts per correct match
            let transScore = 0;

            // Q11: "Transformez en question polie : “Envoyez-moi le programme.”"
            const q11 = (document.querySelector('input[name="t_q0"]')?.value || '').trim().toLowerCase();
            if (q11.includes('pourriez') || q11.includes('pouvez') || q11.includes('plait') || q11.includes('plaît') || q11.includes('veuillez') || q11.includes('possible') || q11.includes('auriez')) {
                transScore += 2;
            }

            // Q12: "Je me permets de vous écrire ______ obtenir des renseignements."
            const q12 = (document.querySelector('input[name="t_q1"]')?.value || '').trim().toLowerCase();
            if (q12 === 'pour' || q12.includes('afin de') || q12.includes("afin d'") || q12.includes('afin d’') || q12.includes('dans le but de')) {
                transScore += 2;
            }

            // Q13: "J'ai pas compris." (professionnel)
            const q13 = (document.querySelector('input[name="t_q2"]')?.value || '').trim().toLowerCase();
            if (q13.includes('compris') || q13.includes('comprend') || q13.includes('saisi') || q13.includes('échappé') || q13.includes('echappe') || q13.includes('saisir') || q13.includes('clarifier') || q13.includes('reformuler') || q13.includes('répéter') || q13.includes('repeter') || q13.includes('entendu') || q13.includes('suivi')) {
                transScore += 2;
            }

            // Q14: "Nous restons à votre disposition ______ toute information complémentaire."
            const q14 = (document.querySelector('input[name="t_q3"]')?.value || '').trim().toLowerCase();
            if (q14 === 'pour' || q14.includes('en cas de') || q14.includes('si vous')) {
                transScore += 2;
            }

            // Q15: phrase avec "cependant"
            const q15 = (document.querySelector('input[name="t_q4"]')?.value || '').trim().toLowerCase();
            if (q15.includes('cependant') && q15.length > 12) {
                transScore += 2;
            }

            const part2Score = mcqScore + transScore;

            // Partie 3 : Production écrite (20 pts)
            const essayText = (document.getElementById('writing-editor')?.value || '').trim();
            const words = essayText ? essayText.split(/\s+/).length : 0;
            let part3Score = 0;
            if (words >= 80) {
                part3Score = 20;
            } else if (words >= 50) {
                part3Score = 15;
            } else if (words >= 30) {
                part3Score = 10;
            } else if (words >= 10) {
                part3Score = 5;
            } else {
                part3Score = 0;
            }

            const totalScore = part1Score + part2Score + part3Score;

            // --- Update Results Dashboard UI ---
            document.getElementById('score-part1').textContent = `${part1Score} / 20`;
            document.getElementById('score-part2').textContent = `${part2Score} / 20`;
            document.getElementById('score-part3').textContent = `${part3Score} / 20`;
            document.getElementById('score-total').textContent = `${totalScore} / 60`;

            // CEFR Level Classification
            let level = 'A1';
            if (totalScore >= 55) {
                level = 'C1';
            } else if (totalScore >= 43) {
                level = 'B2';
            } else if (totalScore >= 31) {
                level = 'B1';
            } else if (totalScore >= 16) {
                level = 'A2';
            } else {
                level = 'A1';
            }

            // Toggle active badge
            const badges = ['a1', 'a2', 'b1', 'b2', 'c1'];
            badges.forEach(b => {
                const badgeEl = document.getElementById(`badge-${b}`);
                if (badgeEl) {
                    if (b === level.toLowerCase()) {
                        badgeEl.classList.add('active-level');
                    } else {
                        badgeEl.classList.remove('active-level');
                    }
                }
            });

            // Tailored recommendations container update
            const recoContainer = document.getElementById('reco-container');
            if (recoContainer) {
                let recoHtml = '';
                if (level === 'A1') {
                    recoHtml = `
                        <div class="reco-card recommended">
                            <h4>Parcours Pré-intermédiaire (A2)</h4>
                            <p>Recommandé pour acquérir les bases essentielles du français de manière structurée et méthodique.</p>
                        </div>
                        <div class="reco-card">
                            <h4>Atelier Flash : Grammaire & Vocabulaire</h4>
                            <p>Renforcez vos bases fondamentales en grammaire et structures pour progresser rapidement.</p>
                        </div>
                    `;
                } else if (level === 'A2') {
                    recoHtml = `
                        <div class="reco-card recommended">
                            <h4>Parcours Intermédiaire (B1)</h4>
                            <p>Idéal pour consolider vos acquis et acquérir une autonomie de communication écrite et orale.</p>
                        </div>
                        <div class="reco-card">
                            <h4>Français Professionnel Élémentaire</h4>
                            <p>Validez vos premières compétences linguistiques appliquées au monde de l'entreprise.</p>
                        </div>
                    `;
                } else if (level === 'B1') {
                    recoHtml = `
                        <div class="reco-card recommended">
                            <h4>Parcours Avancé (B2)</h4>
                            <p>Développez une expression fluide, apprenez à argumenter et à vous intégrer avec aisance.</p>
                        </div>
                        <div class="reco-card">
                            <h4>Préparation DFP B1 (Français Professionnel)</h4>
                            <p>Un parcours diplômant idéal pour valoriser votre profil auprès des recruteurs francophones.</p>
                        </div>
                    `;
                } else if (level === 'B2') {
                    recoHtml = `
                        <div class="reco-card recommended">
                            <h4>Parcours Autonome (C1)</h4>
                            <p>Affinez votre maîtrise de la langue pour traiter de sujets complexes avec précision et aisance.</p>
                        </div>
                        <div class="reco-card">
                            <h4>Management & Négociation DFP B2</h4>
                            <p>Perfectionnez vos compétences de communication stratégique en contexte d'affaires exigeant.</p>
                        </div>
                    `;
                } else { // C1
                    recoHtml = `
                        <div class="reco-card recommended">
                            <h4>Parcours Maîtrise & Perfectionnement (C2)</h4>
                            <p>Atteignez une expression parfaite, fluide et nuancée, adaptée aux plus hautes exigences académiques ou professionnelles.</p>
                        </div>
                        <div class="reco-card">
                            <h4>Prise de Parole en Public & Leadership</h4>
                            <p>Développez votre éloquence, votre impact à l'oral et votre charisme en langue française.</p>
                        </div>
                    `;
                }
                recoContainer.innerHTML = recoHtml;
            }

            // Transition to Result Dashboard
            activeStep.classList.remove('active');
            setTimeout(() => {
                activeStep.style.display = 'none';
                resultStep.style.display = 'block';
                
                setTimeout(() => {
                    resultStep.classList.add('active');
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                }, 50);
            }, 500);
        });
    }
});
