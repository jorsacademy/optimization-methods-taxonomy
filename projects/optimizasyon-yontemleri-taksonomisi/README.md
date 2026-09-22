# Optimizasyon Yöntemleri Taksonomisi

Optimizasyon modellerini ve algoritmalarını, birbirinden bağımsız kavramları birbirine karıştırmadan sınıflandırmak için kavram odaklı bir rehber.

Optimizasyon terminolojisi çoğu zaman yöntemler tek bir basit ağaca aitmiş gibi öğretilir: *kesin (exact) / sezgisel (heuristic)*, *deterministik / stokastik* veya *yerel / küresel*. Bu kullanım pratiktir; ancak eksiktir. Bu etiketler **farklı özellikleri** anlatır. Tek bir algoritma aynı anda birden fazla kategoriye ait olabilir.

Bu repo, bu kategoriler için tutarlı bir zihinsel model kurar; sınırlarını açıklar ve yaygın optimizasyon yöntemlerinin nasıl çok boyutlu biçimde sınıflandırılacağını gösterir.

> **Temel fikir:** Optimizasyon yöntemleri tek ve birbirini dışlayan bir taksonomiye zorlanmamalı; birbirinden bağımsız birden fazla eksen üzerinde tanımlanmalıdır.

## Önce öğrenilmesi gereken dört ayrım

1. **Kesin (exact) / kesin olmayan (non-exact)** ayrımı, çözüm garantisinin türünü açıklar.
2. **Deterministik / stokastik** ayrımı, algoritmanın rassallık kullanıp kullanmadığını açıklar.
3. **Yerel / küresel arama** ayrımı, aramanın kapsamını açıklar; elde edilen optimalite garantisini değil.
4. **Tek çözüm / popülasyon tabanlı** ayrımı, aramanın hangi çözüm temsiliyle yürütüldüğünü açıklar.

Dolayısıyla:

- `exact`, `deterministic` demek değildir;
- `stochastic`, `heuristic` demek değildir;
- `global search`, otomatik olarak `global-optimum guarantee` anlamına gelmez;
- `metaheuristic`, otomatik olarak `population-based` demek değildir;
- `deterministic model` ile `deterministic algorithm` aynı kavram değildir.

## Kısa sınıflandırma haritası

| Eksen | Tipik kategoriler | Temel soru |
|---|---|---|
| Çözüm garantisi | Exact, approximation, heuristic, metaheuristic | Çözüm kalitesi veya optimalite hakkında ne garanti edilebilir? |
| Rassallık | Deterministik, stokastik/rassallaştırılmış | Algoritma rassallık kullanıyor mu? |
| Arama kapsamı | Yerel, küresel | Yalnızca bir komşuluk mu aranıyor, yoksa daha geniş bölgeler mi keşfediliyor? |
| Arama temsili | Tek çözüm, popülasyon tabanlı | Tek bir incumbent mı, yoksa birden fazla aday mı tutuluyor? |
| Karar değişkeni alanı | Sürekli, ayrık/tamsayılı, karma, kombinatoryal | Hangi tür kararlar optimize ediliyor? |
| Matematiksel yapı | Doğrusal, doğrusal olmayan, konveks, konveks olmayan, kuadratik, pürüzsüz olmayan, kara kutu | Model hangi yapısal özellikleri sunuyor? |
| Kısıt yapısı | Kısıtsız, kısıtlı, sert, yumuşak | Uygunluk nasıl tanımlanıyor ve korunuyor? |
| Amaç sayısı | Tek amaçlı, çok amaçlı | Tek kriter mi, birden fazla çelişen kriter mi var? |
| Belirsizlik modeli | Deterministik, stokastik, robust, fuzzy | Belirsizlik nasıl temsil ediliyor? |
| Zaman / bilgi | Statik, dinamik, çevrimiçi, gerçek zamanlı | Bilgi veya sistem durumu zamanla değişiyor mu? |
| Hesaplama organizasyonu | Merkezi, dağıtık | Kararlar ve hesaplamalar nerede yürütülüyor? |
| Modele erişim | Model tabanlı, model bağımsız, vekil model tabanlı | Altta yatan sistem hakkında ne kadar bilgi var? |
| Aramayı yönlendiren bilgi | Birinci derece, ikinci derece, türevsiz / sıfırıncı derece | Arama hangi bilgiyi kullanıyor? |

## Önerilen okuma sırası

1. [Temeller: optimizasyon taksonomileri nasıl düşünülmeli?](docs/01-temeller.md)
2. [Çözüm garantileri: exact, approximation, heuristic ve metaheuristic](docs/02-cozum-garantileri.md)
3. [Rassallık, yerel/küresel arama, exploration ve exploitation](docs/03-rastgelelik-ve-arama.md)
4. [Arama temsili ve metasezgisel aileleri](docs/04-arama-temsili-ve-metasezgiseller.md)
5. [Problem alanları ve matematiksel yapı](docs/05-problem-yapisi.md)
6. [Kısıtlar, amaçlar ve belirsizlik](docs/06-kisitlar-amaclar-ve-belirsizlik.md)
7. [Zaman, hesaplama dağıtımı ve modele erişim](docs/07-zaman-dagitim-ve-model-erisimi.md)
8. [Hibrit yöntemler ve matheuristics](docs/08-hibrit-yontemler.md)
9. [Çok boyutlu karşılaştırma matrisi](docs/09-karsilastirma-matrisi.md)
10. [Herhangi bir optimizasyon algoritması nasıl sınıflandırılır?](docs/10-siniflandirma-is-akisi.md)
11. [Yaygın kavram karışıklıkları ve SSS](docs/11-yaygin-kavram-karisikliklari.md)
12. [Algoritma ve yöntem indeksi](docs/12-algoritma-indeksi.md)

## İlk örnek: Genetic Algorithm'ı doğru sınıflandırmak

Genetic Algorithm yalnızca “stokastik bir yöntem” değildir. Daha eksiksiz bir tanım şöyledir:

- **çözüm garantisi:** metasezgisel; genel durumda sonlu sürede optimalite garantisi vermez,
- **rassallık:** çoğunlukla stokastik,
- **arama kapsamı:** küresel arama odaklı,
- **temsil:** popülasyon tabanlı,
- **arama mekanizması:** evrimsel,
- **bilgi gereksinimi:** tipik olarak türevsiz,
- **problem alanı:** sürekli, ayrık, karma veya kombinatoryal problemlere uyarlanabilir.

Diğer algoritmalar için de aynı çok etiketli tanımlama yaklaşımı kullanılmalıdır.

## İkinci örnek: Branch and Bound'ı doğru sınıflandırmak

Branch and Bound tipik olarak:

- **çözüm garantisi:** gerekli varsayımlar altında tamamlanmasına izin verildiğinde exact,
- **rassallık:** çoğunlukla deterministik; ancak rassal dallanma veya eşitlik bozma kuralları kullanılabilir,
- **arama kapsamı:** uygun çözüm uzayını sistematik biçimde bölmesi bakımından küresel,
- **temsil:** popülasyon değil, arama ağacı,
- **problem alanı:** özellikle ayrık, tamsayılı ve küresel optimizasyon modelleri.

Bu nedenle “exact = deterministic” bir tanım değildir. Determinizm bir uygulama özelliğidir; exactness ise bir garanti özelliğidir.

## Bu repoda kullanılan terminoloji

Optimizasyon literatüründeki terminoloji tamamen standart değildir. Bazı kaynaklar *approximate method* ifadesini approximation algoritmaları, sezgiseller ve metasezgiselleri kapsayan geniş bir üst kavram olarak kullanır. Bazı kaynaklar ise özellikle teorik bilgisayar biliminde *approximation algorithm* terimini kanıtlanmış yaklaşım oranına sahip algoritmalar için ayırır.

Bu repo şu pratik terminolojiyi kullanır:

- **Kesin yöntem (Exact method):** Belirtilen varsayımlar altında optimal bir çözümü veya geçerli bir optimalite sertifikasını ortaya koyabilir.
- **Yaklaşım algoritması (Approximation algorithm):** Optimuma göre kanıtlanabilir bir kalite sınırına, örneğin bir yaklaşım oranına sahiptir.
- **Sezgisel (Heuristic):** Genel bir optimalite veya yaklaşım garantisi olmadan iyi bir çözümü verimli biçimde bulmayı amaçlar.
- **Metasezgisel (Metaheuristic):** Exploration ve exploitation dengesini yöneten, farklı problemlere uyarlanabilen üst düzey arama çerçevesidir; çoğunlukla genel bir sonlu-zaman optimalite garantisi vermez.

Terimlerin birbirinin yerine kullanılmaması için bu tanımlar özellikle açık tutulmuştur.

## Kapsam

Rehber; klasik matematiksel programlama, kombinatoryal optimizasyon, sürekli optimizasyon, metasezgiseller, çok amaçlı optimizasyon, robust ve stokastik optimizasyon, çevrimiçi/dinamik optimizasyon, kara kutu optimizasyonu, vekil model yöntemleri, dağıtık optimizasyon ve hibrit exact–heuristic yaklaşımlarını kapsar. Son algoritma indeksi, rehber boyunca adı geçen yöntemleri tek bir aranabilir ekte toplar.

Bu çalışma bir **taksonomi ve kavramsal rehberdir**; yakınsama teorisi, hesaplama karmaşıklığı, sayısal lineer cebir veya solver implementasyonu üzerine tam kapsamlı bir ders kitabının yerine geçmez.

## İngilizce sürüm

Bu repo Türkçe sürümdür.

İngilizce sürüm: https://github.com/jorsacademy/optimization-methods-taxonomy
