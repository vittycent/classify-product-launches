# Answer keys

**Never give these files to the agent you are testing.** They list every inconsistency planted in Rootline's data and what a good run should notice. The agent's command already forbids reading any folder named `answer-keys`; if you run your own tests, keep it that way.

| File | What it covers |
|---|---|
| `roadmap-traps.md` | The traps in Rootline's roadmap: dates the calls contradict, automatic summaries that get things wrong |
| `company-data-traps.md` | The demo releases and what a good run notices for each; the planted mess in the company data; the challenges, delays and cancellations added before the worked example; the CEO's 2027 requests |

**How to use them.** Run `/tiering-release` on a release, score first, finish the run, and only then read the release's section here. Count what your run caught, what it missed, and what it found that isn't listed.

The files mention the decisions that shaped them (numbers like D-56). Those come from Victor's build log, which is not published.
