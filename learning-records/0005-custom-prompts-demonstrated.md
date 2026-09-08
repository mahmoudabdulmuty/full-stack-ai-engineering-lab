# Custom Prompts with Data demonstrated — Module 2 Lesson 4 mastered

The learner demonstrated genuine understanding of using structured data (dictionaries and lists) to assemble dynamic LLM prompts:
- Constructed nested entity profiles with mixed data types (`str`, `int`, and `list` items).
- Interpolated dictionary keys and chained list indexes directly into multi-line f-string prompts (`{player_profile["preferred_drills"][0]}`).
- Discovered and solidified the critical mental model around f-string evaluation timing: Python evaluates and freezes f-strings upon definition; mutating underlying lists or dictionary keys requires explicit prompt string reconstruction.
- Avoided double-print side effects by correctly managing `print_llm_response()` return values (`None`).

**Implications**: The bridge between structured Python collections and customized LLM prompt engineering is fully solid. Next lesson (M2L5: "Comparing data in Python") introduces boolean comparisons (`==`, `!=`, `<`, `>`) and boolean dictionary flags, paving the way for conditionals (`if`/`else` in M2L6).

**Tutor qualification — 2026-09-08:** The timing rule above is correct, but the preserved `practice/m2l4-custom-prompts.py` builds `training_prompt` before removing equipment and does not rebuild it afterward. This file alone does not verify the claimed corrected update sequence. Whether it preserves an intentional experiment is unconfirmed. Preserve the original work and historical report; use the existing f-string timing review to verify transfer without changing the recorded capability level.
