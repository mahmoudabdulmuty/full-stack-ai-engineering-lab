# Model fallbacks — keep learning without model lock-in

**Last verified:** 2026-09-05. Re-check official model names and availability at every major phase boundary or whenever a provider changes its lineup.

This file maps models by **workload role**, not by claiming they are identical. Different models have different tools, context handling, rate limits, costs, and teaching behavior. A fallback may grade or modify this workspace only when its agent can read the repository, inspect/run Mahmoud's code, and follow `START_HERE.md`. A chat-only model may explain or review pasted material, but it cannot award capability evidence.

This matrix does not install or expose a provider inside Codex. If a listed model is not selectable in the current client, use that provider's own supported app, coding agent, or API and point it at this repository; otherwise choose a fallback that is actually available. The current Codex task environment exposes the OpenAI models in the baseline below.

## Current OpenAI baseline

| Baseline | Use in this lab |
|---|---|
| **GPT-5.6 Sol — Medium** | Normal lessons, explanations, source retrieval, and Socratic practice. |
| **GPT-5.6 Sol — High** | Substantive implementation, debugging, test design, integrations, and assessments. |
| **GPT-6 Astra — High** | Phase audits, difficult architecture decisions, project defense, and hiring-readiness audits. |
| **GPT-6 Astra — XHigh** | Rare escalation for the hardest unresolved or adversarial review. |
| **GPT-5.6 Terra / Luna** | Lower-cost OpenAI substitutes for balanced or low-risk work; never use a faster model as the sole judge of a major gate. |

## Closest role matches across providers

These are starting choices, not benchmark promises. Use the provider/tool you actually have access to, then run the calibration below.

| OpenAI workload role | Anthropic | Z.ai | Meta | Google | xAI | DeepSeek |
|---|---|---|---|---|---|---|
| **Sol Medium — daily tutor** | Claude Sonnet 5, default/high effort | GLM-5.3, `low` | Muse Spark 1.3 only after tutor calibration; max reasoning is usually unnecessary here | Gemini 3.8 Flash | Grok 4.6, `medium` | DeepSeek V4 Flash, thinking mode |
| **Sol High — coding, debugging, tests, assessment** | Claude Opus 5, `high` | GLM-5.3, `high` | Muse Spark 1.3, max reasoning | Gemini 3.8 Flash; Gemini 3.1 Pro Preview when the harder reasoning is worth preview instability | Grok 4.6, `high` | DeepSeek V4 Pro, thinking mode |
| **Astra High/XHigh — audit, architecture, defense** | Claude Opus 5 at high effort first; Claude Fable 5.1 for demanding long-horizon work when Opus still falls short | GLM-5.3, `max`, preferably as an independent second reviewer for a major gate | Muse Spark 1.3, max reasoning, after calibration | Gemini 3.1 Pro Preview for hard review; use a second reviewer because it is a preview model | Grok 4.6, `high` or `xhigh` | DeepSeek V4 Pro, thinking mode, preferably with a second reviewer for a major gate |
| **Terra/Luna — fast or low-risk helper** | Claude Sonnet 5 or Haiku 4.5 | GLM-5.3, `low` (capable but not necessarily efficient for trivial work) | Not the first choice for trivial work | Gemini 3.5 Flash-Lite or Gemini 3.8 Flash | Grok 4.6, `low` | DeepSeek V4 Flash, non-thinking for truly mechanical work |

Provider notes:

- **Claude:** Sonnet is the balanced daily substitute, Opus is the substantive coding/agentic substitute, Fable is the exceptional long-horizon escalation, and Haiku is the fast helper.
- **GLM-5.3:** one model spans the roles through `low`, `high`, and `max`. Its official model card emphasizes complex coding and long-horizon agentic work. Do not self-host the full model merely to avoid a temporary rate limit; use an available hosted service unless local deployment is independently justified.
- **Muse Spark 1.3:** Meta positions it for agentic/coding and long-thread work, with max reasoning in Muse Code and Meta Model API. Treat it as a Sol High or audit candidate, not automatically as the best everyday tutor.
- **Gemini:** the stable Gemini 3.8 Flash is the practical coding/agentic fallback. Gemini 3.1 Pro is a harder-reasoning option but is currently Preview, so availability, rate limits, and deprecation risk require re-checking.
- **Grok:** Grok 4.6 exposes `low`, `medium`, `high`, and `xhigh`, making the mapping direct by workload. Tool access still has to be verified in the chosen client.
- **DeepSeek:** V4 Flash is the daily/cost-conscious option and V4 Pro is the deeper-work option; both support thinking mode in the official API documentation.

## Rate-limit continuity protocol

When the preferred model is unavailable:

1. Stay on the **same current lesson, practice file, and exact next action** from the handoff. Do not open a parallel curriculum, project, assessment, or weak-point track.
2. Choose a fallback from the same workload row above. Prefer an agent with repository and terminal access over a stronger chat-only model.
3. Give the fallback this opener:

   > Read `START_HERE.md` and follow its lean bootstrap. Resume the current handoff and current practice file only. Preserve Training Mode: Mahmoud writes challenge code and gives the first prediction, diagnosis, design, and explanation. Use one hint at a time. Do not promote evidence without inspecting and running the learner's code.

4. Before trusting it for tutoring or assessment, confirm that it can state the current position, live weak point, and exact next action; preserve learner ownership; run the relevant code; grade code/prediction/explanation separately; and keep Guided distinct from Independent.
5. Keep only one tutor as the active editor/grader. A second model may review a major decision, but it must not maintain a competing progress record.
6. If no suitable model is available, continue only work already defined in the handoff: learner-written code, predictions, local execution, selective course material, tests, or a debrief from memory. Queue review for later. Do not invent extra practice merely to fill the 15–20-hour week.

Switching providers never changes the evidence gates, the current roadmap, or the ownership boundary with the Senior Engineering Growth Lab.

## Official sources

- [OpenAI model catalog](https://developers.openai.com/api/docs/models)
- [Anthropic model overview](https://platform.claude.com/docs/en/models/overview)
- [Z.ai GLM-5.3 official model card](https://huggingface.co/zai-org/GLM-5.3)
- [Meta AI — Muse Spark 1.3](https://research.meta.ai/blog/introducing-muse-spark-1-3)
- [Google Gemini model catalog](https://ai.google.dev/gemini-api/docs/models)
- [xAI model catalog](https://docs.x.ai/developers/models)
- [DeepSeek models and pricing](https://api-docs.deepseek.com/quick_start/pricing/)
