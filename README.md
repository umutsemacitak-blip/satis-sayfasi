<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UMEA Projeleri ve Hizmetleri</title>
    <style>
        /* Genel Sayfa Stilleri */
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background-color: #f0f2f5;
            color: #333;
            margin: 0;
            padding: 20px;
        }

        /* Ana Başlık */
        .main-title {
            text-align: center;
            color: #1a237e;
            margin-bottom: 40px;
        }

        /* Kart Konteyneri (Grid Yapısı) */
        .card-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 25px;
            max-width: 1400px;
            margin: auto;
        }

        /* Ana Kart Stili */
        .card {
            background-color: #ffffff;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            padding: 25px;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            overflow: hidden;
        }

        .card.clickable {
            cursor: pointer;
        }

        .card.clickable:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.12);
        }

        .card-title {
            font-size: 1.4em;
            font-weight: 600;
            color: #1a237e;
            margin-top: 0;
            margin-bottom: 15px;
        }
        
        .card-icon {
            font-size: 1.2em;
            margin-right: 8px;
        }

        .card-content {
            font-size: 1em;
            line-height: 1.6;
        }

        .contact-info {
            margin-top: 20px;
            font-weight: bold;
            color: #d81b60;
        }

        /* Alt Kartların Bulunduğu Gizli Alan */
        .sub-card-container {
            display: none; /* Başlangıçta gizli */
            margin-top: 20px;
            padding-top: 20px;
            border-top: 1px solid #eee;
        }

        /* Alan Adı ve Yardım Kartları için Grid Yapısı */
        .sub-card-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
        }
        
        /* Alt Kart Stili */
        .sub-card {
            background-color: #f8f9fa;
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            padding: 20px;
            text-align: center;
            transition: background-color 0.3s;
        }
        
        .sub-card.domain-card {
            cursor: pointer;
        }

        .sub-card:hover {
            background-color: #e9ecef;
        }

        .sub-card-title {
            font-size: 1.2em;
            font-weight: bold;
            color: #0d47a1;
        }
        
        .sub-card-brand-value {
            font-style: italic;
            color: #555;
            margin: 10px 0;
            min-height: 40px; /* Sabit yükseklik */
        }

        .sub-card-price {
            font-size: 1.5em;
            font-weight: bold;
            color: #2e7d32;
            margin-top: 15px;
        }

        /* Modal (Alan Adı Detay Penceresi) */
        .modal {
            display: none; /* Başlangıçta gizli */
            position: fixed;
            z-index: 1000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            overflow: auto;
            background-color: rgba(0,0,0,0.6);
            padding-top: 60px;
        }

        .modal-content {
            background-color: #fefefe;
            margin: 5% auto;
            padding: 30px;
            border: 1px solid #888;
            width: 80%;
            max-width: 700px;
            border-radius: 12px;
            animation: fadeIn 0.5s;
        }
        
        .modal-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid #ddd;
            padding-bottom: 15px;
            margin-bottom: 20px;
        }
        
        .modal-title {
            color: #1a237e;
            font-size: 1.8em;
            margin: 0;
        }

        .close-button {
            color: #aaa;
            font-size: 28px;
            font-weight: bold;
            cursor: pointer;
        }

        .close-button:hover,
        .close-button:focus {
            color: black;
        }
        
        .seo-details h3 {
            color: #d81b60;
        }

        @keyframes fadeIn {
            from {opacity: 0;}
            to {opacity: 1;}
        }
    </style>
</head>
<body>

    <h1 class="main-title">UMEA | Dijital Çözümler ve Sosyal Sorumluluk</h1>

    <div class="card-container">
        <div class="card clickable" onclick="toggleSubCards('domain-sub-cards')">
            <h2 class="card-title"><span class="card-icon">🌐</span>ALAN ADI SATIŞLARIMIZ</h2>
            <div class="card-content">
                Marka değeri yüksek, SEO uyumlu ve projelendirmeye hazır premium alan adlarımız. Detayları görmek için tıklayın.
            </div>
            <div id="domain-sub-cards" class="sub-card-container">
                <div class="sub-card-grid">
                    <div class="sub-card domain-card" onclick="openModal('modal1')">
                        <h3 class="sub-card-title">turkiyegezi.com</h3>
                        <p class="sub-card-brand-value">Türkiye'nin turizm potansiyelini yansıtan jenerik ve akılda kalıcı isim.</p>
                        <div class="sub-card-price">₺250.000</div>
                    </div>
                    <div class="sub-card domain-card" onclick="openModal('modal2')">
                        <h3 class="sub-card-title">finanscepte.net</h3>
                        <p class="sub-card-brand-value">Finans ve ekonomi haberleri için güvenilir ve pratik bir marka kimliği.</p>
                        <div class="sub-card-price">₺180.000</div>
                    </div>
                    <div class="sub-card domain-card" onclick="openModal('modal3')">
                        <h3 class="sub-card-title">yapayzekaokulu.org</h3>
                        <p class="sub-card-brand-value">Eğitim ve teknoloji alanında otoriter bir isim. Geleceğin projesi.</p>
                        <div class="sub-card-price">₺350.000</div>
                    </div>
                    <div class="sub-card domain-card" onclick="openModal('modal4')">
                        <h3 class="sub-card-title">saglikliyemekler.co</h3>
                        <p class="sub-card-brand-value">Sağlıklı yaşam ve beslenme trendlerine uygun, popüler bir niş.</p>
                        <div class="sub-card-price">₺150.000</div>
                    </div>
                    <div class="sub-card domain-card" onclick="openModal('modal5')">
                        <h3 class="sub-card-title">e-ticaretuzmani.com</h3>
                        <p class="sub-card-brand-value">E-ticaret danışmanlığı ve hizmetleri için profesyonel bir kimlik.</p>
                        <div class="sub-card-price">₺120.000</div>
                    </div>
                     <div class="sub-card domain-card" onclick="openModal('modal6')">
                        <h3 class="sub-card-title">oyunforumu.net</h3>
                        <p class="sub-card-brand-value">Geniş kitlelere hitap eden, oyun topluluğu için ideal bir platform.</p>
                        <div class="sub-card-price">₺90.000</div>
                    </div>
                     <div class="sub-card domain-card" onclick="openModal('modal7')">
                        <h3 class="sub-card-title">kriptopara.info</h3>
                        <p class="sub-card-brand-value">Kripto para piyasası hakkında bilgilendirici içerikler için mükemmel.</p>
                        <div class="sub-card-price">₺200.000</div>
                    </div>
                     <div class="sub-card domain-card" onclick="openModal('modal8')">
                        <h3 class="sub-card-title">modatrendleri.tv</h3>
                        <p class="sub-card-brand-value">Moda dünyasına yönelik görsel ve dinamik içerikler için ideal.</p>
                        <div class="sub-card-price">₺160.000</div>
                    </div>
                </div>
            </div>
        </div>

        <div class="card">
            <h2 class="card-title"><span class="card-icon">💰</span>İŞLETMENİZ ARTIK PARA KAZANSIN</h2>
            <div class="card-content">
                Dijital dünyada işletmenizin potansiyelini tam olarak kullanmıyor olabilirsiniz. Gelirinizi artıracak, müşteri sadakati oluşturacak ve marka bilinirliğinizi zirveye taşıyacak özel stratejilerimizle tanışın. Size özel yol haritasını birlikte çizelim.
                <p class="contact-info">Detaylı bilgi ve analiz için bizimle iletişime geçin.</p>
            </div>
        </div>

        <div class="card">
            <h2 class="card-title"><span class="card-icon">📈</span>SOSYAL MEDYADA UMEA ALGORİTMASI İLE FENOMEN OLUN</h2>
            <div class="card-content">
                Sıradan paylaşımlarla kalabalıkta kaybolmayın. UMEA'nın geliştirdiği özel içerik ve etkileşim algoritması ile hedef kitlenize nokta atışı yapın, organik büyümenin keyfini çıkarın ve sosyal medyada bir fenomene dönüşün. Etkileşim rekorları kırmaya hazır mısınız?
                <p class="contact-info">Algoritmamız hakkında bilgi almak için arayınız.</p>
            </div>
        </div>

        <div class="card">
            <h2 class="card-title"><span class="card-icon">🎯</span>GOOGLE'DA REKLAM MI ÇIKMAK İSTİYORSUNUZ?</h2>
            <div class="card-content">
                Doğru yerdesiniz. Bütçenizi boşa harcayan etkisiz reklamlara son! Maksimum dönüşüm ve minimum maliyet ilkesiyle çalışan uzman ekibimiz, anahtar kelime analizinden kampanya optimizasyonuna kadar her adımda yanınızda. Rakiplerinizden bir adım öne çıkın.
                <p class="contact-info">Ücretsiz kampanya analizi için hemen arayın.</p>
            </div>
        </div>
        
        <div class="card">
            <h2 class="card-title"><span class="card-icon">🤖</span>ŞİRKETİNİZE ÖZEL YAPAY ZEKA CHATBOT MU İSTİYORSUNUZ?</h2>
            <div class="card-content">
                Doğru yerdesiniz. Müşteri hizmetleri maliyetlerinizi düşürürken, 7/24 kesintisiz destek sunarak müşteri memnuniyetini artırın. Sıkça sorulan soruları yanıtlayan, sipariş takibi yapan ve potansiyel müşterileri satışa yönlendiren akıllı chatbot'lar ile işinizi otomatikleştirin.
                <p class="contact-info">Size özel chatbot demosu için bizimle iletişime geçin.</p>
            </div>
        </div>

        <div class="card">
            <h2 class="card-title"><span class="card-icon">🚀</span>ŞİRKETİNİZ ZOR DURUMDA MI? UMEA KALKINDIRMA PROJESİ</h2>
            <div class="card-content">
                Doğru yerdesiniz. Finansal darboğazlar, pazar payı kaybı veya verimsizlik... Sorun ne olursa olsun, UMEA Kalkındırma Projesi ile yanınızdayız. Durum analizi, kriz yönetimi, yeniden yapılanma ve büyüme stratejileri ile şirketinizi tekrar ayağa kaldıralım.
                <p class="contact-info">Gizlilik esastır. Çözüm için ilk adımı atın, arayın.</p>
            </div>
        </div>
        
        <div class="card">
            <h2 class="card-title"><span class="card-icon">😊</span>BEN HER ŞEYİ İSTİYORUM MU DİYORSUNUZ? [TEBESSÜM KARTI]</h2>
            <div class="card-content">
                Alan adından yapay zekaya, sosyal medyadan kalkınma projelerine kadar tüm hizmetlerimizi bir arada, size özel bir paketle sunalım. Dijital dünyadaki tüm ihtiyaçlarınız için tek ve güçlü bir çözüm ortağı arıyorsanız, bu kart tam size göre. Hayalinizdeki başarıya birlikte ulaşalım.
                <p class="contact-info">Size özel "Hepsi Bir Arada" teklifimiz için hemen iletişime geçin.</p>
            </div>
        </div>
        
        <div class="card clickable" onclick="toggleSubCards('help-sub-cards')">
            <h2 class="card-title"><span class="card-icon">❤️</span>ANNELERİMİZE VE İHTİYAÇ SAHİPLERİNE YARDIM</h2>
            <div class="card-content">
                Topluma değer katmak bizim için bir görev. Bu bölümden yapacağınız her alışveriş, doğrudan ihtiyaç sahibi ailelere ve annelerimize umut olacaktır. İyilik paylaştıkça çoğalır. Destekleriniz için minnettarız. Ürünleri görmek için tıklayın.
            </div>
            <div id="help-sub-cards" class="sub-card-container">
                <div class="sub-card-grid">
                    <div class="sub-card"><h3 class="sub-card-title">Eğitim Desteği</h3><p class="sub-card-price">₺100</p></div>
                    <div class="sub-card"><h3 class="sub-card-title">Gıda Kolisi</h3><p class="sub-card-price">₺250</p></div>
                    <div class="sub-card"><h3 class="sub-card-title">Kışlık Giysi</h3><p class="sub-card-price">₺150</p></div>
                    <div class="sub-card"><h3 class="sub-card-title">Kırtasiye Seti</h3><p class="sub-card-price">₺120</p></div>
                    <div class="sub-card"><h3 class="sub-card-title">Anne Bebek Paketi</h3><p class="sub-card-price">₺300</p></div>
                    <div class="sub-card"><h3 class="sub-card-title">Sıcak Bir Çorba</h3><p class="sub-card-price">₺50</p></div>
                    <div class="sub-card"><h3 class="sub-card-title">Fatura Desteği</h3><p class="sub-card-price">₺200</p></div>
                    <div class="sub-card"><h3 class="sub-card-title">Sağlık Desteği</h3><p class="sub-card-price">₺350</p></div>
                    <div class="sub-card"><h3 class="sub-card-title">Oyuncak Bağışı</h3><p class="sub-card-price">₺80</p></div>
                    <div class="sub-card"><h3 class="sub-card-title">Barınma Desteği</h3><p class="sub-card-price">₺500</p></div>
                    <div class="sub-card"><h3 class="sub-card-title">Okul Çantası</h3><p class="sub-card-price">₺130</p></div>
                    <div class="sub-card"><h3 class="sub-card-title">Hijyen Kiti</h3><p class="sub-card-price">₺100</p></div>
                    <div class="sub-card"><h3 class="sub-card-title">Ulaşım Desteği</h3><p class="sub-card-price">₺70</p></div>
                    <div class="sub-card"><h3 class="sub-card-title">Bayram Harçlığı</h3><p class="sub-card-price">₺150</p></div>
                    <div class="sub-card"><h3 class="sub-card-title">Kitap Seti</h3><p class="sub-card-price">₺90</p></div>
                    <div class="sub-card"><h3 class="sub-card-title">Meslek Edindirme Kursu</h3><p class="sub-card-price">₺750</p></div>
                    <div class="sub-card"><h3 class="sub-card-title">Engelli Birey Desteği</h3><p class="sub-card-price">₺400</p></div>
                    <div class="sub-card"><h3 class="sub-card-title">Yaşlı Bakım Desteği</h3><p class="sub-card-price">₺300</p></div>
                    <div class="sub-card"><h3 class="sub-card-title">Sokak Hayvanları Mama</h3><p class="sub-card-price">₺60</p></div>
                    <div class="sub-card"><h3 class="sub-card-title">Genel Bağış</h3><p class="sub-card-price">Serbest</p></div>
                </div>
            </div>
        </div>
    </div>
    
    <div id="modal1" class="modal">
        <div class="modal-content">
            <div class="modal-header">
                <h2 class="modal-title">turkiyegezi.com</h2>
                <span class="close-button" onclick="closeModal('modal1')">&times;</span>
            </div>
            <div class="seo-details">
                <h3>SEO ve Marka Değeri Analizi</h3>
                <p><strong>Jenerik ve Akılda Kalıcı:</strong> "Türkiye Gezi" kelimeleri, seyahat ve turizm sektöründe en çok aranan anahtar kelimelerdendir. Bu, doğrudan organik trafik potansiyeli sağlar.</p>
                <p><strong>Arama Motoru Otoritesi:</strong> Alan adı yaşı ve temiz geçmişi sayesinde Google'da hızlı bir şekilde otorite kazanmaya müsaittir.</p>
                <p><strong>Proje Potansiyeli:</strong> Otel rezervasyon sitesi, gezi blogu, turizm acentesi veya şehir rehberleri gibi birçok farklı proje için mükemmel bir temel oluşturur.</p>
            </div>
        </div>
    </div>
    <div id="modal2" class="modal">
        <div class="modal-content">
             <div class="modal-header">
                <h2 class="modal-title">finanscepte.net</h2>
                <span class="close-button" onclick="closeModal('modal2')">&times;</span>
            </div>
            <div class="seo-details">
                <h3>SEO ve Marka Değeri Analizi</h3>
                <p><strong>Hedef Kitleye Uygunluk:</strong> "Finans Cepte", mobil uyumlu ve hızlı erişilebilir bir finans portalı imajı çizer. Bu, günümüz kullanıcı alışkanlıkları için kritiktir.</p>
                <p><strong>Anahtar Kelime Gücü:</strong> "Finans", "cepte" gibi kelimeler, ekonomi haberleri, borsa ve yatırım uygulamaları arayan kullanıcılar için yüksek alaka düzeyine sahiptir.</p>
            </div>
        </div>
    </div>
    <div id="modal3" class="modal"><div class="modal-content"><div class="modal-header"><h2 class="modal-title">yapayzekaokulu.org</h2><span class="close-button" onclick="closeModal('modal3')">&times;</span></div><div class="seo-details"><h3>SEO ve Marka Değeri Analizi</h3><p><strong>Otoriter Uzantı:</strong> ".org" uzantısı, eğitim ve organizasyonel yapılar için Google tarafından güvenilir kabul edilir. Bu, SEO'da önemli bir avantajdır.</p><p><strong>Geleceğin Sektörü:</strong> Yapay zeka, en popüler ve geleceği en parlak teknoloji alanıdır. Bu alanda bir eğitim platformu için biçilmiş kaftandır.</p></div></div></div>
    <div id="modal4" class="modal"><div class="modal-content"><div class="modal-header"><h2 class="modal-title">saglikliyemekler.co</h2><span class="close-button" onclick="closeModal('modal4')">&times;</span></div><div class="seo-details"><h3>SEO ve Marka Değeri Analizi</h3><p><strong>Popüler Niş:</strong> "Sağlıklı yemekler", "diyet tarifleri" gibi aramalar sürekli yüksek hacimlidir. Bu alan adı, bu aramalarda üst sıralara çıkma potansiyeli taşır.</p><p><strong>Markalaşma Kolaylığı:</strong> Kısa, net ve anlaşılır bir isimdir. Sosyal medya ve diğer platformlarda kolayca markalaşabilir.</p></div></div></div>
    <div id="modal5" class="modal"><div class="modal-content"><div class="modal-header"><h2 class="modal-title">e-ticaretuzmani.com</h2><span class="close-button" onclick="closeModal('modal5')">&times;</span></div><div class="seo-details"><h3>SEO ve Marka Değeri Analizi</h3><p><strong>Profesyonel İmaj:</strong> Hizmet odaklı ve uzmanlık belirten bir alan adıdır. B2B (şirketten şirkete) pazarlama için çok güçlüdür.</p><p><strong>Yüksek Değerli Trafik:</strong> Bu alan adına gelecek trafik, doğrudan e-ticaret hizmeti veya danışmanlığı arayan potansiyel müşterilerden oluşur.</p></div></div></div>
    <div id="modal6" class="modal"><div class="modal-content"><div class="modal-header"><h2 class="modal-title">oyunforumu.net</h2><span class="close-button" onclick="closeModal('modal6')">&times;</span></div><div class="seo-details"><h3>SEO ve Marka Değeri Analizi</h3><p><strong>Topluluk Oluşturma:</strong> "Forum" kelimesi, kullanıcıların içerik ürettiği ve etkileşimde bulunduğu bir topluluk sitesi için idealdir.</p><p><strong>Geniş Kitle:</strong> Oyun sektörü, milyonlarca aktif kullanıcıya sahiptir. Bu alan adı, bu geniş kitleye hitap etmek için mükemmel bir başlangıçtır.</p></div></div></div>
    <div id="modal7" class="modal"><div class="modal-content"><div class="modal-header"><h2 class="modal-title">kriptopara.info</h2><span class="close-button" onclick="closeModal('modal7')">&times;</span></div><div class="seo-details"><h3>SEO ve Marka Değeri Analizi</h3><p><strong>Bilgilendirici Uzantı:</strong> ".info" uzantısı, bilgi ve rehber içerikli siteler için uygundur. Google bu tür siteleri referans kaynak olarak görebilir.</p><p><strong>Yüksek Aranma Hacmi:</strong> "Kripto para" anahtar kelimesi, finans dünyasında en çok aranan terimlerden biridir.</p></div></div></div>
    <div id="modal8" class="modal"><div class="modal-content"><div class="modal-header"><h2 class="modal-title">modatrendleri.tv</h2><span class="close-button" onclick="closeModal('modal8')">&times;</span></div><div class="seo-details"><h3>SEO ve Marka Değeri Analizi</h3><p><strong>Görsel Odaklılık:</strong> ".tv" uzantısı, video, galeri ve görsel içeriklerin yoğun olacağı bir platform imajı çizer. Moda sektörü için çok uygundur.</p><p><strong>Marka Çağrışımı:</strong> Akılda kalıcı ve modern bir isimdir. Influencer marketing ve sosyal medya projeleri için büyük potansiyel taşır.</p></div></div></div>


    <script>
        // Alt kartları açıp/kapatan fonksiyon
        function toggleSubCards(elementId) {
            const subCards = document.getElementById(elementId);
            if (subCards.style.display === 'grid' || subCards.style.display === 'block') {
                subCards.style.display = 'none';
            } else {
                // block yerine grid kullanıyoruz çünkü sub-card-grid sınıfımız grid yapısında
                subCards.style.display = 'block'; // Önce block yapıp içeriğin yerleşmesini sağlıyoruz
                const grid = subCards.querySelector('.sub-card-grid');
                if(grid) grid.style.display = 'grid'; // Grid yapısını aktif ediyoruz
            }
            // Diğer kartların tıklama olayının sayfayı yukarı kaydırmasını engelle
            event.stopPropagation();
        }

        // Modal (pencere) açma fonksiyonu
        function openModal(modalId) {
            document.getElementById(modalId).style.display = 'block';
            // Arka plandaki kartın tıklama olayının tetiklenmesini engelle
            event.stopPropagation();
        }

        // Modal (pencere) kapatma fonksiyonu
        function closeModal(modalId) {
            document.getElementById(modalId).style.display = 'none';
        }
        
        // Pencere dışına tıklandığında modalı kapat
        window.onclick = function(event) {
            const modals = document.getElementsByClassName('modal');
            for (let i = 0; i < modals.length; i++) {
                if (event.target == modals[i]) {
                    modals[i].style.display = "none";
                }
            }
        }
    </script>

</body>
</html>
