# 3. Rassallık, Yerel/Küresel Arama, Exploration ve Exploitation

[← Çözüm garantileri](02-cozum-garantileri.md) · [Sonraki: Arama temsili ve metasezgiseller →](04-arama-temsili-ve-metasezgiseller.md)

## 3.1 Deterministik algoritmalar

Bir deterministik algoritma; girdi, başlangıç durumu ve parametreler aynı olduğunda, tie-breaking ve yürütme de deterministikse aynı hesaplama mantığını izler.

```math
(x^{(0)},\theta) \longrightarrow x^{(1)} \longrightarrow \cdots \longrightarrow x^{(T)}.
```

Tüm koşullar sabitken tekrar çalıştırmalar aynı yolu ve sonucu yeniden üretir.

Örnekler:

- sabit pivot kuralıyla Simplex,
- sabit tie-breaking ile Dijkstra,
- full-batch Gradient Descent,
- deterministik greedy algoritmalar,
- deterministik local search,
- sabit branching/node-selection kurallarıyla Branch and Bound,
- Hungarian Algorithm.

Deterministik olmak şu anlamlara **gelmez**:

- exact olmak,
- küresel optimal olmak,
- polinom zamanda çalışmak,
- hızlı olmak,
- başlangıç noktasına dayanıklı olmak.

Deterministik bir local search her çalıştırmada aynı kötü yerel optimuma yakınsayabilir.

## 3.2 Stokastik veya rassallaştırılmış algoritmalar

Bir stokastik algoritma, arama sürecinin en az bir kısmında rassallık kullanır.

```math
x^{(t+1)} \sim P(\cdot \mid x^{(t)}).
```

Bu nedenle farklı çalıştırmalar farklı yörüngeler ve çözümler üretebilir.

Örnekler:

- Genetic Algorithm,
- Simulated Annealing,
- Differential Evolution,
- Particle Swarm Optimization,
- Ant Colony Optimization,
- Random Search,
- Stochastic Gradient Descent,
- randomized rounding.

### Rassallık neden yararlıdır?

Rassallık:

- yerel optimumlardan kaçmaya,
- çeşitliliği korumaya,
- bağlantısız veya düzensiz bölgeleri keşfetmeye,
- tek bir deterministik yola aşırı bağımlılığı azaltmaya,
- enumerate edilemeyecek kadar büyük uzayları örneklemeye

yardımcı olabilir.

### Rassallık neden özel değerlendirme gerektirir?

Tek bir stokastik koşum, performansı karakterize etmek için çoğunlukla yetersizdir. Uygun olduğunda şunları raporlayın:

- bağımsız koşum sayısı,
- random seed'ler,
- ortalama,
- medyan,
- standart sapma veya başka yayılım ölçüsü,
- en iyi ve en kötü değer,
- çalışma süresi veya evaluation budget,
- başarı / hedefe ulaşma oranı,
- durdurma kriterleri.

Deney protokolü özel olarak gerekçelendirmiyorsa yalnızca en iyi koşumu raporlamaktan kaçının.

## 3.3 Randomized exact yöntemler

Rassallık ile exactness uyumludur.

Bir exact framework şu işlemlerde rassal seçim kullanabilir:

- branching order,
- tie-breaking,
- cut selection,
- primal heuristic timing,
- restarts,
- initialization.

Exact mekanizma arama uzayını doğru biçimde taramaya veya sınırlandırmaya devam ediyor ve sonunda optimaliteyi kanıtlıyorsa, rassallık garantiyi değil hesaplama yolunu değiştirir.

Bu, şu yanlış özdeşliğe en açık karşı örnektir:

```math
\text{Exact} = \text{Deterministic}.
```

Bunlar bağımsız özelliklerdir.

## 3.4 Yerel arama

`N(x)`, `x` çözümünün komşuluğu olsun:

```math
N(x)=\{y : y \text{, } x \text{'in komşusu kabul edilir}\}.
```

Bu komşuluğa göre yerel minimum:

```math
f(x^*) \le f(y), \qquad \forall y\in N(x^*).
```

koşulunu sağlar.

Bu, `x^*` çözümünün tüm uygun bölge üzerinde küresel optimum olduğu anlamına gelmez.

Yaygın yerel veya yerel olarak yönlendirilen yöntemler:

- Hill Climbing,
- Local Search,
- 2-opt ve 3-opt,
- Coordinate Descent,
- Gradient Descent,
- Newton türü yöntemler,
- Hooke–Jeeves,
- Nelder–Mead.

Sürekli bir yerel yöntemin küresel optimumu bulup bulamayacağı problem yapısına güçlü biçimde bağlıdır. Konveks optimizasyonda her yerel minimum küreseldir. Konveks olmayan optimizasyonda yerel davranış gerçek bir sınırlama olabilir.

## 3.5 Küresel arama

Küresel optimizasyon yöntemi, yalnızca tek bir yerel komşuluğa değil daha geniş uygun bölgeye ilişkin çıkarım yapmaya veya bu bölgeyi keşfetmeye çalışır.

Küresel minimum:

```math
f(x^*) \le f(x), \qquad \forall x\in X.
```

Ancak **global search** ifadesi, garanti açıkça belirtilmedikçe belirsizdir.

### Exact global yöntemler

Örnekler:

- spatial Branch and Bound,
- geçerli relaxations kullanan deterministic global optimization,
- uygun varsayımlar altında interval methods.

Bunlar küresel optimalite sertifikası sunabilir.

### Küresel arama odaklı metasezgiseller

Örnekler:

- Simulated Annealing,
- Genetic Algorithm,
- Differential Evolution,
- Particle Swarm Optimization,
- Basin Hopping,
- multi-start yöntemler.

Bunlar birden fazla havzayı veya bölgeyi keşfetmek üzere tasarlanır; ancak sonlu bir koşum çoğunlukla küresel optimumu sertifikalandırmaz.

Dolayısıyla:

> **global-search davranışı ≠ global-optimum garantisi**.

## 3.6 Exploration ve exploitation

Metasezgiseller çoğu zaman iki davranış arasındaki dengeyle açıklanır.

### Exploitation / intensification — yoğunlaştırma

Bilinen umut verici bölgelerin çevresinde derin arama yapılır.

Örnekler:

- local improvement,
- elite preservation,
- incumbent çevresinde neighborhood search,
- gradient-based refinement,
- yüksek kaliteli çözümler arasında path relinking.

Aşırı exploitation erken yakınsamaya veya aynı havzada tekrar tekrar sıkışmaya neden olabilir.

### Exploration / diversification — çeşitlendirme

Yeni veya az keşfedilmiş bölgeler aranır.

Örnekler:

- mutation,
- randomized restart,
- large neighborhood moves,
- diversity-preserving selection,
- subpopulation migration,
- perturbation mechanisms.

Aşırı exploration ise iyi bölgelerin yeterince geliştirilmesini engelleyebilir.

Tasarım problemi şu dengedir:

```math
\text{Exploration} \longleftrightarrow \text{Exploitation}.
```

## 3.7 Local/global ile exploration/exploitation aynı şey değildir

Bir yöntem hareket bazında yerel olabilir; ancak restarts, memory veya perturbations sayesinde geniş bir arama yapabilir. Variable Neighborhood Search, Iterated Local Search ve multi-start local search bunun örnekleridir.

Tersine, popülasyon tabanlı bir yöntem çeşitliliğini kaybederek erken yakınsama sonrasında neredeyse yerel davranabilir.

Bu nedenle hem:

- **tek tek hareketlerin mekaniğini**,
- hem de **tüm algoritmanın oluşturduğu genel arama davranışını**

tanımlamak gerekir.
