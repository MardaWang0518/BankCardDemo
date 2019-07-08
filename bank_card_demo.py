import re

s1 = "^(621096|621098|622150|622151|622181|622188|622199|955100|621095|620062|621285|621798|621799|621797|620529|621622|621599|621674|623218|623219)\\d{13}$"
s2 = "^(62215049|62215050|62215051|62218850|62218851|62218849)\\d{11}$"
s3 = "^(622812|622810|622811|628310|625919)\\d{10}$"

s4 = "^(620200|620302|620402|620403|620404|620406|620407|620409|620410|620411|620412|620502|620503|620405|620408|620512|620602|620604|620607|620611|620612|620704|620706|620707|620708|620709|620710|620609|620712|620713|620714|620802|620711|620904|620905|621001|620902|621103|621105|621106|621107|621102|621203|621204|621205|621206|621207|621208|621209|621210|621302|621303|621202|621305|621306|621307|621309|621311|621313|621211|621315|621304|621402|621404|621405|621406|621407|621408|621409|621410|621502|621317|621511|621602|621603|621604|621605|621608|621609|621610|621611|621612|621613|621614|621615|621616|621617|621607|621606|621804|621807|621813|621814|621817|621901|621904|621905|621906|621907|621908|621909|621910|621911|621912|621913|621915|622002|621903|622004|622005|622006|622007|622008|622010|622011|622012|621914|622015|622016|622003|622018|622019|622020|622102|622103|622104|622105|622013|622111|622114|622017|622110|622303|622304|622305|622306|622307|622308|622309|622314|622315|622317|622302|622402|622403|622404|622313|622504|622505|622509|622513|622517|622502|622604|622605|622606|622510|622703|622715|622806|622902|622903|622706|623002|623006|623008|623011|623012|622904|623015|623100|623202|623301|623400|623500|623602|623803|623901|623014|624100|624200|624301|624402|623700|624000)\\d{12}$"
s5 = "^(622200|622202|622203|622208|621225|620058|621281|900000|621558|621559|621722|621723|620086|621226|621618|620516|621227|621288|621721|900010|623062|621670|621720|621379|621240|621724|621762|621414|621375|622926|622927|622928|622929|622930|622931|621733|621732|621372|621369|621763)\\d{13}$"
s6 = "^(402791|427028|427038|548259|621376|621423|621428|621434|621761|621749|621300|621378|622944|622949|621371|621730|621734|621433|621370|621764|621464|621765|621750|621377|621367|621374|621731|621781)\\d{10}$"
s7 = "^(9558)\\d{15}$"
s8 = "^(370246|370248|370249|370247|370267|374738|374739)\\d{9}$"
s9 = "^(427010|427018|427019|427020|427029|427030|427039|438125|438126|451804|451810|451811|458071|489734|489735|489736|510529|427062|524091|427064|530970|530990|558360|524047|525498|622230|622231|622232|622233|622234|622235|622237|622239|622240|622245|622238|451804|451810|451811|458071|628288|628286|622206|526836|513685|543098|458441|622246|544210|548943|356879|356880|356881|356882|528856|625330|625331|625332|622236|524374|550213|625929|625927|625939|625987|625930|625114|622159|625021|625022|625932|622889|625900|625915|625916|622171|625931|625113|625928|625914|625986|625925|625921|625926|625942|622158|625917|625922|625934|625933|625920|625924|625017|625018|625019)\\d{10}$"
s10 = "^(45806|53098|45806|53098)\\d{11}$"
s11 = "^(622210|622211|622212|622213|622214|622220|622223|622225|622229|622215|622224)\\d{10}$"
s12 = "^(620054|620142|620184|620030|620050|620143|620149|620124|620183|620094|620186|620148|620185)\\d{10}$"
s13 = "^(620114|620187|620046)\\d{13}$"

s14 = "^(622841|622824|622826|622848|620059|621282|622828|622823|621336|621619|622821|622822|622825|622827|622845|622849|623018|623206|621671|622840|622843|622844|622846|622847|620501)\\d{13}$"
s15 = "^(95595|95596|95597|95598|95599)\\d{14}$"
s16 = "^(103)\\d{16}$"
s17 = "^(403361|404117|404118|404119|404120|404121|463758|519412|519413|520082|520083|552599|558730|514027|622836|622837|628268|625996|625998|625997|622838|625336|625826|625827|544243|548478|628269)\\d{10}$"
s18 = "^(622820|622830)\\d{10}$"

s19 = "^(621660|621661|621662|621663|621665|621667|621668|621669|621666|456351|601382|621256|621212|621283|620061|621725|621330|621331|621332|621333|621297|621568|621569|621672|623208|621620|621756|621757|621758|621759|621785|621786|621787|621788|621789|621790|622273|622274|622771|622772|622770|621741|621041)\\d{13}$"
s20 = "^(621293|621294|621342|621343|621364|621394|621648|621248|621215|621249|621231|621638|621334|621395|623040|622348)\\d{10}$"
s21 = "^(625908|625910|625909|356833|356835|409665|409666|409668|409669|409670|409671|409672|512315|512316|512411|512412|514957|409667|438088|552742|553131|514958|622760|628388|518377|622788|628313|628312|622750|622751|625145|622479|622480|622789|625140|622346|622347)\\d{10}$"
s22 = "^(518378|518379|518474|518475|518476|524865|525745|525746|547766|558868|622752|622753|622755|524864|622757|622758|622759|622761|622762|622763|622756|622754|622764|622765|558869|625905|625906|625907|625333)\\d{10}$"
s23 = "^(53591|49102|377677)\\d{11}$"
s24 = "^(620514|620025|620026|620210|620211|620019|620035|620202|620203|620048|620515|920000)\\d{10}$"
s25 = "^(620040|620531|620513|921000|620038)\\d{13}$"

s26 = "^(621284|436742|589970|620060|621081|621467|621598|621621|621700|622280|622700|623211|623668)\\d{13}$"
s27 = "^(421349|434061|434062|524094|526410|552245|621080|621082|621466|621488|621499|622966|622988|622382|621487|621083|621084|620107)\\d{10}$"
s28 = "^(436742193|622280193)\\d{10}$"
s29 = "^(553242)\\d{12}$"
s30 = "^(625362|625363|628316|628317|356896|356899|356895|436718|436738|436745|436748|489592|531693|532450|532458|544887|552801|557080|558895|559051|622166|622168|622708|625964|625965|625966|628266|628366|622381|622675|622676|622677)\\d{10}$"
s31 = "^(5453242|5491031|5544033)\\d{11}$"
s32 = "^(622725|622728|436728|453242|491031|544033|622707|625955|625956)\\d{10}$"
s33 = "^(53242|53243)\\d{11}$"

s34 = "^(622261|622260|622262|621002|621069|621436|621335)\\d{13}$"
s35 = "^(620013)\\d{10}$"
s36 = "^(405512|601428|405512|601428|622258|622259|405512|601428)\\d{11}$"
s37 = "^(49104|53783)\\d{11}$"
s38 = "^(434910|458123|458124|520169|522964|552853|622250|622251|521899|622253|622656|628216|622252|955590|955591|955592|955593|628218|625028|625029)\\d{10}$"
s39 = "^(622254|622255|622256|622257|622284)\\d{10}$"
s40 = "^(620021|620521)\\d{13}$"

s41 = "^(402658|410062|468203|512425|524011|622580|622588|622598|622609|95555|621286|621483|621485|621486|621299)(\\d{10}|\\d{11})$"
s42 = "^(690755)\\d{9}$"
s43 = "^(690755)\\d{12}$"
s44 = "^(356885|356886|356887|356888|356890|439188|439227|479228|479229|521302|356889|545620|545621|545947|545948|552534|552587|622575|622576|622577|622578|622579|545619|622581|622582|545623|628290|439225|518710|518718|628362|439226|628262|625802|625803)\\d{10}$"
s45 = "^(370285|370286|370287|370289)\\d{9}$"
s46 = "^(620520)\\d{13}$"
#民生银行
s47 = "^(622615|622616|622618|622622|622617|622619|415599|421393|421865|427570|427571|472067|472068|622620)\\d{10}$"
s48 = "^(545392|545393|545431|545447|356859|356857|407405|421869|421870|421871|512466|356856|528948|552288|622600|622601|622602|517636|622621|628258|556610|622603|464580|464581|523952|545217|553161|356858|622623|625912|625913|625911)\\d{10}$"
s49 = "^(377155|377152|377153|377158)\\d{9}$"

s50 = "^(303)\\d{13}$"
s51 = "^(90030)\\d{11}$"
s52 = "^(620535)\\d{13}$"
s53 = "^(620085|622660|622662|622663|622664|622665|622666|622667|622669|622670|622671|622672|622668|622661|622674|622673|620518|621489|621492)\\d{10}$"
s54 = "^(356837|356838|486497|622657|622685|622659|622687|625978|625980|625981|625979|356839|356840|406252|406254|425862|481699|524090|543159|622161|622570|622650|622655|622658|625975|625977|628201|628202|625339|625976)\\d{10}$"

s55 = "^(433670|433680|442729|442730|620082|622690|622691|622692|622696|622698|622998|622999|433671|968807|968808|968809|621771|621767|621768|621770|621772|621773|622453|622456)\\d{10}$"
s56 = "^(622459)\\d{11}$"
s57 = "^(376968|376969|376966)\\d{9}$"
s58 = "^(400360|403391|403392|404158|404159|404171|404172|404173|404174|404157|433667|433668|433669|514906|403393|520108|433666|558916|622678|622679|622680|622688|622689|628206|556617|628209|518212|628208|356390|356391|356392|622916|622918|622919)\\d{10}$"

s59 = "^(622630|622631|622632|622633|999999|621222|623020|623021|623022|623023)\\d{10}$"
s60 = "^(523959|528709|539867|539868|622637|622638|628318|528708|622636|625967|625968|625969)\\d{10}$"

s61 = "^(621626|623058)\\d{13}$"
s62 = "^(602907|622986|622989|622298|627069|627068|627066|627067|412963|415752|415753|622535|622536|622538|622539|998800|412962|622983)\\d{10}$"
s63 = "^(531659|622157|528020|622155|622156|526855|356869|356868|625360|625361|628296|435744|435745|483536|622525|622526|998801|998802)\\d{10}$"
s64 = "^(620010)\\d{10}$"
#兴业银行
s65 = "^(438589)\\d{12}$"
s66 = "^(90592)\\d{11}$"
s67 = "^(966666|622909|438588|622908)\\d{12}$"
s68 = "^(461982|486493|486494|486861|523036|451289|527414|528057|622901|622902|622922|628212|451290|524070|625084|625085|625086|625087|548738|549633|552398|625082|625083|625960|625961|625962|625963)\\d{10}$"
s69 = "^(620010)\\d{10}$"

s70 = "^(621050|622172|622985|622987|620522|622267|622278|622279|622468|622892|940021)\\d{12}$"
s71 = "^(438600)\\d{10}$"
s72 = "^(356827|356828|356830|402673|402674|486466|519498|520131|524031|548838|622148|622149|622268|356829|622300|628230|622269|625099|625953)\\d{10}$"

s73 = "^(622516|622517|622518|622521|622522|622523|984301|984303|621352|621793|621795|621796|621351|621390|621792|621791)\\d{10}$"
s74 = "^(84301|84336|84373|84385|84390|87000|87010|87030|87040|84380|84361|87050|84342)\\d{11}$"
s75 = "^(356851|356852|404738|404739|456418|498451|515672|356850|517650|525998|622177|622277|628222|622500|628221|622176|622276|622228|625957|625958|625993|625831)\\d{10}$"
s76 = "^(622520|622519)\\d{10}$"
s77 = "^(620530)\\d{13}$"

#	s78 = "^(622516|622517|622518|622521|622522|622523|984301|984303|621352|621793|621795|621796|621351|621390|621792|621791)\\d{10}$"
s79 = "^(622568|6858001|6858009|621462)\\d{13}$"
s80 = "^(9111)\\d{15}$"
s81 = "^(406365|406366|428911|436768|436769|436770|487013|491032|491033|491034|491035|491036|491037|491038|436771|518364|520152|520382|541709|541710|548844|552794|493427|622555|622556|622557|622558|622559|622560|528931|558894|625072|625071|628260|628259|625805|625806|625807|625808|625809|625810)\\d{10}$"
s82 = "^(685800|6858000)\\d{13}$"

s83 = "^(621268|622684|622884|621453)\\d{10}$"
s84 = "^(603445|622467|940016|621463)\\d{13}$"

s85 = "^(622449|940051)\\d{10}$"
s86 = "^(622450|628204)\\d{10}$"
#温州银行
s87 = "^(621977)\\d{10}$"
s88 = "^(622868|622899|628255)\\d{10}$"

s89 = "^(622877|622879|621775|623203)\\d{13}$"
s90 = "^(603601|622137|622327|622340|622366)\\d{11}$"
s91 = "^(628251|622651|625828)\\d{10}$"

s92 = "^(621076|622173|622131|621579|622876)\\d{13}$"
s93 = "^(504923|622422|622447|940076)\\d{10}$"
s94 = "^(628210|622283|625902)\\d{10}$"
#南京银行
s95 = "^(621777|622305|621259)\\d{10}$"
s96 = "^(622303|628242|622595|622596)\\d{10}$"

s97 = "^(621279|622281|622316|940022)\\d{10}$"
s98 = "^(621418)\\d{13}$"
s99 = "^(625903|622778|628207|512431|520194|622282|622318)\\d{10}$"
s100 = "^(625903|622778|628207|512431|520194|622282|622318)\\d{10}$"
#北京银行
s101 = "^(522001|622163|622853|628203|622851|622852)\\d{10}$"

s102 = "^(620088|621068|622138|621066|621560)\\d{13}$"
s103 = "^(625526|625186|628336)\\d{10}$"

s104 = "^(622946)\\d{10}$"
s105 = "^(622406|621442)\\d{11}$"
s106 = "^(622407|621443)\\d{13}$"
s107 = "^(622360|622361|625034|625096|625098)\\d{10}$"
#渣打银行
s108 = "^(622948|621740|622942|622994)\\d{10}$"
s109 = "^(622482|622483|622484)\\d{10}$"

s110 = "^(621062|621063)\\d{10}$"
s111 = "^(625076|625077|625074|625075|622371|625091)\\d{10}$"
#东亚银行
s112 = "^(622933|622938|623031|622943|621411)\\d{13}$"
s113 = "^(622372|622471|622472|622265|622266|625972|625973)\\d{10}$"
s114 = "^(622365)\\d{11}$"

s115 = "^(621469|621625)\\d{13}$"
s116 = "^(622128|622129|623035)\\d{10}$"
s117 = "^(909810|940035|621522|622439)\\d{12}$"

s118 = "^(622328|940062|623038)\\d{13}$"
s119 = "^(625288|625888)\\d{10}$"

s120 = "^(622333|940050)\\d{10}$"
s121 = "^(621439|623010)\\d{13}$"
s122 = "^(622888)\\d{10}$"

s123 = "^(622302)\\d{10}$"
s124 = "^(622477|622509|622510|622362|621018|621518)\\d{13}$"

s125 = "^(622297|621277)\\d{10}$"
s126 = "^(622375|622489)\\d{11}$"
s127 = "^(622293|622295|622296|622373|622451|622294|625940)\\d{10}$"

s128 = "^(622871|622958|622963|622957|622861|622932|622862|621298)\\d{10}$"
s129 = "^(622798|625010|622775|622785)\\d{10}$"

s130 = "^(621016|621015)\\d{13}$"
s131 = "^(622487|622490|622491|622492)\\d{10}$"
s132 = "^(622487|622490|622491|622492|621744|621745|621746|621747)\\d{11}$"

s133 = "^(623078)\\d{13}$"
s134 = "^(622384|940034)\\d{11}$"

s135 = "^(940015|622331)\\d{12}$"
s136 = "^(6091201)\\d{11}$"
s137 = "^(622426|628205)\\d{10}$"

s138 = "^(621019|622309|621019)\\d{13}$"
s139 = "^(6223091100|6223092900|6223093310|6223093320|6223093330|6223093370|6223093380|6223096510|6223097910)\\d{9}$"

s140 = "^(621213|621289|621290|621291|621292|621042|621743)\\d{13}$"
s141 = "^(623041|622351)\\d{10}$"
s142 = "^(625046|625044|625058|622349|622350)\\d{10}$"
s143 = "^(620208|620209|625093|625095)\\d{10}$"
#厦门银行
s144 = "^(622393|940023)\\d{10}$"
s145 = "^(6886592)\\d{11}$"
s146 = "^(623019|621600|)\\d{13}$"

s147 = "^(622388)\\d{10}$"
s148 = "^(621267|623063)\\d{12}$"
s149 = "^(620043|)\\d{12}$"

s150 = "^(622865|623131)\\d{13}$"
s151 = "^(940012)\\d{10}$"
s152 = "^(622178|622179|628358)\\d{10}$"
#汉口银行
s153 = "^(990027)\\d{12}$"
s154 = "^(622325|623105|623029)\\d{10}$"

s155 = "^(566666)\\d{12}$"
s156 = "^(622455|940039)\\d{13}$"
s157 = "^(623108|623081)\\d{10}$"
s158 = "^(622466|628285)\\d{10}$"

s159 = "^(603708)\\d{11}$"
s160 = "^(622993|623069|623070|623172|623173)\\d{13}$"
s161 = "^(622383|622385|628299)\\d{10}$"

s162 = "^(622498|622499|623000|940046)\\d{13}$"
s163 = "^(622921|628321)\\d{10}$"
#乌鲁木齐商业银行
s164 = "^(621751|622143|940001|621754)\\d{13}$"
s165 = "^(622476|628278)\\d{10}$"

s166 = "^(622486)\\d{10}$"
s167 = "^(603602|623026|623086)\\d{12}$"
s168 = "^(628291)\\d{10}$"

s169 = "^(622152|622154|622996|622997|940027|622153|622135|621482|621532)\\d{13}$"
s170 = "^(622442)\\d{11}$"
s171 = "^(940053)\\d{12}$"
s172 = "^(622442|623099)\\d{13}$"

s173 = "^(622421)\\d{13}$"
s174 = "^(940056)\\d{11}$"
s175 = "^(96828)\\d{11}$"
#宁夏银行
s176 = "^(621529|622429|621417|623089|623200)\\d{13}$"
s177 = "^(628214|625529|622428)\\d{10}$"

s178 = "^(9896)\\d{12}$"
s179 = "^(622134|940018|623016)\\d{10}$"

s180 = "^(621577|622425)\\d{13}$"
s181 = "^(940049)\\d{12}$"
s182 = "^(622425)\\d{11}$"

s183 = "^(622139|940040|628263)\\d{10}$"
s184 = "^(621242|621538|621496)\\d{13}$"

s185 = "^(621252|622146|940061|628239)\\d{10}$"
s186 = "^(621419|623170)\\d{13}$"

s187 = "^(62249802|94004602)\\d{11}$"
s188 = "^(621237|623003)\\d{13}$"
#青海银行
s189 = "^(622310|940068)\\d{11}$"
s190 = "^(622817|628287|625959)\\d{10}$"
s191 = "^(62536601)\\d{8}$"

s192 = "^(622427)\\d{10}$"
s193 = "^(940069)\\d{11}$"
s194 = "^(623039)\\d{13}$"
s195 = "^(622321|628273)\\d{10}$"
s196 = "^(625001)\\d{10}$"

s197 = "^(694301)\\d{12}$"
s198 = "^(940071|622368|621446)\\d{13}$"
s199 = "^(625901|622898|622900|628281|628282|622806|628283)\\d{10}$"
s200 = "^(620519)\\d{13}$"

s201 = "^(683970|940074)\\d{12}$"
s202 = "^(622370)\\d{13}$"
s203 = "^(621437)\\d{13}$"
s204 = "^(628319)\\d{10}$"

s205 = "^(622336|621760)\\d{11}$"
s206 = "^(622165)\\d{10}$"
s207 = "^(622315|625950|628295)\\d{10}$"

s208 = "^(621037|621097|621588|622977)\\d{13}$"
s209 = "^(62321601)\\d{11}$"
s210 = "^(622860)\\d{10}$"
s211 = "^(622644|628333)\\d{10}$"

s212 = "^(622478|940013|621495)\\d{10}$"
s213 = "^(625500)\\d{10}$"
s214 = "^(622611|622722|628211|625989)\\d{10}$"

s215 = "^(622717)\\d{10}$"
s216 = "^(628275|622565|622287)\\d{10}$"
#内蒙古银行
s217 = "^(622147|621633)\\d{13}$"
s218 = "^(628252)\\d{10}$"

s219 = "^(623001)\\d{10}$"
s220 = "^(628227)\\d{10}$"

s221 = "^(621456)\\d{11}$"
s222 = "^(621562)\\d{13}$"
s223 = "^(628219)\\d{10}$"

s224 = "^(621037|621097|621588|622977)\\d{13}$"
s225 = "^(62321601)\\d{11}$"
s226 = "^(622475|622860)\\d{10}$"
s227 = "^(625588)\\d{10}$"
s228 = "^(622270|628368|625090|622644|628333)\\d{10}$"

s229 = "^(623088)\\d{13}$"
s230 = "^(622829|628301|622808|628308)\\d{10}$"

s231 = "^(622127|622184|621701|621251|621589|623036)\\d{13}$"
s232 = "^(628232|622802|622290)\\d{10}$"

s233 = "^(622531|622329)\\d{13}$"
s234 = "^(622829|628301)\\d{10}$"

s235 = "^(621578|623066|622452|622324)\\d{13}$"
s236 = "^(622815|622816|628226)\\d{10}$"
s237 = "^(622906|628386|625519|625506)\\d{10}$"

s238 = "^(621592)\\d{10}$"
s239 = "^(628392)\\d{10}$"
#商丘市商业银行
s240 = "^(621748)\\d{13}$"
s241 = "^(628271)\\d{10}$"

s242 = "^(621366|621388)\\d{13}$"
s243 = "^(628328)\\d{10}$"

s244 = "^(621239|623068)\\d{13}$"
s245 = "^(621653004)\\d{10}$"
s246 = "^(622169|621519|621539|623090)\\d{13}$"
s247 = "^(621238|620528)\\d{13}$"
s248 = "^(628382|625158)\\d{10}$"

s249 = "^(621004)\\d{12}$"
s250 = "^(628217)\\d{10}$"

s251 = "^(621416)\\d{10}$"
s252 = "^(628217)\\d{10}$"
#德州银行
s253 = "^(622937)\\d{13}$"
s254 = "^(628397)\\d{10}$"
#德州银行
ss254 = "^(628397)\\d{10}$"
#云南农村信用社
s255 = "^(622469|628307)\\d{10}$"
#柳州银行
s256 = "^(622292|622291|621412)\\d{12}$"
s257 = "^(622880|622881)\\d{10}$"
s258 = "^(62829)\\d{10}$"

s259 = "^(623102)\\d{10}$"
s260 = "^(628234)\\d{10}$"

s261 = "^(628306)\\d{10}$"

s262 = "^(622391|940072)\\d{10}$"
s263 = "^(628391)\\d{10}$"

s264 = "^(622967|940073)\\d{13}$"
s265 = "^(628233)\\d{10}$"
s266 = "^(628257)\\d{10}$"

s267 = "^(621269|622275)\\d{10}$"
s268 = "^(940006)\\d{11}$"
s269 = "^(628305)\\d{11}$"
#贵阳银行
s270 = "^(622133|621735)\\d{13}$"
s271 = "^(888)\\d{13}$"
s272 = "^(628213)\\d{10}$"

s273 = "^(622990|940003)\\d{11}$"
s274 = "^(628261)\\d{10}$"

s275 = "^(622311|940057)\\d{11}$"
s276 = "^(628311)\\d{10}$"

s277 = "^(622363|940048)\\d{13}$"
s278 = "^(628270)\\d{10}$"
#	葫芦岛市商业银行
s279 = "^(622398|940054)\\d{10}$"

s280 = "^(940055)\\d{11}$"
s281 = "^(622397)\\d{11}$"

s282 = "^(603367|622878)\\d{12}$"
s283 = "^(622397)\\d{11}$"

s284 = "^(603506)\\d{13}$"

s285 = "^(622399|940043)\\d{11}$"

s286 = "^(622420|940041)\\d{11}$"

s287 = "^(622338)\\d{13}$"
s288 = "^(940032)\\d{10}$"

s289 = "^(622394|940025)\\d{10}$"

s290 = "^(621245)\\d{10}$"

s291 = "^(621328)\\d{13}$"

s292 = "^(621651)\\d{13}$"

s293 = "^(621077)\\d{10}$"

s294 = "^(622409|621441)\\d{13}$"
s295 = "^(622410|621440)\\d{11}$"
s296 = "^(622950|622951)\\d{10}$"
s297 = "^(625026|625024|622376|622378|622377|625092)\\d{10}$"

s298 = "^(622359|940066)\\d{13}$"

s299 = "^(622886)\\d{10}$"

s300 = "^(940008|622379)\\d{13}"
s301 = "^(628379)\\d{10}$"

s302 = "^(620011|620027|620031|620039|620103|620106|620120|620123|620125|620220|620278|620812|621006|621011|621012|621020|621023|621025|621027|621031|620132|621039|621078|621220|621003)\\d{10}$"
s303 = "^(625003|625011|625012|625020|625023|625025|625027|625031|621032|625039|625078|625079|625103|625106|625006|625112|625120|625123|625125|625127|625131|625032|625139|625178|625179|625220|625320|625111|625132|625244)\\d{10}$"

s304 = "^(622355|623042)\\d{10}$"
s305 = "^(621043|621742)\\d{13}$"
s306 = "^(622352|622353|625048|625053|625060)\\d{10}$"
s307 = "^(620206|620207)\\d{10}$"

s308 = "^(622547|622548|622546)\\d{13}$"
s309 = "^(625198|625196|625147)\\d{10}$"
s310 = "^(620072)\\d{13}$"
s311 = "^(620204|620205)\\d{10}$"

s312 = "^(621064|622941|622974)\\d{10}$"
s313 = "^(622493)\\d{10}$"

s314 = "^(621274|621324)\\d{13}$"

def get_bank_name(card_no):
	if (re.match(s1, card_no) or re.match(s2, card_no) or re.match(s3, card_no)) :
		return "邮储银行"
	elif (re.match(s4, card_no) or re.match(s5, card_no) or re.match(s6, card_no) or re.match(s7, card_no) or re.match(s8, card_no) or re.match(s9, card_no) or re.match(s10, card_no) or re.match(s11, card_no) or re.match(s12, card_no) or re.match(s13, card_no)) :
		return "工商银行"
	elif (re.match(s14, card_no) or re.match(s15, card_no) or re.match(s16, card_no) or re.match(s17, card_no) or re.match(s18, card_no)) :
		return "农业银行"
	elif (re.match(s19, card_no) or re.match(s20, card_no) or re.match(s21, card_no) or re.match(s22, card_no) or re.match(s23, card_no) or re.match(s24, card_no) or re.match(s25, card_no)) :
		return "中国银行"
	elif (re.match(s26, card_no) or re.match(s27, card_no) or re.match(s28, card_no) or re.match(s29, card_no) or re.match(s30, card_no) or re.match(s31, card_no) or re.match(s32, card_no) or re.match(s33, card_no)) :
		return "建设银行"
	elif (re.match(s34, card_no) or re.match(s35, card_no) or re.match(s36, card_no) or re.match(s37, card_no) or re.match(s38, card_no) or re.match(s39, card_no) or re.match(s40, card_no)) :
		return "交通银行"
	elif (re.match(s41, card_no) or re.match(s42, card_no) or re.match(s43, card_no) or re.match(s44, card_no) or re.match(s45, card_no) or re.match(s46, card_no)) :
		return "招商银行"
	elif (re.match(s47, card_no) or re.match(s48, card_no) or re.match(s49, card_no)) :
		return "民生银行"
	elif (re.match(s50, card_no) or re.match(s51, card_no) or re.match(s52, card_no) or re.match(s53, card_no) or re.match(s54, card_no)) :
		return "光大银行"
	elif (re.match(s55, card_no) or re.match(s56, card_no) or re.match(s57, card_no) or re.match(s58, card_no)) :
		return "中信银行"
	elif (re.match(s59, card_no) or re.match(s60, card_no)) :
		return "华夏银行"
	elif (re.match(s61, card_no) or re.match(s62, card_no) or re.match(s63, card_no) or re.match(s64, card_no)) :
		return "平安银行"
	elif (re.match(s65, card_no) or re.match(s66, card_no) or re.match(s67, card_no) or re.match(s68, card_no) or re.match(s69, card_no)) :
		return "兴业银行"
	elif (re.match(s70, card_no) or re.match(s71, card_no) or re.match(s72, card_no)) :
		return "上海银行"
	elif (re.match(s73, card_no) or re.match(s74, card_no) or re.match(s75, card_no) or re.match(s76, card_no) or re.match(s77, card_no)) :
		return "浦发银行"
	elif (re.match(s79, card_no) or re.match(s80, card_no) or re.match(s81, card_no) or re.match(s82, card_no)) :
		return "广发银行"
	elif (re.match(s83, card_no)) :
		return "渤海银行"
	elif (re.match(s84, card_no)) :
		return "广州银行"
	elif (re.match(s85, card_no) or re.match(s86, card_no)) :
		return "金华银行"
	elif (re.match(s87, card_no) or re.match(s88, card_no)) :
		return "温州银行"
	elif (re.match(s89, card_no) or re.match(s90, card_no) or re.match(s91, card_no)) :
		return "徽商银行"
	elif (re.match(s92, card_no) or re.match(s93, card_no) or re.match(s94, card_no)) :
		return "江苏银行"
	elif (re.match(s95, card_no) or re.match(s96, card_no)) :
		return "南京银行"
	elif (re.match(s97, card_no) or re.match(s98, card_no) or re.match(s99, card_no)) :
		return "宁波银行"
	elif (re.match(s100, card_no) or re.match(s101, card_no)) :
		return "北京银行"
	elif (re.match(s102, card_no) or re.match(s103, card_no)) :
		return "北京农村商业银行"
	elif (re.match(s104, card_no) or re.match(s105, card_no) or re.match(s106, card_no) or re.match(s107, card_no)) :
		return "汇丰银行"
	elif (re.match(s108, card_no) or re.match(s109, card_no)) :
		return "渣打银行"
	elif (re.match(s110, card_no) or re.match(s111, card_no)) :
		return "花旗银行"
	elif (re.match(s112, card_no) or re.match(s113, card_no) or re.match(s114, card_no)) :
		return "东亚银行"
	elif (re.match(s115, card_no)) :
		return "广东华兴银行"
	elif (re.match(s116, card_no)) :
		return "深圳农村商业银行"
	elif (re.match(s117, card_no)) :
		return "广州农村商业银行"
	elif (re.match(s118, card_no) or re.match(s119, card_no)) :
		return "东莞农村商业银行"
	elif (re.match(s120, card_no) or re.match(s121, card_no) or re.match(s122, card_no)) :
		return "东莞市商业银行"
	elif (re.match(s123, card_no) or re.match(s124, card_no)) :
		return "广东省农村信用社联合社"
	elif (re.match(s125, card_no) or re.match(s126, card_no) or re.match(s127, card_no)) :
		return "大新银行"
	elif (re.match(s128, card_no) or re.match(s129, card_no)) :
		return "永享银行"
	elif (re.match(s130, card_no) or re.match(s131, card_no) or re.match(s132, card_no)) :
		return "星展银行香港有限公司"
	elif (re.match(s133, card_no) or re.match(s134, card_no)) :
		return "恒丰银行"
	elif (re.match(s136, card_no) or re.match(s135, card_no) or re.match(s137, card_no)) :
		return "天津市商业银行"
	elif (re.match(s138, card_no) or re.match(s139, card_no)) :
		return "浙商银行"
	elif (re.match(s140, card_no) or re.match(s141, card_no) or re.match(s142, card_no) or re.match(s143, card_no)) :
		return "南洋商业银行"
	elif (re.match(s144, card_no) or re.match(s145, card_no) or re.match(s146, card_no)) :
		return "厦门银行"
	elif (re.match(s147, card_no) or re.match(s148, card_no) or re.match(s149, card_no)) :
		return "福建海峡银行"
	elif (re.match(s150, card_no) or re.match(s151, card_no) or re.match(s152, card_no)) :
		return "吉林银行"
	elif (re.match(s153, card_no) or re.match(s154, card_no)) :
		return "汉口银行"
	elif (re.match(s155, card_no) or re.match(s156, card_no) or re.match(s157, card_no) or re.match(s158, card_no)) :
		return "盛京银行"
	elif (re.match(s159, card_no) or re.match(s160, card_no) or re.match(s161, card_no)) :
		return "大连银行"
	elif (re.match(s162, card_no) or re.match(s163, card_no)) :
		return "河北银行"
	elif (re.match(s164, card_no) or re.match(s165, card_no)) :
		return "乌鲁木齐商业银行"
	elif (re.match(s166, card_no) or re.match(s167, card_no) or re.match(s168, card_no)) :
		return "绍兴银行"
	elif (re.match(s169, card_no)) :
		return "成都商业银行"
	elif (re.match(s170, card_no) or re.match(s171, card_no) or re.match(s172, card_no)) :
		return "抚顺银行"
	elif (re.match(s173, card_no) or re.match(s174, card_no) or re.match(s175, card_no)) :
		return "郑州银行"
	elif (re.match(s176, card_no) or re.match(s177, card_no)) :
		return "宁夏银行"
	elif (re.match(s178, card_no) or re.match(s179, card_no)) :
		return "重庆银行"
	elif (re.match(s180, card_no) or re.match(s181, card_no) or re.match(s182, card_no)) :
		return "哈尔滨银行"
	elif (re.match(s183, card_no) or re.match(s184, card_no)) :
		return "兰州银行"
	elif (re.match(s185, card_no) or re.match(s186, card_no)) :
		return "青岛银行"
	elif (re.match(s187, card_no) or re.match(s188, card_no)) :
		return "秦皇岛市商业银行"
	elif (re.match(s189, card_no) or re.match(s190, card_no) or re.match(s191, card_no)) :
		return "青海银行"
	elif (re.match(s192, card_no) or re.match(s193, card_no) or re.match(s194, card_no) or re.match(s195, card_no) or re.match(s196, card_no)) :
		return "台州银行"
	elif (re.match(s197, card_no) or re.match(s198, card_no) or re.match(s199, card_no) or re.match(s200, card_no)) :
		return "长沙银行"
	elif (re.match(s201, card_no) or re.match(s202, card_no) or re.match(s203, card_no) or re.match(s204, card_no)) :
		return "泉州银行"
	elif (re.match(s205, card_no) or re.match(s206, card_no) or re.match(s207, card_no)) :
		return "包商银行"
	elif (re.match(s208, card_no) or re.match(s209, card_no) or re.match(s210, card_no) or re.match(s211, card_no)) :
		return "龙江银行"
	elif (re.match(s212, card_no) or re.match(s213, card_no) or re.match(s214, card_no)) :
		return "上海农商银行"
	elif (re.match(s215, card_no) or re.match(s216, card_no)) :
		return "浙江泰隆商业银行"
	elif (re.match(s217, card_no) or re.match(s218, card_no)) :
		return "内蒙古银行"
	elif (re.match(s219, card_no) or re.match(s220, card_no)) :
		return "广西北部湾银行"
	elif (re.match(s221, card_no) or re.match(s222, card_no) or re.match(s223, card_no)) :
		return "桂林银行"
	elif (re.match(s224, card_no) or re.match(s225, card_no) or re.match(s226, card_no) or re.match(s227, card_no) or re.match(s228, card_no)) :
		return "龙江银行"
	elif (re.match(s229, card_no) or re.match(s230, card_no)) :
		return "成都农村商业银行"
	elif (re.match(s231, card_no) or re.match(s232, card_no)) :
		return "福建省农村信用社联合社"
	elif (re.match(s233, card_no) or re.match(s234, card_no)) :
		return "天津农村商业银行"
	elif (re.match(s235, card_no) or re.match(s236, card_no)) :
		return "江苏省农村信用社联合社"
	elif (re.match(s237, card_no)) :
		return "湖南省农村信用社联合社"
	elif (re.match(s238, card_no) or re.match(s239, card_no)) :
		return "江西省农村信用社联合社"
	elif (re.match(s240, card_no) or re.match(s241, card_no)) :
		return "商丘市商业银行"
	elif (re.match(s242, card_no) or re.match(s243, card_no)) :
		return "华融湘江银行"
	elif (re.match(s244, card_no)) :
		return "衡水市商业银行"
	elif (re.match(s245, card_no)) :
		return "重庆南川石银村镇银行"
	elif (re.match(s246, card_no)) :
		return "湖南省农村信用社联合社"
	elif (re.match(s247, card_no)) :
		return "邢台银行"
	elif (re.match(s248, card_no)) :
		return "临汾市尧都区农村信用合作联社"
	elif (re.match(s249, card_no) or re.match(s250, card_no)) :
		return "东营银行"
	elif (re.match(s251, card_no) or re.match(s252, card_no)) :
		return "上饶银行"
	elif (re.match(s253, card_no) or re.match(s254, card_no)) :
		return "德州银行"
	elif (re.match(ss254, card_no)) :
		return "承德银行"
	elif (re.match(s255, card_no)) :
		return "云南农村信用社"
	elif (re.match(s257, card_no) or re.match(s258, card_no) or re.match(s256, card_no)) :
		return "柳州银行"
	elif (re.match(s259, card_no) or re.match(s260, card_no)) :
		return "威海市商业银行"
	elif (re.match(s261, card_no)) :
		return "湖州银行"
	elif (re.match(s262, card_no) or re.match(s263, card_no)) :
		return "潍坊银行"
	elif (re.match(s264, card_no) or re.match(s265, card_no)) :
		return "赣州银行"
	elif (re.match(s266, card_no)) :
		return "日照银行"
	elif (re.match(s267, card_no) or re.match(s268, card_no) or re.match(s269, card_no)) :
		return "南昌银行"
	elif (re.match(s270, card_no) or re.match(s271, card_no) or re.match(s272, card_no)) :
		return "贵阳银行"
	elif (re.match(s273, card_no) or re.match(s274, card_no)) :
		return "锦州银行"
	elif (re.match(s275, card_no) or re.match(s276, card_no)) :
		return "齐商银行"
	elif (re.match(s277, card_no) or re.match(s278, card_no)) :
		return "珠海华润银行"
	elif (re.match(s279, card_no)) :
		return "葫芦岛市商业银行"
	elif (re.match(s280, card_no) or re.match(s281, card_no)) :
		return "宜昌市商业银行"
	elif (re.match(s282, card_no) or re.match(s283, card_no)) :
		return "杭州商业银行"
	elif (re.match(s284, card_no)) :
		return "苏州市商业银行"
	elif (re.match(s285, card_no)) :
		return "辽阳银行"
	elif (re.match(s286, card_no)) :
		return "洛阳银行"
	elif (re.match(s287, card_no) or re.match(s288, card_no)) :
		return "焦作市商业银行"
	elif (re.match(s289, card_no)) :
		return "镇江市商业银行"
	elif (re.match(s290, card_no)) :
		return "法国兴业银行"
	elif (re.match(s291, card_no)) :
		return "大华银行"
	elif (re.match(s292, card_no)) :
		return "企业银行"
	elif (re.match(s293, card_no)) :
		return "华侨银行"
	elif (re.match(s294, card_no) or re.match(s295, card_no) or re.match(s296, card_no) or re.match(s297, card_no)) :
		return "恒生银行"
	elif (re.match(s298, card_no)) :
		return "临沂商业银行"
	elif (re.match(s299, card_no)) :
		return "烟台商业银行"
	elif (re.match(s300, card_no) or re.match(s301, card_no)) :
		return "齐鲁银行"
	elif (re.match(s302, card_no) or re.match(s303, card_no)) :
		return "BC卡公司"
	elif (re.match(s304, card_no) or re.match(s305, card_no) or re.match(s306, card_no) or re.match(s307, card_no)) :
		return "集友银行"
	elif (re.match(s308, card_no) or re.match(s309, card_no) or re.match(s310, card_no) or re.match(s311, card_no)) :
		return "大丰银行"
	elif (re.match(s312, card_no) or re.match(s313, card_no)) :
		return "AEON信贷财务亚洲有限公司"
	elif (re.match(s314, card_no)) :
		return "澳门BDA"
	else :
		return "未知"



def get_card_type(card_no):
	if (re.match(s1, card_no) or re.match(s2, card_no) or re.match(s4, card_no) or re.match(s5, card_no) or re.match(s6, card_no) or re.match(s7, card_no)
	or re.match(s14, card_no) or re.match(s15, card_no) or re.match(s16, card_no)
	or re.match(s19, card_no) or re.match(s20, card_no) or re.match(s26, card_no) or re.match(s27, card_no) or re.match(s28, card_no)
	or re.match(s34, card_no) or re.match(s35, card_no) or re.match(s36, card_no) or re.match(s41, card_no) or re.match(s42, card_no) or re.match(s43, card_no)
	or re.match(s47, card_no) or re.match(s50, card_no) or re.match(s51, card_no) or re.match(s52, card_no) or re.match(s53, card_no)
	or re.match(s55, card_no) or re.match(s56, card_no) or re.match(s59, card_no) or re.match(s61, card_no) or re.match(s62, card_no)
	or re.match(s65, card_no) or re.match(s66, card_no) or re.match(s67, card_no) or re.match(s70, card_no) or re.match(s71, card_no)
	or re.match(s73, card_no) or re.match(s74, card_no) or re.match(s79, card_no) or re.match(s80, card_no)
	or re.match(s83, card_no) or re.match(s84, card_no) or re.match(s85, card_no) or re.match(s87, card_no) or re.match(s89, card_no) or re.match(s90, card_no)
	or re.match(s92, card_no) or re.match(s93, card_no) or re.match(s95, card_no) or re.match(s97, card_no) or re.match(s98, card_no)
	or re.match(s100, card_no) or re.match(s102, card_no) or re.match(s104, card_no) or re.match(s105, card_no) or re.match(s106, card_no)
	or re.match(s108, card_no) or re.match(s110, card_no) or re.match(s112, card_no) or re.match(s115, card_no) or re.match(s116, card_no) or re.match(s117, card_no)
	or re.match(s118, card_no) or re.match(s120, card_no) or re.match(s121, card_no) or re.match(s123, card_no) or re.match(s124, card_no)
	or re.match(s125, card_no) or re.match(s126, card_no) or re.match(s128, card_no) or re.match(s130, card_no) or re.match(s131, card_no) or re.match(s132, card_no)
	or re.match(s133, card_no) or re.match(s134, card_no) or re.match(s135, card_no) or re.match(s136, card_no) or re.match(s138, card_no) or re.match(s139, card_no)
	or re.match(s140, card_no) or re.match(s141, card_no) or re.match(s144, card_no) or re.match(s145, card_no) or re.match(s146, card_no)
	or re.match(s147, card_no) or re.match(s148, card_no) or re.match(s150, card_no) or re.match(s151, card_no) or re.match(s152, card_no)
	or re.match(s153, card_no) or re.match(s154, card_no) or re.match(s155, card_no) or re.match(s156, card_no) or re.match(s157, card_no) or re.match(s159, card_no)
	or re.match(s160, card_no) or re.match(s162, card_no) or re.match(s164, card_no) or re.match(s166, card_no) or re.match(s167, card_no)
	or re.match(s169, card_no) or re.match(s170, card_no) or re.match(s171, card_no) or re.match(s172, card_no) or re.match(s173, card_no) or re.match(s174, card_no) or re.match(s175, card_no)
	or re.match(s176, card_no) or re.match(s178, card_no) or re.match(s179, card_no) or re.match(s180, card_no) or re.match(s181, card_no) or re.match(s182, card_no)
	or re.match(s183, card_no) or re.match(s184, card_no) or re.match(s185, card_no) or re.match(s186, card_no) or re.match(s187, card_no) or re.match(s188, card_no)
	or re.match(s189, card_no) or re.match(s192, card_no) or re.match(s193, card_no) or re.match(s194, card_no) or re.match(s197, card_no) or re.match(s198, card_no)
	or re.match(s201, card_no) or re.match(s202, card_no) or re.match(s203, card_no) or re.match(s205, card_no) or re.match(s206, card_no) or re.match(s208, card_no)
	or re.match(s209, card_no) or re.match(s210, card_no) or re.match(s212, card_no) or re.match(s217, card_no) or re.match(s219, card_no)
	or re.match(s221, card_no) or re.match(s222, card_no) or re.match(s224, card_no) or re.match(s225, card_no) or re.match(s226, card_no) or re.match(s229, card_no)
	or re.match(s231, card_no) or re.match(s233, card_no) or re.match(s235, card_no) or re.match(s238, card_no) or re.match(s240, card_no) or re.match(s242, card_no)
	or re.match(s244, card_no) or re.match(s245, card_no) or re.match(s246, card_no) or re.match(s247, card_no) or re.match(s249, card_no) or re.match(s251, card_no)
	or re.match(s253, card_no) or re.match(s256, card_no) or re.match(s257, card_no) or re.match(s259, card_no) or re.match(s262, card_no) or re.match(s264, card_no)
	or re.match(s267, card_no) or re.match(s268, card_no) or re.match(s270, card_no) or re.match(s271, card_no) or re.match(s273, card_no) or re.match(s275, card_no) or re.match(s277, card_no)
	or re.match(s279, card_no) or re.match(s280, card_no) or re.match(s282, card_no) or re.match(s284, card_no) or re.match(s285, card_no) or re.match(s286, card_no)
	or re.match(s287, card_no) or re.match(s288, card_no) or re.match(s289, card_no) or re.match(s290, card_no) or re.match(s291, card_no) or re.match(s292, card_no)
	or re.match(s293, card_no) or re.match(s294, card_no) or re.match(s295, card_no) or re.match(s296, card_no) or re.match(s298, card_no) or re.match(s299, card_no) or re.match(s300, card_no)
	or re.match(s302, card_no) or re.match(s304, card_no) or re.match(s305, card_no) or re.match(s308, card_no) or re.match(s309, card_no)
	or re.match(s312, card_no) or re.match(s314, card_no)) :
		return "储蓄卡";
	elif (re.match(s3, card_no) or re.match(s8, card_no) or re.match(s9, card_no) or re.match(s10, card_no) or re.match(s17, card_no) or re.match(s21, card_no)
	or re.match(s29, card_no) or re.match(s30, card_no) or re.match(s31, card_no) or re.match(s37, card_no) or re.match(s38, card_no)
	or re.match(s44, card_no) or re.match(s45, card_no) or re.match(s48, card_no) or re.match(s49, card_no) or re.match(s54, card_no)
	or re.match(s57, card_no) or re.match(s58, card_no) or re.match(s60, card_no) or re.match(s63, card_no) or re.match(s68, card_no) or re.match(s72, card_no)
	or re.match(s75, card_no) or re.match(s81, card_no) or re.match(s82, card_no) or re.match(s86, card_no) or re.match(s88, card_no)
	or re.match(s91, card_no) or re.match(s94, card_no) or re.match(s96, card_no) or re.match(s99, card_no) or re.match(s101, card_no) or re.match(s103, card_no)
	or re.match(s107, card_no) or re.match(s109, card_no) or re.match(s111, card_no) or re.match(s113, card_no) or re.match(s114, card_no) or re.match(s119, card_no)
	or re.match(s122, card_no) or re.match(s127, card_no) or re.match(s129, card_no) or re.match(s137, card_no) or re.match(s142, card_no)
	or re.match(s158, card_no) or re.match(s161, card_no) or re.match(s163, card_no) or re.match(s165, card_no) or re.match(s167, card_no)
	or re.match(s177, card_no) or re.match(s191, card_no) or re.match(s190, card_no) or re.match(s195, card_no) or re.match(s199, card_no)
	or re.match(s204, card_no) or re.match(s207, card_no) or re.match(s211, card_no) or re.match(s214, card_no) or re.match(s216, card_no)
	or re.match(s218, card_no) or re.match(s220, card_no) or re.match(s223, card_no) or re.match(s228, card_no) or re.match(s230, card_no) or re.match(s232, card_no)
	or re.match(s234, card_no) or re.match(s236, card_no) or re.match(s237, card_no) or re.match(s239, card_no) or re.match(s241, card_no) or re.match(s243, card_no)
	or re.match(s248, card_no) or re.match(s250, card_no) or re.match(s252, card_no) or re.match(s254, card_no) or re.match(ss254, card_no) or re.match(s255, card_no)
	or re.match(s258, card_no) or re.match(s260, card_no) or re.match(s261, card_no) or re.match(s263, card_no) or re.match(s265, card_no) or re.match(s266, card_no)
	or re.match(s269, card_no) or re.match(s272, card_no) or re.match(s274, card_no) or re.match(s276, card_no) or re.match(s278, card_no) or re.match(s281, card_no)
	or re.match(s283, card_no) or re.match(s297, card_no) or re.match(s301, card_no) or re.match(s303, card_no) or re.match(s306, card_no)
	or re.match(s313, card_no)) :
		return "信用卡(贷记卡)";
	elif (re.match(s11, card_no) or re.match(s18, card_no) or re.match(s22, card_no) or re.match(s23, card_no) or re.match(s32, card_no) or re.match(s33, card_no)
	or re.match(s39, card_no) or re.match(s76, card_no) or re.match(s196, card_no) or re.match(s213, card_no) or re.match(s215, card_no)
	or re.match(s227, card_no)) :
		return "准贷记卡";
	elif (re.match(s12, card_no) or re.match(s13, card_no) or re.match(s24, card_no) or re.match(s25, card_no) or re.match(s40, card_no)
	or re.match(s46, card_no) or re.match(s64, card_no) or re.match(s69, card_no) or re.match(s77, card_no) or re.match(s143, card_no)
	or re.match(s149, card_no) or re.match(s200, card_no) or re.match(s307, card_no) or re.match(s310, card_no) or re.match(s311, card_no)) :
		return "预付费卡";
	else :
		return "未知";

def excute(card_no):
	bank_name=get_bank_name(card_no)
	card_type=get_card_type(card_no)
	return bank_name,card_type


if __name__ == '__main__':
	card_no='6226190602392981'
	bank_name,card_type=excute(card_no)
	print(bank_name,card_type)
