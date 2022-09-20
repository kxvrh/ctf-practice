#!/usr/bin/python
#coding:utf-8

# 已知n1,n2,n3和c1,c2,c3, 求明文m (e未知)
# 爆破e (理论上e的值不可能特别大) --> 注意e不可以为0

import gmpy2
import time
from Crypto.Util.number import long_to_bytes
from sympy.ntheory.modular import crt

# def CRT(items):
#     N = reduce(lambda x, y: x * y, (i[1] for i in items))
#     result = 0
#     for a, n in items:
#         m = N / n
#         d, r, s = gmpy2.gcdext(n, m)
#         if d != 1: raise Exception("Input not pairwise co-prime")
#         result += a * s * m
#     return result % N, N

for e in range(1,65537):
    print ("e的值为："+ str(e))
    ns = [512485683379248627994222054928198152386318092644738180381554991475217377796405434854335056277622930547863024818767444598344410114539577997600760963632431418175495524212085227342236317690282303579871792604136978688849603906940046044534323144974053231416767418730793910263975433053461456721073431678088001273173284389468140530700307609776388997865772839512574327150259671379170026613490736333987026453811040095250243133527257805577313715212812958664333627735599163789040400505627822241159031720604542905728505522971011717666817345682281260608494735673864681250466412331593958894961131488445737536608944832487664399026112772867107087511943463538583457683579491879673641747689921593966314187930608676512863996255918764250565309330970516261788076369420228272626436321005067854817412234934831868982242339922158712560874614372107706079567173989259456857608363761805364620698478353230772690734471510134342068390134954906482464260622773680007027270240927217704723404590378763918240935998163799908756686555902792898116295063931404222813003278812035337906714468974195245694839181751219111401835806870499348487733491946647101567421316709805465910092315582508830042739317183125257526385847182925549204858279744905286118241383712008804714524959337,438455129905663326510217996453387937818265147158140912081178396743766705601124940665790932344481155400002301338515524231925714648114810219744906401692738457749458278151114387635536422652494466839733126044697474681703619367177810933835403243322075569780826658879869369073520408208881042059373788457691248620041363036256053901332732025192473513880966852569324181325637113811528881626784815652329195878816996045400785780863488097039442217416113657576307367610903230358079374901165790819244990843302685212147937153498655927622235924092330572523305629875231791404715651959183795358420179448279473775095313467638399477146757229070378632818776284346057352441718601252186467300865188809011881157659965626389442897514625454445586427853274594179142076630186758618951856854369899214565996874415367745532324528369058533990486031307221691495860169756892482038169396339092890711719474815240465100920233523155578622866773601776749758630566368939795717596554340628161945827353855540096690670439478394005656412231410467731001387527736194221724672706430756234754940822630104576940365000003870106656376805817265622018226286424874849207544941467791006032204338343828474870841718078157179104550873232976483975616382329979719134670083763882419066043745801,653315011935722683633899239971517941619349225695222088452194012082260326313201677835660945384275485145096065789222102748796071121711741203243670414338927148826702659529852592126552866279897276172924949211665542075745606262930965969289469269385301071552633342358778736510473222632405762525274716680890233538863243345692088160380126514797731426532170556602864402270537622591136334016473986479380886333915960074299602274671326676436465721122648878937456119562883070126768308182048342065999178801029549307888585963509968312202636585782857004099050511100978623830631609264692400949699741726049139455818499378351117228903547409337889830316549423121620369033893579169220786264356102811922557390482838303383978852873130668081323828348612838822334030273451283626768826170742066900163715681536233509267601661429117260438377187730730034557272078251624627747748768164927882629463582925338671073691854448141606348848569385399779605558939845122283956988301029392645516848789335435999529269974727866199089608234196347034929836500632922152689344010813924445789115346540480520677473336451000106471051448922245859528982264117288034012176740729039917085047680314285043383807860886975328022081757231586996665711685759320301324337611554984459865268735881]
    cs = [399010311121182943332309121114907411971005715655147896283369909476319473320142906797174433944197736682155228613837419252518602898442959789436466058872795204684719139465569382123104599556182756881512146887835901762524124952169928552088784468883025949156497960737022461897943895387142452146896439885966442758514883551398180828108448038344602784548819521285900170439253491829051725879130937677485144773782521693714498513283707353421186155236088813956052327129437629781022749262691591903818002745150640452705864306967771312436295009214557351255495381997105698411916814556536780279272815368148780203872635230392276897038561029968066298918693863362128071013792150689063207647118900886716782643660458005277167365424238794827411411025963471035659129582133847548362840024006275626160743108434783501160707247644258474071101048981371157536016841319724905482389910167999437472868380967163152370362239187926424917469145689563508506504834309075169219014250408812927354102861156064165623878898346687465296913386550602835135798632531680549909595951180893284332783411347133761580603793979970749905619763806933044555810234621000823825742812412350701424826572434253481700878717477193917096525871323813383655618357256914271825408980286254757657357995428,101679127888134323725416317100411720344826429929601328830868924222029861957243313130888629593943146715504722159868347829741654002116628427240384129016395510386411083515704260057559942172196997688477611541379008440315525316323378006679145918547369295922501238705223385759650387660754808143678545678441899153341228089669541301309154208551196055571665128996579361850190451835989886402761079553669245333442973834901750807859208019800931394134333884538829836559098119575423601453695242340711462656301014871141326221684472998453644674700574750611088468850059788694559149584998461969466200699430608777201007485329143552935271042350737207244773742158476032266489948431865071820745289852064304693461790424825326755826807490144386639668870704391714183649200687936642883542238703444082716114345750431099371235795680332396127429200259296001455589068681502453198015842837674520962582234472173147801727327037498300172851794008303961739725055356570920954996102811127534547751755606626494829801001521950432984882492261314920320540574998939744987184277444447882158088666360204231746334686511237233889476914338775126672202451100099836815620060273259496385106193137702971000898173496712086672858552829708543458356018009228876954328125176399940266486721,651772959894870840060102038649718098624287975188831353563157895211464117397354692694376307356217104809294356436693017232734414966073515715756220710870282877518135284377272355100684336075930019293411882322079560643529612235963044721844611100622244718471536231327233428643853698908853467079122167042327498402688154226515102711290801517703393081695874935492231825031203363534068625173045722223997882474274748963849884733327551858142505525087203555003800843026732158720251038619039816119396261158977354910621299476774407868591073821412845260844364621190213250892034844436195591940833748984393882432317958987741676458005543046381494570625865553127054568200356516586531928435872450053173532081370638426771798393956893679060639774311468035158208104718372121197462041463810903719442698671063036585602918806277123795224127059383077780909672382158306786154051753779666264201462236110658367733033404001181979613839663302066116787817088037203018689704591027311041019288748853090272606431612223021609997420842480765936764638248845753574667339942415336226419163132243409610852241935411558278958551060715644054460732821982619702657854190398281165478586242902687379449741828444267651003458264204219235283795584568034971205824995190606412406743814912]
    # data = zip(cs, ns)
    # resultant, r = CRT(data)
    resultant, mod = crt(ns, cs)
    m, is_perfect = gmpy2.iroot(resultant, e)
    print (long_to_bytes(m))