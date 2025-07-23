# Döviz Kurları Takip ve Veri Çekme Uygulaması

Bu proje, Python kullanarak belirlenen döviz kurlarının (örneğin USD, EUR, GBP) bir finansal API aracılığıyla çekilmesini, işlenmesini ve konsolda gösterilmesini sağlar. Yazılım bilgisi olmayan işletmelerin dahi anlık veya geçmiş döviz verilerini takip edebilmesi için tasarlanmıştır.

## Ne Yapar?

* **Güncel Döviz Kurları Çekimi:** Belirtilen para birimlerinin (örneğin Dolar, Euro, Sterlin) en güncel alış/satış kurlarını otomatik olarak çeker.
* **API Entegrasyonu:** Güvenilir bir finansal veri sağlayıcının API'sini kullanarak doğru ve güncel verilere erişim sağlar. (NOT: Bu projede API anahtarı güvenliği için `.env` dosyası kullanılmaktadır.)
* **Konsol Çıktısı:** Çekilen döviz verilerini okunaklı bir formatta doğrudan Python konsolunda görüntüler.

## Neden Önemli?

İşletmeler ve bireyler için döviz kurları, fiyatlandırma, maliyet analizi, uluslararası ticaret ve yatırım kararları açısından kritik öneme sahiptir. Bu uygulama:

* **Zaman Kazandırır:** Manuel olarak döviz kurlarını takip etme zahmetini ortadan kaldırır.
* **Doğruluk Sağlar:** API'ler aracılığıyla doğrudan kaynaklardan güvenilir ve güncel veriye ulaşılır.
* **Anlık Veri Erişimi:** En güncel döviz bilgilerine hızlıca ulaşmanızı sağlar.
