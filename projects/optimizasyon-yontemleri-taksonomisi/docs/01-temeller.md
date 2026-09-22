# 1. Temeller: Optimizasyon Taksonomileri Nasıl Düşünülmeli?

[← README'ye dön](../README.md) · [Sonraki: Çözüm garantileri →](02-cozum-garantileri.md)

## 1.1 Tek bir taksonomi neden yanıltıcıdır?

Sık karşılaşılan bir soru, optimizasyon yöntemlerinin iki büyük sınıfa ayrılıp ayrılamayacağıdır:

- exact / deterministic yöntemler,
- heuristic / metaheuristic yöntemler.

Bu sezginin yararlı tarafı, **garanti sunan yöntemlerle** genel bir optimalite garantisi olmadan iyi çözümler arayan yöntemler arasındaki farkı yakalamasıdır. Yanıltıcı tarafı ise `exact` ile `deterministic` kavramlarını birleştirmesidir.

Bu sözcükler farklı sorulara yanıt verir:

- **Exact:** *Yöntem nihai çözüm hakkında neyi kanıtlayabilir?*
- **Deterministic:** *Aynı girdi ve ayarlarla algoritmayı tekrar çalıştırırsam aynı hesaplama yolu izlenir mi?*
- **Local / global:** *Algoritma ne kadar geniş bir bölgeyi arıyor?*
- **Single-solution / population-based:** *Açıkça kaç aday çözüm tutuluyor?*

Bu nedenle yararlı bir taksonomi bir ağaçtan çok **koordinat sistemi** gibi davranır. Her algoritma birden fazla eksende etiket alır.

## 1.2 Optimizasyon problemi gösterimi

Genel bir kısıtlı minimizasyon problemi şöyle yazılabilir:

```math
\begin{aligned}
\min_{x \in X} \quad & f(x) \\
\text{s.t.} \quad & g_i(x) \le 0, \quad i=1,\ldots,m, \\
& h_j(x)=0, \quad j=1,\ldots,p.
\end{aligned}
```

Burada:

- `x` karar vektörüdür,
- `X` karar değişkenlerinin alanını tanımlar,
- `f(x)` amaç fonksiyonudur,
- `g_i(x)` eşitsizlik kısıtlarıdır,
- `h_j(x)` eşitlik kısıtlarıdır.

Farklı optimizasyon yöntemleri bu problemin farklı yapısal özelliklerinden yararlanır.

## 1.3 En önemli bağımsız eksenler

### Eksen A — çözüm garantisi

Sorular:

- Yöntem optimaliteyi kanıtlıyor mu?
- Alt optimalite için bir sınır veriyor mu?
- Yalnızca bulduğu en iyi çözümü mü döndürüyor?

Tipik etiketler: **exact**, **approximation**, **heuristic**, **metaheuristic**.

### Eksen B — rassallık

Sorular:

- Rassal örnekleme kullanılıyor mu?
- Başlangıç rassal mı?
- Hareket, mutasyon, seçim veya dallanma kararları olasılıksal mı?

Tipik etiketler: **deterministik**, **stokastik/rassallaştırılmış**.

### Eksen C — arama kapsamı

Sorular:

- İyileştirme yalnızca mevcut çözümün komşuluğunda mı yürütülüyor?
- Algoritma arama uzayının birden fazla bölgesini keşfetmek üzere mi tasarlanmış?
- Tüm arama uzayı sistematik biçimde bölünüyor mu?

Tipik etiketler: **yerel**, **küresel**, **küresel arama odaklı**.

### Eksen D — arama temsili

Sorular:

- Tek bir incumbent çözüm mü iteratif olarak güncelleniyor?
- Bir çözüm kümesi veya popülasyonu mu evriliyor?
- Arama bir ağaç, grafik, frontier veya olasılık modeli üzerinden mi temsil ediliyor?

Tipik etiketler: **tek çözüm**, **popülasyon tabanlı**, **ağaç tabanlı**, **model tabanlı** ve benzeri yapılar.

## 1.4 Neden “exact = deterministic” yanlıştır?

Bir exact Branch and Bound uygulamasının, eşit önceliğe sahip dallanma adayları arasında rassal seçim yaptığını düşünelim. Farklı çalıştırmalar arama ağacını farklı sıralarda gezebilir. Buna rağmen yöntem doğru biçimde tamamlanırsa aynı optimumu kanıtlayabilir.

Rassallık **izlenen yolu** değiştirir. Exactness ise **garantiyle** ilgilidir.

Sembolik olarak:

```math
\text{Exact} \not\equiv \text{Deterministic}
```

ve benzer şekilde:

```math
\text{Stochastic} \not\equiv \text{Heuristic}.
```

## 1.5 Bir yöntem aynı anda birçok etikete sahip olabilir

Simulated Annealing:

- metasezgiseldir,
- çoğunlukla stokastiktir,
- tek çözüm tabanlıdır,
- küresel arama odaklıdır,
- klasik biçiminde türevsizdir.

Negatif olmayan kenar ağırlıkları için Dijkstra:

- çözdüğü en kısa yol problemi açısından exact'tır,
- sabit tie-breaking kuralıyla deterministiktir,
- bir grafik algoritmasıdır,
- ilgili problem sınıfında küresel çözümü bulur,
- metasezgisel değildir.

Gradient Descent:

- full-batch biçiminde çoğunlukla deterministiktir,
- yerel/iteratif bir yöntemdir,
- tek çözüm tabanlıdır,
- birinci derece bilgi kullanır,
- küresel minimuma ancak konvekslik ve uygun adım uzunluğu gibi varsayımlar altında yakınsar.

Dolayısıyla yalnızca algoritmanın adı yeterli değildir; **problem varsayımları önemlidir**.

## 1.6 Algoritma sınıflandırması ile model sınıflandırmasını ayırmak

Bir başka yaygın karışıklık, bazı sıfatların **modeli**, bazılarının ise **algoritmayı** tanımlamasıdır.

Örneğin:

- **Deterministik optimizasyon modeli**, parametreleri bilinen sabitler kabul eder.
- **Deterministik algoritma**, algoritmik rassallık kullanmaz.

Bu iki özellik mantıksal olarak bağımsızdır. Deterministik bir algoritma stokastik programlama reformülasyonunu çözebilir; rassallaştırılmış bir algoritma deterministik bir modeli çözebilir.

Benzer şekilde:

- `convex` çoğunlukla problem yapısını,
- `first-order` algoritmanın kullandığı bilgiyi,
- `population-based` algoritmanın temsilini,
- `multi-objective` modelin amaç yapısını

tanımlar.

## 1.7 Pratik bir kural

Bir optimizasyon yöntemini anlatırken şu tür cümlelerden kaçının:

> “Genetic Algorithm stokastik bir optimizasyon algoritmasıdır.”

Bu cümle yanlış değildir; ancak eksiktir. Bunun yerine yapılandırılmış bir tanım tercih edin:

> “Genetic Algorithm, çoğunlukla stokastik operatörler kullanan ve arama uzayını geniş biçimde keşfetmek üzere tasarlanmış, popülasyon tabanlı evrimsel bir metasezgiseldir.”

Rehberin devamı, bu tür tanımları hassas biçimde kurmak için gereken kavramları geliştirir.
