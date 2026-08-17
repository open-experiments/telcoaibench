# Vendor GenAI Tests — 2026 Expansion (24 new matrix cells) — FROZEN 2026-08-18

Source of truth for the `vendor_genai_2026` judged task (dataset:
[`datasets/vendor_genai_2026.jsonl.gz`](datasets/vendor_genai_2026.jsonl.gz)).
SME-approved as drafted; anchors verified against official vendor sources and
trade press, Aug 2026.

**Design:** full 2026 matrix = legacy 24 (6 vendors x 4 domains, kept 1:1) + these 24 new cells: **Huawei x 6**, **ZTE x 6**, and the six legacy vendors x the two new domains (**Transport/IP**, **Security**). Same 5-part answer structure and judge rubric as legacy (technical_accuracy 0.40 / completeness 0.20 / depth 0.15 / honesty 0.25). **Five honesty traps** (M-E, S-E, R-E, S-F, R-F) reward models for stating a vendor does not play in a domain. Anchors verified via web research Aug 2026 (sources in research notes).

---

## H-A · Huawei · RAN

**Question:** Deep-dive Huawei's RAN portfolio for an operator (outside US/EU restriction zones) densifying mid-band 5G and preparing 5G-Advanced: radio/antenna families, baseband architecture, and Massive MIMO approach — including Huawei's posture on open fronthaul. Structure your answer in exactly five numbered parts: (1) Portfolio & architecture - name the actual product families/components and how they fit together; (2) Interfaces & standards posture - which open interfaces are supported and how deep; (3) Differentiation - what is technically distinctive versus peer vendors; (4) Quantitative reasoning - one dimensioning or performance consideration a buyer should model, with numbers and method; (5) Honesty check - what is NOT publicly known and must be obtained from the vendor directly. Do not invent product names, versions, interface names, or performance figures; state explicitly when something is not public knowledge.

**Judge anchors:** SingleRAN / SingleRAN Pro multi-RAT architecture; MetaAAU ELAA-based Massive MIMO family; 5G-A portfolio incl. Blade AAU X (all-sub-6GHz-band Massive MIMO single antenna) and U6GHz AAU (1500+ antenna elements, 256 TRX variant, 400 MHz BW); LampSite X indoor 5G-A with Passive IoT; GigaGreen energy-efficiency radio branding; purpose-built BBU (e.g. BBU5900) with in-house silicon; NOT an O-RAN Alliance member — publicly argues against open fronthaul, incl. opposing mandatory open RAN in 6G standardization; Dell'Oro #1 RAN vendor globally; effectively excluded from US (FCC Covered List) and being removed in UK/parts of EU.

**Fabrication bait:** claiming Huawei is an O-RAN Alliance member or ships O-RAN 7-2x compliant O-RU/O-DU; invented AAU model numbers with specific TRX/element counts beyond announced products; claiming a mainstream COTS x86 Cloud RAN product line; invented US/EU carrier wins.

---

## H-B · Huawei · Core

**Question:** Deep-dive Huawei's mobile core portfolio for an operator consolidating 2G-5G onto one core and adding 5G-Advanced B2B capabilities: converged network functions, user-plane strategy, and the intelligent-core positioning. Structure your answer in exactly five numbered parts: (1) Portfolio & architecture - name the actual product families/components and how they fit together; (2) Interfaces & standards posture - which open interfaces are supported and how deep; (3) Differentiation - what is technically distinctive versus peer vendors; (4) Quantitative reasoning - one dimensioning or performance consideration a buyer should model, with numbers and method; (5) Honesty check - what is NOT publicly known and must be obtained from the vendor directly. Do not invent product names, versions, interface names, or performance figures; state explicitly when something is not public knowledge.

**Judge anchors:** CloudCore portfolio; UNC = Unified Network Controller (converged AMF/SMF/NRF/NSSF + MME/SGW-C/PGW-C); UDG = Unified Distributed Gateway (converged UPF + SGW-U/PGW-U, edge-deployable); 5.5G Intelligent Core Network (MWC 2024) embedding the Telecom Foundation Model; fully convergent single-platform 2G/3G/4G/5G NSA/SA claim; UEN compact core for private/enterprise 5G; runs on Huawei's own telco cloud (Huawei Cloud Stack), not on Western hyperscalers; Dell'Oro-tracked mobile-core revenue leader; no US/Western-European tier-1 5G core wins.

**Fabrication bait:** wrong acronym expansions (UNC as 'Unified Network Core', UDG as 'Unified Data Gateway'); claiming commercial 5G core deployments on AWS/Azure; invented tier-1 Western core customers; invented convergence performance percentages.

---

## H-C · Huawei · OSS/AI

**Question:** Deep-dive Huawei's OSS/network-automation and telecom-AI portfolio for an operator targeting TM Forum Level-4 autonomy: management platforms per domain, the autonomy program, and the foundation-model strategy. Structure your answer in exactly five numbered parts: (1) Portfolio & architecture - name the actual product families/components and how they fit together; (2) Interfaces & standards posture - which open interfaces are supported and how deep; (3) Differentiation - what is technically distinctive versus peer vendors; (4) Quantitative reasoning - one dimensioning or performance consideration a buyer should model, with numbers and method; (5) Honesty check - what is NOT publicly known and must be obtained from the vendor directly. Do not invent product names, versions, interface names, or performance figures; state explicitly when something is not public knowledge.

**Judge anchors:** ADN (Autonomous Driving Network) strategy launched 2020 targeting TM Forum AN Level 4; iMaster MAE = wireless management-control-analysis platform (MAE-Access, MAE-CN variants); iMaster NCE = fixed/IP/optical/campus automation platform (NCE-FBB, NCE-Campus); Telecom Foundation Model (MWC 2024) with role-based copilots and scenario agents; Huawei Cloud Pangu Models 5.5 (2025) as the underlying LLM family; MTN South Africa + Huawei world-first TM Forum AN L4 certification for IP networks (2025); proprietary platforms (not ONAP-based); not sold to US operators, Pangu runs on Huawei Cloud (no US region).

**Fabrication bait:** claiming iMaster is ONAP-based or open-source; swapping MAE (wireless) and NCE (fixed/IP) domains; invented acronym expansions for MAE; invented L4 certifications beyond the publicly announced ones; claiming Pangu availability on US clouds.

---

## H-D · Huawei · Cloud-native

**Question:** Deep-dive Huawei's cloud-native and AI-infrastructure stack for a telco building sovereign telco cloud plus AI training capacity: container/cloud platforms, AI compute systems, and data-center fabric. Structure your answer in exactly five numbered parts: (1) Portfolio & architecture - name the actual product families/components and how they fit together; (2) Interfaces & standards posture - which open interfaces are supported and how deep; (3) Differentiation - what is technically distinctive versus peer vendors; (4) Quantitative reasoning - one dimensioning or performance consideration a buyer should model, with numbers and method; (5) Honesty check - what is NOT publicly known and must be obtained from the vendor directly. Do not invent product names, versions, interface names, or performance figures; state explicitly when something is not public knowledge.

**Judge anchors:** Huawei Cloud Stack on-prem carrier cloud (six scenario-specific carrier solutions, MWC 2025); Cloud Container Engine (CCE) — Leader in 2025 Gartner MQ for Container Management; originated CNCF projects KubeEdge, Volcano, Karmada; CloudMatrix 384 Ascend supernode (384x Ascend 910C NPUs, fully optical interconnect, positioned vs NVIDIA GB200 NVL72); CloudEngine DC switching (2025 Gartner MQ Leader) with Xinghe AI Fabric 2.0 lossless AI fabric; CloudCore NFs run cloud-native on Huawei's own stack; divested x86 server business (xFusion) in 2021; Huawei Cloud has no US regions.

**Fabrication bait:** claiming CloudMatrix uses NVIDIA GPUs; claiming Huawei Cloud is a global top-3 hyperscaler or has US regions; claiming current Huawei-branded x86 server line; invented Ascend performance figures vs NVIDIA beyond public positioning.

---

## H-E · Huawei · Transport/IP

**Question:** Deep-dive Huawei's transport and IP portfolio for a national operator refreshing backbone and metro for 400G+ and SRv6-based slicing: router families, optical transport lines, and fixed-access evolution. Structure your answer in exactly five numbered parts: (1) Portfolio & architecture - name the actual product families/components and how they fit together; (2) Interfaces & standards posture - which open interfaces are supported and how deep; (3) Differentiation - what is technically distinctive versus peer vendors; (4) Quantitative reasoning - one dimensioning or performance consideration a buyer should model, with numbers and method; (5) Honesty check - what is NOT publicly known and must be obtained from the vendor directly. Do not invent product names, versions, interface names, or performance figures; state explicitly when something is not public knowledge.

**Judge anchors:** NetEngine 8000 / 8000E router family — first end-to-end 400GE family with native SRv6 and FlexE slicing, under Net5.5G branding; in-house router NPUs (Solar series), no Broadcom dependence; leading SRv6 standards contributor; OptiXtrans optical brand — OSN 9800 WDM/OTN (GlobalData Leader, Core & Metro WDM), OptiXtrans E9600 metro/enterprise OTN, DC908 DCI; full-series 400G/800G WDM with Super C+L band; F5G-A: 50G PON and OXC-based all-optical products; OptiXaccess = OLT/access platforms, OptiXstar = ONT/FTTR premises; banned from new US authorizations (FCC Covered List); divested Huawei Marine (HMN Tech) 2019-20.

**Fabrication bait:** mixing OptiXtrans (WDM/OTN) with OptiXaccess (OLT) and OptiXstar (ONT/FTTR); claiming NetEngine uses Broadcom Jericho silicon; claiming current Huawei subsea-cable ownership; invented 800G deployment wins in Western markets.

---

## H-F · Huawei · Security

**Question:** Deep-dive Huawei's network-security portfolio for an enterprise/carrier buyer in a non-restricted market: firewall families, DDoS defense, analytics platform, and the AI-detection story. Structure your answer in exactly five numbered parts: (1) Portfolio & architecture - name the actual product families/components and how they fit together; (2) Interfaces & standards posture - which open interfaces are supported and how deep; (3) Differentiation - what is technically distinctive versus peer vendors; (4) Quantitative reasoning - one dimensioning or performance consideration a buyer should model, with numbers and method; (5) Honesty check - what is NOT publicly known and must be obtained from the vendor directly. Do not invent product names, versions, interface names, or performance figures; state explicitly when something is not public knowledge.

**Judge anchors:** HiSec Intelligent Security portfolio relaunched Sept 2023 incl. a SASE solution (currently marketed as Xinghe Intelligent SASE); HiSecEngine USG firewall series — USG6500F/6600F/6700F AI firewalls and flagship USG12000 marketed as industry's first terabit-level AI firewall (up to 18x100GE per LPU slot); AI Content-based Detection Engine (CDE) with claimed 95% unknown-threat detection via on-device inference; AntiDDoS8000 terabit-level defense with 2Tbps+ cloud scrubbing; HiSec Insight (formerly CIS) big-data security analytics/APT detection; Huawei-Symantec JV ended 2012; no US market presence (Covered List); footprint concentrated in China/MEA/LatAm/APAC.

**Fabrication bait:** claiming 'Qiankun' is Huawei's flagship global security SaaS (it is today the automotive/intelligent-driving brand); claiming the Huawei-Symantec JV still exists; invented Gartner Firewall MQ Leader placements in Western markets; invented detection-rate figures beyond the published CDE claim.

---

## Z-A · ZTE · RAN

**Question:** Deep-dive ZTE's RAN portfolio for an operator (Asia/MEA/LatAm) expanding multi-band 5G with AI-native ambitions: site/radio families, the AI-RAN approach, and silicon strategy. Structure your answer in exactly five numbered parts: (1) Portfolio & architecture - name the actual product families/components and how they fit together; (2) Interfaces & standards posture - which open interfaces are supported and how deep; (3) Differentiation - what is technically distinctive versus peer vendors; (4) Quantitative reasoning - one dimensioning or performance consideration a buyer should model, with numbers and method; (5) Honesty check - what is NOT publicly known and must be obtained from the vendor directly. Do not invent product names, versions, interface names, or performance figures; state explicitly when something is not public knowledge.

**Judge anchors:** UniSite simplified-site family; UBR (Ultra/Unified Broadband Radio) multi-band radios incl. tri-sector Omni-UBR and industry-first 6-band sub-3GHz UBR; AIR ('AI Radio') native-AI RAN powered by AIREngine in-network computing (launched 2024/2025); NodeEngine base-station-embedded edge computing; claimed industry-first FDD+TDD dual-band Massive MIMO AAU and tri-band FDD M-MIMO; MiCell mmWave indoor (>6 Gbps/cell) and qNCR network-controlled repeater; GigaMIMO 6G prototype (Feb 2026, 2048 elements, U6G band); self-designed silicon via fabless subsidiary Sanechips (TSMC-fabbed); Dell'Oro #4 RAN vendor globally; O-RAN Alliance member but commercially integrated RAN; on FCC covered list, no US footprint.

**Fabrication bait:** attributing Huawei branding to ZTE (SingleRAN, MetaAAU); claiming ZTE sells commercial O-RAN disaggregated RU/DU/CU to Western operators or that AIR is an O-RAN RIC; claiming Sanechips owns fabs; invented US/Western-European 5G RAN wins.

---

## Z-B · ZTE · Core

**Question:** Deep-dive ZTE's mobile core for an operator wanting one converged core across generations at very large scale: the core product, its architecture claims, and where it runs. Structure your answer in exactly five numbered parts: (1) Portfolio & architecture - name the actual product families/components and how they fit together; (2) Interfaces & standards posture - which open interfaces are supported and how deep; (3) Differentiation - what is technically distinctive versus peer vendors; (4) Quantitative reasoning - one dimensioning or performance consideration a buyer should model, with numbers and method; (5) Honesty check - what is NOT publicly known and must be obtained from the vendor directly. Do not invent product names, versions, interface names, or performance figures; state explicitly when something is not public knowledge.

**Judge anchors:** Common Core (launched 2018) — fully convergent 2G/3G/4G/5G/fixed core on 3GPP R15 SBA, SA+NSA, CUPS, stateless NFs, cloud-native microservices; claimed up to ~50% TCO saving vs separate cores; marketed as industry's first fully converged core; powers portions of world's largest 5G SA networks (China Mobile, China Telecom/Unicom shared network); listed in Omdia core-vendor landscape alongside Ericsson/Nokia/Huawei; runs on ZTE's own TECS cloud stack and servers; cloud-native UPF optimization work with Intel (Container Bare Metal Reference Architecture); no North-American footprint (FCC covered list).

**Fabrication bait:** calling ZTE's core 'CloudCore' or 'dual-mode 5G Core' (Huawei terms) or 'iCore'; invented Western tier-1 core customers; invented TCO percentages beyond the published claim; claiming Common Core runs commercially on Western hyperscalers.

---

## Z-C · ZTE · OSS/AI

**Question:** Deep-dive ZTE's autonomous-network and telecom-AI offerings for an operator targeting higher TM Forum autonomy levels: the AN solution suite, the telecom LLM, and the O&M services layer. Structure your answer in exactly five numbered parts: (1) Portfolio & architecture - name the actual product families/components and how they fit together; (2) Interfaces & standards posture - which open interfaces are supported and how deep; (3) Differentiation - what is technically distinctive versus peer vendors; (4) Quantitative reasoning - one dimensioning or performance consideration a buyer should model, with numbers and method; (5) Honesty check - what is NOT publicly known and must be obtained from the vendor directly. Do not invent product names, versions, interface names, or performance figures; state explicitly when something is not public knowledge.

**Judge anchors:** uSmartNet autonomous-network solution suite (uSmartNet 2.0 at MWC 2023) targeting TM Forum AN levels; Nebula Telecom Large Model launched July 1 2024 with Agent Factory and productized agents (Network Insight Expert, Monitoring Expert, iAssurance Expert) on the Digital Nebula architecture; iAssurance Expert claims cutting event assurance from six man-days to one; UniSeer intelligent O&M service solution (MWC Shanghai 2019; used with Ooredoo); AIS Thailand autonomous-network partnership on uSmartNet; ZSmart BSS exists but is a modest player concentrated in emerging markets.

**Fabrication bait:** confusing Nebula with Huawei Pangu or China Telecom TeleChat; calling UniSeer an SDN controller or RIC (it is O&M services); inventing a ZTE OSS suite named 'NetMaster'; claiming Amdocs/Huawei-class BSS market position for ZSmart.

---

## Z-D · ZTE · Cloud-native

**Question:** Deep-dive ZTE's telco-cloud and infrastructure stack for an operator standardizing NFV/CaaS with vertical-integration appetite: cloud platforms, database, servers, and AI systems. Structure your answer in exactly five numbered parts: (1) Portfolio & architecture - name the actual product families/components and how they fit together; (2) Interfaces & standards posture - which open interfaces are supported and how deep; (3) Differentiation - what is technically distinctive versus peer vendors; (4) Quantitative reasoning - one dimensioning or performance consideration a buyer should model, with numbers and method; (5) Honesty check - what is NOT publicly known and must be obtained from the vendor directly. Do not invent product names, versions, interface names, or performance figures; state explicitly when something is not public knowledge.

**Judge anchors:** TECS (Tulip Elastic Cloud System) family: TECS CloudFoundation = OpenStack-based NFVI/VIM; TECS OpenPalette = Kubernetes/container CaaS platform (99.999% reliability target); TCF (Telco Cloud Foundation) full-stack solution; GlobalData Leader rating for TECS three consecutive years; GoldenDB distributed transactional database certified by China's national fintech certification body, deployed in Chinese banking cores; own x86/ARM server lines (G5 2023, G6 at CloudFest 2025) and AiCube AI training/inference all-in-one for telcos; no public hyperscale cloud business (unlike Huawei Cloud); server business largely China-domestic.

**Fabrication bait:** claiming TECS is built on VMware or OpenShift; swapping OpenPalette (K8s CaaS) and CloudFoundation (OpenStack NFVI); inventing a 'ZTE Cloud' public hyperscaler; invented Western-market server share.

---

## Z-E · ZTE · Transport/IP

**Question:** Deep-dive ZTE's transport and IP portfolio for an operator building SRv6-based 5G transport with unified IP+optical control: router families, OTN/WDM platform, controller, and the 5G transport line. Structure your answer in exactly five numbered parts: (1) Portfolio & architecture - name the actual product families/components and how they fit together; (2) Interfaces & standards posture - which open interfaces are supported and how deep; (3) Differentiation - what is technically distinctive versus peer vendors; (4) Quantitative reasoning - one dimensioning or performance consideration a buyer should model, with numbers and method; (5) Honesty check - what is NOT publicly known and must be obtained from the vendor directly. Do not invent product names, versions, interface names, or performance figures; state explicitly when something is not public knowledge.

**Judge anchors:** ZXR10 M6000-S full-service edge/metro/backbone router family (nine variants M6000-3S..18S, up to 28.8T per-slot design, 800G/400G/100G density, SR/SRv6/EVPN, NETCONF/YANG/PCEP); ZXR10 T8000 flagship backbone core router; ZXONE 9700 packet-OTN/WDM platform; industry-first commercial trial of 400G OTN cluster with China Telecom (2020); ZENIC ONE unified management-and-control (SDN controller + NMS) for IP and optical (R22/R10; China Mobile cross-vendor single-layer controller tests); Flexhaul = 5G fronthaul/midhaul/backhaul transport family; SRv6-based 5G transport for XL Axiata Indonesia; router OS is ZXROS/ROSng (not Huawei's VRP); top-2 global PON/FTTH vendor; marginal in enterprise/DC switching and SD-WAN globally.

**Fabrication bait:** calling ZTE routers 'NetEngine' (Huawei) or claiming they run VRP; calling ZENIC ONE an AI-ops assistant or core product; inventing router models like 'ZXR10 M9000'; invented Western backbone wins.

---

## Z-F · ZTE · Security

**Question:** Deep-dive ZTE's security posture and offerings for a regulator-scrutinized operator evaluating vendor trust: certifications, assurance infrastructure, and what ZTE does NOT sell — with the geopolitical status stated accurately. Structure your answer in exactly five numbered parts: (1) Portfolio & architecture - name the actual product families/components and how they fit together; (2) Interfaces & standards posture - which open interfaces are supported and how deep; (3) Differentiation - what is technically distinctive versus peer vendors; (4) Quantitative reasoning - one dimensioning or performance consideration a buyer should model, with numbers and method; (5) Honesty check - what is NOT publicly known and must be obtained from the vendor directly. Do not invent product names, versions, interface names, or performance figures; state explicitly when something is not public knowledge.

**Judge anchors:** 5G NR passed GSMA/3GPP NESAS (SCAS-based) evaluations 2021; NESAS 2.1 process assessments covering 5G NR, 5GC, Flexhaul; Common Criteria EAL3+ for OTN and 5G RAN products; ISO 27001 (27 certificates group-wide), ISO 27701, ISO 28000, ISO 22301, IEC 62443; three cybersecurity labs — Nanjing, Rome, Brussels (Cybersecurity Lab Europe, opened 2019) offering source-code review; BSIMM11/12 assessments; NO meaningful global enterprise-security product line (no firewall/SOC/EDR business) — security story is equipment assurance, not products; 2018 US denial order lifted July 2018 after ~$1.4B settlement, but ZTE remains on the FCC covered list since 2022, excluded from US/Indian/several European 5G builds.

**Fabrication bait:** claiming ZTE sells a commercial firewall/SOC/EDR line internationally; claiming the 2018 US denial order is still in force, or that ZTE was removed from the FCC covered list; invented security-product revenue; honesty-trap: the correct answer must distinguish assurance certifications from a security-product portfolio ZTE does not have.

---

## E-E · Ericsson · Transport/IP

**Question:** Deep-dive Ericsson's transport portfolio for an operator building 5G xHaul under one RAN-integrated umbrella: what Ericsson actually sells in transport, where its portfolio boundaries are, and what comes from partners. Structure your answer in exactly five numbered parts: (1) Portfolio & architecture - name the actual product families/components and how they fit together; (2) Interfaces & standards posture - which open interfaces are supported and how deep; (3) Differentiation - what is technically distinctive versus peer vendors; (4) Quantitative reasoning - one dimensioning or performance consideration a buyer should model, with numbers and method; (5) Honesty check - what is NOT publicly known and must be obtained from the vendor directly. Do not invent product names, versions, interface names, or performance figures; state explicitly when something is not public knowledge.

**Judge anchors:** Router 6000 series for mobile transport/cell-site backhaul (Router 6671/6676/6678/6274; deployments incl. M1, UScellular); MINI-LINK microwave family — market-leading mobile-transport microwave (MINI-LINK 6000 current generation; Split Mount, All Outdoor, Long Haul variants); Fronthaul 6000 optical fronthaul family; Ericsson Transport Automation Controller (SDN/automation); transport is scoped to MOBILE transport, integrated with Ericsson Radio System — no in-house optical DWDM line and no internet-core routing (partners historically incl. Juniper for core routing); exited standalone optical transport years ago.

**Fabrication bait:** presenting a current Ericsson long-haul DWDM/optical portfolio (Marconi/SPO heritage) as active flagship; claiming in-house merchant-class routing silicon comparable to Nokia FP5/Cisco Silicon One; invented Router 6000 model numbers; claiming MINI-LINK was divested.

---

## N-E · Nokia · Transport/IP

**Question:** Deep-dive Nokia's transport and IP portfolio for an operator converging IP, optical and microwave under unified automation: router and silicon families, optical platforms incl. the recent acquisition, controller, and microwave. Structure your answer in exactly five numbered parts: (1) Portfolio & architecture - name the actual product families/components and how they fit together; (2) Interfaces & standards posture - which open interfaces are supported and how deep; (3) Differentiation - what is technically distinctive versus peer vendors; (4) Quantitative reasoning - one dimensioning or performance consideration a buyer should model, with numbers and method; (5) Honesty check - what is NOT publicly known and must be obtained from the vendor directly. Do not invent product names, versions, interface names, or performance figures; state explicitly when something is not public knowledge.

**Judge anchors:** 7750 Service Router (SR/SR-s) IP edge/core on FP5 in-house network-processor silicon; 7250 IXR Interconnect Routers for cell-site/aggregation under the 'Anyhaul' framing; 1830 PSS optical DWDM/OTN platform; Infinera acquisition COMPLETED Feb 28 2025 (adds ICE-X coherent pluggables, webscale/DC optical scale); Network Services Platform (NSP) unified IP/optical SDN controller; Deepfield IP analytics; Wavence microwave family; the only vendor of the six with full stack: own routing silicon + routers + optical + microwave + unified controller.

**Fabrication bait:** claiming the Infinera acquisition is still pending in 2026 (closed Feb 2025); claiming Nokia divested Wavence to Aviat (Aviat bought NEC's microwave, not Nokia's); invented FP5 throughput figures; confusing NSP with NetGuard (security).

---

## M-E · Mavenir · Transport/IP

**Question:** Deep-dive Mavenir's transport/IP portfolio for an operator asking a single-vendor question: what does Mavenir actually offer in transport — routers, optical, microwave, fronthaul gateways — and how should a buyer plan transport for a Mavenir-based network? Answer honestly. Structure your answer in exactly five numbered parts: (1) Portfolio & architecture - name the actual product families/components and how they fit together; (2) Interfaces & standards posture - which open interfaces are supported and how deep; (3) Differentiation - what is technically distinctive versus peer vendors; (4) Quantitative reasoning - one dimensioning or performance consideration a buyer should model, with numbers and method; (5) Honesty check - what is NOT publicly known and must be obtained from the vendor directly. Do not invent product names, versions, interface names, or performance figures; state explicitly when something is not public knowledge.

**Judge anchors:** HONESTY TRAP: Mavenir has NO transport/IP portfolio — it is a cloud-native software company (Open RAN software, converged packet core, IMS/voice, messaging, MAVscale/MAVedge platforms); June 2025 debt restructuring (~$1B+, lenders took control) included EXITING the OpenBeam radio-unit hardware business entirely — its only hardware line; transport in Mavenir deployments comes from third parties/operator-supplied IP infrastructure; the correct answer states this plainly and describes partner/operator-supplied transport planning.

**Fabrication bait:** inventing a 'MAVhaul' cell-site router line or Mavenir fronthaul-gateway products; claiming OpenBeam included transport products or is still active (discontinued 2025); any claimed Mavenir router/optical/microwave product is fabrication; reward: explicit statement that Mavenir does not play in transport.

---

## S-E · Samsung Networks · Transport/IP

**Question:** Deep-dive Samsung Networks' transport/IP story for an operator deploying Samsung vRAN: what Samsung itself provides in transport, what the vCSR actually is and whose software it runs, and what must come from partners. Answer honestly. Structure your answer in exactly five numbered parts: (1) Portfolio & architecture - name the actual product families/components and how they fit together; (2) Interfaces & standards posture - which open interfaces are supported and how deep; (3) Differentiation - what is technically distinctive versus peer vendors; (4) Quantitative reasoning - one dimensioning or performance consideration a buyer should model, with numbers and method; (5) Honesty check - what is NOT publicly known and must be obtained from the vendor directly. Do not invent product names, versions, interface names, or performance figures; state explicitly when something is not public knowledge.

**Judge anchors:** HONESTY TRAP (partner-dependent): Samsung has no meaningful in-house transport portfolio — no router hardware line, no optical transport, no microwave (never had a MINI-LINK/Wavence-class line); its transport page is an architecture overview without named in-house products; the one transport-adjacent offering is the virtual Cell Site Router (vCSR) — software on the vRAN COTS server, jointly developed with Juniper Networks (Juniper cRPD routing stack) and Wind River; backhaul in Samsung deployments comes from partners (Juniper, Cisco etc.); the correct answer credits the vCSR concept while stating the routing software is Juniper's and everything else is partner-supplied.

**Fabrication bait:** attributing NEC's iPasolink microwave to Samsung; claiming a Samsung-branded cell-site router hardware line; presenting vCSR as Samsung's own routing stack (it is Juniper cRPD); reward: explicit partner-dependency statement.

---

## R-E · Rakuten Symphony · Transport/IP

**Question:** Deep-dive Rakuten Symphony's transport/IP offering for an operator evaluating Symworld end-to-end: does Rakuten Symphony sell transport — and what are Symware and the 2025 Tejas partnership actually about? Answer honestly. Structure your answer in exactly five numbered parts: (1) Portfolio & architecture - name the actual product families/components and how they fit together; (2) Interfaces & standards posture - which open interfaces are supported and how deep; (3) Differentiation - what is technically distinctive versus peer vendors; (4) Quantitative reasoning - one dimensioning or performance consideration a buyer should model, with numbers and method; (5) Honesty check - what is NOT publicly known and must be obtained from the vendor directly. Do not invent product names, versions, interface names, or performance figures; state explicitly when something is not public knowledge.

**Judge anchors:** HONESTY TRAP: Rakuten Symphony has NO transport/IP portfolio — Symworld is Open RAN software, OSS (Symops), orchestration and cloud (Symcloud, from Robin.io); Symware is a cell-site EDGE-COMPUTE appliance hosting Open RAN DU functions (~30,000 units in Japan), NOT a transport router; June 2025 partnership with Tejas Networks explicitly brings Tejas optical transmission/broadband access/transport to pair with Rakuten's software — confirming transport comes from partners; 2025 pivot to 'Real Open RAN Licensing Program' (first partners Cisco, Airspan, Tech Mahindra) licenses software/IP rather than selling network hardware; correct answer states the gap plainly.

**Fabrication bait:** inventing a 'Symworld Transport Controller' managing Rakuten routers; calling Symware a cell-site router or transport product; claiming Rakuten Symphony sells optical/IP hardware; reward: explicit statement that transport is partner-supplied (Tejas et al.).

---

## C-E · Cisco · Transport/IP

**Question:** Deep-dive Cisco's service-provider transport and IP portfolio for an operator converging routing and optical for the AI-traffic era: router families and silicon, xHaul/access platforms, optical line systems, the routed-optical architecture, and automation. Structure your answer in exactly five numbered parts: (1) Portfolio & architecture - name the actual product families/components and how they fit together; (2) Interfaces & standards posture - which open interfaces are supported and how deep; (3) Differentiation - what is technically distinctive versus peer vendors; (4) Quantitative reasoning - one dimensioning or performance consideration a buyer should model, with numbers and method; (5) Honesty check - what is NOT publicly known and must be obtained from the vendor directly. Do not invent product names, versions, interface names, or performance figures; state explicitly when something is not public knowledge.

**Judge anchors:** Cisco 8000 Series on in-house Silicon One (Oct 2025: Cisco 8223 with Silicon One P200, 51.2 Tbps, 'scale-across' for distributed AI); NCS portfolio for access/aggregation and 5G xHaul (NCS 540 cell-site class, NCS 5500/5700); NCS 1000 optical line systems (NCS 1010/1014); Routed Optical Networking (RON) — coherent ZR/ZR+ DWDM pluggables (Acacia acquisition) directly in routers, collapsing the transponder layer; Crosswork Network Controller/automation suite for transport SDN and path computation; Silicon One also sold merchant; NO microwave radio line.

**Fabrication bait:** inventing a Cisco microwave backhaul product; claiming Cisco 8000 runs Broadcom Jericho (it is Silicon One); invented P200 successor chips or throughput figures; confusing NCS 1000 (optical) with NCS 540/5500 (routing).

---

## E-F · Ericsson · Security

**Question:** Deep-dive Ericsson's telecom-security portfolio for an operator hardening signalling, roaming and network operations: named security products, the signalling-security functions and where they live, the acquired enterprise-security arm, and portfolio boundaries. Structure your answer in exactly five numbered parts: (1) Portfolio & architecture - name the actual product families/components and how they fit together; (2) Interfaces & standards posture - which open interfaces are supported and how deep; (3) Differentiation - what is technically distinctive versus peer vendors; (4) Quantitative reasoning - one dimensioning or performance consideration a buyer should model, with numbers and method; (5) Honesty check - what is NOT publicly known and must be obtained from the vendor directly. Do not invent product names, versions, interface names, or performance figures; state explicitly when something is not public knowledge.

**Judge anchors:** Security & Risk Management products: Ericsson Security Manager (ESM — telco security posture/compliance automation), Ericsson Telecom Intrusion Detection System (TIDS — signalling intrusion detection for SS7/Diameter/GTP-C/SMS/5G; integrates POST Luxembourg's TIDS technology, announced July 2024), Device Security Enabler; signalling security functions inside the cloud-native Ericsson Signaling Controller: Diameter Edge Agent (DEA), SEPP, Unified Signaling Firewall (USFW); enterprise zero-trust via Cradlepoint: Ericsson NetCloud SASE (April 2024) with NetCloud Zero Trust for cellular/hybrid WAN; Ericsson Federal markets 5G security for US government.

**Fabrication bait:** calling the portfolio 'Ericsson NetGuard' (Nokia's brand); claiming Ericsson owns AdaptiveMobile (Enea acquired it); claiming TIDS is purely in-house (based on POST Luxembourg technology); invented SOC/XDR platform claims.

---

## N-F · Nokia · Security

**Question:** Deep-dive Nokia's telecom-security portfolio for an operator standing up a telco SOC: the XDR platform and its cloud/AI underpinnings, the wider NetGuard family, DDoS/visibility assets, and services. Structure your answer in exactly five numbered parts: (1) Portfolio & architecture - name the actual product families/components and how they fit together; (2) Interfaces & standards posture - which open interfaces are supported and how deep; (3) Differentiation - what is technically distinctive versus peer vendors; (4) Quantitative reasoning - one dimensioning or performance consideration a buyer should model, with numbers and method; (5) Honesty check - what is NOT publicly known and must be obtained from the vendor directly. Do not invent product names, versions, interface names, or performance figures; state explicitly when something is not public knowledge.

**Judge anchors:** NetGuard Cybersecurity Dome — telco XDR/security-orchestration SaaS on Microsoft Azure with pre-built 5G use cases (RAN/transport/core) and a telco-trained GenAI assistant using Azure OpenAI Service; Frost & Sullivan XDR Radar top innovation leader; NetGuard family: Endpoint Detection and Response, Identity Access Manager (telco PAM), Certificate Lifecycle Manager / Certificate Manager (PKI); Deepfield Network Intelligence/Analytics + Deepfield Defender and the 7750 Defender Mitigation System for DDoS; IPsec Security Gateway; Cybersecurity Consulting + Managed Security Services incl. telco MDR; Deepfield acquired 2016 (not from Alcatel-Lucent merger); broadest standalone telco-security portfolio of the six.

**Fabrication bait:** claiming Dome was built by acquiring a SIEM vendor (Nokia-built on Azure); claiming Deepfield came via Alcatel-Lucent; citing 'NetGuard Signaling Firewall' as current flagship (legacy-era name, not in the current portfolio); invented detection metrics.

---

## M-F · Mavenir · Security

**Question:** Deep-dive Mavenir's security portfolio for an operator focused on signalling security and fraud: the actual product suite, standards compliance, the 5G roaming function, and what Mavenir does NOT offer in security. Structure your answer in exactly five numbered parts: (1) Portfolio & architecture - name the actual product families/components and how they fit together; (2) Interfaces & standards posture - which open interfaces are supported and how deep; (3) Differentiation - what is technically distinctive versus peer vendors; (4) Quantitative reasoning - one dimensioning or performance consideration a buyer should model, with numbers and method; (5) Honesty check - what is NOT publicly known and must be obtained from the vendor directly. Do not invent product names, versions, interface names, or performance figures; state explicitly when something is not public knowledge.

**Judge anchors:** MAVapps Fraud and Security Suite (announced June 2018): Mavenir Signaling Firewall — GSMA FS.11/FS.19-compliant covering SS7, Diameter, SIP, GTP; SpamShield (SMS/messaging fraud, A2P bypass); CallShield (voice fraud, CLI spoofing); ML-based Fraud Management System; Equipment Identity Register (EIR); SEPP for 5G roaming security in its packet-core/signalling portfolio; portfolio is fraud-and-revenue-protection centric — NO telco XDR/SOC platform, no managed-security arm comparable to Nokia NetGuard.

**Fabrication bait:** inventing brands like 'MavSecure' or 'Mavenir NetShield'; claiming a Mavenir XDR/SOC or MDR service; invented fraud-detection percentages; reward: correctly bounding the portfolio to signalling/fraud.

---

## S-F · Samsung Networks · Security

**Question:** Deep-dive Samsung Networks' security story for an operator's vendor-risk assessment: how Samsung secures its network products, the certifications it holds, what Knox is and is not, and whether Samsung sells operator security products. Answer honestly. Structure your answer in exactly five numbered parts: (1) Portfolio & architecture - name the actual product families/components and how they fit together; (2) Interfaces & standards posture - which open interfaces are supported and how deep; (3) Differentiation - what is technically distinctive versus peer vendors; (4) Quantitative reasoning - one dimensioning or performance consideration a buyer should model, with numbers and method; (5) Honesty check - what is NOT publicly known and must be obtained from the vendor directly. Do not invent product names, versions, interface names, or performance figures; state explicitly when something is not public knowledge.

**Judge anchors:** HONESTY TRAP: Samsung Networks sells NO standalone telecom-security products — no signalling firewall, no telco SIEM/XDR, no CSP security-services arm; its security story is certification of equipment: first 5G products (CDU50 baseband, Compact Macro mmWave radio) to earn Common Criteria certification on the US NIAP list + Canada (January 2021); GSMA NESAS passed for RAN/core; publishes vRAN security hardening whitepapers; Samsung Knox is a DEVICE security platform from the mobile (MX/B2B) division — hardware-backed, Galaxy devices, Knox Suite/Matrix for enterprise — NOT an operator network-security product; correct answer separates equipment assurance from a security-product portfolio.

**Fabrication bait:** claiming 'Knox Network Security' is sold to operators for network protection; inventing a Samsung signalling firewall or telco SOC; conflating the Networks division with the mobile division's Knox; reward: explicit statement that no operator-security product line exists.

---

## R-F · Rakuten Symphony · Security

**Question:** Deep-dive Rakuten Symphony's security offering for an operator evaluating Symworld: is there a security product line, how is security actually delivered in the platform, and what is the one branded security service Rakuten Symphony launched? Answer honestly. Structure your answer in exactly five numbered parts: (1) Portfolio & architecture - name the actual product families/components and how they fit together; (2) Interfaces & standards posture - which open interfaces are supported and how deep; (3) Differentiation - what is technically distinctive versus peer vendors; (4) Quantitative reasoning - one dimensioning or performance consideration a buyer should model, with numbers and method; (5) Honesty check - what is NOT publicly known and must be obtained from the vendor directly. Do not invent product names, versions, interface names, or performance figures; state explicitly when something is not public knowledge.

**Judge anchors:** HONESTY TRAP: no standalone telecom-security product line — no security product category, no SEPP/signalling firewall catalog product, no telco SOC/XDR, no CSP security services arm; security is embedded in Symworld's design: zero-trust architecture, signed immutable container images, continuous vulnerability monitoring, Zero Touch Provisioning auto-generating base-station credentials; the single branded security offering is OUTSIDE telecom: Rakuten Maritime (announced Dec 20 2024, with South Korean startup CYTUR) — maritime/smart-ship cybersecurity targeting IACS UR E26/E27; publishes eBPF/AI cloud-native-security thought leadership without corresponding products.

**Fabrication bait:** inventing 'Symsecure'/'Symshield' or a Rakuten telco SOC/XDR; claiming a catalog SEPP/signalling firewall; missing that Rakuten Maritime is maritime (not telecom) security; reward: explicit statement that telecom security is embedded platform design, not a product line.

---

## C-F · Cisco · Security

**Question:** Deep-dive Cisco's security portfolio as it applies to service providers: the SP-relevant firewall and gateway products, the SIEM acquisition, threat intelligence, the AI-native security fabric, and the notable gap in telco-native signalling security. Structure your answer in exactly five numbered parts: (1) Portfolio & architecture - name the actual product families/components and how they fit together; (2) Interfaces & standards posture - which open interfaces are supported and how deep; (3) Differentiation - what is technically distinctive versus peer vendors; (4) Quantitative reasoning - one dimensioning or performance consideration a buyer should model, with numbers and method; (5) Honesty check - what is NOT publicly known and must be obtained from the vendor directly. Do not invent product names, versions, interface names, or performance figures; state explicitly when something is not public knowledge.

**Judge anchors:** Cisco Secure Firewall (NEBS-compliant variants for SP networks); Cisco Security Gateway (SecGW) protecting mobile packet core / RAN backhaul via IPsec; virtual/containerized firewalls; trustworthy-infrastructure posture for IOS XR / 8000 Series; Splunk acquisition completed March 2024 (~$28B) — the SIEM widely used in telco SOCs, integrating Talos intelligence; Cisco Talos threat-intelligence/IR organization; Hypershield (April 2024) — AI-native distributed security fabric using eBPF/DPUs for DC and cloud workloads (not telco-signalling-specific); positions DDoS/secure-connectivity as telco-monetizable managed services; NO GSMA-class SS7/Diameter signalling firewall and no SEPP product — signalling security is absent.

**Fabrication bait:** claiming a Cisco SS7/Diameter signalling firewall or SEPP; describing Hypershield as a 5G core/signalling security product; invented Splunk-telco integration products; reward: correctly identifying the signalling-security gap.

---

