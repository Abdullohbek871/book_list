from django.shortcuts import HttpResponse


def book_list(request):
    response = """
         <h1>Book list</h1>        
         <p>This is my books</p>
         <li><a href="book1/">Ikki eshik orasi</a></li>
         <li><a href="book2">Oq kema </a></li>
         <li><a href="book3"> O'tgan kunlar</a></li>       
                """

    return HttpResponse(response)


def book1(request):
    response = """
         <h1>Ikki eshik orasi</h1>        
         <h2>Author: O'tkir Hoshimov</h2>
         <h3>„Ikki eshik orasi“ – oʻzbek yozuvchisi Oʻtkir Hoshimov qalamiga mansub roman. Asar Oʻtkir Hoshimov merosining asosiy oʻrinlardan birini egallaydi[1].

Asarda insonlar taqdiri va inson umrining murakkabligini mahorat bilan tasvirlangan. Adib, birinchi navbatda, tinchlikka rahna solgan urushni tilga oladi. Ayniqsa, urush voqeligining har bir ota-ona qalbini jarohatlagani, koʻngillariga ozor yetkazgani romanning umuminsoniy pafosini tashkil etadi. Adib qalamga olgan obrazlari oddiy odamlarning fazilatlari – mardligi, matonati, vatanparvarligi va sabr-bardoshi haqida soʻzlaydi. Tajribali yozuvchi roman hodisalarini teran oʻrgangani uchun har bir epizod oʻquvchini qalbiga jiddiy taʼsir qiladi. Asarda tasvirlangan hayot manzaralari, insonlararo munosabatlar shuningdek, yozuvchining oʻziga xos badiiy uslubi juda tabiiy hamda samimiyligi bilan ajralib turadi. Yetti qism, qirq yetti bobdan tarkib topgan roman kompozitsion qurilishi jihatidan ham oʻziga xosligi bilan ajralib turadi[2]. Undagi voqea-hodisalar bayonida qatnashgan toʻqqizta personaj hikoyalarini adib bir-biriga ustalik bilan bogʻlagan.</h3>
         <li><a href="../">Back</a></li>      
                """

    return HttpResponse(response)


def book2(request):
    responses = """
         <h1>Oq kema</h1>        
         <h2>Author: CHingiz Aytmatov</h2>
         <h3>„Oq kema“ (ruscha: Белый пароход), „Ertakdan keyin“ deb ham ataladi — qirgʻiz yozuvchisi Chingiz Aytmatov qalamiga mansub qissa. Ilk bor 1970-yil „Noviy mir“ jurnalida chop etilgan. „Oq kema“ bir necha tilga, jumladan, oʻzbek tiliga tarjima qilingan.</h3>
         <li><a href="../">Back</a></li>      
                """

    return HttpResponse(responses)


def book3(request):
    responsess = """
         <h1>O'tkan kunlar</h1>        
         <h2>Author: Abdulla Qodiriy</h2>
         <h3>Oʻtkan kunlar, baʼzi manbalarda Oʻtgan kunlar – oʻzbek yozuvchisi Abdulla Qodiriy qalamiga mansub oʻzbek adabiyotidagi ilk roman[1]. 1969-yil „Oʻzbekfilm“ kinostudiyasida ushbu roman asosida „Oʻtgan kunlar“ nomli film suratga olingan. Adib romanni yozishda arab yozuvchisi Jurji Zaydon asarlaridan ilhomlangan[2]. Roman 1920-yillar boshida yozilgan boʻlib, 1922-yil ilk bor „Inqilob“ jurnalida chop etilgan va 1926-yilda alohida kitob holida nashr etilgan[3].</h3>
         <li><a href="../">Back</a></li>      
                """

    return HttpResponse(responsess)
