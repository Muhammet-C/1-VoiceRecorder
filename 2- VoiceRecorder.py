# Gereken kutuphaneleri yukluyoruz
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

# Örnekleme frekansı
freq = 44100

# Kayit suresi
duration = 5

# Kaydediciyi verilen değerlerle başlat
# süre ve örnekleme sıklığı
recording = sd.rec(int(duration * freq), 
                   samplerate=freq, channels=2)

# Belirtilen saniye sayısı için ses kaydı
sd.wait()

# Bu, NumPy dizisini bir sese dönüştürecek
# Verilen örnekleme frekansına sahip dosya
write("recording0.wav", freq, recording)

# NumPy dizisini ses dosyasına dönüştürme
wv.write("recording1.wav", recording, freq, sampwidth=2)