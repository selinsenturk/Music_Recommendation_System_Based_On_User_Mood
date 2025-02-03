# Music_Recommendation_System_Based_On_User_Mood
# 🎵 Kullanıcı Ruh Haline Göre Müzik Öneri Sistemi

Bu proje, müziğin duygusal ve psikolojik sağlıktaki derin etkisinden yararlanarak, bireyin zihinsel durumuna ve müzik tercihlerine dayalı olarak özel müzik önerileri sunan bir sistem geliştirmektedir.

## 📄 Özet

Projede, Spotify, YouTube ve Mental Health & Music Relationship verileri kullanılarak müzik türlerini ve şarkıları analiz edilmiştir. Sistem, kullanıcıların anksiyete, depresyon, uykusuzluk ve OKB (Obsesif Kompulsif Bozukluk) gibi zihinsel durum seviyelerine ilişkin girdilerini ve favori müzik türlerini toplar. Bu verileri temel alan kişiselleştirilmiş müzik önerileri, kullanıcının mevcut duygusal durumuna ve tercihlerine uygun olarak üretilir.

- Kullanıcı, en az bir favori müzik türü seçmeli, en fazla iki tane seçebilir.
- Seçilen koşullara uyulmazsa, sistem öneri sunmaz.
- Kullanıcılar, istediklerinde en fazla 5 şarkı önerisi alabilir.
- Öneriler, YouTube'da dinlenebilen şarkıları içerir.
- Sistem, önerilen şarkıları Twitter'da paylaşmak için tweet atma seçeneği sunar.

## ⚙️ Materyal ve Yöntemler

### 📚 Materyaller
- **Veri Setleri**: 
  - Spotify Verisi
  - YouTube Verisi
  - Mental Health & Music Relationship Verisi
  - https://www.kaggle.com/datasets/catherinerasgaitis/mxmh-survey-results
  - https://www.kaggle.com/datasets/salvatorerastelli/spotify-and-youtube

- **Kütüphaneler**:
  - Pandas, NumPy, Seaborn, Matplotlib, Pyplot, Missingno, Scikit-learn, Tabulate, Streamlit

### 🛠️ Yöntemler
1. **Veri Ön İşleme**:
   - Label Encoder
   - Temel İstatistiksel Analizler
   - Eksik Veri Analizi
   - Korelasyon Analizleri

2. **Platform Karşılaştırmaları**:
   - Spotify ve YouTube Verilerinin Karşılaştırılması

3. **Görselleştirme Teknikleri**:
   - Ruh Hali ve Müzik İlişkisi

4. **Arayüz Tasarımı**:
   - Streamlit ile interaktif arayüz oluşturma

## 📈 Sonuç ve Öneriler
![Müzik Türü Tercihi ve Ortalama Depresyon Seviyesi]("C:\Users\sseli\Desktop\türdepresyon.png")


### 🔍 Sonuçlar
- **Gospel Müzik**: Uykusuzluk ve depresyon seviyelerini düşüren olumlu etkisi vardır.
- **Lofi Müzik**: Anksiyete ve depresyonla mücadele edenler için faydalıdır, 4-6 saat dinlemesi önerilir.
- **Video Oyun Müziği**: Genellikle olumsuz etkiler gösterir, özellikle genç bireylerde.
- **Rock ve Klasik Müzik**: Uykusuzluk ve depresyon için pek tavsiye edilmez.
- **Diğer Müzik Türleri**: R&B, Jazz, K-pop, Country, EDM, Hip hop, Folk ve Latin müzik gibi türler, genellikle mental sağlık üzerinde olumlu etkiler gösterir.
  
- Gençler arasında en popüler akış servisi **Spotify**'dır. Yetişkinler için de Spotify başta gelirken, yaşlılar arasında **YouTube Music** en çok tercih edilen servistir.
- **Müziğin mental sağlık üzerindeki etkisi** %73.5 olarak görülmektedir.
- 12 saatten fazla müzik dinleyenlerin **depresyon seviyeleri** düşüktür, ancak **uykusuzluk seviyesi** değişkenlik gösterir.
- **Anksiyete** değerleri tüm yaş gruplarında yaygın olarak gözlemlenmiş.
- Genç yaş grubunda (özellikle 15-25) anksiyete daha sık görülürken, ileri yaşlarda (55 ve üzeri) anksiyete daha seyrek gözlemlenmiştir.

Mental Sağlık Durumlarına Göre Müzik Tercihleri:

- Uykusuzluk: Gospel ve Lofi müzikleri, uykusuzluk çeken bireyler için rahatlama sağlayabilir ve uyku düzenini iyileştirebilir.
- OCD: Lofi ve Rap müzikleri, OCD seviyeleri yüksek olan bireyler için rahatlatıcı etkiler yapabilir.
- Depresyon: Lofi, Hip hop ve Rock müzikleri, depresyon yaşayan bireylerle daha çok özdeşleşiyor olabilir. Bu müzikler, duygusal bağ kurma ve içsel bir bağlantı sağlama noktasında faydalı olabilir.
- Anksiyete: Anksiyetesi olan bireyler, çeşitli müzik türlerinden rahatlatıcı unsurlar bulabilir. Özellikle Folk, K-pop ve Jazz gibi türler, duygusal rahatlama ve dikkat dağıtma sağlayabilir.

### 💡 Öneriler
- **Dinleme Süreleri**: Müzik öneri sistemleri, dinleme sürelerini de dikkate alarak, belirli türlerin önerilmesi durumunda önerilen süreleri belirtmelidir. Örneğin, Lofi ve Gospel müziği için 4-6 saatlik dinleme süresi önerilebilirken, Video Oyun Müziği için 2 saatten fazla dinlenmemesi gerektiği hatırlatılmalıdır.
- **Eğitim ve Bilinçlendirme**: Bireylerin müzik türlerinin mental sağlık üzerindeki etkileri hakkında bilinçlendirilmesi önemlidir. Bu sayede, bireyler kendi müzik tercihlerini daha sağlıklı bir şekilde yapabilirler.
- **Araştırma ve Geliştirme**: Farklı demografik gruplar üzerinde daha fazla çalışma, müzik öneri sistemlerinin etkinliğini artırabilir.

---
