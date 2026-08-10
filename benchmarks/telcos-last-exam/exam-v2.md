# Telco's Last Exam v2

Approved 2026-08-10. This file is the source of truth for the 20 v2 questions.

This draft grows the exam from 10 to 30 questions. The original 10 are kept
verbatim (listed at the end with new metadata only). The 20 new questions
below each carry: domain, difficulty tier, points, a reference answer, and
grading notes for the judge. Every numerical result was computed and
verified programmatically before being written here; the calculation steps
are shown so you can re-derive each number.

Difficulty tiers: **foundation** (solid engineer), **advanced** (senior
engineer / architect), **expert** (specialist depth).

Domains: RF/RAN, Core & Protocols, Transport & Fronthaul, Timing & Sync,
Security, OAM & Performance, Cloud-Native, Economics.

Review guidance: challenge every number, every spec reference, and every
"must mention" grading item. Anything you edit becomes the truth the judge
grades against.

---

## RF / RAN Engineering

### RF1 - Uplink link budget and cell range at 3.5 GHz (advanced, 10 pts)

**Question.** A 5G NR TDD cell at 3.5 GHz (n78) uses a 64T64R AAS on a
25 m rooftop. For the *uplink* (the limiting link), assume: UE Tx power
23 dBm, UE antenna gain 0 dBi, gNB effective beamforming gain 25 dBi,
gNB noise figure 3.5 dB, PUSCH allocation 5 MHz, cell-edge target SINR
-3 dB, log-normal shadowing margin 7 dB, deep-indoor penetration loss
20 dB, interference margin 3 dB. Using the 3GPP TR 38.901 UMa NLOS path
loss model at hUT = 1.5 m, compute (a) the receiver sensitivity, (b) the
maximum allowed path loss (MAPL), and (c) the resulting 3D cell range.
Show all steps.

**Reference answer.**
(a) Thermal noise in 5 MHz: -174 + 10log10(5x10^6) = -107.0 dBm.
Noise floor = -107.0 + NF 3.5 = -103.5 dBm.
Sensitivity = noise floor + target SINR = -103.5 + (-3) = **-106.5 dBm**.
(b) MAPL = UE Tx 23 + UE gain 0 + gNB gain 25 - sensitivity (-106.5)
- shadowing 7 - penetration 20 - interference 3 = **124.5 dB**.
(c) TR 38.901 UMa NLOS (hUT = 1.5 m, so the height correction term is
zero): PL = 13.54 + 39.08 log10(d3D) + 20 log10(fc[GHz]).
20 log10(3.5) = 10.88 dB. Solving 124.5 = 13.54 + 39.08 log10(d3D) +
10.88 gives log10(d3D) = 100.08/39.08 = 2.561, so d3D ~ **364 m**
(d2D ~ 363 m after removing the 23.5 m height delta - negligible).
The cell is uplink-limited to roughly 350-400 m for deep-indoor users;
outdoor users (drop the 20 dB penetration) reach ~1.2 km.

**Grading notes.** Must have: correct thermal noise for 5 MHz (-107),
sensitivity -106.5 dBm, MAPL 124.5 dB (+-0.5), use of the UMa NLOS
formula with the 20log10(fc) term, final range 340-390 m. Award partial
credit for correct method with arithmetic slips <= 1 dB. Penalize: using
full 100 MHz noise bandwidth for a 5 MHz PUSCH allocation (a common
error - inflates noise by 13 dB), applying downlink EIRP, or quoting a
range without a path-loss model.

### RF2 - Peak DL throughput per TS 38.306 (expert, 10 pts)

**Question.** Compute the approximate peak downlink data rate of a
single-carrier NR FR1 configuration per the TS 38.306 formula: 100 MHz
bandwidth, mu = 1 (30 kHz SCS), 4 MIMO layers, 256QAM, scaling factor
f = 1, R_max = 948/1024, FR1 downlink overhead OH = 0.14. State the
formula, each parameter's value (including N_PRB for 100 MHz at 30 kHz),
and the result.

**Reference answer.** TS 38.306 5.1a: data rate =
v * Qm * f * R_max * (N_PRB * 12 / T_s) * (1 - OH), where
v = 4 layers, Qm = 8 (256QAM), f = 1, R_max = 948/1024 = 0.9258,
N_PRB = 273 (100 MHz at mu = 1), and T_s = 10^-3 / (14 * 2^mu) =
35.71 us (average OFDM symbol duration).
N_PRB * 12 / T_s = 273 * 12 / 35.71e-6 = 91.73e6 REs/s.
Rate = 4 * 8 * 1 * 0.9258 * 91.73e6 * 0.86 = **~2.34 Gbps**
(2.337 Gbps).

**Grading notes.** Must have: the 38.306 formula shape, N_PRB = 273,
Qm = 8, T_s = 1 ms/(14*2^mu), OH = 0.14, result 2.30-2.37 Gbps.
Penalize: N_PRB = 275 or 270 (wrong table), forgetting (1-OH), or
quoting marketing "~2.5 Gbps" without derivation.

### RF3 - Random-access timing advance limit (foundation, 6 pts)

**Question.** In NR, the RAR's Timing Advance Command is a 12-bit
field with index values 0-3846. With T_c =
1/(480000 * 4096) s, the TA granularity is 16 * 64 * T_c / 2^mu.
For mu = 0 and mu = 1, compute the TA step, the maximum timing advance,
and the maximum cell radius it implies. What practically limits NR cell
range beyond this?

**Reference answer.** TA step = 16*64*T_c/2^mu: for mu = 0 this is
520.83 ns, for mu = 1 260.42 ns. Max TA = 3846 * step: mu = 0 ->
2003.1 us; mu = 1 -> 1001.6 us. Radius = c * TA_max / 2 (round trip):
mu = 0 -> **~300 km** (300.3 km); mu = 1 -> **~150 km** (150.1 km).
Beyond the TA field, range is practically limited by: PRACH format
(cyclic shift/guard time - the preamble must land in the detection
window), UL link budget (23 dBm UE), and for TDD the guard period
between DL and UL.

**Grading notes.** Must have: both step values (521/260 ns), radius
~300 km / ~150 km, the divide-by-2 for round trip, and at least two of
the three practical limiters (PRACH format, link budget, TDD GP).
Accept 3846 or "about 2 ms" phrasing. Penalize: using 4095 (gives
319/160 km - wrong field range), forgetting round-trip halving.

### RF4 - PRACH cyclic-shift planning (expert, 10 pts)

**Question.** A rural TDD n78 site must serve a 15 km cell using PRACH
format 0 (long sequence, L_RA = 839, sequence duration 800 us,
unrestricted set). Assume 5.2 us delay-spread guard. (a) Derive the
minimum N_CS. (b) From the standard unrestricted N_CS set
{..., 93, 119, 167, ...}, which value do you pick? (c) How many
preambles does one root sequence then yield, and how many root
sequences are needed for 64 preambles?

**Reference answer.** (a) One cyclic-shift sample spans 800/839 =
0.9535 us. Round-trip delay for 15 km = 2 * 15 * 3.336 us/km =
100.1 us. Required shift span = (100.1 + 5.2)/0.9535 = 110.4 ->
**N_CS >= 111**. (b) The smallest standard value >= 111 is
**N_CS = 119** (supports ~16 km). (c) Preambles per root =
floor(839/119) = **7**; roots needed = ceil(64/7) = **10 root
sequences**. (N_CS = 93 would cap the cell at ~12.5 km - too small;
167 wastes roots.)

**Grading notes.** Must have: RTD ~100 us for 15 km, the 0.95 us/sample
conversion, N_CS >= ~110, selection of 119 from the standard set,
7 preambles/root, 10 roots. Accept c = 300 m/us (gives 100.0 us) or
299.79. Penalize: one-way instead of round-trip delay (halves N_CS -
classic error), or ignoring the delay-spread guard.

---

## Core Network & Protocols

### CP1 - 5G SA registration call flow (foundation, 8 pts)

**Question.** Walk through the 5G SA initial registration of a UE with
a USIM, from RRC Setup to Registration Accept. Name each NAS/NGAP
message, which function handles it (gNB, AMF, AUSF, UDM), where SUCI
is used, where NAS security starts, and where the 5G-GUTI is assigned.

**Reference answer.** (1) RRC: Msg1 preamble / Msg2 RAR / Msg3
RRCSetupRequest / Msg4 RRCSetup; UE sends RRCSetupComplete carrying the
NAS **Registration Request** with **SUCI** (the encrypted SUPI - used
here because the UE has no valid 5G-GUTI). (2) gNB forwards it in NGAP
**Initial UE Message** to the AMF. (3) AMF invokes AUSF
(Nausf_UEAuthentication_Authenticate); AUSF gets the authentication
vector from UDM (Nudm_UEAuthentication_Get) - UDM/SIDF de-conceals
SUCI -> SUPI. (4) **Authentication Request/Response** (5G-AKA) over
NAS; on success K_AUSF -> K_SEAF -> K_AMF. (5) NAS **Security Mode
Command/Complete** activates NAS ciphering + integrity (this is where
NAS security starts). (6) AMF registers with UDM
(Nudm_UECM_Registration), retrieves subscription
(Nudm_SDM_Get). (7) NGAP **Initial Context Setup Request** installs
the UE context and K_gNB in the gNB (AS Security Mode Command follows
on RRC). (8) NAS **Registration Accept** carries the newly assigned
**5G-GUTI** (assigned by the AMF); UE answers Registration Complete.

**Grading notes.** Must have: SUCI in the initial Registration Request,
AUSF/UDM roles (vector from UDM, SIDF de-concealment), NAS SMC as the
start of NAS security, Initial Context Setup for AS keys, 5G-GUTI in
Registration Accept from AMF. Order must be authentication -> NAS SMC ->
context setup -> Accept. Penalize: putting SUPI on the air interface,
skipping SMC, or assigning GUTI from UDM.

### CP2 - PDU session, QoS flows and DRB mapping (advanced, 10 pts)

**Question.** An SA UE establishes a PDU session for enhanced mobile
broadband plus a voice service. Explain: (a) the SMF/UPF interactions
(which interface/protocol, which rules are installed), (b) how QoS
flows are created for default traffic (5QI 9) and voice (5QI 1 GBR +
5QI 5 for IMS signalling), (c) who maps QoS flows to DRBs and where
that mapping can differ per cell, and (d) which identifiers tie it all
together (QFI, TEID, DRB-ID).

**Reference answer.** (a) SMF selects a UPF and installs packet
handling over **N4 (PFCP)**: PDR (packet detection), FAR (forwarding),
QER (QoS enforcement - MBR/GBR, gating), URR (usage reporting). GTP-U
tunnels on N3 are identified by **TEID**s exchanged in the PFCP session
and signalled to the gNB over N2. (b) The default QoS flow (non-GBR,
**5QI 9**) is created at session establishment; IMS signalling gets a
**5QI 5** non-GBR flow; when the voice call is set up, PCF pushes a
PCC rule and SMF creates a **GBR flow with 5QI 1** (voice media) with
GFBR/MFBR values - each flow tagged by its **QFI** carried in the
GTP-U extension header on N3. (c) The **gNB (SDAP layer)** maps QoS
flows to DRBs; the mapping is a RAN decision and can differ between
cells/vendors - e.g. one cell maps 5QI 5 with the default flow on one
DRB, another gives it a dedicated DRB. (d) End to end: QFI (per-flow,
N3/air), N3 TEIDs (per session tunnel), DRB-ID (per radio bearer);
SDAP header carries QFI on the air interface when reflective QoS or
multi-flow DRBs are used.

**Grading notes.** Must have: PFCP with at least PDR/FAR/QER, 5QI 1
GBR vs 5QI 5/9 non-GBR distinction, PCF-driven dedicated flow for
voice, SDAP/gNB owning flow->DRB mapping, QFI vs TEID vs DRB-ID roles.
Penalize: claiming SMF or AMF maps flows to DRBs, GTP on N4, or voice
media on 5QI 5.

### CP3 - SUCI concealment internals (expert, 8 pts)

**Question.** Detail how SUCI conceals the SUPI: the ECIES scheme
profiles A and B (curves, symmetric and MAC algorithms, ephemeral key
sizes), what parts of the SUPI are and are not concealed, where the
home-network public key lives, and which function de-conceals. Why
does routing still work if the MSIN is encrypted?

**Reference answer.** SUCI = ECIES encryption of the **MSIN only**.
**Profile A**: Curve25519 (X25519 key agreement), AES-128-CTR
encryption, HMAC-SHA-256 with an 8-byte MAC tag, 32-byte ephemeral
public key. **Profile B**: secp256r1, AES-128-CTR, HMAC-SHA-256
(8-byte tag), 33-byte compressed ephemeral public key. The UE holds
the **home network public key** provisioned in the USIM; each
attachment generates a fresh ephemeral key pair, so SUCIs are
unlinkable. **Not concealed**: MCC/MNC (home network identity),
routing indicator, protection scheme id, home key id - these route the
request to the right UDM group. De-concealment is done by the
**SIDF**, a function of the UDM, using the home network private key.
Routing works because the cleartext MCC/MNC + routing indicator are
sufficient to reach the subscriber's UDM; only the subscriber-unique
MSIN is hidden from eavesdroppers and fake base stations.

**Grading notes.** Must have: MSIN-only concealment, both profiles with
correct curve names, SIDF/UDM as de-concealer, home-network public key
on USIM, cleartext routing fields rationale, fresh ephemeral key per
SUCI. Penalize: claiming the whole SUPI or IMSI is encrypted, wrong
curves, de-concealment at AUSF or AMF.

### CP4 - EPS fallback for voice (advanced, 8 pts)

**Question.** An SA network without VoNR-grade coverage uses EPS
fallback. Describe the end-to-end flow from the MO call attempt on NR:
which node decides the fallback, the two RAN mechanisms it may use,
what happens to the IMS signalling and to the 5QI-1 flow, the role of
N26, and the typical call-setup delay penalty. When would you instead
deploy RAT fallback to ng-eNB?

**Reference answer.** The UE registers on NR with IMS voice; on an MO/MT
call, IMS invites proceed and PCF/SMF request a **5QI-1 GBR flow**.
The **gNB** (knowing VoNR is not enabled/qualified) rejects the QoS
flow setup with an EPS-fallback indication and triggers either
(a) **handover to LTE** (if N26 exists - context transferred, IP
preserved via 5GC->EPC interworking with combined SMF+PGW-C) or
(b) **RRC release with redirect** to LTE (slower, UE re-attaches via
TAU with the mapped EPS context). IMS signalling (5QI 5 / QCI 5)
survives the transition; the voice bearer is then established on LTE
as **QCI 1** and the call completes as VoLTE. **N26** enables seamless
context transfer and IP-address preservation; without it, redirection
plus TAU adds delay. Setup penalty: typically **~1-2 s extra**
(HO-based at the low end, redirect-based higher). **RAT fallback**
(to ng-eNB still connected to 5GC) is chosen when the operator wants
to stay on 5GC (slicing, policy continuity) but lacks NR voice
quality - the session stays on the 5GC, only the RAT changes.

**Grading notes.** Must have: gNB as the decision point (reject of
5QI-1 with fallback indication), both HO and redirect variants, N26
role, QCI-1 completion on VoLTE, order-of-1-2 s penalty, RAT vs EPS
fallback distinction (5GC kept vs EPC). Penalize: IMS re-registration
claimed as mandatory, AMF deciding fallback, or dropping the IMS
signalling flow.

---

## Transport & Fronthaul

### TX1 - O-RAN 7-2x fronthaul dimensioning (expert, 10 pts)

**Question.** Dimension the U-plane fronthaul bitrate for one O-RAN
split 7-2x cell: 100 MHz at mu = 1 (273 PRBs), 4 spatial layers/
streams, frequency-domain IQ with 9-bit block-floating-point mantissas
(I and Q) plus one 8-bit exponent per PRB, all 14 symbols of every
slot carrying data. Compute per-layer and total bitrate, then name
what the calculation deliberately ignores and the transport you would
provision.

**Reference answer.** Symbols/s at mu = 1: 14 symbols * 2000 slots/s
= 28,000 sym/s. IQ bits per symbol per layer: 273 PRB * 12 subcarriers
* 2 (I+Q) * 9 bit = 58,968 bits; exponent overhead: 273 * 8 = 2,184
bits; total 61,152 bits/symbol. Per-layer rate = 61,152 * 28,000 =
**1.71 Gbps**. Four layers: **~6.85 Gbps**. Deliberately ignored:
eCPRI/Ethernet/VLAN headers (~1-2%), C-plane and S-plane messages
(small), M-plane, and PRACH/SRS occasions - together < 10%. With
headroom you provision a **10 GbE** (or 25 GbE for growth/2-cell
aggregation) fronthaul link; latency budget ~100 us one-way and
G.8275.1 timing must ride the same network.

**Grading notes.** Must have: 28,000 sym/s, ~61 kbit/symbol/layer
(+-5%), 1.6-1.8 Gbps per layer, 6.5-7.2 Gbps total, at least two
ignored overheads, 10/25 GbE conclusion. Penalize: using time-domain
IQ (that is split 8 - gives ~4x higher), forgetting I+Q doubling, or
per-antenna (64) instead of per-layer/stream (4) scaling for 7-2x.

### TX2 - MTU budget on N3 and the DC fabric (foundation, 6 pts)

**Question.** A UPF in a data center receives N3 GTP-U traffic that
transits a VXLAN underlay. User IP packets are up to 1500 B. Compute
the minimum transport MTU (a) on the N3 path (plain IP transport) and
(b) on the VXLAN fabric (include inner Ethernet), assuming IPv4
outer headers, GTP-U with the 4-byte PDU Session Container extension.
What MTU do you actually configure and why?

**Reference answer.** (a) N3: 1500 (user) + 20 (outer IPv4) + 8 (UDP)
+ 8 (GTP-U) + 4 (ext header) = **1540 B minimum**. (b) VXLAN adds
14 (inner Ethernet) + 8 (VXLAN) + 8 (outer UDP) + 20 (outer IPv4) =
50 B on top of the 1540-byte frame payload -> **1590 B minimum**.
In practice you configure **jumbo MTU 9000 (or >= 1600 "baby
jumbo")** on all transport and fabric links: it absorbs IPv6 outers
(+20), optional GTP-U sequence numbers, double encapsulation cases,
and avoids fragmentation - GTP-U fragmentation on N3 is a
well-known throughput killer, and DF-marked user packets would
otherwise force ICMP-based PMTUD that mobile stacks handle poorly.

**Grading notes.** Must have: 1540 and 1590 with visible arithmetic,
jumbo/>=1600 recommendation, fragmentation-avoidance rationale.
Accept IPv6 variants if stated (+20 on each outer: 1560/1630).
Penalize: forgetting the GTP extension header, or inner-Ethernet
omission on VXLAN.

### TX3 - Segment routing for RAN backhaul (advanced, 8 pts)

**Question.** You are designing xHaul transport for 400 gNBs using
segment routing. Compare SR-MPLS and SRv6 for this use: label/SID
encoding and header overhead, hardware maturity, TI-LFA protection,
network slicing hooks (Flex-Algo), and interworking with existing
MPLS. Give a concrete recommendation with justification.

**Reference answer.** **SR-MPLS** encodes the path as an MPLS label
stack (4 B per label); mature across merchant silicon, brownfield-
friendly (same forwarding plane as LDP/RSVP networks, seamless
interworking/migration via SR-LDP coexistence), TI-LFA gives < 50 ms
FRR with 100% coverage using post-convergence paths, Flex-Algo
(e.g. low-latency metric algo for URLLC slices, separate algo for
best-effort) provides slice-aware steering with zero extra state.
**SRv6** encodes SIDs as 128-bit IPv6 addresses in an SRH - richer
programmability (network programming, END.X/END.DT4 behaviors), no
MPLS at all, but per-SID overhead is 16 B (micro-SID/uSID compresses
this), requires IPv6 underlay everywhere and newer silicon; brownfield
MPLS interworking needs gateways. **Recommendation** for a typical
brownfield operator backhaul: **SR-MPLS with TI-LFA and Flex-Algo**
- full hardware maturity on installed routers, direct migration from
LDP, proven < 50 ms protection; adopt SRv6/uSID only greenfield or
where IPv6-native DC-to-RAN programmability is a hard requirement.

**Grading notes.** Must have: label stack vs SRH/128-bit SID contrast,
TI-LFA sub-50 ms with post-convergence property, Flex-Algo for
slicing, brownfield interworking argument, a definite recommendation
with at least two technical justifications. Accept a reasoned SRv6/
uSID recommendation for greenfield. Penalize: treating TI-LFA as
LFA (coverage claims), or SRv6 overhead ignored.

---

## Timing & Synchronization

### TS1 - G.8275.1 time-error budget (advanced, 8 pts)

**Question.** A TDD RAN requires +-1.5 us time alignment at the air
interface (cell-to-cell). Build a representative ITU-T G.8275.1 full
timing support budget from a PRTC/T-GM through 10 class-B T-BCs to
the gNB (T-TSC), allocating: PRTC+T-GM constant TE, per-hop cTE,
dynamic TE, link asymmetry allocation, and a holdover reserve. Show
the sum and the margin, and name the two failure modes the budget
protects against.

**Reference answer.** Representative allocation: PRTC+T-GM
**+-100 ns**; 10 class-B T-BC hops at **20 ns cTE** each = 200 ns;
dynamic TE (dTE, filtered noise across the chain) **200 ns**;
uncompensated link asymmetries (fiber pairs, dispersion,
patch-panel deltas) **380 ns**; holdover/rearrangement reserve
**400 ns**. Sum = 100 + 200 + 200 + 380 + 400 = **1280 ns**, leaving
**~220 ns margin** against the 1500 ns end budget (matches the
G.8271.1 network-limit style split where ~1100 ns is granted to the
network and 400 ns to failure events). It protects against
(1) **GNSS loss at the T-GM** - the holdover reserve covers the
drift until repair or until the backup grandmaster takes over - and
(2) **path rearrangement/asymmetry changes** after protection
switches, which introduce step changes in TE.

**Grading notes.** Must have: itemized budget summing <= 1.5 us with
class-B 20 ns per hop, explicit asymmetry line item, holdover
reserve, margin statement, both failure modes. Accept class-A
(50 ns) variants if the arithmetic still closes. Penalize: budgets
that ignore asymmetry (the dominant practical killer) or claim
SyncE alone meets phase requirements.

### TS2 - TDD guard period vs cell radius (advanced, 6 pts)

**Question.** In an NR TDD pattern at mu = 1, the guard period between
DL and UL is set in OFDM symbols. Compute the maximum cell radius
supported by guard periods of 1, 2 and 4 symbols (normal CP,
ignore UE switching time), explain the halving factor, and state what
happens to UEs beyond that radius.

**Reference answer.** Symbol duration at mu = 1 (incl. CP, averaged)
= 0.5 ms / 14 = **35.7 us**. The guard must absorb the *round trip*
(DL propagation out + UL propagation back), so radius = c * GP / 2:
1 symbol -> 3e8 * 35.7e-6 / 2 = **5.4 km**; 2 symbols -> **10.7 km**;
4 symbols -> **21.4 km**. (Subtracting a realistic ~10 us UE/gNB
switching time shrinks these by ~1.5 km.) UEs beyond the radius have
their UL (advanced by TA) arrive before the gNB finishes receiving
DL-to-UL switching - their UL transmissions collide with the last DL
symbols at the gNB, causing interference; in practice the network
caps TA / denies access or the cell is planned with a larger GP
(pattern with more flexible symbols).

**Grading notes.** Must have: 35.7 us symbol time, the round-trip
halving explained, 5.4/10.7/21.4 km (+-0.3), and the
interference/access consequence. Accept answers subtracting
switching time if stated. Penalize: forgetting the factor 2, or
using mu = 0 symbol duration.

---

## Security

### SE1 - 5G key hierarchy and handover key handling (advanced, 8 pts)

**Question.** Draw out (textually) the 5G key hierarchy from the
permanent key to the AS keys: name each key, where it is derived and
held. Then explain what happens to K_gNB at an Xn handover -
horizontal vs vertical key derivation, the role of NH/NCC, and why
this gives forward security.

**Reference answer.** **K** (permanent, USIM + UDM/ARPF) ->
**CK/IK** (5G-AKA at ARPF) -> **K_AUSF** (held AUSF) -> **K_SEAF**
(anchor, SEAF in the AMF) -> **K_AMF** (AMF; NAS context) -> NAS
keys **K_NASint / K_NASenc** (AMF+UE) and **K_gNB** (AMF -> gNB) ->
AS keys **K_RRCint / K_RRCenc / K_UPint / K_UPenc** (gNB+UE).
At **Xn handover**: the source gNB derives the target key from the
current K_gNB and target cell parameters (PCI, ARFCN-DL) -
**horizontal derivation** (KDF over the active key) - unless it
holds an unused **{NH, NCC}** pair previously provided by the AMF,
in which case it uses the fresh NH - **vertical derivation**. The
AMF computes NH from K_AMF and increments NCC; the UE, seeing the
NCC in the HO command, mirrors the derivation. Vertical derivation
gives **forward security**: a compromised source gNB cannot compute
future keys derived from a fresh NH it never saw (2-hop forward
security), whereas pure horizontal chains would let it predict all
successor keys.

**Grading notes.** Must have: complete chain K->K_AUSF->K_SEAF->
K_AMF->{NAS keys, K_gNB}->AS keys with correct holders, horizontal
vs vertical distinction, NH/NCC mechanics with AMF as NH source and
NCC signalled to UE, forward-security rationale. Penalize: K_SEAF
in AUSF, K_gNB derived by gNB from nothing, or NCC described as a
key.

### SE2 - Inter-PLMN security with SEPP (foundation, 6 pts)

**Question.** Two 5G operators interconnect for roaming over N32.
Explain the SEPP's role, the two N32 protection modes and when each
applies, what is protected end to end versus hop by hop, and why the
legacy roaming model (plain GTP/Diameter via IPX) motivated this
design.

**Reference answer.** The **SEPP** is the security edge proxy that
terminates all inter-PLMN control-plane (SBI/HTTP2) traffic on
**N32**. Two modes: **N32 with TLS** - mutual TLS directly between
the two SEPPs, used when there is a direct or fully trusted
interconnection (protects everything hop-to-hop between SEPPs); and
**PRINS** (PRotocol for N32 INterconnect Security) - application-
layer protection (JOSE: JWE encryption of sensitive IEs, JWS
integrity over the message) used when **IPX intermediaries** must
read/modify some fields for their services: PRINS lets IPX providers
see and patch only whitelisted IEs, with every modification signed
and attributable, while sensitive IEs (keys, SUPI, location) stay
end-to-end encrypted between SEPPs. Motivation: in 4G/SS7-era
roaming, IPX carriers saw *all* signalling in cleartext - the
source of well-documented interception and location-tracking
attacks; N32 makes the trust boundary explicit and cryptographic.

**Grading notes.** Must have: SEPP as SBI edge for roaming, TLS vs
PRINS with the IPX-modification rationale, JOSE-based selective
protection in PRINS, the legacy cleartext motivation. Penalize:
PRINS described as transport TLS, SEPP on the user plane, or
claiming IPX is eliminated.

---

## OAM & Performance

### OM1 - Composite accessibility KPI from counters (foundation, 6 pts)

**Question.** A monitoring stack exposes these busy-hour counters for
a cell: RRC setup attempts 41,200 / successes 40,994; NGAP initial
context setup attempts 40,990 / successes 40,949; DRB setup attempts
40,940 / successes 40,817. Define the composite accessibility KPI,
compute each stage and the composite (4 decimal places on stages,
2 on the composite %), and state which stage you would investigate
first and what typically causes it.

**Reference answer.** Accessibility = P(RRC) * P(NGAP ICS) * P(DRB).
P(RRC) = 40994/41200 = 0.9950; P(NGAP) = 40949/40990 = 0.9990;
P(DRB) = 40817/40940 = 0.9970. Composite = 0.9950 * 0.9990 * 0.9970
= 0.99103 -> **99.10%**. Investigate **RRC setup (99.50%)** first -
it is the weakest stage and the largest absolute failure count
(206). Typical causes: SRS/PRACH congestion or admission control
under load, UL interference on PUSCH/PUCCH msg3/msg5, parameter
issues (RACH power ramping, T300/T301), or a top-offender cell with
hardware/VSWR alarms. (NGAP failures point at core/transport; DRB
failures at admission/licensing or transport to the UPF.)

**Grading notes.** Must have: multiplicative composite definition,
three stage ratios correct to 4 dp, 99.10% composite, RRC stage
identified with at least two plausible causes. Penalize: averaging
instead of multiplying the stages, or ratios computed against the
wrong denominators.

### OM2 - Erlang-B dimensioning for a voice slice (advanced, 8 pts)

**Question.** A VoNR slice must serve 5,000 subscribers, 25 mErl
each in the busy hour, at <= 1% blocking. Using Erlang B, determine
the offered load and required number of simultaneous-call channels
(show the recursion or a bracketing argument, exact table lookup not
required), then convert to a GBR bandwidth pool assuming 50 kbps
per call including overheads. Why is Erlang B (rather than
Erlang C) the right model, and name one assumption that breaks at
small cell level?

**Reference answer.** Offered load A = 5000 * 0.025 = **125 Erlangs**.
Erlang B recursion B(0)=1, B(n) = A*B(n-1)/(n + A*B(n-1)); computing
until B <= 1% gives **N = 144 channels** (B(144) ~ 0.88%; 143 gives
~1.03%). GBR pool = 144 * 50 kbps = **7.2 Mbps**. Erlang B models
**blocked-calls-cleared** - a blocked VoNR call attempt is rejected
(and typically falls back/re-attempts as a new arrival), not queued;
Erlang C's infinite queue models deferrable work, not conversational
voice admission. Assumption that breaks at small cells: Poisson
arrivals from a *large* independent user population - a small cell
serves few users, so the finite-source (Engset) model applies and
Erlang B over-dimensions.

**Grading notes.** Must have: 125 E, N in 142-146 with <= 1%
justification, 7.1-7.3 Mbps, blocked-calls-cleared rationale,
finite-population/Engset caveat. Penalize: Erlang C usage,
N ~ A ("125 channels") without blocking math.

---

## Cloud-Native Infrastructure

### CN1 - UPF high availability on Kubernetes (advanced, 8 pts)

**Question.** You deploy a CNF UPF as multiple pods on a bare-metal
Kubernetes cluster (SR-IOV data plane). Describe a production HA
design: pod placement constraints, PodDisruptionBudget, what
N4/PFCP-level mechanism complements Kubernetes restarts, how
sessions survive a node loss, and the one thing Kubernetes
fundamentally cannot do for a stateful UPF fast path.

**Reference answer.** Placement: **pod anti-affinity** (required,
topologyKey = kubernetes.io/hostname and zone) spreads UPF replicas
across nodes/racks; nodes are labelled and tainted for the SR-IOV/
DPDK pool; CPU-manager static policy + hugepages pin the fast path.
A **PodDisruptionBudget** (e.g. minAvailable: N-1) blocks voluntary
drains from taking two replicas at once during upgrades. Kubernetes
restart/reschedule is **not** session HA: the complementing
mechanism is **PFCP-level resilience** - SMF association monitoring
via PFCP heartbeats, and either 1:1 UPF geo/local redundancy with
**session state replication** (checkpointing PDRs/FARs/URRs and
GTP-U sequence state to the standby) or stateless-UPF designs that
re-anchor sessions via SMF re-programming on the surviving replica.
On node loss, the standby takes over the N3/N9 addresses (VRRP/BGP
anycast or GARP) so gNBs keep the same tunnel endpoints, and the
SMF re-associates within the PFCP heartbeat timeout. What Kubernetes
cannot do: **preserve in-flight fast-path state** - a rescheduled
pod is a cold process; per-session forwarding state, NIC queues and
DPDK hugepage memory do not migrate, so session continuity must
come from the application-layer replication above, never from the
orchestrator.

**Grading notes.** Must have: required anti-affinity, PDB for
voluntary disruptions, PFCP heartbeat/association awareness,
state replication or SMF re-anchoring for sessions, IP takeover for
N3 continuity, the cold-restart limitation stated explicitly.
Penalize: claiming k8s liveness probes provide session HA, or
live-migration of DPDK pods.

### CN2 - UPF capacity dimensioning (advanced, 6 pts)

**Question.** Dimension the packet-processing cores of a UPF serving
200,000 PDU sessions with a busy-hour average of 100 kbps per
session (both directions combined), peak-to-mean ratio 1.5, average
packet size 600 B, a measured per-core capability of 1.5 Mpps for
the full GTP-U + QoS + usage-reporting pipeline, and a 30%
engineering headroom target. Show throughput, packet rate, and
cores; name two effects that would push the estimate up in
production.

**Reference answer.** Average aggregate = 200,000 * 100 kbps =
20 Gbps; engineered (peak) = 20 * 1.5 = **30 Gbps**. Packet rate =
30e9 / 8 / 600 = **6.25 Mpps**. Raw cores = 6.25/1.5 = 4.17; with
30% headroom (divide by 0.7) = 5.95 -> **6 fast-path cores** (plus
control/OS cores outside this budget). Real-world upward pressure:
(1) **small-packet skew** - voice/gaming/TCP-ACK traffic drags the
average packet size far below 600 B, and pps, not bps, is the
binding constraint; (2) **feature cost** - per-packet URR/charging
triggers, QoS policing on many GBR flows, deep buffer management,
or paging/idle-active churn all cut per-core Mpps; also
(3) traffic asymmetry concentrating load on DL queues.

**Grading notes.** Must have: 30 Gbps engineered, 6.25 Mpps, 6 cores
with the headroom step shown, two named production effects.
Accept ceil variations (7 cores) if the headroom is applied as
multiply-by-1.3 (5.42 -> 6) or argued. Penalize: dividing bps by
core-bps without a packet-size step, or ignoring peak-to-mean.

---

## Economics & Strategy

### EC1 - Private 5G vs Wi-Fi 6E for a factory (advanced, 8 pts)

**Question.** A 40,000 m2 factory needs wireless for 300 AGVs/robots
(handover-sensitive, uplink video) plus office IT. Inputs: private
5G - 8 indoor radios at $12k, core license $60k one-time,
integration $50k, spectrum $15k/yr, operations $30k/yr; Wi-Fi 6E -
24 APs at $1.2k, controller $15k, integration $20k, operations
$18k/yr, plus a 50% AP hardware refresh in year 3. Compute the
5-year TCO of each, then argue the decision beyond TCO: which three
technical factors dominate for AGVs, and what hybrid design do you
actually recommend?

**Reference answer.** 5G TCO(5y) = 8*12,000 + 60,000 + 50,000 +
5*(15,000+30,000) = 96,000 + 110,000 + 225,000 = **$431,000**.
Wi-Fi TCO(5y) = 24*1,200 + 15,000 + 20,000 + 5*18,000 + 14,400
(refresh) = **$168,200**. Wi-Fi is ~$263k cheaper - but for AGVs
three factors dominate over TCO: (1) **deterministic mobility** -
5G network-controlled handover sustains ~0 ms interruption at AGV
speed, while Wi-Fi client-driven roaming (even with 802.11k/v/r)
produces 50-500 ms outages that stall safety-rated AGVs;
(2) **uplink capacity under load** - scheduled SR/BSR-based NR
uplink with configured grants beats CSMA contention for many
simultaneous UL video streams; (3) **interference control** -
licensed/leased spectrum is exclusive, 6 GHz unlicensed must
coexist with neighbors and portable hotspots. Recommendation:
**hybrid** - private 5G (or NR-U/CBRS where applicable) dedicated
to AGVs/robotics and critical OT, Wi-Fi 6E for office IT and
non-critical devices; this caps the 5G footprint (cost) while
putting the deterministic radio where it pays for itself in
prevented line-stop minutes.

**Grading notes.** Must have: both TCO figures correct (+-$1k) with
visible arithmetic, all three technical factors (mobility, UL
scheduling vs contention, spectrum determinism), an explicit hybrid
recommendation tied to a business quantity (downtime/line-stop).
Penalize: TCO-only decisions either way, or claiming Wi-Fi 7 MLO
fully solves deterministic roaming.

---

## Existing questions 1-10 (kept verbatim - metadata assignment only)

The current 10 questions and reference answers in `exam.md` /
`answers.md` remain unchanged. Proposed metadata:

| # | Current topic | Domain | Difficulty | Points |
|---|---|---|---|---|
| 1 | RF link budget (mmWave) | RF/RAN | expert | 10 |
| 2 | Handover/mobility analysis | RF/RAN | advanced | 8 |
| 3 | Spectral efficiency / capacity | RF/RAN | advanced | 8 |
| 4 | Transport/latency budget | Transport | advanced | 8 |
| 5 | Core signalling storm | Core | expert | 10 |
| 6 | Slicing architecture | Core | advanced | 8 |
| 7 | Timing/sync failure | Timing | expert | 10 |
| 8 | Security incident | Security | advanced | 8 |
| 9 | Capacity/growth planning | OAM/Perf | advanced | 8 |
| 10 | Techno-economic tradeoff | Economics | expert | 10 |

(Exact titles to be aligned to the real exam.md numbering during
conversion - flag if you want any of the 10 retired or re-tiered.)

---

**Review checklist for you:** (1) challenge every number - each was
machine-verified but the *scenario parameters* are choices you may
want to tune; (2) confirm spec references (38.901, 38.306, G.8275.1,
33.501 profiles) match the versions you consider canonical; (3) mark
any question whose difficulty tier or points you disagree with;
(4) strike or edit any grading note you find too lenient/strict.
