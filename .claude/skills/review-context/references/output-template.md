# Output template — Review Context

Two skeletons: the corpus doc (only when saving a fresh dump) and the Review Context doc itself. Match the frontmatter style of the existing `Research/Reviews - *.md` files.

## A. Corpus doc (only for a new raw source)

```markdown
---
summary: "<n> <what> from <source>, <date range or undated>, verbatim with IDs."
type: review-corpus
brand: Tudatalatti Kontroll
source: <where it came from, how it was captured, who supplied it>
corpus_size: <n> unique records (<duplicates removed>)
coverage: <partial / positive-selected / hand-picked / export; dated or undated; languages>
privacy: commenters recorded by initials only
imported: <YYYY-MM-DD>
---

# Reviews — <Source> (<What>)

Method: [[Customer Review Mining Method]].

## Corpus (verbatim, original spelling kept)

| ID | Commenter | Date | Reactions | Verbatim | Founder reply |
|---|---|---|---|---|---|
| <PREFIX>01 | <initials> | <date or undated> | <n or —> | „…" | „…" or — |
```

ID prefix: R = Facebook comments, W = website widget, A = ad comments, M = Moly.hu, L = Libri, B = Bookline, S = support or survey. Use a new prefix for a new source so IDs never collide.

## B. Review Context doc

```markdown
---
summary: "Review Context for <scope>: objections, comment-response hooks, emotional stories, complaints and static headline candidates mined from <sources> (N=<n>, <dates or undated>)."
type: review-context
brand: Tudatalatti Kontroll
scope: <product / sources / date range>
sources:
  - Research/Reviews - <…>.md
  - Research/Reviews - <…>.md
corpus_size: <N> records (<per-source breakdown>)
coverage: <partial / positive-selected / dated or undated / languages>
method: Knowledge/Domain Knowledge/Customer Review Mining Method.md
last_updated: <YYYY-MM-DD>
---

# Review Context — <scope>

Sources: [[Reviews - …]], [[Reviews - …]]. Method: [[Customer Review Mining Method]]. Hook formats: [[Hooks]] #1. Headlines: [[Problem-Solution Headline Writer]]. Walls: [[Compliance and Claims Watchlist]].

## Corpus profile

- Records: <N> (<breakdown>). Dates: <range or undated>. Selection: <how>. Languages: <…>.
- Read this as: <directional / positive-selected / representative>.
- Missing: <negative and neutral reviews, retailer reviews, ad comments, course feedback…>.
- Consent: <IDs in the corpus docs' Consent log and Tribal Knowledge → Consent log; "none" otherwise>.

## What to act on first

1. <the consent, pull or test that unlocks the most>
2. <…>
3. <…>

## 1. Objections

| ID | Date | Verbatim (HU) and gloss | Type | Stage | Count of N | Answer direction | Feeds |
|---|---|---|---|---|---|---|---|

<Two or three sentences: which objection is the brake, what recurs, what's a single-instance candidate.>

## 2. Comment-response hook candidates

### H1. <short label>
- **Comment:** „…" (<ID>, <date>, <source>) [R] / [C] NEEDS A REAL COMMENT — direction only
- **Why it stops the scroll:** <mechanism>
- **Response opener (HU):** „…" (<English gloss>)
- **Pairs with:** #1 + #<n> <format>
- **Compliance:** <no second-person attribute / no health outcome / no doctor-bashing: pass or the fix>
- **Governors:** Claims <clear/gated/unusable> · Voice <in-voice/off-voice/transformable>
- **Consent:** <needed / on file / not applicable (composite direction)>

<Repeat for five to eight candidates, ranked by objection recurrence.>

## 3. Emotional stories

### S1. <short label> (<ID>, <date>, <reactions>)
- **Arc:** <beat 1> → <beat 2> → <beat 3> → <beat 4>
- **Keep verbatim:** „…" (gloss) · „…" (gloss)
- **From → to:** <from-state> → <to-state>
- **Witness:** <who, or none>
- **Format fit:** <review-as-primary-text native / static quote card / book-extract video / founder retells in third person>
- **Governors:** Claims <…> · Voice <…> · Cut: „…" (<why>)
- **Consent:** <needed / on file>

## 4. Biggest complaints

| Rank | Complaint (customer words) | IDs | Class | Count of N | So what |
|---|---|---|---|---|---|

<If positive-selected: "This corpus can't show complaints. The visible ones are <…>. Pull <…> before treating the list as complete.">

## 5. Headline candidates for statics

**Product:** <one>. **ICP:** <one>. **Sophistication:** <high/low, why>.

**Problems ranked (one per headline):** <problem 1> · <problem 2> · <…>

**Customer language used:** <10 to 15 phrases with IDs and tags>

**Walls applied:** <Compliance §1–§5 as written for statics; Hungarian; ten words or fewer; quote vs borrowed phrasing>

**5 HEADLINE OPTIONS FOR <PRODUCT>:**

**Option 1:** <HU headline> (<gloss>)
- **Problem Addressed:** <…>
- **Sophistication Level:** <…>
- **Customer Language Used:** „…" (<ID>)
- **Why This Works:** <2 to 3 sentences>

<Options 2 to 5, each a different structure. Mark the one that breaks the brand's usual shape.>

**MY RECOMMENDATION FOR WHAT TO TEST FIRST:** <1 to 2 options, why>

**Brand Context Applied:**
- **What I used:** <…>
- **What I avoided:** <…>
- **Why this fits:** <…>

This is based on everything I've learned about writing effective problem/solution headlines

## Governors (new or changed IDs only)

<First run: changed relative to the corpus docs' own governors tables. Refresh: changed since the previous Review Context. A proposed change to a wall is a proposal; the candidate that depends on it stays blocked.>

| ID | Claims | Voice | Why |
|---|---|---|---|

**Lint pass (own lines only):** <what was checked>. **Compliance §6 walk:** <1–7, pass or fix>.

## Coverage gaps and next pulls

- <what's missing and where to get it>

## Change log

- <YYYY-MM-DD> — created from <sources>, N=<n>.
```
