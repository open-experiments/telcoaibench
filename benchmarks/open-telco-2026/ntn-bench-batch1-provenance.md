# ntn_bench — Batch 1 v2 HARDENED DRAFT (45 questions) — for SME review

**Scope:** NTN (NR-NTN/IoT-NTN, D2D, spectrum, orbits) + private networks (SNPN/PNI-NPN,
CAG, onboarding, deployment models). Functional knowhow only, per the settled recipe -
no archival trivia. Sources: official 3GPP NTN/NPN pages + Ericsson Technology Review
(the one non-3GPP source, used for D2D market/engineering facts 3GPP does not publish).
Correct answer shown as A (shuffled at freeze). Pilot results delivered alongside.

---

## Q1 · NTN mechanism · expert

How does a Rel-17 NR-NTN UE compensate for satellite delay and Doppler?

- **A)** Position from its own GNSS; ephemeris from system information broadcast; UE pre-compensates its uplink ✅
- **B)** Position from network positioning; ephemeris from system information; gNB post-compensates downlink
- **C)** Position from its own GNSS; ephemeris fetched over user-plane data; UE pre-compensates its uplink
- **D)** Position from cell triangulation; ephemeris from GNSS almanac; UE pre-compensates both directions

*Why:* UE-side active pre-compensation (GNSS + ephemeris) is the core NR-NTN design decision. [Re-sourced to official 3GPP NTN material per SME.]
*Source:* 3GPP NTN overview (3gpp.org/technologies/ntn-overview)

## Q2 · NTN mechanism · expert

Which HARQ adaptation does NR-NTN make for satellite delay, and why?

- **A)** From 16 to 32 processes - to keep the pipeline full over satellite RTT so HARQ does not stall awaiting feedback ✅
- **B)** From 16 to 24 processes - to reduce memory on low-cost UEs
- **C)** From 8 to 16 processes - satellite links need fewer parallel processes
- **D)** From 16 to 64 processes - to support multi-satellite carrier aggregation

*Why:* More in-flight HARQ processes prevent HARQ stalling over the long satellite RTT and preserve pipeline utilization/throughput. They do not reduce propagation delay. [Rationale corrected per SME.]
*Source:* 3GPP NTN overview (3gpp.org/technologies/ntn-overview)

## Q3 · NTN mechanism · advanced

The difference between transparent and regenerative satellite payloads is:

- **A)** Transparent payloads relay the radio signal (bent pipe) with the gNB on the ground; regenerative payloads run network functions - up to gNB/5GS functions - on board the satellite ✅
- **B)** Transparent payloads are for GEO only, regenerative for LEO only
- **C)** Regenerative payloads cannot support handover
- **D)** Transparent payloads decode and re-encode every packet on board

*Why:* Rel-19 explicitly adds architecture support for 5GS functions on board (regenerative); transparent = bent-pipe with ground gNB.
*Source:* 3GPP official NTN article (3gpp.org/news-events/3gpp-news/5g-ntn)

## Q4 · NTN mechanism · expert

Rel-19 IoT-NTN store-and-forward operation includes support for 'feeder link switchover'. Why does S&F specifically need this?

- **A)** A S&F satellite stores traffic while feeder connectivity is unavailable and forwards it after a feeder link becomes available - with switchover between feeder links supported ✅
- **B)** Because service links and feeder links use the same frequency
- **C)** To let UEs switch between satellites mid-message
- **D)** Feeder switchover is unrelated to S&F; it is a separate Rel-19 item

*Why:* S&F is defined 'based on regenerative payload, including the support of feeder link switchover' - the stored data must drain via whichever feeder connectivity appears.
*Source:* 3GPP official NTN article (3gpp.org/news-events/3gpp-news/5g-ntn)

## Q5 · NTN mechanism · advanced

Rel-19 NR-NTN Phase 3 adds 'broadcast service area notification'. Its operational purpose is:

- **A)** Informing devices about the geographic area where a broadcast service is available from the satellite ✅
- **B)** Emergency alerts only
- **C)** Notifying ground stations of satellite positions
- **D)** Advertising tariffs to roaming UEs

*Why:* Listed as an NR-NTN Ph3 capability alongside UL capacity and terminal performance.
*Source:* 3GPP official NTN article (3gpp.org/news-events/3gpp-news/5g-ntn)

## Q6 · NTN mechanism · expert

A proprietary 'unmodified 4G from LEO' direct-to-device system compensates delay/Doppler network-side against a reference point. Its fundamental service limitation is:

- **A)** Residual delay/Doppler errors grow as a UE moves away from the reference point and can exceed LTE tolerances - constraining usable beam footprint, and long RTT may even require disabling HARQ ✅
- **B)** It cannot carry voice at all
- **C)** It requires new smartphone chipsets, defeating its purpose
- **D)** It only works over GEO satellites

*Why:* Network-side compensation is exact only near the reference point; NR-NTN's UE-side approach removes this constraint. HARQ may need disabling due to RTT.
*Source:* Ericsson Technology Review: satellite direct-to-device (ericsson.com)

## Q7 · NTN mechanism · advanced

For a Rel-17+ NR-NTN UE, what must be available BEFORE it can transmit its first uplink correctly?

- **A)** Its own GNSS position fix and the satellite ephemeris/parameters from system information ✅
- **B)** A dedicated ranging channel assignment from the satellite
- **C)** A terrestrial anchor cell connection
- **D)** Nothing - uplink timing is corrected after RACH

*Why:* Pre-compensation needs position + ephemeris up front; cold-start/GNSS-denied implications. [Re-sourced to official 3GPP NTN material per SME.]
*Source:* 3GPP NTN overview (3gpp.org/technologies/ntn-overview)

## Q8 · NTN mechanism · expert

Which IoT-NTN + orbit combination does 3GPP-aligned industry material describe as well-suited for basic text-messaging services today?

- **A)** NB-IoT-NTN over existing GEO satellites ✅
- **B)** eMTC over LEO mega-constellations only
- **C)** NR-NTN FR2 over MEO
- **D)** LTE Cat-4 over HEO

*Why:* NB-IoT-NTN + GEO is the commercially deployed basic-messaging path - counterintuitive since GEO has the longest delay.
*Source:* Ericsson Technology Review: satellite direct-to-device (ericsson.com)

## Q9 · NTN release availability · advanced

The foundational NR-NTN and IoT-NTN specifications were completed in which release, with commercial deployments now ongoing?

- **A)** Rel-17, with optimizations in Rel-18 ✅
- **B)** Rel-15, with optimizations in Rel-16
- **C)** Rel-19 - deployments have not started
- **D)** Rel-16, with optimizations in Rel-17

*Why:* Rel-17 is the NTN foundation; Rel-18 optimized; deployments are commercial reality per 3GPP.
*Source:* 3GPP official NTN article (3gpp.org/news-events/3gpp-news/5g-ntn)

## Q10 · NTN release availability · expert

Which pairing correctly describes the two Rel-19 NTN Phase 3 work areas?

- **A)** NR-NTN: terminal performance, UL capacity, broadcast area notification, regenerative payloads, RedCap in FR1 NTN bands | IoT-NTN: store-and-forward on regenerative payload with feeder switchover, UL capacity ✅
- **B)** NR-NTN: FR2 satellite access | IoT-NTN: voice services
- **C)** NR-NTN: store-and-forward | IoT-NTN: regenerative payloads only
- **D)** Both: transparent-payload-only architectures

*Why:* The two Ph3 scopes must not be cross-assigned - S&F is the IoT-NTN item; regenerative 5GS-on-board is listed under NR-NTN architecture.
*Source:* 3GPP official NTN article (3gpp.org/news-events/3gpp-news/5g-ntn)

## Q11 · NTN release availability · advanced

A device vendor wants satellite connectivity for a RedCap-class wearable. The standards path that makes this possible is:

- **A)** Rel-19 support for RedCap devices within FR1 NTN spectrum bands ✅
- **B)** Rel-17 RedCap already included NTN
- **C)** Rel-18 eRedCap FR2 NTN
- **D)** There is no standardized RedCap-over-satellite path

*Why:* RedCap-in-FR1-NTN is an explicit Rel-19 NR-NTN Ph3 item - the wearable/asset-tracker satellite path.
*Source:* 3GPP official NTN article (3gpp.org/news-events/3gpp-news/5g-ntn)

## Q12 · NTN release availability · expert

Direct-to-device NR-NTN service requires which minimum device capability?

- **A)** A Rel-17+ chipset implementing NTN pre-compensation - existing pre-Rel-17 smartphones cannot run standard NR-NTN ✅
- **B)** Any 5G smartphone via software update
- **C)** An external satellite antenna
- **D)** eSIM support only

*Why:* The Rel-17+ chipset requirement is why proprietary unmodified-4G approaches exist for legacy handsets - a key market-structure fact.
*Source:* Ericsson Technology Review: satellite direct-to-device (ericsson.com)

## Q13 · NTN spectrum · expert

Under the current regulatory frameworks, the two spectrum approaches for satellite direct-to-device, with their defining trade-off, are:

- **A)** MSS L/S bands (internationally allocated, established coexistence rules) vs terrestrial mobile spectrum reused via MNO-SNO partnership (mature device ecosystem, but non-interference/non-protection operation with exclusion zones) ✅
- **B)** FR2 mmWave vs unlicensed 6 GHz
- **C)** Broadcast TV bands vs maritime VHF
- **D)** Both approaches require new spectrum auctions

*Why:* MSS = regulatory clarity, terrestrial reuse = ecosystem leverage at the cost of interference management burden - the central commercial-design decision.
*Source:* Ericsson Technology Review: satellite direct-to-device (ericsson.com)

## Q14 · NTN spectrum · advanced

LEO vs GEO orbital characteristics relevant to service design:

- **A)** LEO below ~2,000 km with ~90-minute orbit; GEO at ~35,800 km, geostationary ✅
- **B)** LEO below ~2,000 km with ~90-minute orbit; GEO at ~3,580 km, geostationary
- **C)** LEO below ~8,000 km with ~six-hour orbit; GEO at ~35,800 km, geostationary
- **D)** LEO below ~2,000 km with ~24-hour orbit; GEO at ~35,800 km, geosynchronous-inclined

*Why:* [Re-sourced per SME - the Ericsson article contains an altitude transposition typo] Rounded precision; the engineering distinction (period, geostationarity, constellation need) is what matters.
*Source:* Standard orbital mechanics reference (GEO ~35,786 km; ITU)

## Q15 · NTN spectrum · expert

Under current MNO-SNO terrestrial-spectrum-reuse frameworks, the satellite operator's obligations are characterized as:

- **A)** Non-interference and non-protection: the satellite service must not interfere with terrestrial use and cannot claim protection from it, typically enforced with exclusion zones and interference management ✅
- **B)** Full co-primary status with the MNO
- **C)** Exclusive use of the band over the whole country
- **D)** Protection from terrestrial interference but not vice versa

*Why:* The regulatory asymmetry (satellite is the secondary-style user) shapes coverage commitments an operator can make - regulatory-services relevance.
*Source:* Ericsson Technology Review: satellite direct-to-device (ericsson.com)

## Q16 · NPN design · foundation

The defining difference between an SNPN and a PNI-NPN is:

- **A)** An SNPN operates without relying on PLMN network functions; a PNI-NPN is deployed with PLMN support, from shared infrastructure up to a dedicated slice ✅
- **B)** SNPN uses unlicensed spectrum, PNI-NPN licensed
- **C)** SNPN is for factories, PNI-NPN for offices
- **D)** SNPN cannot support 5G SA

*Why:* The PLMN-dependency axis is THE private-network architecture decision.
*Source:* 3GPP official NPN page (3gpp.org/technologies/npn)

## Q17 · NPN design · advanced

An SNPN is identified by:

- **A)** The combination of a PLMN ID and a Network Identifier (NID), introduced in Rel-16 ✅
- **B)** A dedicated country code
- **C)** Its CAG ID alone
- **D)** An SSID-like text string

*Why:* PLMN ID + NID enables discovery/selection of standalone private networks.
*Source:* 3GPP official NPN page (3gpp.org/technologies/npn)

## Q18 · NPN design · expert

Why did Rel-16 introduce Closed Access Groups (CAG) for PNI-NPNs when network slicing already existed?

- **A)** Network slicing differentiates services/resources but does not itself provide cell-level membership access control - CAG restricts access to CAG cells to authorized subscribers ✅
- **B)** CAG replaces slicing entirely in private networks
- **C)** Slicing is not available in PNI-NPN deployments
- **D)** CAG exists to encrypt the air interface

*Why:* 3GPP's own rationale: cell-access prevention 'where network slicing alone proves insufficient' - a precise access-control layering fact.
*Source:* 3GPP official NPN page (3gpp.org/technologies/npn)

## Q19 · NPN design · expert

Rel-17 NPN onboarding introduces the 'Credentials Holder' concept. Its function is:

- **A)** Allowing the credentials used to access an SNPN to be owned/managed by an entity separate from the SNPN operator, with Onboarding Networks provisioning devices remotely ✅
- **B)** A hardware security module inside the gNB
- **C)** The PLMN always holds all NPN credentials
- **D)** A SIM-card printing service

*Why:* Separating credential ownership from network operation is what makes enterprise/vertical deployment models workable at scale.
*Source:* 3GPP official NPN page (3gpp.org/technologies/npn)

## Q20 · NPN design · advanced

In Rel-16, a UE in an SNPN reaches public PLMN services (and vice versa) via:

- **A)** The non-3GPP access pattern through an N3IWF - treating the other network as untrusted access ✅
- **B)** Native dual registration on both networks simultaneously via NG-RAN
- **C)** A roaming agreement identical to international roaming
- **D)** It cannot - SNPNs are fully isolated by definition

*Why:* The N3IWF overlay path is the Rel-16 service-continuity mechanism; Rel-18 widens non-3GPP access options (wireline, WLAN).
*Source:* 3GPP official NPN page (3gpp.org/technologies/npn)

## Q21 · NPN design · advanced

Rel-18 NPN enhancements include:

- **A)** Equivalent SNPN mobility, SNPN access via non-3GPP access (including wireline/WLAN), localized services, and charging models ✅
- **B)** The first definition of CAG
- **C)** Removal of the NID concept
- **D)** Merging SNPN and PNI-NPN into one architecture

*Why:* The Rel-18 package is about mobility between related SNPNs and broader access/commercial models.
*Source:* 3GPP official NPN page (3gpp.org/technologies/npn)

## Q22 · NPN design · expert

The four canonical NPN deployment models (5G-ACIA-aligned) in increasing PLMN involvement are:

- **A)** Isolated SNPN; shared RAN; shared RAN and control plane; fully PLMN-hosted ✅
- **B)** Slice-only; CAG-only; hybrid; roaming
- **C)** Campus; metro; regional; national
- **D)** Unlicensed; lightly licensed; licensed; leased

*Why:* The spectrum of who-runs-what (RAN, control, data) is the solution-architecture menu for enterprise deals.
*Source:* 3GPP official NPN page (3gpp.org/technologies/npn)

## Q23 · NPN design · expert

Rel-19/20 NPN work adds which capability pair?

- **A)** ProSe (proximity services) support and security for a PLMN hosting an NPN ✅
- **B)** NID introduction and CAG
- **C)** Onboarding and credentials holder
- **D)** IMS emergency and PWS

*Why:* Release-attribution trap: B is Rel-16, C is Rel-17, D is Rel-17 - only ProSe + hosting boundaries are the current wave.
*Source:* 3GPP official NPN page (3gpp.org/technologies/npn)

## Q24 · NOT-form · expert

Which is NOT a standardized 3GPP path for satellite direct-to-device?

- **A)** Rel-17 NR sidelink relayed via satellite reflectors ✅
- **B)** NR-NTN with UE pre-compensation (Rel-17+)
- **C)** NB-IoT-NTN / eMTC-NTN (IoT-NTN)
- **D)** RedCap over FR1 NTN bands (Rel-19)

*Why:* Sidelink-via-reflector is invented; the other three are the real standardized ladder.
*Source:* 3GPP official NTN article (3gpp.org/news-events/3gpp-news/5g-ntn)

## Q25 · NOT-form · expert

Which capability does Rel-19 IoT-NTN store-and-forward NOT provide?

- **A)** Real-time interactive voice service during feeder-link outages ✅
- **B)** Collecting UE uplink data while disconnected from ground stations
- **C)** Delivering stored data after feeder-link connectivity resumes
- **D)** Operation on a regenerative payload

*Why:* S&F is inherently delay-tolerant; anything real-time contradicts the store-then-forward model - service-design boundary.
*Source:* 3GPP official NTN article (3gpp.org/news-events/3gpp-news/5g-ntn)

## Q26 · NOT-form · advanced

Which is NOT a Rel-16 NPN mechanism?

- **A)** Remote onboarding via an Onboarding Network ✅
- **B)** Network Identifier (NID) for SNPN identification
- **C)** Closed Access Groups for PNI-NPN cell access control
- **D)** SNPN-to-PLMN service access via N3IWF

*Why:* Onboarding/ONN is Rel-17; the rest are the Rel-16 foundation - release-boundary NOT-form.
*Source:* 3GPP official NPN page (3gpp.org/technologies/npn)

## Q27 · NOT-form · expert

A vendor claims its 'fully 3GPP-standard Rel-17 NTN' service works on all existing smartphones without hardware changes. Which fact contradicts this?

- **A)** Standard NR-NTN requires Rel-17+ chipset support for UE-side pre-compensation - serving unmodified legacy phones requires a proprietary network-side approach instead ✅
- **B)** Rel-17 NTN requires FR2 antennas
- **C)** 3GPP NTN only supports IoT devices
- **D)** Satellites cannot transmit on terrestrial frequencies at all

*Why:* Claim-checking question: the chipset requirement is exactly what separates standard NR-NTN from proprietary unmodified-4G offerings.
*Source:* Ericsson Technology Review: satellite direct-to-device (ericsson.com)

## Q28 · Operational scenario · expert

A utility deploys sensors along remote transmission lines: a few bytes daily, no terrestrial coverage, decade-long deployment, delay-tolerant. The standards-aligned technical fit is:

- **A)** IoT-NTN (NB-IoT-NTN), with Rel-19 store-and-forward removing the need for continuous feeder-link coverage over sparse constellations ✅
- **B)** NR-NTN broadband with regenerative payloads
- **C)** A nationwide SNPN along the lines
- **D)** RedCap over terrestrial roaming

*Why:* Delay-tolerant tiny payloads = IoT-NTN + S&F; NR-NTN or SNPN towers are massive overkill - cost-fit reasoning.
*Source:* 3GPP official NTN article (3gpp.org/news-events/3gpp-news/5g-ntn)

## Q29 · Operational scenario · expert

A service provider's hard requirement is compatibility with the largest installed base of unmodified LTE smartphones. Which satellite D2D approach best satisfies that requirement, and what is its principal radio-design trade-off?

- **A)** An unmodified-4G D2D system using terrestrial mobile spectrum - network-side delay/Doppler compensation limits design flexibility and can constrain beam footprint and capacity ✅
- **B)** Standard NR-NTN - all LTE phones support it via software update
- **C)** IoT-NTN - LTE smartphones embed NB-IoT-NTN stacks by default
- **D)** A maritime SNPN with CAG

*Why:* [REWRITTEN per SME] The unmodified-device requirement forces the proprietary network-compensated approach; its beam-footprint/capacity constraint is the engineering price.
*Source:* Ericsson Technology Review: satellite direct-to-device (ericsson.com)

## Q30 · Operational scenario · expert

An automotive plant requires that production user-plane data never leaves the site AND that production connectivity survives any public-network outage. The architecture satisfying both constraints is:

- **A)** An isolated SNPN: on-premises core and RAN, no dependency on PLMN network functions ✅
- **B)** A PNI-NPN with a dedicated slice and local breakout
- **C)** CAG on the public macro network with an SLA
- **D)** Dual-SIM devices on two different PLMNs

*Why:* [REWRITTEN per SME - one architecture under one precise constraint set] Both constraints map uniquely to the isolated-SNPN deployment model.
*Source:* 3GPP official NPN page (3gpp.org/technologies/npn)

## Q31 · Operational scenario · expert

A stadium owner wants one radio infrastructure serving multiple MNOs' subscribers plus a private network for operations. In NPN deployment-model terms this is:

- **A)** A shared-RAN arrangement combining public-network RAN sharing for the MNOs with an NPN for operations - control/user planes segregated per network ✅
- **B)** An isolated SNPN with roaming
- **C)** Four separate parallel RANs
- **D)** A CAG-only configuration on one MNO

*Why:* The shared-RAN NPN model is the standards frame for neutral host - VAS/monetization angle.
*Source:* 3GPP official NPN page (3gpp.org/technologies/npn)

## Q32 · Operational scenario · expert

A mining company operates pits in three countries and wants its vehicles' credentials managed once, centrally, while each site runs its own local SNPN. The Rel-17 mechanism enabling this is:

- **A)** The Credentials Holder separation - sites' SNPNs authenticate devices against centrally-held credentials, with onboarding networks provisioning new vehicles remotely ✅
- **B)** International roaming agreements between the SNPNs
- **C)** One global SNPN spanning all countries
- **D)** Copying SIM profiles between sites manually

*Why:* Credentials Holder is exactly the multi-site enterprise identity pattern - OSS/BSS relevance.
*Source:* 3GPP official NPN page (3gpp.org/technologies/npn)

## Q33 · Operational scenario · expert

A national regulator asks whether approving a satellite operator's reuse of an MNO's terrestrial spectrum could degrade rural terrestrial service. The technically-grounded answer is:

- **A)** The satellite service operates under non-interference/non-protection obligations, with exclusion zones and interference management used to protect terrestrial operation - correspondingly constraining satellite coverage/capacity commitments ✅
- **B)** Satellite always overrides terrestrial priority
- **C)** The two cannot share spectrum under any framework
- **D)** Interference is impossible because of the altitude difference

*Why:* Regulatory-services scenario: the asymmetric protection framework answers both the risk and its flip side.
*Source:* Ericsson Technology Review: satellite direct-to-device (ericsson.com)

## Q34 · Operational scenario · expert

An agency needs off-grid, low-bandwidth messaging for field teams and can procure compatible terminals. Which standardized NTN family is the most mature technical fit?

- **A)** IoT-NTN (NB-IoT-NTN) - commercially deployed for exactly this message-class service ✅
- **B)** Rel-19 regenerative-payload NR-NTN broadband
- **C)** A national SNPN
- **D)** FR2 satellite links to handhelds

*Why:* [REWRITTEN per SME - service fit, not procurement-landscape snapshot] Maturity + message-class fit points to IoT-NTN.
*Source:* Ericsson Technology Review: satellite direct-to-device (ericsson.com)

## Q35 · NPN release ladder · expert

Closed Access Groups (CAG) for PNI-NPN cell-access control were introduced in:

- **A)** Rel-16 ✅
- **B)** Rel-15
- **C)** Rel-17
- **D)** Rel-18

*Why:* Adjacent-release distractors; Rel-16 with NID and formal NPN definitions.
*Source:* 3GPP official NPN page (3gpp.org/technologies/npn)

## Q36 · NPN release ladder · expert

The Credentials Holder concept and NPN remote onboarding/provisioning arrived in:

- **A)** Rel-17 ✅
- **B)** Rel-16
- **C)** Rel-18
- **D)** Rel-19

*Why:* Rel-17 package (with IMS emergency and PWS for SNPN).
*Source:* 3GPP official NPN page (3gpp.org/technologies/npn)

## Q37 · NPN release ladder · expert

Equivalent-SNPN mobility and SNPN access via non-3GPP access (wireline/WLAN) arrived in:

- **A)** Rel-18 ✅
- **B)** Rel-17
- **C)** Rel-16
- **D)** Rel-19

*Why:* The Rel-18 package with localized services and charging models.
*Source:* 3GPP official NPN page (3gpp.org/technologies/npn)

## Q38 · NPN release ladder · expert

IMS emergency services and Public Warning System support for SNPNs were added in:

- **A)** Rel-17 ✅
- **B)** Rel-16
- **C)** Rel-18
- **D)** Rel-15

*Why:* Rel-17 - often misattributed to the Rel-16 foundation.
*Source:* 3GPP official NPN page (3gpp.org/technologies/npn)

## Q39 · NPN release ladder · advanced

Rel-15's relationship to private networks is best described as:

- **A)** A private-network concept with subset support only - the formal NPN framework came in Rel-16 ✅
- **B)** Full SNPN support from day one
- **C)** No private-network capability at all
- **D)** CAG without NID

*Why:* The subset-support nuance is the trap; both extremes are wrong.
*Source:* 3GPP official NPN page (3gpp.org/technologies/npn)

## Q40 · Functional mapping · expert

An operator's OSS must provision, configure, and assure its private networks through standard interfaces. Which 3GPP domain owns NPN lifecycle management?

- **A)** The management and orchestration framework (SA5's NPN management specifications, e.g., TS 28.557) ✅
- **B)** The 5GC architecture specifications (SA2) alone
- **C)** RAN OAM via F1-AP
- **D)** GSMA operational guidelines, outside 3GPP

*Why:* [REPLACED spec-digit Q per SME] Tests knowing WHERE the capability lives functionally; the spec number is supporting detail, not the answer.
*Source:* 3GPP official NPN page (3gpp.org/technologies/npn)

## Q41 · Functional mapping · expert

For the device ecosystem, the key difference between MSS-band D2D and terrestrial-spectrum-reuse D2D is:

- **A)** MSS bands require devices to add satellite band support; terrestrial reuse works with the bands existing devices already implement ✅
- **B)** MSS bands work with all existing devices; terrestrial reuse requires new chipsets
- **C)** Both approaches require identical new device hardware
- **D)** Neither approach can serve smartphones

*Why:* [REPLACED spec-digit Q per SME] The ecosystem-leverage asymmetry is the functional reason terrestrial reuse exists at all.
*Source:* Ericsson Technology Review: satellite direct-to-device (ericsson.com)

## Q42 · NTN precision · expert

The satellite link carrying traffic between the satellite and the ground station (vs the UE) is called:

- **A)** The feeder link (service link is satellite-to-UE) ✅
- **B)** The service link (feeder link is satellite-to-UE)
- **C)** The inter-satellite link
- **D)** The anchor link

*Why:* Term-swap trap - S&F and switchover questions are unanswerable without this distinction.
*Source:* 3GPP official NTN article (3gpp.org/news-events/3gpp-news/5g-ntn)

## Q43 · NTN precision · expert

MSS spectrum internationally allocated for mobile satellite service sits in which bands?

- **A)** L and S bands ✅
- **B)** C and Ku bands
- **C)** Ka band only
- **D)** FR2 mmWave bands

*Why:* L/S band precision; C/Ku are fixed-satellite service - the plausible confusion.
*Source:* Ericsson Technology Review: satellite direct-to-device (ericsson.com)

## Q44 · Scenario-inversion · expert

A customer insists LEO always beats GEO for their IoT message-collection service (500 sensors, one reading per day, no latency requirement). The technically honest response is:

- **A)** For delay-tolerant tiny payloads, existing GEO IoT-NTN can serve immediately with continuous regional coverage from one satellite - LEO's latency advantage is irrelevant here, and it brings constellation and mobility-management complexity ✅
- **B)** Agree - GEO cannot carry IoT traffic
- **C)** Agree - LEO is always cheaper
- **D)** Neither works without Rel-19 features

*Why:* Counterintuitive-correct: the popular LEO>GEO intuition fails when latency does not matter - selection reasoning under real constraints.
*Source:* Ericsson Technology Review: satellite direct-to-device (ericsson.com)

## Q45 · Scenario-inversion · expert

An enterprise architect proposes 'PNI-NPN with a dedicated slice' to guarantee production continues if the public network has a nationwide outage. The flaw is:

- **A)** A PNI-NPN relies on PLMN functions, so it cannot provide failure independence from those dependencies - a survivability requirement demanding autonomous local operation points toward SNPN ✅
- **B)** Slices cannot carry industrial traffic
- **C)** PNI-NPN cannot use licensed spectrum
- **D)** There is no flaw - slices are outage-isolated

*Why:* Tests whether the model connects the PLMN-dependency definition to its failure-mode consequence.
*Source:* 3GPP official NPN page (3gpp.org/technologies/npn)
