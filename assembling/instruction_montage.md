
#Construction du lit#
## concept ##
L'idée est de faire un lit démontable surélevé inspiré des meubles de bateau du 19em siècle, d'aspect moderne,
mais disposant de vastes rangements adapté à la vie dans de petite surface .


Ma conception du design est d'avoir un objet :
 * fonctionnel
 * beau
 * durable
 * sobre

L'aspect technique est particulièrement important pour un lit 
qui est un meuble utilisé plusieurs heures par jours et soumis à pas mal de contraintes.
L'aspect esthétique est aussi primordiale, car puisqu'on surélève le lit, 
on augmente beaucoup sa taille subjective, et on court le risque de créer un élément qui écrase le reste de la pièce.


La durabilité est extremement importante philosophiquement (cristallisation du travail qui doit être transmise) et 
économiquement (seul un lit qui peut être gardé longtemps permet de justifier des materiaux de luxe, une construction complexe et un travail important pour le réaliser).


La sobriété découle de mes gouts esthétique et de l'imperatif de durabilité (la sobriété limite la maintenance).
Par ailleurs pour les projets sur mesure il est courant de tomber dans le sur-design.
Je m'inspire du rasoir d'Ockham et décrète que la solution la plus simple est préférable.

## Philosophie du design##

En terme mécanique, le lit ne respect pas les règles appliquées aux materiaux idéaux,
car il faut prendre en compte les variations de dimensions du bois, ses déformations (du à la charge ou pas)
et aussi les marges d'erreur lors de la construction qui doivent être suffisante pour qu'un 
amateur puisse fabriquer le lit.
Les choix d'assemblages sont justifiés.

Je m'inspire de certains éléments du developpement logiciel pour les appliquer à la menuiserie.
 * En particulier, j'intègre la dimension de modularité pour désigner sous systeme par sous système, 
et réduire la complexité de construction et les possibles conséquences d'erreur.
 * le deuxième élément est l'utilisation de méthode de test au fur et à mesure de la construction pour vérifier les sous systèmes, voir chaque assemblage.

## plan ##
Les plans sketchup sont disponibles,
tous les assemblages n'ont pas été dessiné par confort.
On peut consulter le graphe de liaison pour un récapitulatif des assemblages entre les pièces.

Le premier élément à intégrer est la nomenclature.
Le lit est divisé en sous partie,
les numérotations se font de haut en bas ou de gauche à droite 
ou de tête de lit vers le pied de lit.

Les sous parties sont 
 * Le socle (SOC)
 * les armature (A)
 * la ceinture (C)
 * la partie sommier (LS et L)
 
## construction et choix de design##
### Préparation ###
La liste des pièces est disponible,
j'ai acheté le bois au dimension, ce qui requiert d'avoir du bois biens sec pour éviter les déformations ultèrieurs.
La première chose à faire est le transport
Ensuite il faut impérativement nommé chaque pièce, en utilisant de la craie foréstière.
Vu le nombre de pièces (plus d'une centaine), c'est fastidieux mais absolument indispensable.

### Le Socle ###
#### Design####


Pour palier au sol non parfaitement plan, pour permettre un déplacement par glissement du lit,
pour augmenter la rigidité de l'ensemble, le lit est doté d'un socle qui sert de référence et sur lequel repose tout le reste.
A la base il s'agit de 4 planches en réctangles, augmentées de planches supplémentaires sous les éléments verticaux du lit (les armatures).

Ces planches supporte le poids total du lit (250kg+ personnes + poids tiroirs + poids contenu tiroir),
le rectangle pourrait être soumis à des forces de cisaillements (un coté ), et ne doit pas trop 
glisser au sol .

Je choisi des planches de 24 mm de hêtre, avec un doublure adaptée au sol (sol normal : liège, sol très déformé : mousse de tapi de sol)
qui sert d'amortisseur accoustique et mécanique, et d'interface pour limiter les variations de planéité du sol.

##### Socle- Socle
On demande essentiellement à ces planches de maintenir leur equerrage,
la solution classique serait des tenons mortaises, 
je choisi des grandes queues d'arondes à plat en mi bois.

Les avantages sont la rigidité et la resistance,
le défaut est l'hyperstatisme très conséquent qui fait que les 4 planches éxterieur doivent être bien ajustée,
puis les autres parfaitement ajustées à leur tour.

Le plan pour un gabarit est disponible.

##### Socle-Armature
Le plan pour un gabarit est disponible.

Ces assemblages assure la totalité des liaisons entre le lit et le socle. 
La contrainte d'avoir des tiroirs potentiellement traversant empeche d'utiliser des pièces qui feraient équerre en bois.
Le socle ne pourra donc pas maintenir les armatures debout et d'equerre. 
On décompose donc le problème autrement : 
le socle empeche les armatures de bouger dans le plan XY, mais ne garantie pas leur equerrage (celui ci resulte de la boucle armature+ceinture)

Pour cela on utilise des faux tenons, assez peu ajustés dans la longeur, mais ajusté en largeur. De cette façon, les armatures peuvent se déplacer de quelques 
millimètre en translation dans leur largeur, mais sont bloqué à quelques dixième de mm en translation dans la direction perpendiculaire.

L'autre solution serait que les armatures s'encastrent dans le socle, ce qui serait beaucoup plus contraignants en terme de précision d'assemblage,
et ferais risquer l'éclatement.

#### Réalisation ####
##### Socle - Socle
queue d'aronde plates

Tracer sur les planches en rattrapant les éventuels problème de longueurs de certaines planches.
Tracer aussi la ligne centrale sur `S_GD_2 et S_GD_3 et S_TP_2`

J'ai choisi d'utiliser un gabarit pour guider la défonceuse.
découper le gabarit au laser ou à la main de façon très soigneuse.
Il faut impérativement que le gabarit de guidage soit assez épais pour être résistant (medium >5mm).

Pour l'aronde male, réduire le mi bois à la défonceuse ou scie à ruban à lame largetrès rigide.
Dégrossir l'aronde male à la scie (à ruban), puis utiliser la défonceuse guider par le gabarit pour finir la forme exacte.

Pour l'aronde femelle,
percer à mi bois la partie à enlever à la perceuse pour réduire le travail de la défonceuse.
Utiliser la défonceuse avec une fraise roulement en haut et le gabarit pour finir l'aronde femelle,
ou défoncer à main levée et finir au ciseau à bois pour des bords nettes (utiliser une chute pour être bien vertical).

Parafiner les assemblages, puis les tester/ajuster en testant d'abord `S_TP_1, S_GD_1, S_TP_3, S_GD_4`.
Personnellement j'ajuste les assemblages avec une lime fine.
C'est déconseillé, mais je n'ai pas vu de raison valable de ne pas le faire sur bois dur.

Assembler tout le socle et vérifier les dimensions.

##### Socle-Armature #####
mortaise faux tenons

Les tracés sont essentiel.
Utiliser le gabarit pour tracer,
puis utiliser la défonceuse et le guide parallèle pour creuser les mortaises dans le socle.
l'endroit de début et de fin de chaque mortaise étant fait en respectant les tracées, avec qq mm de marge.
Le positionnement des mortaises est en revanche essentielle en largeur de la planche, et doit être le plus précis possible 
(1/10 mm, attention à l'usure de la fraise qui ne fera plus nécessairement 8mm)
Attention, tous les faux tenons ne sont pas centrés, ceux sur `SOC_TP_1, SOC_GD_1` ne le sont pas.
Attention de même pour le positionnement des mortaises sur `SOC_TP_3`.

(optionnel : en profiter pour les marques de début/fin de mortaises sur les parties concernées des armatures,
en pensant bien à tenir compte des parties verticales des armatures).




### Armature ###
#### Design ####

##### Armature - Amature
##### Armature - Socle'

#### Réalisation ####
##### Socle - Socle
##### Socle-Armature #####
