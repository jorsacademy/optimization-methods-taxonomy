# 11. Yaygın Kavram Karışıklıkları ve SSS

[← Sınıflandırma iş akışı](10-siniflandirma-is-akisi.md) · [README'ye dön](../README.md)

## Her exact yöntem deterministik midir?

Hayır. Exactness garantiyi, determinism ise rassallık kullanılıp kullanılmadığını tanımlar. Randomized search order, nihai algoritma optimality proof'u koruyorsa exact framework içinde kullanılabilir.

## Her stokastik yöntem heuristic midir?

Hayır. Randomized exact algorithms vardır. Rassallık optimality guarantee'i kaldırmadan computational path'i değiştirebilir.

## Her heuristic stokastik midir?

Hayır. Greedy construction rules ve deterministic local search yaygın deterministik heuristic örnekleridir.

## Her metaheuristic stokastik midir?

Hayır. Yaygın uygulamaların birçoğu stokastiktir; fakat stochasticity tanımın parçası değildir. Tabu Search ve Variable Neighborhood Descent deterministik uygulanabilir.

## Heuristic ve metaheuristic eş anlamlı mı?

Hayır. Heuristic çoğunlukla doğrudan problem-özel bir çözüm kuralıdır. Metaheuristic ise tekrarlı aramayı, diversification ve intensification'ı yöneten daha genel bir framework'tür.

## Approximation algorithm yalnızca başka bir heuristic midir?

Bu rehberde kullanılan teknik anlamda hayır. Approximation algorithm, solution quality için kanıtlanmış bir sınırla gelir. Generic heuristic çoğunlukla böyle bir garanti vermez.

## “Global optimization method” mutlaka global optimumu garanti eder mi?

Hayır. Bazı global optimization methods exact'tır ve global optimumu sertifikalandırır. Bazıları ise geniş arama yapan fakat finite-time certificate vermeyen heuristic/metaheuristic yöntemlerdir.

## Local search mutlaka heuristic midir?

Combinatorial optimization kullanımında çoğunlukla öyledir. Daha genel olarak “local”, arama mekanizmasını açıklar. Özel yapısal varsayımlar altında locally driven yöntemler yine global guarantee verebilir; convex optimization'da her local minimum global minimumdur.

## Gradient Descent global optimumu bulur mu?

Yalnızca uygun varsayımlar altında. Convex objective ve uygun step-size koşullarıyla global convergence sonuçları vardır. Nonconvex problemde Gradient Descent bir stationary point veya local minimuma yakınsayabilir.

## Newton's Method exact midir?

Newton's Method'a açıklamasız biçimde “exact” demek çoğunlukla yararsızdır. İkinci derece iteratif sayısal yöntemdir. Yakınsama davranışı smoothness, initialization, curvature ve problem class'a bağlıdır. Etiket yerine garanti açıkça belirtilmelidir.

## Simplex deterministik midir?

Sabit pivot ve tie-breaking kurallarıyla evet. Farklı pivot rules farklı yollar izleyebilir. Randomized tie-breaking de mümkündür. LP optimality framework bu implementasyon ayrıntısından bağımsızdır.

## Branch and Bound her zaman optimumu döndürür mü?

Doğru bir exact Branch and Bound prosedürü varsayımları altında tamamlanmasına izin verilirse optimaliteyi sertifikalandırabilir. Pratikte solver time limit, node limit veya kabul edilebilir optimality gap nedeniyle erken durdurulabilir. Bu durumda best incumbent'ın optimal olduğu henüz kanıtlanmış değildir.

## Deterministik model yalnızca deterministik algoritmalarla mı çözülür?

Hayır. Deterministik bir optimizasyon modeli stochastic metaheuristic ile çözülebilir.

## Stochastic programming ile stochastic algorithm aynı şey mi?

Hayır.

- **Stochastic programming:** belirsizlik optimizasyon modelinin parçasıdır.
- **Stochastic algorithm:** rassallık çözüm prosedürünün parçasıdır.

Bunlar birbirinden bağımsız olabilir.

## Robust optimization ile stochastic optimization aynı şey mi?

Hayır. Stochastic optimization çoğunlukla olasılık dağılımları veya probabilistic meaning taşıyan scenarios kullanır. Robust optimization ise uncertainty sets veya ambiguity descriptions üzerinden koruma sağlar ve çoğu zaman worst-case protection'ı vurgular.

## Her linear problem convex midir?

Evet. Standart linear objective ve linear constraint sets konvekstir. Ancak her convex problem linear değildir.

## Her quadratic problem convex midir?

Hayır. Quadratic objective, quadratic matrix positive semidefinite ise konvekstir. Indefinite quadratic forms nonconvex'tir.

## Derivative-free ile black-box aynı şey mi?

Tam olarak değil.

- **Derivative-free:** algoritma türev kullanmaz.
- **Black-box:** değerlendirilen sistemin analitik yapısı bilinmez veya bilinçli olarak göz ardı edilir.

Derivative-free yöntem açık bir formüle uygulanabilir. Black-box optimizer ise türevler erişilemediği için çoğunlukla derivative-free olur.

## Bayesian Optimization metaheuristic midir?

Onu **surrogate-based global optimization framework** olarak tanımlamak daha hassastır. Predictive/probabilistic surrogate kurar ve acquisition strategy ile yeni değerlendirmeleri seçer. Metaheuristics ile bazı pratik hedefleri paylaşsa da farklı bir metodolojik aileye aittir.

## Reinforcement Learning bir optimizasyon yöntemi midir?

Reinforcement Learning, policy veya value functions öğrenerek sequential decision problems çözer. Dynamic Programming, stochastic approximation ve optimal control ile kesişir; ancak tüm RL algoritmalarına generic optimization algorithm demek önemli yapıları gizler. Bu rehberde RL, dynamic/model-free decision optimization bağlantısı içinde ele alınır.

## Population method global search'te her zaman daha mı iyidir?

Hayır. Population diversity kaybedebilir ve tek bir bölgeye collapse olabilir. Population size tek başına exploration garantilemez.

## Single-solution method her zaman local mıdır?

Hayır. Simulated Annealing, Iterated Local Search ve Variable Neighborhood Search tek bir ana çözüm tutar; ancak stochastic acceptance, perturbation, memory veya changing neighborhoods sayesinde geniş arama yapabilir.

## Bir heuristic içinde exact solver kullanmak tüm yöntemi exact yapar mı?

Hayır. Tüm dış prosedür ancak geçerli bir global optimality proof'u koruyorsa exact'tır. Exact subproblem optimization tek başına yeterli değildir.

## Heuristics'in hiç teorisi yok mudur?

Hayır. Bir heuristic'in runtime, convergence, probabilistic behavior veya special-case performance hakkında teorik analizi olabilir. Ayırıcı nokta, genel bir optimality veya approximation-ratio guarantee'in tanımlayıcı özellik olmamasıdır.

## Bir algoritmayı tanımlamanın en güvenli yolu nedir?

Birden fazla etiket kullanın ve varsayımları açıkça yazın:

> garanti + rassallık + arama kapsamı + temsil + problem sınıfı + kullanılan bilgi + önemli notlar.

Örneğin:

> “Differential Evolution, özellikle continuous black-box ve global-search-oriented optimization için kullanılan, stokastik, popülasyon tabanlı, derivative-free evrimsel bir metasezgiseldir; sonlu koşumlar normalde global optimality certificate üretmez.”

Bu ifade yönteme tek bir kategori atamaktan çok daha bilgilendiricidir.
