# POC / RFP Competitive Plan Methodology

## Core principle

A formal evaluation is decided by criteria. Whoever shapes the criteria toward what the buyer genuinely needs, and then proves it, usually wins - and deserves to.

The two ways to lose are to accept the competitor's criteria, or to win on criteria the buyer does not care about.

## Reading a requirements list

Every requirements list has an author and a history. Read it for:

- **Who wrote it.** A list in a competitor's vocabulary was shaped by that competitor, or by an analyst framework they fit. Note the phrases.
- **Pass/fail versus weighted.** Table stakes are pass/fail whatever the scoring says. Spend effort proportionally.
- **What is missing.** The buyer's real constraints - migration, admin burden, what breaks at scale - are often absent from the list because nobody has asked. Those are the trade-off questions.
- **What is copied.** A requirement that reads like a feature name, not a need, is a checkbox. Ask what need sits behind it before proving the feature.

## Mandatory, table stakes, differentiators, irrelevant

The four classes serve different purposes:

- **Mandatory** is the buyer's word, not the team's. Pass/fail in their scoring. One the home product meets is a fast proof; one it does not meet natively is the no-go condition, and calling it "differentiating" because the competitor wins it is how a team talks itself into an evaluation it has already lost.
- **Table stakes** get proved fast and without drama. Losing one is disqualifying; winning one earns nothing.
- **Differentiators** get the proof plan, the demonstration time, and the questions. They are where the evaluation is decided.
- **Irrelevant** criteria are the trap for the home team. A product that wins five criteria the buyer does not weigh has won nothing, and the time spent showing them is time not spent on the two that decide it.

Classification rests on buyer evidence where it exists and on the team's read where it does not. Say which, because the second kind is a question for the next call.

## Verification before commitment

Do not put a criterion in the proof plan until both sides are verified as far as evidence allows.

Home side: approved documentation, the actual limits, what a live demonstration can and cannot show. A capability that exists but cannot be demonstrated in the buyer's environment is a claim for evaluation purposes.

Competitor side: current evidence, with confidence and date. In a POC the buyer will see the competitor's product. A plan built on "they can't do X" that turns out wrong in week two costs more than the criterion.

## Proof events

A proof event is a specific, observable thing the buyer sees or does that settles a criterion. It has:

- a criterion it settles
- an owner
- a definition of pass, in the buyer's terms
- dependencies: data, environment, access, a stakeholder present

"We'll show them the integration" is not a proof event. "The buyer's platform lead connects their own service-management system, creates a change ticket, and sees the reference propagate, in the second week" is.

Differentiators without proof events are claims. Claims are what the competitor also has.

## Trade-off questions

The best evaluation questions help the buyer discover a real trade-off between the options, one they would want to know about whether or not it favors the home product. They typically surface:

- what the workflow looks like end to end, not feature by feature
- what happens at the buyer's scale, not the demo's
- who administers it and how much of their time it takes
- what governance and audit requirements it satisfies without customization
- what migration costs and what breaks

A question whose value depends on the buyer not understanding their own requirement, or on a false picture of the competitor, is not a trade-off question. It is a trap, and buyers who discover one stop trusting the rest of the plan.

## Where the competitor is stronger

Naming it in the plan is not defeatism; it is what lets the team decide how to respond before the buyer raises it. Three honest responses:

- **a workaround with its real cost**, stated
- **a reframe the buyer's own stated priorities support** - not one the team wishes they had
- **acknowledgment**, when neither of the above is true

If the criterion the competitor wins is one the buyer has called decisive, that belongs in the no-go conditions.

## No-go conditions

Written before the evaluation, they protect the team from the sunk-cost decision in week three. Typical conditions:

- a mandatory requirement the home product does not meet and no acceptable workaround exists
- the evaluation is structured around the competitor's strengths and the buyer declines to adjust scope
- the timeline cannot accommodate the proof events that matter
- the decision-maker has signalled the decision is made
- the buyer wants claims the team cannot prove and will not accept the supportable version

Qualifying out of an evaluation the team would lose is a good outcome of this skill.

## RFP answers

When the user wants written answers:

- answer what approved documentation supports
- mark every answer that needs an owner's confirmation - product, security, legal
- do not write "yes" to a requirement the product meets partially; write what it does and does not do
- never write an answer the team cannot demonstrate if the buyer asks

A false "yes" in an RFP is found in the POC, or in production.

## What not to optimize for

Do not optimize for:

- the number of criteria won
- the length of the proof plan
- questions that make the competitor look bad
- an answer to every RFP line

Optimize for:

- the buyer's real criteria, classified honestly
- verified positions on both sides
- proof events that settle the criteria that decide it
- trade-off questions the buyer is glad they were asked
- no-go conditions written while they can still be acted on
