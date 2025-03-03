# awesome-hci-llm-agent-paper (Since 2021)
This repository is dedicated to the exploration of the most recent advancements in Human-Computer Interaction (HCI), Large Language Models (LLM), Multi Large Language Models (MLLM), Agent and Retrieval-Augmented Generation (RAG) among other pertinent fields. The approach is to prioritize the review of the latest research papers, followed by an examination of seminal works in the domain. 

Given the potential for overlap between the domains of LLM and Agent research, a precise categorization of papers into specific areas will, for the moment, be deferred. Instead, the focus will be on the papers' contributions and the tags assigned to them. These tags have been selected to facilitate the indexing of related papers, and while they may appear abundant, they serve the purpose of enhancing navigability. It is acknowledged that the tags currently applied are somewhat broad; there is an intention to refine and reorganize them when possible for more precise indexing and retrieval.

# Todo
- [x] 1.Choose a record format (text or table), text is given priority. Tables can use GPT4o to generate the corresponding markdown format. **Decision:Text!!!**
- [x] 2.Choose which fields are required  (title(including link), publication&year, date,version(v1), code, tags, etc.). Here are the examples. Subsequent dynamic adjustments can be made at any time.
  - **(Current Version) [publication&version year] title(link) [tags,xxx,xxx,et al.] [date (format:year.month)]**
  - Title(Star)	Venue Date Code Demo
  - Date	keywords	Institute	Paper	Publication
  - Example (TPAMI 2023) Multimodal Image Synthesis and Editing: A Survey and Taxonomy [v1(arXiv)](2021.12) ... [v5](2023.08)
  - Towards Tracing Factual Knowledge in Language Models Back to the Training Data. [pdf] [EMNLP 2022] [2022.5]
- [ ] 3.Record related projects (Github, tutorials, official documentation, individual developers) in the project.md file.
- [x] 4.Change to Table.

# HCI

| Source             | Title (Link) | Tag                                                                                                  | Additional info                                                                                                         | Date     |
|--------------------|--------------|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|----------|
| CHI 2023           | [HOOV: Hand Out-Of-View Tracking for Proprioceptive Interaction using Inertial Sensing](https://arxiv.org/abs/2303.07016) | IMU, VR, transformer                                                                               |                                                                                                                         |          |
| Ubicomp 2023       | [From 2D to 3D: Facilitating Single-Finger Mid-Air Typing on QWERTY Keyboards with Probabilistic Touch Modeling](https://dl.acm.org/doi/10.1145/3580829) | mid air, text entry, VR                                                                            |                                                                                                                         |          |
| Ubicomp 2023       | [PrintShear: Shear Input Based on Fingerprint Deformation](https://dl.acm.org/doi/10.1145/3596257) | touch, finger input                                                                                |                                                                                                                         |          |
| CHI 2023           | [IMUPoser: Full-Body Pose Estimation using IMUs in Phones, Watches, and Earbuds](https://arxiv.org/abs/2304.12518) | IMU, pose estimation, BiLSTM                                                                       |                                                                                                                         |          |
| arXiv(v1) 2024      | [IMUSIC: IMU-based Facial Expression Capture](https://arxiv.org/abs/2402.03944) | IMU, generation, simulate, transformer diffusion                                                   | code coming soon ([link](https://sites.google.com/view/projectpage-imusic))                                               | 2024.02  |
| Ubicomp 2023       | [I Know Your Intent: Graph-enhanced Intent-aware User Device Interaction Prediction via Contrastive Learning](https://dl.acm.org/doi/10.1145/3610906) | user device interaction, graph, attention, contrastive learning                                    |                                                                                                                         |          |
| Ubicomp 2023       | [Synthetic Smartwatch IMU Data Generation from In-the-wild ASL Videos](https://dl.acm.org/doi/abs/10.1145/3596261) | IMU, synthetic, ASL recognition                                                                    |                                                                                                                         |          |
| Ubicomp 2023       | [ThumbAir: In-Air Typing for Head Mounted Displays](https://dl.acm.org/doi/10.1145/3569474) | mid air, text entry, VR, HMD, user study                                                           |                                                                                                                         |          |
| Ubicomp 2023       | [TwinkleTwinkle: Interacting with Your Smart Devices by Eye Blink](https://dl.acm.org/doi/abs/10.1145/3596238) | acoustic sensing, eye blink, signal process                                                        |                                                                                                                         |          |
| Ubicomp 2023       | [Voicify Your UI: Towards Android App Control with Voice Commands](https://dl.acm.org/doi/10.1145/3581998) | design, smartphones, sound-based input, dl parser, UI                                              |                                                                                                                         |          |
| Ubicomp 2023       | [LapTouch: Using the Lap for Seated Touch Interaction with HMDs](https://dl.acm.org/doi/10.1145/3610878) | VR, seated, touch, on-body                                                                         |                                                                                                                         |          |
| Ubicomp 2023       | [GLOBEM: Cross-Dataset Generalization of Longitudinal Human Behavior Modeling](https://dl.acm.org/doi/10.1145/3569485) | generalizability, behavior modeling, passive sensing                                               |                                                                                                                         |          |
| Ubicomp 2023       | [StructureSense: Inferring Constructive Assembly Structures from User Behaviors](https://dl.acm.org/doi/10.1145/3570343) | tangible user interfaces, TUI, RFID, user modeling, bayesian inference                               |                                                                                                                         |          |
| Ubicomp 2023       | [Naturalistic E-Scooter Maneuver Recognition with Federated Contrastive Rider Interaction Learning](https://dl.acm.org/doi/10.1145/3570345) | IMU, DCT, contrastive learning, asynchronous federated learning, ehavior analysis                    |                                                                                                                         |          |
| Ubicomp 2023       | [TAO: Context Detection from Daily Activity Patterns Using Temporal Analysis and Ontology](https://dl.acm.org/doi/abs/10.1145/3610896) | behavioral context recognition, activity recognition, ontology, deep learning                        |                                                                                                                         |          |
| Ubicomp 2023       | [HyWay: Enabling Mingling in the Hybrid World∗](https://dl.acm.org/doi/abs/10.1145/3596235) | hybrid mingling, unstructured and semi-structured conversations, awareness, agency, porosity, reciprocity |                                                                                                                         |          |
| Ubicomp 2023       | [Exploring the Opportunities of AR for Enriching Storytelling with Family Photos between Grandparents and Grandchildren](https://dl.acm.org/doi/abs/10.1145/3610903) | AR, storytelling, intergenerational communication                                                  |                                                                                                                         |          |
| Ubicomp 2023       | [Contact Tracing for Healthcare Workers in an Intensive Care Unit](https://dl.acm.org/doi/10.1145/3610924) | contact Tracing, Internet of things (IoT), bluetooth low energy, Covid-19                            |                                                                                                                         |          |
| Ubicomp 2023       | [A Data-Driven Context-Aware Health Inference System for Children during School Closures](https://dl.acm.org/doi/10.1145/3580800) | data analysis, school closures, health inference, risk factor analysis                               |                                                                                                                         |          |
| Ubicomp 2023       | [Privacy-Enhancing Technology and Everyday Augmented Reality: Understanding Bystanders’ Varying Needs for Awareness and Consent](https://dl.acm.org/doi/10.1145/3569501) | AR, privacy, bystanders, altered reality, extended perception, biometrics                            |                                                                                                                         |          |
| Ubicomp 2023       | [MoCaPose: Motion Capturing with Textile-integrated Capacitive Sensors in Loose-fitting Smart Garments](https://dl.acm.org/doi/abs/10.1145/3580883) | motion capture, wearable sensing, capacitive sensing, deep learning, motion tracking, smart textile  |                                                                                                                         |          |
| Ubicomp 2023       | [PoseSonic: 3D Upper Body Pose Estimation Through Egocentric Acoustic Sensing on Smartglasses](https://dl.acm.org/doi/abs/10.1145/3610895?af=R) | human pose estimation, acoustic sensing, smart/AR glasses, deep learning, cross-modal supervision    |                                                                                                                         |          |
| Ubicomp 2023       | [MI-Poser: Human Body Pose Tracking Using Magnetic and Inertial Sensor Fusion with Metal Interference Mitigation](https://dl.acm.org/doi/10.1145/3610891) | EMF, body pose tracking, inverse kinematics, sensor fusion                                           |                                                                                                                         |          |
| Ubicomp 2023       | [Headar: Sensing Head Gestures for Confirmation Dialogs on Smartwatches with Wearable Millimeter-Wave Radar](https://dl.acm.org/doi/abs/10.1145/3610900) | wearable interaction, gestural input, millimeter-wave radar, head gestures, smartwatch               |                                                                                                                         |          |
| Ubicomp 2023       | [DRG-Keyboard: Enabling Subtle Gesture Typing on the Fingertip with Dual IMU Rings](https://dl.acm.org/doi/10.1145/3569463) | text entry, gesture keyboard, fingertip interaction, smart ring                                      |                                                                                                                         |          |
| Ubicomp 2023       | [Abacus Gestures: A Large Set of Math-Based Usable Finger-Counting Gestures for Mid-Air Interactions](https://dl.acm.org/doi/10.1145/3610898) | vision, mid-air, gesture interaction, math, finger counting, abacus                                  |                                                                                                                         |          |
| Ubicomp 2023       | [sUrban: Stable Prediction for Unseen Urban Data from Location-based Sensors](https://dl.acm.org/doi/abs/10.1145/3610877) | urban computing, location-based data, spatial-temporal prediction, out-of-distribution data          |                                                                                                                         |          |
| Ubicomp 2023       | [Spectral-Loc: Indoor Localization Using Light Spectral Information](https://dl.acm.org/doi/10.1145/3580878) | indoor localization, spectral information, ambient light                                           |                                                                                                                         |          |
| arXiv(v2) 2024      | [IMUOptimize: A Data-Driven Approach to Optimal IMU Placement for Human Pose Estimation with Transformer Architecture](https://arxiv.org/abs/2402.08923) | IMU, transformer, interpretability, data driven, time series                                         |                                                                                                                         | 2024.02  |
| CVPR 2024          | [Dynamic Inertial Poser (DynaIP): Part-Based Motion Dynamics Learning for Enhanced Human Pose Estimation with Sparse Inertial Sensors](https://arxiv.org/abs/2312.02196) | IMU, sparse inertial sensors                                                                       |                                                                                                                         | 2024.03  |
| Ubicomp 2023       | [N-euro Predictor: A Neural Network Approach for Smoothing and Predicting Motion Trajectory](https://dl.acm.org/doi/10.1145/3610884) | vision-based interactions, motion-to-photon latency, motion prediction, neural network, perceived jitter and lag |                                                                                                                         |          |
| Ubicomp 2023       | [GC-Loc: A Graph Attention Based Framework for Collaborative Indoor Localization Using Infrastructure-free Signals](https://dl.acm.org/doi/10.1145/3569495) | collaborative indoor localization, graph neural network, geomagnetism                               |                                                                                                                         |          |
| arXiv(v5) 2024      | [Evaluating Human-Language Model Interaction](https://arxiv.org/abs/2212.09746) | LM, human-centered, evaluation                                                                     |                                                                                                                         |          |
| Ubicomp 2023       | [WristAcoustic: Through-Wrist Acoustic Response Based Authentication for Smartwatches](https://dl.acm.org/doi/10.1145/3569473) | smartwatch authentication, bone conduction, acoustic response                                      |                                                                                                                         |          |
| Ubicomp 2023       | [VibPath: Two-Factor Authentication with Your Hand's Vibration Response to Unlock Your Phone](https://dl.acm.org/doi/10.1145/3610894) | user authentication, vibration, IMU, smartphone, wearables, smartwatch                               |                                                                                                                         |          |
| Ubicomp 2024       | [CAvatar: Real-time Human Activity Mesh Reconstruction via Tactile Carpets](https://dl.acm.org/doi/pdf/10.1145/3631424) | human activity reconstruction, 3D human mesh, pressure and vibrations, tactile sensor                |                                                                                                                         |          |
| Ubicomp 2023       | [NF-Heart: A Near-field Non-contact Continuous User Authentication System via Ballistocardiogram](https://dl.acm.org/doi/10.1145/3580851) | continuous authentication, ballistocardiogram (BCG), biometrics, non-contact sensing, smart chair      |                                                                                                                         |          |
| Ubicomp 2023       | [Fingerprinting IoT Devices Using Latent Physical Side-Channels](https://dl.acm.org/doi/abs/10.1145/3596247) | physical side-channels, fingerprinting, internet-of-things                                         |                                                                                                                         |          |
| Ubicomp 2023       | [ViSig: Automatic Interpretation of Visual Body Signals Using On-Body Sensors](https://dl.acm.org/doi/10.1145/3580797) | visual signalling, on-body sensors, UWB, IMU, body signals, fallback communication, sports automation, postures, gestures |                                                                                                                         |          |
| Ubicomp 2024       | Mental-LLM: Leveraging Large Language Models for Mental Health Prediction via Online Text Data |                                                                                                    |                                                                                                                         |          |
| Ubicomp 2023       | SkinLink: On-body Construction and Prototyping of Reconfigurable Epidermal Interfaces |                                                                                                    |                                                                                                                         |          |
| Ubicomp 2023       | Radio2Text: Streaming Speech Recognition Using mmWave Radio Signals |                                                                                                    |                                                                                                                         |          |
| Ubicomp 2023       | HIPPO: Pervasive Hand-Grip Estimation from Everyday Interactions |                                                                                                    |                                                                                                                         |          |
| Ubicomp 2023       | LT-Fall: The Design and Implementation of a Life-threatening Fall Detection and Alarming System |                                                                                                    |                                                                                                                         |          |
| Ubicomp 2022       | [IF-ConvTransformer: A Framework for Human Activity Recognition Using IMU Fusion and ConvTransformer](https://dl.acm.org/doi/10.1145/3534584) | IMU, fusion, multimodal, transformer, attention                                                    |                                                                                                                         |          |
| ISWC 2023          | [On the Utility of Virtual On-body Acceleration Data for Fine-grained Human Activity Recognition](https://dl.acm.org/doi/10.1145/3594738.3611364) | HAR, virtual, IMU                                                                                  |                                                                                                                         |          |
| ISWC 2023          | [C-Auth: Exploring the Feasibility of Using Egocentric View of Face Contour for User Authentication on Glasses](https://dl.acm.org/doi/10.1145/3594738.3611355) | smart glasses, authentication, ecocentric view                                                     |                                                                                                                         |          |
| ISWC 2023          | Towards a Haptic Taxonomy of Emotions: Exploring Vibrotactile Stimulation in the Dorsal Region |                                                                                                    |                                                                                                                         |          |

# LLM

| Source               | Title (Link) | Tag                                      | Additional info                                                                 | Date           |
|----------------------|--------------|------------------------------------------|---------------------------------------------------------------------------------|----------------|
| arXiv(v1) 2023       | [Multimodal Foundation Models: From Specialists to General-Purpose Assistants](https://arxiv.org/abs/2309.10020) | survey                                   |                                                                                 | 2023.09       |
| NIPS 2023            | [Large Language Model as Attributed Training Data Generator: A Tale of Diversity and Bias](https://arxiv.org/abs/2306.15895) | synthetic data generation                |                                                                                 | arXiv(v2) 2023.10 |
| arXiv(v1) 2024       | [Design2Code: How Far Are We From Automating Front-End Engineering?](https://arxiv.org/abs/2403.03163) | llm, auto, google                        |                                                                                 | 2024.03       |
| arXiv(v2) 2023       | [The Good, The Bad, and Why: Unveiling Emotions in Generative AI](https://arxiv.org/abs/2312.11111) | emotion, prompt, attack, decode            | extension of Large language models understand and can be enhanced by emotional stimuli | 2023.12       |
| arXiv(v1) 2024       | [Are You Being Tracked? Discover the Power of Zero-Shot Trajectory Tracing with LLMs!](https://arxiv.org/abs/2403.06201) | iot, imu, cot, prompt                      |                                                                                 | 2024.03       |
| arXiv(v1) 2024       | [Ferret-UI: Grounded Mobile UI Understanding with Multimodal LLMs](https://arxiv.org/abs/2404.05719) | ui, mllm, benchmark, any-resolution        |                                                                                 | 2024.04       |


# RAG

| Source               | Title (Link) | Tag                                                | Additional info | Date     |
|----------------------|--------------|----------------------------------------------------|-----------------|----------|
| arXiv(v6) 2024       | [Health-LLM: Personalized Retrieval-Augmented Disease Prediction System](https://arxiv.org/abs/2402.00746) | RAG, XGBoost, AutoML                           |                 | 2024.03 |
| arXiv(v1) 2024       | CRUD-RAG: A Comprehensive Chinese Benchmark for Retrieval-Augmented Generation of Large Language Models | retrieval-augmented generation, large language models, evaluation |                 | 2024.02 |
| arXiv(v1) 2024       | LLM-Augmented Retrieval: Enhancing Retrieval Models Through Language Models and Doc-Level Embedding | relevant query, doc-Level embedding, embedding-based retrieval, dense retrieval |                 | 2024.04 |


# Agent

| Source               | Title (Link) | Tag                                                | Additional info                                                                                   | Date         |
|----------------------|--------------|----------------------------------------------------|---------------------------------------------------------------------------------------------------|--------------|
| ICLR 2024            | [MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework](https://arxiv.org/abs/2308.00352) | autonomous system, SOP, multi-agent, framework      |                                                                                                   |              |
| arXiv(v1) 2024       | [DataDreamer: A Tool for Synthetic Data Generation and Reproducible LLM Workflows](https://arxiv.org/abs/2402.10379) | pipeline, liarbry, generation                        |                                                                                                   | 2024.02      |
| arXiv(v2) 2023       | [MusicAgent: An AI Agent for Music Understanding and Generation with Large Language Models](https://arxiv.org/abs/2310.11954) | pipeline                                           |                                                                                                   | 2023.10      |
| arXiv(v3) 2023       | [The Rise and Potential of Large Language Model Based Agents: A Survey](https://arxiv.org/abs/2309.07864) | survey, [github paper list](https://github.com/WooooDyy/LLM-Agent-Paper-List) |                                                                                                   | 2023.09      |
| NIPS 2023            | [CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society](https://arxiv.org/abs/2303.17760) | role play, autonomous, user&assistant              |                                                                                                   | 2023.11(v2)  |
| NIPS 2023            | [HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face](https://arxiv.org/abs/2303.17580) | hugging face, API                                  |                                                                                                   | 2023.12      |
| arXiv(v2) 2023       | [VOYAGER: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) | multi, autonomous, microcraft, game                |                                                                                                   | 2023.10      |
| arXiv(v1) 2024       | [More Agents Is All You Need](https://arxiv.org/abs/2402.05120) | multi agent, vote, task                            |                                                                                                   | 2024.02      |
| arXiv(v3) 2023       | [A Survey on Large Language Model based Autonomous Agents](https://arxiv.org/abs/2308.11432) | survey, autonomous                                 | Latest version is v4(2024.03), double columns. But v3(2023.09) single columns is easy to read.   |              |





# Poster
