# 9. Çok Boyutlu Karşılaştırma Matrisi

[← Hibrit yöntemler](08-hibrit-yontemler.md) · [Sonraki: Sınıflandırma iş akışı →](10-siniflandirma-is-akisi.md)

Aşağıdaki tablo, tek boyutlu taksonominin neden yetersiz olduğunu gösterir. Varsayımlar veya uygulama tercihleri önemliyse etiketler özellikle nitelendirilmiştir.

| Yöntem | Garanti sınıfı | Rassallık | Arama kapsamı | Temsil / mekanizma | Tipik alan | Önemli not |
|---|---|---|---|---|---|---|
| Simplex | LP için exact | Genellikle deterministik | LP için küresel | Basis / vertex transitions | Linear programming | Sayısal solver'lar tolerans kullanır; pivot kuralı yolu değiştirir |
| Interior-point methods | Varsayımlar altında convex/LP sınıflarında exact-solution framework | Genellikle deterministik | Uygun convexity varsayımlarında küresel | Continuous trajectory / barrier system | LP, convex optimization | Convergence theory problem sınıfına ve yönteme bağlıdır |
| Branch and Bound | Doğru biçimde tamamlandığında exact | Genellikle deterministik; rassallaştırılabilir | Küresel/sistematik | Search tree + bounds | Integer/global optimization | Nonzero optimality gap ile erken durdurulabilir |
| Branch and Cut | Doğru biçimde tamamlandığında exact | Genellikle deterministik; implementasyona bağlı | Küresel/sistematik | Search tree + cutting planes | MILP | Modern solver'lar içeride heuristics kullanır |
| Dynamic Programming | Kurulan recursion için exact | Genellikle deterministik | State recursion üzerinde küresel | Subproblems / states | Discrete ve sequential problems | State explosion belirleyici olabilir |
| Dijkstra | Varsayımları altında shortest path için exact | Sabit tie ile deterministik | İlgili problem için küresel | Graph frontier | Graph optimization | Nonnegative edge weights gerekir |
| Gradient Descent | Varsayıma bağlı convergence | Full-batch'te genellikle deterministik | Yerel yönelimli | Single solution, first-order | Continuous optimization | Uygun convex assumptions altında global optimum; nonconvex için genel değil |
| SGD | Varsayıma bağlı convergence | Stokastik | Yerel yönelimli | Single solution, sampled first-order | Large-scale learning/optimization | Rassallık sampled gradient estimates'ten gelir |
| Hill Climbing | Heuristic | Deterministik veya stokastik | Yerel | Single solution | General/discrete | Neighborhood ve initialization'a çok duyarlıdır |
| Nearest Neighbor | Heuristic | Start/tie kurallarından sonra genellikle deterministik | Constructive/local decision rule | Tek constructive solution | TSP-like routing | Hızlıdır; genel optimality guarantee yoktur |
| Christofides | Approximation algorithm | Standart biçimde deterministik | Global construction | Constructive graph algorithm | Metric TSP | Guarantee metric assumptions'a bağlıdır |
| Simulated Annealing | Metaheuristic | Stokastik | Küresel arama odaklı | Single solution | General | Finite run global optimumu normalde sertifikalandırmaz |
| Tabu Search | Metaheuristic | Deterministik veya stokastik | Küresel arama odaklı | Single solution + memory | Combinatorial optimization | Memory ve neighborhood tasarımı kritiktir |
| Genetic Algorithm | Metaheuristic | Genellikle stokastik | Küresel arama odaklı | Population, evolutionary | General | Genel finite-run optimality certificate yoktur |
| Particle Swarm Optimization | Metaheuristic | Genellikle stokastik | Küresel arama odaklı | Population/swarm | Continuous ve uyarlanmış türler | Parameterization/topology'ye duyarlıdır |
| Differential Evolution | Metaheuristic | Stokastik | Küresel arama odaklı | Population, evolutionary | Continuous/global optimization | Birçok black-box problemde güçlü derivative-free baseline |
| Ant Colony Optimization | Metaheuristic | Stokastik | Küresel arama odaklı | Multi-agent + pheromone model | Combinatorial optimization | Kalıcı search information pheromone tabanlıdır |
| Bayesian Optimization | Surrogate-based approximate optimization | Implementasyona bağlı | Küresel arama odaklı | Surrogate + acquisition | Expensive black-box optimization | Evaluation pahalı olduğunda uygundur; dimensionality önemlidir |
| CMA-ES | Metaheuristic / Evolution Strategy | Stokastik | Küresel arama odaklı | Population + adaptive covariance | Continuous black-box optimization | Derivative-free; evaluation cost yüksek olabilir |
| NSGA-II | Multi-objective evolutionary metaheuristic | Stokastik | Küresel arama odaklı | Population + Pareto ranking | Multi-objective optimization | Pareto set/front için approximation üretir |
| ADMM | Decomposition / first-order framework | Genellikle deterministik | Modele bağlı | Distributed/decomposed iterates | Convex structured optimization | Klasik garantiler convexity/regularity varsayımlarına dayanır |

## 9.1 Tablo nasıl okunmalı?

Aynı satır farklı bağımsız eksenlerden etiketler içerir.

### Genetic Algorithm

- **metaheuristic** = garanti/search-framework sınıflandırması,
- **stochastic** = rassallık sınıflandırması,
- **global-search-oriented** = arama kapsamı,
- **population** = temsil,
- **evolutionary** = arama mekanizması.

### Branch and Bound

- **exact** = garanti sınıflandırması,
- **usually deterministic** = yaygın implementasyon davranışı,
- **global/systematic** = arama kapsamı,
- **search tree + bounds** = temsil/mekanizma.

Bu, tüm taksonominin amaçlanan kullanım biçimidir.
