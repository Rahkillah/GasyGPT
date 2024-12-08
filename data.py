# utilisation d'un dictionnaire pour représenter un fichier JSON d'intentions
# ATO IHAN MANAMPY AN LE PDF F AZA KITIHAN TSONY NY CODE REHETRA AMBINY ANY AMBANY ANY
data = {
    "intents": [
        {
            "tag": "slt",
            "patterns": ["Salama ", "Ao veee", "yo", "Salut", "slt"],
            "fampidirana": ["mmh "],
            "responses": [
                "Salamee, in n azoko atao anao ?",
                "salut, in n azo atao ?",
                "slt, in n ketrika androany ",
                "ieee, in vaovao ",
                "ok, in ny ataontsika androany ",
            ],
            "famaranana": ["", "", "", "", ""],
        },
        {
            "tag": "aretina",
            "patterns": ["fadim-bolana", "regles", "tonga fotoana", "menstruations"],
            "fampidirana": [
                "aaayy : ",
                "aay vee, ",
                "otranzao ny fanaovana azy : ",
                "ok, ",
                "ty ar : ",
            ],
            "responses": [
                "misotro rano mafana betsaka, mihinana persil 1 andro mialoha, orana citron ny kibo\\nmihinana sokola tonga dia manasitrana\\nRano bien sucrée\\nmandeha matetika eo ambony vatokely tsy manao kapa na kiraro na mandeha tongotra pieds nus matetika\\nMitsako tongolo oignon iray,\\nMisotro rano-mangahazo lena.Efa masaka io an.@ le izy marary iny no misotro. Mahandro mangahazo lena zany enao d le ranony no sotroina . 1 na 2 kaopy d ampy\\n"
            ],
            "famaranana": [
                "So d mbl misy zvtr tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "aretina2",
            "patterns": ["lamosina", "valahana"],
            "fampidirana": [
                "aaayy : ",
                "aay vee, ",
                "otranzao ny fanaovana azy : ",
                "ok, ",
                "ty ar : ",
            ],
            "responses": [
                "atao massagy io vao afaka, manaraka trajet de nerf traitement\\nfanafody ve? manala fanaintanana fotsiny iny. kinésithérapie et rééducation fonctionnelle no mety. tsy massage fa kinésithérapie.Zaraiko aminao, fa mila ezaka aloa, na @ fotoana na \\nfitandremana :\\n Raha somary vaventy de mampihena tena, tsy mifady hanina akory fa mihinana sakafo arapahasalamana fa kely\\n Milomano ny mety indrindra, manao crowl (70¨%) – dos (30%). Raha sendra mandalo any Antsirabe de ao @ ranomafana, raha mahavita adiny 2 fotsiny ao ianao de ho hitanao fa \\nhihena be ny fanantainana\\n Asio barre fixe ao aminao, de mihantona @ tanana eo ianao araka izay vita isan’andro,\\nsomary atao mihodina mora2 havia sy havanana ny vantana, mampisaraka ireo tolondamosina manery ny nerfs io\\n Fadio ny miondrika raha maka zavatra, ny lohaloka no haforitra dia ny vantana ambony hajanona mahitsy\\n Aza mibata zavatra mavesatra intsony\\n Tandremo ny otra fa tsy voatery ho mety akory\\n"
            ],
            "famaranana": [
                "So d mbl misy zvtr tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "aretina3",
            "patterns": ["asthme", "sempotra"],
            "fampidirana": [
                "aaayy : ",
                "aay vee, ",
                "otranzao ny fanaovana azy : ",
                "ok, ",
                "ty ar : ",
            ],
            "responses": [
                "Ento miotra mba isokatra ny tratrany.café tsy de mahery b. natation sy bicyclette ko mampisokatra ny tratrany. ampihinanano romboromailala matetika\\nny mpivarotra voromailala mahalala ny fampiasana azy bebe kokoa. mihinana bitro koa hono fa ny fandrahoana azy no tsy haiko hoe ahoana! \\nizy.rehefa mikohaka izy d lay sirop expectorant reny omena azy.ohatra oe farmad, pneumorel.... madetosyl ratsimamanga ko tsara. asaivo am-panaoviny natation na tennis\\nMenak avy nanendasana ovy, d omena iray sotro izy ! \\n Miompy sokatra ao antrano, omena kafé, asaina mifofona tantely, nahazo ny zanako, ary afaka tao anaty 02 herinandro \\nronono iray kaopy avy nampangotrahana asiana tongolo hasiny 3.alona 10 mn. tatavanina d sotroina isanandro. mandritry ny 3 volana7\\nHenan'ny kibobo koa mety be amimy.\\nravina raketa kikisana d afangaro @ tantely l zavatra madity b azo avy ao iny. Omena 1sotro maraina sy hariva d herinandro d ajanona herinandro d tohizana herinandro mandritra ny 3 volana toy zay hatrany fa na entinao eny @ tany b vovoka aza izy tsy ho sempotra intsony! manampy betsaka @ fisokafan'ny bronchite zaza io. RAKETA fa tsy vahona a \\nZanaka voromailala ilay mbola kely matavy2 tsara iny ilay mbola tsy mahay manidina no andrahoina hoatran'ny akoho. Omena azy hataony laoka miaraka am roniny. Atao matetika \\nra n'ny sokatra manta no tena tsara indrindra,Miara matory amin sokatra  \\nmenaka do koa tsara omena 1 sotro dité isan' andro \\nràm-bitro voalavo ,Rà ana bitro voalavo,manta le vao mafana, aingana be! Loarina @ antsy ny vômason'ilay bitro,Fa tandremo tsara ny volony tsy hisy tafiditra any ambavan'ilay za2 fa vao maika olana! Zay no anaovana azy eo@ mason'ilay biby!  \\n"
            ],
            "famaranana": [
                "So d mbl misy zvtr tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "aretina4",
            "patterns": ["bilariziozy"],
            "fampidirana": [
                "aaayy : ",
                "aay vee, ",
                "otranzao ny fanaovana azy : ",
                "ok, ",
                "ty ar : ",
            ],
            "responses": [
                "Voana papaye 150 isa totoina de alefa am rano 1litra laniana 1 andro. Ravitoto 1 sotro manta atao amin'ny rano 1 vera indray mandeha isanandro dia mifady sira amizay vetivety de sitrana \\ndia vovoka bois de rose 1sotro alona anaty rano dia sotroina .tsy atao betsaka tokony rano 1 litatra dia sotroina tsy laniana iray andro io akory\\nAndramo ny tantely sy tamotamo 1csc tamotamo dia 3csc tantely efa nisy havana dia efficasy fa ratsy tsiro 1csc par jour fa ahenao kely ny tamotamo sao mampandoha \\nRavina paraky lena, polipolesina @ tanana dia sotroina 1 sotrokely ny ranony. Olona fantatro no nisy nanoro an'io, efa nataony daholo ireo voalaza eo ambony, sitrana izy avy eo.\\n"
            ],
            "famaranana": [
                "So d mbl misy zvtr tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "aretina5",
            "patterns": ["fo", "gros coeur"],
            "fampidirana": [
                "aaayy : ",
                "aay vee, ",
                "otranzao ny fanaovana azy : ",
                "ok, ",
                "ty ar : ",
            ],
            "responses": [
                "akondro tetehana atao anaty rano faran izay mangatsika .de atao sakafo ampidirina ny vava voalohany\\nMihinana sosety, ravitsosety tanehana d atao rano fisotro fa zao tsy atao ela fa sao dia very rano be loatra \\nMisotro ranon'apango manitra , zany hoe dorana ny vary , dia ilay ranovola manitra be iny  \\nFa ref manao sosety de manaova ravina voaroy hazo @ izay tsy mi decal enao \\ntraitement jus de noni, nisy namako voa ohatran'io fa tsy areti-po , fa vavony dia nanao traitement dia sitrana \\n Mihinakinana ihany ireny vahona sy tantely ireny fa sao mety mahasoa \\nTy ndray tsy tambavy fa fomba hafa isamarina na tolakandro efa Ivaiva masoandro iny de aza mikapa na Mikiraro de mandehandehana manitsaka goudron, bonbon voanjo reny atao 30 mn au moins par jour na rehefa tsy mahavita an’izay de aza mikapa mihintsy rehefa ao antrano raha toa ka ciment na carreaux ny dallage\\n, mila maka rivotra kely mihintsy ianao an! dia averina aotra mihintsy fa raha tsy mety@zay vao mandeha manantona mpitsabo, mila fitoniantsaina ianao.\\nMankanesa any ambanivohitra raha mety, na dia sabotsy anankiray fotsiny aza! zay\\nfilaminantsaina mihirahira manao zavatra mafinaritra MIVAVAKA no tena zavadehibe tsy azo adino \\n"
            ],
            "famaranana": [
                "So d mbl misy zvtr tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "aretina6",
            "patterns": ["hemoraida", "hemorroide"],
            "fampidirana": [
                "aaayy : ",
                "aay vee, ",
                "otranzao ny fanaovana azy : ",
                "ok, ",
                "ty ar : ",
            ],
            "responses": [
                "Tantely hanosorana sy asisika any @ lavapivoahana,dia haleteho mihintsy @ izay sitrana. \\nHanitrinimpatsaka ampangotrahina dia hatao anaty tavy ohatra hatao bain de siège an ataovy mamay faran'izay zaka mandritry ny 3 Andro, tena mandaitra,\\nazo hanasana ilay mivonto mivoaka kely iny mihitsy \\nmaka tongolo be dia totoy apetaho eo amy lay izy fa hijanona ny fanaintainana.Raha afaka mividy ilay 'bauma guéritou' ianareo dia hosorana aminy fa tena haingana be, no sady manala ny fanaintainana\\nVoana mahabibo atao @poche gauche droit fa mijan hoa ,vazaha aza niaiky \\nAjanony daholo ny ‘excitant’rehetra aloha toy ny sakay, café, tabako,fa hisy fiovana, Misasa aminy rano mati2  \\nRaha ady gasy no lazaina dia ny volon-drano (eny an-tanimbary eny no misy azy, mitovitovy @ anandrano. Ampangotrahina\\natao anaty lamba avy eo, hipetrahana (Ny hafanana faran'izay zaka amin'iny no ilaina,\\nKikisana aminy vato tamotamo mahazo rano erany sotro asina Alamo kely de sotrona mahazahoa fahasalamana, sakay pilo \\nmisotroa ranona ravitoto manta eran ny sotro isa maraina vao mifoha \\nRavitoto sy oignon kisana.andrahoan d vao mangotra-tokana iny d ataovy anaty tavimandry dia mipetrak eo. Fa tena mandaitra io a sady mora\\nMaka permenganate de manaova ranomafana de lomy ao anaty koveta le permanganaty ho rava de aveo mipetraha elaela ao d ataovy anatiny 10 jours fa tena sitrana io ary tsy mverina tsony\\n"
            ],
            "famaranana": [
                "So d mbl misy zvtr tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "aretina7",
            "patterns": ["calcium", "fanomezana tanjaka", "kalisioma"],
            "fampidirana": [
                "aaayy : ",
                "aay vee, ",
                "otranzao ny fanaovana azy : ",
                "ok, ",
                "ity ary e : ",
            ],
            "responses": [
                "Voasary \\nRavombomanga si patsa, mihinana huîtres,ravina voarohy tenehina de sotroina\\nSoja koa mety o!ravina voaroy tenehina\\nRavina voroy hazo atao fisotro, manaova vary aminanana @ ana-patsa ihany koa \\nMihinana akondro iray isan'andro na .roa tsy maninona\\nMihinàna anandrano mandritra ny roa herinandro\\nMisotro ranovisy na visy gasy.mila maka aina.mihinana akondro.misotro jus d fruits natures\\nmihinana chocolat noire.Tsy ampy oksizena ianao no tena mahatônga an'izany\\nNy tsy fahampiana vy no mahatônga izany\\nMila mitandrina ihany ny fihinanana akondro be loatra, fa mety mampitohana !!!!\\nMihinana cafe sy atody afangaro rehefale miasa @alina iny fa calcium be io \\n\\n"
            ],
            "famaranana": [
                "So dia mbolal misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay ny azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "aretina8",
            "patterns": ["mampihena kibo", "kibo", "fanadiovana kibo"],
            "fampidirana": [
                "aaayy : ",
                "aay vee, ",
                "otranzao ny fanaovana azy : ",
                "ok, ",
                "ity ary : ",
            ],
            "responses": [
                "Fanafody ho an'ny kibo dia miankina amin'ny olana manokana\\n*Raha te ampihena kibo:\\nsport ihany fa tsy de misy miracle\\nmanaova fanatanjahatena, vao maraina dia manao 'course de vitesse' 100m * 2! \\n*Raha te hanadio kibo\\nKaosoud\\nAtao sur 12 Zany oe raviny 6 pr 1l d eau\\n Mila laniana indray andro. Mila misakafo b fa hikaka b enao so d malemilemy. Aza gaga raha tsemboka sy mangovitra n lohalika • aferotany \\nravina voaroitsaka no nataon'ny ntaolo fanadiovan-kibo, eo koa ny tapabatana ; ity farany tena ilana fitandremana • Ravina Quatre epingle \\n*Misy fanafody ady amin'ny fivalanana malaza ao Madagasikara, toy ny:\\nMenta: Manampy amin'ny fanalefahana ny tsinay sy ny fanaintainana\\nTsingy: Vokatra nentim-paharazana ho an'ny fivalanana.\\nSokatra: Amin'ny ankapobeny, manampy amin'ny fandehanana tsara.\\n*Raha manotika ny kibo\\nMitsako tsatsambaitra(zavamaniry io) dia atelina ny ranony\\nMitsako tanamasoandro (zavamaniry mangidy be)\\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tianao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "Tsara ny manatona mpitsabo na mpitsabo nentim-paharazana raha toa ka mitohy ny olana. Mety ho zava-dehibe ny fitsaboana ara-pahasalamana.",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "aretina10",
            "patterns": ["lanin'ny biby"],
            "fampidirana": [
                "aaayy : ",
                "aay vee, ",
                "otranzao ny fanaovana azy : ",
                "ok, ",
                "ity ary : ",
            ],
            "responses": [
                "any mpanao ody biby mandeha \\nAsiana oignon hono refa avy sasana tsara am savony nosy \\nMakà vovo misy alikaola apetaho @ le marary dia fonosy miaraka @ io dia rampitso vao alàna \\nilay mando2 avy ao am vagin iny hono mantsy odi biby tena mandaitra. eny na d kaikitrin maingoka aza\\nkoseo am laven rehefa mangidihidy tsy maninona koa osorana mihitsy \\nfanafody lanin'ny takolapanenjika:\\nTifiro amin'ireny insecticide ireny fa tonga de maina le biby ary tsy miverina eo intsony \\npipy \\nhosorana gros oignon \\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay ny azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "aretina9",
            "patterns": ["kohaka"],
            "fampidirana": [
                "aaayy : ",
                "aay vee, ",
                "otranzao ny fanaovana azy : ",
                "ok, ",
                "ty ar : ",
            ],
            "responses": [
                "Tantely,citron,sakamalao,tamenak atody1,beure 1sotro atsonika de afangaro daholo ireo de sotroy, de raha toa ka mitsonika ny lelo maka taoka kely d sasao ny lavak orona.\\nTongolo râpena dia afangaroy tantely mitovy fatra dia misotro iray sotro isaky ny adiny 4 eo tohizo foana mandrapahafaka  :\\nTongolo be @ izao hanina fa mampitony ny kohaka somary masiaka fa miaritra.\\nMievoka amin'ny ravim-boafotsy alohan'ny hatory no tena hitako nandaitra tamiko, ampiana an'ilay mahazatra tantely/citron/sakamalaho/tamenak'atody\\nMahereza misotro rano mafana ihany koa \\nHanitry ny Mpatsaka dia azo atao ody kohaka:atao dite asiana siramamy kely omena azy \\nnavet atao tetehana manify de rarahana siramamy eo amboniny de lasa misy ranony de iny no omena azy erakin'ny sotro fihinanana pendant 3 jours.\\nTantely sy vovona cannelle\\nMaka jaboran'omby fahefany kg + menaka sakafo 4 sotro lehibe fihinanana dia ampangotray \\nPecto na contra tout sy vinaigra.Atao anaty vera dia tapany ampy + contra tous 5 na mahery dia efa ampy \\nka rehefa mitsonika tsara dia asio huile essentiel katrafay goutte kely , avelao hangatsiaka , de hosory azy ny lamosiny sy ny tratrany , de mankanesa eo akaikiny Fpvm Rasalama fa manampy azy ny otra faladia  \\nomeo dibera nohepohina mafana 1sotrokely safovavany latsaka izy tsy dia feno dia hosory menaka mafana ny tratrany sy ny lamosiny aloha ny atory ary fonosy foana ny tendanymety daholo ireo torohevitra ireo fa mila orona isanandro koa aloa izy sao tery ny tratrany.ianao ihany dia mahavita azy \\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "aretina11",
            "patterns": ["loha"],
            "fampidirana": [
                "aaayy : ",
                "aay vee, ",
                "otranzao ny fanaovana azy : ",
                "ok, ",
                "ty ar : ",
            ],
            "responses": [
                "mitsako persila \\nMety misy *sinusite na rhinite * ngamba fa mankanesa ao Ampandrana Besarety akaiky ny FPVM fa misy mitsabo @alalan'ny otra Réflexologie ao, Sao d mba cysticercose koa e!\\nSakamalao mixena asina tantely atao masisika fa tsy mamy be 1 sotro 3 isan'andro eficace be io za 5ans narary loha natoron'olona anio tao @ Fb sitrana tsy marary handoa intsony aho \\nNa sakamalao sy sira kely tsakotsakona tonga de mijanona fa migrane no anaranizany aretina izany \\nRaha marary loha fadio ny milona rano mafana fa mahafaty ozatra.\\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "aretina12",
            "patterns": ["gripa", "grippe", "tazo mahery", "sery"],
            "fampidirana": [
                "aaayy : ",
                "aay vee, ",
                "otranzao ny fanaovana azy : ",
                "ok, ",
                "toy izao ary : ",
            ],
            "responses": [
                "*Akora ampiasaina: \\nRano mangotraka 1 L\\nTongolo mena lehibe 2\\nSakamalao 1 lehibe\\nTately fatra izay maha mamy azy tsara\\nVoasary makirana (citron) 2 lehibe\\nVoasary makirana (citron) 2 lehibe\\nFikarakarana azy :\\nKikisana ny tongolo sy sakamalao ary harotsaka avy hatrany ny rano 1L vao avy nampangotrahina dia andrasina kely dia potserina ny voasary makirana.\\nVita izay dia maka fatra 250ml/1 kaopy asina tantely izay maha mamy azy dia sotroina mahamay tsara.\\nSotroina mandritran’ny tontolo andro rampitso mamerina vaovao indray.\\nzaraina efatra ny oignon de tsakona ary avela ilona ao ambava manditra ny 1mn.De atao ohatrzay daholo\\nEvoka Ravitsara sy kininina fotsy\\noignon ihany: tetehina madinika de atao anaty vilia de apetraka ao atrano, manala virus.mirary soa!\\nny tongotsokina 1sotro desera a hatao infusion rano mangotraka 1tasy alona 1O mn \\nRavina papay mitovy habe am felatanana apangotrahana 8 mn sotroina ao anatin ny adiny 2 mandritra ny 3 andro de averina afaka telo andro raha mbola tsy tsara, apina ravina kininina fotsy sy vosary no tena tsara dia evohana, efa oe asina kinina fotsy dia asina siramamy\\nCitron io somary didina de ampangotrahana de atao evoka de avy eo sotroina fa tonga de misava io.maka rano mangotraka 1l d potserina ao ny voasary makiran roa lehibe dia mamina atao tsy dia mamy be dia evohana ny entona entiny sady sotroina atao mamay izay zaka \\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "aretina13",
            "patterns": ["sinusite", "sinizita"],
            "fampidirana": [
                "aaayy : ",
                "aay vee, ",
                "otranzao ny fanaovana azy : ",
                "ok, ",
                "toy izao ary : ",
            ],
            "responses": [
                "Dintina ramy, atao eo ambony sotrokely, Dia hafanaina eo ambony charbon mamay. Manao 'cornet ' taratasy dia trohana ny setroka manitra avoakany. \\nMampitomany mihitsy io nefa haingam-piasa ihany koa. Salamà e!Eny amin'ny mpivarotra fanafody malagasy\\nSAKAMALAO totoina de le ranony iny atao goutte 3 isaky ny lavak'orona,atao 2/jour 2-KINININA FOTSY ,maka raviny 3dia apangotrahina 10mn am rano 150ml dia sotroina in2/jour\\nna alaina ny raviny dia ampangotrahina dia atao evoka \\nTONGOLO OINION(antibacterie),totoina de apangotrahina 5mn,atao evoka aveo sotroina,afaka atao goutte ihany koa \\nVINAIGRE PAOMA,sotroina 1sotro kely atao 3/jour,na afaka afangaro am TANTELY ny vinaigre paoma 2 sotro dia sotroina 3/jour \\nVOALOBOKA(antibacterie)hoanina isanandro ra misy \\nRANO SY SIRA afangaro am rano matimaty dia trohana am orona dia ahisina avy eo hanadio ny ati-orona atao 2/jour \\nMAKA LAMBA MADIO ALONA ANATY RANO MAMAY DIA APETAKA EO AO FARITRY NY ORONA 15mn atao matetika\\nZAKARANDA,atao evoka na fohana am orona \\nRAVINA VOATABIA totoina de atao goutte ny ranony \\nNY RANO,tena ilaina ny fisotroana rano 1l 1/2/jour \\nNy sakafo misy VITAMINE A,ary ny fihinana tongolo gasy,poivre,sakay,tongolo be dia manasitrana ny sinusite ihany koa \\nRANOTSIRASY KARIBONETRA, rano 1kopy,sira 1/2sotrokely,karibonetra indray mitsongo,trohana de ahisina atao in3/jour \\nNy SOLILA(menthe) na THYM atao evoka mandritra ny 3jour,ary atao 2/jour 13-HYDROTHERAPIE PAR CONTRASTE(peta-gilasy moa zany ve? )alaina ny compresse mafana de apetaka eo am faritry ny orona 3mn,aveo njei alaina ny compresse mangatsiaka de apetaka 1mn,dia ampifandimbiasina izay de atao in3/jour \\nTONGOLO GASY(antiviral,antifungal)maka sigana tongolo gasy 3 apangotrahina am rano 1kopy,afaka asina tamotamo 1/2sotro ra misy dia sotroina isanandro,hoanina manta koa ny tongolo gasy tena tsara\\n*Rehefa tsentsina be iny ianao dia mba andramo kely ity torohevitra ity fa mety hanampy anao: \\n: makà hoditra akondro dia dory ilay izy, atao izay ahazoana lavenona, dia ranoina amin’ny rano kely, toy ireny manao ‘masque’ ireny.Iny no apetraka eo amin'ny 'points sinus'\\nTsy azo ajanona mihoatra ny 10 minitra ary tsy azo atao matetika ihany koa izy ity, satria mitroka ilay loto izy ka raha atao matetika na ajanona ela loatra dia ny atidohanao indray no mety ho trohany \\nRehefa tapitra ilay fepotoana dia diovina tsara amin'ny rano matimaty ny tarehy.\\nNy Romarin koa mahafaka tsara, iny tahony maina iny no dorana dia ilay setroka no trohina mafy amin’ny orona \\nRavina kininina fotsy evohana in-telo isan'andro mandritra ny 21 andro fa afaka Mifoaka romarin isan'andro\\nRanona voasary makirana sy tongolo lay tena mety fa fadiana ny mandena loha\\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay ny azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "aretina15",
            "patterns": ["tosidra", "tension"],
            "fampidirana": [
                "aaayy : ",
                "aay vee, ",
                "otranzao ny fanaovana azy : ",
                "ok, ",
                "salama tompoko,",
            ],
            "responses": [
                "* Mamana rano iray litatra sy sasany, atao mangotraka tsara.\\nDia arotsaka ao anatin’io rano mangotraka io ny ravin-tsaosety fito efa voasasa madio mialoha. Avela hangotraka kely mandritra ny fotoana fohy, ka rehefa miova mivolom-bolamena ilay rano misy azy, dia entanina avy eo ambony fatana ka esorina ireo ravin-tsaosety. Avela hangatsiaka. Sotroina araka izay itiavana azy mandritra ny iray andro. Ilaina ny mitandrina satria mampivalan-drano be tahaka ny mihinana ny fanafody simika fampiasa amin’ ny « tension » izy io. Tena mahasoa ireo izay voatery mihinam-panafody tsy miato izy ity, araka ny traikefa efa niainan’ ny namana samihafa. Raha sendra tsy mahita ravin-tsaosety aza dia mety ihany koa ny saosety vongany, tsy voasana fa avy dia arotsaka ao am-bilana amin’ilay rano mangotraka 1 litatra sy sasany,\\ndia ato toy izay efa voalaza etsy aloha ihany. Mazava araka izany fa tena tsara ny mihinana saosety atao laoka na salady. \\nAnkoatra an’io, mbola fanafody “tension” ihany koa ny 'ravina artichaut',\\nsatria mahatsara ny tosidra ary mampidina izany izy amin’ ny ankapobeny.\\n*Tsy izay ihany anefa fa ny tsy firindran’nyfirindran’ny fiasan’ny aty, ny olona marary aty (calculs biliaires), ny olana amin’ny vavony, ny olona mandrezatra lava tsy amin’ ny fotoanany, ny ngorongosy, ny sirôzy sy ny tsy fahalevonan- anina dia azo ampiasaina ity ravina artichaut ity ihany koa.\\nNy fomba fanaovana azy dia rano iray litatra no ampiasaina amin’ ny ravina “artichaut” folo :  \\nalaina ny rano iray litatra dia ampangotrahina tsara. Arotsaka ao ireo, dia avela ao mandritra ny 10 minitra, mba hahazoana ilay daozy ilaina. Alana avy eo ambony fatanana avy eo ary avela hangatsiaka ilay rano. \\nny fampiasana azy dia eran’ ny kaopy fisotroana kafe no sotroina, ka intelo isan’andro no ilaina\\nary raha azo atao dia sotroina mialoha ny sakafo. Mila mahavatra araka izany ireo manana tosidra miakatra fa hanampy azy izany\\nTsy atoro firy intsony angamba ny fampiasana ny tongolo lay na tongolo gasy.Anisan’ ireo tsy mampihetsika fa mampihenahena ny tosidra, ka raha miakatra izany dia mampidina ny tongolo gasy ary raha midina izany dia mampiakatra izy. \\nMisy ny manao azy ho 'suppositoire', izany hoe alaina ny49 hasiny iray dia voasana dia iny no atsofoka amin’ ny lavaka fivoahan’ ny maloto. Atao indray mandeha isanandro\\nMisy indray kosa ny efa mahazaka mihinana izany avy hatrany, ka hasiny fito no hanina kepohina dia arahina rano avyeo. Azoatao tsara ny mihina io koa mandritra ny sakafo\\nRehefa mahatsiaroho marariray hatoka na mihenjakenjan-katoka dia ny tongolo gasy no tokony hokepokepohina haingana.Rehefa hita fa mihena anefa ny tosidra dia ajanona izany fa tsy atao intsony.\\nAzo hanina manta ny tongolo gasy saingy mety hisy fofona kely ny vava rehefa avy mihinana azy dia azonao atao ny mihinana frezy mba hanalana ny fofona na koa aza zavatra hafa manimanitra kokoa sady mahafinaritra kokoa toy ny persil.\\nNy ravina kily koa dia tena maha-antoniny ny tosidra ; tsy misy refiny na fatrany ampiasaina fa eran’ny tanana anila dia efa ampy tsara, ampangotrahina dia sotroina ny ranony \\nNy ravina taindelon-tsinoa koa dia fampidinana tosidra : kosehina fotsiny dia orohina na fofonina mafy.\\nNy anamamy dia fampiakarana tosidra, koa tsy tsara ataon’izay efa manana tosidra ambony hatao laoka \\n-	Mazotoa koa mihinana akondro.Maha atonony ny tension ny fihinanana azy .\\n"
            ],
            "famaranana": [
                "Sao dia mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay ny azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "aretina16",
            "patterns": ["tosidra ambony", "tosidra miakatra", "miakatra tension"],
            "fampidirana": [
                "aaayy : ",
                "aay vee, ",
                "otranzao ny fanaovana azy : ",
                "ok, ",
                "ty ar : ",
            ],
            "responses": [
                "manangona ravina radriaka(taindelon-tsinoa) ravina maitso fito (7) sy akotry folo (10)ampandevezina amina rano iray litatra,\\nraha vao miketrika dia esorinahangatsiaka dia ataovy rano fisotro,indray andro .\\nNy anamamy dia fampiakarana tosidra, koa tsy tsara ataon’izay efa manana tosidra ambony hatao laoka \\nravina garanadrelina gasy 3 na 4, radriaka (zava-maniry madinidini-dravina, be tsilotsilo ny tahony, mamoa vony mavokely matsora rehefa volana ôktôbra, misy voany madinika kely miloko manga antitra) tahony kely 3 miaraka amin’ny raviny,\\nampangotrahina ao anaty rano 1 litatra, sotroina mangidy iray kaopy isanandro ka atao intelo isanandro\\nEntina miady amin'ny fiakaran'ny tosi-dra ihany koa ny anamadinika, koa dia mety ny manao azy ho laoka ho an'ireo misy tosi-dra \\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "aretina21",
            "patterns": ["vato", "calcul renal", "rein", "marary voa"],
            "fampidirana": [
                "aaayy : ",
                "aay vee, ",
                "otranzao ny fanaovana azy : ",
                "ok, ",
                "ity ary ny torohevitra omeko anao e : ",
            ],
            "responses": [
                "Phytocalcul homeopharma ny ahy no nataoko d afaka io no atao rano fisotro mety koa alo io ody vato masy io \\nefa nisotro le ody vato ny Ratsimamanga za fa nety ny ah az ef 7 mm d ra le fito calcul Homeo d mila ampina fitorein miarak aminy fa io otran ela2 fa Ratsimamang no rapide tena za ntena mtovy aminao mereza misotro tambavy sosety fa tsy maninona io\\nFakan-tsilo telo rirana no atao tambavy (Tsilo tahaka ny raketa izy ity, saingy miendrika telo rirana, ary mandady amin'izay zavatra eo akaikiny eo, toy ny rindrina, ny hazo\\nAlaina ny fakany, zany hoe ilay entiny mamikitra amin'ny zavatra andadizany iny\\nSahabo ho eran'ny tanana no ilaina amin'izany, dia sasana tsara ary arotsaka anaty rano mangotraka iray litatra ; dia avela hiketrika kelikely eo sahabo ho 3mn hatramin'ny 5 mn. \\nDia iny no isotroana matetika \\n Azo ampiarahana amin'ny loha-pary ihany koa io fakan-tsilo io, dia ireo no miara-tenehana. Fihinanana persil ihany koa mitsabo ny calcul, azonao hohanina manta, azonao totoina ranoina atao 'jus', na ampiarahana amin'ny salady sy ny sakafo isan-karazany. \\n*Fanamarihana : somary mahery ihany ity fakan-tsilo ity, ka ny hoe eran'ny tanana an'ila dia tahaka ny hoe fakany 5 na 6 isa eo ary manana halava 5 cm eo ho eo. \\n*Tsara ho fantatra ihany koa fa ny fihinana épinard dia tsy tokony atao be loatra (isan'andro) fa mahavoan'ny calcul\\nvolo katsaka sy tenina \\ncalcul rénal ve zany? Fakatsilo+vodina vôplera+valanirana tena rapide sd mvok manark ny pipi ny vato\\n Tanehana de sotroina 1kopy matin, midi soir.hazavao tsara oe ry andrianiniaina le vodina voplera mahalala voplera ve alo enao e? zavamaniry zay izy de ref angadiana d mis vodin, d iny le alaina Otran le vonikazo miliardera ren ny ravin fa ts msoratsoratr,\\nmis voniny zay ar ref voasan de mis voniny bori2 maint kel bdb ao anatin. Le valanirana met mis @mpivarotr tapakazo. \\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay ny azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "aretina22",
            "patterns": ["vava"],
            "fampidirana": [
                "aaayy : ",
                "aay vee, ",
                "otranzao ny fanaovana azy : ",
                "ok, ",
                "ity ary e : ",
            ],
            "responses": [
                "*Salama daholo! feno aphete ny vavako tsy afaka misokatra,tsy nihinana omaly sy androany fa marary be, inona no mety atao aminy fa tena mijaly be \\nlemo rano mangotraka ilay infusette dite sahambavy reny dia apetaho anaty vava e! ny ditimbahona ahosotra raha mahita sauge ny solila (menthe) hatao tisane de hatao gararaka anontsanana manampy e\\nsolutricine capsule tsetsafina dia ohatran'ny tsy teo.Na ravina vahimantsina tanehana hanontsanana vava in-3 isan'andro raha tambavy gasy no resahina!vakio mihitsy le mibontsina rà, dia ataovy afaka tsara le rà tao, dia sasao alikaola dia sitrana fa mety voakikin-javatra ny ati-vava ka tonga dia manangona rà ilay'membrane manify', dia ario le rà fa aza atelina \\n*Ny tokony atao raha te hanala fofom-bava:\\nMisotro rano mafana nasiana voasary makirana isa-maraina vao mifoha!andramo tapabolana fa tsy aheno fofm-bava zany intsony!ny voasary makirana sy rano mafana anisan'ny manasitrana ny aty sy izay rehetra tsy salama any anaty rehetra Tsy asina siramamy ka!rano mafana fa tsy mamay \\nmihinana 'persil'(Bain de bouche) dia alona kelikely ao ambava ilay fanafody vao arora aminizay e\\njerena aloha ny nify ra misy simba dia entina any am panao nify,ra mbola misy fofona ny vava dia mety ny vavony ko no misy tsy milamina dia lasa ny vava no mamoka fofona ,borosina tsara koa ny lela refa miborosy nify \\nmarary aty na nify simba na tsy miborosy nify aorian sakafo.. tsakoy persil manta. ontsano am rano misy alamo na karibonetra kely 1/jr , manao ‘bain de bouche #carbonate\\nMinana tantely iray sotrokely isa maraina koa fa manasitrana vavony\\nTsy ho simba nify izany na misy olitra akory raha mampiasa an'io ho hitanao fa hiafotsy toy ny coco ny nifinao \\nSolila na'menthe tsakoina fa ilay aretim-bavony aloha dia mazana no antony\\nmanala fofona chocolat, persil, tongolo ail, mamono mety ho fofona masiso avy ao anaty vava, ety ho vokatri'ny sakafo hohanina tsy zaka no mahatonga ny vavaony mamoaka fofona, mety ho nify ihany koa no mararay ka mila fitsaboana malaky. rehefa sitrana voatsabo tsara ny nify dia andramo ilay torohevitra natao tetsy aloha fa mahasoa anao io\\nMitsakotsako persil manta Mitsako persila manta na mihinana ''yaourt maison''matetika.Matetika koa vavony na ny aty vava no efa misy olana, fa tsara jerena ihany\\nborosiana am karbonetra sao de efa vavony kosa no ts normal eSo d ef ms nify simb e?ra mis mts d TS afk mts n fo2mbava ra TS oe esorina le nif sao dia mb misy g0ka n nify?ny dentiste iany no mahita hoe mbola tokon azo tapenana na tong d esorina. \\nPersil 200ar ampagotraho am rano 1l sotroy mpahariva ny andro ataovy matetika fa sady manadio vavony no manala fofona ny solila koa mety tsara \\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "aretina27",
            "patterns": ["ratra", "fery"],
            "fampidirana": [
                "aaayy : ",
                "aay vee, ",
                "otranzao ny fanaovana azy : ",
                "ok, ",
                "ity ary e : ",
            ],
            "responses": [
                "alamo sy diloilo ahosotra eo @lay fery\\nravina radrika na hoy ny sasany hoe ravina voamason'omby,sasana tsara ny raviny maro2 dia kosehina @ fela-tanana 2,ary in ranony maintso2 be iny n atao @ fery dia ho maina tsara n fery.andramo alhmaniry eny @sisindalana na zaridaina le radrika.mis fleur mavo n mavokely d mahery fofona iz..misy voniny iz io\\nAsio ravina voaloboka eo amle fery fa io mitroka nanaTAMOTAMO sy TANTELY manasitrana fery anaty .Afangaro ny tantely sy tamotamo vovony iray sotrokely avy dia hanina alohan ny sakafoalohan ny sakafo :maraina antoandro,hariva mandra-pahasitrany e!!ataoko fa tsy haharitra ela raha mahavatra \\nHafanao ny menaka dia ararak amin’ilay lavaka nidiran’ilay fantsika,dia mitaneha koa kadradraka de le ranony sotroina fa tsy manina io\\nTonga dia maka citron dia vakio roa dia dorana amin’ny afo dia avy eo itsahana,mafy be! \\nalamino ny sainao sy fonao retention d eau efa nahazo ahy dia mihinana fanafody , ampiakarina ampiana ondana ny tongotra rehefa matory amin ny alina\\nraha ratra kiaka kely tsy lasa lalina dia sasao tsara fotsiny dia avelao amin'izao fotsiny mba avela hiasa irery koa ny vatana \\nravina tsindahory sasana madio d tsakoina d apetak eo amin.ilay fery\\nHosory fetan'argile verte dia aza alàna eo intsony io fa lasa tako-pery @ farany \\nle malemilemy ao anaty vahona iny atao maraina sy hariva \\nSatrikoazamaratra no totoina dia ilay ranony azo avy eo no apetapetaka eo! \\nMakà ravina fotsy avadika dia totoy ary apetaho eo amin'ilay fery eo\\n*Fery anaty:\\nHo an'ilay fery anaty zao dia voakilalaka mety. Eny amin'ny <petite vitesse> misy azy. <antibiotique> matanjaka izy io\\nTrondro fibata atao lasopy de ranony sotroina . Za koa nodidiana natao oc fa io no natao latasy vetivety de tsy naninona tsony\\nRanona voatabia sy tantely\\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "aretina30",
            "patterns": ["maso"],
            "fampidirana": [
                "aaayy : ",
                "aay vee, ",
                "otranzao ny fanaovana azy : ",
                "ok, ",
                "ty ar : ",
            ],
            "responses": [
                "*Ny atao mba hanalana ditsoka amin'ny maso :\\nRaiso ny masonao roa dia sintony midina!Averimbereno io rano io\\nMaka serenge madio ary fenoy rano ka sokafy ny maso misy dintsika avieo aporitsiho ao anaty maso ny rano\\nManatona koa reny mampinono, ka tsirovy rononondreny ilay maso, fa io koa tena fanafody naturel sady vetivety.Ronono io ataovy fa za zao efa sitrany izany, mitadiava vehivavy mampinono \\n*ady gasy manafaka takodomena:\\nTongolo gasy \\nhosory tantely eo amin'ilay misy takodimena fa tena mandaitra\\ntotoina ilay tongolo gasy ary ahosotra @ faritra misy takodimena ny ranony \\nmividiana frakidex eny @ pharmacie fa tonga dia vaky io d afaka Maso\\nAmpandalovy(glaçon)vita t@ ravimboafotsy na ranona kokombra na faikana ovy manta nokikisana n tantely na (yaourt+jus de citron).15mn kobany. \\nAkipio ny maso 5mn eo ho eo! Avadibadio havia, havanana, Ambony ,ambany.Mamorona manôka ary akaro miakatra ny tanana ary mihinjitra toa iny koa ny vatana\\nKikiso ny karaoty ,ny ranony apetapetaka @tarehy.Ny faikany atao eo ambony maso mikipy.Manaova vongan-dranomandry(glaçon) vita t@ Ravitsara na Ravimboafotsy na ranona \\nkaokaombra .Ka apandehandehano eo ambony maso mikipy sy ny tarehy+tenda.Akipio 5 minitra ny maso ka ataovy mivadibadika havia-havanana, Ambony -Ambany. Mandritra izany miaina mafy be @ orona ary avôka@ vava\\nRehefa lanaky ny asa iny mihinjira ary mamorona ôka (manoaka,mihinàna akondro ,misotroa ranom-boasary \\n"
            ],
            "famaranana": [
                "So d mbl misy zvtr tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "aretina100",
            "patterns": ["vay", "kely be fototra"],
            "fampidirana": [
                "aaayy : ",
                "aay vee, ",
                "otranzao ny fanaovana azy : ",
                "ok, ",
                "ity ary e : ",
            ],
            "responses": [
                "* ady gasy fanalana haingana ny nana sy ny ankalany anaty vay:\\nKabaro na ofika kikiso @vato dia ilay potipotiny iny no ahosotra manodidina ilay vavan'ny vay tsy tapenana ny vavany \\naovy manta kikisana, ahosotra amile vay, tsy asina le vavany, avela ho maina, rehefa masaka le vay dia potserina hivoka ny nana sy ny ankalan’ny vay \\nRavi-mangahazo lena maromaro apetaka eo @ vay mihitsy, apetakao io ny alina manontolo afaka tanteraka io rehefa maraina ary maina tanteraka koa ilay ravi-mangahazo zany\\npapay manta alaina dia anosorana le otrany ronono iny, avy eo mandidy nofony manify apetaka eo ami vavan’ lay vay de tazonina ami bandy na sparadrap\\nraha vay efa masaka de misintona haingana le akalany io papay manta io\\nmaka vera, dia maka vovo 'coton' kely misy alikaola, dorana io dia atao anatin'ilay vera, rehefa maty ilay afo, tonga dia apetaka eo amin'ilay faritra misy ilay vay ilay vera, lasa ohatran'ny 'ventouse' tonga dia misintona ilay nana rehetra hivoaka io\\noxygenee haingana de haingana maka vovo asio io oxygenee io manao slip na kilaoty teritery de aleo ho eo fa ho hitanao fa tahaka ny tsy misy io vay io \\nmitoto tongolo gasy dia atao eo amin'ilay vay.avela alina tontolo.manamasaka anazy aingana io.na 'pensement alcoolisé' ihany koa mety\\nAspirine 2 indray mihnan alohan'ny hatory f maraina tsis marary tsony \\ntsy tia mivonto, ampiana mandrava sarotra sy avozo kikisana de ahosotra eo ambony ravinambiaty\\n"
            ],
            "famaranana": [
                "Sao dia mbola misy zaavtra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay ny azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "aretina33",
            "patterns": ["nify"],
            "fampidirana": [
                "aaayy : ",
                "aay vee, ",
                "otranzao ny fanaovana azy : ",
                "ok, ",
                "toy izao ary e : ",
            ],
            "responses": [
                "*Ny ady gasy atao amin'ny nify mivonto be:\\nontsany amin'ny ranotsira matetika dia osory tantely ilay mivonto, dia maka aina.\\natao massage eo amin ny afovoany ankibe sy ny fanondro amin zay mivonto.minan antibiotique \\nOntsany amin'ny ravina goavy ampangotrahina misy sira, ataovy mafanafana. Mihinana ihany'antibiotique'.\\n*madilo ny nify, tsy mahazaka kikiaka na vy mifampikasoka:\\nTsy ampy calcium izany fa mihinana calcium sao mba mety, ravina voaroy hazo hono tena mahahomby saingy tsy haiko ny fatrany kosa alohaNy antsika tambavy, matetika very sasaka no fanao, izany hoe , raha rano 1 l no narotsaka, avela hangotra ao ilay ravina dia 1/2 l sisa vao ajanona ny afo\\nfanafody nify:‘Clou de girofle’ tsakoina de atao ao anaty nify marary. Na kanela miampy tantely atao paty de atao ao anaty nify\\n*Asio karibonetra o! Mirary fahasitranana.mety tsy fahampiana' calcium sy magnésium' vokatry ny fampinona.Mividiana calcium MASY fa tena mety io.Mangalaha ravingoavy le mbola tanora de teneho kely de hanontsano vava \\nmihinana sakafo be kalsioma,manaova ilay yaourt+akondro+persil+atody akoho gasy, mixerna io dia hohanina mandritry ny 3 andro fa tonga dia afaka, ilay ravin-goavy\\nPersil+atody+yaourt +citron mixena de sotroina 3fois / jr pendant 3j de afaka tanteraka io!!Midecalc enao satria mifoha am alina mampinono am atoandro mbola mitaiza miampy ny raharaha mjinijinika ! Mazotoa misakafo ary ataovy sakafo be calcium !!Ts de tsara ny mihinana fanafody (comprimé) ohatra oe calci fort fa manjary mivadika calcul de ho sahirana eo ndray hanala azy \\nMaka ravina ambatry dia totoy dia ataovy @ ilay nify marary \\nRavina girofle maina na ilay mbola maintso iny tsakotsakoina dia apetao ao anaty ilay nify marary, fa eo no eo dia mijanona \\nAsio sira vongany,Hontsany @ ranotsira matimaty \\nvoatabia atao lasary dia asina siramamy fa zay nataoko dia nijanona \\nfotsy avadika totoina ikoseana azy \\n"
            ],
            "famaranana": [
                "Sao dia mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay ny azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "kabary2",
            "patterns": ["kabary fiharabana"],
            "fampidirana": [
                "aaayy : ",
                "aay vee, ",
                "otranzao ny fanaovana azy : ",
                "ok, ",
                "toy izao ary : ",
            ],
            "responses": [
                "-Tompokolahy sy tompokovavy, Razoky va re no manitra vonin-kazo sa razandry no manitra ravin-kazo no toa manimanitra asaramanitra izany trano?\\nTsy razoky akory no manitra vonin-kazo na razandry no manitra ravinkazo, fa isika rehetra no tonga maro ka manamanitra ny trano.\\nMijoro eto ny tenako misolo tena ireto mpiaramiasa mitondra ny teny fiarahabana. Mety ho gaga angamba ianareo hoe : ireto mpiara-miasa ireto angaha fary ka ny lohany indray no matsatso, na koa hoe vary ka ny madinika indray no lohany raha mitondra ny fitenenana eto ny tenako; tsia tompoko! Ao @ ireo mpiara-miasa ireo tokoa ireo\\nafaka hitondra ny fitenenana no sady malady no havanana @ izany, fa noho ny entana natao tsara fehy, noho ny teny tsy hifandrombahana, ary noho ny andraikitra nifampizarana dia ny tenako no mampitondraina izany fitenenana izany.\\nRaha mitondra ny fitenenana anefa ny tenako dia mahatsiaro tena toy ny vano eny ambalam-parihy, tazanina toa avo ihany, nony antonina nefa kely fingotra\\nAza ny ahakeliny re tompoko no jerena fa ny fonay manolotra azy, izay feno fitiavana sy fifaliana tokoa, toy ny maso-tsokina mason-tsinoa ka ny kely ananana no ahiratra. \\nAry farany tompoko manana ray aman-dreny tokoa izahay manana anareo, koa hoy ny fitenenana manao hoe : ny manan-jandry afak'olan'entana, ny mananjoky afak'olan-teny, ary ny manan-dray aman-dreny mihanta,\\nka dia mihanta aminareo izahay tompoko ka mangataka, aza hadinoina re ilay 'solompenakoho' izay efa mahazatra anay isan-taona e! Mino sy manantena izahay fa lehibe ianareo ka mahalala ny tokony hatao, \\nhandrandrana ka tsy hanafenana loha sola, hitsabo ka tsy hanafenana ny aretina, ary ray aman-dreny ka hitarainana ny manahirana. \\nHataka @ Andriana ihany anefa izany tompoka ka ny tanana mitsotra, ny vava misaotra, ny tongotra mitsaoka.\\nNy vary tokoa no misy fatrany, ny kibo misy fotrany, ny atao misy fetrany ; ary tonga eo @ fetra farany isika, koa misaotra tompokolahy ary mankasitraka tompokovavy.\\nEnga anie ity taona ity hitondra soa sy fanambinana ho antsika. Raha mitodika ny fampandrosoana ny orinasa izahay dia tsy takon'afenina ny fahaizanareo mitondra satria tsy mitsahatra mandroso ny orinasan-tsika, ka anisan'ny reharehanay mpiara-miasa ny fanananay ray aman-dreny mahay mitantana no malady sy havanana ihany koa @ fitondrana orinasa.\\nLava ihany izay teniko izay kanefa ny tady lava hono no misy mahazaka fa ny teny lava tsy misy mahazaka, ary raha lava ny ahitra very ny gisa fa raha lava ny resaka lainga no sisa, \\nka eto am-pamaranana dia hoy aho hoe ny vary tsy arahin-dranonorana hono manakofa ary ny fifampiarahabana tahaka izao no tsy arahina fanomezana dia zava-poana ihany, koa misy fanomezana kely izay nomen-tsika anarana hoe : 'solombodiakoho' avy aty @ireto mpiaramiasa,\\nkely ihany mety tsy ho mendrika ny voninahitrareo kanefa sahaza ny tana-manolotra, kely fa ataonay toy ny tantely tapa-bata ka ny vava miteny no mameno azy, kely temerim-pitiavana... Izay no ela tompokolahy sy tompokovavy,\\nela niniana nolalovana anefa satria saran'ny lalana sy voha vavahady ary ela zary elatra nitondra antsika nisidina aty @ tena resaka, koa noho izany, misaotra an'Andriananitra isika @ izao fotoana izao \\nsatria izy no mitantana antsika. Ary manana ray aman-dreny izahay eto, ray aman-dreninay @ alalan'ity orinasa ity, faly tokoa izahay ary misaotra an'Andriamanitra fa nahatsipaka iny taona lasa iny ianareo ary nahatratra ity taona vaovao ity, ianareo tokoa no vovonana iadian'ny lohany, varivariny \\nhandrian'ny tafony, ary felatana mangaika ny rantsana, miarahaba anareo izahay ka enga anie ianareo hikapa hahita ny tonony, handidy hahita ny vaniny, hitsara hahita ny meloka, ho ela fanapahana @ fitondrana ity orinasa ity, ka ho ambinina @izay nisasaranareo,\\ntsy ho voafitaky ny mpamahan-dalitra, ho ambinin-drary, ho ambinintsodrano, indrindra indrindra ho salama tsara ianareo sy ny ankohonanareo, satria ny fahasalamana no voalohan-karena.. \\nManaraka izany, ialako ny tsiny fa ny miteny tsy miala tsiny hono dia tahaka ilay banga nifiaka fary, ka ny natao hanamandimandina ny tenda indray no indrisy  nampitsovaka ny akanjonify. \\nIalako ny tsiny satria ny tsiny toy ny vato, kely manafitohina lehibe manakandalana, tsy zakan'ny teo aloha ka ombako tsy mahazaka ihany koa.\\n.\\nTeny ihany anefa izany ary resaka ihany ka resaka fa aza ny lohasaha mangina no jerena fa Andriamanitra antampon'ny loha. Ary manaova ny soa sy ny tsara dia hisaraka tsy misy maratra tahaka ny mpifankatia mifampitolona ianao sy ny tsiny Izany indrindra no hanaovako ny azafady raha miteny mialoha anareo satria\\ntazako manatrika eto ireo ray amandreny izay toy ny vovonana na ka mahatsinjo ny lavitra, toy ny varavarana ka mahita ny mivoaka sy ny miditra, ela nihetezana ka lava volo, ela nisotroan-dronono ka fotsy volom-bava; \\neo ihany koa ireo zoky izay tsy hialoava-mandeha, tsy azo atao rano dikain'ny zinga; eo ianareo mitovy saranga @ tena izay ankizy niara-nilalao\\ntanora nitovy soroka, ary mino  aho fa raha antitra dia mbola hiara-hitanin'andro; eto ireto zandry zanaka izay sakeli-mihoa-joro, saojo mihoatra akondro, vorom-panova hena ary ho avin'ny firenena; nataoko am-para filaza nefa ny faratampomboninahitra dia ianareo andriambavilanitra izay faka nitondra ny taho nivadika ho ravina ka zary felana ary tonga voa. \\nKoa ny miteny mialoha izany rehetra izany dia mahasaikatra tokoa ka hanaovana ny azafady satria izany no fangatahandalana raha hiteny no fanomezam-boninahitra anareo hitenenana.\\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "kabary3",
            "patterns": ["kabary fisaorana"],
            "fampidirana": [
                "aaayy : ",
                "aay vee, ",
                "otranzao ny fanaovana azy : ",
                "ok, ",
                "ity ary e : ",
            ],
            "responses": [
                "Tompkolahy sy tompokovavy, Sambatra raha samy zava-maniry hono ny maintsoririnina, fahavaratra mbola misalahy amin‟ny maro; fa sambatra raha samy faritra eto boeny fa sady manana toeram-papianarana manjaitra kanto dia kanto no mbola tsy menamitaha, no voalohany @fahaizana mampianatra raha @ io sehatra io no asiana-teny.\\nNy isa moa tompoko, fitarihana isa,ny tady fitariham-bato fa ny azafady kosa fitarihan-teny, koa manolotra azafadyTL, manolotra azafady TV, indrindra indrindra fa manoloana izato voninahitrareo ny maivana ato raha tahaka ny vato, silam-bato fanao tambi-toko, songosongo fanao sisin-tsaha. \\nNy lango no misy hono, teny ierana avy @vary, ny vero no afa-mijoro teny erana avy @ rivotra, ny jabo no azo tafiana teny ierana avy @ landy, fa izaho no afa-mandahatra kosa dia misolo tena ireto valala-be mandry manoloana anareo eto izao, ka izay no anaovako azafady.\\nEny TL sy TV, fa na nomena ahy aza ny handahatra sy hitondra ny teny fisaorana dia miala tsiny aho, fa tsy hitoe-poana toa volon-tratra fa hitoe- mahatsinjo toa volomaso ary hitoe-mitadidy toa volo-tsofina. Ny zozoro hono telo rirany, ny goaika fotsy tenda, ny lambo soso-nify, tsy olon‟ny ela aho fa mahatadidy ny fomba tsy maintsy hifanaovana mba tsy hisian‟ny fanomezantsiny.\\nTsy noho ny tsy fahaizako miteny anefa no mahatonga ahy hiala tsiny eto, fa noho ny voninahitrareo manoloana ahy. Iza moa ny tenako hiloa-bava anatrehanareo tompoko?\\nRaha ny tiko sy nahazatra ahy manko tompoko dia ny mahita anareo solon-tenam-pajakana, izay voasokajy ho isan‟ny RAD sy ianareo zoky tsy hialoava-mandeha mitondra fitenenana. \\nNefa ankehitriny toa miakadrova ity ny sotrokely mitondra teny eto masonareo, ka dia miala tsiny TL, miala fondro TV Nefa tompoko! tsy ho afaka ny tsiny raha tsy manao ny marina isika satria ny marina dia avy @ Atra, ary mendrika ny ho tolorana hasina manokana Izy @ izany fitiavana izany.\\nTsy ho adino ihany koa ny hasina ho antsika rehetra izay manatrika etoana; ka toy ny fiposak'Ingahibemasoandro izany, ka ny lehibe sy avo toerana no tokany aloha. Koa satria moa misolotena amin‟ny endrika roa samy hafa ny tenako, ary tsy noho ny fitiavantenako akory sanatria no ijoroako ho toy ny ireo mpiantra namako ireo fa nohon‟ny fahalalana fa fianarana ny zavatra rehetra ary ny “ecole coupe et couture volana mahajanga (ECCOVMA)” no nampahalala anay dia izay no itondranay teny fisaorana teny eto amboalohany.\\nTsy hilaza ho miara-mahita anefa ny tena, raha hanambara fa tontosa an-tsakany sy an-davany ny fianarana zaitra izay nimasoanay nandritrany fotoana maromaro izay ka hatramin‟izao fotoana izay hamoahana anay andiany faha XI izao, izay antom-pivorianatsika eto .Izao no tanteraka moa dia tsy inona fa ny fikirizana izay nataon‟ny Ramatoa VOLANA t@ fikelezany aina nanorina izao toeram-panofanana zaitra izao. \\nNy veliranon‟ny mpianakavy hono : izay mivadika aloha resehin‟ny fasana ; ny veliranon‟ ny mpiray tampoho:izay mivadika aloha ambadikain‟ ny nono niraisana ; ny veliranom-bazimba : izay mivadika kely ila, fa ny veliranon‟ ny tale jeneraly kosa dia «Tsy voatery mividy vao miankajo tsara» koa tanteraka ary tsapanay tokoa ankehitriny ny fahamarinan‟izany. \\nKoa hisaoranay ‘Miakanjo tsara andiany XI’ ianao Ramatoa tale fa mbola tsy nanankevitra ny hivadika tamin‟izany velirano nataonao izay ianao. Toloranay fisaorana sy fankatelemana tompoko ianao sy ny fianakavianao satria hinoanay fa nanampy anao tamin‟izato asa lehibe izato izy ireo, ary indrindra ihany koa fa ireo solontenanao mpiasa sy ny mpampianatra aty Mahajanga. \\nTena nahatsapa mihitsy izahay fa ianao sy izy ireo dia iray ihany „izy ireo sy izahay mpianatra dia iray koa, ary ny mpianatra, ny mpampianatra ary tale jeneraly dia iray ihany koa . \\nIzahay mpianatra andian‟ny XI dia manome toky anareo apahibemaso eto anatrehan‟ireto olona maro, solon-tenam-panjakana, sivily sy miaramila ireto fa tsy handrara-kilomby andoha, fa haneo hatrany ny fahaizana izay natolotrareo ho anay n‟ aiza n‟aiza .\\nFa hita tokoa ankehitriny: ny akaiky fatana mandroso afo, ny akaiky fanjaitra miakanjo tsara, ary ny akaiky «micro » omena fitenenana. Eto dia hitoetra amin‟ny toerana izay nosafidinanay izahay dia tsy aiza izany fa eto amin‟ny ECCOVMA, dia entina ny fisaorana anareo satria tsy ny ataka no zava-tsarobidy sy tena andrasana fa ny fisaorana, nefa izany raha atao ambany tsy hita ny endrika mahatsara azy. \\nKoa toloranay fisaorana mitafotafo ianao Rtoa Minisitry ny fampianarana arateknikasy ny fiofanana arak‟asa izay tonga manome voninahitra izao fotoan‟ny ECCOVMA eto anoloanay ‘Miakanjo tsara andiany XI’ izao. misolo-tena ny fanjakana fohibe moa tompoko ianao no eto, ary iangavianay mihintsy ianao mba hanao tsara laza any @ filoham-pirenena any hoe “Raha tehiankanjo tsara? Dia tongava hoe any mahajanga fa ao ny miankanjo tsara andiany XI miandry anao” Izany midika tompoko fa tsy honohono ny fahavononanay fa tena @ ankitiny hoy ny fiteninay azy izay.\\nAo koa ianao Atoa lehiben‟ny faritra boeny (na solon-tenany) mankasitraka re @ fanatrehanareo izao fotoana lehibe dia lehibe izao. Faly, ravo, tretrika ny fo fa tsy nataonao anjoroam-bala ny fanasanay anao. [raha solon-tena dia tohizana hoe : ka na dia tsy afaka aza ny tenany dia nandefa solon-tena ihany izy, ka ataovy tanteraka any ny hafatra izay mbola ho itanareo eo @ defilet izay ataonay manaraka avy eo]. \\nEto dia mitodika aminareo RAD ny tenako, zary fanaka tokoa ny hazo satria natao tsaravoatra, ary zary olona izahay fa nataonareo tsarakolo. Ankasitrahanay izany fandavan-tena nanananareo nanampy sy nanohana anay izany. Eny fa na dia @ izao andro efa madiva ho maizina izao ary mbola manotrona anay eto ianareo. \\nAo ianareo namana maro, ny mpanao gazety, ny mpandrindra izao lanonana izao dia mendrika ny hisaorana tanteraka satria tsy mbola mahatsiaro ny reraka ianareo ny @ fanampianareo anay ary tsy mbola tao an-tsainareo ny hanosibohotanana ny fangatahanay ny hiara-iasa aminareo. Sitraka sy telina tompoko ny vitanareo. \\nNy hamaranako ny teniko dia mitodika aminareo izay hanaraka ny dia izay nijoroanay ny tenako “tsy izay efa hay no tsara ho fantatra fa izay mbola tsy nisy no mendrika ho karohina” (dit ratax) Ho faranako ny teniko ka hoy aho manao hoe: 'raha tany an-trano isika tsirairay izao dia farahetsiketsika dia ny hidintrano,fa eto kosa ny fara-hetsiketsika dia ny fisaorana antsika tsy ankanavaka ary mirary soa sy fahafinaretana satria hitohy @ filatroana izao fotoana izao ka ireo vokatra izay avy t@ fanjaitra sy lamba nanananay no haranty anatin‟izany rehetra izany \\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "kabary4",
            "patterns": [
                "kabary ankaratsiana",
                "famangiana manjo",
                "kabarim-pahafatesana",
            ],
            "fampidirana": [
                "aaayy : ",
                "aay vee, ",
                "otranzao ny fanaovana azy : ",
                "ok, ",
                "ity ary : ",
            ],
            "responses": [
                "mpamangy : Akory avy izato ianareo, tompoko (miara-miteny an’io ny mpamangy)\\nVangiana : Indreto izahay eto ihany, tompoko (miara-miteny ihany koa ny vangiana)\\nMpamangy : Avy mamangy amin'ny fahoriana, tompoko (mbola miara-miteny ihany)\\nVangiana : Misaotra indrindra, tompoko, ary hotahian'Andriamanitra anie ianareo (mbola miaramiteny ihany koa ny vangiana )\\nMpamangy : (eto dia ilay solontenan'ny Mpamangy irery amin'izay no miteny)\\nAzafady indrindra, ry izy mianakavy, fa amin'izao fahoriana midona sy mihatra aminareo izao dia tonga eto izahay (lazaina eo izay fifandraisan'ny mpamangy amin'ny vangiana, ohatra mpiara-miasa na mpinamana...) izay tsy hafa fa mpiara-miasa, iray vatsy, iray aina, iray trano, iray donak'afo, iray petsapetsa amin'Itompokolahy na Itompokovavy.\\nTsy tonga hamendrofendro na hanetsika alahelo anefa na hanampy trotraka ny ratram-po izay efa mianjady aminareo, fa tonga hanao tongotra miara-mamindra, soroka miara-milanja ary hanao maso sy orona ka iray alahelo aminareo.\\nNy varavarana nivoahana mantsy, tompoko, no anareo, fa ny fahoriana sy ny alahelo dia iarahantsika mianakavy mizaka.\\nAry tsy maintsy misy moa ny mpampangy sy vangiana dia izany no antony itsangananay eto, satria tsy maintsy mifankahery isika fa raha tsy izany dia mipetraka ho vangiana koa izahay, amin'ny maha iray antsika\\nVitsivitsy ihany izahay no indreto tonga midodododo manoloana anareo,noho ny adidy amanandraikitra samihafa sy ny tokatrano samy manana,dia solon-tena havana sy tapaka ary fianakaviana iray ihany isika no mifamangy sy mitondra ny teny fampiononana\\nAtao ahoana moa, tompoko, fa tsy maintsy mionona isika fa izay nositrapon'Andriamanitra. Izy no nanome ary Izy koa no naka, ka isaorana eto ny anarany. Ary fantatsika tsara koa fa fandalovana ihany ny eto an-tany, ary vahiny sy mpivahiny isika, ka rehefa tonga ny fotoana tsy maintsy handehanana dia mbola handalo amin'izany ihany isika. \\nTombon-dalana ny azy fa isika rehetra mbola ho any avokoa\\nNoho izany dia mionona ary mahaiza mionona, tompoko, fa izy tsy hiverina intsony ary isika mbola ho any. Mahaiza mionona ary mahereza , tompoko.\\nVangiana : Misaotra anareo (lazaina eo ilay mpamangy raha tadidy), tompoko, izahay amin'izao fahatongavanareo izao sy fijoroanareo mampionona anay izao. \\nMafy sy mavesatra tokoa ny fahoriana noho ny fisarahana, satria andry lehiben'ny fianakaviana tokoa no lasa. Kanefa noho izao ataonareo izao, tsy namela anay hitomany irery, fa avy midodododo, maneho ny fiaraha-miory sy miara-mizaka ny mafy aminay.\\nTsy misy mampionona aza, tompoko, mionona, mainka fa misy anareo marobe tsy manadino, mampahery anay toy izao! Ka dia misaotra, tompoko, ary enga anie mba ho fifaliana indray no hihaonantsika fa tsy fahoriana intsony.\\nMpamangy : Aza misosoka alahelo intsony, tompoko.  \\nEny, tompoko, araka ny fomban-drazantsika moa izay mbola tohizintsika mandraka ankehitriny, dia indreto izahay tsy tonga hampifendrofendro fa kosa mitondra ny varavaintikely voatsirambin'ny tanana izahay ho fao-dranomaso (na solon-dranom-bary tsy masaka nasolon-drambon-damba) ho an'ny maty, mba ho mariky ny firaisantsika sy ny fifankatiavantsika (raha hanatitra lamba na voninkazo, dia omena amin'io koa).\\n(Manolotra vola anaty valopy misy ny anaran’ireo fianakaviana rehetra tonga mamangy. Io tolotra io dia omen’izay olona efa voatondro hatramin’ny voalohany an’izay olona iray vangiana mipetraka eo anoloana eo).\\nDia ho tsara levenana anie ny maty ary ho henikaja amam-boninahitra koa anie ny velona ! Ho lasan’izay ny ratsy sy ny loza mahazo antsika izao fa dia mba ho tsara sy ny soa ary ny mahafinaritra amin’izay no aoka hifanodiavantsika mianakavy ! \\nVangiana : Mbola mamerina ny fisaorana sy fahatelemana anareo ihany izahay, tompoko, amin'izao ataonareo izao. Tsy vitan'ny fahatongavanareo fotsiny sy fitondranareo ny teny mamy, fa mbola nampiarahanareo vola aman-karena indray. Mionera be ny lany. \\nKa tsy ny maty akory no mahafaly fa izao ataonareo izao no tena mahavelom-pisaorana. Misaotra tompoko.\\nMpamangy : Raha amin'ny tokony ho izy dia tokony hiara-mipetrapetraka eto isika, nefa noho ny adidy tsy azo ialana sy zarazarain'ny tokantrano samy manana ny azy, dia mangata-dalana aminareo izahay, ka hilaozanay hitsaitsaika aloha ianareo.\\n(raha handeha ny mpamangy no miteny izany, fa raha mbola hijanona izy dia toy izao ny tenenina ) Izahay moa, ry izy mianakavy, mbola hiara-kipetrapetraka aminareo eto ihany ka mbola tsy hifanao veloma aloha isika fa dia mahaiza mionona daholo. \\nVangiana : Eny, tompoko, tsy misy tsiny mihitsy raha handeha ianareo, satria mipetraka eto ianareo hanao adidy, handeha any ianareo mbola hanao adidy, ary izahay moa mbola eto ihany, ka dia omendalana ianareo ary mbola memerina ny fisaorana farany, tompoko. \\nMpamangy : Aza misosoka alahelo intsony tompoko\\nVangiana : Misaotra tompoko \\nFanamarihana  : Mandray tanana ny vangiana ny mpamangy vao mitsaitsaika mivoaka na mipetraka. Raha betsaka loatra anefa ny olona vangiana dia ny eny aloha ihany matetika no raisina tanananSantionana famangiana manjo ihany io fa miankina amin'izay tiana hotenenina sy ny fomban-tany ny famangiana manjo\\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "kabary5",
            "patterns": ["fandrika kabary am-panambadiana", "fandrika kabary"],
            "fampidirana": [
                "aaayy : ",
                "aay vee, ",
                "otranzao ny fanaovana azy : ",
                "ok, ",
                "toy izao ary e : ",
            ],
            "responses": [
                "Dingana:Eny amin’ny vavahady:\\n*Mpamoaka:Voahira-manaitra ny eny Itasy, volom-bato manondoka ny eny Antongona izay mitsoboka ao rendrika ary izay misangy any lavo. F’izato ianareo hoy aho narebirebin’ny mpivoy sa hendratren-dratsy ny mpandalo no nanadino ny teny nifanomezana ka tsy nahatsiaro ny fotoam-boatendry. \\n+Mpangataka:Eny topoko, ny rahona hono nengain'ny rivotra, ny vorona nengain'ny elany fa izahay kosa nengain'ny fitiavana. Ka ny manambara tsy mandodona, ny mampatsiahy tsy manery fa anio toko ilay fotoana efa nifanarahana, ny omby indray mandry nefa topoko tsy indray mifoha, ka mbola misy fifampiandrasana kely ary eo ihany ko ny fitohanan'ny fiara ka dia ialana tsiny ndrindra topoko ny fahatarana kely. \\nFanombohana :\\n*Mpamoaka:Aloha ny hirosoantsika amin’ny dinika tompoko dia milazà hoe inareo anarankena anan-kiroa? \\n+Mpangataka:Henomby sy henkisoa vorivory kena sy tongotr'omby \\nEny amin’ny vavahady: \\n*Mpamoaka:Zovy ianareo tompoko havana sa fahavalo?\\n+Mpangataka:Sady tsy havana izahay tompoko no tsy fahavalo fa tany ama-monina tonga hiandra vovonana aty aminareo. Fa raha havana mantsy dia hoy ianareo hoe: izahay tsy manam-bady havana ary raha hamaly izahay hoe: fahavalo, dia hamaly ianareo hoe: izahay tsy mampiditra fahavalo antanàna. Koa noho izany tompoko tsy havanareo izahay no tsy fahavalo ihany koa fa mba te ho isan’ireo fianakaviana. \\nManotany havoriana: \\n*Mpamoaka:Efa vory izahay tompoko fa ny bozaka aman’ahitra sisa no misavoritaka \\n+Mpangataka:Alamino ary aloha tompoko fa izahay zanakin'ny fanatenana ka vonona hiandry ahatramin'ny farany \\nEny amin’ny vavahady: \\n*Mpamoaka:eny ary tompoko, avy azia tokoa moa ianareo, ary ho aiza, ary inona no nitondra anareo \\n+Mpangataka:avy any amin'ny vohitry ny fiavananana izahay tompoko, no tonga eto amin'ny vohitry ny fitiavana ary ny fitiavana no nanosika , nitondra anay aty tompoko \\nEny amin’ny vavahady: \\n*Mpamoaka:Tsiriry vorona sa tsiriry ahitra ianareo tompoko no tonga eto aminay? \\n+Mpangataka:Raha nisafidy ny tsiriry ahitra: (…) Ny tsiriry vorona tokoa mantsy manifi-drano izy dia lasa indrindra fa rehefa ritra ny rano dia mikopak’elatra izy dia mifindra farihy. Ny tsiriry ahitra kosa raha tondraka ny rano dia milemodemoka ery izy, raha ritra ny rano havadika ny bainga dia eo ihany izy dia mba tahaka izany ihany izahay tompoko. Raha nisafidy ny tsiriry vorona: (…) Tsiriry vorona izahay tompoko satria tsy hiara-mitoetra aminareo akory Andriamatoa fa rehefa avy mangataka dia mandeha mamorina tokontrano fa tsy ho vesatry ny rafozana. \\nEny ivelany Fahatongavana: \\n*Mpamoaka:Ny olona tonga maraina moa tompoko hitaky trosa, ny olona tonga hatoandro hinankanina, ny olona tonga hariva hatory fa ianareo kosa ity tompoko tonga antenantenam-potoana tsy fantatra hoe: hanao inona? \\n+Mpangataka:Izahay moa tompoko tsy tonga amin’ilay hiran’i Samoela hoe: taratara amin’i Zoly. Fa matoa izahay no tara dia tao dia tao ny antony, dia tsy inona akory fa noho ny zanakareo ihany no mahatonga an’izany ary raha tsy tara tamin’ny zanakareo Andriamatoa dia tsy tonga teto izahay. \\nFanteram-bodiondry:tapimaso\\n*Mpamoaka:ny omby indray mandry raha vonokiorimpaka ianareo mba asehoy aloha ny soron-daingo,ny mifady hanina mifonofono no nahatratra antintra ny amalom-be; ka inona no hevitranareo makasika an'ity  \\n+Mpangataka:Eny topoko. Ny lehilahy hivonona ny ho rangahy dia tsy manintsy manaja ny anadahy. Ka ity re topono ny Tapi-maso satria resaka fady tokoa ity \\nMarina tokoa tompoko izany. Nefa amin'ny maha olombelona dia misy ilay fomba fiteny manao hoe ' Ny manta ao ambolany mila mpahandro, ny masaka an-dovia mila mpihinana. Ka raha izay no itondranareo ny resaka dia hoy izahay manao hoe : Esory ary ny fonosana dia zarao iaraha-mihinana \\ntokimpitiavana:\\n*Mpamoaka:tsy azom-bika tsy azon-tarehy fa ny fanahy fito no mahasarika azy, raha fitiavana tompoko no resahinareo dia azonay antoka fa ny manan-tsira mahay mahandro, ny manam-bola moa mahay miantsena fa ny manam-pitiavana kosa mahay mangata-bady, raha ny adidy indray no hoventesinareo dia tsy ho diso fanantenana izahay fa ny vy tinefy no vonona hisedra ny\\nmahamay,\\nary ny lehilahy mangatabady vonona hanefa ny loloha rehetra, noho izany re tompoko omeo valinteny faha-telo izahay fa iny no tsy fantatry ny fianakaviana.\\nMisaotra tompoko ENY Tompko raha izany no valinteninareo Ambarao ny marina tsy miolaka izahay mba hanandratana ny hasim-pitiavana Eny tompoko tsy  zaza mosarena fitia izaha ka vao tohinina de hiroboka, fa kely mahalala ny antony ka ny tsy mahandry no aoka hamoy azy.\\nvalamben'ny fahalala ary kianjaben'ny fahaizana tompoko ny fanambadiana ve am taolana namajikana ny ts=roka sa ladimboatavbo afa-paka faran'izay tsotra aty aminay nefa faratn'izaytrstra any aminareon fa ny fanambadia ve tompoko Ary roborobon'ny marofihir=tra ve sa vadibarotr'ilay manoa (tononiko ho vady vao zary ranitra), ka handny zara ny eo an-tanana fotsiny \\n+Mpangataka:vohirana ravo marivo morona ka fitan-tokana ihany Ny fitiavana no atao iampitana fa raha zahatra mandrendrika \\nfamoahana zazavavy:fangatahana vodiondry: \\n*Mpamoaka:fa raha izay ary ny sora-bilia endriky trano mba manao kosa ilay tsihy endriky ny vatra, satria mantsy ianareo kristianina, izahy koa mba mivavaka ihany, ambarao sy tantarao aminay izany didy fahaefatra izany fa liana dia liana ny fianakaviana, misaotra tompoko Hanara-doahasa, sa hianika tendrombohitra mari-dalana : lalana fito, sapanana fito, ka mariho izay alehanareo hasin'ny  tanàna ny : ny hasina re fandaingo aty aminay, ka hampisoka ny rano tambiazina, ve ianreo sa handaingo ny hatao loaka \\ndom-baravarana, \\ndikan-tokonana, \\nhasin'ny tolana \\nhasin'ny lapa \\ntapimaso \\nhoa 'ny dadato avy amin'ny dada\\nnenito avy dada \\ndadato avy am neny \\nnenito avy neny \\nmanomboka etony fangatahana hanonona anarana \\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "kabary6",
            "patterns": ["kabary fanokafana lanonana", "kabary fanentanana"],
            "fampidirana": [
                "aaayy : ",
                "aay vee, ",
                "otranzao ny fanaovana azy : ",
                "ok, ",
                "ity ary e : ",
            ],
            "responses": [
                "Tompokolahy sy tompokovavy, Ny horakorakin'ny sahona hono fambara andro mazava , Ny siotsiokan-tsarovazo fambara andro maraina, ary ny fijoroako eto kosa manambara fandraisam-pitenenana. \\nMety hilaza angamba ianareo hoe, nakaiza Ny hazo mafy no ambiaty no atao fehitrano,farihibe maty mamba ve Ny (fikambana) no zaza madinika no asaina mitondra teny ?  \\nTsy ferana tompoko ny saina aman'eritreritrareo fa ny miteny hono toy vato ka izay maivana no atoraka, toy ny antsy ka izay maranitra no adidy. \\nTsy ny raozy marevaka anjaridaina anefa aho fa ny amberivatry fanao sisimboly ihany, fa noho ny teny natao lany era sy entana natao tsara fehy dia nomeny ahy ny fitenenana, ka dia entiko ampitiavana sy am-panetren-tena izany.  \\n Na nomena ahy aza ny andahatra, dia tsy hanao kabarin-jatovo aho ka avy hatrany dia vetesina,  na sodoka atao mandroso ka hiantsampy eny am-pitoeran'entana, fa Ny fanombohany isa dia ny akiakely, ny fanombohany asa dia vavany ARY Ny fanombohany teny kosa dia ny azafady. \\n Fa ny azafady hono sady fangatahan-dalana hiteny no fanomezam-boninahitra anareo hitenenana. \\n Na dia eo aza izany, tsy entanim-pitia toa lalitra izahay ny hanolotra seho ho anareo, Ka itsambaka alohan' ny sotro; Fa ny lali-manga tia tsabatsabaka hono no maty \\n manafitohina, fa ny ro nisosany tsy azo diasina, ny fatiny anefa tsy mba fandefina akory. \\nKoa raha izany no izy dia aleo mijanona fa ho zava-poana ity fitorina ataonay eto ity. \\nAnaovako azafady ihany koa fa tsy mbola irony fiaramanidina mahatety izao tontolo izao irony ny fampisehoana hoentinay fa mbola posiposy kely madinika ihany ka tsy afaka ny hiampita ranomasina akory raha tsy eo ianareo manontrona izao lanonana izao. \\n Ka raha tsy fary antitra azo fiahina izany dia mba hevero ho toy ny voly antitra azo itsefana mamy, ka izay mety ho tsirony atelomy ary izay mety ho sanatria faikany alohavy re Tompoko. \\n Fa tsy izay miazakazaka manko no tonga aloha fa izay mijery ny marim-pototra ary izay tonga soa no arabaina. \\n Ka aleo ny fitenenana arafitra sahala amin'ny biriky ee, miakatra tsirairay. \\n Dia miala tsiny aminareo koa aho fa tsy hanala nify mbola tanora amin'ity fitenenana ara-pomnandrazana ity, satria raha mitsangana tsy zoto, moa raha mipetraka tsy laina; fa raha ny tianay mantsy dia naleo tsy niteny fa avy hatrany dia natao ady voay aman'mandan'ny Kirijavola ka avy hatrany dia ny voamason'ny no nokendrena, Nefa raha izany toa manan-jara ny moana. Tsy maniry ny ho moana anefa izahay, fa hitory sy hampihely aminareo eto ny fahatsarana avy amin'ilay Andriamanitra. \\nAnkehitriny dia tsaroina fa ny Trano vohatr'olombelona, ny olombelona vohatr'Andriamanitra. Izy no antok'izao fotoana lalovantsika eto izao ka tokony  homena voninahitra. \\n Ny sahobakaka mifamangy, hono, ny mpamangy mototra; ny vangina mototra ny rahona mifamangy isaky mihaona dia mitomany fa isika mitafa eto kosa, dia toy ny fodilahy mamangy railovy ny vangiana misiotsioka, ny  mpamangy mihirahira... Koa raha hiantsinanana ianareo, higoka fiadanana raha miankandrefana, ho lavitry ny fahafatesana raha mizotra mianavaratra, ny fahasoavana anie hiraraka ary raha hianatsimo, Andriamanitra tsy hanadino.... \\n Arahabaiko toy ny olo-malaza ianareo ka hivoaka ho maro mpitazana, hamindra ho maro mpanontrona, mivolana maro mpihaino.\\nArahabaiko toa olo-mahery e, ka raha miady ho maro mpihoby, mandresy ho maro mpitehaka, miasa ho maro mpandrisika. \\n Izay no ela ry izy mianakavy; ela tsy azo nodikaina fa antitra mpanome tsodrano. \\n Ndeha ary isika hiroso amin'ny sarin-tsary kely ho an'ity fampisehoana eto ity anio. \\n(...FANDAMINANA, NY FIZOTRAN'NY LANONANA, NY LAMINA MARO SAMIHAFA...)  \\n Misaotra Tompokolahy mankasitraka Tompokovavy. \\n 'Misy ampahany kabary izay nindramina tamin'ny namana'\\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "kabary7",
            "patterns": ["fisehoana", "vodiondry", "fisehona"],
            "fampidirana": [
                "aaayy : ",
                "aay vee, ",
                "otranzao ny fanaovana azy : ",
                "ok, ",
                "ity ary e : ",
            ],
            "responses": [
                "\\ny dingana voalohany tsy maintsy atao rehefa nifanapatapak’ahitra ny olona lahy sy vavy fa tena hiroso amin’ny fanambadiana, dia « ny fisehoana sy ny fiantranoana »\\nFISEHOANA:\\nAorian’ny fanapahan-kevitra ataon’ny zazalahy sy zatovovavy, rehefa nifampizaha toetra nandritra ny fotoana maharitraritra ihany dia mifanaiky izy roaroa fa haseho eo anatrehan’ireo Ray aman-dRain’ilay zatovovavy ilay zatovolahy miakasa haka azy ho vady. Izany dia atao aorian’ny dinika sava ranon’ando ataon’ilay zatovovavy amin’ireo Ray aman-dReniny niteraka azy na koa nitaiza azy (raha toa ka kamboty izy). Io no antsoina hoe : Fisehoana. \\nAnjaran’ilay zatovolahy koa indray no mitatitra izay “Fisehoana” izay eo amin’ireo Ray aman-dReny niteraka azy na ireo nitaiza azy (raha toa ka kamboty izy). Rehefa mifanaiky izy ireo dia mangataka fihaonana amin’ireo Ray aman-dRain’ilay zatovovavy ny Ray aman-dRenin’ilay zatovolahy. Izay fihaonan’ny Ray aman-dreny roa tonta handinika sy handrindra ny fotoana hanaovana ny fangataham-panambadiana, satria efa mifankatia ny ankizy. \\nNy Fangatahana dia fotoana iray ihaonan’ireo solon-tena mahefa avy amin’ny fianakaviana Roa Tonta hanatanterahana ny fangatahana ny tovovavy mba ho tokatranon’ilay tovolahy sy fanaterana ny hajam-bolana malagasy na ny “Vodiondry”  \\nRehefa mamangy ny fianakavian-drazazavavy ny an-drazazalahy fa hangatabady. Amin’io fotoana io no anolorana 'ny ala-fady' isan-karazany, kanefa izany dia ialohavan’ny kabary am-panambadiana hatrany : Tsy ampandrosoana avy hatrany ireo mpangataka fa avela hanana faharetana. Izany dia endrika ahitana fa vonona hiaritra ny mafy tokoa ny fianakaviana indrindra Ra-zazalahy. Manao. Rehefa ampandrosoana izy vao miditra ny varavarana : Izany no atao hoe Miandra vovonana na Fiantranoana\\nRehefa tafiditra ao antokantranon-drazazavavy ny vahiny dia toy izao no fizotry ny kabary am-panambadiana :\\nMpangataka : Manontany havoriana – vaky lela – dom-baravarana – ala fady.  \\nMpamoaka: Valin’ny havoriana.\\nMpangataka: – Azafady + ala sarona .- Fialan-tsiny.- Hasina sy arahaba ary firarian-tsoa.- Ranja kabary.  \\nMpamoaka: Azafady + ala sarona. Fialan-tsiny. Hasina sy arahaba ary firarian-tsoa. Ranja kabary ,Fisaorana vaky lela, dom-baravarana, ala fady- Tokim-pitiavana\\nMpangataka: Valin’ny tokim-pitiavana. \\nMpamoaka: Fisaorana noho ny tokim-pitiavana.\\nMpangataka: Fanomezam-bodiondry.\\nMpamoaka: Mandray vodiondry ary maneho fisaorana. \\nMpangataka: Mangataka ny hampandrosoana an-drazatovovavy.\\nMpamoaka: Mampiditra an-drazatovovavy + filazana azy ny dinika vita sy fananarana.\\nMpangataka: Fanolorana peratra rehefa avy nokarohina ka hita. \\nMpangataka: Fanolorana peratra rehefa avy nokarohina ka hita. \\nMpangataka: Fanolorana peratra rehefa avy nokarohina ka hita. \\nMpamoaka: – Fanasana ho amin’ny sakafo raha misy. \\nMofomamy: tapahin-drazatovolahy ny mofo ho an’drazatovovavy (fanapahana ny fitiavana / didian-drazatovovavy koa ny fitiavany ho andrazatovolahy manontolo). \\nMpamoaka: Fisaorana.  \\nMpangataka: Fisaorana. \\nFOMBA FANAO HISOROHANA NY TSINY SY NY TODY:\\nny tampimason’anadahy :izay tsy inona fa fomba fangatahan-dalana amin’ny anadahy fa hiresaka zavapady eo imasony dia ny fanambadiana izany.   \\nny vodiondry : \\nio kosa dia atolotra ny renin-drazazavavy. Ny fahatontosana an’io no manamarika ny fifatoran’ny fanambadiana ara-piarahamonina. \\nManana anjara toerana lehibe tokoa io fomba io, araka izany, satria « tsy tsara ny mitari-bady tsy lasam-bodiondry », hoy ihany ny Ntaolo.\\nNiovaova endrika ny fomba entimanolotra azy io : valopy tao alohaloha tao, dia niova ho lambakely tato aoriandriana ampiarahana amin’ny vatokely vitsivitsy, mba ho firariana fa ho mafy tahaka ny vato ny fatoram-panambadiana izay ajoro.  \\nAnkehitriny dia kitapo kely vita amin’ny landy tsara tarehy, misy kofehy miloko ranom-bolamena io. Mety ho angetsana angamba, hoy ianao, kanefa angetsana manandratra avo ny satan’ny fanambadiana. \\n–	ny saronan-karona : \\nsady fangatahan-dalana amin’ny zoky vavy io satria mandeha manambady alohany, no fanomezana tsodrano azy koa hahita ny anjarany. Harona kely mifanarona mitahiry fanomezana miavaka ataon-jandriny amin-jokiny io. Ny ho zaodahy no manolotra azy. \\nIreto koa misy ampaha-pomba mifandraika amin’ny fangataham-bady rahatr’izay: \\n1.	Fisehoana raha haka vady mba hahalalana fa tsy sangisangy tsy akory na sanatria ka hanao fanahin-jiolahim-boto na ho fitovoana foana.\\n2.	Fiantranoana sy fanateram-bodiondry ; ary amin’izany dia misy fombafomba izay mitoko telo miefa-madinika toy ny rano ankitsak’akoho toy izao : \\n3.	Fampakaran-teny fa tsy azo atao ny mitratrevatreva fiavy fa tsy maintsy mandady rariny sady vonona hanaraka ny hitsiny. Ampandrosoina vao mahazo miditra. \\n4.	Fialan-tsiny araka ireny efa fanaom-bahoaka sy ny fanaon’ny mpikabary raha handroso ny fitenenana ireny. \\n5.	Dom-baravarana ka misy vola atolotra amin’izany ho mariky ny hafaliana sahady fa nahazo nandroso. Efa be ny fanantenana na tsy mbola manomboka akory aza ny resaka. Vola io \\n6.	Sava ranonando, izany hoe, hiditra sy hanitsaka ny trano izay efa nohitsahin’ny razana efa nialoha ka dia manolotra ny haja sy ny sava ranonando amin’ny alalan’ny làlan-kodiavina. Vola io \\n7.	Aron-driaka na fanalana diso, izany hoe, be ny dinika sady ho be ny resaka ka ny teny maro tsy ilaozan’ota, sady be ny zava-tsy fantatra ; mpangataka fa tsy tompony. \\nNy mihinana aza misy latsaka; koa raha sanatria misy diso na zava-tsy fantatra nefa tokony ho natao dia aza itsingolohana izay vava diso na fahadisoana lahy fa areno ka ataovy zana-borona vonjen’ny reniny; atoroy fa toko tapaka, vilany mitongilana ka izay tsy mety areno. \\nKoa dia atolotra mialoha mba ho fisorohana ny fahadisoana ny 'aroriaka raha main’andro'. Vola io \\n8.	Alafady, izany hoe, hiteny fanambadiana eto anatrehan’ny olom-pady dia ny ray aman-dreny sy ny anadahin-jaza rehetra sy ny olom-pady hafa koa ao anatin’ny fianakaviana ka dia indro atolotra ny « alafady »Vola io \\n9.	Fangatahana hikabary sy hidinidinika ka miera fa ny akoho no maty eran’ny mpivady ary ny fanambadiana no raikitra eran’ny mpianaka. (tsy misy vola)\\n10.Fanolorana ny vodiondry izay kofehy lehibe hamatorana ny fanambadiana fa mahamenatra sy mahafa-baraka izany mitari-bady tsy lasam-bodiondry. Vola io, ary vola be tokoa. \\n11.Valim-babena, hani-mamy, solon-draharaha, kilalaon-jaza, lamba sy akanjon-dray aman-dreny. Vola io. \\n12.Hajan’ireo kiady sy voninahitry ny zazavavy; zaram-pangadin’anadahin-jaza, saron’ankaron’ny rahavavin-jaza fahatsiarovana ireo anadahin-drenin-jaza sy rahavavin-drenin-jaza ; rahalahin-drain-jaza sy anabavin-drain-jaza fa izany no atao hoe « fianakaviana ». Vola avokoa. \\n13.Solon-taozavatra ho harena hikambanan’izy mivady sy hampitomboiny. Vola io. \\n14.Hajan’ny mpikabarin-dRazazavavy dia ny rano an-tandrom-potsy izany hoe, toaka no atolotra na solon-toaka rehefa tsy misy ny toaka. Vola io. \\n15.Veloma farany fa hiainga ka dia atolotra ny saran-tsodrano sy ny ranom- bavaka mahabe fitahiana. Vola io. \\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "ohabolana malagasy",
            "patterns": ["ohabolana", "haingonteny"],
            "fampidirana": [
                "Ny ohabolana dia anisan'ny kolotsaina malagasy ary maro be ,ireto misy maromaro ary : ",
                "aay vee, ",
                "otranzao ny fanaovana azy : ",
                "ok, ",
                "ity ary e : ",
            ],
            "responses": [
                "aleo ro-madio tsy arahin-dromoromo toy izay hena matavy arahin'alahelo \\nMaty an-tanana toy ny valala samborim-boka \\nTsy ny tany no fady fa ny vavan'ny olona \\n.— Mandia tany isika, miloloha lanitra, mandiniha rehefa miteny, mijere vao mamindra\\nIzay misiditsidina ny eritreriny dia ho potraka noho ny nataony \\nMamono biby an-davaka ka hifoteran'ny rambony \\nSokiny nanani-bato ka tapa-dalan-kaleha \\nNy hazo avo halan'ny rivotra\\nTanon'Antanananarivo io ka izay mahavita aloha no manenina\\n Solafaka omen-tehina,potraka omen-kiraro \\nSolafa omen-tehina,potraka omen-kiraro \\nToy ny mamoaka omby tokana,vao mitehin-doha dia tapitra. \\nNy hana-dray aman-dreny dia toa ny tsipak'ombalahy,raha mahavoa mahafatsy raha tsy mahavoa mahafanina \\nTrano takatra ka izay mandrava azy mialoha no boka \\nAza atao tsy tiako bika ,tsy tiako tarehy\\nAza ny antsanga tsy aman'orana no alahatra \\nNy lela dia maranitra mandratra na malefaka manome tso-drano. \\nToy ny haloky ny tarehy eo amin'ny rano ny fo,izay havoakan'ny vavanao no maha hianao anao. \\nTsy misy ny afo raha tsy misy kitay,tsy misy ny ady raha tsy misy ny mpifosa \\nMiriorio ny angindina fa any an-kady ihany no hihafarany \\nNy zavona no manamaizina ny mazava. \\nNahoana no lala-masaka omaly, ka dia manjary tevan-kamono? \\nFanafodin'ny osa ny marina ataony. \\nraha zanaka tsy tia ray aman-dreny miteraha mba hahita \\nRaha zanaka tsy tia, miteraha mba hahita \\nRafotsibe mandinga-tatatra ka manitatra ny efa mikatona \\nNy soa atao hilevenam-bola, ny ratsy atao loza mihantona \\nAza zatra manao lalandririnina ka fahavaratra avy no manao hitsin-dalana \\naza manao mpitari-bato vilam-bava, ny tondroin'ny molotra hafa, ny ataon'ny tanana hafa \\nAleo enjehin'ny omby masiaka toy izay enjehin'ny heritreritra \\nMamoiza ry vaotay fa nangery eny ambony vato ny ankizy \\nBe famangotra toa rambon'osy, ny lanitra tsy ienjera tohanana fa ny vody kekerin'ny moka tsy heverina \\nataovy maro ny tiana dia ho vitsy ny fahavalo\\nAza miandry ny ho faly vao hitsiky fa mitsikia mba ho faly \\ntoy ny tsy hita de iray ny fiainana ka lozan'izay tia roa \\nhazakazaka arahitosika ity ny fiainana ka izay voky ihany no lelafin'ny namany, fa rehefa kely ianao de toy ny rafotsibe kendan'ny vomanga ka any antenda no manitsy azy\\n Afo anatin-tany ny fiainan'olombelona: soa izy ao , ratsy izy ao \\nNy olombelona voatr'ampangoro, ka mifandimby ambony sy ambany \\nAza mitomany ny randrana manendrika ny hafa Angady tokana;raha tapaka tsy misy hanakambanana azy indray. \\nAngady tokana;raha tapaka tsy misy hanakambanana azy indray. \\nNy tarehy ratsy tsy azo hovana fa ny fanahy ratsy kosa azo ovana \\nAza ny lohasaha mangina no jerena fa Andriamanitra eo an-tampon'ny loha \\nAza be siasia toy ny amalona andrano. \\nManao an'Andriamanitra tsy hisy ka mitsambiki-mikipy \\nAza manao: tsindrio fa resy;tano fa azo \\nTsy misy valiny ;hoatra ny manao soa aman-kazo. \\nTain'angely ka samy manilika ny ambaravarany\\nTsy maso fa sa fiandry loha no tsy mahita izay hojerena? \\nAza manao joko tsoriaka mahasambo-kary \\nIlatsahan'ny varatra am-pangerena, sady maty no mihoson-tay Toy ny ovy am-bato ny olona, maniry ihany fa tsy tomombana \\nToy ny ovy am-bato ny olona, maniry ihany fa tsy tomombana \\nTonga fa tsy tafiditra am-pahitra, toy ny omby noroahin-jaza \\nSakay sy voantsiperifery: ka samy mitondra ny ngidiny ho azy \\nNy vilany nandahoana no efa nipoaka \\nMaizina ny andro, azo tsilovina, lalina ny rano, azo lakanina, lalina ny hady, azo toharina, fa ny ratsy atao tsy mb azon-kevitra\\nNahoana no ho maty volon'ny ratsy, ka ny soa no ampanirina? \\naza manao solafaka andro mitsidika \\nNy zavona no manamaizina ny mazava. \\nNahoana no lala-masaka omaly, ka dia manjary tevan-kamono? \\nFanafodin'ny osa ny marina ataony. \\nraha zanaka tsy tia ray aman-dreny miteraha mba hahita \\nRafotsibe mandinga-tatatra ka manitatra ny efa mikatona \\nNy soa atao hilevenam-bola, ny ratsy atao loza mihantona \\nAza zatra manao lalandririnina ka fahavaratra avy no manao hitsin-dalana \\naza manao mpitari-bato vilam-bava, ny tondroin'ny molotra hafa, ny ataon'ny tanana hafa \\nAleo enjehin'ny omby masiaka toy izay enjehin'ny heritreritra \\nMamoiza ry vaotay fa nangery eny ambony vato ny ankizy \\nBe famangotra toa rambon'osy, ny lanitra tsy ienjera tohanana fa ny vody kekerin'ny moka tsy heverina \\nAza miandry ny ho faly vao hitsiky fa mitsikia mba ho faly \\nhazakazaka arahitosika ity ny fiainana ka izay voky ihany no lelafin'ny namany, fa rehefa kely ianao de toy ny rafotsibe kendan'ny vomanga ka any antenda no manitsy azy\\nAfo anatin-tany ny fiainan'olombelona: soa izy ao , ratsy izy ao \\nMaitso foana ny ahitra eny an-jaridainan'ny olona. \\nNy fifalian'ny sasany toa fahorian'ny hafa,ny sakafon'ny sasany toa pozina mifono ho an'ny hafa\\nFidio izay asa tena tianao ary dia tsy hanampy andro iray hiasana amin'ny fiainanao intsony ianao \\nNy fahadisoana dia zavatra tsy maitsy alohanao amin'ny fiainanao rehetra\\nRafotsy be kendam-bomanga, kenad ny nasesiky ny tananany \\nArakaraky ny eritreretanao ny farim-piainanao no fandanianao vola\\nTahaka ny kitoza ny fiainana , ka izay mahadinidinika azy ihany no mandre ny tsirony \\n Angady tokana;raha tapaka tsy misy hanakambanana azy indray\\nNy tarehy ratsy tsy azo hovana fa ny fanahy ratsy kosa azo ovana \\nAza ny lohasaha mangina no jerena fa Andriamanitra eo an-tampon'ny loha \\nManao an'Andriamanitra tsy hisy ka mitsambiki-mikipy \\n"
            ],
            "famaranana": [
                "So d mbl misy zvtr tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "hainteny2",
            "patterns": ["hainteny momban'ny alahelo"],
            "fampidirana": [
                "aaayy : ",
                "aay vee, ",
                "otranzao ny fanaovana azy : ",
                "ok, ",
                "ty ar : ",
            ],
            "responses": [
                "alahelo tsy ambara havana, zakan'ny tompony ihany \\nAkanga miditra ny ala, handroso tsy afaka, hiverina tapak'elatra, hijanona maninkavana \\nAntitra mikalokalo ka miafara amin ny ranomaso \\nAsesiky ny fitia sy ny hanina azy ka tsy mahalala masoandro ho faty \\nAza manao fihavanan-karena ka tomany handratra ny sasany \\nAza matoky fitiavana ka hitanjaka imasom-bady\\n\\nFaly malahelo toy ny manantena handova \\nIlay nihaino kalo ka tsetsetra no enti-mody \\nIzay mamì-maso manome alahelo; Fa ho lavo ny adala maro vava\\nIzay manome ny malahelo tsy hanan-java mahory, fa izay mitapi maso hahazo ozona be\\n\\nMampalahelo raha d kanosa loatra ka tsy maty raha tsy hianjeran-tanan-tsotro \\nMatin'ny ebo kely ka ataon’ny alahelo mitakiky \\nMitomany an-dreniny te-hinono; mitomany an-drainy te-hobabena \\n\\nNy alahelo toy ny rahona, raha mavesatra mianjera \\nNy alahelo toy ny raki-malala, ka raha tsy ny olon-tiana tsy amorahana azy\\nNy alahelon-janaka entamavesatra, tsy azony zaraina nefa mibaby ny zioga \\nNy fahafatesana lalan-kiraisana ihany fa tombon-dalana no an'ny lasa \\nNy faty mpanazakazaka, ary ny aretina vadin-koditry ny olombelona\\nNy nambolena tsy naniry, ny nasosoka maty maso \\nNy tompon'alahelo leo ihany, fa ny mpamendrofendro no tsy tanty \\nNy zanaka hendry mahafaly ny rainy; Fa ny zanaka adala mampalahelo ny reniny\\nNy zavona no manamaizina ny mazava \\nNy fifalian ny sasany toa fahorian'ny hafa, ny sakafon'ny sasany toa poizina mifono ho any hafa \\n\\nRaha indray mandeha no misambobary ka tsy mahazo, aza mandoro ny fatambary \\nSarotin'alahelo ka tia tsiri-pasana \\nSetroka sy tomany tsy mba sarotra fantarina \\nTapa-dia toy ny omby nafahy \\nTranobongo misy ronono ka sarotra atao malahelo \\nVahotra ny lela, mangidy ny rora, tsy hita izay voambolana ilazàna ny fahabangana \\nVivy nanitrika ka bongo-mason'ny nahiny \\nVorona tokana amoron-drano, ka miherikerika irery \\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "hain-teny",
            "patterns": ["fialantsiny", "fialan-tsiny"],
            "fampidirana": [
                "aaayy : ",
                "aay vee, ",
                "otranzao ny fanaovana azy : ",
                "ok, ",
                "ity ary e : ",
            ],
            "responses": [
                "Rehefa manomboka mikabary, fomba ny miala tsiny aloha ho fanajana sy \\nfanomezamboninahitra ireo olona manatrika ary koa ho fiarovan-tena ny mpikabary noho ny teny diso mety hambara na fahavotsana mandahatra. \\nIty misy santionanan-fialan-tsiny izay noraisina tao amin'ny  boky ' Faka sy Kolo Mikabary 21.3'.  \\n\\n Na dia omena ahy aza ny hitondra ny fitenenana eto anio, dia tsy maintsy miala tsiny ihany aho manoloana ny voninahitrareo rehetra izay manatrika etoana. \\n Ny hitsikitsika, hono, no tompon'ny dihy; \\n Ny vivy, hono, no tompon'ny rano\\n Ny railovy, no tompon'ny feo; \\n Ny Raiamandreny, no tompon'ny fitenenana\\n\\nTsy tokony hilaza aho, fa natao hilazana; tsy tokony hiteny, fa natao hitenenana; koa miala tsiny raha mandray fitenenana eto ankehitriny\\nMiala tsiny amin'izay rehetra hambarako etoana, noho  ny fahavotsavotsako mandahatra, ny fiambakavakako mivolona, mahatsiaro tena ho mitafy lamba imason'ny tompony ihany,\\n raha miteny eto anatrehanareo; tsy misy mahay mamindra tahaka ny akoho, hono, fa raha mandia sahafa solafaka ihany. \\n. Ny fitenenana mantsy toy ny rafi-biriky ka na tsara dinty sy tsara lasitra aza tsy hilaozan'izay hisy ho tapaka\\nNy didididiana, tsy ary mitovy; \\nNy kapakapaina, misy somaka; \\nNy fariparitana, tsy ary ho voatana; \\nNy teny maro, tsy hilaozan-diso\\n\\nKoa miala tsiny tompoko, fa ny tsiny mantsy tahaka ny tevan-dalina, itsiriha-mahafanina, ianjera-mahafaty ary tahaka ny oram-panala, tsy hita fa an-koditra vao mahangoly,\\nraha ananan-tsiny, hono, toy ilay petak'orona voan'ny sery, ka avo roa heny sy fahakentsonana. Tsy ho lany nadro hamira vava ny tsiny eto anefa isika, teny ihany izany ka teny, tsy izay hosoran-tantely akory no mamy, na izay hosoran-tsakay no mangidy,\\nfa  ny atao ihany no mahasoa na maharatsy. Koa lalao ny Fanahy mahaolona fa ny malemy fanahy sitr'olona, ny tsara fanahy tratra am-parany.\\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "kabary9",
            "patterns": ["taridresaka", "tari-dresaka"],
            "fampidirana": [
                "aaayy : ",
                "aay vee, ",
                "otranzao ny fanaovana azy : ",
                "ok, ",
                "ity ary : ",
            ],
            "responses": [
                "Tompokolahy sy tompokovavy hajaina Ambohimanambola no voka-tsaramaso, Ambohimanarina no mizihi-kibo Anjeva no matavy omby, Ambohimalaza no lafo kitay Antananarivo no vaventy trano, Ivakiniadiana no solavantony \\nNy tranokalantsika kosa no tiana hitombo hasina, ny fahendrena nentin-drazana no ndeha hiarahantsika mizaha sy manandratra eto anivon’izao sehatra fampirantina sy fifanakalozana izao.\\nMety ho lasan’eritreritra ihany angamba ianareo ka hanao hoe: efa lany taranaka sy lany tamingana angaha ny anivon’ny riaka? Sa sanatria ala nilaozan’apanga na kijàna nilaozan’omby?\\nLany  olomanga ve ny firenena? Nankaiza ny ray aman-dreny, nankaiza ny fotsy volo amin’ny tany, nankaiza ny manam-pahaizana sy ny kinga amin’ny fandaharana no dia ny zandry olona sy mbola maitso volo toa ny RNS vao 36 taona no mitondra ny teny sy mitarika amin’izao fikarohana izao? \\nSa kosa izao ilay hoe: « bingo manao matso ka misalovana ny anjaran’ny sasany »? \\nMarina izany tompokolahy, ekena tokoa re tompokovavy. Nefa nony tsy izany hoe « fandrotrarana an-tanàna haolo ka mandimby ray tsy satry », nony tsy izany hoe: « \\nhandidy hena eo ambony fe ka hisolo vaika ny ankàlana » dia tsaroana fa tsy ny railovy malaza ho andriamborona ny tena fa ny tsikirity madinika momba fody, tsy tompon-dia fa mpanaraka, mpiandry omby volavita, tsy tompony fa mpamerin-doha. \\nIzany indrindra no hanaovana azafady anareo mpamaky satria ny azafady sady fangatahan-dàlana no fanolorana ny haja mendrika anareo feno voninahitra manatrika sy manodidina eto. \\nMbola eto mantsy ny ray aman-dreny lolohavina an-tampon’ny loha, masoandro amam-bolana ary raha ny hitsikitsika no tompon’ny dihy, ny vivihy no tompon’ny rano, ireny no tompon’ny teny. \\nAo koa ny zoky be toa ray, angady nananana sy vy nahitana, tabiha sy rehareha tsy ialohava- mandeha, tsy salonani-miteny. \\nAo ianareo mitovy saranga amin’ny tena, kijeja niara-nita, valala niara-nanjohy, ny sasany aminareo aza zandry aman-taona fa zoky aman-pahalalàna sy fahendrena. Dia ao koa ianareo zandry, zanaka mahaleo mahalasana, saonjo mihoatra akondro, sakely mihoa-joro, kolokolo dimbin’ny vary. \\nAry farany am-pitenenana fa farany natao ho tsaroana satria heniky ny haja, dia ao ianareo andriambavilanitra loharanon’aina, loharanom-pianakaviana, mandeha izy ireny endriky ny lalana, mitoetra ravaky ny tokantrano. \\nIzany antanatohatra voatonona teo izany ry izy mianakavy no rano tsy dikain’ny zinga, ny iray tamin’ireo voatanisa ireo no tokony nandahatra teto. Ny miteny alohan’izy ireo dia toa ny miteny lango eo imason’ny vary, ny mikabary anoloan’izy ireo dia toy ny mitafy lamba eo imason’ny tompony. \\nNefa noho ny fahafantaran’ny CEN fa ny teny toa ny vato ka izay maivana ihany no atoraka, ny teny toa ny antsy ka izay maranitra ihany no adidy, ny sinibe rahateo tsy entim-matsaka dia izahay izao no tonga amin’ilay fampirisihan’ny Ombalahibemaso manao hoe: \\n« Ialahy no lefona tsy mba varombo, atomboka tsy mba milefitra. Ialahy no tangen-tsara hafatra, tsy menamaso mitsara. Ialahy no antsy be tsara hofana, adidy tsy mba madilo sady tsy miola-taola-mahery. Ka ento ny teny hoy izy fa lehilahy ialahy omban’ireo ombalahy antitra ireo » \\nTsapanareo amin’izany ary tompoko fa teny nomena ka mahasolanga fa raha tsy nomena izy no maha-joko. \\nSantatra am-bavarano ihany anefa iny ny anay, ny manetsabe mbola ho avy. Raha toa ka misy ny banga, ianareo mpamaky kosa handray ny andraikitra eto ampifanakalozana: tohizana izay maito, tentenana izay madilana. \\nMankasitraka tompokolahy, mankatelina tompokovavy\\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay ny azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "kabary11",
            "patterns": ["alasarona", "ala sarona"],
            "fampidirana": [
                "aaayy : ",
                "aay vee, ",
                "otranzao ny fanaovana azy : ",
                "ok, ",
                "ity ary e : ",
            ],
            "responses": [
                "Hoy ny Razana : Ny havozo hanitry ny ala, ny rambiazina hanitry ny tanety, ny voasary hanitry ny saha, fa ny kabary kosa hoy izahay hanitry ny fotoam-pivoriana.  \\nNy vilany mitongila adidy ny toko, ny basy tsy mipoaka adidin'ny vanja, ny omby mahia adidin'ny fahitra, ny akoho tsy maneno adidin'ny fisoko, ary ny kabary raha mati-maso adidin'ny malagasy tompony.  \\n\\nNy kabary nefa tsy toy ny vorodamba, hatriatra atsy, hatriatra aroa, fa mandeha an-drindrany toy ny rafitra ary mandry antsipriany tahaka ny didy savony no sady tsy bambaray tahaka an'i betsimitatatra fa singatsinganin'ny hain-teny aman'ohabolana;  \\nny kabary tsy ravahan'ireny vato nilaozan-tsahondra, tanety nilaozan'avoko farihy nilaozan-tsiriry, dobo nilaozan-tsikovoka, ary ala nilaozan-tanety, ka nialan'ny soa sy ny tsara. Kanefa na soa aza ny kabary; raha tsy hay tsinona tsy misy antony; fa toy ny fary fiahin'ny banga, tahaka ny penina anoratan'ny tsy nianatra.  \\n\\n Ny malagasy sy ny fahaiza-mikabary aza dia mbola azo antsoina hoe voahangy mitohom-bolamena, lopotra migalom-bolafotsy, solohoto sy firaka, harahara sy vy, tatamo sy voahirana ary rano sy vary. \\n\\n Fatratra ery izy izany! mba hahazoanao manandrana azy dia ity misy torolalana tsotra, atolotro anao amin'ny alalan'ity tranokala ity. \\n\\nTsy mihambo ity tranokala ity ho tonga lafatra ny tena, ny marina aza dia sila-bato fanao tambin-toko,tantely fanampin'ny aloka voankazo fanao hamohamo nefa mino anay fa ahitanao hevitra sy hanovozanao saina hahatonga anao ho isan'ny MAHAY MIKABARY  \\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "filozofia",
            "patterns": [
                "filôzôfia",
                "NY FANDINIHANA SY NY TOETSAINA FIOLOZOFIKA",
                "toe-tsaina filozofika",
                "filozofia",
            ],
            "fampidirana": [
                "aaayy : ",
                "aay vee, ",
                "otranzao ny fanaovana azy : ",
                "ok, ",
                "toy izao ary : ",
            ],
            "responses": [
                "\1-  Inona no atao hoe: filôzôfia?  \\n Ara-piforonan-teny ny filozofia dia «fitiavana ny fahendrena»na, raha ny marimarina kokoa dia hoe « sophia» izay midika fahaizana no sady fahafana miaina araka ny tokony ho izy, nefa ihany koa midika ho fahaizana.I Pythagore no namorona io teny io izay navadik’i M Heidegger ho toy ny fahendren’ny fitiavana taty aoriana.  \\n Ny fiolozofia ihany koa dia mety ho mitovy dika amin’ny hoe fahendrena raha ny dikateny malalaka, fa sady tsotra no manaiky ho vavolombelon’ny fitsarana tsy miangatra eo anatrehan’ny zavtra rehetra\\n Nanomboka tamin’ny andron’i Aristote (-384,-322) ka hatramin’ny taonjato faha XVIII, ny filozofia dia nitovy hevitra amin’ny hoe siansa raha ny hevitry ny teny amin’ny ankapobeny. Ny filozofia ihany koa dia rafitra homba-tsikera momba ireo resaka natokana hoan’ny fahalalana an’Andriamanitra sy ny amin’ny asa fanao\\n Ny filozofia ankapobeny dia manakaikikaiky amin’ny hoe metafizika (izay mandinika ny any ambadiky ny tontolon’ny tsapa na ny takatry ny taovam-pandrenesana)  \\nRaha ny hoe filozofia voalohany kosa indray, ny ontolojia, dia izay miresaka ny amin’ny antonantony voalohany sy ireo fitsipika fototra voalohany (Andriamanitra, ireo zavatra marina foana mandrakizay \\n2-	Inona no antsoina hoe: filôzôfy?   \\nHo an’ny fomba nenti-paharazan filozofika, ny hoe filozofy dia manondro an’ny raibe Pythagore. Nitovy dika tamin’ny hoe manam-pahaizana io teny io hataramin’ny taojato fahavao ambin’ny folo. Ilazana ihany koa ireo olona mandray ny fiainana ho amin’ny lafitsarany foana ihany koa ny filozofy na ireo izay mandray ny fiainana amim-paharetana \\nMbola azo iantsoina ny filozofy ihany koa ireo olona tsy manaiky afa-tsy ny saina ihany no tompom-pahefana amin’ny zavatra rehetra \\n. Raha lazaina kosa hoe «ireo filozofy » dia tsy iza fa ireo mpikambana tao amin’ny taonjaton’ny fahazana, sady tsy nino an’Andrfiamanitra, toan-dry VOLTAIRE, DIDEROT,…\\n3-	Ny fandinihana filozofika:  \\nNy fandiniha filozofika dia karazan fisintahana iray ary miezaka ny hamantatra ny tontolo no tanjony. Azo ampiharina izy araka izany na inona na inona olana mianjady amin’ny olona. I E KANT dia namintina ny fandaharan’asan’ny filozofia ho amin’ny fanontaniana efatra lehibe :  \\nIza moa aho? Io fanontaniana io dia miresaka indrindra ny olona araka ny fisiany. Mitovy hevitra amin’ny hoe « inona no atao hoe olona » araka izany io fanontaniana io.  \\nInona no azoko fantarina? : io fanontaniana io indray dia miresaka momba ny olan’ny fahalalana\\nInona no tsy maintsy ataoko? : ny amin’izany indray dia fitsipi-pitondra-tena na ny moraly no tena imasoany. Eton y olona dia tsy maintsy manatanteraka ny zavatra andrasana aminy fa manana saina sy fahafahana izy ; manana fitiavana sy adidy izy ary manana ny marina izay tsy maintsy ataony izy. \\nInona no azoko antenaina? : io fanontaniana io indray dia manontany antsika hoe misy dikany va ny fiainana ? Tena ny olona tokoa ve no mibaiko ny fiainany sa lalaovin’ireo hery anjamban’ny natiora fotsiny izy? \\n4- Ny toetsaina filozofika:\\nNy mampiavaka ny toetsaina filozofika dia noho ny fananany ireo toetra roa: toetra ara-pahalalana sy toetra ara- moraly. Raha te hanao filozofia araka izany dia tsy maintsy manana ireo toetra roa ireo :  \\na) Ireo toetra ara-pahalalan’ny toetsaina filozofika :\\ntoetsaina mahay mandinika ,toetsaina mahay mitsara\\nfisalasalana : fisalasalana siantifika, fisalasalana septika, fisalasalana metodika, fisalasalana hyperbolique  \\ntoetsaina mahay mitsikera  \\ntoetsaina mahay mamakafaka  \\ntoetsaina mahay mandravona \\nb) Ireo toetoetra ara-moralin’ny toetsaina filozofika :\\nfietre-tena ,hafanam-po ,herim-po ,faharetana  \\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "fiarovatena1",
            "patterns": ["ody varatra", "varatra", "fiaro"],
            "fampidirana": [
                "aaayy : ",
                "aay vee, ",
                "otranzao ny fanaovana azy : ",
                "ok, ",
                "toy izao ary : ",
            ],
            "responses": [
                "maro be ireo ody afaka atao mba hiarovana ny ratsy ka mila ianao mitoky amizay ampiasaina ary mila masim-bava tsara.Fadio ny mihinana fady amam-bava.\\nVomahery,bolila,tsy mahalatsaka,tsy maty vonoina,tsy lavon-drivotra,tany tsipaka,tsilavo andriana,lavenona,sakamalao,mafotera sy mavalia,oditra sokatra. \\nTotoina ireo dia ataovy anaty lamba mena dia ahatony aminy varavarana sy varavarakely ary ento anaraka anao na aiza naiza. \\n NB: Araho tsara ny andro sy ora anaovana azy ary ataovy aminy andro manarina anao hatrany,,,ora fanaovana azy amin'ny 122 atoandro.\\nMisaotra tompoko!\\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "fiarovatena2",
            "patterns": ["mpamosavy", "fandroahana mpamosavy"],
            "fampidirana": [
                "aaayy : ",
                "aay vee, ",
                "otranzao ny fanaovana azy : ",
                "ok, ",
                "toy izao ary : ",
            ],
            "responses": [
                "Fandroahana mpamosavy:\\nMangalaha tavohangy \\nAsio rano vohasina\\nRotsay sakamalao\\nampio fanjaitra 3 .\\nAleveno eo afovoany tokitany amin'ny 12 alina\\ntsy hisy mpamosavy andalo intsony eo mandrapaha \\nmiala ilay tavohangy\\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "fiarovatena3",
            "patterns": ["fisamborana mpamosavy"],
            "fampidirana": [
                "aaayy : ",
                "aay vee, ",
                "otranzao ny fanaovana azy : ",
                "ok, ",
                "toy izao ary : ",
            ],
            "responses": [
                "alaivo ny filahin'ny omby lahy tena mety\\nomby mainty tokam-bolo\\nhosory tantely\\nho itanao fa ny mpamosavy tonga dia malemy rah vao misakana anao\\ntsy fanao kosa anefa ny hoe andeha hoeny amin'ny fasana andro alina amin'ny tsisy dikany .\\nna hoe hiandry mpamosavy eny amin'ny fasana fa mety hiteradoza sy atambo\\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "fiarovatena4",
            "patterns": [
                "ody sy fanota mpamosavy",
                "ody",
                "fanota mpamosavy",
                "mpamosavy",
                "ody mpamosavy",
            ],
            "fampidirana": [
                "aaayy : ",
                "aay vee, ",
                "otranzao ny fanaovana azy : ",
                "ok, ",
                "toy izao ary : ",
            ],
            "responses": [
                "alaivo ny tahona mangahazo naniry nandritra ny 2 taona \\nDory ho lasa tapamporohana\\nmangalaha voanjo bory mainty\\nlelany cameleon\\natsofoy anaty tahomangazo\\nho ento rehefa mandeha amin'ny alina\\nfa tsisy mpamosavy sahy isakana anao zany\\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "fanafody gasy",
            "patterns": ["laingona goavy", "laingongoavy"],
            "fampidirana": [
                "toy izao ary ny vokatsoa azo avy amin'ny laingona goavy : "
            ],
            "responses": [
                "\\ny laingona goavy dia azo itsaboana areti-kibo ,kohaka\\nMitaneha ravina goavy 20 isa, rano tampakiny litre raha ohatra tratriny aretikibo sotroinaa mantetika namitsakoa raviny dia antelina ny ranony fa ariana ny faikany\\nTotoy ny raviny goavy atao zay azahoana ranony iray vera ampio ranomboasary makirana ary sotroy raha tratrany kohoka tohizana mandrampahafany tsara\\n\\nmirarisoa!\\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "fanafody gasy1",
            "patterns": ["papay", "ravina papay"],
            "fampidirana": [
                "toy izao ary ny vokatsoa azo avy amin'ny papay na ravina papay : "
            ],
            "responses": [
                "\\nRaha misy olona mitohana ka tsy afaka mamany ny lehilahy no tena betsaka voa dia mangalaha ravimpapay 30 ISA Efa nihitsana\\nTsy lay olona marary no aampakana azy afa olokafa\\nSasao ny ravina hadio dia totoy ataovy anaty vilany madio dia tampoy rano 5litre\\nTaneho mandritrany 30 minitra \\nAvelao angangatsiaka amizay dia omeo isotro ray vera izy ny maraian ray vera atoandro ray verany ariva\\nArakarakiny grave ny aretina ny fatrany rano omena azy siny vokatriny fahasitranana\\nTokony ho 48 dia hiverina normal ny toe-batany\\nmirarisoa!\\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "fanafody gasy2",
            "patterns": ["Tranompangaraka", "tranona fangaraka"],
            "fampidirana": [
                "toy izao ary ny vokatsoa azo avy amin'ny tranona fangaraka : "
            ],
            "responses": [
                "\\nOdy voankanina hoan-jaza izy ity\\nMangala ary tsanompangaraka rava ampio tany masiana naTany andohafasany andriana\\nAmpio volombody trano efa momoka iny\\nAfaka rory reo ary aampio rano zay itanao fa ampy lay zaza atao mandritrany herinandro\\nTokony 3 ANDRO DIA efa mahita vokatra\\nmirarisoa!\\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "aretina50",
            "patterns": ["fivaviana", "fivaviana mamofona"],
            "fampidirana": ["toy izao ary ny ady gasy amin'ny fivaviana mamofona : "],
            "responses": [
                "\\nAlaivo ny buble ny akondro ankitelo totoy izy rehetra esory ny faikany dia lay ranoniny ampio ranokely\\nAoriany fadimbolana izany no hatao ary aza manao firaisana mihitsy mandritra io telo andro io\\nmirarisoa!\\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "aretina51",
            "patterns": ["typhoide", "tifoida"],
            "fampidirana": ["toy izao ary ny ady gasy amin'ny typhoide : "],
            "responses": [
                "\\nIty no fanafody natoraly hitsaboina ny typhoide mba tsy andaniana volabe any aminy dokotera\\nMagalaha ronono 2litre aza asiana siramamy\\nOignons lehibe roa 1/2kg tongolo gasy\\nTotoy ireo tongolo rehefa avy nesorina ny odiny\\nAmpangotray anaty casserole ilay ronono  sy ireo tongolo teo\\nAvelao hangotraka 10NA15minitra aza atao mihoatra na latsaka\\nMisotroa 1/2NYMARAINA MBOLA TSY NISAKAFO siny hariva 30 minalohany hisakafo ataovy inindroa herinandro fotsiny\\nmirarisoa!\\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "fanafody gasy33",
            "patterns": ["fanabeazanaizana", "fandrindram-piterahana"],
            "fampidirana": ["toy izao ary ny ady gasy amin'ny fanabeazana aizana : "],
            "responses": [
                "\\nAlaivo ny voa ny tanatanamena\\nVoa sy lay hodiny voaloaha asorina koa lay faharoa ny nofony  zany sisa eo\\nAtelomy iny voa iny tsy asina rano an\\nIny dia ampy anao heritaona\\nFataro anefa aloha hoe mbola tsy mitoejaza ianao aza gaga koa famande ato iny mahazatra anao iny ny fadimbolanao\\nmirarisoa!\\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "aretina53",
            "patterns": ["sida", "SIDA"],
            "fampidirana": ["toy izao ary ny ady gasy amin'ny SIDA  : "],
            "responses": [
                "\\nMaro no efa nanao fikarohana mombany fanafody iadiana aminy ty aretina mandoza ity ka ity misy fomba ts tsotra izay inoako fa tsy vintsy mpahalala intsony\\nAlaivo ny ravina na mangahazo\\nTotoy ataovy betsaka tantavano ilay rano maintso be iny atao erakiny kaompy café\\nSotroy isamaraina alohany hinana sakafo maraiana, Ny traitement dia atao isamaraina mandritrany herinandro\\nmirarisoa!\\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "ohabolana1",
            "patterns": [
                "ohabolana momban'ny fanambadiana",
                "ohabolana mahakasika ny fanambadiana",
            ],
            "fampidirana": [
                "Ireto ary misy ohabolana vitsy2 mahakasina ny fanambadiana  : "
            ],
            "responses": [
                "\\n1.''Raha tianao ny hanana, dia aoka hianatra'.\\nManentana fa ny fitiavana sy ny fanambadiana dia mitaky fahalalana sy fahaiza-manao.\\n2.	'Ny fanambadiana dia toy ny hazo, mila fikarakarana.'\\nMampiseho fa ny fanambadiana dia mitaky fikarakarana sy fanohanana hatrany.\\n3.'Ny vato tsy ho tapaka raha ny hazo no mitazona.'\\nMampitaha ny fiarahana sy ny fanohanana eo amin'ny mpivady, milaza fa ny fifanampiana dia manamafy ny firaisana\\n4.Aza mitady ny tonga lafatra, fa mitadiava ny mifanaraka\\nManampy antsika hahatakatra fa tsy misy olona tonga lafatra, fa ny fifanarahana sy ny fandeferana no zava-dehibe\\n\\nIreo ohabolana ireo dia manan-danja amin'ny fanamafisana ny maha-zava-dehibe ny fanambadiana sy ny fitiavana. Raha te-hahafantatra bebe kokoa ianao, dia lazao fotsiny!\\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "ohabolana1",
            "patterns": [
                "ohabolana momban'ny fianarana",
                "ohabolana mahakasika ny fianarana",
            ],
            "fampidirana": [
                "Ireto ary misy ohabolana vitsy2 mahakasina ny fianarana  : "
            ],
            "responses": [
                "\\n1.	'Ny fianarana no fanalahidin'ny fahombiazana'\\nMampiseho fa ny fianarana dia manokatra varavarana ho an'ny fahombiazana sy ny fandrosoana.\\n2.'Raha tianao ny hanana, dia aoka hianatra'\\nManentana fa ny fianarana no lalana mankany amin'ny fahazoana sy ny fananana\\n3.'Ny hazo tsy mahavokatra raha tsy ampy ny fianarana'\\nMampitaha ny fianarana amin'ny fitomboan'ny hazo, fa ilaina ny fianarana mba hahatonga azy ho mahasoa.\\n4.'Ny fianarana tsy mety very'\\nManamafy fa ny fahalalana sy ny fahaiza-manao izay azo avy amin'ny fianarana dia tsy very na oviana na oviana.\\n5.'Ny fianarana no lova tsara indrindra'\\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "ohabolana2",
            "patterns": [
                "ohabolana momban'ny fanambadiana",
                "ohabolana fanambadiana",
                "ohabolana mahakasika ny fanambadiana ",
            ],
            "fampidirana": [
                "Ireto ary misy ohabolana vitsy2 mahakasina ny fanambadiana  : "
            ],
            "responses": [
                "\\n1.'Ny fanambadiana dia toy ny rohy, mila mitazona sy manohana'\\nMampiseho fa ny fanambadiana dia mitaky fahaiza-manao sy fandeferana\\n2.'Aza mitady ny tsara 100%, fa mitady ny tsara 80% sy mahay mankaty'\\n'Manampy antsika hahatakatra fa tsy misy olona tonga lafatra, fa ny fifandanjana sy ny fandeferana no zava-dehibe.'\\n3.'Ny fitiavana dia fanambadiana, ny fitiavana no andry'\\n'Mampitaha ny fitiavana sy ny fanambadiana ho fototry ny fiainana iombonana.'\\n4.'Tsy mifandray amin'ny vary ny fanambadiana'\\nMampiseho fa ny fanambadiana dia mila fikarakarana sy fanohanana, fa tsy mitovy amin'ny zavatra mora tohina.\\n\\nIreo ohabolana ireo dia manamafy ny lanjan'ny fanambadiana sy ny fitiavana amin'ny fiainam-piarahamonina. Raha te-hahafantatra bebe kokoa ianao, dia aza misalasala\\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "soatoavina1",
            "patterns": [
                "ohabolana momban'ny fihavanana",
                "ohabolana mahakasika ny fihavanana",
            ],
            "fampidirana": [
                "Ireto ary misy ohabolana vitsy2 mahakasina ny fihavanana  : "
            ],
            "responses": [
                "\\n1.'Ny fihavanana no fiainana.'\\nMampiseho fa ny firaisankina sy ny fifandraisana tsara no fototry ny fiainana mirindra.\\n2.'Aza mitady ny hadisoan'ny namanao, fa mitadiava ny tsara ao aminy.'\\nManentana antsika hijery ny tsara sy ny maha-samy hafa fa tsy hiady na hifanditra.\\n3.'Tsy hihafina ny angano, ny fihavanana no sira.'\\nMampitaha ny fahamarinan'ny fihavanana amin'ny fitohizan'ny tantara sy ny fifandraisana.\\n4.'Fihavanana, toy ny rano: raha miara-mitondra, madio.'\\nManampy antsika hahatakatra fa ny fiaraha-miasa sy ny fifankatiavana dia mitarika amin'ny fahasalamana sy ny fanadiovana.\\n\\nIreo ohabolana ireo dia manamafy ny maha-zava-dehibe ny fihavanana amin'ny fiainana andavanandro. Raha te-hahafantatra bebe kokoa ianao dia aza misalasala!\\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "OhabolanaM",
            "patterns": ["ohabolana", "famaritana ny atao hoe ohabolana"],
            "fampidirana": ["toy izao ary ny momban'ny ohabolana malagasy  : "],
            "responses": [
                "\\nNy ohabolana dia teny na andian-teny fohifohy mitovy amin'ny fiteny malagasy, izay ahitana hevitra lalina sy lesona momba ny fiainana, ny kolontsaina, na ny fomba amam-panao. Izy ireo dia matetika ampiasaina hanazavana hevitra na hanome ohatra amin'ny fomba fanao sy ny fihetsika.\\nIreto ny toetra manokana momba ny ohabolana:\\n1.	Fampianarana: Mampita lesona sy fahendrena amin'ny fomba tsotra.\\n2.	Fanairana: Mampahatsiahy ny olona amin'ny tokony hatao na tsy tokony hatao.\\n3.	Fomba fiteny: Matetika manan-kery sy mahasarika ny saina, amin'ny alalan'ny sary sy ny teny mamy. \\n\\nNy ohabolana dia manan-danja amin'ny kolontsaina malagasy, satria mitahiry ny fahendren'ny razana sy ny fiainam-piarahamonina. Raha mila fanazavana fanampiny ianao, dia aza misalasala!\\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "fomba malagasy",
            "patterns": ["famorana", "didipoitra"],
            "fampidirana": ["toy izao ary e  : "],
            "responses": [
                "\\nNy famorana dia fomban-drazana malagasy izay mifanandrify amin'ny fanombohana sy ny fankalazana ny fiainana, matetika amin'ny fotoana manokana toy ny fety na lanonana.\\nIty fombafomba ity dia mitaky fanajana sy fankatoavana, ary matetika misy ireo singa toy ny:\\n1.	Fandraisana anjara: Misy ny fianakaviana sy ny namana mandray anjara amin'ny fety na lanonana.\\n2.	Fanoloran-tena: Mety hisy sorona na fanomezana ho an'ny razana na andriamanitra\\n3.	Hira sy dihy: Mampifandray ny olona amin'ny alalan'ny kolontsaina sy ny fombafomba.\\n4.	Fifandraisana: Manampy amin'ny fanamafisana ny rohy eo amin'ny samy olona sy ny fianakaviana.\\n\\nNy famorana dia manan-danja amin'ny fankalazana sy ny fanamafisana ny maha-malagasy. Raha mila fanazavana fanampiny ianao, dia lazao fotsiny!\\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "fomba malagasy1",
            "patterns": ["famadihana"],
            "fampidirana": ["toy izao ary e  : "],
            "responses": [
                "\\nNy famadihana dia fomban-drazana malagasy izay midika hoe 'fandefasana ny razana.' Ity fombafomba ity dia atao amin'ny fankalazana ny razana, amin'ny alalan'ny fanokafana ny fasana sy ny famindrana ny taolam-baton'ny maty amin'ny akanjo vaovao.\\n\\nIreto ny tena endriky ny famadihana:\\n1.	Fankalazana: Manatanteraka fety miaraka amin'ny fianakaviana sy ny namana, miaraka amin'ny hira sy dihy.\\n2.	Fanaovana sorona: Mety hisy fanomezana na sorona ho an'ny razana sy ny andriamanitra.\\n3.	Fizahan-tany: Mampifandray ny taranaka sy manamafy ny fifandraisana amin'ny razana.\\n4.	Fampahatsiahivana: Mampahatsiahy ny olona ny zava-nitranga sy ny tantaran'ny fianakaviana.\\n\\nNy famadihana dia manan-danja amin'ny kolontsaina malagasy, satria manampy amin'ny fankalazana ny fianakaviana sy ny fahaiza-manao mankany amin'ny razana. Raha te-hahafantatra bebe kokoa ianao dia aza misalasala!\\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "anganon'ny Ntaolo",
            "patterns": ["angano", "anganon'ny Ntaolo"],
            "fampidirana": ["toy izao ary e  : "],
            "responses": [
                "\\nNy angano na angano ny ntaolo dia tantara na fomban-tantara malagasy, matetika mitantara ny zava-niseho taloha, ny tantaran'ny razana, ary ny fomban-drazana. Izy ireo dia ahitana:\\n1.Tantara mitombina: Mety ahitana zava-misy sy olona tena nisy, na tantara foronina.\\n2.Fampianarana: Manana hafatra na lesona izay tiana ampitaina, toy ny fitsipika sy ny fomba fanao\\n3.Fomban-drazana: Mampiseho ny kolontsaina sy ny fomba amam-panao malagasy, ary ny fiheverana ny razana.\\n4.Sary sy fihetseham-po: Mampiasa sary sy fihetseham-po maromaro hanazavana ny tantara sy ny vokany.\\n\\nNy angano dia ampiasaina amin'ny fanabeazana sy ny fankalazana ny kolontsaina, ary manampy amin'ny fanamafisana ny maha-malagasy.\\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "kolotsaina",
            "patterns": ["ankamatatra", "ankamantatra"],
            "fampidirana": ["toy izao ary e  : "],
            "responses": [
                "\\nNy ankamatatra dia fomba fiteny malagasy izay midika hoe 'fahatsiarovana' na 'fampahatsiahivana.' Izy io dia matetika ampiasaina amin'ny resaka manan-danja momba ny tantaram-pianakaviana, ny kolontsaina, na ny zavatra hafa izay tiana hotadidina.\\nIreto ny toetra manokana momba ny ankamatatra:\\n1.Fahatsiarovana: Mampahatsiahy ny olona ny zava-nitranga na ny olona manan-danja teo aloha.\\n2.Fampitandremana: Mety ho fampitandremana ho an'ny taranaka ho avy, mba tsy hanadino ny tantara sy ny fomban-drazana.\\n3.Fanamafisana ny maha-izy azy: Manampy amin'ny fanamafisana ny fiaviana sy ny kolontsaina malagasy.\\n\\nNy ankamatatra dia manan-danja amin'ny fanajana sy ny fankalazana ny tantara sy ny razana. Raha te-hahafantatra bebe kokoa ianao dia aza misalasala!\\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "kolotsaina1",
            "patterns": ["ohatra momban'ny anganon'ny ntaolo", "ohatra amin'ny angano"],
            "fampidirana": ["toy izao ary e  : "],
            "responses": [
                "\\nIreto misy ohatra vitsivitsy amin'ny angano malagasy malaza:\\n1.Ny Anganon'i Ibonia: Tantara mitantara an'i Ibonia, lehilahy mahery sy manam-pahaizana, izay niatrika ady sy nanavotra ny fianakaviany. Izy dia naneho ny fitiavana sy ny faharetana amin'ny toe-javatra sarotra.\\n2.Ny Tantara momba an'i Tsiranana: Ity angano ity dia mitantara ny fiainan'ny mpiaramiasa sy ny olona nahavita zava-dehibe ho an'ny fiarahamonina. Mampiseho ny herin'ny fiaraha-miasa sy ny fahaiza-manao.\\n3.Ny Fomban-drazana momba ny Rano: Misy angano manazava ny lanjan'ny rano sy ny fomba fanao amin'ny fanajana ny natiora, mampahatsiahy antsika ny tokony hitandrina sy hikarakara ny tontolo iainana.\\n4.Ny Anganon'ny Rano sy ny Vato: Tantara mampifandray ny rano sy ny vato, maneho ny fifandanjana sy ny fifandraisana amin'ny natiora.\\n\\nIreo angano ireo dia manampy amin'ny fampitana hafatra sy lesona momba ny fiainana sy ny kolontsaina. Raha mila fanazavana fanampiny ianao dia aza misalasala!\\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "kolotsaina2",
            "patterns": ["ohatra amin'ny kolontsaina malagasy"],
            "fampidirana": ["toy izao ary e  : "],
            "responses": [
                "\\nIreto misy ohatra amin'ny kolontsaina malagasy:\\n1.	Fomba fanao amin'ny famadihana: Fombafomba izay ahitana ny fanokafana ny fasana sy ny famindrana ny taolam-baton'ny maty amin'ny akanjo vaovao, miaraka amin'ny fety sy ny fiarahana.\\n2.	Hira sy dihy: Ny hira sy dihy malagasy, toy ny hira gasy sy ny sodina, dia manan-danja amin'ny fankalazana sy ny lanonana.\\n3.	Fomba fanajana: Ny fanajana ny razana sy ny fomban-drazana, toy ny fandehanana any amin'ny fasana sy ny fanompoana ny razana.\\n4.	Fianakaviana: Ny maha-zava-dehibe ny fianakaviana sy ny fifandraisana ara-pianakaviana, izay manamafy ny firaisankina sy ny fiahiana.\\n5.	Sakafo sy lovia: Ny sakafo malagasy, toy ny vary amin'anana sy romazava, dia anisan'ny kolontsaina, ary ny fomba fandrahoana sy fizarana sakafo.\\n\\nIreo ohatra ireo dia manampy amin'ny fanehoana ny maha-samy hafa sy ny hasin'ny kolontsaina malagasy. \\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "kabary1",
            "patterns": ["kabary malagasy", "kabary"],
            "fampidirana": ["toy izao ary e  : "],
            "responses": [
                "\\nNy kabary malagasy dia karazana teny na lahateny, matetika atao amin'ny fomba ofisialy na amin'ny lanonana manan-danja. Izy io dia ahitana:\\n1.	Fampidirana: Mampahafantatra ny mpihaino sy ny tanjon'ny kabary\\n2.	Fampahatsiahivana: Manazava ny lohahevitra sy ny antony mahatonga ny kabary.\\n3.	Fanehoan-kevitra: Manome hevitra na soso-kevitra amin'ny olana iray.\\n4.	Fanamafisana: Manamafy ny hafatra na ny tanjona tiana hotratrarina.\\n5.	Fifandraisana: Manampy amin'ny fananganana fifandraisana tsara eo amin'ny mpandray anjara.\\n\\nNy kabary dia matetika ampiasaina amin'ny fety, fanasan-draharaha, na hetsika ara-panjakana. Zava-dehibe ny fahamailoana sy ny fahaiza-manao amin'ny fiteny sy ny fomba fanao amin'ny kabary. \\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana?",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "kolotsaina6",
            "patterns": ["hain-teny malagasy", "hainteny", "hain-teny"],
            "fampidirana": ["toy izao ary e  : "],
            "responses": [
                "\\nNy 'hain-teny malagasy' dia manondro ny fahaiza-manao amin'ny fiteny malagasy, indrindra ny fahalalana sy ny fahaiza-miteny, manoratra, ary mahatakatra ny fomba fiteny sy ny fitsipika ara-pitenenana.\\nAnisan'izany ny:\\n1.Fampiasana ny voambolana: Mahafantatra sy mahay mampiasa ny teny sy ny andian-teny malagasy.\\n2.Fahamalinana amin'ny fehezanteny: Mahay mamorona sy mandinika fehezanteny araka ny fitsipika sy ny fomba fiteny malagasy.\\n3.Fahazoana sy fanekena: Mahatakatra ny dikan'ny teny sy ny fehezanteny, na amin'ny endrika miteny na amin'ny endrika soratana.\\n4.Fahaiza-manao ara-kolontsaina: Mahafantatra ny fomban-drazana, ny tononkira, sy ny fomba amam-panao malagasy.\\n\\nNy hain-teny dia zava-dehibe amin'ny fifandraisana sy ny fiaraha-miasa eo amin'ny olona, ary manampy amin'ny fanamafisana ny maha-malagasy. \\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "soatoavina malagasy2",
            "patterns": ["fihavanana"],
            "fampidirana": ["toy izao ary e  : "],
            "responses": [
                "\\nNy fihavanana dia foto-kevitra manan-danja amin'ny kolontsaina malagasy, izay midika hoe firaisankina, fifandraisana tsara, sy fahatsapana ho an'ny hafa.\\nManampy amin'ny fanamafisana ny fifandraisana sy ny fiaraha-miasa eo amin'ny olona, na amin'ny fianakaviana, namana, na ny fiarahamonina.\\n -Ny fihavanana dia manampy amin'ny fananganana fiaraha-monina miray, sy amin'ny fahaiza-manao miara-miasa.\\nMisy karazany maro ny fihavanana, anisan'izany:\\n1.	Fihavanana ara-pianakaviana: Mifandray amin'ny fifandraisana sy ny fanohanana eo anivon'ny fianakaviana.\\n2.	Fihavanana ara-tsosialy: Manamafy ny firaisankina sy ny fifandraisana tsara eo amin'ny olona ao amin'ny fiaraha-monina.\\n3.	Fihavanana ara-pivavahana: Mampifandray ireo olona amin'ny finoana mitovy na samihafa, amin'ny alalan'ny fivoriana sy ny fanompoam-pivavahana.\\n4.	Fihavanana ara-politika: Manamafy ny fiaraha-miasa sy ny fifanampiana eo amin'ny olona na antoko politika, amin'ny tanjona iraisana.\\n5.	Fihavanana ara-kolontsaina: Manampy amin'ny fizarana sy ny fankalazana ny kolontsaina sy ny fomban-drazana iombonana.\\n\\nNy fihavanana dia manan-danja amin'ny fanamafisana ny fiaraha-miasa sy ny fanampiana eo amin'ny samy olona. \\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "kolotsaina17",
            "patterns": ["fanandroana"],
            "fampidirana": ["toy izao ary e  : "],
            "responses": [
                "\\n Ny fanandroana dia fomban-drazana malagasy izay atao amin'ny alalan'ny fanombanana ny zava-mitranga sy ny toe-javatra amin'ny hoavy\\n Ity fomban-drazana ity dia matetika ampiasaina hanampiana ny olona haminavina ny hoaviny, toy ny amin'ny:\\n1 . Fampiasana ny fomba fanandroana:\\n -Astrologie: Misy ny fomban-drazana mifandray amin'ny fanandroana araka ny kintana sy ny volana.\\n -Fangatahana: Misy mpanandro (mpanao fanandroana) izay manao fivoriana amin'ny olona, mandray anjara amin'ny fivavahana sy ny fanompoam-pivavahana.\\n2. Tanjon'ny fanandroana: \\n -Fahendrena: Ny fanandroana dia manampy amin'ny fitadiavana vahaolana amin'ny olana sy ny fanapahan-kevitra.\\n -Fampaherezana: Izy io dia manome toky sy fanantenana ho an'ny olona amin'ny hoavy.\\n 3. Fomban-drazana sy kolotsaina\\n -	Fampirantiana: Ny fanandroana dia matetika ampiana fomban-drazana sy kolotsaina, mitazona ny fomba amam-panao.\\n -	Fivoriana: Mety hisy fivoriana sy fombafomba manokana ho an'ny fanandroana, izay mitazona ny maha-zava-dehibe azy.\\n\\n Ny fanandroana dia anisan'ny fomban-drazana malagasy, izay mitahiry ny soatoavina sy ny fomba fisainana mifandraika amin'ny fiainana sy ny hoavy.\\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "kolotsaina20",
            "patterns": ["sikidy"],
            "fampidirana": ["toy izao ary e  : "],
            "responses": [
                "\\nNy sikidy dia fomba fanao malagasy amin'ny fanandroana sy ny faminaniana, izay miorina amin'ny fomban-drazana sy ny kolotsaina.\\nIzy io dia mifandray amin'ny fanombanana ny zava-mitranga amin'ny hoavy, ary matetika ampiasaina amin'ny fanapahan-kevitra sy ny fisaintsainana. Ireto ny antsipiriany momba ny sikidy:\\n1. Fomba fanao:\\nFangatahana: Ny olona mangataka fanazavana amin'ny sikidy amin'ny alalan'ny fanontaniana manokana.\\nFandrafetana: Ny sikidy dia atao amin'ny alalan'ny fanaovana sary na endrika manokana (matetika amin'ny alalan'ny fanoratana amin'ny tany na taratasy)\\n2. Fitaovana:\\nFangaro: Misy fitaovana sy zavatra ilaina amin'ny fanatanterahana ny sikidy, toy ny vato na hazo.\\nSary: Ny fanamboarana endrika manokana dia zava-dehibe amin'ny fandraisana fanapahan-kevitra.\\n3.Tanjon'ny sikidy:\\nFaminaniana: Manampy amin'ny faminaniana sy ny fanombanana ny hoavy.\\nFahendrena: Ny sikidy dia manampy amin'ny fitadiavana vahaolana amin'ny olana sy ny toe-javatra.\\n4.Fomban-drazana:\\nKolotsaina: Ny sikidy dia ampahany manan-danja amin'ny kolotsaina sy ny fomban-drazana malagasy, mitahiry ny fomba fisainana sy ny soatoavina.\\nFanompoam-pivavahana: Mety hisy fombafomba sy fanompoam-pivavahana manodidina ny sikidy, manampy amin'ny fanamafisana ny maha-zava-dehibe azy.\\n\\nAmin'ny ankapobeny, ny sikidy dia fomba iray ahafahan'ny Malagasy maminavina sy mandinika ny hoavy, mitazona ny kolotsaina sy ny fomban-drazana amin'ny fiainana andavanandro.\\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "kolotsaina malagasy0",
            "patterns": ["firaisankina", "firaisankiana"],
            "fampidirana": ["toy izao ary e  : "],
            "responses": [
                "\\nNy firaisankina dia midika hoe fiaraha-miasa sy fiaraha-mientana amin'ny olona na vondrona iray. Izy io dia manan-danja amin'ny sehatra maro, toy ny:\\n1. Fiaraha-miasa:\\nFandaharan'asa: Ny firaisankina dia manampy amin'ny fanatanterahana ny tanjona iraisana, na amin'ny lafiny sosialy, toekarena, na politika.\\n2. Fifandraisana:\\nFifankatiavana: Mampitombo ny fifankatiavana sy ny firaisan-kina eo amin'ny olona, manampy amin'ny fandeferana sy ny fifanampiana.\\n3. Fampitomboana hery:\\nHery: Amin'ny alalan'ny firaisankina, afaka mahatratra vokatra lehibe sy mahomby kokoa ny olona, satria mitambatra ny loharanon'asa sy ny fahaiza-manao.\\n4. Fanabeazana:\\nSoatoavina: Ny firaisankina dia mitazona sy mampita soatoavina, fomban-drazana, ary kolotsaina, manampy amin'ny fitazonana ny maha-izy azy.\\n5. Fampandrosoana:\\nFandrosoana: Ny firaisankina dia zava-dehibe amin'ny fandrosoana sy ny fanatsarana ny fiainana andavanandro, satria manampy amin'ny fanatsarana ny toe-javatra iainana.\\n\\nAmin'ny ankapobeny, ny firaisankina dia manan-danja amin'ny fanamafisana ny fiaraha-monina sy ny fandrosoana amin'ny sehatra rehetra.\\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "ohabolana0",
            "patterns": [
                "ohabolana momban'ny firaisankina",
                "mahakasika ny firaisankina",
                "firaisakina",
            ],
            "fampidirana": ["toy izao ary e  : "],
            "responses": [
                "\1.	'Ny hery iray dia mahatonga ny asa'\\nMampiseho ny maha-zava-dehibe ny fiaraha-miasa sy ny firaisankina amin'ny fanatanterahana ny tanjona.\\n2.'Ny tanana iray tsy manasaka'\\nManondro fa tsy afaka miasa irery ny olona, fa ilaina ny fiaraha-miasa.\\n3.'Raha tsy mitambatra, tsy mitranga'\\n'Mampitandrina fa ny fiaraha-miasa no mitondra vokatra.'\\n4.'Iray ny tenda, iray ny rantsam-bato'\\nManambara fa na dia samy manana ny anjara asany aza, dia ilaina ny firaisankina amin'ny fahatanterahana ny tanjona.\\n5.'Tsy misy olona tonga lafatra.'\\nMampiseho fa ilaina ny mifanohana sy miara-miasa, satria samy manana ny fahalemena sy ny tanjona.\\n\\nIreo ohabolana ireo dia maneho ny lanjan'ny firaisankina sy ny fiaraha-miasa eo amin'ny fiaraha-monina.\\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "kolontsaina MALAGASY ",
            "patterns": ["kolotsaina malagasy", "kolotsaina", "kolontsaina"],
            "fampidirana": ["toy izao ary e  : "],
            "responses": [
                "\\ny kolotsaina malagasy dia manankarena sy maro karazana, miorina amin'ny tantara sy ny fomba fiainana manokana. Ireto ny sasany amin'ireo singa lehibe ao anatin'ny kolotsaina malagasy:\\n1. Fiteny:\\nMalagasy: Ny fiteny ofisialy, miaraka amin'ny fiteny frantsay.\\nFiteny sy fomban-drazana: Samy manana ny teniny sy ny fomba fiteniny ny faritra.\\n2. Sakafo:\\n•	Gastronomie: Ahitana sakafo mahazatra toy ny romazava, ravitoto, ary mofo gasy.\\n•	Zavamaniry: Ny vary dia fototry ny sakafo, ary ny anana sy ny hena dia ampiasaina betsaka.\\n3. Fomban-drazana:\\n•	Fety sy fanompoam-pivavahana: Ny Famadihana (fombafomba manam-pahaizana) sy ny Fetra (fety amin'ny fomba amam-panao).\\n•	Fampifandraisana: Ny fianakaviana sy ny havana dia zava-dehibe, ary ny fifandraisana ara-pihavanana dia voahaja.\\n4. Mozika sy Diabe:\\n•	Mozika: Misy karazana mozika toy ny salegy, hiragasy, ary tsapiky.\\n•	Diabe: Misy ny diabe sy ny fety lehibe, ahitana hira sy dihy.\\n5. Haisoratra sy Kolontsaina:\\n•	Lahatsoratra: Ahitana tononkalo, tantara, sy angano malagasy.\\n•	Proverbes: Fomba fiteny manankarena, manan-danja amin'ny fianarana sy ny fifandraisana.\\n6. Fanatanjahan-tena:\\n•	Fanatanjahantena: Ny basketball, football, ary ny moraingy (karazana ady an-tsehatra) dia malaza.\\n7. Zavakanto:\\n•	Hoso-doko: Misy ny zavakanto vita tanana, toy ny sary hosodoko sy ny famoronana.\\n•	Sary: Ny haikanto, toy ny vato sy ny hazo, dia ampiasaina amin'ny famoronana.\\n\\nNy kolotsaina malagasy dia mirakitra ny fiainana sy ny fomba fisainana manokana, mitahiry ny lova sy ny tantara izay anisan'ny maha izy azy ny Malagasy.\\n"
            ],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
        {
            "tag": "mandrapihaona",
            "patterns": ["bye", "viloma", "okay ary", "adios", ""],
            "fampidirana": ["ie, ", "ok, ", "eeenar, ", "Salut, ", "zayzn, "],
            "responses": ["C'était sympa de te parler", "à plus tard", "-!"],
            "famaranana": [
                "Sao mbola misy zavatra tinao anontaniana? ",
                "Mino aho fa nahafapo ny valiny",
                "izay n azo atolotra aloa",
                "mety mahavaly ny fanontanianao ve?",
                "ok, fanontaniana manaraka",
            ],
        },
    ]
}
