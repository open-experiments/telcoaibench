# Vendor GenAI Tests v2

Approved 2026-08-10. This file is the source of truth for the v2 matrix, anchors, and rubric.

This draft grows the suite from 3 mega-questions to a **6-vendor x
4-domain matrix (24 questions)** and upgrades grading from a single
0-10 score to **per-criterion structured judging**.

Because this suite has no answer key, quality lives in two places:
(1) questions engineered so that fabrication is detectable, and
(2) **judge anchors** per question - durable, publicly established
facts the judge can lean on, plus known fabrication bait to watch
for. Anchors are deliberately restricted to long-stable facts
(product families, architectural approaches, well-known heritage),
not release-version claims that rot.

Vendors: **Ericsson, Nokia, Mavenir** (existing) + **Samsung
Networks, Rakuten Symphony, Cisco** (new - chosen for RAN, open-RAN
webscale, and core/transport contrast; flag if you want a different
set, e.g. Juniper, NEC, Amdocs).

Domains per vendor: **A. RAN architecture** | **B. Core & converged
services** | **C. OSS/automation & AI** | **D. Cloud-native
infrastructure strategy**.

---

## Grading upgrade: per-criterion structured judging

The judge grades each answer on four criteria, each 0-10, and must
return machine-readable JSON:

```json
{
  "technical_accuracy": 0-10,   // claims consistent with public knowledge; no invented products/specs/numbers
  "completeness":       0-10,   // every numbered part of the question addressed
  "depth":              0-10,   // concrete components, interfaces, quantitative reasoning vs marketing prose
  "honesty":            0-10,   // separates public knowledge from speculation; abstains rather than invents
  "verdict": "<=25 words: dominant strength or failure>",
  "rationale": "<3-6 sentences citing specific claims judged right or wrong>"
}
```

Overall score = weighted mean: **accuracy 0.40, honesty 0.25,
completeness 0.20, depth 0.15** (accuracy and honesty dominate by
design - this suite exists to punish confident fabrication).
Normalized to 0-1 for the results table; per-criterion means are
also reported per run.

Judge instructions additionally state: award honesty credit for
explicit "this is not public / would require vendor engagement"
statements; deduct accuracy for any invented product name, version
number, interface name, or performance figure; when unsure whether
a claim is fabricated, deduct depth rather than accuracy.

---

## Question matrix

Each question below shows: the prompt (all have the same 5-part
structure for comparability) and the judge anchors. The common
5-part structure per question:

1. Portfolio & architecture: name the actual product family/
   components and how they fit together.
2. Interfaces & standards posture: which open interfaces are
   supported and how deep.
3. Differentiation: what is technically distinctive vs peers.
4. Quantitative reasoning: one dimensioning or performance
   consideration a buyer should model.
5. Honesty check: what is NOT publicly known that a buyer must get
   from the vendor directly.

### Ericsson

**E-A (RAN).** Deep-dive Ericsson's RAN portfolio for a brownfield
operator adding mid-band 5G: radio and baseband product families,
purpose-built vs Cloud RAN paths, and Massive MIMO approach.
*Anchors:* AIR (Antenna Integrated Radio) family for Massive MIMO;
baseband processors (purpose-built silicon) alongside a Cloud RAN
offering that runs vDU/vCU on COTS; Ericsson Silicon custom ASICs;
historically cautious-then-committed posture on O-RAN interfaces
(supports open fronthaul in Cloud RAN contexts); uplink booster and
carrier aggregation strengths. Fabrication bait: invented AIR model
numbers with specific antenna configs, invented O-RAN compliance
matrices, specific TCO percentages.

**E-B (Core).** Ericsson's 5G core: product line, dual-mode story,
and how EPC/5GC coexistence is handled for an operator migrating
from LTE. *Anchors:* dual-mode 5G Core combining EPC and 5GC in one
cloud-native codebase; heritage from Ericsson virtual EPC; combined
SMF+PGW-C style interworking for EPS fallback; container-based
deployment on Ericsson's or third-party CaaS. Bait: invented
per-node session-capacity numbers, invented product sub-names.

**E-C (OSS/AI).** Ericsson's network automation and AI story:
platforms for service/network orchestration, RAN automation apps,
and where AI actually lands. *Anchors:* Ericsson Intelligent
Automation Platform (EIAP) as SMO/non-RT-RIC with rApps; Cognitive
Software heritage in network optimization; energy-saving and
performance rApps as flagship use cases. Bait: invented rApp names
with quantified gains, claims of fully autonomous L4+ operations in
production.

**E-D (Cloud-native).** How Ericsson packages its cloud-native
infrastructure dependencies: what it certifies to run on, its own
CaaS assets, and the operator lock-in tradeoffs. *Anchors:*
applications delivered as CNFs with a certified-stack model
(own CNIS/CaaS or certified third-party platforms incl. Red Hat
OpenShift); bare-metal-first performance posture for user-plane
workloads. Bait: invented benchmark deltas between CaaS choices.

### Nokia

**N-A (RAN).** Nokia's RAN portfolio and silicon strategy for a
greenfield TDD operator, including its open-RAN posture.
*Anchors:* AirScale portfolio (radios, baseband) on ReefShark
SoCs; anyRAN approach pairing purpose-built and Cloud RAN on the
same software; comparatively early/vocal O-RAN participation among
the big incumbents; MantaRay SON/management heritage (formerly Eden-NET/
self-organizing tooling). Bait: invented ReefShark generation
specs, invented open fronthaul throughput claims.

**N-B (Core).** Nokia's core and converged offering, including its
telco cloud posture and the voice stack. *Anchors:* cloud-native
5G core packaged with its telco cloud assets; long IMS/voice
heritage; Nokia's core commonly deployed on third-party clouds and
hyperscalers as well. Bait: invented per-VNF KPIs, invented
hyperscaler exclusivity claims.

**N-C (OSS/AI).** Nokia's automation/AI assets across network and
service management. *Anchors:* Network Services Platform (NSP) for
IP/optical automation; MantaRay for RAN management/SON; AVA as the
AI/analytics brand; Bell Labs research halo feeding AI features.
Bait: invented AVA use-case metrics, invented product mergers.

**N-D (Cloud-native).** Nokia's approach to CNF packaging and
infrastructure neutrality; where Nokia differs from Ericsson on
cloud strategy. *Anchors:* Nokia positions relative openness to
running on operator-chosen CaaS/hyperscalers; CNF delivery with
its own container services layer available; historically more
public about hyperscaler partnerships for core workloads. Bait:
invented certification matrices, invented performance ratios.

### Mavenir

**M-A (RAN).** Mavenir's Open RAN offering and how a webscale-
native challenger differs architecturally from incumbents.
*Anchors:* software-first, containerized vDU/vCU on COTS with open
fronthaul to third-party O-RUs; O-RAN flagship vendor narrative;
partnerships for radio hardware rather than own high-volume radio
manufacturing at incumbent scale. Bait: invented O-RU partner
matrices, invented massive-MIMO performance parity numbers.

**M-B (Core).** Mavenir's core and IMS/messaging heritage and its
"any-G" positioning. *Anchors:* deep IMS/VoLTE/RCS and messaging
lineage (heritage incl. Mavenir/Mitel/Xura/Comverse ancestry);
cloud-native converged packet core positioning across 4G/5G;
webscale deployment claims typically referencing greenfield or
challenger operators. Bait: invented tier-1 brownfield core
displacements, invented subscriber-scale numbers.

**M-C (OSS/AI).** Mavenir's automation/AI posture given its size:
what it plausibly builds itself vs integrates. *Anchors:*
RIC-aligned automation ambitions consistent with O-RAN posture;
realistically thinner OSS estate than incumbents - honesty about
integration with third-party OSS is the expected good answer.
Bait: claims of a full-suite OSS competing with NetAct/EIAP-class
platforms.

**M-D (Cloud-native).** Mavenir's cloud-native story as a
born-cloud vendor: packaging, CaaS neutrality, hyperscaler
deployments. *Anchors:* containerized from origin rather than
re-platformed VNFs; public cloud deployments (incl. hyperscaler
infrastructure) as a differentiation narrative; webscale CI/CD
positioning. Bait: invented uptime/scale metrics, invented
exclusive cloud partnerships.

### Samsung Networks

**S-A (RAN).** Samsung's network business RAN portfolio and its
notable market wins profile; vRAN posture. *Anchors:* significant
vRAN + open fronthaul deployments (notably with large US and
Japanese operators publicly discussed); own radio portfolio incl.
Massive MIMO; among the earliest large-scale commercial vRAN
vendors; chipset heritage from the broader Samsung group. Bait:
invented deployment scale figures, invented exclusive operator
lists beyond well-publicized ones.

**S-B (Core).** Samsung's core offering relative to its RAN
strength - an honest answer acknowledges the asymmetry. *Anchors:*
Samsung offers a 5G core but its market presence is RAN-led; core
wins are less prominent publicly than its RAN footprint - honesty
credit for stating this. Bait: invented tier-1 core deployments.

**S-C (OSS/AI).** Samsung's management/automation assets for its
RAN, including SON/analytics. *Anchors:* management suite oriented
to its own RAN estate; AI features positioned around RAN
optimization/energy; thinner multi-vendor OSS ambition than
incumbent OSS houses - honesty expected. Bait: invented
multi-vendor OSS platform claims.

**S-D (Cloud-native).** Samsung's vRAN cloud stack choices and
what a buyer must verify. *Anchors:* vRAN commercially run on
third-party CaaS in public references (incl. hyperscaler-adjacent
and operator-chosen stacks); accelerator strategy (lookaside/
inline L1) is a live design axis in its public materials. Bait:
invented L1 accelerator benchmark numbers.

### Rakuten Symphony

**R-A (RAN).** Symphony's Open RAN productization of the Rakuten
Mobile build: what is actually productized and the operational
model it sells. *Anchors:* productized from Rakuten Mobile's
greenfield fully-virtualized network; Symware edge appliances;
sells the operating model (automation-heavy, low-touch) as much
as the RAN software; radio units historically from partners
(incl. its acquisition lineage). Bait: invented incumbent-scale
brownfield wins, invented performance parity claims vs
purpose-built Massive MIMO.

**R-B (Core).** Symphony's core assets and their provenance;
honesty about what came from where. *Anchors:* core lineage
includes acquired assets (e.g. the former Innoeye/other
acquisitions feeding Symworld); Rakuten Mobile's own network as
the reference deployment; multi-vendor reality inside the
reference network (honesty credit for noting the reference
network also uses third-party core elements). Bait: invented
standalone core wins at major operators.

**R-C (OSS/AI).** Symworld platform story: the app-store-like
operations platform claim, and what a buyer should verify.
*Anchors:* Symworld as the umbrella platform (OSS, orchestration,
apps); "1000s of cell sites per engineer"-style opex claims are
marketing anchors that deserve scrutiny - honesty credit for
flagging that such ratios are context-dependent. Bait: repeating
opex ratios as established fact without caveats.

**R-D (Cloud-native).** Symphony's infrastructure stack and
edge-cloud model. *Anchors:* fully containerized stack with its
own cloud/edge layering productized from Rakuten Mobile's
distributed telco cloud; Symware at far edge; positioning as an
integrated vertical stack (which trades openness for coherence -
a good answer surfaces this tension). Bait: invented third-party
CaaS certifications.

### Cisco

**C-A (RAN).** Cisco's actual position in RAN - an honesty-heavy
question: what Cisco does and does not offer in RAN. *Anchors:*
Cisco is not a macro RAN vendor - no own macro radio/baseband
portfolio; RAN-adjacent presence via transport (fronthaul/
backhaul routing), private-5G offerings, and past O-RAN
ecosystem/RIC-adjacent involvement; a good answer says "for macro
RAN, Cisco is the wrong shortlist" explicitly. Bait: invented
Cisco macro RAN products - this question exists to catch models
that give every vendor every portfolio.

**C-B (Core).** Cisco's packet core heritage and current 5G core
posture. *Anchors:* Starent acquisition heritage -> ASR 5000/
StarOS EPC lineage -> cloud-native mobility (Ultra/cloud core
line); strong historical EPC share incl. major US operators;
converged policy/charging assets from earlier acquisitions. Bait:
invented 5GC tier-1 SA wins beyond public ones, invented product
renames.

**C-C (OSS/AI).** Cisco's automation stack relevant to telco:
network automation, assurance, and AI positioning. *Anchors:*
Crosswork family for network automation/assurance in SP networks;
NSO (Tail-f acquisition) as the flagship service orchestrator
with wide multi-vendor adoption; AI positioning concentrated in
assurance/observability (incl. ThousandEyes lineage). Bait:
invented RAN-domain AI apps, invented NSO competitor-displacement
claims.

**C-D (Cloud-native).** Cisco's role in telco cloud
infrastructure: where it plays (and doesn't) in CaaS for CNFs.
*Anchors:* strength in the underlay (data-center fabrics, SP
routing, optics) and in orchestration (NSO) rather than owning
the telco CaaS layer; honest answers position Cisco as
infrastructure + automation around third-party Kubernetes
platforms. Bait: invented Cisco telco-CaaS market share.

---

## Dataset schema (per record)

```json
{"id": "E-A", "vendor": "Ericsson", "domain": "RAN",
 "question": "<full 5-part prompt>",
 "judge_anchors": "<the anchor text - passed to the judge>",
 "fabrication_bait": "<the bait text - passed to the judge>"}
```

The judge prompt injects anchors + bait as *grading context* (the
candidate never sees them). This keeps rubric grading tethered to
stated public facts instead of the judge's own recall alone.

---

**Review checklist:** (1) approve/adjust the vendor set (swap
Cisco/Samsung/Rakuten for others if you prefer); (2) challenge any
anchor you believe is stale or wrong - anchors become grading
truth; (3) check the criterion weights (0.40/0.25/0.20/0.15);
(4) confirm the honesty-trap questions (C-A, S-B, M-C) match your
intent - they deliberately reward models that say "this vendor
does not do that."
