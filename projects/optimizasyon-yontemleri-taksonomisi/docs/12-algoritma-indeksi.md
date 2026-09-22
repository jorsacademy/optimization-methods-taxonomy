# 12. Algoritma ve Yöntem İndeksi

[← Yaygın kavram karışıklıkları](11-yaygin-kavram-karisikliklari.md) · [README'ye dön](../README.md)

Bu ek, rehber boyunca adı geçen yöntemleri tek yerde toplar ve kısa sınıflandırmalar verir. Ana bölümlerde açıklanan varsayım ve nitelendirmelerin yerine geçmez.

## Exact mathematical programming ve discrete optimization yöntemleri

### Simplex

Linear programming için basis-based algoritmadır. Optimizasyon anlamında exact LP solution framework'üdür; pivoting ve tie-breaking kuralları sabitse deterministiktir.

### Dual Simplex

Primal feasibility'ye doğru ilerlerken dual feasibility'yi koruyan Simplex varyantıdır. Özellikle model değişiklikleri veya branching kararlarından sonra LP/MILP solver'larda yaygın kullanılır.

### Interior-Point Methods

Linear ve convex optimization için barrier-based numerical methods. Convergence ve optimality guarantees problem class ve method assumptions'a bağlıdır; pratik solver'lar numerical tolerances kullanır.

### Branch and Bound

Feasible region'ı parçalayan ve incumbent'ı iyileştiremeyecek bölgeleri bounds ile budayan exact search framework. Integer, mixed-integer ve global optimization'da yaygındır.

### Branch and Cut

Arama sırasında üretilen valid inequalities ile güçlendirilmiş Branch and Bound. Modern MILP solving'in temel bileşenlerinden biridir.

### Cutting Plane Methods

Geçerli hedef çözümleri dışlamadan infeasible veya nonintegral relaxation solutions'ı kesen valid constraints iteratif olarak eklenir.

### Branch and Price

Branch and Bound ile column generation'ın birleşimidir. Doğal formülasyonda çok büyük sayıda değişken olduğunda yararlıdır.

### Branch-Cut-and-Price

Branching, cutting planes ve column generation'ı birleştiren solver framework.

### Dynamic Programming

Geçerli Bellman recursion gerekli state space'i kapsadığında exact'tır. Sequential/decomposable problemler için güçlüdür; state-space explosion'a duyarlıdır.

## Graph ve network algoritmaları

### Dijkstra

Nonnegative edge weights için exact single-source shortest-path algorithm.

### Bellman–Ford

Reachable negative cycle bulunmaması koşuluyla negative edge weights'e izin veren exact single-source shortest-path algorithm.

### Floyd–Warshall

All-pairs shortest paths için dynamic-programming algorithm.

### Kruskal

Minimum spanning tree için greedy exact algorithm.

### Prim

Minimum spanning tree için greedy exact algorithm.

### Ford–Fulkerson

Maximum flow için augmenting-path framework. Sonlanma ayrıntıları capacity assumptions ve path selection'a bağlıdır.

### Edmonds–Karp

Breadth-first search kullanan polynomial-time augmenting-path implementation.

### Hungarian Algorithm

Assignment problem için exact algorithm.

## Approximation algorithms ve schemes

### Vertex Cover 2-Approximation

Kanıtlanmış factor-2 worst-case bound'a sahip klasik approximation algorithm örneği.

### Christofides' Algorithm

Metric TSP için, metric assumptions altında kanıtlanmış worst-case guarantee sunan polynomial-time approximation algorithm.

### Set Cover Approximation

Greedy Set Cover logaritmik türde approximation guarantee sunar.

### PTAS

Polynomial-Time Approximation Scheme, böyle bir scheme kabul eden problem sınıflarında her sabit `ε>0` için `(1+ε)` türü approximation sunar.

### FPTAS

Fully Polynomial-Time Approximation Scheme hem input size hem `1/ε` bakımından polynomial'dır.

## Constructive heuristics ve local improvement

### Nearest Neighbor

En yakın ziyaret edilmemiş şehri seçerek ilerleyen constructive TSP heuristic. Hızlı ve basittir; genel optimality guarantee yoktur.

### Greedy Assignment / Placement Rules

Her construction step'te yerel olarak tercih edilen feasible seçimi yapan problem-specific heuristics.

### First Fit ve Best Fit

Packing problemlerinde, seçilmiş ordering altında öğeleri ilk veya en uygun feasible konuma yerleştiren klasik heuristics.

### Savings Algorithm

Vehicle routing ile ilişkilendirilen, calculated savings üzerinden route merging yapan constructive routing heuristic.

### Hill Climbing

Improving moves'ı tekrar tekrar kabul eden local-search heuristic. Move selection'a bağlı olarak deterministic veya randomized olabilir.

### Local Search

Tanımlı neighborhood kullanarak mevcut çözümü iyileştiren geniş yöntem ailesidir. Davranışı neighborhood ve acceptance rule belirler.

### 2-opt ve 3-opt

Sırasıyla iki veya üç edge'i değiştiren route-improvement neighborhoods. TSP ve routing'de yaygındır.

## Continuous numerical optimization

### Gradient Descent

First-order iterative method. Global-optimum convergence; convexity ve uygun step-size rule gibi varsayımlar gerektirir. Nonconvex settings'te genel olarak local/stationarity-oriented'dır.

### Stochastic Gradient Descent — SGD

Sampled veya noisy gradient estimates kullanan stochastic first-order method. “Stochastic” sözcüğü algoritmik gradient estimate'i tanımlar; stochastic optimization model ile karıştırılmamalıdır.

### Coordinate Descent

Her adımda bir coordinate veya coordinate block günceller. Guarantees convexity, smoothness ve update rules'a bağlıdır.

### Newton's Method

Hessian information kullanan second-order method. Uygun çözüm yakınında çok hızlı yakınsayabilir; global behavior problem structure ve globalization mechanisms'a bağlıdır.

### BFGS ve L-BFGS

Second-order information'ı yaklaşık kullanan Quasi-Newton yöntemleri. L-BFGS limited memory kullanır ve large-scale smooth optimization'da yaygındır.

### Conjugate Gradient

Quadratic systems ve ilişkili optimization problems için temel yöntemlerden biridir. Rolü ve garantileri formülasyona bağlıdır.

### Sequential Quadratic Programming — SQP

Constrained nonlinear optimization'ı quadratic subproblems dizisiyle çözen framework.

### Nelder–Mead

Simplex of points kullanan derivative-free direct-search method. Low-dimensional black-box optimization'da yaygındır; genel global-optimum guarantee yoktur.

### Hooke–Jeeves / Pattern Search

Exploratory/pattern moves veya structured polling directions kullanan derivative-free search.

### Powell-Type Methods

Explicit gradients gerektirmeden directional searches kullanan continuous derivative-free methods.

## Single-solution metaheuristics

### Simulated Annealing

Genellikle stokastiktir. Local trapping'i azaltmak için temperature-dependent probability ile bazı worsening moves'ı kabul eder. Single-solution ve global-search-oriented'dır.

### Tabu Search

Tabu restrictions, aspiration ve diversification/intensification kullanan memory-based metaheuristic. Deterministic veya stochastic olabilir.

### Iterated Local Search — ILS

Local optimization ile perturbation/re-optimization arasında geçiş yaparak attraction basins arasında hareket eder.

### Variable Neighborhood Search — VNS

Local optima'dan kaçmak ve farklı yapıları keşfetmek için neighborhoods'ı sistematik biçimde değiştirir.

### Variable Neighborhood Descent — VND

Birden fazla neighborhood'u descent framework içinde, çoğu zaman deterministik olarak kullanır.

### GRASP

Greedy Randomized Adaptive Search Procedure. Tekrar tekrar randomized greedy solution kurar ve local improvement uygular.

### Multi-Start Local Search

Search space coverage'ı artırmak için local optimizer'ı birden fazla starting point'ten çalıştırır.

### Basin Hopping

Perturbations ile local minimization'ı birleştirir ve basins arasındaki transitions'ı kabul/reddeder.

## Evolutionary ve population-based metaheuristics

### Genetic Algorithm — GA

Selection, crossover ve mutation kullanan population-based evolutionary metaheuristic. Genellikle stochastic ve derivative-free'dir.

### Evolution Strategy — ES

Mutation, selection ve strategy-parameter adaptation'a güçlü vurgu yapan evolutionary optimization family.

### Differential Evolution — DE

Özellikle continuous derivative-free optimization'da öne çıkan population-based stochastic evolutionary method.

### Genetic Programming — GP

Fixed-length numeric vectors yerine program structures veya symbolic expressions üzerinde evolutionary search yapar.

### Memetic Algorithm

Population-based search ile local improvement'ı birleştiren hybrid evolutionary method.

### Scatter Search

Stratejik olarak seçilen çözümleri sistematik biçimde birleştiren population/reference-set metaheuristic.

### CMA-ES

Covariance Matrix Adaptation Evolution Strategy. Continuous black-box optimization için multivariate search distribution'ı adapte eden stochastic derivative-free method.

## Swarm-intelligence yöntemleri

### Particle Swarm Optimization — PSO

Particles'ın positions'ını individual/shared search information ile güncellediği population/swarm metaheuristic. Genellikle stokastiktir.

### Ant Colony Optimization — ACO

Artificial ants'in çözümler kurduğu ve pheromone information ile dolaylı iletişim yaptığı multi-agent metaheuristic.

### Artificial Bee Colony — ABC

Aday bölgelerde exploration/exploitation için farklı arama rolleri kullanan swarm-inspired population method.

### Firefly Algorithm

Aday çözümler arasındaki attraction relationships kullanan population-based stochastic metaheuristic.

## Diğer nature/process-inspired metaheuristics

### Harmony Search

Musical improvisation metaforundan esinlenen population-based metaheuristic. Harmony memory, memory consideration ve randomization mechanisms kullanır.

### Gravitational Search

Candidate agents arasındaki gravitational interaction metaforunu kullanan population-based metaheuristic.

### Electromagnetism-Like Optimization

Charged particles arasındaki attraction/repulsion metaforundan esinlenen population-based search.

Metafor ikincildir; bu yöntemler yine representation, randomness, operators, guarantee ve evaluation cost üzerinden analiz edilmelidir.

## Multi-objective yöntemler

### Weighted Sum

Birden fazla amacı weighted scalar objective'e dönüştürür. Basittir; fakat nonconvex Pareto frontier'ın bazı bölgelerini bulamayabilir.

### ε-Constraint Method

Bir amacı optimize ederken diğer amaçları bounded constraints'e dönüştürür. Multi-objective optimization için klasik mathematical-programming yaklaşımıdır.

### Goal Programming

Target/aspiration levels'tan sapmaları modeller ve seçilen deviation measures'ı minimize eder.

### NSGA-II

Nondominated sorting ve diversity preservation kullanan stochastic population-based evolutionary metaheuristic.

### NSGA-III

Reference directions/points kullanarak özellikle many-objective problems için tasarlanan multi-objective evolutionary algorithm.

### SPEA2

Strength Pareto Evolutionary Algorithm 2. Dominance ve density information kullanan population-based multi-objective evolutionary method.

### MOEA/D

Multi-Objective Evolutionary Algorithm based on Decomposition. Multi-objective problemi etkileşimli scalar subproblems'a ayırır.

### Multi-Objective PSO

Nondominated trade-off solutions kümesini korumak ve keşfetmek üzere uyarlanmış PSO türleri.

## Uncertainty, sequential ve distributed optimization

### Two-Stage Stochastic Programming

First-stage decisions belirsizlik ortaya çıkmadan, recourse decisions ise belirsizlik görüldükten sonra verilir.

### Multistage Stochastic Programming

Stochastic decision-making'i birden fazla information-revelation stage boyunca genişletir.

### Sample Average Approximation — SAA

Stochastic expectations'ı finite sampled scenario set ile yaklaşıklar ve ortaya çıkan deterministic sample problem'i çözer.

### Chance-Constrained Programming

Constraints'in uncertainty model altında belirli probability level ile sağlanmasını ister.

### Robust Optimization

Tek bir nominal parameter realization'a güvenmek yerine uncertainty sets veya ilgili ambiguity descriptions'a karşı optimize eder.

### Model Predictive Control — MPC

Sistem geliştikçe finite-horizon optimization problem'i tekrar tekrar çözer, yakın dönem control action'ı uygular ve yeni state information ile yeniden optimize eder.

### Approximate Dynamic Programming — ADP

Large state spaces'i yönetmek için value functions, policies veya ilgili DP bileşenlerini yaklaşıklar.

### Reinforcement Learning — RL

Stochastic control ve Dynamic Programming ile ilişkili geniş sequential decision-learning ailesidir. Generic optimization etiketiyle indirgenmemelidir.

### ADMM

Alternating Direction Method of Multipliers. Uygun varsayımlar altında structured convex optimization ve distributed computation için yaygın decomposition framework.

### Dual Decomposition

Coupling constraints'e bağlı dual variables üzerinden structured problems'ı ayrıştırır.

### Consensus Optimization

Agents'in shared variables/decisions üzerinde anlaşmaya doğru koordine olduğu distributed optimization.

### Distributed Gradient Descent

Communication/consensus steps ile birden fazla agent veya compute node üzerinde yürütülen first-order optimization.

### Federated Optimization

Raw local data'nın doğrudan paylaşımını azaltmak üzere tasarlanabilen, data-holding clients arasında distributed learning/optimization.

## Surrogate ve black-box optimization

### Bayesian Optimization

Expensive objectives için surrogate-based global optimization framework. Predictive model kurma ile acquisition function üzerinden yeni evaluations seçme arasında dönüşümlü çalışır.

### Gaussian-Process Surrogates

Özellikle relatively low-dimensional expensive functions için Bayesian Optimization'da yaygın kullanılan probabilistic surrogate models.

### Random-Forest Surrogates

Bazı black-box settings'te nonlinear ve mixed-structure response modeling için yararlı tree-ensemble surrogates.

### Neural-Network Surrogates

Yeterli evaluation data bulunduğunda kullanılabilen esnek learned approximations.

### Polynomial Response Surfaces

Response-surface methodology'de kullanılan klasik low-order surrogate models.

### Radial Basis Function Surrogates

Derivative-free ve expensive black-box optimization'da sık kullanılan interpolation/approximation models.

## Hybrid ve matheuristic yöntemler

### Local Branching

Incumbent çevresinde matematiksel neighborhood tanımlar ve mixed-integer programming machinery ile arar.

### Relaxation Induced Neighborhood Search — RINS

Incumbent ile relaxation solution bilgisini kullanarak exact veya bounded optimization için restricted neighborhood tanımlar.

### Feasibility Pump

Mixed-integer programming'de feasibility aramak için relaxation information ile integer-oriented projections/rounding arasında dönüşümlü çalışan heuristic.

### Fix-and-Optimize

Incumbent'ın bir bölümünü sabitlerken seçilmiş variable block'u yeniden optimize eder.

### Relax-and-Fix

Integer variables'ı blocks'a ayırır; sonraki blokları geçici relax ederken integrality/fixing decisions'ı kademeli olarak uygular.

### Large Neighborhood Search — LNS

Çözümün bir kısmını destroy eder ve oluşan large neighborhood'u repair/reoptimize eder. Repair step heuristic veya exact olabilir.

## Son hatırlatma

Bu indeksteki hiçbir yöntem tek bir sıfat üzerinden sınıflandırılmamalıdır. Eksiksiz tanım en az şu boyutları sorar:

```text
garanti
+ rassallık
+ arama kapsamı
+ temsil
+ problem yapısı
+ kullanılan bilgi
+ varsayımlar
```

Bu çok eksenli tanımlama, reponun temel ilkesidir.
