/**
 * test-en.js - Logic for the Campus Superia English Placement Test
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

    // --- English Grammar Quiz Data (Part 2) ---
    const grammarQuestions = [
        { q: "1. I ______ to the campus every morning.", options: ["come", "comes", "coming"] },
        { q: "2. Yesterday, we ______ your complete application file.", options: ["receive", "received", "will receive"] },
        { q: "3. Could you please ______ this registration form?", options: ["complete", "completing", "completed"] },
        { q: "4. If you have any questions, you can ______ us by email.", options: ["contact", "contacts", "contacted"] },
        { q: "5. The appointment is confirmed, ______ the candidate must arrive at 9:50 AM.", options: ["so", "but", "because"] },
        { q: "6. I have been studying at Campus Superia ______ two months.", options: ["for", "since", "during"] },
        { q: "7. ______ it be possible to reschedule the interview?", options: ["Would", "Should", "Will"] },
        { q: "8. We appreciate ______ your prompt feedback.", options: ["receiving", "to receive", "received"] },
        { q: "9. The candidate arrived late, ______ he was still allowed to take the test.", options: ["but", "because", "since"] },
        { q: "10. I would like ______ more information about the training program.", options: ["to obtain", "obtained", "obtaining"] }
    ];

    const grammarTransformations = [
        "11. Transform into a polite request: “Send me the program.”",
        "12. Complete: “I am writing ______ inquire about the professional courses.”",
        "13. Reformulate in a professional tone: “I didn't get what you said.”",
        "14. Complete: “Please do not hesitate to contact us ______ you require any further assistance.”",
        "15. Write a single sentence using “nevertheless” in a professional context."
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

    // Scroll directly to form when clicking top "Start the Test"
    const startBtn = document.getElementById('start-btn');
    if (startBtn) {
        startBtn.addEventListener('click', () => {
            document.querySelector('.test-form-card').scrollIntoView({ behavior: 'smooth' });
        });
    }

    // --- 2. Render Grammar Section (Part 2) ---
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
                    <input type="text" class="q-input" name="t_q${index}" placeholder="Your answer...">
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
            "1. Reading Comprehension and Vocabulary",
            "2. Grammar and Sentence Structure",
            "3. Written Production"
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

    // --- 4. Written Production (Word Counter) ---
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
            autoSaveStatus.textContent = "Saving...";
            clearTimeout(autoSaveTimer);
            autoSaveTimer = setTimeout(() => {
                autoSaveStatus.textContent = "Saved just now";
            }, 1000);
        });
    }

    // --- 5. Dynamic Scoring & Diagnostic Dashboard Submission ---
    const submitBtn = document.getElementById('submit-test-btn');
    if (submitBtn) {
        submitBtn.addEventListener('click', () => {
            // Fill final progress bar
            progressBar.style.width = `100%`;
            progressText.textContent = `100%`;

            // --- Dynamic Grading Logic ---

            // Part 1: Reading Comprehension and Vocabulary (20 pts)
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

            // Part 2: Grammar and Sentence Structure (20 pts)
            // MCQ (10 pts)
            const mcqAnswers = ["come", "received", "complete", "contact", "so", "for", "Would", "receiving", "but", "to obtain"];
            let mcqScore = 0;
            mcqAnswers.forEach((ans, idx) => {
                const checkedRadio = document.querySelector(`input[name="g_q${idx}"]:checked`);
                if (checkedRadio && checkedRadio.value === ans) {
                    mcqScore += 1;
                }
            });

            // Transformations (10 pts) - 2 pts per correct match
            let transScore = 0;

            // Q11: "Transform into a polite request: “Send me the program.”"
            const q11 = (document.querySelector('input[name="t_q0"]')?.value || '').trim().toLowerCase();
            if (q11.includes('please') || q11.includes('could you') || q11.includes('would you') || q11.includes('mind') || q11.includes('kindly') || q11.includes('can you') || q11.includes('may i')) {
                transScore += 2;
            }

            // Q12: "I am writing ______ inquire about the professional courses."
            const q12 = (document.querySelector('input[name="t_q1"]')?.value || '').trim().toLowerCase();
            if (q12 === 'to' || q12.includes('in order to') || q12.includes('so as to') || q12.includes('for inquiring')) {
                transScore += 2;
            }

            // Q13: "I didn't get what you said." (professional)
            const q13 = (document.querySelector('input[name="t_q2"]')?.value || '').trim().toLowerCase();
            if (q13.includes('understand') || q13.includes('repeat') || q13.includes('catch') || q13.includes('miss') || q13.includes('clarify') || q13.includes('pardon') || q13.includes('appreciate') || q13.includes('explain') || q13.includes('follow') || q13.includes('quite') || q13.includes('sorry') || q13.includes('apologize') || q13.includes('hear')) {
                transScore += 2;
            }

            // Q14: "Please do not hesitate to contact us ______ you require any further assistance."
            const q14 = (document.querySelector('input[name="t_q3"]')?.value || '').trim().toLowerCase();
            if (q14 === 'if' || q14 === 'should' || q14.includes('in case') || q14.includes('whenever') || q14.includes('when')) {
                transScore += 2;
            }

            // Q15: phrase with "nevertheless"
            const q15 = (document.querySelector('input[name="t_q4"]')?.value || '').trim().toLowerCase();
            if (q15.includes('nevertheless') && q15.length > 12) {
                transScore += 2;
            }

            const part2Score = mcqScore + transScore;

            // Part 3: Written Production (20 pts)
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
                            <h4>Pre-intermediate Track (A2)</h4>
                            <p>Recommended to acquire the essential foundations of English in a structured and highly supportive learning environment.</p>
                        </div>
                        <div class="reco-card">
                            <h4>Grammar & Vocabulary Booster</h4>
                            <p>Reinforce your fundamental sentence structures and core vocabulary to progress rapidly.</p>
                        </div>
                    `;
                } else if (level === 'A2') {
                    recoHtml = `
                        <div class="reco-card recommended">
                            <h4>Intermediate Track (B1)</h4>
                            <p>Highly recommended to consolidate your communication foundations, expand vocabulary, and gain autonomy.</p>
                        </div>
                        <div class="reco-card">
                            <h4>Elementary Professional English</h4>
                            <p>Validate your first language skills applied directly to standard business interactions.</p>
                        </div>
                    `;
                } else if (level === 'B1') {
                    recoHtml = `
                        <div class="reco-card recommended">
                            <h4>Upper-intermediate Track (B2)</h4>
                            <p>Communicate with spontaneity, learn to argue complex viewpoints, and integrate into high-demand teams.</p>
                        </div>
                        <div class="reco-card">
                            <h4>Professional Certificate Prep</h4>
                            <p>Ideal to prepare for international corporate standards and officially validate your career advancement.</p>
                        </div>
                    `;
                } else if (level === 'B2') {
                    recoHtml = `
                        <div class="reco-card recommended">
                            <h4>Advanced Track (C1)</h4>
                            <p>Express ideas fluently, negotiate professionally, and process complex academic or corporate topics with ease.</p>
                        </div>
                        <div class="reco-card">
                            <h4>Management & Strategic Negotiation</h4>
                            <p>Perfect your corporate presence, report writing skills, and high-stakes negotiation capacity.</p>
                        </div>
                    `;
                } else { // C1
                    recoHtml = `
                        <div class="reco-card recommended">
                            <h4>Mastery & Perfection Track (C2)</h4>
                            <p>Achieve native-level fluency, mastering subtle linguistic nuances for competitive international academic or business roles.</p>
                        </div>
                        <div class="reco-card">
                            <h4>Public Speaking & Leadership</h4>
                            <p>Maximize your communicative impact, perfect your delivery, and master leadership storytelling in English.</p>
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
