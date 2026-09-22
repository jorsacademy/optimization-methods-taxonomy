# 6. Kısıtlar, Amaçlar ve Belirsizlik

[← Problem yapısı](05-problem-yapisi.md) · [Sonraki: Zaman, dağıtım ve modele erişim →](07-zaman-dagitim-ve-model-erisimi.md)

## 6.1 Kısıtsız optimizasyon

Kısıtsız problem:

```math
\min_{x\in\mathbb{R}^n} f(x).
```

Değişken alanındaki her nokta biçimsel olarak adaydır. Zorluk açık feasibility constraints'ten değil amaç fonksiyonunun yapısından kaynaklanır.

## 6.2 Kısıtlı optimizasyon

```math
\begin{aligned}
\min \quad & f(x) \\
\text{s.t.}\quad & g_i(x)\le0, \\
& h_j(x)=0.
\end{aligned}
```

Önemli kavram ve yöntemler:

- Lagrange multipliers,
- KKT conditions,
- penalty methods,
- barrier methods,
- interior-point methods,
- Augmented Lagrangian methods,
- feasibility restoration.

## 6.3 Sert kısıtlar — Hard constraints

Hard constraint mutlaka sağlanmalıdır:

```math
x_1+x_2\le100.
```

Kısıtı ihlal eden çözüm infeasible'dır.

Exact mathematical-programming solver'lar model ve sayısal toleranslar doğrultusunda feasibility'yi korur veya yeniden sağlar. Heuristics ise explicit feasibility-preserving operators veya repair mechanisms gerektirebilir.

## 6.4 Yumuşak kısıtlar — Soft constraints

Soft constraint ihlal edilebilir; ancak bir maliyet uygulanır.

```math
F(x)=f(x)+\lambda P(x),
```

burada `P(x)` ihlali, `λ` ise cezanın gücünü ölçer.

Soft constraints, gereksinimler vazgeçilmez kurallar değil tercih olduğunda yararlıdır.

## 6.5 Tek amaçlı optimizasyon

Tek amaçlı model bir skaler kriter optimize eder:

```math
\min f(x).
```

Örnekler:

- maliyeti azaltmak,
- mesafeyi azaltmak,
- makespan'i azaltmak,
- negatif kârı minimize ederek kârı artırmak.

Birden fazla iş kriteri ağırlıklar veya cezalarla tek bir skaler amaçta birleştirilebilir; ancak bu bir modelleme tercihidir.

## 6.6 Çok amaçlı optimizasyon

Bir multi-objective problem birden fazla kriteri optimize eder:

```math
\min
\begin{bmatrix}
f_1(x)\\
f_2(x)\\
\vdots\\
f_k(x)
\end{bmatrix}.
```

Tipik çelişkiler:

- maliyet / hizmet seviyesi,
- kalite / teslim süresi,
- getiri / risk,
- maliyet / karbon emisyonu.

### Pareto dominasyonu

Minimizasyonda `y`, `x`'i domine eder:

```math
f_i(y)\le f_i(x), \qquad \forall i,
```

ve en az bir `j` amacı için:

```math
f_j(y)<f_j(x).
```

Başka bir uygun çözüm tarafından domine edilmeyen çözüm Pareto optimal'dir.

Amaç çoğu zaman tek bir “mutlak en iyi” çözüm değil, **Pareto frontier** elde etmektir.

### Yaygın yaklaşımlar

- Weighted Sum,
- ε-constraint,
- Goal Programming,
- NSGA-II,
- NSGA-III,
- SPEA2,
- MOEA/D,
- Multi-Objective PSO.

## 6.7 Deterministik optimizasyon modelleri

Deterministik model, parametreleri bilinen sabitler kabul eder:

```math
c,\;A,\;b
```

sabit veridir.

Buradaki “deterministik” ifadesi **modeli** tanımlar, algoritmayı değil.

## 6.8 Stokastik optimizasyon modelleri

Stokastik model belirsiz nicelikleri rassal değişkenler olarak temsil eder:

```math
\xi\sim P.
```

Yaygın amaç:

```math
\min_x \mathbb{E}[f(x,\xi)].
```

Başlıca yaklaşımlar:

- two-stage stochastic programming,
- multistage stochastic programming,
- Sample Average Approximation,
- chance-constrained programming.

Stochastic Gradient Descent farklıdır: adındaki “stochastic” esas olarak **algoritmik örnekleme/rassallığı** tanımlar; karar modelindeki belirsizliği değil.

## 6.9 Robust optimization

Robust optimization'da belirsiz parametrelerin bir uncertainty set içinde olduğu varsayılır:

```math
\xi\in U.
```

Basit worst-case formülasyonu:

```math
\min_x \max_{\xi\in U} f(x,\xi).
```

Klasik stochastic optimization ile temel fark:

- stochastic optimization olasılık modeli veya dağılım bilgisi kullanır,
- robust optimization belirlenmiş bir uncertainty set veya ambiguity description'a karşı koruma sağlar.

Distributionally robust optimization gibi daha gelişmiş türler vardır; ancak kavramsal ayrım yine yararlıdır.

## 6.10 Fuzzy optimization

Fuzzy optimization, kesin olmayan hedef veya parametreleri fuzzy sets ve membership functions ile temsil eder.

Örnek ifadeler:

- “maliyet yaklaşık 100 olmalı”,
- “teslim süresi makul ölçüde düşük olmalı”,
- “risk kabul edilebilir seviyede kalmalı”.

Fuzzy optimization, probabilistic uncertainty'den kavramsal olarak farklıdır. Membership grade, zorunlu olarak olasılık değil tatmin/uygunluk derecesidir.

## 6.11 Model belirsizliği ile algoritmik rassallığı karıştırmayın

Dört kombinasyonun tamamı mümkündür:

| Model | Algoritma | Mümkün mü? |
|---|---|---|
| Deterministik | Deterministik | Evet |
| Deterministik | Stokastik | Evet |
| Stokastik | Deterministik | Evet |
| Stokastik | Stokastik | Evet |

Örneğin deterministik bir TSP örneği stokastik Genetic Algorithm ile çözülebilir. Tersine, deterministik bir decomposition algorithm stokastik programlama reformülasyonunu çözebilir.
