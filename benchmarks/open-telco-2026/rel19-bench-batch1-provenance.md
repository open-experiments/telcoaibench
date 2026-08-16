# rel19_bench — Batch 1 v3 FUNCTIONAL KNOWHOW  v3.1 (52 questions) 

---

## Q1 · Capability limits · foundation

Rel-18 eRedCap targets a peak data rate cap of approximately:

- **A)** 10 Mbps ✅
- **B)** 100 Mbps
- **C)** 1 Gbps
- **D)** 250 kbps

*Why:* [KEPT - caught muse] The 10 Mbps ceiling determines which IoT/wearable services eRedCap can carry.
*Source:* 3GPP RedCap articles (3gpp.org/technologies/nr-redcap-glimpse; redcap-gsa-article01)

## Q2 · Capability limits · advanced

Rel-19 MIMO Phase 5 extends CSI support up to how many ports, and adds which uplink antenna configuration?

- **A)** 128 CSI ports; 3-Tx uplink ✅
- **B)** 64 CSI ports; 2-Tx uplink
- **C)** 256 CSI ports; 8-Tx uplink
- **D)** 32 CSI ports; 1-Tx uplink

*Why:* [KEPT - caught BOTH] Port count bounds MU-MIMO precoding resolution; 3-Tx UL bounds uplink capacity planning.
*Source:* 3GPP Rel-19 summary, TSGs#112 June 2026 (3gpp.org official)

## Q3 · Capability limits · advanced

Classic Rel-17 RedCap constrains UE bandwidth in FR1 to:

- **A)** 20 MHz ✅
- **B)** 10 MHz
- **C)** 40 MHz
- **D)** 5 MHz

*Why:* 20 MHz cap - drives cell planning and scheduler treatment of RedCap users.
*Source:* 3GPP RedCap articles (3gpp.org/technologies/nr-redcap-glimpse; redcap-gsa-article01)

## Q4 · Capability limits · expert

Ambient IoT Device 1 tolerates an initial sampling frequency offset of up to:

- **A)** 1e5 ppm ✅
- **B)** 1e3 ppm
- **C)** 1e4 ppm
- **D)** 1e6 ppm

*Why:* Crystal-less design tolerance - dictates the whole non-coherent waveform design.
*Source:* 3GPP Rel-19 Ambient IoT article (3gpp.org/technologies/rel19-aiot)

## Q5 · Capability limits · advanced

Ambient IoT Device 1 peak power consumption is approximately:

- **A)** 1 microwatt ✅
- **B)** 1 milliwatt
- **C)** 100 microwatts
- **D)** 10 nanowatts

*Why:* ~1 uW - the constraint that removes active RF components entirely.
*Source:* 3GPP Rel-19 Ambient IoT article (3gpp.org/technologies/rel19-aiot)

## Q6 · Release availability · expert

As of Release 19, which capability was studied but NOT established as a normative AI/ML air-interface feature?

- **A)** Two-sided AI/ML CSI compression (UE encoder + network decoder) ✅
- **B)** AI/ML beam management with lifecycle management
- **C)** AI/ML-assisted positioning
- **D)** One-sided CSI prediction

*Why:* The Rel-19 two-sided CSI compression STUDY exists; the normative feature does not. Deployment-planning relevance: what can actually ship.
*Source:* 3GPP RAN Rel-19 status article (3gpp.org/technologies/ran-rel-19)

## Q7 · Release availability · advanced

eRedCap was introduced in which release, with which Rel-19 addition?

- **A)** Rel-18 introduction; Rel-19 adds NR-NTN support for (e)RedCap in FR1 bands ✅
- **B)** Rel-19 introduction; Rel-20 adds NTN support
- **C)** Rel-17 introduction; Rel-18 adds NTN support
- **D)** Rel-18 introduction; Rel-19 adds FR2 operation

*Why:* Release ladder + the satellite-IoT solution path that opens in Rel-19.
*Source:* 3GPP RedCap articles (3gpp.org/technologies/nr-redcap-glimpse; redcap-gsa-article01)

## Q8 · Release availability · advanced

L1/L2-triggered mobility (LTM) first appeared in Rel-18. Rel-19 Mobility Phase 4 extends it primarily by:

- **A)** Inter-CU operation with enhanced measurements and RRM requirements ✅
- **B)** Introducing LTM for the first time
- **C)** Removing candidate-cell pre-configuration
- **D)** Extending LTM to 2G/3G

*Why:* Whether LTM works across CU boundaries determines where it helps a real RAN topology.
*Source:* 3GPP Rel-19 summary, TSGs#112 June 2026 (3gpp.org official)

## Q9 · Release availability · expert

As of August 2026, the accurate statement of ISAC standardization status is:

- **A)** SA1 normative service requirements exist (TS 22.137); the RAN channel model is merged into TR 38.901 Rel-19; Rel-20 hosts the RAN ISAC study (TR 38.765); no normative RAN sensing feature is complete ✅
- **B)** Rel-19 froze normative NR sensing PHY specs
- **C)** ISAC was abandoned pending 6G
- **D)** Only vendor-proprietary sensing exists; 3GPP has no ISAC documents

*Why:* [Q48+Q20 merged per SME - TR 38.765 cite added] The full status chain matters for anyone planning sensing-based services.
*Source:* ISAC verification 2026-08 (3GPP portal + RP-234069; TR 38.765 Rel-20 study)

## Q10 · Release availability · advanced

The first structured 6G study items (requirements, architecture, security, radio evolution) are hosted in:

- **A)** Release 20, alongside continued 5G-Advanced commercial features ✅
- **B)** Release 19
- **C)** Release 21
- **D)** A separate 3GPP2 track

*Why:* Roadmap literacy: Rel-20 dual role.
*Source:* 3GPP Release 20 page (3gpp.org/specifications-technologies/releases/release-20)

## Q11 · Spec mapping · foundation

Which 3GPP technical report contains the Rel-18 study on AI/ML for the NR air interface that Rel-19 normative work builds on?

- **A)** TR 38.843 ✅
- **B)** TR 38.901
- **C)** TR 38.848
- **D)** TR 22.837

*Why:* [KEPT - caught qwen; re-sourced to official 3GPP AI/ML article]
*Source:* 3GPP AI/ML overview (3gpp.org/news-events/3gpp-news/ai-ml-2025; TR 38.843)

## Q12 · Spec mapping · advanced

The Rel-19 service requirements and architecture for Ambient IoT are found in:

- **A)** TS 22.369 and TS 23.369 ✅
- **B)** TS 22.261 and TS 23.501
- **C)** TS 38.843 and TS 38.300
- **D)** TR 22.837 and TS 23.288

*Why:* [KEPT - caught qwen] Where to look when designing an AmbIoT service.
*Source:* 3GPP Rel-19 Ambient IoT article (3gpp.org/technologies/rel19-aiot)

## Q13 · Spec mapping · expert

Where were the Rel-19 ISAC channel-model study results captured?

- **A)** Merged into TR 38.901 itself (Rel-19 version) ✅
- **B)** A new standalone TR 38.9xx sensing report
- **C)** TR 22.837 annex
- **D)** TS 38.300 stage-2 text

*Why:* Anyone evaluating sensing propagation needs to know the model lives in 38.901 Rel-19, not a separate TR.
*Source:* ISAC verification 2026-08 (3GPP portal + RP-234069; TR 38.765 Rel-20 study)

## Q14 · Spec mapping · expert

Which SA4 specification mapping for XR/AR media is correct?

- **A)** TS 26.119 = Media Capabilities for Augmented Reality; TS 26.565 = Split Rendering; TS 26.264 = IMS-based AR RTC ✅
- **B)** TS 26.119 = Split Rendering; TS 26.565 = IMS-based AR RTC; TS 26.264 = Media Capabilities for Augmented Reality
- **C)** TS 26.119 = IMS-based AR RTC; TS 26.565 = Media Capabilities for Augmented Reality; TS 26.264 = Split Rendering
- **D)** TS 26.119 = XR codecs; TS 26.565 = haptics; TS 26.264 = avatar formats

*Why:* IMS/VAS solution work: which spec to open for which piece. Permuted distractors need all three known.
*Source:* 3GPP article: Device media capabilities for AR services (3gpp.org/technologies/ar-capable); TS 26.119/26.264/26.565

## Q15 · Spec mapping · expert

AIML_MT_Ph2 introduced its Rel-19 Stage-1 functional requirements and KPIs primarily through CRs to which specification?

- **A)** TS 22.261 ✅
- **B)** TS 22.278
- **C)** TS 22.101
- **D)** TS 22.011

*Why:* Near-identical 22-series distractors; the CR trail to TS 22.261 is portal-verifiable.
*Source:* 3GPP portal CR list, WI 1000030 AIML_MT_Ph2 -> TS 22.261 (portal.3gpp.org)

## Q16 · Spec mapping · expert

The Rel-20 6G use-cases and service-requirements study, approved by SA, is documented in:

- **A)** TR 22.870 ✅
- **B)** TR 22.837
- **C)** TR 21.900
- **D)** TS 22.261

*Why:* Official spec page: Study on 6G Use Cases and Service Requirements.
*Source:* 3GPP spec page TR 22.870 (3gpp.org/dynareport/22870.htm)

## Q17 · Spec mapping · expert

In TS 26.565, the metric poseToRenderToPhoton is calculated as:

- **A)** actualDisplayTime - estimatedAtTime ✅
- **B)** receptionTime - serverTransmitTime
- **C)** startToRenderAtTime - sceneUpdateTime
- **D)** actualDisplayTime - lastChangeTime

*Why:* [SME-authored replacement for the unsupported 10-50ms question] All four are plausible latency expressions from the same spec's tables; the true formula is the XR QoE metric an operator would actually monitor.
*Source:* ETSI TS 126 565 V19.0.0 (Rel-19 Split Rendering Media Service Enabler)

## Q18 · Mechanism · expert

In Rel-19 AI/ML lifecycle management for UE-sided models, which function set keeps a deployed model trustworthy in the field?

- **A)** Performance monitoring with activation/deactivation/fallback and model selection/switching ✅
- **B)** Mandatory federated retraining across UEs of the same vendor
- **C)** gNB weight updates over SIB
- **D)** Continuous on-device gradient descent

*Why:* [KEPT - caught muse] LCM is the AIOps-for-RAN control loop of the standardized AI features.
*Source:* 3GPP AI/ML overview (3gpp.org/news-events/3gpp-news/ai-ml-2025; TR 38.843)

## Q19 · Mechanism · expert

A UE supports LP-WUS. Which receiver-architecture and waveform statement is fully correct?

- **A)** Separate low-power receiver; wake-up signal generated with DFT-s-OFDM, detected non-coherently (OOK envelope or OFDM sequence correlation) ✅
- **B)** Separate low-power receiver; Zadoff-Chu preamble detected coherently
- **C)** Main receiver duty-cycled; DFT-s-OFDM detected coherently
- **D)** Separate receiver; LoRa chirp waveform

*Why:* Superposed OOK/OFDM-sequence design enables two receiver classes - each distractor corrupts one element.
*Source:* 3GPP Rel-19 LP-WUS article (3gpp.org/technologies/rel19-lpwus)

## Q20 · Mechanism · expert

Rel-19 LP-WUS supports UE battery savings in which RRC states, via what?

- **A)** Idle/inactive (main radio in ultra-deep/deep sleep before paging) AND connected (LP-WUS-triggered PDCCH monitoring) ✅
- **B)** Idle only - paging wake-up
- **C)** Idle and inactive only
- **D)** Connected only - DRX replacement

*Why:* [Fixed per SME - state coverage instead of unanchored 70-90% claim] Both state families are supported with distinct mechanisms.
*Source:* 3GPP Rel-19 LP-WUS article (3gpp.org/technologies/rel19-lpwus)

## Q21 · Mechanism · expert

In LP-WUS connected-mode operation, the option that monitors wake-up occasions OUTSIDE Active Time enables:

- **A)** The gNB to wake and schedule the UE almost at any time, with LP-WUS cycles as short as 10-20 ms ✅
- **B)** The UE to skip all RRM measurements permanently
- **C)** Paging-free operation in idle mode
- **D)** Elimination of HARQ feedback

*Why:* Option-2 monitoring is the low-latency scheduling hook - relevant to XR/IM service design.
*Source:* 3GPP Rel-19 LP-WUS article (3gpp.org/technologies/rel19-lpwus)

## Q22 · Mechanism · expert

The evaluated LP-WUS idle/inactive power saving of up to ~90% versus legacy I-DRX holds under which condition?

- **A)** Sufficient RRM measurement relaxation (relaxation factor >= 8) ✅
- **B)** Only when paging load is zero
- **C)** Only with OFDM-sequence receivers
- **D)** Unconditionally in all deployments

*Why:* [Fixes SME Q27 objection: the % is now anchored to its evaluation condition] The conditional is the engineering truth - savings die without RRM relaxation.
*Source:* 3GPP Rel-19 LP-WUS article (3gpp.org/technologies/rel19-lpwus)

## Q23 · Mechanism · expert

A counterintuitive LP-WUS connected-mode evaluation result for small-packet services (e.g., instant messaging) is:

- **A)** Up to 180% user-plane-throughput improvement alongside 60%+ power savings - waking precisely when data arrives beats long DRX cycles on both axes ✅
- **B)** Throughput always degrades as the price of power savings
- **C)** Power savings only materialize above 100 Mbps
- **D)** UPT gains require disabling DRX entirely

*Why:* The win-win breaks the intuitive latency-vs-battery trade-off assumption - a real service-design insight.
*Source:* 3GPP Rel-19 LP-WUS article (3gpp.org/technologies/rel19-lpwus)

## Q24 · Mechanism · advanced

Rel-19 sub-band full duplex (SBFD) specifies:

- **A)** Simultaneous DL and UL on non-overlapping sub-bands within a TDD carrier ✅
- **B)** Same-frequency full duplex with self-interference cancellation
- **C)** FDD in TDD bands via carrier aggregation
- **D)** UL-only carriers

*Why:* The non-overlapping qualifier is what makes it deployable now.
*Source:* 3GPP Rel-19 summary, TSGs#112 June 2026 (3gpp.org official)

## Q25 · Mechanism · expert

SBFD deployment next to a legacy synchronized-TDD operator introduces which interference pair not present under synchronized legacy TDD operation?

- **A)** gNB-to-gNB cross-link interference: the SBFD cell receives UL in its sub-band while the neighbor transmits DL ✅
- **B)** UE-to-satellite leakage
- **C)** PRACH collision storms
- **D)** SSB beam collisions

*Why:* Rel-19 adds gNB-gNB CLI measurement/mitigation. The deployment-blocking consideration for SBFD rollouts.
*Source:* 3GPP RAN Rel-19 status article (3gpp.org/technologies/ran-rel-19)

## Q26 · Mechanism · expert

At LTM cell-switch execution, what sits on the critical path?

- **A)** An L1/L2 cell-switch command (LTM Cell Switch Command MAC CE) - RRC configuration was front-loaded at candidate preparation ✅
- **B)** Full RRC reconfiguration with key change
- **C)** NAS registration update
- **D)** SIB1 re-acquisition

*Why:* LTM Cell Switch Command MAC CE per RAN2 material. The mechanism that produces the latency win.
*Source:* 3GPP RAN Rel-19 status article (3gpp.org/technologies/ran-rel-19)

## Q27 · Mechanism · expert

On-demand SIB1 in Rel-19 energy saving: which UE population is it aimed at, and what triggers it?

- **A)** Idle/inactive UEs; an uplink wake-up signal (UL-WUS) requests SIB1 transmission ✅
- **B)** Connected UEs; RRC request
- **C)** Idle UEs; GPS timing
- **D)** All UEs; 5 ms periodic broadcast

*Why:* [UL-WUS term per SME] The gNB can stay quiet until a UE actually asks.
*Source:* 3GPP Rel-19 LP-WUS article (3gpp.org/technologies/rel19-lpwus)

## Q28 · Mechanism · advanced

Rel-19 NTN Phase 3: which capability pairing is correct?

- **A)** Store-and-forward for discontinuous feeder links AND regenerative payload operation ✅
- **B)** Store-and-forward AND transparent-payload-only
- **C)** Regenerative payloads AND no timing advance
- **D)** Multicast AND FR2-only

*Why:* S&F rides on regenerative payloads - both halves must be known together.
*Source:* 3GPP Rel-19 summary, TSGs#112 June 2026 (3gpp.org official)

## Q29 · Mechanism · expert

Rel-19 slice replacement (TEI19_SliceSel): who initiates and who governs?

- **A)** An authorized application (AF-requested) initiates; the operator governs via authorization ✅
- **B)** The UE initiates autonomously
- **C)** The operator initiates; the application consents
- **D)** NWDAF initiates from analytics

*Why:* AF-requested, operator-governed. The trust boundary matters for exposing this to enterprises (VAS/BSS).
*Source:* 3GPP Rel-19 TEI19_SliceSel CRs (AF-requested slice replacement) (3gpp.org/technologies/ran-rel-19)

## Q30 · Mechanism · advanced

Rel-19 MASSS extends multi-access traffic steering beyond Rel-18 by adding:

- **A)** Steering of IP and Ethernet traffic (MPQUIC-IP/Ethernet) - Rel-18 already had MPQUIC-UDP ✅
- **B)** Bluetooth as a 3GPP access
- **C)** Removal of N3IWF
- **D)** Wi-Fi as mandatory default

*Why:* MPQUIC-UDP was Rel-18 per CR record. Determines which enterprise traffic types ATSSS can carry - transport/packet planning.
*Source:* 3GPP CR record: MPQUIC-UDP in Rel-18; MASSS adds IP/Ethernet (portal.3gpp.org)

## Q31 · Mechanism · expert

Rel-19 AI/ML positioning is scoped as:

- **A)** ML-assisted location derivation with LCM signaling, complementing - not replacing - legacy positioning methods ✅
- **B)** Full replacement of legacy positioning
- **C)** GNSS-free E911 mandate
- **D)** Network-side models only

*Why:* Scope literacy: it is an enhancement layer, which matters when composing a positioning solution.
*Source:* 3GPP AI/ML overview (3gpp.org/news-events/3gpp-news/ai-ml-2025; TR 38.843)

## Q32 · Ambient IoT design · expert

Rel-19 Ambient IoT topology and spectrum (D1T1): which statement is correct?

- **A)** Indoor device talks directly and bidirectionally to a BS reader; FR1 licensed FDD - R2D on DL spectrum, D2R and the external carrier wave on UL spectrum ✅
- **B)** Intermediate UEs relay to base stations (Topology 2)
- **C)** Unlicensed 2.4 GHz operation
- **D)** R2D on UL spectrum, D2R on DL spectrum

*Why:* Topology 2 (UE readers) is Rel-20, not Rel-19; the spectrum split is the deployable configuration.
*Source:* 3GPP Rel-19 Ambient IoT article (3gpp.org/technologies/rel19-aiot)

## Q33 · Ambient IoT design · expert

The Rel-19 Ambient IoT protocol stack removes which function set relative to NR?

- **A)** RRC, PDCP, SDAP, ARQ, L1 HARQ, mobility, and AS security - along with scrambling, interleaving, and MIMO ✅
- **B)** Only HARQ; RRC is retained for configuration
- **C)** Only mobility; security is retained
- **D)** Nothing - the full NR stack runs in simplified form

*Why:* No-RRC/no-AS-security has direct integration and security-architecture consequences (regulatory/security review flavor).
*Source:* 3GPP Rel-19 Ambient IoT article (3gpp.org/technologies/rel19-aiot)

## Q34 · Ambient IoT design · expert

Ambient IoT D2R contention access uses:

- **A)** Slotted-ALOHA with simple randomization/back-off, plus contention-free targeting of specific devices ✅
- **B)** Standard NR 4-step RACH
- **C)** CSMA/CA listen-before-talk
- **D)** Polling only, no contention

*Why:* Inventory-scan capacity planning (OSS flavor) depends on the ALOHA access model.
*Source:* 3GPP Rel-19 Ambient IoT article (3gpp.org/technologies/rel19-aiot)

## Q35 · Ambient IoT design · expert

Why is R2D multiplexing restricted to TDMA only in Rel-19 Ambient IoT?

- **A)** The wideband envelope-detector receiver cannot separate frequency channels, so devices cannot be frequency-multiplexed on the downlink ✅
- **B)** Regulators prohibit FDMA below 1 GHz
- **C)** TDMA is more energy-efficient at the reader
- **D)** To reuse the LTE frame structure

*Why:* Mechanism-reason join: the receiver architecture forces the multiplexing choice.
*Source:* 3GPP Rel-19 Ambient IoT article (3gpp.org/technologies/rel19-aiot)

## Q36 · Ambient IoT design · expert

The R2D vs D2R link asymmetry in Rel-19 Ambient IoT is:

- **A)** R2D: OOK + Manchester, no channel coding, TDMA. D2R: OOK or BPSK + Manchester with m-sequence preambles, LTE convolutional coding, FDMA via repetition-rate separation ✅
- **B)** Both links: OFDM with polar coding
- **C)** R2D coded, D2R uncoded
- **D)** Both links identical OOK, both TDMA

*Why:* The asymmetry (coding only where the READER decodes) reflects where processing power lives - a design insight, not trivia.
*Source:* 3GPP Rel-19 Ambient IoT article (3gpp.org/technologies/rel19-aiot)

## Q37 · Ambient IoT design · expert

In the Rel-19 Ambient IoT network architecture, the AIOTF:

- **A)** Terminates the NAS protocol with the device and manages service triggering, interfacing with RAN directly or via AMF ✅
- **B)** Replaces the AMF entirely
- **C)** Is a RAN-internal scheduler
- **D)** Handles only billing records

*Why:* Packet-core integration point - where AmbIoT lands in the 5GC (OSS/BSS integration flavor).
*Source:* 3GPP Rel-19 Ambient IoT article (3gpp.org/technologies/rel19-aiot)

## Q38 · Ambient IoT design · expert

Ambient IoT device addressing at scale uses:

- **A)** A globally unique structured permanent identifier (PLMN ID, information type, EPC, ...) with core-network masks addressing device subsets ✅
- **B)** Randomly assigned session IDs per inventory round
- **C)** IMSI reuse from spare ranges
- **D)** MAC addresses from an IEEE block

*Why:* Mask-based subset addressing is how million-tag inventories become manageable - OSS/BSS-relevant.
*Source:* 3GPP Rel-19 Ambient IoT article (3gpp.org/technologies/rel19-aiot)

## Q39 · NOT-form · expert

Which is NOT a Rel-19 network energy saving mechanism?

- **A)** Mandatory nightly cell shutdown windows negotiated via RRC ✅
- **B)** On-demand SSB for SCells
- **C)** On-demand SIB1 for idle/inactive UEs
- **D)** Low-power wake-up signal

*Why:* [KEPT] The fake option sounds operational but is not a 3GPP mechanism.
*Source:* 3GPP Rel-19 LP-WUS article (3gpp.org/technologies/rel19-lpwus); Netw_Energy_NR_enh (Rel-19 NES)

## Q40 · NOT-form · expert

Which sensing mode is NOT among the six defined in the Rel-19 ISAC channel model?

- **A)** Satellite-TRP bistatic ✅
- **B)** TRP monostatic
- **C)** UE-UE bistatic
- **D)** TRP-UE bistatic

*Why:* [KEPT] The taxonomy is TRP/UE mono/bistatic combinations (modes 1-6); satellite is not an endpoint.
*Source:* 3GPP sensing-mode enumeration (modes 1-6), current 3GPP material

## Q41 · NOT-form · advanced

Which is NOT part of Rel-19 XR Phase 3?

- **A)** Guaranteed 8K per-eye encoding mandates ✅
- **B)** Cancellable measurement gaps
- **C)** Non-integer traffic periodicity handling
- **D)** Power-saving refinements for periodic XR flows

*Why:* [KEPT] Codec mandates are not RAN scope.
*Source:* 3GPP Rel-19 summary, TSGs#112 June 2026 (3gpp.org official)

## Q42 · NOT-form · advanced

Which is NOT a Rel-19 security enhancement?

- **A)** Mandatory post-quantum lattice key exchange on the air interface ✅
- **B)** 256-bit algorithms (SNOW 5G, AES-256, ZUC-256)
- **C)** ACME-based automated certificate management for SBA
- **D)** Security support for mobility over non-3GPP access that avoids full primary authentication

*Why:* [FIXED per SME: base ACM_SBA is Rel-18 - distractor now names the specifically-Rel-19 ACME-based work; D sharpened to the official building block.]
*Source:* 3GPP portal CR lists: TS 33.310 ACME-based ACM (Rel-19); CT1 WI list (non-3GPP access mobility security)

## Q43 · NOT-form · expert

Which capability is NOT specified for Ambient IoT Device 1?

- **A)** Coherent OFDM downlink demodulation ✅
- **B)** RF envelope-detector reception
- **C)** Passive backscatter D2R transmission
- **D)** Battery-less operation from harvested energy

*Why:* [KEPT] Coherent demod contradicts the ~1uW envelope-detector design.
*Source:* 3GPP Rel-19 Ambient IoT article (3gpp.org/technologies/rel19-aiot)

## Q44 · NOT-form · advanced

Which traffic type was ALREADY steerable by ATSSS before Rel-19 MASSS?

- **A)** UDP-based traffic (MPQUIC-UDP) ✅
- **B)** Native Ethernet frames
- **C)** Arbitrary IP traffic
- **D)** SCTP signaling

*Why:* [KEPT] Inverted form: the Rel-18 baseline vs the Rel-19 additions.
*Source:* 3GPP CR record: MPQUIC-UDP in Rel-18; MASSS adds IP/Ethernet (portal.3gpp.org)

## Q45 · Operational scenario · expert

An operator plans dense-urban 5G-Advanced with: (1) AI-CSI prediction, (2) LP-WUS wearables, (3) SBFD. Which item carries the largest INTER-SITE interference risk requiring coordinated deployment?

- **A)** SBFD - it changes the interference topology (gNB-gNB and UE-UE CLI); the other two are per-link features ✅
- **B)** LP-WUS - wake-up signals jam neighbor paging
- **C)** AI-CSI - prediction errors raise Tx power
- **D)** All three equally

*Why:* [KEPT] Deployment-risk triage across features.
*Source:* 3GPP Rel-19 summary, TSGs#112 June 2026 (3gpp.org official)

## Q46 · Operational scenario · expert

A utility wants battery-free asset tags in a fenced indoor substation, a few bytes read per day, no maintenance for 10 years, and alarms pushed instantly from the tag when a fault occurs. Which requirement is NOT satisfiable with Rel-19 Ambient IoT?

- **A)** Instant tag-initiated alarms - DO-A traffic is unsupported; Rel-19 tags only respond when triggered by the reader ✅
- **B)** Battery-free operation
- **C)** Indoor BS-reader deployment
- **D)** Small daily payloads

*Why:* Solution-fit analysis: three requirements fit D1T1; the autonomous-alarm one silently fails. Exactly the analysis an SA does before proposing.
*Source:* 3GPP Rel-19 Ambient IoT article (3gpp.org/technologies/rel19-aiot)

## Q47 · Operational scenario · expert

A gaming service needs 90 fps cloud-rendered XR with a strict motion-to-photon budget on mid-tier headsets. Which Rel-19 combination addresses (a) radio latency jitter, (b) device thermals, (c) late pose correction?

- **A)** (a) XR-aware scheduling + cancellable gaps + LTM, (b) split rendering offload per TS 26.565, (c) on-device Asynchronous Time Warping ✅
- **B)** (a) SBFD, (b) Ambient IoT, (c) 128-port CSI
- **C)** (a) LP-WUS, (b) eRedCap, (c) MASSS
- **D)** (a) on-demand SIB1, (b) SNOW 5G, (c) slice replacement

*Why:* [KEPT] Cross-domain composition: RAN XR treatment (NR_XR_Ph3), split rendering (TS 26.565), ATW (XR study material) - each component separately sourced per SME.
*Source:* NR_XR_Ph3 WI; ETSI TS 126 565 V19.0.0; 3GPP XR-over-5G study material (ATW)

## Q48 · Operational scenario · expert

An AIOps platform wants closed-loop actions driven by exposed UPF events, QoS-monitoring results, and user-plane metadata. Which Rel-19 enhancement provides the enabling exposure hook?

- **A)** UPEAS Phase 2 - UPF event notifications, QoS-monitoring reporting, and payload-header functionality exposed through SBA patterns ✅
- **B)** TEI19_SliceSel
- **C)** NR_duplex_evo
- **D)** LP-WUS

*Why:* [FIXED per SME: per-flow-anomaly wording removed - abnormal-traffic-pattern events are Rel-20 AIML_CN_Ph2] User-plane observability/event exposure is the Rel-19 hook for closed-loop ops.
*Source:* 3GPP portal CR list, TS 29.564 UPEAS Ph2 (portal.3gpp.org)

## Q49 · Operational scenario · expert

A nationwide IoT tender requires mobility, network slicing, and data bursts up to 10 Mbps. Which Rel-18/19 technology fits, and what is the architectural trade-off vs NB-IoT?

- **A)** eRedCap - native 5GS integration and mobility with a 10 Mbps ceiling; vs NB-IoT it trades higher device/radio capability for substantially more throughput and broader 5G service integration ✅
- **B)** NB-IoT - it now supports slicing
- **C)** Ambient IoT - if tags are battery-less
- **D)** LTE Cat-1bis - identical capabilities

*Why:* [FIXED per SME: market claims (module cost, battery, sub-100ms) removed - comparison is now architectural.]
*Source:* 3GPP RedCap articles (3gpp.org/technologies/nr-redcap-glimpse; redcap-gsa-article01)

## Q50 · Operational scenario · expert

In Rel-19 UPEAS Phase 2, the exposed UPF capability set includes:

- **A)** Event notifications, QoS-monitoring reporting, payload-header functionality, and defined behavior across UPF relocation and session release ✅
- **B)** In-UPF model training for traffic prediction
- **C)** Direct RAN scheduler control from the UPF
- **D)** Subscriber billing mediation

*Why:* [NEW - 5GC/AIOps slot per SME] The concrete capability list from the TS 29.564 CR trail - what an integration architect can actually consume.
*Source:* 3GPP portal CR list, TS 29.564 UPEAS Ph2 (portal.3gpp.org)

## Q51 · Operational scenario · expert

An operator's management system must plan capacity for and monitor RedCap devices as a distinct population. What does Rel-19 provide for this (NR_RedCap_OAM)?

- **A)** Network resource model extensions and RedCap-specific performance measurements for the management plane ✅
- **B)** A separate RedCap core network
- **C)** Nothing - RedCap devices are indistinguishable in OAM
- **D)** Per-device GPU telemetry

*Why:* [NEW - OSS/management slot per SME] The OAM gap operators hit in early RedCap rollouts, closed in Rel-19.
*Source:* 3GPP Rel-19 summary, TSGs#112 June 2026 (3gpp.org official)

## Q52 · Operational scenario · expert

Rel-19 IMS-based AR conversational services deliver 2D/3D avatar media to the far end via:

- **A)** IMS data channels within the call session (TS 26.264) ✅
- **B)** A parallel OTT WebRTC session outside IMS
- **C)** MMS attachments
- **D)** SIP MESSAGE bodies

*Why:* [NEW - IMS/VAS slot per SME] Avatar transport inside the IMS session is what makes it an operator service rather than an OTT bolt-on - VAS/monetization relevance.
*Source:* 3GPP article: Device media capabilities for AR services (3gpp.org/technologies/ar-capable); TS 26.119/26.264/26.565
