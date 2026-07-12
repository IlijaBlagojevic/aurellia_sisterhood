# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define igrac = Character("[iname]")
define p = Character("???")
default iname = "Paul"


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.



    $ iname = renpy.input("Unesi ime: ", default="Paul", length=15, allow="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ").strip()
    if iname == "":
        $ iname = "Paul"

    play music "audio/IgracPesma.mp3" fadein 2.0

    "Vec je gluvo doba noci."
    
    "Mnogi mladi ljudi odlucuju da se sele iz zemlje u potrazi za boljim zivotom."
    "Medjutim retki su oni koji su spremni da sami sebi iskroje sudbinu."

    scene bg soba
    with fade

    igrac "Gospode boze ove studije ne idu nikako..."
    igrac "Ne secam se kada sam polozio poslednji ispit."
    igrac "Stalno moram da se bkcem sa istim govnima akademskim"
    igrac "Od deset ispita ove godine polozio sam samo 3"
    igrac "Fakticki nisam ni na pola puta"
    igrac "Glad... Beda... Ocaj..."
    igrac "Bez prebijene pare u novcaniku"
    igrac "Tako mi i treba kad se razbacujem. Pre neki dan sam imao pravu gozbu."
    igrac "Uzeo sam pljeskavicu, pomfrit, veliku kolu i sladoled."
    igrac "Ne moze da se zivi kao car svaki dan."
    igrac "Pare sto mi moji salju nisu dovoljne za moje potrebe, dobio sam i otkaz sa part time joba sto sam imao"
    igrac "Mamlaz me nije ni isplatio kao coveka, ribao sam toalete kao obican bednik"
    igrac "Smrad se jos vuce zamnom, osecam ga duboko u nosu ughhh....."
    igrac "Samo sto nisam povratio"
    igrac "Vec neko vreme slusam na jutjubu magicne price o ljudima koji su nasli dobar posao online"
    igrac "Mozda je vreme da i ja potrazim tako nesto, ali sta??"
    igrac "Nisam dobar niucemu"
    igrac "Ja sam samo obican student medicine u pokusaju, ne bi mogao ni da izlecim coveka od prehlade"
    igrac "Verovatno bi dobio upalu pluca i umro kasnije"
    igrac "Da vidim neke od opcija na internetu"

    "Internet je bio pun oglasa koji nisu odgovarali ukusu naseg igraca"
    "Ili to ili nije imao dovoljno iskustva ni skolovanja za neke od pozicija"
    "Otvara prvi oglas..."
    "Potrebno pet godina iskustva za juniorsku poziciju"
    igrac "Bestraga..."
    "zatvara karticu"
    "Neplacena praksa uz mogucnost zaposlenja"
    igrac "Sta sam ja ovde rb?"
    "zatvara karticu"
    "Brza zarada od kuce"
    igrac "ne trazim brzu zaradu, samo hocu normalan posao"
    "Nakon sat vremena pretrage uspeo je da nadje manu svakoj ponudi"
    "Al onda mu je za oko zapao oglas"
    "Junior Assistant – Personal Guide | Aurellia Sisterhood"
    "Trazimo empaticne i organizovane osobe koje zele da rade sa zenama na njihovom putu licnog razvoja i samopouzdanja."
    igrac "Ovo zapravo zvuci zanimljivo"
    igrac "Asitent"
    igrac "Ne prodavac, ne agent"
    igrac "Asistent"
    igrac "Ako samo odgovaram na mejlove i zakazujem ruckove ne bi trebalo da bude toliko tesko"
    "Klik"
    "Sajt je izgledao normalno"
    "Fine boje, dobar UI"
    igrac "Empowerment"
    igrac "To je danas normalno, mnoge usamljene sredovecne zene koje imaju para i ne znaju sta ce sa sobom padaju na ove fore"
    igrac "Ok da popunim formular i posaljem zahtev, zanima me sta li ce mi reci"

    "Nakon nekog vremena zazvonio mu je telefon"

    scene bg phone
    with fade

    igrac "halo?"
    p "halo..."
    "Bio je to zenski glas"
    p "Da li je to [iname] ??"
    igrac "Da, to sam ja"
    p "Vidim zainteresovao vas je nas oglas za posao"
    igrac "Uhm... da, poslao sam vam svoje inf.."
    p "Imacemo sastanak sutra u 18h u kaficu. Radujem se nasem susretu i buducoj saradnji"
    "Klik"

    scene bg soba
    with fade

    "I samo tako je prekinula poziv"
    igrac "Pa ovo je bilo cudno... nisam ocekivao da cu dobiti poziv tako brzo"
    igrac "Kako god bilo moram da se spremim za sutrasnji sastanak"
    igrac "Iskreno nisam bio na sastanku za posao dugo vremena"
    igrac "Sada je vreme za spavanje"

    scene black 
    with fade

    "I tako sa osmehom na licu i malo nervoze [iname] je otisao na spavanje"
    "Ni sam nije bio svestan sta ce mu doneti sutrasnji dan"

    scene bg soba
    with fade


    # This ends the game.

    return
