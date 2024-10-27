Ana içeriğe geç
Binance Logo
Genel Bilgi

Bu sayfada
Genel Bilgi
Genel API 
Aşağıdaki temel uç noktalar mevcuttur:
https://api.binance.com
https://api1.binance.com
https://api2.binance.com
https://api3.binance.com
https://api4.binance.com
Yukarıdaki noktadaki son 4 uç nokta ( api1- api4) daha iyi performans sağlayabilir ancak daha az kararlılığa sahiptir. Lütfen kurulumunuz için en iyi işe yarayanı kullanın.
Tüm uç noktalar bir JSON nesnesi veya dizisi döndürür.
Veriler artan sırada döndürülür . En eskisi ilk, en yenisi son.
Tüm zaman ve zaman damgası ile ilgili alanlar milisaniye cinsindendir .
HTTP Dönüş 
Hatalı isteklerde HTTP 4XXdönüş kodları kullanılır; sorun gönderici tarafındadır.
403WAF Limiti (Web Uygulama Güvenlik Duvarı) ihlal edildiğinde HTTP dönüş kodu kullanılır.
HTTP 409dönüş kodu, cancelReplace siparişi kısmen başarılı olduğunda kullanılır. (örneğin, siparişin iptali başarısız olursa ancak yeni sipariş yerleştirme başarılı olursa.)
İstek oranı sınırını aşarken HTTP 429dönüş kodu kullanılır.
HTTP 418dönüş kodu, bir IP'nin kod aldıktan sonra istek göndermeye devam etmesi nedeniyle otomatik olarak yasaklanması durumunda kullanılır 429.
HTTP dönüş kodları dahili hatalar için kullanılır; sorun Binance'in tarafındadır. Bunu bir başarısızlık işlemi olarak değerlendirmemek5XX önemlidir ; yürütme durumu BİLİNMİYOR ve başarılı olabilirdi.
Hata Kodları ve 
Bir hata varsa, API, nedenini belirten bir mesajla birlikte bir hata döndürecektir.
API ve SAPI üzerindeki hata yükü şu şekildedir:

{
  "code": -1121,
  "msg": "Invalid symbol."
}

Hata Kodları'nda tanımlanan belirli hata kodları ve mesajları .
 Hakkında Genel Bilgiler
Uç noktalar için GETparametreler . olarak gönderilmelidir query string.
POST, PUT, ve uç noktaları için parametreler veya içerik türünde gönderilebilir DELETE. İsterseniz hem ve arasında parametreleri karıştırabilirsiniz .query stringrequest bodyapplication/x-www-form-urlencodedquery stringrequest body
Parametreler herhangi bir sırayla gönderilebilir.
query stringBir parametre hem 'de hem de ' de gönderilirse request body, query stringparametre kullanılacaktır.
 Hakkında Genel Bilgiler
Başlıklar için aşağıdaki intervalLetterdeğerler:
İKİNCİ => S
DAKİKA => M
SAAT => S
GÜN => D
intervalNumaralığın miktarını tanımlar. Örneğin, M intervalNumile 5 intervalLetter"Her 5 dakikada" anlamına gelir.
Dizi /api/v3/exchangeInfo rateLimits, borsanın RAW_REQUESTS, REQUEST_WEIGHT, ve oran limitleriyle ilgili nesneleri içerir. Bunlar , altındaki bölümde ORDERSdaha ayrıntılı olarak tanımlanmıştır .ENUM definitionsRate limiters (rateLimitType)
Talep oranı limiti veya emir oranı limiti ihlal edildiğinde 429 döndürülür.
IP 
X-MBX-USED-WEIGHT-(intervalNum)(intervalLetter)Her istek , yanıt başlıklarında tanımlanan tüm istek oranı sınırlayıcıları için IP için kullanılan geçerli ağırlığı içerecektir .
Her rota, weighther uç noktanın saydığı istek sayısını belirleyen bir 'e sahiptir. Daha ağır uç noktalar ve birden fazla sembol üzerinde işlem yapan uç noktalar daha ağır bir 'e sahip olacaktır weight.
429 aldığınızda, API olarak geri çekilmeniz ve API'ye spam göndermemeniz sizin sorumluluğunuzdur.
Hız sınırlarının tekrar tekrar ihlal edilmesi ve/veya 429 aldıktan sonra geri çekilmemeniz, otomatik IP yasağına (HTTP durumu 418) neden olacaktır.
IP yasakları takip ediliyor ve tekrarlayan ihlaller için süresi 2 dakikadan 3 güne kadar değişiyor .
418 veya 429 yanıtlarıyla bir başlık gönderilir ve 429 durumunda yasağı önlemek için beklenmesi gereken saniye sayısınıRetry-After , 418 durumunda ise yasağın sona ermesini sağlar .
API'deki sınırlamalar API anahtarlarına değil IP'lere dayanmaktadır.
Veri almak için mümkün olduğunca web soketini kullanmanızı öneririz, çünkü bu istek oranı sınırına dahil edilmeyecektir.
Sipariş Oranı 
X-MBX-ORDER-COUNT-(intervalNum)(intervalLetter)Her başarılı sipariş yanıtı , tanımlanan tüm sipariş oranı sınırlayıcıları için hesaba ait geçerli sipariş sayısını içeren bir başlık içerecektir .

Sipariş sayısı limiti aştığında, başlık olmadan 429 hatası alırsınız Retry-After. Lütfen kullanarak Sipariş Oranı Limiti kurallarını kontrol edin GET api/v3/exchangeInfove buna göre yeniden etkinleştirmeyi bekleyin.

X-MBX-ORDER-COUNT-**Reddedilen/başarısız siparişlerin yanıtta başlıklara sahip olması garanti edilmez .

Her hesaba karşılık emir oranı limiti hesaplanır .

Sipariş sayısı kullanımını izlemek için GET'e bakınapi/v3/rateLimit/order

Websocket 
WebSocket bağlantıları saniyede 5 gelen mesaj sınırına sahiptir. Bir mesaj şu şekilde değerlendirilir:
Bir PING çerçevesi
Bir PONG çerçevesi
JSON kontrollü bir mesaj (örneğin abone ol, aboneliği iptal et)
Sınırı aşan bağlantı kesilir; tekrar tekrar kesilen IP'ler yasaklanabilir.
Tek bir bağlantıyla en fazla 1024 yayın dinlenebilir.
Her IP için her 5 dakikada bir deneme başına 300 bağlantı sınırı vardır .
/api/ ve /sapi/ Sınır 
/api/*ve uç noktaları /sapi/*, IP sınırları veya UID (hesap) sınırları olmak üzere iki erişim sınırlama kuralından birini benimser.

İlgili uç noktalar /api/*:

IP ve UID (hesap) limiti olmak üzere iki modun her biri birbirinden bağımsızdır.
Uç noktalar IP bazlı olarak dakikada 6000 sınırını paylaşırlar.
X-MBX-USED-WEIGHT-(intervalNum)(intervalLetter)Yanıtlar , geçerli IP tarafından kullanılan ağırlığı tanımlayan başlığı içerir .
X-MBX-ORDER-COUNT-(intervalNum)(intervalLetter)Başarılı sipariş yanıtları , UID tarafından kullanılan sipariş sınırını tanımlayan başlığı içerir .
İlgili uç noktalar /sapi/*:

Uç noktalar IP veya UID sınırına ve bunlara karşılık gelen ağırlık değerine göre işaretlenir.
IP limiti olan her uç noktanın dakikada 12000'lik bağımsız bir limiti vardır.
UID limiti olan her uç noktanın dakikada 180000'lik bağımsız bir limiti vardır.
X-SAPI-USED-IP-WEIGHT-1MIP sınırlamaları olan uç noktalardan gelen yanıtlar , geçerli IP tarafından kullanılan ağırlığı tanımlayan başlığı içerir .
X-SAPI-USED-UID-WEIGHT-1MUID sınırlamaları olan uç noktalardan gelen yanıtlar , geçerli UID tarafından kullanılan ağırlığı tanımlayan başlığı içerir .
Veri 
API sistemi asenkron olduğundan yanıtta bir miktar gecikme olması normal ve beklenen bir durumdur.
Her uç noktanın, verilerin nereden alındığını gösteren bir veri kaynağı vardır ve böylece hangi uç noktaların en güncel yanıta sahip olduğu gösterilir.
Bunlar, güncellemelerde potansiyel gecikmeler olan kaynaktan en güncel cevaba kadar sıralanmış üç kaynaktır.

Eşleştirme Motoru - veriler eşleştirme motorundan alınmıştır
Bellek - veriler sunucunun yerel veya harici belleğinden gelir
Veritabanı - veriler doğrudan bir veritabanından alınır
Bazı uç noktalar 1'den fazla veri kaynağına sahip olabilir. (Örneğin Bellek => Veritabanı)

Bu, uç noktanın ilk Veri Kaynağını kontrol edeceği ve aradığı değeri bulamazsa bir sonrakine bakacağı anlamına gelir.
Uç nokta güvenlik 
Her uç noktanın, onunla nasıl etkileşim kuracağınızı belirleyen bir güvenlik türü vardır. Bu, uç noktanın ADI'nın yanında belirtilir.
Hiçbir güvenlik türü belirtilmemişse, güvenlik türünün HİÇBİRİ olduğunu varsayın.
API anahtarları başlık aracılığıyla Rest API'ye geçirilir X-MBX-APIKEY .
API anahtarları ve gizli anahtarlar büyük/küçük harfe duyarlıdır .
API anahtarları yalnızca belirli türdeki güvenli uç noktalara erişecek şekilde yapılandırılabilir. Örneğin, bir API anahtarı yalnızca TİCARET için kullanılabilirken, başka bir API anahtarı TİCARET rotaları hariç her şeye erişebilir.
Varsayılan olarak API anahtarları tüm güvenli rotalara erişebilir.
Güvenlik Türü	Tanım
HİÇBİRİ	Son noktaya serbestçe erişilebilir.
TİCARET	Son nokta geçerli bir API Anahtarı ve imza gönderilmesini gerektirir.
MARJ	Son nokta geçerli bir API Anahtarı ve imza gönderilmesini gerektirir.
KULLANICI_VERİLERİ	Son nokta geçerli bir API Anahtarı ve imza gönderilmesini gerektirir.
KULLANICI_AKIŞI	Son nokta geçerli bir API Anahtarı gönderilmesini gerektirir.
PAZAR_VERİLERİ	Son nokta geçerli bir API Anahtarı gönderilmesini gerektirir.
TRADEve MARGINuç USER_DATAnoktalar SIGNEDuç noktalardır.
İMZALANMIŞ (TİCARET, KULLANICI_VERİLERİ VE MARJ) Uç nokta 
SIGNEDuç noktaların veya signatureiçinde gönderilecek ek bir parametreye, , ihtiyacı vardır .query stringrequest body
HMAC SHA256Uç noktalar imzaları kullanır . HMAC SHA256 signatureAnahtarlı bir işlemdir. Anahtar olarak your ve HMAC işlemi için değer olarak HMAC SHA256your kullanın .secretKeytotalParams
signatureBüyük / küçük harfe duyarlı değildir .
totalParamsquery string, ile birleştirilmiş olarak tanımlanır request body.
Zamanlama 
Bir SIGNEDuç noktanın ayrıca, isteğin oluşturulduğu ve gönderildiği zamanın milisaniye cinsinden zaman damgası olması gereken bir parametrenin timestampgönderilmesi gerekir.
An additional parameter, recvWindow, may be sent to specify the number of milliseconds after timestamp the request is valid for. If recvWindow is not sent, it defaults to 5000.
The logic is as follows:

  if (timestamp < (serverTime + 1000) && (serverTime - timestamp) <= recvWindow)
  {
    // process request
  } 
  else 
  {
    // reject request
  }

Serious trading is about timing. Networks can be unstable and unreliable, which can lead to requests taking varying amounts of time to reach the servers. With recvWindow, you can specify that the request must be processed within a certain number of milliseconds or be rejected by the server.

It is recommended to use a small recvWindow of 5000 or less! The max cannot go beyond 60,000!
SIGNED Endpoint Examples for POST /api/v3/order - HMAC Keys
Here is a step-by-step example of how to send a vaild signed payload from the Linux command line using echo, openssl, and curl.

Key	Value
apiKey	vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A
secretKey	NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j
Parameter	Value
symbol	LTCBTC
side	BUY
type	LIMIT
timeInForce	GTC
quantity	1
price	0.1
recvWindow	5000
timestamp	1499827319559
Example 1: As a request body

Example 1

HMAC SHA256 signature:

    $ echo -n "symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559" | openssl dgst -sha256 -hmac "NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j"
    (stdin)= c8db56825ae71d6d79447849e617115f4a920fa2acdcab2b053c4b2838bd6b71


curl command:

    (HMAC SHA256)
    $ curl -H "X-MBX-APIKEY: vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A" -X POST 'https://api.binance.com/api/v3/order' -d 'symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559&signature=c8db56825ae71d6d79447849e617115f4a920fa2acdcab2b053c4b2838bd6b71'
    


requestBody:
symbol=LTCBTC
&side=BUY
&type=LIMIT
&timeInForce=GTC
&quantity=1
&price=0.1
&recvWindow=5000
&timestamp=1499827319559

Example 2: As a query string

Example 2

HMAC SHA256 signature:

    $ echo -n "symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559" | openssl dgst -sha256 -hmac "NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j"
    (stdin)= c8db56825ae71d6d79447849e617115f4a920fa2acdcab2b053c4b2838bd6b71
    


curl command:

    (HMAC SHA256)
   $ curl -H "X-MBX-APIKEY: vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A" -X POST 'https://api.binance.com/api/v3/order?symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559&signature=c8db56825ae71d6d79447849e617115f4a920fa2acdcab2b053c4b2838bd6b71'
    


queryString:
symbol=LTCBTC
&side=BUY
&type=LIMIT
&timeInForce=GTC
&quantity=1
&price=0.1
&recvWindow=5000
&timestamp=1499827319559

Example 3: Mixed query string and request body

Example 3

HMAC SHA256 signature:

   $ echo -n "symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTCquantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559" | openssl dgst -sha256 -hmac "NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j"
    (stdin)= 0fd168b8ddb4876a0358a8d14d0c9f3da0e9b20c5d52b2a00fcf7d1c602f9a77
    


curl komutu:

    (HMAC SHA256)
    $ curl -H "X-MBX-APIKEY: vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A" -X POST 'https://api.binance.com/api/v3/order?symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC' -d 'quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559&signature=0fd168b8ddb4876a0358a8d14d0c9f3da0e9b20c5d52b2a00fcf7d1c602f9a77'


queryString:
symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC

requestBody:
quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559

Note that the signature is different in example 3. There is no & between "GTC" and "quantity=1".

SIGNED Endpoint Example for POST /api/v3/order - RSA Keys
This will be a step by step process how to create the signature payload to send a valid signed payload.
We support PKCS#8 currently.
To get your API key, you need to upload your RSA Public Key to your account and a corresponding API key will be provided for you.
For this example, the private key will be referenced as test-prv-key.pem

Key	Değer
apiKey	CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ
Parametre	Değer
sembol	BTCUSDT
taraf	SATMAK
tip	SINIR
zamanGüçlü	Genel Şartlar
miktar	1
fiyat	0,2
almaPenceresi	5000
zaman damgası	1668481559918
İmza yükü (listelenen parametrelerle):

symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000

Adım 1: Yükü oluşturun

Parametre listesini bir dizgeye düzenleyin. Her parametreyi bir &. ile ayırın.

Adım 2: İmzayı hesaplayın:

2.1 - İmza yükünü ASCII verisi olarak kodlayın.

Adım 2.2

 $ echo -n 'symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000' | openssl dgst -sha256 -sign ./test-prv-key.pem


2.2 - SHA-256 karma fonksiyonu ile RSASSA-PKCS1-v1_5 algoritmasını kullanarak yükü imzalayın.

Adım 2.3

$  echo -n 'symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000' | openssl dgst -sha256 -sign ./test-prv-key.pem | openssl enc -base64 -A
HZ8HOjiJ1s/igS9JA+n7+7Ti/ihtkRF5BIWcPIEluJP6tlbFM/Bf44LfZka/iemtahZAZzcO9TnI5uaXh3++lrqtNonCwp6/245UFWkiW1elpgtVAmJPbogcAv6rSlokztAfWk296ZJXzRDYAtzGH0gq7CgSJKfH+XxaCmR0WcvlKjNQnp12/eKXJYO4tDap8UCBLuyxDnR7oJKLHQHJLP0r0EAVOOSIbrFang/1WOq+Jaq4Efc4XpnTgnwlBbWTmhWDR1pvS9iVEzcSYLHT/fNnMRxFc7u+j3qI//5yuGuu14KR0MuQKKCSpViieD+fIti46sxPTsjSemoUKp0oXA==


2.3 - Çıktıyı base64 string olarak kodla.

Adım 2.4

HZ8HOjiJ1s%2FigS9JA%2Bn7%2B7Ti%2FihtkRF5BIWcPIEluJP6tlbFM%2FBf44LfZka%2FiemtahZAZzcO9TnI5uaXh3%2B%2BlrqtNonCwp6%2F245UFWkiW1elpgtVAmJPbogcAv6rSlokztAfWk296ZJXzRDYAtzGH0gq7CgSJKfH%2BXxaCmR0WcvlKjNQnp12%2FeKXJYO4tDap8UCBLuyxDnR7oJKLHQHJLP0r0EAVOOSIbrFang%2F1WOq%2BJaq4Efc4XpnTgnwlBbWTmhWDR1pvS9iVEzcSYLHT%2FfNnMRxFc7u%2Bj3qI%2F%2F5yuGuu14KR0MuQKKCSpViieD%2BfIti46sxPTsjSemoUKp0oXA%3D%3D


/2.4 - İmza ve içerebileceğinden =, bu isteğin gönderilmesinde sorunlara neden olabilir. Bu yüzden imzanın URL kodlu olması gerekir.

Adım 2.5

 curl -H "X-MBX-APIKEY: CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ" -X POST 'https://api.binance.com/api/v3/order?symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918recvWindow=5000&signature=HZ8HOjiJ1s%2FigS9JA%2Bn7%2B7Ti%2FihtkRF5BIWcPIEluJP6tlbFM%2FBf44LfZka%2FiemtahZAZzcO9TnI5uaXh3%2B%2BlrqtNonCwp6%2F245UFWkiW1elpgtVAmJPbogcAv6rSlokztAfWk296ZJXzRDYAtzGH0gq7CgSJKfH%2BXxaCmR0WcvlKjNQnp12%2FeKXJYO4tDap8UCBLuyxDnR7oJKLHQHJLP0r0EAVOOSIbrFang%2F1WOq%2BJaq4Efc4XpnTgnwlBbWTmhWDR1pvS9iVEzcSYLHT%2FfNnMRxFc7u%2Bj3qI%2F%2F5yuGuu14KR0MuQKKCSpViieD%2BfIti46sxPTsjSemoUKp0oXA%3D%3D'


2.5 - curl komutu

Bash betiği

#!/usr/bin/env bash

# Set up authentication:
API_KEY="put your own API Key here"
PRIVATE_KEY_PATH="test-prv-key.pem"

# Set up the request:
API_METHOD="POST"
API_CALL="api/v3/order"
API_PARAMS="symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2"

# Sign the request:
timestamp=$(date +%s000)
api_params_with_timestamp="$API_PARAMS&timestamp=$timestamp"
signature=$(echo -n "$api_params_with_timestamp" \
            | openssl dgst -sha256 -sign "$PRIVATE_KEY_PATH" \
            | openssl enc -base64 -A)

# Send the request:
curl -H "X-MBX-APIKEY: $API_KEY" -X "$API_METHOD" \
    "https://api.binance.com/$API_CALL?$api_params_with_timestamp" \
    --data-urlencode "signature=$signature"

Benzer adımları içeren örnek Bash betiği sağ tarafta mevcuttur.

Öncesi
giriiş
Sonraki
Hacim Katılımı (VP) Yeni Sipariş (TİCARET)
Telif Hakkı © 2024 Binance.