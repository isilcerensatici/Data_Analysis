import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# 0 ile 80 arasında 100 rastgele sayı üretme
data = np.random.randint(0, 80, 100)

# İstatistiksel hesaplamalar
mean = np.mean(data)
median = np.median(data)
range_val = np.ptp(data)
std_dev = np.std(data, ddof=1)
oms = np.mean(np.abs(data - mean))
variance = np.var(data, ddof=1)
cv = (std_dev / mean) * 100
skewness = stats.skew(data)
kurtosis = stats.kurtosis(data)

# Grafikler için stil
sns.set(style="whitegrid")

# Histogram ve Kutu Grafiği
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Histogram
sns.histplot(data, bins=10, kde=True, ax=axes[0], color="skyblue")
axes[0].axvline(mean, color='red', linestyle='--', label=f'Ortalama: {mean:.2f}')
axes[0].axvline(median, color='green', linestyle='--', label=f'Medyan: {median:.2f}')
axes[0].set_title("Histogram ve Ortalama/Medyan Gösterimi")
axes[0].set_xlabel("Değerler")
axes[0].set_ylabel("Frekans")
axes[0].legend()

# Kutu Grafiği
sns.boxplot(data=data, ax=axes[1], color="lightcoral")
axes[1].set_title("Kutu Grafiği")
axes[1].set_xlabel("Değerler")

# İstatistiksel Sonuçları Ekrana Yazdırma
print("Ortalama:", mean)
print("Medyan:", median)
print("Dağılım Genişliği:", range_val)
print("Ortalama Mutlak Sapma (OMS):", oms)
print("Varyans:", variance)
print("Standart Sapma:", std_dev)
print("Değişim Katsayısı (%):", cv)
print("Çarpıklık Katsayısı:", skewness)
print("Basıklık Katsayısı:", kurtosis)

plt.tight_layout()
plt.show()
