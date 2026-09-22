# 4. Arama Temsili ve Metasezgisel Aileleri

[← Rassallık ve arama](03-rastgelelik-ve-arama.md) · [Sonraki: Problem yapısı →](05-problem-yapisi.md)

## 4.1 Tek çözüm tabanlı yöntemler

Tek çözüm tabanlı bir yöntem, bir ana incumbent veya mevcut çözüm tutar:

```math
x^{(t)} \rightarrow x^{(t+1)}.
```

Örnekler:

- Hill Climbing,
- Simulated Annealing,
- Tabu Search,
- Iterated Local Search,
- Variable Neighborhood Search,
- GRASP içindeki local improvement aşamaları.

Avantajları:

- daha düşük bellek ihtiyacı,
- çoğu zaman daha basit durum yönetimi,
- güçlü yerel iyileştirme,
- problem-özel neighborhood yapılarıyla kolay entegrasyon.

Sınırlamaları:

- aynı anda yalnızca bir arama bölgesi açıkça temsil edilir,
- çeşitliliği korumak zor olabilir,
- zor yerel optimumlardan kaçmak için ek mekanizmalar gerekir.

## 4.2 Popülasyon tabanlı yöntemler

Popülasyon tabanlı yöntem bir aday çözüm kümesi tutar:

```math
P^{(t)} = \{x_1^{(t)},x_2^{(t)},\ldots,x_n^{(t)}\}.
```

Örnekler:

- Genetic Algorithm,
- Differential Evolution,
- Particle Swarm Optimization,
- Evolution Strategies,
- Artificial Bee Colony,
- Scatter Search,
- birçok multi-objective evolutionary algorithm.

Ant Colony Optimization da doğal olarak multi-agent/population-oriented bir yöntemdir; ancak kalıcı arama durumu çoğu zaman yalnızca tutulan çözümlerde değil pheromone bilgisinde temsil edilir.

Avantajları:

- birden fazla arama bölgesi aynı anda temsil edilebilir,
- çeşitlilik mekanizmaları daha doğal uygulanabilir,
- Pareto tabanlı çok amaçlı aramayla uyumludur.

Sınırlamaları:

- iterasyon başına daha fazla objective evaluation,
- daha fazla bellek ve hesaplama maliyeti,
- population collapse veya premature convergence yine mümkündür.

## 4.3 Temsil, stokastiklikle aynı şey değildir

Popülasyon tabanlı yöntemler çoğu zaman stokastiktir; ancak bu bir tanım değildir. Deterministik selection, crossover, mutation veya update kuralları tasarlanabilir.

Tek çözüm tabanlı yöntemler de stokastik olabilir. Simulated Annealing bunun standart örneğidir.

```text
single-solution ≠ deterministic
population-based ≠ stochastic
```

## 4.4 Evrimsel algoritmalar

Evrimsel algoritmalar soyut evrim mekanizmalarını taklit eder.

Tipik operatörler:

- selection,
- recombination / crossover,
- mutation,
- elitism,
- replacement.

Temsilci yöntemler:

- Genetic Algorithm,
- Evolution Strategies,
- Differential Evolution,
- Genetic Programming.

Bunlar çoğunlukla:

- popülasyon tabanlı,
- stokastik,
- türevsiz,
- küresel arama odaklıdır.

Ancak bunlar tipik özelliklerdir; evrensel tanımlar değildir.

## 4.5 Swarm intelligence

Sürü algoritmaları birden fazla ajanın kolektif davranışını modeller.

Örnekler:

- Particle Swarm Optimization,
- Ant Colony Optimization,
- Artificial Bee Colony,
- Firefly Algorithm.

Bilgi paylaşımı yönteme göre değişir:

- PSO, personal/global best durumları üzerinden bilgi paylaşır,
- ACO, pheromone trails üzerinden dolaylı bilgi paylaşır,
- bee-inspired yöntemler ajanlar arasında farklı arama rolleri tanımlar.

Biyolojik metafordan çok altta yatan arama mekanizması önemlidir.

## 4.6 Fiziksel süreçlerden esinlenen yöntemler

Örnekler:

- Simulated Annealing,
- Gravitational Search,
- Electromagnetism-like Optimization.

Analitik açıdan önemli soru “hangi doğal süreçten esinlenmiştir?” değil, şunlardır:

- yeni adaylar nasıl üretiliyor,
- kabul mekanizması nasıl çalışıyor,
- parametreler zamanla nasıl değişiyor,
- hangi yakınsama ifadeleri kurulabiliyor?

## 4.7 Hafıza tabanlı yöntemler

Tabu Search klasik örnektir.

Yakın zamanda kullanılan hareketleri veya özellikleri sınırlandırmak için tabu list gibi hafıza yapıları kullanır. Tipik bileşenler:

- short-term memory,
- aspiration criteria,
- intensification,
- diversification.

Bu yapı onu hafızasız local improvement'tan ayırır.

## 4.8 Komşuluk değiştiren yöntemler

Variable Neighborhood Search (VNS), komşuluk yapılarını sistematik biçimde değiştirir.

Variable Neighborhood Descent (VND), çoğunlukla deterministik bir descent çerçevesinde birden fazla local-search neighborhood'u uygular.

Temel ilke:

> Bir komşuluğa göre yerel optimum olan çözüm, başka bir komşuluğa göre yerel optimum olmak zorunda değildir.

## 4.9 Multi-start ve perturbation yöntemleri

Örnekler:

- Multi-start Local Search,
- GRASP,
- Iterated Local Search.

Genel yapı:

```text
kur / başlat
        ↓
yerel iyileştirme
        ↓
yeniden başlat veya perturb
        ↓
yerel iyileştirme
        ↓
tekrarla
```

Bu yöntemler yerel bir optimizer'ı daha geniş arama stratejisine dönüştürür.

## 4.10 Memetic Algorithms

Memetic Algorithm çoğunlukla evrimsel popülasyon mekanizmasını güçlü yerel iyileştirmeyle birleştirir:

```math
\text{Evolutionary search} + \text{Local search}.
```

Evrimsel bileşen diversification sağlar; local search umut verici bireylerin çevresinde intensification yapar.

## 4.11 “Nature-inspired” neden birincil taksonomi olmamalı?

Algoritmalar kimi zaman metaforlarına göre evolutionary, swarm, physics, biology, chemistry gibi gruplara ayrılır. Tarihsel açıdan yararlı olsa da bu sınıflandırma çoğunlukla hesaplama mekanizmasına göre sınıflandırmadan daha zayıftır.

Ciddi analizde öncelik verilmesi gerekenler:

- garanti,
- temsil,
- neighborhood/operator tasarımı,
- hafıza kullanımı,
- rassallık,
- exploration/exploitation stratejisi,
- parameter adaptation,
- evaluation cost,
- stopping rule.

Davranışı algoritmanın adındaki metafordan çok bu özellikler belirler.
