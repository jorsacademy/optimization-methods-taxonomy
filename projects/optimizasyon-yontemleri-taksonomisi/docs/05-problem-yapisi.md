# 5. Problem Alanları ve Matematiksel Yapı

[← Arama temsili ve metasezgiseller](04-arama-temsili-ve-metasezgiseller.md) · [Sonraki: Kısıtlar, amaçlar ve belirsizlik →](06-kisitlar-amaclar-ve-belirsizlik.md)

## 5.1 Sürekli optimizasyon

Sürekli karar değişkenleri:

```math
x_i \in \mathbb{R}.
```

Genel problem:

```math
\min_{x\in\mathbb{R}^n} f(x).
```

Yaygın yöntemler:

- Gradient Descent,
- Newton yöntemleri,
- BFGS ve L-BFGS,
- Conjugate Gradient,
- interior-point methods,
- SQP,
- Differential Evolution,
- CMA-ES.

Uygulamalar:

- parametre kestirimi,
- mühendislik tasarımı,
- portföy optimizasyonu,
- optimal control,
- makine öğrenmesi eğitimi.

## 5.2 Ayrık ve tamsayılı optimizasyon

Ayrık değişkenler sonlu veya sayılabilir bir kümeden değer alır:

```math
x_i \in \{0,1\}
```

veya

```math
x_i \in \mathbb{Z}.
```

Uygulamalar:

- çizelgeleme,
- rotalama,
- atama,
- tesis yeri seçimi,
- packing,
- network design.

Tipik yaklaşımlar:

- Branch and Bound,
- Branch and Cut,
- Dynamic Programming,
- Cutting Planes,
- Local Search,
- Tabu Search,
- Genetic Algorithms,
- Ant Colony Optimization.

## 5.3 Karma değişkenli optimizasyon

Karma modeller farklı alanlardan değişkenler içerir:

```math
x\in\mathbb{R}^n, \qquad y\in\mathbb{Z}^m.
```

Önemli sınıflar:

- MILP — Mixed-Integer Linear Programming,
- MINLP — Mixed-Integer Nonlinear Programming,
- MIQP — Mixed-Integer Quadratic Programming,
- mixed-integer convex optimization.

Karma değişken yapısı çoğu zaman decomposition, relaxation ve hybrid exact–heuristic yöntemleri motive eder.

## 5.4 Kombinatoryal optimizasyon

Kombinatoryal çözüm çoğu zaman:

- permutation,
- subset,
- matching,
- graph structure,
- route,
- schedule,
- assignment

biçimindedir.

Örnekler:

- Traveling Salesperson Problem,
- Vehicle Routing Problem,
- Job Shop Scheduling,
- Graph Coloring,
- Set Cover,
- Maximum Clique,
- Assignment Problem.

Arama uzayı permutation'larda:

```math
|X|=n!
```

veya subset'lerde:

```math
|X|=2^n
```

gibi büyüyebilir.

Bu patlayıcı büyüme, tam enumeration'ın neden hızlıca olanaksızlaştığını ve bounding, decomposition, approximation ve heuristic search'ün neden önemli olduğunu açıklar.

## 5.5 Doğrusal optimizasyon

Doğrusal programın amacı ve kısıtları doğrusaldır:

```math
\begin{aligned}
\min \quad & c^T x \\
\text{s.t.}\quad & Ax\le b.
\end{aligned}
```

Uygun bölge konvekstir. Bu nedenle her yerel optimum aynı zamanda küresel optimumdur.

Doğrusal yapı; olgun algoritmaları, duality theory'yi ve güçlü optimality certificates'i mümkün kılar.

## 5.6 Doğrusal olmayan optimizasyon

Bir nonlinear program'da amaç veya en az bir kısıt nonlinear'dır:

```math
\min f(x)
```

subject to

```math
g_i(x)\le 0.
```

Alt sınıflar:

- convex nonlinear optimization,
- nonconvex optimization,
- quadratic optimization,
- polynomial optimization,
- fractional programming,
- nonsmooth optimization,
- black-box optimization.

“Nonlinear” etiketi tek başına hesaplama zorluğu hakkında çok az şey söyler; convexity ve exploitable structure çoğunlukla daha belirleyicidir.

## 5.7 Konveks optimizasyon

`f` fonksiyonu:

```math
f(\lambda x+(1-\lambda)y)
\le
\lambda f(x)+(1-\lambda)f(y),
\qquad 0\le\lambda\le1
```

koşulunu sağlıyorsa konvekstir.

Uygun bölge de konvekse, her yerel minimum küresel minimumdur.

Yaygın yöntem aileleri:

- gradient methods,
- interior-point methods,
- proximal methods,
- subgradient methods,
- yapısal problemler için ADMM.

Konvekslik optimizasyondaki en değerli yapısal özelliklerden biridir; çünkü yerel çıkarımlar küresel garantilere dönüşebilir.

## 5.8 Konveks olmayan optimizasyon

Nonconvex problemler şunları içerebilir:

- birden fazla yerel minimum,
- saddle points,
- bağlantısız uygun bölgeler,
- flat regions,
- zor nonlinear constraints.

Örnek bir nonconvex amaç:

```math
f(x)=x^4-3x^2+x.
```

Olası stratejiler:

- multi-start,
- Basin Hopping,
- Simulated Annealing,
- evolutionary algorithms,
- deterministic global optimization,
- spatial Branch and Bound.

Önemli ayrım, yöntemin yalnızca geniş arama yapması ile gerçekten global optimality certificate sunabilmesi arasındadır.

## 5.9 Kuadratik optimizasyon

Kuadratik amaç:

```math
\min \frac12 x^TQx+c^Tx.
```

`Q \succeq 0` ise amaç konvekstir.

Önemli sınıflar:

- QP,
- QCQP,
- MIQP,
- MIQCP.

Kuadratik yapı; portföy, kontrol, makine öğrenmesi ve birçok mühendislik probleminde görülür.

## 5.10 Türevlenebilir optimizasyon

Gradient ve Hessian bilgisi mevcutsa:

```math
\nabla f(x), \qquad \nabla^2 f(x),
```

verimli yerel aramayı yönlendirebilir.

Örnekler:

- Gradient Descent,
- Newton,
- BFGS,
- SQP.

## 5.11 Türevsiz optimizasyon

Türevler:

- mevcut değilse,
- güvenilir değilse,
- süreksizse,
- çok pahalıysa,
- bir simülatörün arkasında gizliyse

derivative-free yöntemler yararlıdır.

Örnekler:

- Nelder–Mead,
- Pattern Search,
- Powell-type methods,
- Bayesian Optimization,
- evolutionary methods,
- CMA-ES.

## 5.12 Sıfırıncı, birinci ve ikinci derece bilgi

### Sıfırıncı derece

Yalnızca fonksiyon değerlerini kullanır:

```math
f(x).
```

### Birinci derece

Gradient kullanır. Steepest-descent yönü:

```math
d_k=-\nabla f(x_k),
```

güncelleme:

```math
x_{k+1}=x_k+\alpha_k d_k.
```

### İkinci derece

Hessian gibi eğrilik bilgisini kullanır:

```math
x_{k+1}
=
x_k-[\nabla^2 f(x_k)]^{-1}\nabla f(x_k).
```

Newton ve trust-region Newton yöntemleri klasik örneklerdir.

## 5.13 Kara kutu optimizasyonu

Black-box optimization'da iç analitik yapı bilinmeyebilir. Optimizer yalnızca:

```math
x \mapsto f(x)
```

değerlendirmesi yapabilir.

Uygulamalar:

- simulation optimization,
- hyperparameter tuning,
- pahalı mühendislik yazılımları,
- fiziksel deneyler.

Black-box olmak stokastik olmak demek değildir. Kara kutu fonksiyonu deterministik veya gürültülü olabilir.
