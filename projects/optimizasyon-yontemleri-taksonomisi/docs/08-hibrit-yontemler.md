# 8. Hibrit Yöntemler ve Matheuristics

[← Zaman, dağıtım ve modele erişim](07-zaman-dagitim-ve-model-erisimi.md) · [Sonraki: Karşılaştırma matrisi →](09-karsilastirma-matrisi.md)

## 8.1 Exact ve heuristic yöntemler neden birlikte kullanılır?

Exact/heuristic ayrımı kavramsal olarak yararlıdır; ancak gerçek optimizasyon sistemleri çoğu zaman ikisini birlikte kullanır.

Büyük bir mixed-integer problem şunları içerebilir:

- tractable exact subproblem,
- zor bir combinatorial master problem,
- exact aranabilen neighborhoods,
- bilgilendirici bounds veren relaxations,
- güçlü incumbent'ları hızlı üreten domain-specific construction rules.

Hibrit yapı her bileşeni güçlü olduğu yerde kullanabilir.

## 8.2 Matheuristics

Bir **matheuristic**, mathematical programming ile heuristic veya metaheuristic search'ü birleştirir.

Tipik kalıplar:

- Large Neighborhood Search içinde MILP solver kullanmak,
- Genetic Algorithm içinde exact subproblem çözmek,
- çözümün bir kısmını sabitleyip kalan değişkenleri exact optimize etmek,
- relaxation bilgisinden neighborhood tanımlamak,
- heuristic incumbents ile exact solver'ı hızlandırmak.

Temsilci teknikler:

- Local Branching,
- Relaxation Induced Neighborhood Search (RINS),
- Feasibility Pump,
- Fix-and-Optimize,
- Relax-and-Fix,
- exact repair/subproblem solving kullanan Large Neighborhood Search.

## 8.3 Local Branching

Local Branching, incumbent çevresindeki aramayı sınırlandıran bir kısıt ekler ve bu neighborhood'u MILP solver ile exact veya kontrollü toleransta arar.

```text
incumbent çözüm
      ↓
exact matematiksel neighborhood tanımla
      ↓
MILP mekanizmasıyla neighborhood'u çöz
      ↓
incumbent'ı güncelle
      ↓
neighborhood'u taşı / genişlet / yeniden tanımla
```

Bu, exact mekanizmanın heuristic arama stratejisi içine gömülmesinin açık bir örneğidir.

## 8.4 Fix-and-Optimize

Değişkenlerin bir alt kümesi incumbent değerlerine sabitlenir; diğer alt küme yeniden optimize edilir.

Neighborhood, serbest bırakılan değişken bloğu tarafından oluşturulur.

Özellikle şu durumlarda etkili olabilir:

- tam model çok zorsa,
- küçük subproblem'ler çok daha kolaysa,
- problem zaman, lokasyon, ürün, araç veya makine bazında doğal decomposition içeriyorsa.

## 8.5 Relax-and-Fix

Değişkenler bloklara ayrılır. Bazıları integer olarak zorlanır, bazıları önceki kararlardan sabitlenir, sonraki blokların bir kısmı geçici olarak relax edilir.

Yöntem daha küçük problemlerin dizisi üzerinden aşamalı biçimde feasible integer solution kurar.

Büyük planlama ve çizelgeleme modellerinde constructive heuristic olarak sık kullanılır.

## 8.6 Metaheuristic içinde exact subproblem optimization

Bir routing metaheuristic'in bazı müşterileri çözümden çıkarıp yeniden yerleştirdiğini düşünelim. Greedy reinsertion yerine bu alt problem exact çözülebilir.

```text
metaheuristic nerede aranacağını seçer
           +
exact solver o neighborhood içinde optimize eder
```

Genel yöntem yine otomatik olarak exact değildir. Bir subproblem'in exact çözülmesi, tüm hibritin global exactness özelliğini sağlamaz.

## 8.7 Memetic ve hybrid metaheuristics

Hybridization yalnızca mathematical programming ile sınırlı değildir.

Örnekler:

- Genetic Algorithm + Local Search,
- PSO + gradient refinement,
- ACO + 2-opt,
- GA + Tabu Search,
- evolutionary search + exact repair.

Bir hibrit; her bileşeniyle ve **tüm algoritmanın** garantisiyle sınıflandırılmalıdır. En güçlü bileşenin etiketi tüm yönteme otomatik olarak aktarılmaz.

## 8.8 Kritik sınıflandırma kuralı

Bir yöntem exact solver içeriyorsa şu soruyu sorun:

> Tüm dış algoritma geçerli bir global optimality proof'u koruyor mu?

Cevap hayırsa, içeride bir alt problem exact çözülüyor diye tüm yöntem exact olarak adlandırılmamalıdır.

Benzer şekilde bir exact solver içeride primal heuristics kullanabilir ve exact search/certification machinery geçerliliğini koruyorsa solver'ın bütünü yine exact olabilir.

Bu ayrım modern solver mimarilerinde kritiktir; exact ve heuristic bileşenler aynı sistem içinde yoğun biçimde birlikte kullanılır.
