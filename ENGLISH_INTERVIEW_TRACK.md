# Professional English for Engineering — Parallel Track

This track runs alongside the Python curriculum. It is not a separate grammar course. Its purpose is to help Mahmoud explain code, reasoning, bugs, and design decisions clearly in interviews, engineering meetings, and conversations with clients or other business stakeholders.

## Language agreement

- The tutor always replies in English, even when Mahmoud writes in Arabic.
- Mahmoud may use Arabic when it is the clearest way to express a difficult thought.
- When that happens, the tutor understands the idea, gives a natural English version, and continues the technical discussion in English.
- Do not correct every language mistake. Correct one high-value issue at a time so Python practice keeps moving.
- Prefer clear, simple English over impressive vocabulary.

## Routine inside each Python lesson

1. **Warm-up explanation:** Mahmoud explains one previously learned idea in two or three English sentences.
2. **Prediction:** Before running code, he predicts the result in English.
3. **Debug narration:** When something fails, he explains what he expected, what happened, and what he will inspect next.
4. **Interview answer:** At the end of the lesson, he gives a 60–90 second answer about the main concept.
5. **Focused feedback:** Grade technical accuracy and English clarity separately. Give one improved phrase or sentence pattern, then let him try again.

This full routine is appropriate for substantive lessons during fundamentals. For trivial continuations, use only the communication action that adds learning value. As technical independence grows, rotate from explanation drills toward requirements, reviews, architecture, incidents, demos, and stakeholder conversations.

## Interview answer structure

Use this four-part shape when explaining a concept:

1. **Definition:** “A file handle is an object that represents an open connection to a file.”
2. **Purpose:** “I use it to read from or write to that file.”
3. **Example:** “For example, I can pass the handle to `csv.DictReader`.”
4. **Important detail:** “The reader depends on the open handle, but a list already created from it remains usable after the file closes.”

The goal is a correct, structured explanation—not memorising the sample wording.

## Recovery phrases for moments when a word disappears

- “Let me explain it in a simpler way.”
- “I do not remember the exact term, but the idea is…”
- “What I mean is…”
- “Let me use an example.”
- “I would verify that assumption by…”
- “The important difference is…”

These phrases are a professional way to keep speaking instead of freezing.

## Progress stages

### Stage 1 — Explain familiar code

- Describe what a short block does.
- Explain the difference between two related objects or operations.
- Use sequence words: first, then, after that, finally.

### Stage 2 — Explain decisions and bugs

- Say why one approach was chosen.
- Describe expected versus actual behaviour.
- Explain the fix and the lesson learned.

### Stage 3 — Interview pressure

- Answer without reading notes.
- Handle one follow-up question.
- Think aloud during a small unfamiliar problem.
- Recover naturally after forgetting a word or making a language mistake.

### Stage 4 — Engineering ownership

- Clarify incomplete requirements and confirm decisions.
- Defend architecture and trade-offs without buzzwords.
- Give concise code-review feedback and respond professionally to disagreement.
- Narrate an incident, uncertainty, mitigation, and follow-up action.
- Run project demos and architecture walkthroughs fully in English.

## Module checkpoint

At the end of each Python module, run a short mock interview:

- Two concept questions.
- One code-reading or prediction question.
- One debugging question.
- One “tell me about a mistake you fixed” question.

Score each answer separately:

- **Technical accuracy:** correct / partly correct / incorrect.
- **Structure:** clear / understandable but scattered / unclear.
- **English delivery:** confident / hesitant but complete / blocked.

Record only recurring English weaknesses. Do not create a review item for every small grammar error.

## Progressive interview mode

Use only topics supported by reached capabilities: Python, debugging, backend/API, SQL, testing, project deep-dive, architecture/trade-offs, AI application reliability/evaluation, product reasoning, ownership, and English technical communication.

When formally assessing, announce:

`INTERVIEW MODE`

During this mode:

- do not teach or give normal tutor hints;
- ask realistic follow-ups and challenge vague claims;
- sometimes change a requirement and require justification;
- allow “I don’t know” followed by first-principles reasoning;
- separate technical gaps from communication gaps;
- if Mahmoud explicitly abandons the problem, end Interview Mode before teaching resumes.

Afterward assess separately: technical correctness, reasoning, depth, communication, English, interview behavior, knowledge gaps, evidence gaps, and next reinforcement. Do not inflate scores. Grow from short module checks to realistic 30–60 minute interviews only near application readiness.

## Workplace and client communication

Interview English and workplace English share the same foundation: clear explanations, structured thinking, useful technical vocabulary, and confidence when answering follow-up questions. Workplace English also requires practice with collaboration and business context.

Alongside interview questions, rotate these realistic situations into lessons:

- Give a concise progress update: completed work, current work, blocker, and next step.
- Clarify an unclear requirement without sounding confrontational.
- Explain a technical limitation to a non-technical client.
- Compare two options using benefits, risks, time, and cost.
- Correct a misunderstanding politely.
- Disagree professionally and propose an alternative.
- Ask for time to investigate instead of guessing.
- Summarise a decision and confirm ownership of the next action.
- Explain a code-review concern and propose a safer alternative.
- Walk through an architecture and its accepted trade-offs.
- Communicate uncertainty without guessing and state the verification plan.
- Give an incident update: impact, evidence, mitigation, current risk, and next step.
- Explain an AI limitation or evaluation result to a non-technical stakeholder.

Useful structures include:

- “My understanding is that you need…”
- “Could you clarify what you mean by…?”
- “The main trade-off is…”
- “From a technical perspective…”
- “The current blocker is…, and my next step is…”
- “I would not want to guess. Let me verify that and follow up.”
- “To confirm, we agreed that…”
- “I see your point. My concern is…, so I suggest…”

Keep the practice relevant to engineering work. Avoid generic corporate vocabulary that Mahmoud is unlikely to use.

Technical accuracy and English clarity are always graded separately. Correct only one high-value language issue at a time unless Mahmoud explicitly asks for a deeper language review.

## Current focus

Start with the vocabulary already active in Module 3: file path, file handle, mode, context manager, in-memory value, parser, iterator, dictionary row, filtering, `KeyError`, and `IndexError`. Use those concepts for both interview answers and short meeting-style explanations.
