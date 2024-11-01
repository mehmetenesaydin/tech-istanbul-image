# Görüntü İşleme Uygulaması

Bu proje, kullanıcıların bir resmi yükleyip çeşitli filtreler uygulamalarına olanak tanıyan bir Flask tabanlı görüntü işleme uygulamasıdır. Uygulama, Python'da OpenCV kütüphanesi ile geliştirilmiştir ve HTML, CSS kullanılarak oluşturulmuş bir kullanıcı arayüzüne sahiptir.

## Proje Yapısı

- **app.py**: Flask web sunucusunun ana dosyasıdır. Görüntülerin yüklenmesi, seçilen filtrelerin uygulanması ve işlenmiş görüntülerin gösterilmesi işlevlerini içerir.
- **filters.py**: Farklı filtrelerin tanımlandığı modüldür. Görüntülere çeşitli filtreler uygulamak için `apply_filter` fonksiyonunu içerir.
- **style.css**: Uygulamanın basit ve duyarlı bir kullanıcı arayüzü tasarımını sağlar.
- **index.html**: Uygulamanın ana sayfa şablonunu içerir. Kullanıcıların resim yükleyip filtre seçimi yapabildiği bir form içerir.

## Dosya Açıklamaları

### `app.py`

Ana dosya olan `app.py`, Flask ile oluşturulmuş bir web sunucusudur. İşlevleri şunlardır:

- **`index` route**: Ana sayfayı (`index.html`) render eder.
- **`upload` route**: Kullanıcının yüklediği resmi alır, seçilen filtreyi uygular ve işlenmiş resmi kullanıcıya döner.

**Temel işleyiş:**

1. Kullanıcı, `index.html` aracılığıyla bir resim yükler ve bir filtre seçer.
2. `upload` fonksiyonu, yüklenen resmi kaydeder ve `filters.py` dosyasındaki `apply_filter` fonksiyonu ile seçilen filtreyi uygular.
3. İşlenmiş görüntü, kullanıcıya `send_file` ile döndürülür.

### `filters.py`

Bu dosya, `apply_filter` fonksiyonunu içerir. Bu fonksiyon, farklı filtreleri uygulayarak görüntüyü işler.

**Desteklenen filtreler:**

- `grayscale`: Görüntüyü gri tonlamaya dönüştürür.
- `invert`: Görüntünün renklerini ters çevirir.
- `brightness`: Görüntünün parlaklığını artırır.
- `sepia`: Sepya efekti uygular.
- `gaussian_blur`: Görüntüyü Gaussian bulanıklığı ile yumuşatır.
- `sharpen`: Görüntüyü keskinleştirir.
- `edge_detection`: Kenar algılama filtresi uygular.
- `autumn`: Sonbahar renk haritası uygular.

### `style.css`

Uygulamanın görünümünü ve kullanıcı deneyimini iyileştirmek için kullanılan CSS dosyasıdır.

- **Genel stil ayarları**: Sayfanın merkezde konumlanmasını sağlar, renk, yazı tipi ve diğer stil özelliklerini belirler.
- **Mobil uyumluluk**: 600px altındaki ekran boyutları için duyarlı tasarım sağlar.
- **Buton ve form stili**: Yükleme formu ve butonun görünümünü özelleştirir.

### `index.html`

Uygulamanın ana sayfa şablonudur. Kullanıcıların resim yüklemesini ve filtre seçmesini sağlar.

**Bileşenler:**

- **Form**: Resim yükleme ve filtre seçimi yapılabilen form.
- **Filtre seçenekleri**: Kullanıcının seçebileceği filtreleri içeren açılır menü.
- **Gönder Butonu**: Seçilen filtreyi uygulamak için formu gönderir.

## Kurulum ve Çalıştırma

1. Gerekli Python paketlerini yükleyin:

   ```bash
   pip install flask opencv-python
   ```

2. Sunucuyu çalıştırın:

   ```bash
   python app.py
   ```

3. Tarayıcıda [http://localhost:5000](http://localhost:5000) adresine giderek uygulamayı kullanın.

## Kullanım

1. Ana sayfada bir resim yükleyin ve uygulamak istediğiniz filtreyi seçin.
2. "Filtreyi Uygula" butonuna basarak işlenmiş resmi görüntüleyin.

---

**Not:** Bu proje, Mehmet Enes AYDIN tarafından "Tech Istanbul Görüntü İşleme Atölyesi" etkinliği için hazırlanmıştır.
