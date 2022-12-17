Öncelikle yazımızda yer alacak olan kavramlara bir bakalım

Train ve Test seti;
Veri setinde model için çalışılan kesite Train, modelin nasıl çalıştığını gözlemlemek için ayrılan veriye Test denir.
Overfitting;
Bir modelde overfitting durmunu train ve test arasında ki doğruluk farkından anlayabiliriz. Overfittingin oluşma sebebi eğittiğimiz modelin 
Train de sunulan veriyi ezberlemesi ve test anında gelen girdilere alakasız sonuçlar vermesi.
Underfitting;
Yetersiz ya da eksik öğrenme
Bias;
Kısaca hata,yanlılık,sapma.
Variance (Varyans);
Verilerin nasıl yayıldığını bize gösteren değerdir.

Bir makine öğrenmesi modeli kurarken her zaman için overfitting ve underfitting durumlarını algoritmanın her aşamasında düşünmemiz gerekiyor. 
Yaşanabilecek bu sıkıntıları bazen veri hazırlığında bazen de model parametre optimizasyonunda çözebiliriz. 
Ancak her zaman train veri setindeki doğruluk oranının test veri setinden yüksek olması durumu overfitting olduğuna işaret etmeyebilir.

Bir model için bias değeri yüksek ve varyansı değeri düşük olduğu durumda underfitting var diyebiliriz.
Bias değeri düşük ancak varyansı yüksek ise overfitting’den bahsedebiliriz.
Modelleri oluştururken amacımız modelin tahmin başarısını daha doğru değerlendirmektir. Bunu varyans ve yanlılık (bias) arasında denge kurarak 
sağlamaya çalışıyoruz.
Doğru model ise düşük yanlılığa ve düşük varyansa sahip modeldir.
Amerika’da yapılan araştırmalarda daha yüksek ücretli iş ilanlarının sadece erkeklere veya beyaz mahallelerdeki ev ilanlarının sadece beyazlara 
gösterildiği sonucuna varan deneyler yapılmıştır. Aynı şekilde bu veriler kullanılarak üretilecek bir yapay zeka algoritması, cinsiyeti bir karar 
mekanizması olarak kullanacaktır. İnternetten alınan hazır verilerle eğitilen çeşitli Doğal Dil İşleme modelleri, kadınlara veya farklı ırklara m
ensup insanlara olumsuz çağrışımlar ekleme eğilimindedir. Bunun sebebi sosyal medyada var olan mevcut kişilerin sahip olduğu sosyal önyargıların, 
eğitim verilerine yansımasından kaynaklıdır.
Tamamen deneysel bir olay olması ve önceden belirlenmiş değişkenlere sahip olmaması nedeniyle bu duruma önemli bir örnek olarak gösterilebilecek 
bir Twitter botu, Microsoft tarafından 2016 yılında aktif edildi. Microsoft, Tay ismindeki yapay zekalı robot ile ne kadar çok sohbet edilirse o 
kadar akıllı hale geldiğini ve insanlarla “sıradan ve eğlenceli sohbetler” yoluyla etkileşim kurmayı öğrendiğini söyledi. Yani kullanıcılar bu 
yapay zeka ile etkileşime geçtikçe yapay zeka öğrenecek ve kendini geliştirecekti. Ne yazık ki, işler Microsoft’un beklediği yönde ilerlemedi. T
ay piyasaya sürüldükten çok kısa bir süre sonra, kullanıcılar yapay zekaya her türlü kadın düşmanı, ırkçı ifadelerle eğitmeye başladı. 
Ve yapay zeka, elde ettiği bu verilerle kendini eğiterek, bunları kullanıcılara tekrarlamaya başladı. Kısa sürede tepki alan bu yapay zeka, 
Microsoft tarafından sonlandırıldı. Bu olay, yapay zeka modellerinin eğitiminde kullanılan verilerin önemini tekrardan kanıtladı.

Bias önleme yolları;

Bu noktada geliştireceğimiz modelimizde neyi çözdüğünüzü ve neyin yanlış gideceğini bilmemiz gerekiyor. Geliştirdiğimiz bu model nedir? 
Son kullanıcıda ne gibi sorunlar ortaya çıkabilir? Veri kümesinde dengesizlikler var mı?(örneğin kadın yazılımcı - erkek yazılımcı)
Veriyi nereden aldık? — Aldığımız kaynak yanlı olabilir.
Yeteri kadar uç durumlar var mı? — Bunlar olmadan modelimiz normalin dışında olan durumları tanımlamakta zorlanacaktır.
Modeller verilerle öğrenir. İyi veri iyi model doğurur, kötü veri kötü model doğurur ve yanlı veri yanlı model doğurur.
Modelimizi eğittikten sonra sadece doğruluk oranına bakmak yerine modelin ürettiği tahminleri değerlendirmek gerekir.
