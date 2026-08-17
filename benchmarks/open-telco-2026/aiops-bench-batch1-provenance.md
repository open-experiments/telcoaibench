# aiops_bench — Batch 1 v4 (60 questions) — FROZEN 2026-08-17

SME-reviewed (L3/L4 human-participation correction, capability-depth block added,
2026 block trimmed to survey/operator facts); pilot-screened on two live models
(58/60 both; only misses in the post-cutoff 2026 block; NGMN eight-area key
source-verified). Frozen as `aiops_bench_A/_B` (seeds 60001/60002, sha256 in
[`datasets/lite/MANIFEST.json`](datasets/lite/MANIFEST.json)).

**Scope:** TM Forum/3GPP autonomy levels (L3/L4 boundary emphasis), intent-driven
management (TS 28.312), NWDAF (TS 23.288, AnLF/MTLF), O-RAN RIC control loops
(timescales, A1/E2/O1, xApps/rApps), AI-RAN Alliance taxonomy, agentic-NOC patterns
(guardrails, HITL, change verification, drift, digital twins).
Deliberately distinct from rel19_bench's AI/ML-air-interface coverage.
Correct answer shown as A (shuffled at freeze). Pilot results delivered alongside.

---

## Q1 · Autonomy levels · expert

The defining difference between TM Forum/3GPP autonomous-network Level 3 and Level 4 is:

- **A)** L3: conditional autonomy where execution still materially relies on human supervision/decision participation; L4: within the assessed scenario the system analyzes, decides, executes and adapts, with humans governing and handling exceptions ✅
- **B)** L3 is manual with tooling; L4 adds scripted automation
- **C)** L3 covers one domain; L4 requires every network domain simultaneously
- **D)** There is no functional difference - L4 is a marketing label

*Why:* [CORRECTED per SME: the discriminator is the degree of human participation in the loop, NOT scenario breadth - TM Forum certifies L4 in specific high-value scenarios.]
*Source:* 3GPP TS 28.100 (autonomous network levels); TS 28.312 (intent-driven management)

## Q2 · Autonomy levels · expert

An operator's assurance system auto-resolves fiber-cut reroutes end-to-end, but only for its transport domain and only for pre-modeled failure types. On the autonomy ladder this is best classified as:

- **A)** Level 4 for that scenario - the system perceives, decides, executes and adapts end-to-end with humans handling only exceptions; L4 is assessed per scenario, not per whole network ✅
- **B)** Level 3 - being limited to one domain caps it at L3
- **C)** Level 2 - because humans defined the failure types
- **D)** Level 5 - within its domain it is fully autonomous

*Why:* [KEY CORRECTED per SME: scenario-scoped L4 is exactly how TM Forum certifies it (cross-domain fault mgmt, private-line assurance, RAN energy). The breadth-caps-it-at-L3 distractor is the misconception being tested.]
*Source:* 3GPP TS 28.100 (autonomous network levels); TS 28.312 (intent-driven management)

## Q3 · Autonomy levels · advanced

In the level framework, what distinguishes Level 5?

- **A)** Full autonomy across all scenarios and lifecycle phases - no human operational involvement ✅
- **B)** Autonomy for consumer services only
- **C)** A certified AI model in every network function
- **D)** Real-time closed loops under 10 ms

*Why:* L5 is the across-all-scenarios endpoint; loop speed and model placement are orthogonal.
*Source:* 3GPP TS 28.100 (autonomous network levels); TS 28.312 (intent-driven management)

## Q4 · Autonomy levels · expert

Per 2026 TM Forum reporting, the industry milestone reached by leading operators is best described as:

- **A)** Early Level-4 autonomous operations in production domains - a 'significant change' from L2/L3 pilots ✅
- **B)** Industry-wide Level 5 completion
- **C)** Abandonment of the level framework
- **D)** Regression to Level 2 after AI failures

*Why:* [Date-stamped 2026] The L4-in-production milestone is the current state marker.
*Source:* TM Forum autonomous networks framework (IG1218 family; agentic NOC PoC, inform.tmforum.org 2026)

## Q5 · Intent management · expert

In 3GPP intent-driven management (TS 28.312), an intent expresses:

- **A)** The desired outcome/expectations (e.g., coverage or QoS targets) - leaving the how to the management system, which continuously evaluates fulfillment ✅
- **B)** A step-by-step configuration script
- **C)** A one-time CLI command batch
- **D)** A hardware purchase order

*Why:* Outcome-not-procedure is the definitional core; continuous fulfillment evaluation is what separates intent from a ticket.
*Source:* 3GPP TS 28.100 (autonomous network levels); TS 28.312 (intent-driven management)

## Q6 · Intent management · expert

Two intents conflict: an energy-saving intent wants cells sleeping; a coverage-assurance intent wants them awake. Architecturally, the resolution belongs in:

- **A)** The intent management function, which detects conflicts and arbitrates by priority/policy before actuation - not in the individual closed loops ✅
- **B)** Whichever closed loop acts last
- **C)** The RAN scheduler at symbol level
- **D)** Manual NOC tickets, always

*Why:* Conflict arbitration ABOVE the loops is the design principle; last-writer-wins is the failure mode being prevented.
*Source:* 3GPP TS 28.100 (autonomous network levels); TS 28.312 (intent-driven management)

## Q7 · Intent management · advanced

The operational benefit of intent abstraction for an AIOps platform is:

- **A)** Outcomes remain stable while the system freely re-plans the means - automation can evolve without rewriting the operator's expressed goals ✅
- **B)** It removes the need for monitoring
- **C)** It guarantees zero misconfigurations
- **D)** It replaces all northbound APIs

*Why:* Stability-of-goals vs freedom-of-means is why intent scales where scripts do not.
*Source:* TM Forum autonomous networks framework (IG1218 family; agentic NOC PoC, inform.tmforum.org 2026)

## Q8 · NWDAF architecture · expert

The NWDAF functional split in TS 23.288 separates:

- **A)** AnLF (analytics logical function - inference/serving analytics) from MTLF (model training logical function - training and provisioning models) ✅
- **B)** Data collection from data storage
- **C)** RAN analytics from core analytics
- **D)** Batch from streaming pipelines

*Why:* The AnLF/MTLF split is 3GPP's train-vs-serve separation - the architectural fact behind scalable in-network analytics.
*Source:* 3GPP TS 23.288 (NWDAF architecture: AnLF/MTLF)

## Q9 · NWDAF architecture · expert

An NWDAF consumer asks for 'UE mobility analytics'. What can it request, per the analytics framework?

- **A)** Either statistics (about the past) or predictions (about the future) for the analytics ID, with confidence information on predictions ✅
- **B)** Only raw event streams
- **C)** Only real-time alerts
- **D)** Direct SQL access to UDR

*Why:* Statistics-vs-predictions duality with confidence is the consumption model; raw data access is exactly what NWDAF abstracts away.
*Source:* 3GPP TS 23.288 (NWDAF architecture: AnLF/MTLF)

## Q10 · NWDAF architecture · advanced

Which pairing correctly maps the analytics chain in a 5GC closed loop?

- **A)** UPF/NFs expose events -> NWDAF derives analytics/predictions -> PCF/NSSF/consumers adjust policy or selection -> enforcement follows policy ✅
- **B)** NWDAF configures the RAN scheduler directly
- **C)** PCF trains models; NWDAF enforces QoS
- **D)** UDM performs analytics; NWDAF stores subscriptions

*Why:* Who-does-what in the loop; distractors give NWDAF enforcement powers it does not have.
*Source:* 3GPP TS 23.288 (NWDAF architecture: AnLF/MTLF)

## Q11 · RIC control loops · expert

The O-RAN control-loop timescale mapping is:

- **A)** Non-RT RIC (in SMO): >1 s loops via rApps and A1 policies; Near-RT RIC: 10 ms-1 s loops via xApps over E2; sub-10 ms stays in the RAN nodes themselves ✅
- **B)** Non-RT RIC: sub-10 ms; Near-RT RIC: >1 s; RAN nodes: 10 ms-1 s
- **C)** All three operate at the same timescale with different vendors
- **D)** xApps run in the SMO; rApps run in the DU

*Why:* The three-timescale split with app/interface placement is THE O-RAN architecture join; option B rotates it.
*Source:* O-RAN architecture (Non-RT RIC/SMO, Near-RT RIC, A1/E2/O1, xApps/rApps)

## Q12 · RIC control loops · expert

An AI model that steers traffic between cells every ~200 ms belongs where in the O-RAN architecture?

- **A)** As an xApp on the Near-RT RIC, acting over E2 ✅
- **B)** As an rApp on the Non-RT RIC, acting over A1
- **C)** Inside the O-DU scheduler
- **D)** In the SMO inventory function

*Why:* 200 ms falls squarely in the Near-RT window - placement-by-timescale is the practical skill.
*Source:* O-RAN architecture (Non-RT RIC/SMO, Near-RT RIC, A1/E2/O1, xApps/rApps)

## Q13 · RIC control loops · expert

The A1 interface's role is:

- **A)** Non-RT RIC conveying policies, enrichment information, and ML model guidance down to the Near-RT RIC ✅
- **B)** Near-RT RIC controlling CU/DU directly
- **C)** SMO performing FCAPS on O-RUs
- **D)** Inter-RIC state replication

*Why:* A1 = policy/enrichment/model guidance downlink between the two RICs; E2 is node control, O1 is FCAPS.
*Source:* O-RAN architecture (Non-RT RIC/SMO, Near-RT RIC, A1/E2/O1, xApps/rApps)

## Q14 · RIC control loops · expert

Why does energy-saving cell-sleeping logic typically live as an rApp rather than an xApp?

- **A)** Sleep decisions ride hourly/daily traffic patterns - slow loops with SMO-wide data visibility fit the Non-RT RIC; sub-second E2 control adds nothing to a decision made on hours-scale evidence ✅
- **B)** xApps cannot access energy data
- **C)** rApps are cheaper to license
- **D)** Sleeping cells requires human approval by regulation

*Why:* Matching loop speed to decision cadence - the reasoning behind app placement rather than the rule itself.
*Source:* O-RAN architecture (Non-RT RIC/SMO, Near-RT RIC, A1/E2/O1, xApps/rApps)

## Q15 · AI-RAN taxonomy · expert

The AI-RAN Alliance's three concept pillars are:

- **A)** AI-for-RAN (AI improving RAN performance/efficiency), AI-on-RAN (AI applications running on RAN infrastructure), AI-and-RAN (shared infrastructure orchestrating AI and RAN workloads together) ✅
- **B)** AI-in-RAN, AI-out-RAN, AI-around-RAN
- **C)** Train-RAN, Serve-RAN, Share-RAN
- **D)** The alliance defines no taxonomy

*Why:* The three prepositions carry real architectural meaning: optimize the RAN, host on the RAN, co-schedule with the RAN.
*Source:* AI-RAN Alliance published taxonomy (AI-for-RAN / AI-on-RAN / AI-and-RAN)

## Q16 · AI-RAN taxonomy · expert

An operator monetizes idle RAN GPU capacity by selling inference services alongside RAN workloads with dynamic sharing. In alliance terms this is:

- **A)** AI-and-RAN - shared, co-orchestrated infrastructure for AI and RAN workloads ✅
- **B)** AI-for-RAN - it improves the RAN's economics
- **C)** AI-on-RAN - any AI near a base station qualifies
- **D)** None - GPU sharing is out of scope

*Why:* The taxonomy classification trap: revenue improvement tempts 'for-RAN', but workload co-scheduling is the and-RAN definition.
*Source:* AI-RAN Alliance published taxonomy (AI-for-RAN / AI-on-RAN / AI-and-RAN)

## Q17 · Agentic operations · expert

In 2026 TM Forum agentic-NOC material, deployed agent autonomy is bounded by:

- **A)** Guardrails plus human-in-the-loop oversight: agents recommend, validate, and trigger actions within defined limits rather than acting unboundedly ✅
- **B)** Nothing - full autonomy is the demonstrated state
- **C)** A regulation forbidding any automated network change
- **D)** Read-only access for all agents

*Why:* [Date-stamped 2026] Guardrailed-agency-with-HITL is the actual deployed pattern - both extremes are wrong.
*Source:* TM Forum agentic-NOC Catalyst material (2026): guardrailed agents, human-in-the-loop

## Q18 · Agentic operations · expert

A closed-loop assurance system connects which three record types with service-aware context, per the agentic-NOC pattern?

- **A)** Incidents, problems, and configuration changes ✅
- **B)** Invoices, contracts, and SLAs
- **C)** Alarms, logs, and traces only
- **D)** Tickets, emails, and calls

*Why:* The incident-problem-change triangle with service context is what turns siloed ITSM into closed-loop autonomy.
*Source:* TM Forum agentic-NOC Catalyst material (2026): guardrailed agents, human-in-the-loop

## Q19 · Agentic operations · expert

An autonomous change window applies a config push that degrades KPIs 40 minutes later. The design element that limits blast radius is:

- **A)** Post-change KPI verification tied to automatic rollback triggers - the change is not 'done' until its observation window closes clean ✅
- **B)** Requiring larger, less frequent change batches
- **C)** Disabling KPI collection during changes to avoid noise
- **D)** Waiting for customer complaints as the signal

*Why:* Change-verification-with-rollback is closed-loop discipline applied to the automation itself.
*Source:* TM Forum agentic-NOC Catalyst material (2026): guardrailed agents, human-in-the-loop

## Q20 · Agentic operations · expert

Model drift silently degrades a traffic-prediction model feeding a scaling loop. The AIOps control that catches this class of failure is:

- **A)** Continuous model performance monitoring against ground truth with degradation thresholds triggering retraining or fallback to non-ML operation ✅
- **B)** Retraining on a fixed annual schedule regardless of signals
- **C)** Increasing the loop's actuation frequency
- **D)** Averaging the model's output with last year's

*Why:* Monitor-against-outcomes with fallback mirrors 3GPP's AI/ML LCM philosophy applied at the ops layer.
*Source:* TM Forum agentic-NOC Catalyst material (2026): guardrailed agents, human-in-the-loop

## Q21 · Agentic operations · expert

Why do digital twins appear in autonomous-network architectures, per the Catalyst material?

- **A)** To qualify service changes against forecast network state before touching the production network - pre-deployment validation for closed loops ✅
- **B)** As 3D visualizations for executives
- **C)** To replace the OSS inventory entirely
- **D)** As backup networks during outages

*Why:* Pre-actuation qualification is the twin's role in the control loop - simulation as a guardrail.
*Source:* TM Forum agentic-NOC Catalyst material (2026): guardrailed agents, human-in-the-loop

## Q22 · NOT-form · expert

Which is NOT part of the NWDAF's standardized role?

- **A)** Enforcing QoS decisions on user-plane packets ✅
- **B)** Producing analytics statistics and predictions for consumers
- **C)** Model training via its MTLF function
- **D)** Collecting data from network functions and OAM

*Why:* NWDAF informs; PCF decides; UPF enforces - giving NWDAF enforcement is the classic architecture error.
*Source:* 3GPP TS 23.288 (NWDAF architecture: AnLF/MTLF)

## Q23 · NOT-form · expert

Which is NOT an O-RAN interface-role pairing?

- **A)** E2: SMO performing FCAPS management on the Near-RT RIC ✅
- **B)** A1: Non-RT RIC policy guidance to the Near-RT RIC
- **C)** E2: Near-RT RIC control/subscription toward CU/DU nodes
- **D)** O1: SMO management-plane access to O-RAN functions

*Why:* E2 belongs between Near-RT RIC and nodes; FCAPS is O1's job - the swap is the trap.
*Source:* O-RAN architecture (Non-RT RIC/SMO, Near-RT RIC, A1/E2/O1, xApps/rApps)

## Q24 · NOT-form · advanced

Which is NOT a realistic property of current (2026) agentic NOC deployments?

- **A)** Unsupervised agents rewriting network policy without guardrails or review ✅
- **B)** Agents triggering pre-approved runbook actions
- **C)** Human exception-handling in the loop
- **D)** Closed-loop incident-problem-change correlation

*Why:* [Date-stamped] The industry explicitly reports guardrailed patterns; unbounded agency is the overclaim.
*Source:* TM Forum agentic-NOC Catalyst material (2026): guardrailed agents, human-in-the-loop

## Q25 · NOT-form · expert

Which is NOT how intent differs from policy in management architecture?

- **A)** Intent is always expressed in natural language while policy must be JSON ✅
- **B)** Intent states outcomes; policies/configurations are among the means
- **C)** Intent fulfillment is continuously evaluated over time
- **D)** Multiple policies may be derived and re-derived from one intent

*Why:* The format claim is false (intent models are structured, e.g., TS 28.312 information models); the other three are the real distinctions.
*Source:* 3GPP TS 28.100 (autonomous network levels); TS 28.312 (intent-driven management)

## Q26 · Operational scenario · expert

An operator wants an LLM to draft RAN parameter changes from incident context, with changes applied automatically. Which architecture keeps this deployable under current autonomy practice?

- **A)** LLM proposes within a bounded action catalogue -> automated pre-checks (twin/qualification) -> guardrail policy decides auto-apply vs human approval by risk class -> post-change verification with rollback ✅
- **B)** Direct LLM shell access to network elements for speed
- **C)** LLM output emailed to engineers for manual retyping
- **D)** Block all LLM involvement in operations

*Why:* The graduated-autonomy pipeline is the deployable middle between the two extremes - and maps to L3-to-L4 progression.
*Source:* TM Forum agentic-NOC Catalyst material (2026): guardrailed agents, human-in-the-loop

## Q27 · Operational scenario · expert

A RAN vendor claims 'L4 autonomy' because their SON auto-tunes handover parameters network-wide. The sharpest technical challenge to this claim is:

- **A)** Degree of human participation: parameter auto-tuning under human supervision and review is L2/L3-class automation - L4 requires the system to analyze, decide, execute and adapt in the scenario with humans only governing and handling exceptions ✅
- **B)** SON is prohibited above L2
- **C)** Handover tuning cannot be automated safely
- **D)** L4 requires covering every network domain at once

*Why:* [CORRECTED per SME: the challenge is who participates in decisions/exceptions, not scenario breadth - and the breadth argument now appears as a distractor.]
*Source:* 3GPP TS 28.100 (autonomous network levels); TS 28.312 (intent-driven management)

## Q28 · Operational scenario · expert

During an AI-and-RAN deployment, RAN load spikes while a colocated inference job runs. The orchestration principle that must hold is:

- **A)** RAN workload priority: the co-scheduler preempts or migrates AI workloads to protect radio processing deadlines - monetization capacity is whatever the RAN leaves over ✅
- **B)** AI jobs finish first because customers paid for them
- **C)** Static 50/50 GPU partitioning at all times
- **D)** The conflict cannot occur on shared infrastructure

*Why:* RAN-first preemption is the invariant that makes shared infrastructure viable; static splits waste exactly the capacity being monetized.
*Source:* AI-RAN Alliance published taxonomy (AI-for-RAN / AI-on-RAN / AI-and-RAN)

## Q29 · Operational scenario · expert

An operator's automation journey plan reads: 'assisted scripted runbooks -> rule-triggered partial automation -> conditional closed loops with human decision participation -> highly autonomous loops where humans handle exceptions only.' Mapped to autonomy levels this progression is:

- **A)** Roughly L1 -> L2 -> L3 -> L4 ✅
- **B)** L2 -> L3 -> L4 -> L5
- **C)** L0 -> L1 -> L2 -> L3
- **D)** The steps do not correspond to levels

*Why:* [REWORDED per SME: steps defined by human participation, not scenario breadth] Assisted, partial, conditional, high autonomy = L1-L4.
*Source:* 3GPP TS 28.100 (autonomous network levels); TS 28.312 (intent-driven management)

## Q30 · 2026 state precision · expert

NGMN's 2026 agentic-AI publication identifies how many critical challenge areas for agent-based autonomous networks?

- **A)** Eight ✅
- **B)** Five
- **C)** Twelve
- **D)** Three

*Why:* The eight-area framework (fragmentation, interoperability, knowledge-sharing standards, information modeling, security/trust, HMI, governance/lifecycle, economic/organizational readiness).
*Source:* NGMN Agentic AI for Autonomous Mobile Networks publication, 11 Aug 2026 (ngmn.org) - enumeration questions cite the publication itself

## Q31 · 2026 state precision · expert

Which is NOT among NGMN's 2026 named challenge areas for agentic autonomous networks?

- **A)** Insufficient GPU supply for agent inference ✅
- **B)** Lack of standards for agent knowledge/context sharing
- **C)** Missing end-to-end security, identity and trust frameworks
- **D)** Under-addressed economic and organizational readiness

*Why:* GPU supply is the plausible-but-absent option; the listed three are verbatim challenge areas.
*Source:* NGMN Agentic AI for Autonomous Mobile Networks publication, 11 Aug 2026 (ngmn.org) - enumeration questions cite the publication itself

## Q32 · 2026 state precision · expert

NGMN's 'Zero-Trust Agent Ecosystem' concept comprises:

- **A)** Secure identity, authentication, authorization, policy enforcement, audit logging, and runtime monitoring for agents ✅
- **B)** Air-gapped agents with no network access
- **C)** A single-vendor certified agent stack
- **D)** Blockchain consensus between agents

*Why:* The six-element zero-trust enumeration applied to agents - governance mechanics, not isolation.
*Source:* NGMN Agentic AI for Autonomous Mobile Networks publication, 11 Aug 2026 (ngmn.org) - enumeration questions cite the publication itself

## Q33 · 2026 state precision · expert

NGMN's core diagnosis of why agents alone cannot deliver autonomous networks is:

- **A)** Ecosystem fragmentation - different vendor data models and terminology prevent agents from forming consistent cross-domain network understanding ✅
- **B)** Agents are too expensive to run
- **C)** Regulation prohibits agent-driven changes
- **D)** LLMs cannot parse telemetry formats

*Why:* The shared-semantics gap is the headline warning - agents need interoperable meaning, not just APIs.
*Source:* NGMN Agentic AI for Autonomous Mobile Networks publication, 11 Aug 2026 (ngmn.org) - enumeration questions cite the publication itself

## Q34 · 2026 state precision · expert

Per TM Forum's 2026 survey (125 respondents, 80 companies), the share of respondents operating at Level 3 or above is:

- **A)** 21%, up from 19% the prior year ✅
- **B)** 32%, up from 21%
- **C)** 12%, down from 19%
- **D)** 51%, up from 37%

*Why:* The 21/19 pair; 32% is the genAI-deployment figure from the same survey - the cross-trap.
*Source:* TM Forum 2026 autonomous-networks report coverage (survey + L4 certifications)

## Q35 · 2026 state precision · expert

China Mobile's certified L4 achievement is scoped to which domain, with which reported outcomes?

- **A)** Network operations centers - ~30% backend O&M workforce reduction and ~30% MTTR reduction ✅
- **B)** Radio access network - 50% energy reduction
- **C)** Core network - zero-touch slice creation
- **D)** Transport - 99.999% availability

*Why:* Domain + the 30/30 pair; distractors relocate the achievement to plausible other domains.
*Source:* TM Forum 2026 autonomous-networks report coverage (survey + L4 certifications)

## Q36 · 2026 state precision · expert

Telkomsel's reported east-Indonesia autonomous-operations trial results were:

- **A)** 12.6% wireless traffic-loss reduction, 6% MTTR improvement, 14.7% customer-experience index increase ✅
- **B)** 6% traffic-loss reduction, 12.6% MTTR improvement, 14.7% CX increase
- **C)** 30% workforce reduction and 30% MTTR reduction
- **D)** No quantified results were reported

*Why:* Triple join; option B swaps two real numbers; option C is China Mobile's result - the attribution trap.
*Source:* TM Forum 2026 autonomous-networks report coverage (survey + L4 certifications)

## Q37 · 2026 state precision · expert

Which obstacle triple does 2026 TM Forum reporting name for autonomy progression?

- **A)** Legacy BSS/OSS systems, limited talent availability, and subjective high-level testing criteria ✅
- **B)** GPU shortages, spectrum costs, and handset fragmentation
- **C)** Regulation, unionization, and vendor lock-in
- **D)** No obstacles were identified

*Why:* The named obstacle set incl. the testing-criteria critique (ANLET) - distractors are plausible industry complaints not in the report.
*Source:* TM Forum 2026 autonomous-networks report coverage (survey + L4 certifications)

## Q38 · Classification tasks · expert

An alarm storm floods the NOC: one fiber cut raises 4,000 alarms across layers. The ML/automation task that reduces this to one actionable incident is:

- **A)** Alarm correlation/root-cause classification - grouping sympathetic alarms under the causal event using topology and temporal features ✅
- **B)** Forecasting tomorrow's alarm volume
- **C)** Auto-acknowledging all alarms above a rate threshold
- **D)** Sentiment analysis of alarm text

*Why:* Storm-to-incident reduction is correlation + root-cause classification, powered by topology context - the highest-value NOC classification job.
*Source:* Operational ML practice for network automation (established AIOps task taxonomy)

## Q39 · Classification tasks · expert

You must group historical alarms into recurring patterns, but no one has ever labeled them. The appropriate technique family is:

- **A)** Unsupervised clustering - structure discovery without labels; labels can be assigned to clusters afterwards ✅
- **B)** Supervised classification - train on the labels
- **C)** Reinforcement learning against a reward
- **D)** Linear regression on alarm counts

*Why:* No labels = no supervised training; the labeled-vs-unlabeled fork is the first technique decision in every AIOps project.
*Source:* Operational ML practice for network automation (established AIOps task taxonomy)

## Q40 · Classification tasks · expert

Trouble tickets arrive as free text and must route to RAN, transport, core, or IT queues. As an ML task this is:

- **A)** Supervised multi-class text classification, trained on historically routed tickets - with periodic drift review as products and vocabulary change ✅
- **B)** Binary anomaly detection
- **C)** Time-series forecasting
- **D)** Unsupervised clustering only - routing needs no labels

*Why:* Historical routing decisions ARE the labels; drift review is the ops-hygiene half of the answer.
*Source:* Operational ML practice for network automation (established AIOps task taxonomy)

## Q41 · Classification tasks · expert

Anomaly DETECTION and failure CLASSIFICATION differ operationally in that:

- **A)** Detection identifies deviation without necessarily knowing the fault type; supervised failure classification learns mappings to known failure categories from labeled examples ✅
- **B)** They are synonyms
- **C)** Detection requires more labels than classification
- **D)** Classification always runs before detection

*Why:* The label-requirement asymmetry decides which is deployable when failure history is thin - detect first, classify as labels accumulate.
*Source:* Operational ML practice for network automation (established AIOps task taxonomy)

## Q42 · Predictive operations · expert

For hardware failure prediction (optics, fans, PSUs), plain accuracy is a misleading metric because:

- **A)** Failures are rare, so a model predicting 'no failure' everywhere achieves very high headline accuracy while having zero recall on the failure class; precision/recall on failures with cost-weighted thresholds is the honest measure ✅
- **B)** Accuracy cannot be computed for hardware
- **C)** Hardware telemetry is always mislabeled
- **D)** Regulators require F1 scores

*Why:* Class imbalance is THE trap in predictive maintenance evaluation - the 99%-accurate useless model.
*Source:* Operational ML practice for network automation (established AIOps task taxonomy)

## Q43 · Predictive operations · expert

An optics-degradation predictor is being tuned. Which threshold-setting logic is operationally correct?

- **A)** Weigh the asymmetric costs: a missed failure means an outage and truck roll, a false alarm means an early planned swap - so bias toward recall on failures within the maintenance-capacity budget ✅
- **B)** Maximize overall accuracy regardless of class
- **C)** Set the threshold at 0.5 because probabilities are calibrated by definition
- **D)** Alert only on 100%-certain predictions

*Why:* Cost-asymmetric thresholding tied to maintenance capacity is how prediction becomes an operations tool rather than a dashboard.
*Source:* Operational ML practice for network automation (established AIOps task taxonomy)

## Q44 · Predictive operations · expert

What supervision signal trains a hardware-failure predictor, and what horizon makes it useful?

- **A)** Labels from historical failure/replacement records joined to preceding telemetry; a prediction horizon at least as long as the maintenance planning-and-dispatch lead time ✅
- **B)** Synthetic labels generated by the model itself; any horizon
- **C)** Vendor datasheets; a 5-year horizon
- **D)** Real-time alarms; a zero-second horizon

*Why:* Label provenance (maintenance history) + horizon-matched-to-lead-time is the deployability pair - predicting 10 minutes ahead helps nobody dispatch a crew.
*Source:* Operational ML practice for network automation (established AIOps task taxonomy)

## Q45 · Predictive operations · expert

Capacity forecasting for a metro aggregation ring should be framed as:

- **A)** Time-series forecasting with trend and seasonality, at a horizon matching upgrade lead time - so augmentation orders land before exhaustion ✅
- **B)** Binary classification of full/not-full
- **C)** Clustering of link utilizations
- **D)** A lookup of last year's peak plus 10%

*Why:* Forecast-horizon = procurement-lead-time is the planning insight; the +10% heuristic is the legacy practice being replaced.
*Source:* Operational ML practice for network automation (established AIOps task taxonomy)

## Q46 · Dynamic scaling · expert

A UPF's traffic doubles during evening peaks. Reactive CPU-threshold autoscaling keeps arriving late because new instances need minutes to warm and attract sessions. The corrective design is:

- **A)** Predictive scaling: forecast the recurring peak and pre-scale ahead of it by at least the instance warm-up time, keeping reactive scaling as backstop ✅
- **B)** Lower the CPU threshold to 10%
- **C)** Remove the warm-up by skipping health checks
- **D)** Scale only manually during business hours

*Why:* Forecast-driven pre-provisioning offset by warm-up time is the canonical fix for slow-to-warm NFs - reactive stays as the safety net.
*Source:* Operational ML practice for network automation (established AIOps task taxonomy)

## Q47 · Dynamic scaling · expert

Scaling DOWN a stateful network function (e.g., UPF with active sessions) safely requires:

- **A)** Draining: stop assigning new sessions to the instance, let existing sessions complete or migrate, then remove it - the scale-in direction carries the service risk ✅
- **B)** Immediate termination - sessions reconnect anyway
- **C)** Scaling down only at midnight
- **D)** Never scaling down once scaled up

*Why:* Graceful drain is what makes elasticity compatible with session state; the asymmetry (up is easy, down is risky) is the operational knowhow.
*Source:* Operational ML practice for network automation (established AIOps task taxonomy)

## Q48 · Dynamic scaling · expert

An autoscaler oscillates: scale-up at 70% load, scale-down at 65%, repeating every few minutes. The standard controls are:

- **A)** Hysteresis (wider gap between up and down thresholds) plus cooldown windows between actions - damping the control loop ✅
- **B)** Faster polling so it reacts even quicker
- **C)** Removing the scale-down rule entirely
- **D)** Alerting a human for every scaling decision

*Why:* Flapping is a control-loop stability problem; hysteresis + cooldown is the damping answer, not more speed.
*Source:* Operational ML practice for network automation (established AIOps task taxonomy)

## Q49 · Dynamic scaling · expert

RAN energy-saving automation sleeps capacity cells at night. The guard that must pair with the sleep decision is:

- **A)** A wake trigger with guaranteed coverage continuity: coverage-layer cells stay on, and demand or event triggers restore sleeping capacity within the service constraint ✅
- **B)** Sleeping all cells including the coverage layer for maximum savings
- **C)** A fixed 8-hour sleep regardless of demand
- **D)** Disabling emergency call handling during sleep

*Why:* Sleep is only autonomous when the wake path and coverage floor are part of the same loop - savings without stranded users.
*Source:* Operational ML practice for network automation (established AIOps task taxonomy)

## Q50 · Task-technique mapping · expert

Which task-to-technique mapping is fully correct?

- **A)** Ticket routing -> supervised text classification; unlabeled alarm grouping -> clustering; hardware failure -> supervised prediction with imbalance handling; capacity -> time-series forecasting ✅
- **B)** Ticket routing -> clustering; alarm grouping -> forecasting; hardware failure -> unsupervised detection; capacity -> classification
- **C)** Everything -> reinforcement learning
- **D)** Everything -> a single anomaly-detection model

*Why:* The four-way mapping join - each element must be right; option B rotates them plausibly.
*Source:* Operational ML practice for network automation (established AIOps task taxonomy)

## Q51 · Task-technique mapping · expert

A network scaling loop moves from 'human approves every action' to 'human reviews exceptions weekly'. In autonomy-level and risk terms, what must have been added to justify the change?

- **A)** Demonstrated loop reliability plus guardrails: bounded action ranges, automatic rollback on KPI regression, and audit trails - the controls that convert L2/L3 supervision into L4 exception handling ✅
- **B)** A faster GPU
- **C)** A larger action space with no bounds
- **D)** Removal of KPI monitoring to reduce noise

*Why:* [Per SME framing] The shift from human decision-participation (L2/L3) to human exception-handling (L4) is earned through demonstrated reliability and guardrails - not declared.
*Source:* Operational ML practice for network automation (established AIOps task taxonomy)

## Q52 · Classification depth · expert

A ticket can simultaneously carry Domain=Transport, Technology=IP/MPLS, Category=Congestion, Impact=Enterprise VPN, Priority=P1. Which ML formulation fits, and why is plain multi-class wrong?

- **A)** Hierarchical/multi-output classification - several dependent label dimensions are predicted per ticket; multi-class forces exactly one label from one flat set and cannot represent this ✅
- **B)** Multi-class classification - concatenate everything into one label
- **C)** Clustering - labels emerge automatically
- **D)** Binary classification per ticket: problem / no problem

*Why:* [SME-requested] Telecom classifications are rarely flat; the multi-class reflex is the trap being caught.
*Source:* Operational ML practice for network automation (established AIOps task taxonomy)

## Q53 · Classification depth · expert

A ticket reads: 'Enterprise slice latency jumped from 18 ms to 75 ms after UPF maintenance; 140 premium users affected.' A competent AIOps classifier should output:

- **A)** A structured multi-field result: domain=5GC/user-plane; category=performance degradation; probable cause=change-related; affected service=enterprise slice; priority from service impact; resolver=packet core ✅
- **B)** The single label 'latency'
- **C)** A binary anomaly flag
- **D)** A cluster ID with no interpretation

*Why:* [SME-authored example] Real intent/ticket classification is structured extraction across dimensions - not one label.
*Source:* Operational ML practice for network automation (established AIOps task taxonomy)

## Q54 · Classification depth · expert

Operator NL requests hit an AIOps front-end: 'why is Cluster-7 slow?' vs 'add capacity to Cluster-7' vs 'show Cluster-7 KPIs'. Intent classification must at minimum separate:

- **A)** The action class (observe vs diagnose vs recommend vs execute) and the target/parameters - because execution intents trigger guarded workflows that observation intents must never enter ✅
- **B)** The user's seniority level
- **C)** Message length categories
- **D)** Grammatical mood only

*Why:* [SME dimension] Observe/diagnose/recommend/execute is the safety-relevant intent axis; parameter extraction makes it actionable.
*Source:* Operational ML practice for network automation (established AIOps task taxonomy)

## Q55 · Classification depth · expert

A new network function emits alarms whose embeddings sit far outside all known incident classes; the classifier's top class probability is 0.37. The correct system behavior is:

- **A)** Abstain: route to an unknown/OOD queue for human labeling, and do NOT auto-execute any remediation tied to a weak classification ✅
- **B)** Execute the remediation of the 0.37 class - it is still the argmax
- **C)** Suppress the alarms as noise
- **D)** Retrain immediately on the unlabeled alarms

*Why:* [SME-authored] Calibrated abstention + OOD routing + no-action-on-weak-confidence in one check - the safe-autonomy reflex.
*Source:* Operational ML practice for network automation (established AIOps task taxonomy)

## Q56 · Predictive operations · expert

A hardware-failure model reports 0.99 AUC. Investigation finds one feature is 'maintenance ticket opened in previous 30 minutes'. Why is the result invalid?

- **A)** Target/temporal leakage - the feature contains information downstream of the event being predicted, so the model 'predicts' failures that humans already discovered ✅
- **B)** AUC cannot exceed 0.95 legitimately
- **C)** Maintenance tickets are always mislabeled
- **D)** The model needs more epochs

*Why:* [SME-authored] Leakage detection separates predictive-operations competence from algorithm knowledge.
*Source:* Operational ML practice for network automation (established AIOps task taxonomy)

## Q57 · Root-cause ranking · expert

Given a correlated event group (200 alarms, 12 candidate causes), the evidence that should RANK root-cause candidates is:

- **A)** Topological position (upstream of the symptom spread), temporal precedence (first in the causal window), and consistency of the predicted impact set with observed symptoms - not raw alarm frequency ✅
- **B)** Alarm count per candidate - the loudest cause wins
- **C)** Alphabetical order of network elements
- **D)** The candidate with the most recent software version

*Why:* [SME gap #4] Upstream+first+consistent is causal ranking; loudest-wins is the frequency fallacy that misroutes NOCs.
*Source:* Operational ML practice for network automation (established AIOps task taxonomy)

## Q58 · Action-risk policy · expert

Which proposed-action risk classification correctly separates auto-execution from human approval?

- **A)** Restart one stateless pod: low risk, auto-executable; drain one redundant UPF: medium, auto with enhanced verification; alter national routing policy or bulk-rewrite RAN parameters: high, human approval required ✅
- **B)** All four are equally safe once a model proposes them
- **C)** All four require CEO approval
- **D)** Risk depends only on the time of day

*Why:* [SME-authored] Blast-radius classification IS the decision behind 'less human intervention' - graduated execution policy by reversibility and scope.
*Source:* Operational ML practice for network automation (established AIOps task taxonomy)

## Q59 · Ops maturity ladder · expert

The analytics-to-autonomy progression in operations is:

- **A)** Descriptive (what happened) -> diagnostic (why) -> predictive (what will happen) -> prescriptive (what to do) -> autonomous (act and verify under policy/guardrails) ✅
- **B)** Predictive -> descriptive -> autonomous -> diagnostic
- **C)** All five are synonyms for monitoring
- **D)** Prescriptive comes before diagnostic

*Why:* [SME backbone] observe -> classify -> correlate -> diagnose -> predict -> decide -> act -> verify -> learn; the ladder orders the capability stack.
*Source:* Operational ML practice for network automation (established AIOps task taxonomy)

## Q60 · Scaling objective · expert

Two autoscaling policies both meet the latency SLO: Policy A uses 30% more GPUs and never violates; Policy B uses less compute with 0.5% SLO violations. The autonomous controller should:

- **A)** Neither can be chosen without the operator's expressed intent - the SLO/violation tolerance and cost function decide; the controller optimizes the stated objective, it does not invent one ✅
- **B)** Always choose A - SLOs are sacred
- **C)** Always choose B - cost wins
- **D)** Alternate between them hourly

*Why:* [SME-authored] Scaling optimizes a multi-term objective (SLO risk, cost, headroom, action frequency) supplied by intent - simplistic models pick a side.
*Source:* Operational ML practice for network automation (established AIOps task taxonomy)
