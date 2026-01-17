# Awesome HCI-LLM-Agent Papers

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated collection of research papers on **HCI**, **LLM**, **MLLM**, **Agent**, **RAG**, **Agentic-RL**, and **Embodied AI** (2021–present).

> **[Jan 2025]** Added new sections: **Agentic-RL** and **MLLM**. Regular updates resumed.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=WILLOSCAR/Awesome-HCI-LLM&type=Date)](https://star-history.com/#WILLOSCAR/Awesome-HCI-LLM&Date)

## Quick Start

```bash
pip install -e .                          # Install CLI
paper add 2312.00752 LLM -t "llm, mamba"  # Add paper
paper search transformer -t IMU           # Search
paper stats                               # Statistics
```

## Documentation

- [USAGE.md](USAGE.md) - CLI reference
- [FIELDS_GUIDE.md](FIELDS_GUIDE.md) - Field guide
- [FORMAT_EXAMPLES.md](FORMAT_EXAMPLES.md) - Format examples

---

# HCI
<!-- TABLE_START: HCI -->
| Source | Title (Link) | Authors | Tag | Subjects | Additional info | Date |
|---|---|---|---|---|---|---|
| arXiv(v1) (CHI23) | [HOOV: Hand Out-Of-View Tracking for Proprioceptive Interaction using Inertial Sensing](https://arxiv.org/abs/2303.07016) | Paul Streli, et al. | IMU, VR, transformer | cs.HC, cs.CV, I.2; I.5; H.5 |  |  |
| Ubicomp23 | [From 2D to 3D: Facilitating Single-Finger Mid-Air Typing on QWERTY Keyboards with Probabilistic Touch Modeling](https://dl.acm.org/doi/10.1145/3580829) |  | mid air, text entry, VR |  |  |  |
| Ubicomp23 | [PrintShear: Shear Input Based on Fingerprint Deformation](https://dl.acm.org/doi/10.1145/3596257) |  | touch, finger input |  |  |  |
| arXiv(v1) (CHI23) | [IMUPoser: Full-Body Pose Estimation using IMUs in Phones, Watches, and Earbuds](https://arxiv.org/abs/2304.12518) | Vimal Mollyn, et al. | IMU, pose estimation, BiLSTM | cs.HC, cs.CV |  |  |
| arXiv(v1) 2024 | [IMUSIC: IMU-based Facial Expression Capture](https://arxiv.org/abs/2402.03944) | Youjia Wang, et al. | IMU, generation, simulate, transformer diffusion | cs.CV | code coming soon ([link](https://sites.google.com/view/projectpage-imusic)) | 2024.02 |
| Ubicomp23 | [I Know Your Intent: Graph-enhanced Intent-aware User Device Interaction Prediction via Contrastive Learning](https://dl.acm.org/doi/10.1145/3610906) |  | user device interaction, graph, attention, contrastive learning |  |  |  |
| Ubicomp23 | [Synthetic Smartwatch IMU Data Generation from In-the-wild ASL Videos](https://dl.acm.org/doi/abs/10.1145/3596261) |  | IMU, synthetic, ASL recognition |  |  |  |
| Ubicomp23 | [ThumbAir: In-Air Typing for Head Mounted Displays](https://dl.acm.org/doi/10.1145/3569474) |  | mid air, text entry, VR, HMD, user study |  |  |  |
| Ubicomp23 | [TwinkleTwinkle: Interacting with Your Smart Devices by Eye Blink](https://dl.acm.org/doi/abs/10.1145/3596238) |  | acoustic sensing, eye blink, signal process |  |  |  |
| Ubicomp23 | [Voicify Your UI: Towards Android App Control with Voice Commands](https://dl.acm.org/doi/10.1145/3581998) |  | design, smartphones, sound-based input, dl parser, UI |  |  |  |
| Ubicomp23 | [LapTouch: Using the Lap for Seated Touch Interaction with HMDs](https://dl.acm.org/doi/10.1145/3610878) |  | VR, seated, touch, on-body |  |  |  |
| Ubicomp23 | [GLOBEM: Cross-Dataset Generalization of Longitudinal Human Behavior Modeling](https://dl.acm.org/doi/10.1145/3569485) |  | generalizability, behavior modeling, passive sensing |  |  |  |
| Ubicomp23 | [StructureSense: Inferring Constructive Assembly Structures from User Behaviors](https://dl.acm.org/doi/10.1145/3570343) |  | tangible user interfaces, TUI, RFID, user modeling, bayesian inference |  |  |  |
| Ubicomp23 | [Naturalistic E-Scooter Maneuver Recognition with Federated Contrastive Rider Interaction Learning](https://dl.acm.org/doi/10.1145/3570345) |  | IMU, DCT, contrastive learning, asynchronous federated learning, ehavior analysis |  |  |  |
| Ubicomp23 | [TAO: Context Detection from Daily Activity Patterns Using Temporal Analysis and Ontology](https://dl.acm.org/doi/abs/10.1145/3610896) |  | behavioral context recognition, activity recognition, ontology, deep learning |  |  |  |
| Ubicomp23 | [HyWay: Enabling Mingling in the Hybrid World∗](https://dl.acm.org/doi/abs/10.1145/3596235) |  | hybrid mingling, unstructured and semi-structured conversations, awareness, agency, porosity, reciprocity |  |  |  |
| Ubicomp23 | [Exploring the Opportunities of AR for Enriching Storytelling with Family Photos between Grandparents and Grandchildren](https://dl.acm.org/doi/abs/10.1145/3610903) |  | AR, storytelling, intergenerational communication |  |  |  |
| Ubicomp23 | [Contact Tracing for Healthcare Workers in an Intensive Care Unit](https://dl.acm.org/doi/10.1145/3610924) |  | contact Tracing, Internet of things (IoT), bluetooth low energy, Covid-19 |  |  |  |
| Ubicomp23 | [A Data-Driven Context-Aware Health Inference System for Children during School Closures](https://dl.acm.org/doi/10.1145/3580800) |  | data analysis, school closures, health inference, risk factor analysis |  |  |  |
| Ubicomp23 | [Privacy-Enhancing Technology and Everyday Augmented Reality: Understanding Bystanders’ Varying Needs for Awareness and Consent](https://dl.acm.org/doi/10.1145/3569501) |  | AR, privacy, bystanders, altered reality, extended perception, biometrics |  |  |  |
| Ubicomp23 | [MoCaPose: Motion Capturing with Textile-integrated Capacitive Sensors in Loose-fitting Smart Garments](https://dl.acm.org/doi/abs/10.1145/3580883) |  | motion capture, wearable sensing, capacitive sensing, deep learning, motion tracking, smart textile |  |  |  |
| Ubicomp23 | [PoseSonic: 3D Upper Body Pose Estimation Through Egocentric Acoustic Sensing on Smartglasses](https://dl.acm.org/doi/abs/10.1145/3610895?af=R) |  | human pose estimation, acoustic sensing, smart/AR glasses, deep learning, cross-modal supervision |  |  |  |
| Ubicomp23 | [MI-Poser: Human Body Pose Tracking Using Magnetic and Inertial Sensor Fusion with Metal Interference Mitigation](https://dl.acm.org/doi/10.1145/3610891) |  | EMF, body pose tracking, inverse kinematics, sensor fusion |  |  |  |
| Ubicomp23 | [Headar: Sensing Head Gestures for Confirmation Dialogs on Smartwatches with Wearable Millimeter-Wave Radar](https://dl.acm.org/doi/abs/10.1145/3610900) |  | wearable interaction, gestural input, millimeter-wave radar, head gestures, smartwatch |  |  |  |
| Ubicomp23 | [DRG-Keyboard: Enabling Subtle Gesture Typing on the Fingertip with Dual IMU Rings](https://dl.acm.org/doi/10.1145/3569463) |  | text entry, gesture keyboard, fingertip interaction, smart ring |  |  |  |
| Ubicomp23 | [Abacus Gestures: A Large Set of Math-Based Usable Finger-Counting Gestures for Mid-Air Interactions](https://dl.acm.org/doi/10.1145/3610898) |  | vision, mid-air, gesture interaction, math, finger counting, abacus |  |  |  |
| Ubicomp23 | [sUrban: Stable Prediction for Unseen Urban Data from Location-based Sensors](https://dl.acm.org/doi/abs/10.1145/3610877) |  | urban computing, location-based data, spatial-temporal prediction, out-of-distribution data |  |  |  |
| Ubicomp23 | [Spectral-Loc: Indoor Localization Using Light Spectral Information](https://dl.acm.org/doi/10.1145/3580878) |  | indoor localization, spectral information, ambient light |  |  |  |
| arXiv(v2) 2024 | [IMUOptimize: A Data-Driven Approach to Optimal IMU Placement for Human Pose Estimation with Transformer Architecture](https://arxiv.org/abs/2402.08923) | Varun Ramani, et al. | IMU, transformer, interpretability, data driven, time series | cs.LG |  | 2024.02 |
| arXiv(v1) (CVPR24) | [Dynamic Inertial Poser (DynaIP): Part-Based Motion Dynamics Learning for Enhanced Human Pose Estimation with Sparse Inertial Sensors](https://arxiv.org/abs/2312.02196) | Yu Zhang, et al. | IMU, sparse inertial sensors | cs.CV |  | 2024.03 |
| Ubicomp23 | [N-euro Predictor: A Neural Network Approach for Smoothing and Predicting Motion Trajectory](https://dl.acm.org/doi/10.1145/3610884) |  | vision-based interactions, motion-to-photon latency, motion prediction, neural network, perceived jitter and lag |  |  |  |
| Ubicomp23 | [GC-Loc: A Graph Attention Based Framework for Collaborative Indoor Localization Using Infrastructure-free Signals](https://dl.acm.org/doi/10.1145/3569495) |  | collaborative indoor localization, graph neural network, geomagnetism |  |  |  |
| arXiv(v5) 2024 | [Evaluating Human-Language Model Interaction](https://arxiv.org/abs/2212.09746) | Mina Lee, et al. | LM, human-centered, evaluation | cs.CL |  |  |
| Ubicomp23 | [WristAcoustic: Through-Wrist Acoustic Response Based Authentication for Smartwatches](https://dl.acm.org/doi/10.1145/3569473) |  | smartwatch authentication, bone conduction, acoustic response |  |  |  |
| Ubicomp23 | [VibPath: Two-Factor Authentication with Your Hand's Vibration Response to Unlock Your Phone](https://dl.acm.org/doi/10.1145/3610894) |  | user authentication, vibration, IMU, smartphone, wearables, smartwatch |  |  |  |
| Ubicomp24 | [CAvatar: Real-time Human Activity Mesh Reconstruction via Tactile Carpets](https://dl.acm.org/doi/pdf/10.1145/3631424) |  | human activity reconstruction, 3D human mesh, pressure and vibrations, tactile sensor |  |  |  |
| Ubicomp23 | [NF-Heart: A Near-field Non-contact Continuous User Authentication System via Ballistocardiogram](https://dl.acm.org/doi/10.1145/3580851) |  | continuous authentication, ballistocardiogram (BCG), biometrics, non-contact sensing, smart chair |  |  |  |
| Ubicomp23 | [Fingerprinting IoT Devices Using Latent Physical Side-Channels](https://dl.acm.org/doi/abs/10.1145/3596247) |  | physical side-channels, fingerprinting, internet-of-things |  |  |  |
| Ubicomp23 | [ViSig: Automatic Interpretation of Visual Body Signals Using On-Body Sensors](https://dl.acm.org/doi/10.1145/3580797) |  | visual signalling, on-body sensors, UWB, IMU, body signals, fallback communication, sports automation, postures, gestures |  |  |  |
| Ubicomp24 | Mental-LLM: Leveraging Large Language Models for Mental Health Prediction via Online Text Data |  |  |  |  |  |
| Ubicomp23 | SkinLink: On-body Construction and Prototyping of Reconfigurable Epidermal Interfaces |  |  |  |  |  |
| Ubicomp23 | Radio2Text: Streaming Speech Recognition Using mmWave Radio Signals |  |  |  |  |  |
| Ubicomp23 | HIPPO: Pervasive Hand-Grip Estimation from Everyday Interactions |  |  |  |  |  |
| Ubicomp23 | LT-Fall: The Design and Implementation of a Life-threatening Fall Detection and Alarming System |  |  |  |  |  |
| Ubicomp22 | [IF-ConvTransformer: A Framework for Human Activity Recognition Using IMU Fusion and ConvTransformer](https://dl.acm.org/doi/10.1145/3534584) |  | IMU, fusion, multimodal, transformer, attention |  |  |  |
| ISWC 2023 | [On the Utility of Virtual On-body Acceleration Data for Fine-grained Human Activity Recognition](https://dl.acm.org/doi/10.1145/3594738.3611364) |  | HAR, virtual, IMU |  |  |  |
| ISWC 2023 | [C-Auth: Exploring the Feasibility of Using Egocentric View of Face Contour for User Authentication on Glasses](https://dl.acm.org/doi/10.1145/3594738.3611355) |  | smart glasses, authentication, ecocentric view |  |  |  |
| ISWC 2023 | Towards a Haptic Taxonomy of Emotions: Exploring Vibrotactile Stimulation in the Dorsal Region |  |  |  |  |  |
| arXiv(v2) 2024 | [Finding Candidate TeV Halos among Very-High Energy Sources](http://arxiv.org/abs/2403.16074v2) | Dong Zheng, et al. | VR, AR, egocentric, pose estimation | astro-ph.HE | 15 pages, 7 figures, 4 tables, referee's comments incorporated, accepted for publication in ApJ | 2024.05 |
| arXiv(v1) 2024 | [Exploring Text-to-Motion Generation with Human Preference](http://arxiv.org/abs/2404.09445v1) | Jenny Sheng, et al. | IMU, human object interaction, dataset | cs.LG, cs.AI, cs.CV | Accepted to CVPR 2024 HuMoGen Workshop | 2024.04 |
| arXiv(v1) 2024 | [LLMs in HCI Data Work: Bridging the Gap Between Information Retrieval and Responsible Research Practices](http://arxiv.org/abs/2403.18173v1) | Neda Taghizadeh Serajeh, et al. | VR, AR, avatar control, pose estimation | cs.HC, cs.IR | 5 pages, CHI2024 Workshop on LLMs as Research Tools: Applications and Evaluations in HCI Data Work | 2024.03 |
| arXiv(v1) 2024 | [Modeling stock price dynamics on the Ghana Stock Exchange: A Geometric Brownian Motion approach](http://arxiv.org/abs/2403.13192v1) | Dennis Lartey Quayesam, et al. | VR, AR, motion capture, egocentric | math.OC, q-fin.ST |  | 2024.03 |
| Ubicomp23 | [CAvatar](https://doi.org/10.1145/3631424) | Wenqiang Chen, et al. | human activity, 3D mesh, tactile, pressure |  |  | 2023.12 |
| Ubicomp24 | [ViObject](https://doi.org/10.1145/3643547) | Wenqiang Chen, et al. | mental health, LLM, text data |  |  | 2024.03 |
| Ubicomp24 | [HyperHAR](https://doi.org/10.1145/3643511) | Nafees Ahmad, et al. | LLM, passive sensing, sensemaking |  |  | 2024.03 |
| arXiv(v1) 2024 | [WheelPoser: Sparse-IMU Based Body Pose Estimation for Wheelchair Users](http://arxiv.org/abs/2409.08494v1) | Yunzhi Li, et al. | IMU, pose estimation, wheelchair, accessibility | cs.GR, cs.CV, cs.HC | Accepted by ASSETS 2024 | 2024.09 |
| arXiv(v1) 2024 | [Modeling and optimization for arrays of water turbine OWC devices](http://arxiv.org/abs/2403.14509v1) | M. Gambarini, et al. | VR, AR, motion capture, egocentric, stereo camera | math.OC, physics.flu-dyn |  | 2024.03 |
| arXiv(v2) 2025 (PRX Quantum 6, 020311 (April 2025)) | [Device-Independent Quantum Key Distribution Based on Routed Bell Tests](http://arxiv.org/abs/2404.01202v2) | Tristan Le Roy-Deloison, et al. | IMU, RGB, human object interaction, dataset, 3D tracking | quant-ph | Version2: Slight improvements in the text. Close to published version | 2025.05 |
| arXiv(v1) 2024 | [On depth prediction for autonomous driving using self-supervised learning](http://arxiv.org/abs/2403.06194v1) | Houssem Boulahbal, et al. | VR, AR, avatar, pose estimation, headset | cs.CV | PhD thesis | 2024.03 |
| arXiv(v1) 2024 | [Evaluating Text Classification Robustness to Part-of-Speech Adversarial Examples](http://arxiv.org/abs/2408.08374v1) | Anahita Samadi, et al. | IMU, transformer, pose estimation, calibration | cs.CL, cs.LG |  | 2024.08 |
| arXiv(v2) 2025 | [Modeling Future Conversation Turns to Teach LLMs to Ask Clarifying Questions](http://arxiv.org/abs/2410.13788v2) | Michael J. Q. Zhang, et al. | IMU, diffusion, pose estimation, loose sensor | cs.CL | Presented at ICLR 2025 | 2025.03 |
| arXiv(v1) 2025 | [Broadband shot-to-shot transient absorption anisotropy](http://arxiv.org/abs/2503.14144v1) | Maximilian Binzer, et al. | VR, AR, egocentric, motion capture, FRAME | physics.optics | The following article has been submitted to The Journal of Physical Chemistry. After it is published, it will be found at https://pubs.aip.org/aip/jcp | 2025.03 |
| arXiv(v2) 2024 | [PRISM: Patient Records Interpretation for Semantic Clinical Trial Matching using Large Language Models](http://arxiv.org/abs/2404.15549v2) | Shashi Kant Gupta, et al. | IMU, RGB, HOI, dataset, tracking | cs.CL, cs.AI | 30 Pages, 8 Figures, Supplementary Work Attached | 2024.04 |
| arXiv(v1) 2024 | [Bayesian Learned Models Can Detect Adversarial Malware For Free](http://arxiv.org/abs/2403.18309v1) | Bao Gia Doan, et al. | VR, AR, simulated avatar, headset | cs.CR | Accepted to the 29th European Symposium on Research in Computer Security (ESORICS) 2024 Conference | 2024.03 |
| CHI24 | [Towards Robotic Companions: Understanding Handler-Guide Dog Interactions for Informed Guide Dog Robot Design](https://doi.org/10.1145/3613904.3642181) | Hochul Hwang, et al. | LLM, HCI, CHI, interaction |  |  | 2024.05 |
| arXiv(v4) 2025 | [LLaSA: A Sensor-Aware LLM for Natural Language Reasoning of Human Activity from IMU Data](http://arxiv.org/abs/2406.14498v4) | Sheikh Asif Imran, et al. | IMU, LLM, wearable, sensor, HAR | cs.CL |  | 2025.09 |
| arXiv(v1) 2024 | [IMUGPT 2.0: Language-Based Cross Modality Transfer for Sensor-Based Human Activity Recognition](http://arxiv.org/abs/2402.01049v1) | Zikang Leng, et al. | IMU, LLM, cross-modality, HAR | cs.CV |  | 2024.02 |
| arXiv(v4) 2025 | [SensorLLM: Aligning Large Language Models with Motion Sensors for Human Activity Recognition](http://arxiv.org/abs/2410.10624v4) | Zechen Li, et al. | IMU, LLM, motion sensor, HAR | cs.CL | Accepted by EMNLP 2025 Main Conference | 2025.08 |
| arXiv(v2) 2024 | [Health-LLM: Large Language Models for Health Prediction via Wearable Sensor Data](http://arxiv.org/abs/2401.06866v2) | Yubin Kim, et al. | LLM, wearable, health prediction | cs.CL, cs.AI, cs.LG |  | 2024.04 |
| Ubicomp24 | [Sensor2Text: Enabling Natural Language Interactions for Daily Activity Tracking Using Wearable Sensors](https://doi.org/10.1145/3699747) | Wenqiang Chen, et al. | LLM, wearable, natural language, activity tracking |  |  | 2024.11 |
| CHI25 | [Interactive Debugging and Steering of Multi-Agent AI Systems](https://doi.org/10.1145/3706598.3713581) | Will Epperson, et al. | LLM, agent, multi-agent, debugging, HCI |  |  | 2025.04 |
| CHI25 | [Understanding the LLM-ification of CHI: Unpacking the Impact of LLMs at CHI through a Systematic Literature Review](https://doi.org/10.1145/3706598.3713726) | Rock Yuren Pang, et al. | LLM, HCI, CHI, survey, systematic review |  |  | 2025.04 |
| CHI25 | [Users' Expectations and Practices with Agent Memory](https://doi.org/10.1145/3706599.3720158) | Brennan Jones, et al. | LLM, agent, memory, user expectations, HCI |  |  | 2025.04 |
| arXiv(v4) 2025 | [LLM-Based Human-Agent Collaboration and Interaction Systems: A Survey](http://arxiv.org/abs/2505.00753v4) | Hengyi Peng, et al. | LLM, agent, human-agent collaboration, HCI, survey | cs.HC, cs.AI, cs.CL |  | 2025.05 |
| arXiv(v1) 2025 | [Through the Lens of Human-Human Collaboration: A Configurable Research Platform for Exploring Human-Agent Collaboration](http://arxiv.org/abs/2509.18008v1) | Bingsheng Yao, et al. | LLM, agent, human-agent collaboration, CSCW, platform | cs.HC, cs.AI, cs.CL |  | 2025.09 |
| arXiv(v1) 2025 | [MobilePoser: Real-Time Full-Body Pose Estimation and 3D Human Translation from IMUs in Mobile Consumer Devices](http://arxiv.org/abs/2504.12492v1) | Vimal Mollyn, et al. | IMU, pose estimation, mobile, consumer device, real-time | cs.CV, cs.HC |  | 2025.04 |
| arXiv(v1) 2025 | [BaroPoser: Real-time Human Motion Tracking from IMUs and Barometers in Everyday Devices](http://arxiv.org/abs/2508.03313v1) | Riku Arakawa, et al. | IMU, barometer, pose estimation, motion tracking | cs.CV, cs.HC |  | 2025.08 |
| arXiv(v1) 2024 | [EMHI: A Multimodal Egocentric Human Motion Dataset with HMD and Body-Worn IMUs](http://arxiv.org/abs/2408.17168v1) | Zelin Ye, et al. | IMU, VR, HMD, dataset, egocentric, pose estimation | cs.CV, cs.HC | 885 sequences, 58 subjects, 28.5 hours | 2024.08 |
| arXiv(v1) 2025 | [Garment Inertial Poser: Human Motion Capture from Loose and Sparse Inertial Sensors with Garment-aware Diffusion Models](http://arxiv.org/abs/2506.15290v1) | Tao Wang, et al. | IMU, pose estimation, loose sensor, diffusion, garment | cs.CV |  | 2025.06 |
| arXiv(v1) 2025 | [Ego4o: Egocentric Human Motion Capture and Understanding from Multi-Modal Input](http://arxiv.org/abs/2504.08449v1) | Jian Wang, et al. | egocentric, IMU, pose estimation, multimodal, VR | cs.CV, cs.HC |  | 2025.04 |
| arXiv(v1) 2025 | [DiffCap: Diffusion-based Real-time Human Motion Capture using Sparse IMUs and a Monocular Camera](http://arxiv.org/abs/2508.06139v1) | Zongmian Li, et al. | IMU, diffusion, motion capture, real-time, camera | cs.CV |  | 2025.08 |
| arXiv(v2) 2026 | [LLM-Guided Exemplar Selection for Few-Shot Wearable-Sensor Human Activity Recognition](http://arxiv.org/abs/2512.22385v2) | Elsen Ronando, et al. | LLM, HAR, wearable, few-shot, exemplar selection | cs.CL, cs.AI, cs.CV | 88.78% F1 on UCI-HAR | 2025.12 |
| arXiv(v1) 2025 | [SensorLM: Learning the Language of Wearable Sensors](http://arxiv.org/abs/2506.09108v1) | Tong Xia, et al. | wearable, sensor, LLM, activity recognition, foundation model | cs.LG, cs.HC |  | 2025.06 |
| CHI25 | [Gesture and Audio-Haptic Guidance Techniques to Direct Conversations with Intelligent Voice Interfaces](https://doi.org/10.1145/3706598.3714310) | Xiyuan Shen, et al. | LLM, wearable, voice interface, gesture, haptic, smart glasses |  | Ray-Ban Meta Glasses, GPT-4o | 2025.04 |
| CHI25 | [Exploring Personalized Health Support through Data-Driven, Theory-Guided LLMs: A Case Study in Sleep Health](https://doi.org/10.1145/3706598.3713852) | Xin Tong, et al. | LLM, wearable, health, sleep, personalized, chatbot |  | HealthGuru multi-agent framework | 2025.04 |
| CHI25 | [LLM Integration in Extended Reality: A Comprehensive Review of Current Trends, Challenges, and Future Perspectives](https://doi.org/10.1145/3706598.3714224) | Chengkun Wu, et al. | LLM, VR, AR, XR, survey, extended reality |  | Survey paper | 2025.04 |
| CHI25 | [FIP: Endowing Robust Motion Capture on Daily Garment by Fusing Flex and Inertial Sensors](https://doi.org/10.1145/3706598.3714140) | Yiwei Zhao, et al. | IMU, flex sensor, motion capture, pose estimation, garment |  | 19.5% improvement over SOTA | 2025.04 |
| CHI25 | [WritingRing: Enabling Natural Handwriting Input with a Single IMU Ring](https://doi.org/10.1145/3706598.3714066) | Xiaoying Yang, et al. | IMU, ring, handwriting, text entry, wearable |  | Single IMU ring | 2025.04 |
| CHI25 | [Talk to the Hand: an LLM-powered Chatbot with Visual Pointer as Proactive Companion for On-Screen Tasks](https://doi.org/10.1145/3706598.3715579) | Zhepeng Wang, et al. | LLM, chatbot, UI, on-screen tasks, visual pointer |  |  | 2025.04 |
| CHI25 | [ChainBuddy: An AI-assisted Agent System for Generating LLM Pipelines](https://doi.org/10.1145/3706598.3714085) | Xinyue Chen, et al. | LLM, agent, pipeline, AI-assisted, prompt engineering |  |  | 2025.04 |
| CHI25 | [GazeNoter: Co-Piloted AR Note-Taking via Gaze Selection of LLM Suggestions to Match Users' Intentions](https://doi.org/10.1145/3706598.3714294) | Zhiyi Rong, et al. | LLM, AR, gaze, note-taking, eye tracking |  |  | 2025.04 |
| CHI25 | [Canvil: Designerly Adaptation for LLM-Powered User Experiences](https://doi.org/10.1145/3706598.3713139) | Kenneth Li, et al. | LLM, design, UX, user experience, adaptation |  |  | 2025.04 |
| CHI25 | [Playing Dumb to Get Smart: Creating and Evaluating an LLM-based Teachable Agent within University Computer Science Classes](https://doi.org/10.1145/3706598.3713644) | Naiming Liu, et al. | LLM, teachable agent, education, learning |  |  | 2025.04 |
| UIST24 | [SHAPE-IT: Exploring Text-to-Shape-Display for Generative Shape-Changing Behaviors with LLMs](https://doi.org/10.1145/3654777.3676348) | Wanli Qian, et al. | LLM, shape display, tangible, generative, text-to-shape |  | AI-chaining approach | 2024.10 |
| UIST24 | [VizAbility: Enhancing Chart Accessibility with LLM-based Conversational Interaction](https://doi.org/10.1145/3654777.3676414) | Mandi Cai, et al. | LLM, accessibility, chart, visualization, conversational |  |  | 2024.10 |
| UIST24 | [Patchview: LLM-powered Worldbuilding with Generative Dust and Magnet Visualization](https://doi.org/10.1145/3654777.3676352) | Jeongyeon Kim, et al. | LLM, worldbuilding, writing, creative, visualization |  |  | 2024.10 |
| UIST24 | [SituationAdapt: Contextual UI Optimization in Mixed Reality with Situation Awareness via LLM Reasoning](https://doi.org/10.1145/3654777.3676470) | Zhipeng Li, et al. | LLM, MR, UI, adaptive, context-aware, mixed reality |  |  | 2024.10 |
| Ubicomp24 | [IMUGPT 2.0: Language-Based Cross Modality Transfer for Sensor-Based Human Activity Recognition](https://doi.org/10.1145/3678545) | Zikang Leng, et al. | IMU, LLM, HAR, cross-modality, motion synthesis |  | 20 citations, IMWUT Vol 8 Issue 3 | 2024.09 |
| Ubicomp25 | [One Model to Fit Them All: Universal IMU-based Human Activity Recognition with LLM-assisted Cross-dataset Representation](https://doi.org/10.1145/3749509) | Wei Wei, et al. | IMU, LLM, HAR, universal model, cross-dataset |  | IMWUT Vol 9 Issue 3 | 2025.09 |
| SenSys25 | [Toward Sensor-In-the-Loop LLM Agent: Benchmarks and Implications](https://doi.org/10.1145/3715014.3722082) | Zechen Li, et al. | LLM, agent, sensor, wearable, benchmark |  |  | 2025.11 |
| CSCW24 | [Is Human-AI Interaction CSCW?](https://doi.org/10.1145/3678884.3689134) | Meredith Ringel Morris, et al. | human-AI collaboration, CSCW, LLM, panel |  | Panel discussion | 2024.11 |
| CSCW25 | [An Emergent Understanding of Human-AI Collaboration in Deliberation](https://doi.org/10.1145/3715070.3749265) | Authors TBD, et al. | LLM, human-AI collaboration, deliberation, citizen assembly |  |  | 2025.11 |
| CSCW25 | [Exploring Collaboration Patterns and Strategies in Human-AI Co-creation through the Lens of Agency: A Scoping Review](https://doi.org/10.1145/3757594) | Authors TBD, et al. | human-AI co-creation, agency, collaboration, scoping review |  | PACM HCI | 2025.11 |
| CHI25 | [HaptiCoil: Soft Programmable Buttons with Hydraulically Coupled Haptic Feedback and Sensing](https://doi.org/10.1145/3706598.3713175) | Authors TBD, et al. | haptic, soft button, sensing, feedback |  | 1-500Hz bandwidth | 2025.04 |
| CHI25 | [BudsID: Mobile-Ready and Expressive Finger Identification Input for Earbuds](https://doi.org/10.1145/3706598.3714133) | Authors TBD, et al. | earbuds, finger identification, magnetometer, wearable |  | 96.9% accuracy | 2025.04 |
| CHI25 | [FingerGlass: Enhancing Smart Glasses Interaction via Fingerprint Sensing](https://doi.org/10.1145/3706598.3713929) | Authors TBD, et al. | smart glasses, fingerprint, gesture recognition, CNN, LSTM |  |  | 2025.04 |
| CHI25 | [PPG Earring: Wireless Smart Earring for Heart Health Monitoring](https://doi.org/10.1145/3706598.3713856) | Authors TBD, et al. | PPG, earring, heart rate, wearable, health monitoring |  | 14mm, 2g, 21h battery | 2025.04 |
| CHI25 | [BallistoBud: Heart Rate Variability Monitoring using Earbud Accelerometry for Stress Assessment](https://doi.org/10.1145/3706598.3714029) | Authors TBD, et al. | earbuds, accelerometer, BCG, heart rate, stress |  |  | 2025.04 |
| CHI25 | [Cross, Dwell, or Pinch: Around-Device Selection Methods for Unmodified Smartwatches](https://doi.org/10.1145/3706598.3714308) | Authors TBD, et al. | smartwatch, sonar, around-device, input |  | First sonar-based around-device input on consumer smartwatch | 2025.04 |
| CHI25 | [Spatial Haptics: A Sensory Substitution Method for Distal Object Detection Using Tactile Cues](https://doi.org/10.1145/3706598.3714083) | Authors TBD, et al. | haptic, tactile, sensory substitution, localization |  |  | 2025.04 |
| CHI25 | [VibWalk: Mapping Lower-limb Haptic Experiences of Everyday Walking](https://doi.org/10.1145/3706598.3714254) | Authors TBD, et al. | haptic, walking, vibration, wearable, foot |  |  | 2025.04 |
| CHI25 | [Prototyping with Prompts: Emerging Approaches and Challenges in Generative AI Design](https://doi.org/10.1145/3706598.3713166) | Hari Subramonyam, et al. | generative AI, prompt engineering, design, prototyping |  |  | 2025.04 |
| CHI25 | [FusAIn: Composing Generative AI Visual Prompts Using Pen-based Interaction](https://doi.org/10.1145/3706598.3714027) | Xiaohan Peng, et al. | generative AI, pen-based, prompt, visual design |  |  | 2025.04 |
| CHI25 | [IdeationWeb: Tracking the Evolution of Design Ideas in Human-AI Co-Creation](https://doi.org/10.1145/3706598.3713375) | Authors TBD, et al. | LLM, human-AI co-creation, ideation, design |  |  | 2025.04 |
| CHI25 | [Inkspire: Supporting Design Exploration with Generative AI through Analogical Sketching](https://doi.org/10.1145/3706598.3713397) | Authors TBD, et al. | generative AI, T2I, sketching, design exploration |  |  | 2025.04 |
| CHI25 | [AI-Instruments: Embodying Prompts as Instruments](https://doi.org/10.1145/3706598.3714259) | Authors TBD, et al. | LLM, prompt, instruments, direct manipulation |  |  | 2025.04 |
| UIST25 | [SketchGPT: A Sketch-based Multimodal Interface for Application-Agnostic LLM Interaction](https://doi.org/10.1145/3746059.3747598) | Authors TBD, et al. | LLM, sketch, multimodal, interface |  |  | 2025.10 |
| UIST25 | [ImaginationVellum: Generative-AI Ideation Canvas with Spatial Prompts](https://doi.org/10.1145/3746059.3747631) | Authors TBD, et al. | generative AI, ideation, canvas, spatial prompts, co-creation |  |  | 2025.10 |
| TEI25 | [Tangible LLMs: Tangible Sense-Making For Trustworthy Large Language Models](https://doi.org/10.1145/3689050.3708338) | Authors TBD, et al. | LLM, tangible, trustworthy AI, physical interface |  |  | 2025.02 |
| Ubicomp25 | [Hapt-Aids: Self-Powered, On-Body Haptics for Activity Monitoring](https://doi.org/10.1145/3749468) | Authors TBD, et al. | haptic, self-powered, activity monitoring, wearable |  | IMWUT Vol 9 Issue 3 | 2025.09 |
| CHI24 | [As an AI language model I cannot: Investigating LLM Denials of User Requests](https://doi.org/10.1145/3613904.3642135) | Authors TBD, et al. | LLM, denial, user request, perception |  |  | 2024.05 |
| CHI24 | [Learning Agent-based Modeling with LLM Companions: ChatGPT and NetLogo Chat](https://doi.org/10.1145/3613904.3642377) | Authors TBD, et al. | LLM, agent-based modeling, NetLogo, learning |  |  | 2024.05 |
| CHI24 | [CharacterMeet: Supporting Creative Writers' Character Construction Through LLM-Powered Chatbot Avatars](https://doi.org/10.1145/3613904.3642105) | Authors TBD, et al. | LLM, chatbot, creative writing, character design |  |  | 2024.05 |
| CHI24 | [ChaCha: Leveraging Large Language Models to Prompt Children to Share Their Emotions](https://doi.org/10.1145/3613904.3642152) | Authors TBD, et al. | LLM, chatbot, children, emotion, conversation |  |  | 2024.05 |
| CHI24 | [How AI Processing Delays Foster Creativity: CoQuest](https://doi.org/10.1145/3613904.3642698) | Authors TBD, et al. | LLM, agent, research question, creativity, co-creation |  |  | 2024.05 |
| CHI24 | [Understanding the Impact of Long-Term Memory on Self-Disclosure with LLM-Driven Chatbots](https://doi.org/10.1145/3613904.3642420) | Authors TBD, et al. | LLM, chatbot, long-term memory, self-disclosure, health |  |  | 2024.05 |
| CHI24 | [The HaLLMark Effect: Supporting Provenance and Transparent Use of LLMs in Writing](https://doi.org/10.1145/3613904.3641895) | Authors TBD, et al. | LLM, writing, provenance, visualization, transparency |  |  | 2024.05 |
| CHI24 | [Bridging the Gulf of Envisioning: Cognitive Challenges in Prompt Based Interactions with LLMs](https://doi.org/10.1145/3613904.3642754) | Authors TBD, et al. | LLM, prompt, cognitive challenges, user study |  |  | 2024.05 |
| Ubicomp24 | [Leveraging LLMs to Predict Affective States via Smartphone Sensor Features](https://doi.org/10.1145/3675094.3678420) | Authors TBD, et al. | LLM, smartphone, sensing, affective state, digital phenotyping |  | First LLM work for affective state prediction | 2024.10 |
| Ubicomp24 | [Leveraging Large Language Models for Generating Mobile Sensing Strategies in Human Behavior Modeling](https://doi.org/10.1145/3675094.3678423) | Authors TBD, et al. | LLM, mobile sensing, behavior modeling, strategy generation |  |  | 2024.10 |
| Ubicomp24 | [Capturing the College Experience: A Four-Year Mobile Sensing Study of Mental Health](https://doi.org/10.1145/3643501) | Authors TBD, et al. | mobile sensing, mental health, college, longitudinal |  | 19 citations, IMWUT Vol 8 Issue 1 | 2024.03 |
| SenSys25 | [Demo: An LLM-Powered Multimodal Mobile Sensing System for Personalized Health Behavior Analysis](https://doi.org/10.1145/3715014.3724376) | Authors TBD, et al. | LLM, mobile sensing, multimodal, health, personalized |  | Demo paper | 2025.11 |
| CHI25 | [LifeInsight: Design and Evaluation of an AI-Powered Assistive Wearable for Blind and Low Vision People](https://doi.org/10.1145/3706598.3713486) | Authors TBD, et al. | AI, wearable, accessibility, BLV, assistive |  |  | 2025.04 |
| CHI25 | [Human Robot Interaction for Blind and Low Vision People: A Systematic Literature Review](https://doi.org/10.1145/3706598.3713438) | Authors TBD, et al. | robot, accessibility, BLV, HRI, survey |  |  | 2025.04 |
| CHI25 | [TableNarrator: Making Image Tables Accessible to Blind and Low Vision People](https://doi.org/10.1145/3706598.3714329) | Authors TBD, et al. | accessibility, BLV, tables, image, data |  |  | 2025.04 |
| CHI25 | [DanmuA11y: Making Time-Synced Video Comments Accessible to BLV Users](https://doi.org/10.1145/3706598.3713496) | Authors TBD, et al. | accessibility, BLV, video, Danmu, audio |  |  | 2025.04 |
| Ubicomp25 | [HandSAW: Wearable Hand-based Event Recognition via On-Body Surface Acoustic Waves](https://doi.org/10.1145/3712276) | Kaylee Yaxuan Li, et al. | SAW, wrist, hand, object interaction, wearable |  | IMWUT Vol 9 Issue 1 | 2025.03 |
| Ubicomp25 | [Respiration Rate Estimation via Smartwatch-based PPG and Accelerometer Data](https://doi.org/10.1145/3712280) | Authors TBD, et al. | respiration, smartwatch, PPG, accelerometer, transfer learning |  | IMWUT Vol 9 Issue 1 | 2025.03 |
| Ubicomp25 | [Ring-a-Pose: A Ring for Continuous Hand Pose Tracking](https://doi.org/10.1145/3699741) | Authors TBD, et al. | ring, hand pose, tracking, wearable |  | IMWUT | 2025.03 |
| Ubicomp25 | [Sleep Monitoring with Continuous Posture, Heart Rate, Respiratory Rate Tracking](https://doi.org/10.1145/3749461) | Authors TBD, et al. | sleep, posture, heart rate, respiration, monitoring |  | IMWUT Vol 9 Issue 3 | 2025.09 |
| Ubicomp25 | [Contact-free Vital Signs Monitoring and Separating Distinct Vital Signs](https://doi.org/10.1145/3749496) | Authors TBD, et al. | vital signs, contactless, respiration, monitoring |  | IMWUT Vol 9 Issue 3 | 2025.09 |
| Ubicomp25 | [Mindfulness Meditation and Respiration: Accelerometer-based Respiration Rate Estimation](https://doi.org/10.1145/3749498) | Authors TBD, et al. | mindfulness, respiration, accelerometer, meditation |  | IMWUT Vol 9 Issue 3 | 2025.09 |
| CHI25 | [RadEye: Tracking Eye Motion Using FMCW Radar](https://doi.org/10.1145/3706598.3713775) | Authors TBD, et al. | radar, eye tracking, FMCW, gaze |  |  | 2025.04 |
| CHI25 | [Online-EYE: Multimodal Implicit Eye Tracking Calibration for XR](https://doi.org/10.1145/3706598.3713461) | Authors TBD, et al. | eye tracking, XR, VR, calibration, implicit |  |  | 2025.04 |
| CHI25 | [COMETIC: Enhancing Smartphone Eye Tracking with Cursor-Based Implicit Calibration](https://doi.org/10.1145/3706598.3713936) | Authors TBD, et al. | eye tracking, smartphone, calibration, cursor |  | 27.2% improvement | 2025.04 |
| CHI25 | [Lookee: Gaze Tracking-based Infant Vocabulary Comprehension Assessment](https://doi.org/10.1145/3706598.3713386) | Authors TBD, et al. | gaze, infant, vocabulary, assessment, AI |  |  | 2025.04 |
| CHI25 | [SocialEyes: Scaling Mobile Eye-tracking to Multi-person Social Settings](https://doi.org/10.1145/3706598.3713910) | Authors TBD, et al. | eye tracking, mobile, social, multi-person |  |  | 2025.04 |
| CHI25 | [M2SILENT: Enabling Multi-user Silent Speech Interactions via Multi-directional Speakers](https://doi.org/10.1145/3706598.3714174) | Authors TBD, et al. | silent speech, multi-user, speaker, shared space |  |  | 2025.04 |
| CHI25 | [Spatial Speech Translation: Translating Across Space With Binaural Hearables](https://doi.org/10.1145/3706598.3713745) | Authors TBD, et al. | speech translation, binaural, hearables, spatial audio |  |  | 2025.04 |
| CHI25 | [Sonora: Human-AI Co-Creation of 3D Audio Worlds](https://doi.org/10.1145/3706598.3713316) | Fernanda M De La Torre, et al. | AI, audio, 3D, soundscape, LLM, co-creation |  | Uses LLM for voice commands | 2025.04 |
| CHI25 | [The Voice of Endo: Leveraging Speech for Illness Flare-up Forecasting](https://doi.org/10.1145/3706598.3714040) | Authors TBD, et al. | speech, health, voice, endometriosis, forecasting |  |  | 2025.04 |
| CHI25 | [SPECTRA: Personalizable Sound Recognition for DHH Users through Interactive ML](https://doi.org/10.1145/3706598.3713294) | Steven M. Goodman, et al. | sound recognition, DHH, accessibility, interactive ML |  |  | 2025.04 |
| CHI25 | [LLM Powered Text Entry Decoding and Flexible Typing on Smartphones](https://doi.org/10.1145/3706598.3714314) | Authors TBD, et al. | LLM, text entry, typing, smartphone, gesture |  | 93.1% top-1 accuracy | 2025.04 |
| CHI25 | [Seeing and Touching the Air: Eye-Hand Coordination in Mid-Air Gesture Typing for MR](https://doi.org/10.1145/3706598.3713743) | Authors TBD, et al. | gesture typing, MR, mid-air, eye-hand coordination |  |  | 2025.04 |
| CHI25 | [PropType: Everyday Props as Typing Surfaces in Augmented Reality](https://doi.org/10.1145/3706598.3714056) | Authors TBD, et al. | AR, typing, props, text entry |  |  | 2025.04 |
| CHI25 | [FineType: Fine-grained Tapping Gesture Recognition for Text Entry](https://doi.org/10.1145/3706598.3714278) | Authors TBD, et al. | tapping, gesture, text entry, IMU, wristband |  |  | 2025.04 |
| CHI25 | [Exploring Mobile Touch Interaction with Large Language Models](https://doi.org/10.1145/3706598.3713554) | Authors TBD, et al. | LLM, touch, mobile, gesture, interaction |  |  | 2025.04 |
| CHI25 | [Tap&Say: Touch Location-Informed LLM for Multimodal Text Correction](https://doi.org/10.1145/3706598.3713376) | Authors TBD, et al. | LLM, touch, voice, multimodal, text correction |  |  | 2025.04 |
| CHI25 | [MotionBlocks: Modular Geometric Motion Remapping for Accessible VR](https://doi.org/10.1145/3706598.3713837) | Authors TBD, et al. | VR, accessibility, motion, remapping, limited mobility |  |  | 2025.04 |
| CHI25 | [Your Hands Can Tell: Detecting Redirected Hand Movements in VR](https://doi.org/10.1145/3706598.3713679) | Authors TBD, et al. | VR, hand, redirection, detection |  |  | 2025.04 |
| CHI25 | [Spatial Hand Actions: Hand Actions for Spatial Thinking in 3D Assembling](https://doi.org/10.1145/3706598.3713424) | Authors TBD, et al. | hand, spatial, 3D, assembling, gesture |  |  | 2025.04 |
| CHI25 | [SpellRing: Recognizing Continuous Fingerspelling in ASL using a Ring](https://doi.org/10.1145/3706598.3713721) | Authors TBD, et al. | ring, ASL, sign language, fingerspelling, wearable |  |  | 2025.04 |
| CHI25 | [Effects of Acoustic Transparency of Wearable Audio Devices on Audio AR](https://doi.org/10.1145/3706598.3713907) | Yuki Watanabe, et al. | audio AR, wearable, acoustic transparency, hearables |  |  | 2025.04 |
| CHI25 | [Designing Accessible Audio Nudges for Voice Interfaces](https://doi.org/10.1145/3706598.3713563) | Hira Jamshed, et al. | voice interface, audio, nudging, older adults, accessibility |  |  | 2025.04 |
| CHI25 | [Weaving Sound Information to Support Real-Time Sensemaking for DHH Users](https://doi.org/10.1145/3706598.3714268) | Jeremy Zhengqi Huang, et al. | sound, DHH, accessibility, AI, sensemaking |  |  | 2025.04 |
<!-- TABLE_END: HCI -->

# LLM
<!-- TABLE_START: LLM -->
| Source | Title (Link) | Authors | Tag | Subjects | Additional info | Date |
|---|---|---|---|---|---|---|
| arXiv(v1) 2023 | [Multimodal Foundation Models: From Specialists to General-Purpose Assistants](https://arxiv.org/abs/2309.10020) | Chunyuan Li, et al. | survey | cs.CV, cs.CL |  | 2023.09 |
| arXiv(v1) (NIPS23) | [Large Language Model as Attributed Training Data Generator: A Tale of Diversity and Bias](https://arxiv.org/abs/2306.15895) | Yue Yu, et al. | synthetic data generation | cs.CL, cs.AI, cs.LG |  | arXiv(v2) 2023.10 |
| arXiv(v1) 2024 | [Design2Code: How Far Are We From Automating Front-End Engineering?](https://arxiv.org/abs/2403.03163) | Chenglei Si, et al. | llm, auto, google | cs.CL, cs.CV, cs.CY |  | 2024.03 |
| arXiv(v2) 2023 | [The Good, The Bad, and Why: Unveiling Emotions in Generative AI](https://arxiv.org/abs/2312.11111) | Cheng Li, et al. | emotion, prompt, attack, decode | cs.AI, cs.CL, cs.HC | extension of Large language models understand and can be enhanced by emotional stimuli | 2023.12 |
| arXiv(v1) 2024 | [Are You Being Tracked? Discover the Power of Zero-Shot Trajectory Tracing with LLMs!](https://arxiv.org/abs/2403.06201) | Huanqi Yang, et al. | iot, imu, cot, prompt | cs.CL, cs.AI, cs.HC, cs.LG |  | 2024.03 |
| arXiv(v1) 2024 | [Ferret-UI: Grounded Mobile UI Understanding with Multimodal LLMs](https://arxiv.org/abs/2404.05719) | Keen You, et al. | ui, mllm, benchmark, any-resolution | cs.CV, cs.CL, cs.HC |  | 2024.04 |
| arXiv(v7) 2023 | [Attention Is All You Need](http://arxiv.org/abs/1706.03762v7) | Ashish Vaswani, et al. | arxiv | cs.CL, cs.LG | 15 pages, 5 figures | 2023.08 |
| arXiv(v3) 2025 | [Beyond 2:4: exploring V:N:M sparsity for efficient transformer inference on GPUs](http://arxiv.org/abs/2410.16135v3) | Kang Zhao, et al. | LLM, GUI agent, interface | cs.LG, cs.AI |  | 2025.06 |
| arXiv(v3) 2025 | [Lai Loss: A Novel Loss for Gradient Control](http://arxiv.org/abs/2405.07884v3) | YuFei Lai, et al. | LLM, agent, interface, UI | cs.LG | The experiment in this article is not very rigorous and may require further testing for its effectiveness | 2025.05 |
| arXiv(v2) 2024 | [Massively parallel CMA-ES with increasing population](http://arxiv.org/abs/2409.11765v2) | David Redon, et al. | LLM, agent, HCI, user interface | cs.DC |  | 2024.10 |
| arXiv(v1) 2024 | [In-Band Full-Duplex MIMO Systems for Simultaneous Communications and Sensing: Challenges, Methods, and Future Perspectives](http://arxiv.org/abs/2410.06512v1) | Besma Smida, et al. | LLM, GUI agent, computer use | cs.IT, cs.ET, eess.SP | 12 pages, 5 figures, White Paper to appear at IEEE SPM | 2024.10 |
| arXiv(v1) 2024 | [OrientedFormer: An End-to-End Transformer-Based Oriented Object Detector in Remote Sensing Images](http://arxiv.org/abs/2409.19648v1) | Jiaqi Zhao, et al. | LLM, agent, GUI, interface | cs.CV | The paper is accepted by IEEE Transactions on Geoscience and Remote Sensing (TGRS) | 2024.09 |
| arXiv(v3) 2025 | [SignLLM: Sign Language Production Large Language Models](http://arxiv.org/abs/2405.10718v3) | Sen Fang, et al. | LLM, agent, user interface, HCI, interaction | cs.CV, cs.CL | website at https://signllm.github.io/ | 2025.04 |
| arXiv(v6) 2025 | [LLaVA-CoT: Let Vision Language Models Reason Step-by-Step](http://arxiv.org/abs/2411.10440v6) | Guowei Xu, et al. | LLM, GUI agent, survey, computer use | cs.CV | 17 pages, ICCV 2025 | 2025.07 |
| arXiv(v1) 2024 | [A Scalable Communication Protocol for Networks of Large Language Models](http://arxiv.org/abs/2410.11905v1) | Samuele Marro, et al. | LLM, agent, GUI, computer use, interface | cs.AI, cs.LG |  | 2024.10 |
| arXiv(v1) 2024 | [ShowUI: One Vision-Language-Action Model for GUI Visual Agent](http://arxiv.org/abs/2411.17465v1) | Kevin Qinghong Lin, et al. | LLM, UI, vision-language, GUI | cs.CV, cs.AI, cs.CL, cs.HC | Technical Report. Github: https://github.com/showlab/ShowUI | 2024.11 |
| arXiv(v1) 2024 | [OS-ATLAS: A Foundation Action Model for Generalist GUI Agents](http://arxiv.org/abs/2410.23218v1) | Zhiyong Wu, et al. | LLM, agent, computer use, GUI, foundation model | cs.CL, cs.CV, cs.HC |  | 2024.10 |
| arXiv(v1) 2024 | [Unlocking the Power of Environment Assumptions for Unit Proofs](http://arxiv.org/abs/2409.12269v1) | Siddharth Priya, et al. | LLM, GUI, agent, survey | cs.SE, cs.PL | SEFM 2024 | 2024.09 |
| arXiv(v1) 2025 (WACV 2026) | [AFRAgent: An Adaptive Feature Renormalization Based High Resolution Aware GUI agent](http://arxiv.org/abs/2512.00846v1) | Neeraj Anand, et al. | GUI agent, VLM, smartphone automation, multimodal | cs.CV | WACV 2026 | 2025.12 |
| arXiv(v2) 2024 (ACL 2025) | [GUICourse: From General Vision Language Models to Versatile GUI Agents](http://arxiv.org/abs/2406.11317v2) | Wentong Chen, et al. | GUI agent, VLM, training data, OCR, grounding | cs.CV, cs.CL, cs.HC | ACL 2025 | 2024.06 |
| arXiv(v2) 2025 | [Mobile-Agent-v3: Fundamental Agents for GUI Automation](http://arxiv.org/abs/2508.15144v2) | Junyang Wang, et al. | GUI agent, mobile, smartphone automation, VLM | cs.CV, cs.AI |  | 2025.08 |
| arXiv(v1) 2026 | [GUI-Eyes: Tool-Augmented Perception for Visual Grounding in GUI Agents](http://arxiv.org/abs/2601.09770v1) | Shuofei Qiao, et al. | GUI agent, visual grounding, tool use, perception | cs.CV, cs.AI |  | 2026.01 |
<!-- TABLE_END: LLM -->

# RAG
<!-- TABLE_START: RAG -->
| Source | Title (Link) | Authors | Tag | Subjects | Additional info | Date |
|---|---|---|---|---|---|---|
| arXiv(v6) 2024 | [Health-LLM: Personalized Retrieval-Augmented Disease Prediction System](https://arxiv.org/abs/2402.00746) | Qinkai Yu, et al. | RAG, XGBoost, AutoML | cs.CL |  | 2024.03 |
| arXiv(v1) 2024 | CRUD-RAG: A Comprehensive Chinese Benchmark for Retrieval-Augmented Generation of Large Language Models |  | retrieval-augmented generation, large language models, evaluation |  |  | 2024.02 |
| arXiv(v1) 2024 | LLM-Augmented Retrieval: Enhancing Retrieval Models Through Language Models and Doc-Level Embedding |  | relevant query, doc-Level embedding, embedding-based retrieval, dense retrieval |  |  | 2024.04 |
| arXiv(v1) 2025 | [Ask in Any Modality: A Comprehensive Survey on Multimodal Retrieval-Augmented Generation](http://arxiv.org/abs/2502.08826v1) | Zihan Wang, et al. | multimodal, RAG, retrieval, survey, LLM | cs.CL, cs.IR |  | 2025.02 |
| arXiv(v1) 2025 | [A Survey of Multimodal Retrieval-Augmented Generation](http://arxiv.org/abs/2504.08748v1) | Zihan Zhao, et al. | multimodal, RAG, retrieval, survey, vision-language | cs.CV, cs.CL |  | 2025.04 |
| arXiv(v1) 2025 | [A Systematic Review of Key RAG Systems: Progress, Gaps, and Future Directions](http://arxiv.org/abs/2507.18910v1) | Authors TBD, et al. | RAG, survey, systematic review, knowledge base | cs.CL, cs.IR |  | 2025.07 |
| arXiv(v1) 2025 | [RAG Survey: Architectures, Enhancements, and Robustness Frontiers](http://arxiv.org/abs/2506.00054v1) | Authors TBD, et al. | RAG, survey, architecture, robustness | cs.CL, cs.IR |  | 2025.06 |
| arXiv(v1) 2025 | [RAG Evaluation in the Era of LLMs: A Comprehensive Survey](http://arxiv.org/abs/2504.14891v1) | Authors TBD, et al. | RAG, evaluation, benchmark, LLM | cs.CL, cs.IR |  | 2025.04 |
| arXiv(v1) 2025 | [HiRAG: Retrieval-Augmented Generation with Hierarchical Knowledge](http://arxiv.org/abs/2503.10150v1) | Authors TBD, et al. | RAG, hierarchical, knowledge, indexing | cs.CL, cs.IR |  | 2025.03 |
| arXiv(v1) 2025 | [RAGLens: Toward Faithful RAG with Sparse Autoencoders](http://arxiv.org/abs/2512.08892v1) | Authors TBD, et al. | RAG, hallucination, faithfulness, detection | cs.CL |  | 2025.12 |
| arXiv(v1) 2025 | [Agentic RAG for Fintech: Design and Evaluation](http://arxiv.org/abs/2510.25518v1) | Authors TBD, et al. | RAG, agentic, fintech, query reformulation | cs.CL, cs.IR |  | 2025.10 |
| arXiv(v1) 2025 | [Agentic RAG: A Survey](http://arxiv.org/abs/2501.09136v1) | Authors TBD, et al. | RAG, agentic, survey, LLM agent | cs.CL, cs.IR |  | 2025.01 |
| arXiv(v1) 2025 | [CG-RAG: Citation Graph RAG for Research Question Answering](http://arxiv.org/abs/2501.15067v1) | Authors TBD, et al. | RAG, citation graph, research QA | cs.CL, cs.IR |  | 2025.01 |
| arXiv(v1) 2025 | [Vendi-RAG: Adaptively Trading Off Diversity and Quality in RAG](http://arxiv.org/abs/2502.11228v1) | Authors TBD, et al. | RAG, diversity, quality, adaptive | cs.CL, cs.IR |  | 2025.02 |
| arXiv(v1) 2025 | [GFM-RAG: Graph Foundation Model for Retrieval Augmented Generation](http://arxiv.org/abs/2502.01113v1) | Authors TBD, et al. | RAG, graph, foundation model, knowledge graph | cs.CL, cs.IR | 8M params, 60 KGs, 14M triples | 2025.02 |
| arXiv(v1) 2025 | [KG2RAG: Knowledge Graph-Guided Retrieval Augmented Generation](http://arxiv.org/abs/2502.06864v1) | Authors TBD, et al. | RAG, knowledge graph, retrieval, fact-level | cs.CL, cs.IR |  | 2025.02 |
| arXiv(v1) 2025 | [GraphRAG-Bench: When to Use Graphs in RAG](http://arxiv.org/abs/2506.05690v1) | Authors TBD, et al. | RAG, graph, benchmark, evaluation | cs.CL, cs.IR |  | 2025.06 |
| arXiv(v1) 2025 | [Late Chunking: Contextual Chunk Embeddings for RAG](http://arxiv.org/abs/2409.04701v3) | Authors TBD, et al. | RAG, chunking, embedding, contextual | cs.CL, cs.IR | Updated July 2025 | 2025.07 |
| arXiv(v1) 2025 | [Rethinking Chunk Size for Long-Document Retrieval: Multi-Dataset Analysis](http://arxiv.org/abs/2505.21700v2) | Authors TBD, et al. | RAG, chunking, chunk size, retrieval | cs.CL, cs.IR | 64-1024 tokens optimal | 2025.05 |
| arXiv(v1) 2025 | [CDTA: Cross-Document Topic-Aligned Chunking for RAG](http://arxiv.org/abs/2601.05265v1) | Authors TBD, et al. | RAG, chunking, cross-document, topic alignment | cs.CL, cs.IR | 0.93 faithfulness on HotpotQA | 2025.11 |
| arXiv(v1) 2026 | [L-RAG: Balancing Context and Retrieval with Entropy-Based Lazy Loading](http://arxiv.org/abs/2601.06551v1) | Authors TBD, et al. | RAG, lazy loading, entropy, context | cs.CL, cs.IR |  | 2026.01 |
| arXiv(v1) 2025 | [Practical Code RAG at Scale: Task-Aware Retrieval Design](http://arxiv.org/abs/2510.20609v1) | Authors TBD, et al. | RAG, code, retrieval, hybrid, dense | cs.CL, cs.IR | BM25 + dense hybrid | 2025.10 |
| arXiv(v1) 2025 | [ChunkRAG: Novel Context-Aware Chunking for RAG Systems](http://arxiv.org/abs/2501.00045v1) | Authors TBD, et al. | RAG, chunking, context-aware, retrieval | cs.CL, cs.IR |  | 2025.01 |
| arXiv(v1) 2025 | [RAG-Fusion: Query Expansion and Multi-Source Retrieval](http://arxiv.org/abs/2502.08541v1) | Authors TBD, et al. | RAG, query expansion, multi-source, fusion | cs.CL, cs.IR |  | 2025.02 |
<!-- TABLE_END: RAG -->

# Agent
<!-- TABLE_START: Agent -->
| Source | Title (Link) | Authors | Tag | Subjects | Additional info | Date |
|---|---|---|---|---|---|---|
| arXiv(v1) (ICLR24) | [MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework](https://arxiv.org/abs/2308.00352) | Sirui Hong, et al. | autonomous system, SOP, multi-agent, framework | cs.AI, cs.MA |  |  |
| arXiv(v1) 2024 | [DataDreamer: A Tool for Synthetic Data Generation and Reproducible LLM Workflows](https://arxiv.org/abs/2402.10379) | Ajay Patel, et al. | pipeline, liarbry, generation | cs.CL, cs.LG |  | 2024.02 |
| arXiv(v2) 2023 | [MusicAgent: An AI Agent for Music Understanding and Generation with Large Language Models](https://arxiv.org/abs/2310.11954) | Dingyao Yu, et al. | pipeline | cs.CL, cs.MM, eess.AS |  | 2023.10 |
| arXiv(v3) 2023 | [The Rise and Potential of Large Language Model Based Agents: A Survey](https://arxiv.org/abs/2309.07864) | Zhiheng Xi, et al. | survey, [github paper list](https://github.com/WooooDyy/LLM-Agent-Paper-List) | cs.AI, cs.CL |  | 2023.09 |
| arXiv(v1) (NIPS23) | [CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society](https://arxiv.org/abs/2303.17760) | Guohao Li, et al. | role play, autonomous, user&assistant | cs.AI, cs.CL, cs.CY, cs.LG, cs.MA |  | 2023.11(v2) |
| arXiv(v1) (NIPS23) | [HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face](https://arxiv.org/abs/2303.17580) | Yongliang Shen, et al. | hugging face, API | cs.CL, cs.AI, cs.CV, cs.LG |  | 2023.12 |
| arXiv(v2) 2023 | [VOYAGER: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) | Guanzhi Wang, et al. | multi, autonomous, microcraft, game | cs.AI, cs.LG |  | 2023.10 |
| arXiv(v1) 2024 | [More Agents Is All You Need](https://arxiv.org/abs/2402.05120) | Junyou Li, et al. | multi agent, vote, task | cs.CL, cs.AI, cs.LG |  | 2024.02 |
| arXiv(v3) 2023 | [A Survey on Large Language Model based Autonomous Agents](https://arxiv.org/abs/2308.11432) | Lei Wang, et al. | survey, autonomous | cs.AI, cs.CL | Latest version is v4(2024.03), double columns. But v3(2023.09) single columns is easy to read. |  |
| arXiv(v2) 2024 | [Feasibility Consistent Representation Learning for Safe Reinforcement Learning](http://arxiv.org/abs/2405.11718v2) | Zhepeng Cen, et al. | LLM, agent, UI, LAUI, interface | cs.LG | ICML 2024 | 2024.06 |
| arXiv(v1) 2024 | [Simultaneous identification of the parameters in the plasticity function for power hardening materials : A Bayesian approach](http://arxiv.org/abs/2412.05241v1) | Salih Tatar, et al. | LLM, agent, computer use, evaluation | math.NA, math.AP |  | 2024.12 |
| arXiv(v1) 2025 | [Understanding Tool-Integrated Reasoning](http://arxiv.org/abs/2508.19201v1) | Heng Lin, et al. | LLM, agent, tool use, reasoning, TIR | cs.LG, cs.AI, stat.ML |  | 2025.08 |
| arXiv(v2) 2025 | [Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools](http://arxiv.org/abs/2502.04644v2) | Junde Wu, et al. | LLM, agent, agentic reasoning, tool use, framework | cs.AI, cs.CL | ACL 2025 | 2025.07 |
| arXiv(v1) 2025 | [From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review](http://arxiv.org/abs/2504.19678v1) | Mohamed Amine Ferrag, et al. | LLM, agent, survey, autonomous, comprehensive review | cs.AI, cs.LG |  | 2025.04 |
| arXiv(v1) 2025 | [ReMA: Unlocking the Power of Multi-Agent LLM for Reasoning: From Lazy Agents to Deliberation](http://arxiv.org/abs/2511.02303v1) | Zhiwei Zhang, et al. | multi-agent, LLM, reasoning, lazy agent, deliberation | cs.AI, cs.CL |  | 2025.11 |
| arXiv(v1) 2025 | [MAR: Multi-Agent Reflexion Improves Reasoning Abilities in LLMs](http://arxiv.org/abs/2512.20845v1) | Xinyuan Lu, et al. | multi-agent, LLM, reflexion, reasoning, debate | cs.CL, cs.AI |  | 2025.12 |
| arXiv(v1) 2025 | [LongVideoAgent: Multi-Agent Reasoning with Long Videos](http://arxiv.org/abs/2512.20618v1) | Jingyi Zhang, et al. | multi-agent, video understanding, LLM, reasoning | cs.CV, cs.AI |  | 2025.12 |
| arXiv(v1) 2025 | [LLM-based Agentic Reasoning Frameworks: A Survey from Methods to Scenarios](http://arxiv.org/abs/2508.17692v1) | Bingxi Zhao, et al. | LLM, agent, reasoning, survey, framework | cs.AI, cs.CL |  | 2025.08 |
| arXiv(v4) 2025 | [Towards Embodied Agentic AI: Review and Classification of LLM- and VLM-Driven Robot Autonomy and Interaction](http://arxiv.org/abs/2508.05294v4) | Harshitha Manoj, et al. | embodied AI, robot, LLM, VLM, autonomy, survey | cs.RO, cs.AI |  | 2025.08 |
| arXiv(v3) 2025 | [Embodied AI Agents: Modeling the World](http://arxiv.org/abs/2506.22355v3) | Pascale Fung, et al. | embodied AI, world model, VLM, robot, avatar | cs.AI | Meta AI | 2025.07 |
| arXiv(v1) 2025 | [Agent0: Self-Evolving Agents from Zero Data via Tool-Integrated Reasoning](http://arxiv.org/abs/2511.16043v1) | Authors TBD, et al. | LLM agent, self-evolving, tool use, reasoning | cs.AI, cs.CL | 18% improvement on math, 24% on general | 2025.11 |
| arXiv(v1) 2025 | [Toward a Theory of Agents as Tool-Use Decision-Makers](http://arxiv.org/abs/2506.00886v1) | Authors TBD, et al. | LLM agent, tool use, theory, decision making | cs.AI, cs.CL |  | 2025.06 |
| arXiv(v1) 2025 | [Beyond Task Completion: Assessment Framework for Agentic AI Systems](http://arxiv.org/abs/2512.12791v1) | Authors TBD, et al. | LLM agent, evaluation, framework, benchmark | cs.AI, cs.CL |  | 2025.12 |
| arXiv(v1) 2025 | [Routine: A Structural Planning Framework for LLM Agent System in Enterprise](http://arxiv.org/abs/2507.14447v1) | Authors TBD, et al. | LLM agent, planning, enterprise, framework | cs.AI, cs.CL |  | 2025.07 |
| arXiv(v1) 2025 | [Architecting Resilient LLM Agents](http://arxiv.org/abs/2509.08646v1) | Authors TBD, et al. | LLM agent, resilience, architecture | cs.AI, cs.CL |  | 2025.09 |
| arXiv(v1) 2025 | [A Survey on Code Generation with LLM-based Agents](http://arxiv.org/abs/2508.00083v1) | Authors TBD, et al. | code agent, LLM, code generation, survey | cs.SE, cs.AI |  | 2025.08 |
| arXiv(v1) 2025 | [DeepCode: Open Agentic Coding](http://arxiv.org/abs/2512.07921v1) | Authors TBD, et al. | code agent, agentic coding, open source | cs.SE, cs.AI |  | 2025.12 |
| arXiv(v1) 2026 | [LLM-Based Agentic Systems for Software Engineering: Challenges and Opportunities](http://arxiv.org/abs/2601.09822v1) | Authors TBD, et al. | code agent, software engineering, survey | cs.SE, cs.AI |  | 2026.01 |
| arXiv(v1) 2025 | [SWE-RL: Training Superintelligent Software Agents through Self-Play](http://arxiv.org/abs/2512.18552v1) | Authors TBD, et al. | code agent, self-play, RL, software engineering | cs.SE, cs.LG |  | 2025.12 |
| arXiv(v1) 2025 | [BrowserAgent: Web Agents with Human-Inspired Browsing Actions](http://arxiv.org/abs/2510.10666v1) | Authors TBD, et al. | agent, browser, web, automation | cs.AI, cs.CL |  | 2025.10 |
| arXiv(v1) 2025 | [Building Browser Agents: Architecture, Security, and Practical Solutions](http://arxiv.org/abs/2511.19477v1) | Authors TBD, et al. | agent, browser, security, architecture | cs.AI, cs.CL |  | 2025.11 |
| arXiv(v1) 2026 | [InfiniteWeb: Scalable Web Environment Synthesis for GUI Agent Training](http://arxiv.org/abs/2601.04126v1) | Authors TBD, et al. | agent, web, GUI, training, environment | cs.CV, cs.AI | 600 tasks across websites | 2026.01 |
| arXiv(v1) 2025 | [AgentRewardBench: Benchmark for LLM Judges in Web Agent Evaluation](http://arxiv.org/abs/2504.12721v1) | Authors TBD, et al. | agent, benchmark, web, evaluation, reward | cs.AI, cs.CL | 1,302 trajectories | 2025.04 |
| arXiv(v1) 2025 | [WebRL: Training LLM Web Agents via Self-Evolving Curriculum RL](http://arxiv.org/abs/2505.11451v1) | Authors TBD, et al. | agent, web, RL, curriculum, self-evolving | cs.LG, cs.AI |  | 2025.05 |
| arXiv(v1) 2025 | [Dark Patterns Impact on LLM-Based Web Agents](http://arxiv.org/abs/2510.18113v1) | Authors TBD, et al. | agent, web, dark patterns, decision making | cs.HC, cs.AI |  | 2025.10 |
| arXiv(v1) 2025 | [MCP-Bench: Benchmarking Tool-Using LLM Agents](http://arxiv.org/abs/2508.20453v1) | Authors TBD, et al. | agent, benchmark, tool use, MCP | cs.AI, cs.CL |  | 2025.08 |
<!-- TABLE_END: Agent -->

# Poster





# Todo
- [x] 1.Choose a record format (text or table), text is given priority. Tables can use GPT4o to generate the corresponding markdown format. 
- [x] 2.Choose which fields are required  (title(including link), publication&year, date,version(v1), code, tags, etc.). Here are the examples. Subsequent dynamic adjustments can be made at any time.
  - **(Current Version) [publication&version year] title(link) [tags,xxx,xxx,et al.] [date (format:year.month)]**
  - Title(Star)Venue Date Code Demo
  - DatekeywordsInstitutePaperPublication
  - Example (TPAMI 2023) Multimodal Image Synthesis and Editing: A Survey and Taxonomy [v1(arXiv)](2021.12) ... [v5](2023.08)
  - Towards Tracing Factual Knowledge in Language Models Back to the Training Data. [pdf] [EMNLP 2022] [2022.5]
- [x] 3.Record related projects (Github, tutorials, official documentation, individual developers) in the project.md file.
- [x] 4.Change to Table.
- [x] 5.Find a way to edit markdown table. (Solved by creating a script to automatically generate tables from papers.csv) 
- [x] 6.Automate arXiv paper entry by fetching metadata (authors, subjects, etc.) from the arXiv API.
- [x] 7.Refine table display format (e.g., author list, column visibility) for better readability.
- [x] 8.Smart Source column format - prioritize arXiv version information (`arXiv(v1) 2024 (ICLR 2024)`).

# Agentic-RL
<!-- TABLE_START: Agentic-RL -->
| Source | Title (Link) | Authors | Tag | Subjects | Additional info | Date |
|---|---|---|---|---|---|---|
| arXiv(v1) 2025 | [AGENTRL: Scaling Agentic Reinforcement Learning](http://arxiv.org/abs/2510.04206v1) | Authors TBD, et al. | agentic RL, RLHF, LLM agent, scaling | cs.LG, cs.AI | Outperforms GPT-5 and Claude-Sonnet-4 | 2025.10 |
| arXiv(v1) 2025 | [The Landscape of Agentic Reinforcement Learning for LLMs: A Survey](http://arxiv.org/abs/2509.02547v1) | Authors TBD, et al. | agentic RL, survey, LLM, POMDP | cs.LG, cs.AI |  | 2025.09 |
| arXiv(v1) 2025 | [iStar: Agentic Reinforcement Learning with Implicit Step Rewards](http://arxiv.org/abs/2509.19199v1) | Authors TBD, et al. | agentic RL, credit assignment, implicit PRM | cs.LG, cs.AI |  | 2025.09 |
| arXiv(v1) 2025 | [Process Reward Models for LLM Agents: Practical Framework](http://arxiv.org/abs/2502.10325v1) | Authors TBD, et al. | PRM, reward model, LLM agent, RLHF | cs.LG, cs.AI | InversePRM | 2025.02 |
| arXiv(v1) 2025 | [Enhancing Agentic RL with Progressive Reward Shaping and VSPO](http://arxiv.org/abs/2512.07478v1) | Authors TBD, et al. | agentic RL, reward shaping, GRPO, tool use | cs.LG, cs.AI |  | 2025.12 |
| arXiv(v1) 2025 | [Reward Hacking Mitigation using Verifiable Composite Rewards](http://arxiv.org/abs/2509.15557v1) | Authors TBD, et al. | RLHF, reward hacking, RLVR, verification | cs.LG, cs.AI |  | 2025.09 |
| arXiv(v1) 2025 | [Provably Efficient Online RLHF with One-Pass Reward Modeling](http://arxiv.org/abs/2502.07193v1) | Authors TBD, et al. | online RLHF, reward modeling, efficiency | cs.LG, cs.AI |  | 2025.02 |
| arXiv(v1) 2025 | [DPO Meets PPO: Reinforced Token Optimization for RLHF](http://arxiv.org/abs/2404.18922v1) | Han Zhong, et al. | agentic RL, DPO, PPO, RLHF, token-level | cs.LG, cs.AI | RTO framework | 2025.04 |
| arXiv(v1) 2025 | [REINFORCE++: Critic-Free Policy Optimization with Global Advantage Normalization](http://arxiv.org/abs/2501.03262v1) | Authors TBD, et al. | agentic RL, REINFORCE, critic-free, GRPO | cs.LG, cs.AI | Outperforms PPO | 2025.01 |
| arXiv(v1) 2025 | [OPPO: Accelerating PPO-based RLHF via Pipeline Overlap](http://arxiv.org/abs/2509.25762v1) | Authors TBD, et al. | agentic RL, PPO, RLHF, efficiency, overlap | cs.LG, cs.AI |  | 2025.09 |
| arXiv(v1) 2025 | [Technical Survey of RL Techniques for Large Language Models](http://arxiv.org/abs/2507.04136v1) | Authors TBD, et al. | agentic RL, survey, PPO, DPO, GRPO | cs.LG, cs.AI |  | 2025.07 |
| arXiv(v1) 2025 | [RL Foundations for Deep Research Systems: A Survey](http://arxiv.org/abs/2509.06733v1) | Authors TBD, et al. | agentic RL, deep research, survey, post-DeepSeek | cs.LG, cs.AI | Post Feb 2025 papers | 2025.09 |
| arXiv(v1) 2025 | [PRL: Process Reward Learning Improves LLM Reasoning](http://arxiv.org/abs/2601.10201v1) | Authors TBD, et al. | agentic RL, PRM, process reward, reasoning | cs.LG, cs.AI |  | 2026.01 |
| arXiv(v1) 2025 | [Hierarchical Multi-Step Reward Models for Enhanced Reasoning](http://arxiv.org/abs/2503.13551v1) | Authors TBD, et al. | agentic RL, reward model, hierarchical, reasoning | cs.LG, cs.AI |  | 2025.03 |
| arXiv(v1) 2025 | [Comprehensive Survey of Reward Models: Taxonomy and Applications](http://arxiv.org/abs/2504.12328v1) | Authors TBD, et al. | agentic RL, reward model, survey, taxonomy | cs.LG, cs.AI |  | 2025.04 |
| arXiv(v1) 2025 | [RLSR: Reinforcement Learning with Supervised Reward](http://arxiv.org/abs/2510.14200v1) | Authors TBD, et al. | agentic RL, supervised reward, instruction following | cs.LG, cs.AI |  | 2025.10 |
| arXiv(v1) 2025 | [On Designing Effective RL Reward at Training Time for LLM Reasoning](http://arxiv.org/abs/2410.15115v1) | Authors TBD, et al. | agentic RL, reward design, reasoning, training | cs.LG, cs.AI |  | 2025.10 |
| arXiv(v1) 2025 | [Sailing by the Stars: Survey on Reward Models and Learning Strategies](http://arxiv.org/abs/2505.02686v2) | Authors TBD, et al. | agentic RL, reward model, survey, learning | cs.LG, cs.AI |  | 2025.06 |
<!-- TABLE_END: Agentic-RL -->

# MLLM
<!-- TABLE_START: MLLM -->
| Source | Title (Link) | Authors | Tag | Subjects | Additional info | Date |
|---|---|---|---|---|---|---|
| arXiv(v1) 2025 | [VIRAL: Visual Representation Alignment for MLLMs](http://arxiv.org/abs/2509.07979v1) | Authors TBD, et al. | MLLM, visual alignment, fine-grained understanding | cs.CV, cs.CL |  | 2025.09 |
| arXiv(v1) 2025 | [VLM-R1: A Stable and Generalizable R1-Style Large VLM](http://arxiv.org/abs/2504.07615v1) | Authors TBD, et al. | MLLM, VLM, reasoning, R1-style | cs.CV, cs.CL |  | 2025.04 |
| arXiv(v1) 2025 | [Vision-R1: Incentivizing Reasoning Capability in MLLMs](http://arxiv.org/abs/2503.06749v1) | Authors TBD, et al. | MLLM, reasoning, visual reasoning | cs.CV, cs.CL |  | 2025.03 |
| arXiv(v1) 2025 | [R1-Zero's Aha Moment in Visual Reasoning on a 2B Non-SFT Model](http://arxiv.org/abs/2503.05132v1) | Authors TBD, et al. | MLLM, visual reasoning, R1-Zero, emergent | cs.CV, cs.CL |  | 2025.03 |
| arXiv(v1) 2025 | [Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey](http://arxiv.org/abs/2508.13073v1) | Authors TBD, et al. | MLLM, VLA, robotics, manipulation, survey | cs.RO, cs.CV |  | 2025.08 |
| arXiv(v1) 2025 | [Visual Perception Token for Multimodal Large Language Models](http://arxiv.org/abs/2502.17425v1) | Authors TBD, et al. | MLLM, visual perception, token, autonomous control | cs.CV, cs.CL | 829k training samples | 2025.02 |
| arXiv(v1) 2025 | [Manager: Aggregating Insights from Unimodal Experts in VLMs and MLLMs](http://arxiv.org/abs/2506.11515v1) | Authors TBD, et al. | MLLM, VLM, unimodal experts, fusion | cs.CV, cs.CL |  | 2025.06 |
| arXiv(v1) 2025 | [Insight-V: Exploring Long-Chain Visual Reasoning with MLLMs](https://openaccess.thecvf.com/CVPR2025) | Authors TBD, et al. | MLLM, visual reasoning, long-chain, CVPR | cs.CV | CVPR 2025 | 2025.06 |
| arXiv(v1) 2025 | [MT-Video-Bench: Video Understanding Benchmark for MLLMs in Multi-Turn Dialogues](http://arxiv.org/abs/2510.17722v1) | Authors TBD, et al. | MLLM, video understanding, benchmark, multi-turn | cs.CV, cs.CL |  | 2025.10 |
| arXiv(v1) 2025 | [MVU-Eval: Multi-Video Understanding Evaluation for MLLMs](http://arxiv.org/abs/2511.07250v1) | Authors TBD, et al. | MLLM, multi-video, evaluation, benchmark | cs.CV, cs.CL |  | 2025.11 |
| arXiv(v1) 2025 | [VideoLLM Benchmarks and Evaluation: A Survey](http://arxiv.org/abs/2505.03829v1) | Authors TBD, et al. | MLLM, video, benchmark, evaluation, survey | cs.CV, cs.CL |  | 2025.05 |
| arXiv(v1) 2025 | [MM-Spatial: Exploring 3D Spatial Understanding in Multimodal LLMs](http://arxiv.org/abs/2503.13111v1) | Erik Daxberger, et al. | MLLM, 3D, spatial, understanding, benchmark | cs.CV, cs.CL | ICCV 2025 | 2025.03 |
| arXiv(v1) 2025 | [SpatialThinker: Reinforcing 3D Reasoning in Multimodal LLMs via Spatial Rewards](http://arxiv.org/abs/2511.07403v1) | Authors TBD, et al. | MLLM, 3D reasoning, spatial, RL | cs.CV, cs.CL | Outperforms GPT-4o | 2025.11 |
| arXiv(v1) 2025 | [MLLM-For3D: Adapting Multimodal Large Language Model for 3D Reasoning Segmentation](http://arxiv.org/abs/2503.18135v1) | Authors TBD, et al. | MLLM, 3D, segmentation, reasoning | cs.CV |  | 2025.03 |
| arXiv(v1) 2025 | [SpaceVLLM: Endowing MLLM with Spatio-Temporal Video Grounding](http://arxiv.org/abs/2503.13983v1) | Authors TBD, et al. | MLLM, video, spatio-temporal, grounding | cs.CV, cs.CL |  | 2025.03 |
| arXiv(v1) 2025 | [Mobile-VideoGPT: Fast and Accurate Video Understanding Language Model](http://arxiv.org/abs/2503.21782v1) | Authors TBD, et al. | MLLM, video, mobile, efficient | cs.CV, cs.CL |  | 2025.03 |
| arXiv(v1) 2025 (CVPR 2025) | [LLaVA-ST: Multimodal LLM for Fine-Grained Spatial-Temporal Understanding](https://openaccess.thecvf.com/CVPR2025) | Authors TBD, et al. | MLLM, spatial-temporal, video, CVPR | cs.CV | CVPR 2025 | 2025.06 |
| arXiv(v1) 2025 | [RynnEC: Bringing MLLMs into Embodied World](http://arxiv.org/abs/2508.14160v1) | Authors TBD, et al. | MLLM, embodied, video, spatial reasoning | cs.CV, cs.RO |  | 2025.08 |
| arXiv(v1) 2025 | [From Indoor to Open World: Revealing the Spatial Reasoning Gap in MLLMs](http://arxiv.org/abs/2512.19683v1) | Authors TBD, et al. | MLLM, spatial reasoning, benchmark, open world | cs.CV, cs.CL |  | 2025.12 |
| arXiv(v1) 2025 | [Med3DVLM: An Efficient Vision-Language Model for 3D Medical Image Analysis](http://arxiv.org/abs/2503.20047v1) | Authors TBD, et al. | MLLM, medical, 3D, VLM, CT | cs.CV |  | 2025.03 |
| arXiv(v1) 2025 | [MedBridge: Bridging Foundation Vision-Language Models to Medical Image Diagnosis](http://arxiv.org/abs/2505.21698v1) | Authors TBD, et al. | MLLM, medical, VLM, diagnosis | cs.CV |  | 2025.05 |
| arXiv(v1) 2025 | [Grounding the Ungrounded: Spectral-Graph Framework for Quantifying Hallucinations in MLLMs](http://arxiv.org/abs/2508.19366v1) | Authors TBD, et al. | MLLM, hallucination, grounding, detection | cs.CV, cs.CL |  | 2025.08 |
| arXiv(v1) 2025 | [Two Causes, Not One: Rethinking Omission and Fabrication Hallucinations in MLLMs](http://arxiv.org/abs/2509.00371v1) | Authors TBD, et al. | MLLM, hallucination, omission, fabrication | cs.CV, cs.CL |  | 2025.09 |
| arXiv(v1) 2026 | [Ground What You See: Hallucination-Resistant MLLMs via Caption Feedback](http://arxiv.org/abs/2601.06224v1) | Authors TBD, et al. | MLLM, hallucination, caption feedback, grounding | cs.CV, cs.CL |  | 2026.01 |
| arXiv(v1) 2025 | [Seeing is Believing: Rich-Context Hallucination Detection via Backward Visual Grounding](http://arxiv.org/abs/2511.12140v1) | Authors TBD, et al. | MLLM, hallucination, detection, visual grounding | cs.CV, cs.CL | Outperforms GPT-4o | 2025.11 |
| arXiv(v1) 2025 | [MemVR: Memory-Space Visual Retracing for Hallucination Mitigation in MLLMs](http://arxiv.org/abs/2410.03577v1) | Authors TBD, et al. | MLLM, hallucination, mitigation, memory | cs.CV, cs.CL | Plug-and-play | 2025.10 |
| CVPR25 (CVPR 2025) | [Seeing Far and Clearly: Mitigating Hallucinations in MLLMs with Attention Reweighting](https://openaccess.thecvf.com/CVPR2025) | Authors TBD, et al. | MLLM, hallucination, attention, CVPR | cs.CV | CVPR 2025 | 2025.06 |
<!-- TABLE_END: MLLM -->

# Memory
<!-- TABLE_START: Memory -->
| Source | Title (Link) | Authors | Tag | Subjects | Additional info | Date |
|---|---|---|---|---|---|---|
| arXiv(v1) 2025 | [Memory in the Age of AI Agents](http://arxiv.org/abs/2512.13564v1) | Yuyang Hu, et al. | memory, survey, LLM, agent | cs.CL, cs.AI | Comprehensive survey on agent memory | 2025.12 |
| arXiv(v1) 2024 | [A Survey on the Memory Mechanism of Large Language Model based Agents](http://arxiv.org/abs/2404.13501v1) | Zeyu Zhang, et al. | memory, survey, LLM, agent | cs.AI | ACM TOIS, 39 pages | 2024.04 |
| arXiv(v1) 2025 | [A-MEM: Agentic Memory for LLM Agents](http://arxiv.org/abs/2502.12110v1) | Authors TBD, et al. | memory, agentic, self-organizing, Zettelkasten | cs.AI, cs.CL | Dynamic memory organization | 2025.02 |
| arXiv(v1) 2025 | [MemR3: Memory Retrieval via Reflective Reasoning for LLM Agents](http://arxiv.org/abs/2512.20237v1) | Authors TBD, et al. | memory, retrieval, reflection, reasoning | cs.AI, cs.CL | Router + evidence-gap tracker | 2025.12 |
| arXiv(v1) 2025 | [Hindsight is 20/20: Building Agent Memory that Retains, Recalls, and Reflects](http://arxiv.org/abs/2512.12818v1) | Authors TBD, et al. | memory, hindsight, reflection, retention | cs.AI, cs.CL | Retain-Recall-Reflect framework | 2025.12 |
| arXiv(v1) 2025 | [From Human Memory to AI Memory: A Survey on Memory Mechanisms in the Era of LLMs](http://arxiv.org/abs/2504.15965v1) | Authors TBD, et al. | memory, survey, episodic, semantic, working memory | cs.CL, cs.AI | Personal/system, parametric/non-parametric | 2025.04 |
| arXiv(v1) 2025 | [Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](http://arxiv.org/abs/2504.19413v1) | Authors TBD, et al. | memory, long-term, scalable, production | cs.AI, cs.CL | 26% improvement over OpenAI | 2025.04 |
| arXiv(v1) 2025 | [Memory-R1: Enhancing LLM Agents to Manage and Utilize Memories via RL](http://arxiv.org/abs/2508.19828v1) | Authors TBD, et al. | memory, RL, memory manager, ADD/UPDATE/DELETE | cs.AI, cs.LG | Memory Manager + Answer Agent | 2025.08 |
| arXiv(v1) 2026 | [MemBuilder: Reinforcing LLMs for Long-Term Memory Construction via Attributed Dense Rewards](http://arxiv.org/abs/2601.05488v1) | Authors TBD, et al. | memory, long-term, construction, dense reward | cs.CL, cs.AI |  | 2026.01 |
| arXiv(v1) 2025 | [Position: Episodic Memory is the Missing Piece for Long-Term LLM Agents](http://arxiv.org/abs/2502.06975v1) | Authors TBD, et al. | memory, episodic, long-term, position paper | cs.AI, cs.CL | Encoding and retrieval | 2025.02 |
| arXiv(v1) 2026 | [Beyond Dialogue Time: Temporal Semantic Memory for Personalized LLM Agents](http://arxiv.org/abs/2601.07468v1) | Authors TBD, et al. | memory, temporal, semantic, personalized | cs.CL, cs.AI | Durative memory, Zep architecture | 2026.01 |
| arXiv(v1) 2026 | [Continuum Memory Architectures for Long-Horizon LLM Agents](http://arxiv.org/abs/2601.09913v1) | Authors TBD, et al. | memory, continuum, long-horizon, consolidation | cs.AI, cs.CL | Episodic-to-semantic conversion | 2026.01 |
| IJCAI25 (IJCAI 2025) | [AriGraph: Learning Knowledge Graph World Models with Episodic Memory](https://www.ijcai.org/proceedings/2025/0002) | Authors TBD, et al. | memory, knowledge graph, episodic, world model | cs.AI | IJCAI 2025 | 2025.08 |
| arXiv(v1) 2026 | [Active Context Compression: Autonomous Memory Management in LLM Agents](http://arxiv.org/abs/2601.07190v1) | Authors TBD, et al. | memory, compression, context, autonomous, Focus | cs.CL, cs.AI | 22.7% token savings | 2026.01 |
| arXiv(v1) 2025 | [Acon: Optimizing Context Compression for Long-horizon LLM Agents](http://arxiv.org/abs/2510.00615v1) | Authors TBD, et al. | memory, compression, context, optimization | cs.CL, cs.AI | 26-54% memory reduction | 2025.10 |
| arXiv(v1) 2025 | [Adaptive Focus Memory for Language Models](http://arxiv.org/abs/2511.12712v1) | Authors TBD, et al. | memory, adaptive, focus, compression, AFM | cs.CL, cs.AI | 2/3 token reduction | 2025.11 |
| ACL25 (ACL 2025) | [Pretraining Context Compressor for LLMs with Embedding-Based Memory](https://aclanthology.org/2025.acl-long.1394) | Authors TBD, et al. | memory, compression, embedding, context | cs.CL | PCC framework | 2025.07 |
| arXiv(v1) 2025 | [Memory in LLM-based Multi-agent Systems: Mechanisms, Challenges, and Collective](http://arxiv.org/abs/2509.15234v1) | Authors TBD, et al. | memory, multi-agent, collective, survey | cs.AI, cs.MA |  | 2025.09 |
| arXiv(v1) 2025 | [Enabling Personalized Long-term Interactions in LLM-based Agents through Persistent Memory](http://arxiv.org/abs/2510.07925v1) | Authors TBD, et al. | memory, personalized, long-term, user profile | cs.CL, cs.AI |  | 2025.10 |
<!-- TABLE_END: Memory -->

# Personalization
<!-- TABLE_START: Personalization -->
| Source | Title (Link) | Authors | Tag | Subjects | Additional info | Date |
|---|---|---|---|---|---|---|
| arXiv(v1) 2025 | [Personalization of Large Language Models: A Survey](http://arxiv.org/abs/2411.00027v1) | Zhehao Zhang, et al. | personalization, survey, LLM, user profile | cs.CL, cs.AI | Comprehensive taxonomy | 2025.07 |
| arXiv(v1) 2025 | [A Survey of Personalized Large Language Models: Progress and Future Directions](http://arxiv.org/abs/2502.11528v1) | Authors TBD, et al. | personalization, survey, LLM, prompting, finetuning | cs.CL, cs.AI | Input/model/objective level | 2025.02 |
| arXiv(v1) 2025 | [A Survey on Personalized and Pluralistic Preference Alignment in Large Language Models](http://arxiv.org/abs/2504.07070v1) | Authors TBD, et al. | personalization, preference alignment, survey, pluralistic | cs.CL, cs.AI | Training and inference-time methods | 2025.04 |
| arXiv(v1) 2025 | [PersonaMem-v2: Towards Personalized Intelligence via Learning Implicit User Personas](http://arxiv.org/abs/2512.06688v1) | Authors TBD, et al. | personalization, persona, implicit, user modeling | cs.CL, cs.AI | 1000 personas, 20k preferences, 128k context | 2025.12 |
| arXiv(v1) 2025 | [PersonalizedRouter: Personalized LLM Routing via Graph-based User Preference Modeling](http://arxiv.org/abs/2511.16883v1) | Authors TBD, et al. | personalization, routing, GNN, user preference | cs.CL, cs.AI |  | 2025.11 |
| arXiv(v1) 2025 | [PrefEval: Do LLMs Recognize Your Preferences? Evaluating Personalized Preference Following](http://arxiv.org/abs/2502.09597v1) | Authors TBD, et al. | personalization, benchmark, preference, evaluation | cs.CL | 3000 preference-query pairs, 20 topics | 2025.02 |
| arXiv(v1) 2025 | [PLUS: Learning to Summarize User Information for Personalized RLHF](http://arxiv.org/abs/2507.13579v1) | Authors TBD, et al. | personalization, RLHF, user summary, preference | cs.LG, cs.AI | 11-77% reward model improvement | 2025.07 |
| arXiv(v1) 2025 | [Know Me, Respond to Me: Benchmarking LLMs for Dynamic User Profiling](http://arxiv.org/abs/2504.14225v1) | Authors TBD, et al. | personalization, benchmark, user profiling, dynamic | cs.CL, cs.AI |  | 2025.04 |
| arXiv(v1) 2025 | [PersonaX: A Recommendation Agent Oriented User Modeling Framework](http://arxiv.org/abs/2503.02398v1) | Authors TBD, et al. | personalization, recommendation, user modeling, agent | cs.IR, cs.AI | 3-11% improvement on AgentCF | 2025.03 |
| arXiv(v1) (SIGIR25) | [CoT-Rec: Enhancing LLM-Based Recommendations Through Personalized Reasoning](http://arxiv.org/abs/2502.13845v1) | Authors TBD, et al. | personalization, recommendation, CoT, reasoning | cs.IR, cs.AI | SIGIR 2025 | 2025.07 |
| arXiv(v1) 2025 | [MAP: Memory Assisted LLM for Personalized Recommendation System](http://arxiv.org/abs/2505.03824v1) | Authors TBD, et al. | personalization, recommendation, memory, history | cs.IR, cs.AI |  | 2025.05 |
| arXiv(v1) 2025 | [DEP: Latent Inter-User Difference Modeling for LLM Personalization](http://arxiv.org/abs/2507.20849v1) | Authors TBD, et al. | personalization, latent, embedding, difference-aware | cs.CL, cs.AI | Sparse autoencoder | 2025.07 |
| arXiv(v1) 2025 | [PerRecBench: Can LLMs Understand Preferences in Personalized Recommendation?](http://arxiv.org/abs/2501.13391v1) | Authors TBD, et al. | personalization, benchmark, recommendation, preference | cs.IR, cs.CL | 19 LLMs evaluated | 2025.01 |
| arXiv(v1) 2025 | [Agentic Recommender Systems in the Era of Multimodal LLMs: Survey](http://arxiv.org/abs/2503.16734v1) | Authors TBD, et al. | personalization, recommendation, agent, MLLM, survey | cs.IR, cs.AI | User agent simulation | 2025.03 |
| arXiv(v1) 2025 | [PaRT: Enhancing Proactive Social Chatbots with Personalized Real-Time Retrieval](http://arxiv.org/abs/2504.20624v1) | Authors TBD, et al. | personalization, chatbot, retrieval, real-time | cs.CL, cs.AI | 21.77% dialogue improvement, production deployed | 2025.04 |
| arXiv(v1) 2025 | [Steerable Chatbots: Personalizing LLMs with Preference-Based Activation Steering](http://arxiv.org/abs/2505.04260v1) | Authors TBD, et al. | personalization, chatbot, activation steering, inference | cs.CL, cs.AI | Training-free | 2025.05 |
| arXiv(v1) 2025 | [HumAIne-Chatbot: Real-Time Personalized Conversational AI via RL](http://arxiv.org/abs/2509.04303v1) | Authors TBD, et al. | personalization, chatbot, RL, real-time | cs.CL, cs.AI |  | 2025.09 |
| arXiv(v1) 2025 | [GRAVITY: Personalized Text Generation via Profile-Grounded Synthetic Preferences](http://arxiv.org/abs/2510.11952v1) | Authors TBD, et al. | personalization, text generation, profile, synthetic | cs.CL, cs.AI |  | 2025.10 |
| arXiv(v1) 2025 | [Evaluating Style-Personalized Text Generation: Challenges and Directions](http://arxiv.org/abs/2508.06374v1) | Authors TBD, et al. | personalization, style, text generation, evaluation | cs.CL | Write like me | 2025.08 |
| arXiv(v1) 2025 | [ExPerT: Effective and Explainable Evaluation of Personalized Long-Form Text Generation](http://arxiv.org/abs/2501.14956v1) | Authors TBD, et al. | personalization, evaluation, explainable, long-form | cs.CL | 7.2% improvement in human alignment | 2025.01 |
| arXiv(v1) 2025 | [StyleVector: Personalized Text Generation with Contrastive Activation Steering](http://arxiv.org/abs/2503.05213v1) | Authors TBD, et al. | personalization, style, activation steering, training-free | cs.CL, cs.AI | Disentangles content and style | 2025.03 |
| arXiv(v1) 2026 | [Multilingual LLMs Personalized Text Generation: Groups and Social-Media Platforms](http://arxiv.org/abs/2601.03752v1) | Authors TBD, et al. | personalization, multilingual, social media, group | cs.CL | Platform-personalization | 2026.01 |
| arXiv(v1) 2025 | [Position: It's Time to Act on the Risk of Efficient Personalized Text Generation](http://arxiv.org/abs/2502.06560v1) | Authors TBD, et al. | personalization, risk, style imitation, position paper | cs.CL, cs.CY | Safety concerns | 2025.02 |
| arXiv(v1) 2025 | [Catch Me If You Can? LLMs Still Struggle to Imitate Implicit Writing Styles](http://arxiv.org/abs/2509.14543v1) | Authors TBD, et al. | personalization, style, imitation, evaluation | cs.CL | Authorship attribution study | 2025.09 |
| arXiv(v1) 2026 | [ProUtt: LLM-Driven Preference Data Synthesis for Proactive User Utterance Prediction](http://arxiv.org/abs/2601.09713v1) | Authors TBD, et al. | personalization, dialogue, preference, intent tree | cs.CL, cs.AI |  | 2026.01 |
| arXiv(v1) 2025 | [FaST: Feature-aware Sampling and Tuning for Personalized LLM](http://arxiv.org/abs/2508.04698v1) | Authors TBD, et al. | personalization, finetuning, feature-aware, sampling | cs.CL, cs.LG |  | 2025.08 |
<!-- TABLE_END: Personalization -->
