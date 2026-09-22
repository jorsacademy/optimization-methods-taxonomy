# 2. Çözüm Garantileri: Exact, Approximation, Heuristic ve Metaheuristic

[← Temeller](01-temeller.md) · [Sonraki: Rassallık ve arama →](03-rastgelelik-ve-arama.md)

## 2.1 Kesin yöntemler — Exact methods

Bir **exact method**, matematiksel varsayımları altında ve normal biçimde tamamlanmasına izin verildiğinde optimal bir çözümü belirleyebilecek veya geçerli bir optimalite sertifikası sunabilecek şekilde tasarlanır.

```math
\min_{x\in X} f(x)
```

problemi için optimal `x^*` çözümü:

```math
f(x^*) \le f(x), \qquad \forall x\in X
```

koşulunu sağlar.

Exactness hızla ilgili değildir; matematiksel garantiyle ilgilidir. Bir exact yöntem bir örnekte çok hızlı, başka bir örnekte hesaplama açısından uygulanamaz olabilir.

### Tipik exact yöntem aileleri

#### Doğrusal programlama

```math
\begin{aligned}
\min \quad & c^T x \\
\text{s.t.}\quad & Ax \le b
\end{aligned}
```

gibi bir doğrusal program için başlıca exact çözüm algoritması aileleri:

- Simplex,
- Dual Simplex,
- interior-point methods.

Pratik kayan noktalı solver'larda “exact”, optimizasyon anlamında kullanılmalıdır: matematiksel algoritma optimal çözümü hedefler; solver ise sayısal feasibility/optimality toleransları içinde durur. Bu ifade sembolik aritmetik veya sıfır sayısal hata anlamına gelmez.

#### Karma tamsayılı ve ayrık optimizasyon

Önemli exact çerçeveler:

- Branch and Bound,
- Branch and Cut,
- Cutting Plane yöntemleri,
- Branch and Price,
- Branch-Cut-and-Price.

Temel yaklaşım; sınırlar üretmek, uygun bölgeyi bölmek, incumbent'ı iyileştiremeyecek bölgeleri elemek ve optimality gap'i kapatmaktır.

Bir minimizasyon probleminde solver çoğunlukla:

- en iyi uygun incumbent'tan gelen bir **üst sınır**,
- gevşetmelerden veya düğüm sınırlarından gelen bir **alt sınır**

tutar.

Sınırlar seçilen tolerans içinde birleştiğinde optimalite sertifikalandırılır.

#### Dinamik programlama

Dynamic Programming, problemi örtüşen alt problemlere ve optimal alt yapı ilişkisine ayırır. Genel bir Bellman özyinelemesi:

```math
V(s)=\min_{a\in A(s)} \left\{c(s,a)+V(T(s,a))\right\}.
```

Uygulamalar:

- knapsack türleri,
- en kısa yol formülasyonları,
- stok kontrolü,
- kaynak tahsisi,
- çok aşamalı karar problemleri.

Dynamic Programming exact olabilir; ancak durum uzayı üstel veya kombinatoryal büyüyebilir. Bu durum klasik **boyut laneti (curse of dimensionality)** problemidir.

#### Özel grafik algoritmaları

Belirli problem sınıflarında exact olan algoritmalar:

- Dijkstra — negatif olmayan kenar ağırlıklarıyla en kısa yol,
- Bellman–Ford — erişilebilir negatif çevrim bulunmaması koşuluyla negatif kenarlı en kısa yol,
- Floyd–Warshall — tüm çiftler arasında en kısa yollar,
- Kruskal ve Prim — minimum spanning tree,
- Edmonds–Karp — maximum flow,
- Hungarian Algorithm — assignment problem.

Bunlar keyfi optimizasyon modelleri için genel amaçlı exact solver'lar değildir; garantileri ilgili problem sınıfının yapısına dayanır.

## 2.2 Sürekli optimizasyonda “exact” sözcüğünü dikkatli kullanmak

Sürekli sayısal optimizasyonda, iteratif bir yönteme doğrudan “exact” demektense **yakınsama garantilerini** açıklamak çoğu zaman daha doğrudur.

Örnekler:

- Gradient Descent,
- Newton's Method,
- BFGS gibi Quasi-Newton yöntemleri,
- Conjugate Gradient,
- Sequential Quadratic Programming (SQP).

Bu yöntemlerin küresel optimuma ulaşıp ulaşmaması şu tür varsayımlara bağlıdır:

- konvekslik veya güçlü konvekslik,
- türevlenebilirlik veya düzgünlük,
- constraint qualifications,
- line-search veya trust-region koşulları,
- başlangıç noktası ve sayısal toleranslar.

Konveks bir problemde uygun yöntem küresel optimuma yakınsama garantisi verebilir. Konveks olmayan bir problemde aynı yöntem yalnızca durağan noktaya veya yerel optimuma yakınsayabilir.

Bu nedenle:

> **Algoritma adı + problem varsayımları + yakınsama teoremi**, sürekli bir yönteme açıklamasız biçimde “exact” demekten daha bilgilendiricidir.

## 2.3 Yaklaşım algoritmaları — Approximation algorithms

Bir **approximation algorithm**, optimuma göre kanıtlanmış bir kalite sınırı olan çözüm döndürür.

Bir minimizasyon problemi için `α`-yaklaşım garantisi:

```math
f(x_{alg}) \le \alpha f(x^*), \qquad \alpha \ge 1.
```

biçiminde olabilir.

`α = 2` ise algoritma, ilgili teoremin varsayımları altında amaç değerinin optimumun en fazla iki katı olacağını garanti eder.

Örnekler:

- Vertex Cover için 2-approximation,
- Metric TSP için Christofides Algorithm,
- Set Cover için logaritmik katsayılı yaklaşımlar,
- Knapsack türleri için FPTAS yapıları.

Tanımlayıcı fark, approximation algoritmasının pratikte her zaman bir heuristic'ten daha iyi olması değildir. Temel fark, **teorik bir worst-case kalite garantisi** bulunmasıdır.

### PTAS

Polynomial-Time Approximation Scheme, uygun minimizasyon problemlerinde her `ε > 0` için `(1+ε)` türünde garanti veren bir çözümü, sabit `ε` için polinom zamanda üretir.

Ancak `1/ε`'a bağımlılık çok pahalı olabilir.

### FPTAS

Fully Polynomial-Time Approximation Scheme:

- girdi boyutunda,
- `1/ε`'da

polinom zamanda çalışır. Bu daha güçlü bir hesaplama garantisidir.

## 2.4 Sezgiseller — Heuristics

Bir **heuristic**, çoğunlukla genel bir optimalite ispatı veya worst-case approximation ratio sunmadan iyi bir çözümü verimli biçimde bulmayı amaçlayan problem çözme kuralıdır.

Sezgiseller çoğunlukla probleme özgüdür.

Örnekler:

- TSP için Nearest Neighbor,
- greedy assignment kuralları,
- packing için First Fit / Best Fit,
- scheduling priority rules,
- routing için Savings Algorithm,
- repair procedures,
- constructive insertion rules.

### Örnek: TSP için Nearest Neighbor

1. Bir başlangıç şehri seçilir.
2. Ziyaret edilmemiş en yakın şehre gidilir.
3. Tüm şehirler ziyaret edilene kadar devam edilir.
4. Başlangıç şehrine dönülür.

Avantajları:

- basittir,
- hızlıdır,
- ölçeklenebilir,
- başlangıç incumbent'ı üretmek için yararlıdır.

Sınırlamaları:

- yerel olarak cazip kararlar kötü küresel turlara yol açabilir,
- kalite örnek geometrisine ve başlangıç koşullarına bağlıdır,
- genel optimalite garantisi yoktur.

## 2.5 Metasezgiseller — Metaheuristics

Bir **metaheuristic**, aday çözümlerin nasıl üretileceğini, kabul edileceğini, çeşitlendirileceğini ve yoğunlaştırılacağını yöneten üst düzey arama çerçevesidir.

Genel yapı:

```text
başlangıç çözümü/çözümleri
    ↓
aday üretimi
    ↓
değerlendirme
    ↓
kabul / seçim
    ↓
hafıza / adaptasyon / çeşitlendirme
    ↓
durdurma kuralı
```

Tipik amaçlar:

- kötü yerel optimumlardan kaçmak,
- birden fazla arama bölgesini keşfetmek,
- umut verici çözümlerin çevresinde aramayı yoğunlaştırmak,
- exploration ile exploitation'ı dengelemek,
- önceki iterasyonlardan edinilen bilgiyi kullanmak.

Yaygın metasezgiseller:

- Genetic Algorithm,
- Simulated Annealing,
- Tabu Search,
- Particle Swarm Optimization,
- Ant Colony Optimization,
- Differential Evolution,
- Variable Neighborhood Search,
- GRASP,
- Iterated Local Search,
- Scatter Search,
- Evolution Strategies,
- Memetic Algorithms.

### Heuristic ile metaheuristic farkı

| Heuristic | Metaheuristic |
|---|---|
| Çoğunlukla probleme özgüdür | Genellikle yeniden kullanılabilir arama çerçevesidir |
| Doğrudan bir kurma/iyileştirme kuralı ifade eder | Tekrarlı arama sürecini düzenler |
| Tek geçişli olabilir | Çoğunlukla iteratif/adaptiftir |
| Anlık yerel kararlara ağırlık verebilir | Daha geniş arama davranışını açıkça yönetir |
| Örnek: Nearest Neighbor | Örnek: Genetic Algorithm |

Bu sınır her yayında mutlak değildir. Pratikte en yararlı ayrım şudur: metaheuristic, **aramayı kontrol eden algoritmik çerçevedir**; heuristic ise çoğu zaman doğrudan probleme özgü bir kuraldır.

## 2.6 Bu kategoriler arasındaki ilişki

Pratik bir hiyerarşi:

```text
Optimizasyon çözüm yaklaşımları
├── Exact yöntemler
└── Non-exact / approximate yaklaşımlar
    ├── Teorik kalite sınırı olan approximation algoritmaları
    ├── Heuristics
    └── Metaheuristics
```

Ancak terminoloji alana göre değişir. Teorik bilgisayar biliminde “approximation algorithm” özel bir garanti anlamı taşır. Yöneylem araştırması pratiğinde “approximate methods” daha geniş kullanılabilir.

En güvenli yaklaşım, yalnızca etikete güvenmek yerine garantiyi açıkça belirtmektir.

## 2.7 Garantiler raporlanırken ne belirtilmeli?

Bir optimizasyon algoritmasını sunarken şu noktaları açıkça yazın:

- küresel optimalite garantisi var mı,
- garanti hangi varsayımlar altında geçerli,
- sonlanma sonlu zamanda mı yoksa asimptotik mi,
- garanti küresel optimum, yerel optimum veya durağan nokta için mi,
- approximation ratio var mı,
- sayısal feasibility ve optimality toleransları neler,
- sonuç bir ispat/sertifika mı yoksa yalnızca bulunan en iyi incumbent mı.

Bu ayrım, “çok iyi çözüm buldu” ile “optimal olduğunu kanıtladı” ifadelerinin karışmasını engeller.
