# 7. Zaman, Hesaplama Dağıtımı ve Modele Erişim

[← Kısıtlar, amaçlar ve belirsizlik](06-kisitlar-amaclar-ve-belirsizlik.md) · [Sonraki: Hibrit yöntemler →](08-hibrit-yontemler.md)

## 7.1 Statik optimizasyon

Statik bir optimizasyon probleminde veriler çözüm süreci boyunca sabit kabul edilir. Model tek bir karar problemi olarak çözülür.

Bir veri anlık görüntüsünden oluşturulan birçok planlama, tasarım ve kaynak tahsis modeli bu sınıfa girer.

## 7.2 Dinamik optimizasyon

Dinamik optimizasyonda zamanla değişen bir durum vardır:

```math
x_{t+1}=F(x_t,u_t)
```

ve amaç zaman boyunca tanımlanır:

```math
\min \sum_{t=0}^{T} c(x_t,u_t).
```

İlgili yaklaşımlar:

- Dynamic Programming,
- optimal control,
- Model Predictive Control,
- Approximate Dynamic Programming,
- Reinforcement Learning.

Dynamic optimization, kararlar ve durumlar arasındaki zamansal bağ ile ilgilidir; yalnızca “iteratif çalışan algoritma” demek değildir.

## 7.3 Çevrimiçi optimizasyon — Online optimization

Online optimization'da kararlar, gelecekteki tüm bilgi bilinmeden verilir. Yeni bilgi ardışık biçimde gelir.

Örnekler:

- online scheduling,
- real-time pricing,
- traffic routing,
- ad allocation,
- server resource allocation.

Performans alana göre regret, competitive ratio, service level veya gerçekleşen operasyonel maliyet gibi ölçülerle değerlendirilebilir.

## 7.4 Gerçek zamanlı optimizasyon — Real-time optimization

Real-time optimization katı bir hesaplama deadline'ı getirir. Matematiksel olarak daha iyi olsa bile çok geç gelen çözüm operasyonel açıdan değersiz olabilir.

Uygulamalar:

- autonomous control,
- power-grid control,
- industrial process control,
- emergency routing.

Bu durumda doğrudan şu trade-off oluşur:

- çözüm kalitesi,
- robustness,
- computational budget,
- response time.

## 7.5 Merkezi optimizasyon

Centralized optimization'da tam karar problemi merkezi bir optimizer'a gönderilir.

Avantajları:

- global bilgiye erişim,
- daha kolay koordinasyon,
- sistem çapında daha güçlü optimizasyon olasılığı.

Sınırlamaları:

- communication burden,
- scalability constraints,
- single point of failure,
- privacy veya data-governance sorunları.

## 7.6 Dağıtık optimizasyon

Dağıtık problem örneği:

```math
\min \sum_{i=1}^{N} f_i(x_i)
```

ve coupling veya consensus constraints bulunabilir.

Yöntemler:

- ADMM,
- dual decomposition,
- consensus optimization,
- distributed gradient methods,
- federated optimization türleri.

“Distributed”, hesaplama organizasyonunu açıklar; yöntemin exact, heuristic, deterministic veya stochastic olduğunu söylemez.

## 7.7 Model tabanlı yöntemler

Model-based optimizer açık bir matematiksel veya dinamik modele erişebilir.

Örneğin:

```math
x_{t+1}=Ax_t+Bu_t.
```

Bilinen denklemlerden, kısıtlardan, türevlerden veya yapısal özelliklerden yararlanabilir.

## 7.8 Model bağımsız yöntemler

Model-free yaklaşım, sistem dinamiklerinin bilinen açık bir modeline dayanmaz.

Örnekler:

- model-free Reinforcement Learning,
- black-box search,
- evolutionary optimization,
- bandit optimization.

“Model-free” bağlama bağlıdır. Evolutionary algorithm türev veya sistem denklemi gerektirmese bile açık kısıtları ve objective evaluations'ı kullanabilir.

## 7.9 Vekil model tabanlı yöntemler — Surrogate-based methods

Gerçek amaç pahalıysa bir vekil model (surrogate) yaklaşıklar:

```math
\hat f(x) \approx f(x).
```

Olası surrogate modeller:

- Gaussian Processes,
- Random Forests,
- Neural Networks,
- polynomial response surfaces,
- radial basis functions.

Bayesian Optimization önde gelen surrogate-based framework'lerden biridir. Genel döngüsü:

1. surrogate modelin kurulması/güncellenmesi,
2. acquisition function ile bilgilendirici aday seçilmesi,
3. pahalı objective'in değerlendirilmesi,
4. modelin güncellenmesi.

Surrogate-based olmak otomatik olarak stochastic olmak değildir. Surrogate, acquisition function ve onu optimize eden yöntem ayrı ayrı deterministik veya stokastik olabilir.
