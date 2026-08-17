# netapi_bench — Batch 1 v3 DRAFT (38 questions; SME corrections applied incl. 1Q26 heatmap re-reads) — for SME review

**Scope:** CAMARA/Open Gateway APIs (mechanics), 3GPP exposure architecture (NEF/CAPIF),
ecosystem roles (CAMARA/GSMA/TMF), monetization structure, operational selection scenarios.
**NTN-lesson applied:** no market-snapshot numbers as keys; official 1Q26-report facts are
date-stamped in the stem. Monetization tested structurally (units), never price points.
Correct answer shown as A (shuffled at freeze). Pilot results delivered alongside.

---

## Q1 · API mechanics · expert

How does the CAMARA Phone Number Verify operation confirm a supplied phone number?

- **A)** Silent network/SIM-based authentication verifies the supplied number corresponds to the authenticated device and returns a true/false verification result - no SMS OTP is sent ✅
- **B)** By sending a silent SMS one-time-password and auto-reading it
- **C)** By returning the subscriber's MSISDN to the developer for comparison
- **D)** By querying the device's SIM applet over the user plane

*Why:* [Per SME: operation-specific stem; SUPI/GPSI realization removed; note the API family also has a Device Phone Number Retrieval operation where supported/lawful.]
*Source:* Network-API exposure architecture material (NEF per 3GPP TS 29.522; CAMARA mechanics)

## Q2 · API mechanics · expert

What information can CAMARA SIM Swap expose for fraud decisioning?

- **A)** Whether a swap occurred within a requested interval and/or the date/time of the most recent swap - without exposing SIM identifiers such as ICCID ✅
- **B)** The full SIM change history with retailer identity
- **C)** The ICCID of the current SIM card
- **D)** A block/unblock control for the subscription

*Why:* [Per SME: check-vs-retrieve-date precision] The two operations (boolean interval check, timestamp retrieval) are the fraud signals; no SIM identifiers leave the operator.
*Source:* Network-API exposure architecture material (NEF per 3GPP TS 29.522; CAMARA mechanics)

## Q3 · API mechanics · expert

Which conceptual 5GC control-to-enforcement chain underlies a QoD request?

- **A)** Exposure (NEF) -> policy control (PCF) -> session management (SMF) -> user-plane enforcement (UPF) ✅
- **B)** NEF -> UDM -> AUSF -> UPF
- **C)** PCF -> NEF -> AMF -> gNB directly
- **D)** NEF -> NWDAF -> SMF -> UPF

*Why:* The exposure-to-enforcement chain; each distractor swaps in a plausible NF that plays no role in QoS application.
*Source:* Network-API exposure architecture material (NEF per 3GPP TS 29.522; CAMARA mechanics)

## Q4 · API mechanics · expert

When a developer requests 'stable 20 Mbps, low latency' via QoD, the network realizes it by:

- **A)** Mapping the requested CAMARA QoS profile onto underlying 3GPP QoS policy and flow parameters appropriate to that profile, as realized by the operator ✅
- **B)** Moving the subscriber to a premium slice permanently
- **C)** Raising the UE's transmit power
- **D)** Reserving a dedicated carrier for the session

*Why:* Profile-to-5QI mapping onto a dedicated QoS flow is the mechanism - not slicing, power, or spectrum reservation.
*Source:* Network-API exposure architecture material (NEF per 3GPP TS 29.522; CAMARA mechanics)

## Q5 · API mechanics · advanced

The two CAMARA Device Location variants differ how?

- **A)** Verification answers whether a device is within a supplied area; Retrieval returns the network-derived location area/geometry (circle or polygon) and location time ✅
- **B)** Verification is GPS-based; Retrieval is cell-based
- **C)** Verification requires user consent; Retrieval does not
- **D)** They are identical except for pricing

*Why:* The boolean-vs-coordinates split is the privacy-relevant design line: verification answers without disclosing location.
*Source:* Network-API exposure architecture material (NEF per 3GPP TS 29.522; CAMARA mechanics)

## Q6 · API mechanics · expert

Why do CAMARA verification APIs often offer boolean decision responses instead of returning the underlying attribute?

- **A)** Data minimization: the consumer gets a decision, not the underlying personal data - easing privacy/GDPR posture and user trust ✅
- **B)** Booleans are cheaper to transmit
- **C)** Operators cannot access the underlying data themselves
- **D)** It avoids the need for authentication

*Why:* The privacy-by-design rationale is the functional insight; distractors are surface plausible.
*Source:* Network-API exposure architecture material (NEF per 3GPP TS 29.522; CAMARA mechanics)

## Q7 · API mechanics · expert

When a CAMARA API requires end-user consent under the applicable legal basis, where is consent enforcement placed in the architecture?

- **A)** At the API provider's authorization server, which validates the purpose and required consent before issuing or accepting authorization for the API invocation ✅
- **B)** In the developer application's terms and conditions
- **C)** In the aggregator's contract with the operator
- **D)** Nowhere - consent is collected once at SIM purchase

*Why:* [REWRITTEN per SME - consent is NOT universally mandated; legal basis varies. CAMARA's Identity & Consent framework supports OIDC code, CIBA, client-credentials and JWT-bearer flows; when consent is required, the provider enforces it at authorization time.]
*Source:* Network-API exposure architecture material (NEF per 3GPP TS 29.522; CAMARA mechanics)

## Q8 · API mechanics · expert

A subscriber is roaming abroad. Why can a home-operator CAMARA API call behave differently for them?

- **A)** Some APIs depend on capabilities or network state in the visited network, so roaming requires home/visited operator exposure and federation support - capability availability can differ while roaming ✅
- **B)** CAMARA APIs are legally banned while roaming
- **C)** The visited network always answers on behalf of the home network
- **D)** Roaming devices lose their subscription identity

*Why:* [Per SME: topology-abstracted] The operational fact is capability variability under roaming, not one deployment architecture.
*Source:* 3GPP exposure framework (NEF TS 29.522; CAPIF TS 23.222; TS 23.502 exposure procedures)

## Q9 · Exposure architecture · advanced

In the 5G core, the function that exposes network capabilities to external applications - the anchor for CAMARA-class APIs - is:

- **A)** NEF (Network Exposure Function) ✅
- **B)** NWDAF
- **C)** NRF
- **D)** UDR

*Why:* NEF is the northbound bridge; NWDAF is analytics, NRF discovery, UDR data storage.
*Source:* 3GPP exposure framework (NEF TS 29.522; CAPIF TS 23.222; TS 23.502 exposure procedures)

## Q10 · Exposure architecture · expert

The 3GPP Common API Framework (CAPIF) provides:

- **A)** A common model for API publication, discovery, onboarding of API invokers, and security across exposure platforms ✅
- **B)** The billing engine for API monetization
- **C)** The QoS enforcement path for QoD
- **D)** A replacement for OAuth in 5GC

*Why:* CAPIF is the framework layer (who may discover/invoke which APIs, how they authenticate) - not billing or enforcement.
*Source:* 3GPP exposure framework (NEF TS 29.522; CAPIF TS 23.222; TS 23.502 exposure procedures)

## Q11 · Exposure architecture · expert

In a channel-partner/aggregated Open Gateway deployment, the layered path from a developer's app to the 5G core is:

- **A)** Application -> aggregation platform -> operator API exposure platform (OAuth-secured) -> NEF -> core network functions ✅
- **B)** Application -> NEF -> aggregation -> PCF -> operator platform
- **C)** Application -> operator BSS -> UDM -> NEF
- **D)** Application -> RAN API gateway -> gNB -> core

*Why:* The stack order matters operationally (where auth happens, where federation happens); distractors scramble it.
*Source:* Network-API exposure architecture material (NEF per 3GPP TS 29.522; CAMARA mechanics)

## Q12 · Exposure architecture · expert

What makes the aggregation layer valuable in the Open Gateway model?

- **A)** Developers want one integration reaching many operators' subscribers - aggregators federate access so each operator's API instance is reachable without per-operator bespoke integration ✅
- **B)** Operators are prohibited from exposing APIs directly
- **C)** NEF cannot terminate TLS
- **D)** To translate between CAMARA and SOAP

*Why:* Solving developer-side fragmentation is the commercial raison d'etre - the direct answer to why telco APIs failed in previous attempts.
*Source:* Network-API exposure architecture material (NEF per 3GPP TS 29.522; CAMARA mechanics)

## Q13 · Exposure architecture · expert

In the Open Gateway operating model, TMF Operate APIs (TMF93x family) serve which role relative to CAMARA APIs?

- **A)** CAMARA defines the developer-facing service APIs; TMF Operate APIs standardize the operator-to-aggregator/partner operational interfaces (ordering, settlement, lifecycle) behind them ✅
- **B)** TMF APIs replace CAMARA at the developer edge
- **C)** CAMARA handles billing while TMF handles QoS
- **D)** They are competing specifications for the same interface

*Why:* The two-sided architecture: service API to developers, operate APIs between commercial parties - both needed for a working market.
*Source:* GSMA Open Gateway 1Q26 update (camaraproject.org, official PDF, Feb 2026)

## Q14 · Exposure architecture · advanced

The three organizations and their roles in the network-API ecosystem are:

- **A)** CAMARA (Linux Foundation open-source project): defines the API specifications | GSMA Open Gateway: operator federation initiative and MoU | TM Forum: operational/commercial APIs and ODA framework ✅
- **B)** GSMA writes the APIs; CAMARA signs operators; TMF runs the aggregators
- **C)** CAMARA is a GSMA subsidiary; TMF certifies devices
- **D)** All three publish competing versions of the same APIs

*Why:* Role separation is foundational ecosystem literacy for anyone building an exposure strategy.
*Source:* GSMA Open Gateway 1Q26 update (camaraproject.org, official PDF, Feb 2026)

## Q15 · Ecosystem status · expert

Per the official 1Q26 Open Gateway heatmap, the six API categories organizing the commercial portfolio are:

- **A)** Payments & Charging; Authentication & Fraud Prevention; Communications Quality; Device Information; Location Services; Computing Services ✅
- **B)** Authentication & Fraud Prevention; Location Services; Communications; Quality/Device Information; Payments & Charging
- **C)** Voice; Video; Messaging; Data; Roaming; Billing
- **D)** RAN Control; Core Control; Transport; OSS; BSS; Cloud

*Why:* [CORRECTED per SME - six categories incl. Computing Services; the five-domain distractor is the plausible near-miss grouping.]
*Source:* GSMA Open Gateway 1Q26 update (camaraproject.org, official PDF, Feb 2026)

## Q16 · Ecosystem status · expert

Per the 1Q26 Open Gateway heatmap, which commercially launched API has the largest operator count?

- **A)** SIM Swap - 75 operators ✅
- **B)** Number Verification - 64 operators
- **C)** Device Location Verification - 27 operators
- **D)** Device Status - 24 operators

*Why:* [CORRECTED per SME - heatmap: SIM Swap 75, Number Verification 64, DLV 27, Device Status 24; Device Location Retrieval only 7] All four options carry REAL numbers from the slide.
*Source:* GSMA Open Gateway 1Q26 update (camaraproject.org, official PDF, Feb 2026)

## Q17 · Ecosystem status · advanced

The Open Gateway commercial model reaches developers primarily through:

- **A)** Channel partners/aggregators federating operator API instances, alongside operators' own developer portals ✅
- **B)** A single global GSMA-operated API gateway
- **C)** App stores bundling the APIs
- **D)** Direct 5GC access credentials for developers

*Why:* The channel-partner structure (61 partners in the 1Q26 update) is how one-to-many actually works.
*Source:* GSMA Open Gateway 1Q26 update (camaraproject.org, official PDF, Feb 2026)

## Q18 · NOT-form · expert

Which is NOT true of the CAMARA Phone Number Verify operation?

- **A)** It sends a silent SMS to the device to complete verification ✅
- **B)** It uses the operator as an OIDC identity provider
- **C)** It returns a match result rather than the subscriber's number
- **D)** It authenticates against network subscription data

*Why:* The defining feature is NO SMS - a model that associates 'number verification' with OTP flows fails here.
*Source:* Network-API exposure architecture material (NEF per 3GPP TS 29.522; CAMARA mechanics)

## Q19 · NOT-form · expert

Which capability does the QoD API NOT provide?

- **A)** A guaranteed end-to-end SLA independent of radio conditions ✅
- **B)** Prioritized QoS treatment for an application's flows
- **C)** Time-bounded quality sessions requested via API
- **D)** Mapping developer intent onto 3GPP QoS mechanisms

*Why:* QoS is prioritization within physics - radio conditions still bound what is deliverable. Overclaiming SLAs is the classic sales error.
*Source:* Network-API exposure architecture material (NEF per 3GPP TS 29.522; CAMARA mechanics)

## Q20 · NOT-form · advanced

When end-user consent IS required for a CAMARA API, which is NOT a party in the consent chain?

- **A)** The device OEM approving API categories at manufacture time ✅
- **B)** The end user granting the consent
- **C)** The API provider/authorization server enforcing and recording it
- **D)** The application requesting authorized access

*Why:* [Per SME: conditional framing - consent applies when the legal basis requires it] OEMs are never a consent party.
*Source:* Network-API exposure architecture material (NEF per 3GPP TS 29.522; CAMARA mechanics)

## Q21 · NOT-form · expert

Which is NOT a CAPIF function?

- **A)** Enforcing GBR bit rates on the user plane ✅
- **B)** API invoker onboarding
- **C)** API discovery
- **D)** Security/authorization framework for API access

*Why:* CAPIF governs access to APIs; enforcement of what APIs DO lives in the core (PCF/SMF/UPF).
*Source:* 3GPP exposure framework (NEF TS 29.522; CAPIF TS 23.222; TS 23.502 exposure procedures)

## Q22 · Operational scenario · expert

A bank wants to cut account-takeover fraud in its app login. Which API combination directly addresses the two dominant attack vectors, and why is it stronger than SMS OTP?

- **A)** Number Verification (network-authenticated possession check, no interceptable SMS) plus SIM Swap (detects recent swap before trusting the number) - both are operator-derived signals that are substantially harder to manipulate from the application layer than SMS-based evidence alone ✅
- **B)** QoD plus Device Location - fast and geographic
- **C)** Carrier Billing plus KYC-Match - payment-grade identity
- **D)** SMS OTP plus email OTP - two channels beat one

*Why:* The fraud-stack pairing and the WHY (network-side signals defeat SIM-swap + SMS-intercept attacks) is the flagship monetization story.
*Source:* Network-API exposure architecture material (NEF per 3GPP TS 29.522; CAMARA mechanics)

## Q23 · Operational scenario · expert

A cloud-gaming service wants low-latency treatment for premium users during peak hours only. Which exposure product fits, and which charging unit most naturally aligns to its API resource lifecycle?

- **A)** QoD sessions - time-bounded QoS resources created and deleted via the API; the session is the natural charging unit (an economic inference, not a standardized billing rule) ✅
- **B)** A permanent network slice per gamer - billed monthly
- **C)** Number Verification - billed per call
- **D)** An MEC colocation contract - billed per rack

*Why:* Matching the service need to the API product AND its commercial unit - the VAS/monetization pairing.
*Source:* Network-API exposure architecture material (NEF per 3GPP TS 29.522; CAMARA mechanics)

## Q24 · Operational scenario · expert

A drone operator must prove to a regulator that each flight stays inside an approved corridor, without streaming precise positions to a third party. The privacy-preserving API design is:

- **A)** Device Location Verification against the corridor geofence - boolean compliance answers, no coordinate disclosure ✅
- **B)** Device Location Retrieval streamed to the regulator
- **C)** QoD with location reporting enabled
- **D)** SIM Swap polling per waypoint

*Why:* Verification-not-retrieval is the data-minimizing compliance pattern - regulatory-services flavor.
*Source:* Network-API exposure architecture material (NEF per 3GPP TS 29.522; CAMARA mechanics)

## Q25 · Operational scenario · expert

An operator's product team debates exposing QoS control via CAMARA QoD versus offering enterprises direct PCF integration. The architectural argument for the API route is:

- **A)** Standardized exposure keeps the core's trust boundary intact (NEF mediates and authenticates API invocation) and the same product works across operators via aggregation - bespoke PCF integrations do neither ✅
- **B)** Direct PCF access is technically impossible
- **C)** QoD is always cheaper for the operator to run
- **D)** PCF integration would violate 3GPP licensing

*Why:* Trust-boundary + federation reasoning is the real architecture decision; absolutist distractors are wrong.
*Source:* 3GPP exposure framework (NEF TS 29.522; CAPIF TS 23.222; TS 23.502 exposure procedures)

## Q26 · Operational scenario · expert

A retailer wants age-appropriate content controls using operator data. Which response pattern minimizes unnecessary personal-data disclosure while serving the retailer's need?

- **A)** An attribute-check API (KYC Age Verification-style) answering 'is the subscriber over 18: yes/no' - never returning birthdate or identity attributes ✅
- **B)** Returning the subscriber's full KYC record under NDA
- **C)** Selling anonymized birthdates in bulk
- **D)** Having the retailer query UDM directly

*Why:* Boolean attribute checks generalize the KYC-Match/data-minimization pattern to any eligibility decision.
*Source:* Network-API exposure architecture material (NEF per 3GPP TS 29.522; CAMARA mechanics)

## Q27 · Operational scenario · expert

Why do different network APIs naturally support different monetization events?

- **A)** Because the value event differs per API class: a fraud check delivers value at each decision, a QoS session over its lifetime, a payment at transaction completion - charging models tend to follow the value event ✅
- **B)** Because 3GPP mandates a billing model per API
- **C)** Because aggregators set uniform global prices
- **D)** They do not - all network APIs monetize identically

*Why:* [REWRITTEN per SME: tests value-event reasoning instead of asserting universal billing rules.]
*Source:* Network-API exposure architecture material (NEF per 3GPP TS 29.522; CAMARA mechanics)

## Q28 · Business-model scenario · expert

An MVNO asks whether it can join Open Gateway offerings without owning a 5G core exposure stack. The structurally accurate answer (commercial arrangements vary) is:

- **A)** Yes via its host operator's exposure platform or an aggregator - but the network-derived signals (SIM swap, location, QoS) still originate from the host network, which shapes the commercial split ✅
- **B)** No - only facilities-based operators may expose APIs
- **C)** Yes - MVNOs can synthesize the signals themselves
- **D)** Only if the MVNO builds its own NEF

*Why:* Where the signal originates determines who must be in the value chain - the structural insight for wholesale/BSS discussions.
*Source:* Network-API exposure architecture material (NEF per 3GPP TS 29.522; CAMARA mechanics)

## Q29 · 1Q26 report precision · expert

Per the official 1Q26 Open Gateway update, how many commercial API instances are launched, across how many networks and markets?

- **A)** 280 instances across 85 networks in 50 markets ✅
- **B)** 237 instances across 85 networks in 50 markets
- **C)** 280 instances across 81 networks in 61 markets
- **D)** 237 instances across 81 networks in 50 markets

*Why:* [CORRECTED per SME: 280 = commercial instances; 237 = certified API assets - now used as the strongest distractor. 81/61 are the operator-group/channel-partner counts, real numbers from the same deck.]
*Source:* GSMA Open Gateway 1Q26 update (camaraproject.org, official PDF, Feb 2026)

## Q30 · 1Q26 report precision · expert

Per the 1Q26 heatmap, the operator counts for SIM Swap and Number Verification are:

- **A)** SIM Swap 75, Number Verification 64 ✅
- **B)** SIM Swap 64, Number Verification 75
- **C)** SIM Swap 27, Number Verification 24
- **D)** SIM Swap 95, Number Verification 84

*Why:* [CORRECTED per SME: 75 belongs to SIM Swap, not Device Location Retrieval (which has only 7)] The reversal distractor remains the trap.
*Source:* GSMA Open Gateway 1Q26 update (camaraproject.org, official PDF, Feb 2026)

## Q31 · 1Q26 report precision · expert

The 1Q26 update reports CAMARA's API pipeline as:

- **A)** 33 tagged released APIs with 40 in development ✅
- **B)** 40 tagged released with 33 in development
- **C)** 20 released with 60 in development
- **D)** 53 released with 20 in development

*Why:* Released-vs-pipeline pair with a reversal distractor.
*Source:* GSMA Open Gateway 1Q26 update (camaraproject.org, official PDF, Feb 2026)

## Q32 · 1Q26 report precision · expert

Regional API-instance distribution in the 1Q26 update is led by:

- **A)** Europe (98), then APAC (56) and LATAM (52) ✅
- **B)** LATAM (98), then Europe (56) and APAC (52)
- **C)** APAC (98), then LATAM (56) and Europe (52)
- **D)** North America (98), then Europe (56)

*Why:* Region-to-number mapping; rotation distractors.
*Source:* GSMA Open Gateway 1Q26 update (camaraproject.org, official PDF, Feb 2026)

## Q33 · 1Q26 report precision · expert

The Open Gateway ecosystem scale reported in 1Q26 is:

- **A)** 81 operator groups and 61 channel partners representing 292 networks ✅
- **B)** 61 operator groups and 81 channel partners representing 292 networks
- **C)** 45 operator groups and 30 channel partners representing 150 networks
- **D)** 120 operator groups and 90 channel partners representing 400 networks

*Why:* Operator-vs-partner counts with a swap distractor.
*Source:* GSMA Open Gateway 1Q26 update (camaraproject.org, official PDF, Feb 2026)

## Q34 · 1Q26 report precision · expert

On market demand, the 1Q26 update identifies the strongest-demand API as:

- **A)** Quality on Demand (17 markets), followed by Scam Signal (15) ✅
- **B)** Scam Signal (17 markets), followed by QoD (15)
- **C)** Number Verification (17 markets), followed by KYC-Match (15)
- **D)** Carrier Billing (17 markets), followed by QoD (15)

*Why:* Demand differs from deployment (Device Location leads adoption; QoD leads demand) - the join across two report sections.
*Source:* GSMA Open Gateway 1Q26 update (camaraproject.org, official PDF, Feb 2026)

## Q35 · 1Q26 report precision · expert

The 1Q26 update's coverage claim for aligned operator networks is:

- **A)** About 80% of mobile connections, with 27 markets at 100% API alignment ✅
- **B)** About 50% of mobile connections, with 12 markets at 100% alignment
- **C)** About 95% of mobile connections, with 45 markets at full alignment
- **D)** About 30% of mobile connections, with 5 markets at full alignment

*Why:* Coverage + alignment pair, adjacency-scaled distractors.
*Source:* GSMA Open Gateway 1Q26 update (camaraproject.org, official PDF, Feb 2026)

## Q36 · Mechanics join · expert

Which mapping correctly distinguishes the nature of the underlying network information per API?

- **A)** Number Verification -> network-authenticated subscription/number binding; SIM Swap -> operator SIM-change event history; Location Retrieval -> network positioning information ✅
- **B)** Number Verification -> positioning information; SIM Swap -> policy state; Location -> SIM-change history
- **C)** All three derive from the same subscriber profile record
- **D)** All three are computed inside the NEF's local database

*Why:* [REWRITTEN per SME: CAMARA abstracts the internal realization - tests the NATURE of the signal, not a specific NF placement.]
*Source:* Network-API exposure architecture material (NEF per 3GPP TS 29.522; CAMARA mechanics)

## Q37 · Mechanics join · expert

A QoD session request succeeds but the user's measured latency barely changes. The MOST likely architectural explanation is:

- **A)** The dominant latency lies outside the operator-controlled QoS path - for example application-server or external-network latency - so improved QoS treatment barely moves total end-to-end latency ✅
- **B)** The PCF silently rejected the request
- **C)** QoD only takes effect after 24 hours
- **D)** The UE must reboot to apply QoS

*Why:* Scope-of-control reasoning: the QoS flow governs the 3GPP segment; end-to-end latency has other components.
*Source:* Network-API exposure architecture material (NEF per 3GPP TS 29.522; CAMARA mechanics)

## Q38 · Mechanics join · expert

Why was CIBA + TS.43 temporary-token support added in newer CAMARA Number Verification releases (2.0.0+)?

- **A)** To support Number Verification when the device is on Wi-Fi rather than an operator-identifiable mobile-data bearer - the historical cellular-path dependency limited coverage ✅
- **B)** To replace OAuth entirely in the CAMARA stack
- **C)** To let SMS OTP work faster over Wi-Fi
- **D)** To remove the need for user authorization

*Why:* [REWRITTEN per SME: the API evolved - the Wi-Fi limitation is now the MOTIVATION for CIBA/TS.43, which is both current and harder.]
*Source:* Network-API exposure architecture material (NEF per 3GPP TS 29.522; CAMARA mechanics)
