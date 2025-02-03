import streamlit as st
import pandas as pd
from urllib.parse import quote

import os
workspace_path = "C:/Users/sseli/Desktop/Music_Recommendation_ System_Based_On_User_Mood"

os.chdir(workspace_path)

# Sayfa ayarlarını ilk sırada yapıyoruz
st.set_page_config(page_title="Müzik Öneri Sistemi", page_icon="🎶")

# Veriyi yükleme
df_music = pd.read_csv(r'analiz_sonuclari/df_music_analiz_sonuclari.csv')
df_spotify = pd.read_csv(r'analiz_sonuclari/df_spotify_analiz_sonuclari.csv')

# Müzik türleri ve görselleri
genres = {
    "Classical": r"classical.png",
    "Country": r"country.jpeg",
    "EDM": r"edm.jpg",
    "Folk": r"folk.jpg",
    "Gospel": r"gospel.jpg",
    "Hip Hop": r"hiphop.png",
    "Jazz": r"jazz.jpg",
    "K-pop": r"k-pop.jpg",
    "Latin": r"latin.jpg",
    "Lofi": r"lofi.jpg",
    "Metal": r"metal.jpeg",
    "Pop": r"pop.jpg",
    "R&B": r"r&b.png",
    "Rap": r"rap.jpg",
    "Rock": r"rock.jpg",
    "Video game music": r"videogame.png"
}

# Başlık ve giriş
st.title("🎵 Müzik Öneri Sistemi")
st.markdown("Bu sistem, ruhsal durum seviyelerinize uygun müzik önerileri sunar. Lütfen formu doldurun.")
st.markdown("<h2 style='color:blue;'>Müzik Türleri ve Ruh Halleri</h2>", unsafe_allow_html=True)

# Kullanıcı giriş formu
def get_user_input():
    with st.sidebar:
        st.header("Kullanıcı Tercihleri")
        
        # Ruhsal durum seviyeleri
        st.subheader("Ruhsal Durum Seviyeleri")
        
        anxiety_level = st.slider("😟 Anksiyete seviyesi:", 0, 10, 5)
        depression_level = st.slider("😔 Depresyon seviyesi:", 0, 10, 5)
        insomnia_level = st.slider("😴 Uykusuzluk seviyesi:", 0, 10, 5)
        ocd_level = st.slider("🔄 OKB Seviyesi:", 0, 10, 5)

        # Favori müzik türleri
        st.subheader("Favori Müzik Türleri")
        selected_genres = st.multiselect("Seçmek istediğiniz müzik türlerini seçin:", list(genres.keys())) #multiselect kullanıcının birden fazla seçenek seçmesine olanak tanır.
            
        # Öneri sayısını alma
        num_recommendations = st.number_input("Öneri Sayısı:", min_value=1, max_value=5, value=5 )

    return anxiety_level, depression_level, insomnia_level, ocd_level, selected_genres, num_recommendations

# Tür belirleme fonksiyonu
def determine_genre(selected_genres):
    return selected_genres[0] if selected_genres else None

# Ruhsal durum seviyelerine göre öneri cümleleri
def display_recommendation_text(anxiety_level, depression_level, insomnia_level, ocd_level):
    st.subheader("Ruhsal Durumunuza Göre Öneriler")
    
    if anxiety_level > 7:
        st.markdown("🌿 **Ruh halinizi sakinleştirecek, doğa sesleri ve yumuşak tonlu müzikler öneriyoruz.**")
    elif anxiety_level > 4:
        st.markdown("🧘‍♀️ **Kaygınızı hafifletecek hafif tempolu müzikler dinleyebilirsiniz.**")
    else:
        st.markdown("🌟 **Düşük anksiyete seviyeniz var. Enerjik ve motive edici müzikler sizin için uygun olabilir.**")

    if depression_level > 7:
        st.markdown("⚡ **Enerji verecek, pozitif ve neşeli şarkılarla ruh halinizi yükseltin!**")
    elif depression_level > 4:
        st.markdown("🚀 **Motivasyon artırıcı, sizi iyi hissettirecek müzikler dinleyebilirsiniz.**")
    else:
        st.markdown("😊 **Düşük depresyon seviyeniz var. Neşeli ve eğlenceli müzikler sizin için uygun olabilir.**")

    if insomnia_level > 7:
        st.markdown("😴 **Rahatlatıcı ve uykuya geçişi kolaylaştıracak müzikler öneriyoruz.**")
    elif insomnia_level > 4:
        st.markdown("🌙 **Hafif enstrümantal müzikler ile uyku kalitenizi artırabilirsiniz.**")
    else:
        st.markdown("🌜 **Düşük uykusuzluk seviyeniz var. Rahatlatıcı ancak enerji veren müzikler sizin için uygun olabilir.**")

    if ocd_level > 7:
        st.markdown("🌀 **Odaklanmanızı sağlayacak düzenli ritme sahip müzikler öneriyoruz.**")
    elif ocd_level > 4:
        st.markdown("🎵 **Ruh halinizi dengeleyebilecek akıcı müzikler dinleyebilirsiniz.**")
    else:
        st.markdown("🎶 **Düşük OKB seviyeniz var. Serbest ve çeşitli müzikler sizin için uygun olabilir.**")

# Öneri fonksiyonu
def recommend_music(genre, num_recommendations=10):
    st.subheader("🎧 Önerileriniz Hazırlanıyor...")
    
    # Spotify veri setine göre filtreleme
    if genre == "Classical":
        filtered_songs = df_spotify[df_spotify["Valence"] < 0.3]
    elif genre == "EDM":
        filtered_songs = df_spotify[df_spotify["Danceability"] > 0.8]
    elif genre == "Hip Hop":
        filtered_songs = df_spotify[df_spotify["Energy"] > 0.7]
    elif genre == "Rock":
        filtered_songs = df_spotify[df_spotify["Energy"] > 0.6]
    else:
        filtered_songs = df_spotify.sample(n=10)

    # Öneri bulunamazsa hata mesajı
    if filtered_songs.empty:
        st.error("Seçtiğiniz ruhsal durum seviyelerine uygun müzik bulunamadı.")
        return pd.DataFrame()
    
    # Öneri sayısını sınırlama
    recommended_songs = filtered_songs.sample(n=min(num_recommendations, len(filtered_songs)))

    return recommended_songs[['Track', 'Artist', 'Album', 'Energy', 'Valence', 'Danceability', 'Url_youtube']]

# Dinamik oynatma listesi oluşturma
def create_playlist(recommended_songs):
    st.subheader("🎶 Oynatma Listesi")
    for index, row in recommended_songs.iterrows():
        st.write(f"**Şarkı:** {row['Track']} - **Sanatçı:** {row['Artist']} - **Albüm:** {row['Album']}")
        st.markdown(f"🎵  [Dinle]({row['Url_youtube']})")

def social_media_share(recommended_songs):
    st.subheader("Önerilen Şarkıları Paylaş")
    for index, row in recommended_songs.iterrows():
        # URL kodlama
        track_name = quote(row['Track'])
        youtube_url = row['Url_youtube']

        if pd.notna(youtube_url):  # Eğer YouTube bağlantısı mevcutsa
            st.markdown(
                f"**{row['Track']}**: "
                f"[▶️ Twitter'da Paylaş](https://twitter.com/intent/tweet?text=Bu%20şarkıyı%20dinle:%20{track_name}%20-%20{quote(youtube_url)})"
            )
        else:  # YouTube bağlantısı yoksa
            st.markdown(f"**{row['Track']}**: ▶️ YouTube bağlantısı bulunamadı.")

# Müzik türlerini ve görsellerini gösterme
def display_genres(genres):
    st.subheader("Müzik Türleri")
    cols = st.columns(4)  # 4 sütun oluştur
    for i, (genre, image_path) in enumerate(genres.items()):
        with cols[i % 4]:  # Her sütunda bir müzik türü ve görseli göster
            st.image(image_path, caption=genre, use_container_width=True)

# Ana fonksiyon
def main():
    display_genres(genres)  # Müzik türlerini göster
    anxiety_level, depression_level, insomnia_level, ocd_level, selected_genres, num_recommendations = get_user_input()
    
    # 2'den fazla tür seçildiğinde işlem tamamen durduruluyor
    if len(selected_genres) > 2:
        st.error("En fazla 2 müzik türü seçebilirsiniz! Lütfen seçimlerinizi azaltın.")
        return  # İşlemi sonlandır, aşağıdaki kod çalışmaz

    # Ruhsal durum seviyelerine göre öneri cümlelerini göster
    display_recommendation_text(anxiety_level, depression_level, insomnia_level, ocd_level)

    if selected_genres:
        selected_genre = determine_genre(selected_genres)
        recommended_songs = recommend_music(selected_genre, num_recommendations)
        
        if not recommended_songs.empty:
            create_playlist(recommended_songs)
            social_media_share(recommended_songs)
    else:
        st.warning("Lütfen en az bir müzik türü seçin.")

if __name__ == "__main__":
    main()