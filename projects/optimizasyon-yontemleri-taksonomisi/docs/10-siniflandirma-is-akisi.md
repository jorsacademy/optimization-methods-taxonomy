# 10. Herhangi Bir Optimizasyon Algoritması Nasıl Sınıflandırılır?

[← Karşılaştırma matrisi](09-karsilastirma-matrisi.md) · [Sonraki: Yaygın kavram karışıklıkları →](11-yaygin-kavram-karisikliklari.md)

Tanımadığınız bir optimizasyon yöntemiyle karşılaştığınızda bu iş akışını kullanın.

## Adım 1 — Çözülen optimizasyon problemini belirleyin

Şunları sorun:

- Karar değişkenleri neler?
- Sürekli, integer, binary, permutation, subset veya mixed mı?
- Amaç fonksiyonu ne?
- Kısıtlar neler?
- Model linear, nonlinear, convex veya nonconvex mı?
- Amaç deterministic, noisy veya stochastic mı?

Problem sınıfını anlamadan algoritmayı sınıflandırmayın. Garantiler çoğunlukla problem bağımlıdır.

## Adım 2 — Yöntemin hangi garantiyi verdiğini sorun

Olası cevaplar:

- global optimality certificate,
- local optimality/stationarity guarantee,
- approximation ratio,
- varsayımlar altında asymptotic convergence,
- formal solution-quality guarantee yok.

Bu bilgi **exact**, **approximation**, **heuristic** veya **metaheuristic** terimlerinin uygun olup olmadığını belirler.

## Adım 3 — Finite-time garantiler ile asimptotik ifadeleri ayırın

Bunlar eşdeğer değildir.

Bir algoritmanın, ideal koşullarda iterasyon sayısı sonsuza giderken küresel optimuma yakınsadığını söyleyen bir teoremi olabilir. Bu, mevcut çözümün sonlu zamanda küresel optimal olduğunu sertifikalandırmakla aynı şey değildir.

Her zaman sorun:

- İfade finite-time mı, asymptotic mi?
- Deterministic mi, probabilistic mi?
- Her instance için mi, özel varsayımlar altında mı geçerli?

## Adım 4 — Algoritmanın rassallık kullanıp kullanmadığını belirleyin

Şunları arayın:

- random initialization,
- probabilistic transitions,
- mutation,
- sampling,
- randomized rounding,
- randomized tie-breaking,
- Monte Carlo estimates.

Rassallık varsa bu eksende yöntemi stochastic/randomized olarak sınıflandırın.

Buradan otomatik olarak “heuristic” sonucu çıkarmayın.

## Adım 5 — Arama temsilini belirleyin

Algoritma hangi durumu tutuyor?

- one incumbent solution,
- population,
- search tree,
- frontier / priority queue,
- probability distribution,
- surrogate model,
- dual variables ve decomposed subproblems.

Bu yapı çoğu zaman yöntemi metaforik isminden daha iyi açıklar.

## Adım 6 — Yerel ve küresel davranışı belirleyin

Sorular:

- Her iterasyon yalnızca bir neighborhood'u mu inceliyor?
- Restarts veya perturbations var mı?
- Tüm feasible region sistematik olarak partition/bound ediliyor mu?
- Diversity açıkça korunuyor mu?
- Yöntem birden fazla basin'i ziyaret etmek üzere mi tasarlanmış?

Bir heuristic geniş arama yapıyor fakat global optimality proof vermiyorsa **global-search-oriented / küresel arama odaklı** ifadesini kullanın.

**Globally optimal** ifadesini arama niyeti için değil garanti için ayırın.

## Adım 7 — Bilgi gereksinimini belirleyin

Yöntem ne kullanıyor?

- yalnızca objective values,
- gradients,
- Hessians,
- constraint Jacobians,
- relaxations,
- bounds,
- simulations,
- surrogate predictions.

Buna göre:

- zeroth-order,
- first-order,
- second-order,
- derivative-free,
- model-based,
- surrogate-based

etiketleri kullanılabilir.

## Adım 8 — Modeli ayrıca sınıflandırın

Algoritmadan bağımsız olarak modelin:

- deterministic veya stochastic,
- robust,
- fuzzy,
- single- veya multi-objective,
- static, dynamic veya online,
- centralized veya distributed

olduğunu kaydedin.

Model özelliklerini algoritma özellikleriyle birleştirmeyin.

## Adım 9 — Implementasyona bağlı özellikleri açıkça belirtin

Bazı özellikler yöntem ailesinin doğal tanımının parçası değildir.

Örnekler:

- Tabu Search deterministic veya stochastic olabilir.
- Branch and Bound randomized branching kullanabilir.
- Bayesian Optimization deterministic veya stochastic acquisition optimization kullanabilir.
- Hill Climbing deterministic best-improvement veya randomized move selection kullanabilir.

Gerektiğinde “genellikle”, “standart implementasyonda” veya “implementasyona bağlı” ifadelerini tercih edin.

## Adım 10 — Nihai sınıflandırmayı cümle olarak yazın

### Simulated Annealing örneği

> Simulated Annealing, yerel optimumlarda sıkışma riskini azaltmak ve daha geniş aramayı teşvik etmek için sıcaklık kontrollü bir kurala göre bazı kötüleşen hareketleri kabul eden, tek çözüm tabanlı ve çoğunlukla stokastik bir metasezgiseldir. Sonlu bir koşum normalde küresel optimaliteyi sertifikalandırmaz.

### Branch and Cut örneği

> Branch and Cut, Branch and Bound ile dinamik üretilen geçerli eşitsizlikleri birleştiren exact mixed-integer optimization framework'üdür. Kavramsal düzeyde çoğunlukla deterministiktir; ancak solver implementasyonları randomized veya adaptive bileşenler kullanabilir. Optimality gap kapanmadan durdurulursa incumbent henüz kanıtlanmış optimum değildir.

### NSGA-II örneği

> NSGA-II, multi-objective optimization için stokastik, popülasyon tabanlı evrimsel bir metasezgiseldir. Tek bir evrensel en iyi çözüm yerine Pareto frontier'ı yaklaşık temsil etmek için nondominated sorting ve diversity preservation kullanır.

## Yeniden kullanılabilir sınıflandırma şablonu

```text
Yöntem:
Problem sınıfı:
Garanti:
Rassallık:
Arama kapsamı:
Temsil:
Kullanılan bilgi:
Kısıt yönetimi:
Tek / çok amaçlı:
Model belirsizliği:
Tipik güçlü yönler:
Tipik sınırlamalar:
Önemli varsayımlar / notlar:
```

Bu alanlar dikkatli doldurulduğunda yaygın taksonomi hatalarının çoğu ortadan kalkar.
