---
url: https://blog.cloudflare.com/fr-fr/rss/
title: Le blog Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:14:30.302442+00:00
---

# Le blog Cloudflare

> Source: https://blog.cloudflare.com/fr-fr/rss/

Le blog CloudflareAnalyses techniques approfondies, mises à jour produit et perspectives des équipes qui contribuent à bâtir un Internet meilleur.https://blog.cloudflare.com/fr-fr/ fr-frhttps://blog.cloudflare.com/favicon.icoLe blog Cloudflarehttps://blog.cloudflare.com Thu, 08 Oct 2026 08:14:27 GMTBâtir une autorité de certification post-quantique avec les certificats MTC (Merkle Tree Certificate)https://blog.cloudflare.com/fr-fr/pq-ca-with-mtcs/ Thu, 08 Oct 2026 04:51:32 GMTAlors que l’adoption des signatures post-quantiques menace de ralentir le déroulement des négociations TLS et de surcharger les registres de transparence des certificats (CT, Certificate Transparency), les certificats MTC (Merkle Tree Certificate) apportent une réponse permettant une authentification compacte et vérifiable. La nouvelle autorité de certification de Cloudflare prendra en charge l’émission à grande échelle de ces certificats.Certificate TransparencyCryptographieLe post-quantiqueSécuritéSemaine anniversaireTLSLorsque vous saisissez une adresse dans un navigateur, comment savez-vous que vous vous connectez au bon site web ? L’infrastructure à clés publique du web (Web Public Key Infrastructure, Web PKI) est un écosystème complexe et distribué de politiques, de protocoles et d’opérateurs d’infrastructure qui vous permet d’avoir la certitude de ne pas être redirigé vers un site incorrect ou malveillant. Au cours des dernières décennies, cet écosystème a connu des changements considérables. L’un d’eux réside dans l’apport de la transparence : l’obligation désormais incontournable d’enregistrer tous les certificats dans des registres publics de transparence des certificats (CT, Certificate Transparency). Cet écosystème fait désormais face à un autre défi : l’arrivée imminente de l’ordinateur quantique, qui nous contraint à migrer vers la cryptographie post-quantique (PQ) [d’ici 2029](https://blog.cloudflare.com/post-quantum-roadmap/).

Cette transition n’a rien de simple : la simple substitution de la cryptographie post-quantique aux algorithmes actuels des certificats à l’échelle d’Internet entraînerait une dégradation inacceptable des performances. Cette situation exige une nouvelle approche de l’infrastructure Web PKI, permettant de traiter la transparence comme une propriété native, et non pas comme un module complémentaire, et de concevoir un nouveau système capable d’adapter efficacement l’ampleur du déploiement des signatures post-quantiques.

Après avoir remporté un large soutien dans l’industrie, les certificats MTC ([Merkle Tree Certificate](https://datatracker.ietf.org/doc/draft-ietf-plants-merkle-tree-certs/?cf_target_id=CFFC2E8567A6377F4364011133409D19)) se sont imposés comme la voie à suivre. Cette année, au terme d’un [déploiement expérimental](https://blog.cloudflare.com/bootstrap-mtc/) réussi avec Chrome, Cloudflare avance à pleine vitesse sur les certificats MTC.

Suite à l’annonce d’aujourd’hui, dans laquelle Cloudflare déclare son intention de devenir une [autorité de certification (Certification Authority, CA)](https://blog.cloudflare.com/cloudflare-certificate-authority/), nous sommes ravis d’annoncer que cette autorité de certification prendra en charge l’émission de certificats MTC, avec l’objectif d’une inclusion début 2027 au sein du nouveau programme de clés racine à l’épreuve de l’informatique quantique ([Quantum-Resistant Root Store](https://googlechrome.github.io/chromerootprogram/index.html?cf_target_id=E232127C8952E7250AE8961A49E9A8F3)) lancé par Chrome. Fidèles à notre mission de contribuer à bâtir un Internet meilleur, et dans le respect de la tradition de Cloudflare consistant à offrir [gratuitement](https://blog.cloudflare.com/post-quantum-crypto-should-be-free/) la cryptographie la plus robuste qui soit, nous proposerons l’émission standard de certificats MTC sans frais. Disposer d’une autorité de certification capable d’émettre à la fois des certificats classiques et des certificats MTC nous permet d’adopter par défaut la méthode d’authentification la plus sécurisée disponible, et ainsi, de proposer à une grande partie d’Internet une approche simple et performante de l’évolution vers la cryptographie post-quantique.

## **L’écosystème de confiance actuel**

Pour comprendre en quoi les certificats MTC changent la donne, commençons par expliquer quelques notions sur l’établissement de la confiance sur le web aujourd’hui.

Côté client, les navigateurs (dans ce contexte, les « clients TLS ») gèrent des programmes racine qui définissent un ensemble de politiques que les autorités de certification doivent respecter pour être reconnues de confiance. Côté serveur, les autorités de certification se comportent comme les garants de la confiance : elles exploitent une infrastructure d’émission de certificats au sein de laquelle elles valident la propriété des domaines et confirment le lien existant entre un nom de domaine et une clé publique qui démontre la propriété de ce domaine.

Mais comment vérifier que les autorités de certification respectent ces règles ? C’est là qu’intervient la transparence des certificats (Certificate Transparency, CT), qui rend l’émission de certificats publiquement vérifiable. Lorsqu’une autorité de certification émet un certificat, elle doit également le soumettre à au moins deux registres publics. Cloudflare exploite la famille de registres CT [Nimbus](https://blog.cloudflare.com/introducing-certificate-transparency-and-nimbus/) depuis 2016 et lance aujourd’hui Raio, une nouvelle famille de [registres CT statiques](https://blog.cloudflare.com/azul-certificate-transparency-log/).

Bien que l’écosystème CT rende les certificats consultables par tous, cela ne garantit pas pour autant qu’ils ont été correctement émis ou qu’ils sont sûrs d’utilisation. La surveillance pèse ici dans la balance, en comparant les entrées de ces enregistrements avec les informations qu’attendaient les propriétaires de domaines et en signalant toute activité suspecte. Cloudflare a lancé le programme [Certificate Transparency Monitoring](https://blog.cloudflare.com/introducing-certificate-transparency-monitoring/) en 2019 et l’a récemment proposé en [disponibilité générale](https://blog.cloudflare.com/certificate-transparency-monitoring-ga/). Nous publions également des mesures à grande échelle sur les certificats sur la page [Certificate Transparency](https://radar.cloudflare.com/certificate-transparency?cf_page=pq-ca-with-mtcs%2F&cf_target_id=E27CCFEF5B960B537C9CFD2D6DD9CEDC) dans Radar (anciennement appelée Merkle Town).

À mesure que les entreprises commenceront à mettre à niveau leurs serveurs pour adopter l’authentification post-quantique, la surveillance de la transparence des certificats jouera un rôle encore plus important dans la détection d’éventuelles attaques par rétrogradation post-quantique. Les propriétaires de domaines ayant accompli la migration vers l’authentification post-quantique devront surveiller les registres de transparence des certificats pour détecter l’émission inattendue de certificats hérités, afin d’éviter que les clients ne basculent vers un schéma de rétrogradation malveillant.

Un des problèmes affectant le système actuel réside dans l’ajout a posteriori de la transparence, qui entraîne des problèmes de déploiement de grande ampleur. Les certificats sont fréquemment enregistrés plusieurs fois, sous différentes formes, dans plusieurs registres distincts, contraignant les outils de surveillance à télécharger et à traiter chaque registre afin de ne manquer aucune émission. Cette démarche peut être coûteuse, freinant l’émergence d’un ensemble diversifié d’opérateurs de registres à l’échelle d’Internet. Selon nos estimations, les signatures post-quantiques multiplieront par 40 le volume de données que devront stocker les journaux de transparence des certificats. Ce défi d’évolutivité et le défaut d’alignement des incitations qui en découle sont au cœur de la problématique du déploiement à grande échelle de la cryptographie post-quantique.

## **La problématique du déploiement à grande échelle de la cryptographie post-quantique**

Nous avons écrit un nombre considérable d’articles sur les [difficultés que comporte le déploiement à grande échelle de la cryptographie post-quantique](https://blog.cloudflare.com/bootstrap-mtc/), mais pour résumer nos réflexions : pour prendre en charge l’authentification des serveurs à l’échelle d’Internet, l’infrastructure Web PKI doit authentifier environ un milliard de serveurs TLS sans précharger la clé publique de chaque serveur sur chaque client. Historiquement, les autorités de certification ont résolu ce problème en utilisant des chaînes de certification comme un mécanisme de distribution de la confiance. Au fil du temps, toutefois, des ajouts tels que les vérifications de révocation de clés et la transparence des certificats ont entraîné l’accumulation des clés publiques et de signatures – cinq signatures et deux clés lors d’une négociation TLS typique. Les signatures post-quantiques sont environ 40 fois plus volumineuses que les signatures classiques, entraînant d’importantes surcharges de données, dont la gestion à grande échelle s’avérerait coûteuse pour les clients, les autorités de certification, les registres et les outils de surveillance.

C’est là qu’interviennent les certificats [Merkle Tree Certificates](https://datatracker.ietf.org/doc/search?name=draft-ietf-transcert-merkle-tree-certs&rfcs=on&activedrafts=on&olddrafts=on&cf_target_id=9B6622E7145450DAB15BCBE6729DA4C5) (MTC), une spécification en cours d’élaboration par le groupe de travail [PLANTS de l’IETF](https://datatracker.ietf.org/group/plants/about/?cf_target_id=4B0919233143D8572778FB2863B1D133), qui décrit une architecture permettant d’obtenir des certificats post-quantiques compacts et efficients. Les certificats MTC regroupent les certificats dans un arbre de Merkle à ajout exclusif («  _append only_ »), permettant à une autorité de certification de signer la racine de cet arbre plutôt qu’une multitude de certificats individuels. Les navigateurs ou autres clients peuvent ainsi vérifier un certificat au moyen d’une preuve d’inclusion compacte (c’est-à-dire une séquence de hachages cryptographiques) adossée à une tête d’arbre signée, au lieu de devoir valider chaque certificat individuellement. Une [idée fondamentale](https://datatracker.ietf.org/meeting/124/materials/slides-124-plants-solution-space-and-dispatched-work-00?cf_target_id=64022AE848C0F9046785AA5EEAB10EF6) des certificats MTC réside dans le postulat « n’enregistrez pas ce que vous émettez, émettez en enregistrant ». En couplant l’émission et l’enregistrement, la transparence devient une condition intrinsèque de fonctionnement, et non un simple module complémentaire.

## **Le rôle d’une autorité de certification dans une PKI repensée**

Nous développons notre capacité à émettre des certificats MTC comme une facette indissociable de la création de l’autorité de certification Cloudflare. Cela exige d’assurer le suivi des nouvelles exigences des programmes de clé racine post-quantique et de concevoir une pile logicielle d’émission et de réplication («  _mirroring_ »), tout en développant les infrastructures, les opérations et les fonctions de conformité de l’autorité de certification traditionnelle. C’est un défi de taille !

L’avantage est que nous pouvons hiérarchiser, dès le premier jour, les exigences et l’architecture de cette nouvelle infrastructure PKI post-quantique, en structurant notre environnement d’une manière fidèle aux valeurs et au réseau mondial de Cloudflare, avec l’ambition de rester aussi transparents que possible pendant cette nouvelle aventure.

Examinons l’architecture mise à jour pour les certificats MTC :

Si vous la comparez à l’écosystème d’une autorité de certification traditionnelle, vous remarquerez que les responsabilités d’une autorité de certification restent sensiblement les mêmes : valider le contrôle d’un domaine, lier ce domaine à une clé publique, puis émettre des certificats. La principale différence réside dans le fait que, dans l’écosystème MTC, au lieu de signer directement les certificats, puis de les enregistrer, l’autorité de certification gère désormais un registre de transparence adossé à un arbre de Merkle, où une preuve d’inclusion du certificat dans l’arbre sert d’ancre de confiance. Les autorités de certification exploiteront également des cosignataires de réplication __(« mirroring cosigners ») qui conservent une copie des registres d’émission, en vérifient la cohérence en ajout exclusif et garantissent la transparence et la disponibilité de ces registres pour l’ensemble de l’écosystème.

### **Émettre des certificats MTC**

Les certificats MTC se présentent sous deux formes, pouvant toutes deux être encodées dans le format de certificat X.509 que les logiciels clients reconnaissent aujourd’hui, avec simplement un algorithme de signature « inhabituel ». Sous sa forme autonome («  _standalone »)_ , la valeur de signature du certificat contient une tête d’arbre cosignée d’un registre d’émission et une preuve d’inclusion (c’est-à-dire une suite de hachages) démontrant que le certificat est bien contenu dans ce registre. Si les clients peuvent obtenir les têtes d’arbre cosignées hors bande (par exemple, via un mécanisme de mise à jour du navigateur), le certificat peut alors être servi sous une forme relative à un point de repère («  _landmark-relative_ »). Dans ce cas, la valeur de signature consiste en la preuve d’inclusion légère, sans aucune signature post-quantique volumineuse.

Pour simplifier, prenons l’exemple de l’émission d’un certificat autonome. Lorsqu’un site web requiert un certificat pour son domaine, il peut le demander auprès d’une autorité de certification via le protocole ACME (Automatic Certificate Management Environment), qui gère les demandes de certificats, la validation du contrôle de domaine et les flux d’émission. L’infrastructure ACME de Cloudflare sera un fork de [Boulder](https://github.com/letsencrypt/boulder?cf_target_id=A6BFE2F45BAE186A5FFDA4C9474F83C0), le logiciel ACME largement déployé et éprouvé sur lequel repose Let’s Encrypt. Let’s Encrypt développe activement la [prise en charge des certificats MTC](https://letsencrypt.org/2026/06/03/pq-certs?cf_target_id=1C78F33F785DDD4CD36995A30DA067DB) dans Boulder, et nous avons l’intention de gérer notre propre fork qui intègre ces modifications en amont ainsi que des modifications spécifiques à Cloudflare, tout en contribuant, autant que possible, à l’initiative en amont.

Lorsque l’autorité de certification MTC reçoit une demande d’émission de certificat, le serveur ACME de l’autorité de certification vérifie que le serveur demandeur contrôle effectivement le domaine. Si ces vérifications réussissent, l’autorité de certification sérialise ces données et les ajoute à un registre à ajout exclusif.

Après avoir ajouté l’entrée MTC à son registre d’émission, l’autorité de certification calcule l’état mis à jour du registre, puis signe un point de contrôle («  _checkpoint_ ») correspondant à cet état. Ce point de contrôle atteste que l’autorité de certification a émis chaque entrée incluse dans l’arbre de Merkle du registre jusqu’à ce moment précis.

L’autorité de certification envoie ensuite son état de registre mis à jour et son nouveau point de contrôle à un cosignataire de confiance, qui conserve durablement une copie du registre d’émission de l’autorité de certification et vérifie que chaque nouvel état est conforme au principe d’ajout exclusif, reste cohérent avec l’arbre précédent et est correctement formé. Cette cosignature supplémentaire garantit aux clients et aux outils de surveillance qu’un tiers de confiance a observé le même état du registre et a vérifié que l’autorité de certification ne présente pas des visions divergentes de l’émission aux différentes parties de l’écosystème. Elle garantit également que les certificats émis restent disponibles aux fins de la surveillance, même si le registre d’émission de l’autorité de certification devient indisponible.

La [politique provisoire du programme de clés racine à l’épreuve de l’informatique quantique (Quantum-Resistant Root Program)](https://googlechrome.github.io/chromerootprogram/cqrp/draft-policy/?cf_target_id=281E7879BC2BC1DCECCED306F10B9A5C) de Chrome exige au moins deux cosignatures : l’une provenant d’un cosignataire de réplication («  _Mirroring Cosigner_ ») reconnu par Chrome et exploité par une organisation distincte, et l’autre provenant de l’autorité de certification MTC émettrice elle-même. Nous gérerons donc des systèmes de réplication pour d’autres autorités de certification pilote et exigerons au moins une cosignature indépendante sur nos propres certificats émis.

Cloudflare intégrera son cosignataire de réplication à [Azul](https://github.com/cloudflare/azul?cf_target_id=8C0EFCF2F40FB988632140F9DBC0EA0B), notre registre de transparence open source écrit en Rust et, pour une interopérabilité maximale, implémentera le protocole [tlog mirror de c2sp](https://c2sp.org/tlog-mirror@v0.1.0?cf_target_id=3CA9474DEEB73A3D70C7548A42CE20D8).

Enfin, après avoir reçu avec succès la cosignature d’un cosignataire de réplication, l’autorité de certification assemble un certificat MTC avec les cosignatures, la clé publique du serveur et une preuve d’inclusion. Elle transmet ensuite ce certificat MTC au serveur, qui peut alors l’utiliser pour l’établissement de connexions TLS.

### **Distribuer efficacement les signatures post-quantiques : l’optimisation par points de repère (« _landmarks_ »)**

Bien que les certificats autonomes soient pleinement fonctionnels, ils transmettent encore des signatures post-quantiques volumineuses lors de la négociation TLS, ce qui limite leur efficacité. Les véritables gains de performance qu’offre l’architecture des certificats MTC proviennent des certificats relatifs à un point de repère («  _landmark-relative_ »).

Au lieu de transmettre des cosignatures incluses dans chaque certificat, les autorités de certification peuvent désigner comme point de repère («  _landmark_ ») une séquence de sous-arbres englobant l’ensemble des certificats actifs dans le registre, puis diffuser ces sous-arbres (ainsi que les données permettant de les authentifier) auprès des clients via un service de mise à jour hors bande. Lors d’une négociation TLS, l’authentification effective auprès du serveur se déroule lorsque le navigateur vérifie que les données de certificat du serveur (notamment son nom de domaine et sa clé publique) figurent bien dans un sous-arbre de confiance du registre de l’autorité de certification. Si la preuve d’inclusion relie ce certificat à un point de repère («  _landmark_ ») cosigné, et si la clé publique prouve ensuite la propriété lors de la négociation TLS, le client sait qu’il communique avec le bon serveur.

En transmettant périodiquement ces signatures et ces métadonnées d’arbre aux clients TLS hors bande, un nombre restreint de signatures par lots MTC peut permettre de couvrir efficacement des milliards de certificats émis par une autorité de certification donnée. Bien que les repères se montrent plus efficaces à grande échelle, ils n’éliminent pas pour autant le besoin de certificats MTC autonomes : des clients peuvent avoir été récemment installés, être hors ligne ou ne pas disposer de la mise à jour du point de repère («  _landmark_ ») concerné. C’est pourquoi il est important que les serveurs conservent une solution de secours, sous la forme d’un certificat autonome.

## **Les certificats MTC dans la réalité : résultats de notre expérience avec Chrome**

Cette année, nous avons réalisé une expérience avec Chrome afin de tester la faisabilité des certificats MTC entre un client et un serveur. Nous avons exploité une « autorité de certification d’amorçage » (concrètement, une fausse autorité de certification simulant le pipeline d’émission) qui émettait des certificats MTC adossés à une chaîne de certification traditionnelle pour une sélection de domaines Cloudflare hébergés sur l’offre « gratuite » de Cloudflare, et nous avons délivré ces certificats à 50 % des utilisateurs de Chrome Beta 146. Pendant cette expérience, nous avons délivré avec succès des milliards de certificats MTC.

En ce qui concerne TLS, nous avons constaté que le cas d’usage est assez efficace : avec un certificat relatif à un point de repère («  _landmark-relative_ »), la négociation n’a besoin de transmettre qu’une clé publique, une signature et une preuve d’inclusion de moins de 1 ko. Pendant l’expérience, nous avons basculé vers la chaîne de certification traditionnelle, plutôt que vers un certificat autonome dans les cas où nous ne pouvions pas négocier un certificat relatif à un point de repère avec le client. Au regard de la transparence des certificats (Certificate Transparency, CT), les certificats MTC modifient également les propriétés d’évolutivité de la transparence : le registre n’a besoin de conserver que des hachages des clés publiques ; il n’y a pas de signature par entrée, et la signature sur la tête d’arbre couvre l’ensemble du registre. Ceci évite la prolifération massive des certificats, car le registre d’émission de l’autorité de certification devient la source unique de vérité pour tous les certificats émis, et les consommateurs de registres n’ont besoin de récupérer qu’une seule copie de chaque certificat.

En conclusion, les certificats MTC fonctionnent vraiment ! En médiane, l’utilisation d’un certificat MTC avec point de repère MTC est 9 % plus rapide qu’une chaîne de signatures classique (il est vrai que la majeure partie de ce gain de performance est liée à l’élimination des certificats intermédiaires). Et parce que nous avons testé les certificats MTC avec des signatures classiques, nous anticipons une amélioration encore plus grande avec les signatures post-quantiques. Forts de ces résultats satisfaisants et du niveau de collaboration intersectorielle autour des certificats MTC au sein du groupe de travail [PLANTS](https://datatracker.ietf.org/wg/plants/documents/?cf_target_id=8335A889D12318472725B9F10A9669C3) de l’IETF, nous avons commencé à mettre fin à cette expérience le mois dernier (août 2026).

## **L’avenir des certificats MTC**

Nous sommes ravis que notre expérience avec Chrome ait permis de démontrer le fonctionnement des certificats MTC dans la pratique, et nous sommes particulièrement enthousiastes à la perspective d’émettre des certificats en tant qu’autorité de certification à part entière.

Il reste cependant des questions plus vastes auxquelles nous ne pourrons répondre qu’en réalisant cette grande expérience à l’échelle de l’écosystème PKI dans son ensemble. Les outils de surveillance indépendants seront-ils capables de [consommer et de vérifier](https://transparency.dev/summit2025/talks/verifiable-indexes.html?cf_target_id=E1796EAC8A8AAFB2E9C2E5A45AE0209B) les registres d’émission de certificats MTC au volume de la production ? Une multitude d’autorités de certification et de cosignataires émergera-t-elle pour assurer la diversité indispensable à la résilience du système ? Comment les navigateurs doivent-ils équilibrer les gains de performance des certificats MTC légers basés sur les points de repère («  _landmarks_ ») et les chemins de secours indispensables pour les clients sans points de repère récents ? Les certificats MTC s’imposent comme l’architecture de référence pour l’authentification post-quantique, mais prouver leur efficacité à l’échelle d’Internet et au volume de la production exigera l’implication d’un ensemble diversifié de programmes de clés racine, d’éditeurs de navigateurs, d’autorités de certification, de cosignataires de réplication, d’outils de surveillance et de la communauté dans son ensemble.

C’est un honneur pour nous de participer à cette prochaine phase de l’écosystème Web PKI, et nous prenons très au sérieux la responsabilité d’exploiter une infrastructure d’autorité de certification. Les autorités de certification occupent une position privilégiée au sein de l’écosystème de confiance : navigateurs, propriétaires de domaines et utilisateurs du quotidien comptent sur elles pour assurer correctement la validation des identités, protéger les clés de signature, respecter les politiques et fonctionner de manière fiable. Avant que l’autorité de certification de Cloudflare puisse obtenir la confiance des navigateurs pour l’émission de certificats MTC, nous devrons déposer notre candidature au programme de programme de clés racine à l’épreuve de l’informatique quantique (Quantum Resistant Root Store) de Chrome et nous soumettre à un processus d’évaluation rigoureux. Nous accueillons cet examen avec plaisir et nous entendons nous montrer à la hauteur de toutes les autres autorités de certification qui assument la responsabilité de contribuer à la sécurité d’Internet. Nous espérons que d’autres autorités de certification émergeront pour soutenir l’adoption des certificats MTC, et nous sommes impatients de collaborer avec tout navigateur souhaitant déployer ces certificats.

]]>01M4CTB5VJSJ26SAXKSF4ZPTVVPrésentation de cf : la CLI agentique pour l’ensemble de l’API Cloudflarehttps://blog.cloudflare.com/fr-fr/cloudflare-cf-cli-launch/ Thu, 08 Oct 2026 03:57:39 GMTNous publions cf, notre nouvel outil en ligne de commande qui reflète l'intégralité de l'API Cloudflare et prend en charge la configuration programmatique en TypeScript. Nous rendons également Forge, notre générateur de SDK interne, disponible en open source.AgentsAPIcfDéveloppeursSemaine anniversaireAu cours de l’année écoulée, l’utilisation de Wrangler par les agents a explosé.

En mars 2026, les agents étaient à l’origine d’un quart de l’utilisation de Wrangler, contre des pourcentages à un chiffre l’année précédente. La semaine dernière, la part d’utilisation par les agents a atteint 48 %.

Les agents sont des utilisateurs plus prolifiques : ils utilisent presque deux fois plus de commandes distinctes par jour et sont presque quatre fois plus susceptibles d’utiliser six commandes ou plus.

Les agents adorent les interfaces de ligne de commande (CLI). Or, Wrangler ne propose des commandes que pour environ 280 opérations, là où Cloudflare en propose des milliers.

Plus tôt cette année, nous vous avons laissé entrevoir [comment nous comptions résoudre ce problème](https://blog.cloudflare.com/cf-cli-local-explorer), et aujourd’hui, nous donnons aux agents la capacité d’utiliser tous les produits Cloudflare en introduisant une nouvelle CLI : cf.

cf est une CLI conçue pour la nouvelle génération du développement logiciel :

  * Les agents peuvent trouver la commande exacte dont ils ont besoin pour accomplir n’importe quelle tâche grâce à des fonctionnalités de recherche et de guidage sur mesure.
  * Le format JSON est l’interface par défaut, formaté de manière lisible par les humains et condensé pour les agents, afin de maximiser les économies de contexte.
  * cloudflare.config.ts est le nouveau format de configuration pour l’ensemble de Cloudflare, en commençant par Workers ; il apporte la sécurité et la précision de TypeScript à votre protocole de serveur de langage (Language Server Protocol LSP) et à celui de votre agent.
  * Vite devient le serveur par défaut, offrant le meilleur serveur de développement local ainsi qu’une suite de plugins pour les développeurs et les créateurs de frameworks.



Installez la bêta ouverte dès aujourd’hui partout dans le monde et exécutez-la depuis n’importe où :

**Copy prompt**
    
    
    Please update your global agent instructions, so you use Cloudflare's new `cf` CLI.
    
    Add the Markdown below to the user-level instructions file that you load in every project – not this repository's AGENTS.md or CLAUDE.md. Use the file for the agent you are: Claude Code `~/.claude/CLAUDE.md`, Codex `~/.codex/AGENTS.md`, OpenCode `~/.config/opencode/AGENTS.md`, Pi `~/.pi/agent/AGENTS.md`. For any other agent, use its equivalent global rules file; if your global rules can only be set in a settings screen, tell me what to paste there instead. Create the file if it doesn't exist. Keep everything already in it, but replace any existing instruction about Wrangler or the Cloudflare CLI instead of adding a conflicting one. If the same guidance is already there, leave the file as it is. When you're done, tell me the path of the file you changed.
    
    ```markdown
    ## Cloudflare CLI - cf - v20260928
    
    `cf` is Cloudflare's current CLI and covers the whole Cloudflare platform. Prefer it over Wrangler: create projects with `cf init`, develop with `cf dev`, deploy with `cf deploy`, and manage account resources with `cf <product> …` (for example `cf d1 list`).
    
    Wrangler is only for projects that already use it – a `wrangler.jsonc`, `wrangler.json` or `wrangler.toml` file – or when the user asks for it. Keep using Wrangler in those projects unless asked to migrate, and use `cf migrate` in this case.
    
    `cf` commands differ from Wrangler's; check `cf --help` or `cf cli search <what you want to do>` instead of guessing. If a `cf` command fails in a project that doesn't use Wrangler, don't fall back to Wrangler (including `npx wrangler`) without offering to report it.

## **cf donne à votre agent accès à l’ensemble de l’API Cloudflare**

Et si votre agent pouvait accomplir tout ce dont Cloudflare est capable ? C’est la question qui a éveillé notre intérêt en début d’année : si les agents devenaient toujours plus puissants, ce qu’ils pouvaient accomplir avec la CLI de Cloudflare restait limité.

Wrangler a été développé de manière artisanale, chaque équipe produit contribuant et adoptant sa propre approche de l’expérience développeur de commandes. Harmoniser les pratiques des différentes équipes s’est avéré pratiquement impossible, même sur nos quelque 280 parcours de commandes. Nous nous trouvions face à une terminologie incohérente entre `d1 info`, `hyperdrive get` et `workflows describe`, chaque équipe ayant développé ses propres pratiques à différents moments. Certaines équipes ont développé des expériences entièrement personnalisées, représentant des milliers de lignes de code, qui n’ont été que très rarement utilisées, tandis que d’autres ont adopté des approches différentes pour résoudre les mêmes problèmes.

Nous voulions à la fois standardiser l’existant et procéder à une expansion massive, le tout en une seule fois. [Forge](https://blog.cloudflare.com/forge-open-source-generation-pipeline), le nouveau pipeline unifié de génération d’API de Cloudflare, nous a permis d’y parvenir, en s’appuyant sur le principe de générer nos commandes CLI directement à partir du schéma d’API qui alimente notre documentation d’API et notre génération de SDK. Tout ce que nous proposons dispose d’un schéma OpenAPI ; il suffit d’y ajouter quelques annotations supplémentaires pour pouvoir l’utiliser comme source pour générer une CLI avec Forge.

Cela nous permet de développer `cf`, en évoluant des quelque 280 fonctions accumulées par Wrangler pour englober l’intégralité de la surface de l’API Cloudflare, soit plus de 3 000 opérations.

Désormais, il suffit de fournir `cf` à votre agent et de lui demander de configurer une instance Workers, de la déployer, de la surveiller, de la protéger avec Cloudflare Access, d’acheter un nom de domaine, puis de le sécuriser avec le pare-feu WAF de Cloudflare – et tout cela, depuis un outil unique.

## **Développer une solution pour un agent qui n’a jamais utilisé cf**

cf a été développé pour accompagner la trajectoire du génie logiciel, à une époque où le développement agentique transforme radicalement l’approche du développement et du déploiement d’applications. Cette année, nous avons priorisé la fourniture d’outils destinés à accompagner cette évolution, une démarche qui a abouti au lancement de cf. cf a été fondamentalement développé en tenant compte des agents, et inclut des outils novateurs conçus pour la découverte de commandes par les agents, qui deviendra, selon nous, la norme dans de nombreuses CLI dans un avenir proche.

Wrangler bénéficiait d’un avantage : des années de documentation, d’articles de blog et de guides tiers ont été assimilées pendant le processus d’entraînement des LLM. Il présentait toutefois le désavantage inverse : modifier le fonctionnement de Wrangler va désormais à l’encontre des comportements appris, et un changement considérable serait inévitable au vu de l’ampleur des améliorations que nous souhaitons apporter.

Introduire une nouvelle CLI que les agents n’ont jamais vu semble être une rupture majeure, mais c’est en réalité la démarche la plus saine que nous puissions adopter. Grâce aux décisions architecturales que nous avons prises, aux injections de contexte que nous pouvons effectuer et aux fichiers AGENTS.md que nous pouvons ajouter, opérer un tel changement est en réalité moins déroutant pour un agent que de lui demander de contextualiser les différences majeures entre deux versions d’un outil qu’il connaît déjà. Nous lançons cette version en y intégrant quelques-unes de ces fonctionnalités pensées pour les agents, et d’autres suivront prochainement.

## **Les agents doivent filtrer du JSON, pas analyser des tableaux**

Lorsque les agents utilisent Wrangler, ils ajoutent `--json` à chaque commande qu’ils exécutent, puis filtrent généralement le résultat avec `jq` afin d’en extraire un sous-ensemble de champs. Or, seules certaines commandes de Wrangler prenaient en charge l’indicateur `--json` ; beaucoup renvoyaient des tableaux en caractères Unicode, conçus pour des utilisateurs humains consultant l’affichage dans leur terminal. Les agents peuvent les interpréter, mais cela leur demande plus de temps et plus de tokens qu’un filtre `jq`.

Dans cf, nous adoptons la démarche inverse : les agents ont uniquement besoin de JSON, et si les agents sont appelés à devenir les utilisateurs principaux de cet outil, JSON doit logiquement devenir le choix par défaut. Pour la grande majorité des commandes, qui ne seront que rarement utilisées par des opérateurs humains, c’est de toute évidence la bonne décision.

En tant qu’utilisateur humain de cette CLI, vous êtes, en réalité, un intermédiaire en retrait d’un niveau de son utilisation directe. Il est préférable que les agents puissent facilement filtrer leurs résultats, puis vous présenter cette liste filtrée dans le format de votre choix que de vous fournir des tableaux que vous ne lirez probablement jamais directement.

Mais qu’en est-il si vous cherchez à accomplir une action qui nécessite une réelle saisie personnelle, par exemple, rechercher un nom de domaine à acheter ?

Pour les commandes auxquelles votre agent peut accéder en enchaînant des paramètres nommés dans une longue et fastidieuse séquence, vous pouvez simplement remplir un formulaire. cf décompose les exigences de l’API en une série de saisies validées, transformant l’achat d’un nom de domaine (même avec des exigences complexes) en une démarche simple à réaliser.

Ou, si vous y tenez vraiment, demandez simplement à votre agent de s’en occuper.

## **Votre agent peut trouver la bonne commande par lui-même**

Avec 3 000 itinéraires possibles dans une CLI, comment votre agent peut-il identifier rapidement l’opération dont il a besoin sans saturer vos informations de contexte ? C’est la raison pour laquelle nous avons également ajouté `cf cli search`.

Cette commande permet à votre agent de formuler en langage naturel la tâche qu’il souhaite accomplir, et un index de recherche léger lui renvoie une liste de commandes appropriées, établie en fonction de leur description d’API et de leurs paramètres. Nous informons automatiquement votre agent de l’existence de cette commande lorsqu’il exécute `--help` pour la première fois.

## **Une configuration avec vérification de type pour votre agent**

Notre nouveau format de configuration repose sur TypeScript ; facile à analyser pour les humains et les agents, il vous permet d’écrire votre configuration de façon programmatique.

Une configuration typée s’avère extrêmement utile pour les agents. Nous avons constaté que, même sans connaissance préalable du format de configuration programmatique, les agents parviennent facilement à identifier et modifier la configuration à la demande, même pour des éléments comme `env`, dont le fonctionnement a considérablement changé par rapport à la fonctionnalité du même nom dans Wrangler. Tous les agents utilisant des plugins LSP, comme Claude Code et Codex, tirent parti d’une meilleure capacité d’interprétation contextuelle du fichier de configuration, qui leur permet de formuler des suggestions beaucoup plus précises.

Comparez cela au format TOML, qui ne proposait pas de schéma accessible, ou à JSONC, dont le schéma associé était rarement utilisé par les agents.

Certains fichiers de configuration Wrangler internes à Cloudflare ont été condensés de 40 %, passant de plus de 5 000 lignes avec de nombreux environnements personnalisés par développeur à des fichiers « d’usine » qui génèrent plus efficacement la configuration de chaque développeur.

Ce résultat est obtenu en définissant programmatiquement chaque environnement à partir d’une même base universelle, au lieu de dupliquer des blocs `env` comme c’était l’usage dans Wrangler. Une instance Workers simple comportant plusieurs environnements bascule désormais simplement vers l’argument `mode` natif de Vite pour passer d’un ensemble de configuration à un autre.

Une configuration simple permettant d’appliquer cette approche se présente désormais comme ceci :

Vous pouvez migrer votre instance Cloudflare Workers vers ce nouveau format via la commande `cf migrate`.

Nous vous proposons également plusieurs fonctions d’assistance, grâce auxquelles le développement de votre instance Workers devient un jeu d’enfant.

`bindings` offre à votre agent un espace centralisé depuis lequel découvrir tout ce que propose la plateforme pour développeurs. Toutes les ressources, des variables d’environnement au stockage, aux bases de données et aux files d’attente, peuvent être automatiquement suggérées et expliquées par votre éditeur.

De la même manière, nous avons intégré une fonction d’aide pour les déclencheurs (`triggers`), qui constituent la nouvelle façon de définir les routes, les files d’attente, les plannings et les déclencheurs d’e-mails pour votre instance Workers. Plutôt que de travailler avec des déclencheurs disséminés dans votre fichier de configuration, vous pouvez désormais retrouver facilement, dans un seul bloc, les actions susceptibles de déclencher l’exécution de votre instance Workers.

`defineConfig.worker` n’est que le point de départ. Notre objectif, avec cloudflare.config.ts, est de proposer un outil central de gestion pour l’ensemble de l’écosystème Cloudflare. Chaque produit dont vous avez besoin (ainsi que son API, qui sera accessible à votre agent via cf) pourra être exprimé à travers une configuration fortement typée. Bientôt, vous pourrez configurer des politiques complètes, paramétrer des zones, gérer le DNS et bien davantage via ce fichier de configuration.

## **Une expérience de développement inégalée**

Quand Wrangler a commencé à développer des instances Workers JavaScript, [Vite](https://vite.dev/) n’existait pas encore. À la place, nous utilisions esbuild dans Wrangler pour bundler vos instances Workers. Le serveur de développement que proposait Wrangler sur le port : 8787 était un outil créé par notre équipe spécialiste de Wrangler, et la moindre modification impliquait de s’immerger longuement dans les arcanes d’outils locaux spécifiques à Cloudflare, comme Miniflare.

Vite offre une amélioration considérable à cet égard : il propose un vaste écosystème de plugins, l’un des meilleurs serveurs de développement du marché avec remplacement des modules à chaud (Hot Module Replacement, HMR) et des builds qui utilisent Rolldown, une bibliothèque écrite en langage Rust, pour l’élimination du code mort (ou «  _tree-shaking_ »). Tout ce que vous pouvez accomplir avec Vite est réalisable avec le plugin Vite pour Cloudflare.

Le plugin Vite pour Cloudflare constitue la méthode recommandée pour développer des instances Workers, quelle que soit la nature de votre projet : qu’il s’agisse d’un projet orienté frontend ou d’une API backend. Associé à notre plugin Vitest, il offre un environnement de développement et de test cohérent, qui correspond au runtime Workers et vous donne un accès direct aux bindings et aux API de la plateforme.

cf est développé dans Vite, par défaut. La plupart de vos instances Workers pourront être migrées avec facilité, grâce aux agents. Pour d’autres, la migration pourra demander plus de temps ; c’est pourquoi cf continuera de déléguer à Wrangler la gestion du développement et du déploiement des instances Workers JavaScript qui doivent continuer à utiliser esbuild, ainsi que des instances Workers Rust et Python.

## **Migration depuis Wrangler**

Migrer une instance Workers depuis Wrangler est aussi simple qu’exécuter la commande cf migrate

Les instances Workers qui développent déjà des applications avec Vite seront automatiquement converties vers cloudflare.config.ts. Si votre instance Workers s’appuie sur Wrangler pour esbuild, cf continuera de déléguer les builds à Wrangler.

À la fin de la bêta ouverte, nous publierons une dernière version majeure de Wrangler qui vous guidera, vous et votre agent, vers l’utilisation de cf. Nous maintiendrons le support de Wrangler pendant 18 mois après la fin de la bêta, afin de vous laisser le temps d’effectuer la migration.

Vous pouvez également configurer automatiquement de nouveaux projets pour Cloudflare en exécutant `cf init/deploy`, qui installera le plugin Vite pour Cloudflare et créera votre fichier de configuration

Les sites statiques ne nécessitent toujours aucun fichier de configuration pour démarrer, et leur déploiement est aussi simple que le fait d’exécuter `cf deploy` dans votre projet.

Pour démarrer un nouveau projet « Hello World » avec cf, utilisez la commande `cf init`.

_cf est un projet open source et les problèmes peuvent être[ signalés sur notre dépôt GitHub](https://github.com/cloudflare/cf)_.

]]>01M4CSZT5KJMCF20H8GJEKB70QDécouvrez The Cold Start : présentez votre start-up en direct lors de l’événement Cloudflare Connecthttps://blog.cloudflare.com/fr-fr/introducing-the-cold-start/ Thu, 08 Oct 2026 03:47:18 GMTCloudflare lance The Cold Start, une compétition de start-ups offrant à cinq entreprises en phase de démarrage cinq minutes sur scène à Cloudflare Connect. Le grand gagnant remporte $500 000 en crédits, un panneau publicitaire à San Francisco et une invitation à notre dîner VIP des intervenants.Cloudflare for StartupsDéveloppeursSemaine anniversaireIl y a seize ans, Cloudflare était l’une de plus de 1 000 jeunes entreprises qui espéraient monter sur la scène de l’événement TechCrunch Disrupt.

À première vue, nous n’étions pas un choix évident. Cloudflare faisait de l’infrastructure : nous rendions les sites web plus rapides et les protégions contre les attaques ; une offre encore mal comprise par le grand public, à l’époque. L’infrastructure est souvent invisible, jusqu’au moment précis où elle devient cruciale.

Le 27 septembre 2010, pourtant, Matthew Prince et Michelle Zatlyn sont montés sur la scène du Startup Battlefield pour présenter Cloudflare au public. Pendant la présentation, des personnes ont commencé à s’inscrire, puis d’autres se sont jointes à elles, encore plus nombreuses. Lorsque le jury a fini de poser ses questions, des centaines de sites web avaient rejoint Cloudflare, mettant immédiatement nos cinq premiers datacenters à rude épreuve. Au cours des sept jours qui ont suivi, le trafic traversant notre réseau a été multiplié par près de dix, et Cloudflare a bondi du millième rang mondial pour rejoindre les 50 sites plus grands sites.

Cloudflare n’a pas remporté le trophée principal ce jour-là. Lors de la cérémonie de remise des prix, Mike Arrington, fondateur de TechCrunch, a qualifié ce que nous faisions comme une activité semblable à « la réparation de pots d’échappement pour Internet » – et pour être honnête, il n’avait pas tout à fait tort. Mais il nous a tout de même décerné le titre de « Most Innovative Company » (l’entreprise la plus innovante). Comme Matthew Prince l’a écrit plus tard : «  _Vous ne remporterez peut-être pas le trophée, mais vous recevrez quelque chose de bien plus important._ »

Il y a des moments dans la vie d’une entreprise où quelqu’un vous offre une scène, un micro et un peu de temps pour expliquer le concept qui vous obsède, auquel vous consacrez tout votre temps depuis des mois, voire des années. La plupart du temps, il ne se passe rien de magique. Mais parfois, les bonnes personnes vous écoutent au bon moment, et soudain, une idée qui n’existait fondamentalement que dans l’esprit d’une poignée d’individus commence à se répandre dans le monde.

Ce mois d’octobre, alors que Cloudflare fête ses 16 ans, nous voulons offrir, à notre tour, une scène à cinq jeunes entreprises.

## **Découvrez The Cold Start**

[ The Cold Start](https://www.cloudflare.com/connect/cold-start/?cf_page=introducing-the-cold-start%2F) est un concours de start-ups en direct qui se déroulera le mois prochain lors de l’événement Cloudflare Connect, à San Francisco. Nous sélectionnerons cinq jeunes entreprises et leur accorderons chacune cinq minutes sur scène pour expliquer ce qu’elles développent, pourquoi cela doit exister, et pourquoi elles sont les mieux placées pour le créer.

Nous nous intéressons moins aux présentations parfaitement léchées qu’à l’explication claire d’idées intéressantes. Vous n’avez pas besoin de trente diapositives, d’un calcul de marché adressable étrangement précis, ni d’un récit bien rodé sur la façon dont votre enfance vous a préparé à révolutionner la gestion des comptes clients. Ce que nous voulons, c’est comprendre votre vision : quelle évolution dans le monde l’a rendue possible, ce que vous voyez que d’autres ont manqué et pourquoi vous ne pouvez pas vous arrêter d’y penser.

Les cinq finalistes plaideront leur cause devant le public de la conférence Cloudflare Connect et trois personnes qui ont consacré une bonne partie de leur vie à réfléchir aux entreprises, à l’infrastructure et à Internet :

  * Matthew Prince, cofondateur, et CEO de Cloudflare
  * Michelle Zatlyn, cofondatrice et présidente de Cloudflare
  * Dane Knecht, CTO de Cloudflare



Le jury sélectionnera une jeune entreprise qui remportera 500 000 $ en crédits Cloudflare, sera affichée sur un panneau publicitaire à San Francisco et recevra une invitation pour assister à notre dîner VIP des intervenants ce soir-là.

Cinq entreprises, cinq minutes chacune, et une salle remplie de personnes attentives.

### **Que recherchons-nous ?**

The Cold Start est ouvert aux jeunes entreprises ambitieuses en phase de démarrage, basées aux États-Unis et au Canada, qui ont levé moins de dix millions de dollars. Au-delà de ces critères, nous gardons intentionnellement une définition large, car les entreprises les plus intéressantes rentrent rarement dans les cases.

Nous voulons voir des idées qui semblent évidentes lorsque quelqu’un les concrétise enfin, mais aussi des idées qui paraissent, à première vue, légèrement déraisonnables. Nous recherchons de l’infrastructure qui paraît ennuyeuse jusqu’à ce que l’on se rende compte que tout le monde va en avoir besoin ; des produits qui n’auraient pas pu exister il y a encore quelques années ; de nouvelles interfaces étranges ; de nouvelles façons de développer des logiciels ; des projets ciblant d’immenses marchés existants tout comme des projets ciblant des marchés que personne n’a encore pris la peine de nommer.

Surtout, nous voulons rencontrer des personnes qui ont remarqué quelque chose dans le monde et ont décidé de faire bouger les lignes.

Dans le cadre de la candidature, nous vous demanderons de nous dire qui vous êtes, de nous proposer votre présentation en une ligne, d’expliquer ce que vous créez et pourquoi, de nous parler de votre niveau de financement et de vos revenus, de nous montrer comment Cloudflare s’intègre dans votre pile technologique et de nous orienter vers tout ce qui peut nous aider à comprendre qui vous êtes et ce que vous faites.

L’objectif est simple : faites-nous comprendre pourquoi ce que vous êtes en train de créer devrait exister.

**[Demandez](https://www.cloudflare.com/connect/cold-start/?cf_page=introducing-the-cold-start%2F)[ The Cold Start](https://www.cloudflare.com/connect/cold-start/?cf_page=introducing-the-cold-start%2F).**

**_Les candidatures sont ouvertes dès maintenant et seront clôturées le vendredi 2 octobre 2026._**

## **Cinq minutes à San Francisco**

L’événement The Cold Start se déroulera le lundi 19 octobre, de 16h00 à 17h00 HNP dans le centre Moscone West à San Francisco, dans le cadre de la conférence [Cloudflare Connect](https://www.cloudflare.com/connect/?cf_page=introducing-the-cold-start%2F). Cloudflare prendra en charge les billets d’avion des cinq finalistes pour se rendre à San Francisco pour le concours.

Connect rassemble les personnes qui construisent et imaginent l’avenir d’Internet. L’affiche de cette année réunit le Dr Fei-Fei Li, pionnière de l’IA ; Bill Gross, fondateur d’Idealab ; Adam Grant, psychologue du travail et des organisations et auteur ; Mark Papermaster, CTO d’AMD ; Evan You, créateur de Vue.js et de Vite ; Fabian Hedin, cofondateur et CTO de Lovable ; et Peter Steinberger, membre de l’équipe technique d’OpenAI et créateur d’OpenClaw.

Nous réservons une partie de cette scène à cinq jeunes entreprises. Chacune disposera de 5 minutes pour présenter son projet, suivies de 3 à 5 minutes de questions du jury.

Il y a, dans cette symétrie, quelque chose qui nous plaît. Il y a seize ans, Cloudflare avait besoin que quelqu’un donne sa chance à une entreprise d’infrastructure avec un concept difficile à expliquer et nous accorde quelques minutes devant le bon public. Aujourd’hui, nous avons la chance d’avoir notre propre scène, et nous voulons transmettre cette même opportunité à des entreprises qui se lancent tout juste.

## **Commencez modestement. Construisez quelque chose d’immense.**

Il y a une raison pratique pour laquelle Cloudflare consacre autant de temps à travailler avec les jeunes entreprises : les très petits groupes de personnes possèdent une capacité surprenante à entreprendre de très grands projets.

Le problème est que les logiciels ambitieux dépendent toujours davantage d’une infrastructure que, dans un passé encore récent, seules les plus grandes entreprises technologiques au monde avaient les moyens de construire pour leur propre usage. Le calcul distribué dans le monde entier, le stockage, le réseau, la sécurité, les systèmes en temps réel, l’inférence IA et la capacité à survivre au succès soudain et inattendu de leur projet ne devraient pas exiger qu’une entreprise devienne colossale, dans un premier temps.

Nous pensons que vous devriez pouvoir accéder à ces capacités dès le premier jour.

C’est en quelque sorte l’esprit du programme [Cloudflare for Startups](https://www.cloudflare.com/startups/?cf_page=introducing-the-cold-start%2F), grâce auquel les jeunes entreprises éligibles peuvent recevoir jusqu’à $350 000 en crédits Cloudflare pour un an. C’est aussi l’une des raisons pour lesquelles nous continuons à enrichir la plateforme pour développeurs de Cloudflare : une toute petite équipe devrait pouvoir créer quelque chose le mardi et, si Internet décide de s’y intéresser le mercredi, passer son jeudi à se concentrer sur son produit, plutôt que s’improviser en urgence experts en infrastructure mondiale.

Cloudflare a débuté avec sa propre idée légèrement déraisonnable : rendre les performances, la sécurité et le calcul distribué dans le monde entier réservés aux plus grandes entreprises sur Internet accessibles à tous dès le premier jour. En 2010, nous avons eu l’occasion de monter sur scène pour expliquer pourquoi cela importe.

Seize ans plus tard, nous disposons d’un réseau beaucoup plus vaste, d’une équipe un peu plus grande et de disjoncteurs considérablement plus efficaces.

Et maintenant, nous voulons entendre ce que vous allez créer.

[Demandez The Cold Start.](https://www.cloudflare.com/connect/cold-start/?cf_page=introducing-the-cold-start%2F)

]]>01M4CSHS7YHM7TSWK00326P45CDécouvrez Forge : le pipeline open source dédié à la génération de SDK, de CLI, de documentation et bien d’autres choseshttps://blog.cloudflare.com/fr-fr/forge-open-source-generation-pipeline/ Thu, 08 Oct 2026 03:39:38 GMTForge est un pipeline de génération open source, modulaire et extensible, qui s'exécute dans CI pour générer des SDKs, des CLIs et de la documentation directement à partir des définitions d'API. En déplaçant la génération en amont dans les dépôts individuels des équipes, Forge maintient les outils de développement en permanence synchronisés.AgentsAPICLIDéveloppeursSDKSemaine anniversaireAujourd’hui, nous présentons [Forge](https://github.com/cloudflare/forge), une nouvelle approche pour générer des SDK, des CLI, de la documentation et des bibliothèques. Forge est un pipeline de génération open source, modulaire et extensible, que chacun peut déployer et utiliser gratuitement.

Forge n’en est qu’à ses débuts, mais génère déjà les ressources nécessaires à la [CLI cf](https://blog.cloudflare.com/cloudflare-cf-cli-launch/) et, au cours des mois à venir, il alimentera la documentation de l’API Cloudflare, les SDK et bien d’autres choses.

Nous avons créé Forge parce que nous en avions nous-mêmes besoin pour traiter les agents comme nos clients. Maintenant, nous le rendons open source parce que nous pensons que chacun devrait pouvoir générer l’ensemble des interfaces dont les agents ont besoin. Autrefois, seuls les produits destinés aux développeurs nécessitaient des CLI, des SDK d’API, des serveurs MCP, tous accompagnés d’une documentation d’excellente qualité. Aujourd’hui, ces ressources constituent les prérequis fondamentaux pour chaque produit.

## **Notre API est devenue trop vaste pour nos générateurs**

L’API de Cloudflare compte plus de 3 500 opérations, et les centaines de services qui alimentent ces API sont écrits dans de nombreux langages, notamment Rust, Go, TypeScript et Python. Lorsque nous nous sommes lancés dans le développement d’une CLI pour l’ensemble de l’API Cloudflare (y compris nos SDK et notre documentation d’API), nous avons eu besoin d’un pipeline de génération de code capable d’absorber cette échelle. Ce pipeline doit être suffisamment flexible pour fonctionner avec les différents langages et les méthodes de travail de chacune de nos équipes d’ingénierie.

Nous avions besoin d’un moyen de réduire la surcharge de travail qu’entraînait la coordination des différentes équipes. Lorsqu’une équipe produit de Cloudflare apporte une modification à une API, elle doit pouvoir utiliser une version de prévisualisation de la CLI, du SDK et du site de documentation qui seront générés à l’échelle de Cloudflare avant de fusionner cette modification et de la déployer auprès des clients. Nous avions besoin d’un moyen de nous assurer qu’une équipe ne compromettrait pas involontairement le pipeline de génération, et nous avions besoin d’un système extensible, capable de générer bien plus qu’un SDK, de Cap’n Web à MCP et au-delà.

Nous avons essayé plusieurs produits hébergés qui tentent de résoudre ce problème, et nous en avons même essayé certains en production. Aucun d’eux n’a permis de résoudre ce problème, et certains se sont purement et simplement bloqués. Une équipe fusionnait une modification qui entraînait une interruption involontaire du pipeline de génération, une autre équipe s’en apercevait au moment du déploiement, et nous passions trop de temps à remonter le courant en jonglant avec des outils hébergés que nous ne contrôlions pas, à coordonner les modifications entre équipes et fournisseurs.

C’est ainsi que nous avons commencé à développer Forge.

Forge vise à résoudre tous ces problèmes : il s’exécute dans le pipeline d’intégration continue, sur les dépôts d’API de chaque équipe, tout comme notre relecteur de code IA et nos pipelines de tests. Il analyse statistiquement (_lint_) chaque modification, puis génère des versions de prévisualisation de la CLI, de la documentation et des SDK en mettant uniquement en évidence vos modifications, que vous pouvez installer afin de les tester. Le principe est identique à [Workers Previews](https://blog.cloudflare.com/worker-previews/) : une version de prévisualisation complète pour chaque modification, mais appliquée à la génération de SDK à grande échelle, notamment lorsque la surface d’API est répartie sur des centaines de services et de dépôts. C’est ce que promet Forge.

## **Les transformateurs de Forge peuvent tout générer, y compris Cap’n Web**

Cloudflare a plus de raisons que la plupart des entreprises de vouloir un générateur capable d’aller bien au-delà des cibles de langages habituelles. [Cap’n Web](https://capnweb.com/) est le système de RPC de Cloudflare qui permet à TypeScript d’appeler une API distante comme s’il s’agissait d’une méthode locale.

Forge permet de prendre une spécification OpenAPI et de générer directement du Cap’n Web. Cette capacité ouvre la porte à la génération de [bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/) entre Workers et d’autres API. Après tout, dans le runtime Workers, les bindings sont implémentés sous forme d’instances Workers qui exposent des méthodes RPC.

Et ce n’est pas spécifique à Cap’n Web : d’autres outils populaires sur lesquels vous vous appuyez peut-être déjà ont le même besoin. Si vous utilisez TanStack Query, vous souhaiteriez idéalement pouvoir générer des bindings [TanStack Query](https://tanstack.com/query/) pour votre application, créés directement depuis votre API ; toujours à jour, et toujours validés par rapport à votre API réelle. Cela s’applique également à la génération de schémas Zod ou Valibot, de serveurs MCP ou de tout autre élément facilitant la consommation de votre API.

Tout cela est possible grâce à la flexibilité des générateurs de code de Forge, qui sont conçus pour faire circuler l’information d’une ressource à une autre.

## **Les transformateurs de Forge peuvent être chaînés : générer des ressources à partir d’autres ressources**

Nous avons conçu Forge pour être modulaire et extensible et prendre en charge de nombreux types d’entrées et de sorties. Forge fournit des générateurs de CLI, de SDK et de documentation, mais rien ne vous empêche d’ajouter un transformateur générant un package spécifique à une bibliothèque, voire un tableau de bord ou une application complète. Aujourd’hui, Forge prend en charge OpenAPI comme format d’entrée, mais nous l’avons pensé pour intégrer, à l’avenir, [AsyncAPI](http://asyncapi.com), GraphQL, Cap’n Proto, Protobuf ou d’autres formats d’entrée.

Il s’agit de bien plus que d’une simple compatibilité : cela vous permet de chaîner des cibles en utilisant le résultat d’une cible pour en produire d’autres. C’est une pratique courante dans d’autres générateurs, où les cibles CLI et Terraform sont produites à partir du SDK Go. Mais ce qui manque, et ce que Forge apporte, c’est un moyen pour l’utilisateur de contrôler lui-même ce système de chaînage.

Nous avions nous-mêmes besoin d’une solution à ce problème, car notre propre CLI cf est écrite en TypeScript, un langage dont d’autres générateurs de SDK ne permettent généralement pas le chaînage pour les CLI. Cependant, notre propre situation nous a fait prendre conscience d’un problème plus profond : pourquoi un outil de génération de SDK prendrait-il cette décision à votre place ? Peut-être utilisez-vous essentiellement Python et souhaitez-vous que votre CLI soit développée dans ce langage.

Si vous vous dites « Et alors, qu’importe que ce soit en Python ou pas ? Le code est généré automatiquement, » c’est parce que les CLI sont différentes. Les CLI introduisent souvent des comportements locaux qui n’auraient aucun sens dans un SDK ; des comportements que vous écrivez à la main, car ils ne reposent intrinsèquement pas sur un appel d’API. Par exemple, la CLI cf propose des commandes comme cf dev et cf build, qui s’ajoutent au reste des résultats générés. Ces commandes doivent appeler des API TypeScript fournis par d’autres packages, comme Vite.

Maintenant, ajoutons la documentation à l’équation. Si vous générez votre CLI et votre documentation exclusivement à partir de votre spécification OpenAPI, comment réintégrez-vous ces commandes écrites à la main dans votre documentation, pour qu’elles soient documentées aux côtés des autres ressources ?

Nous n’avons trouvé aucun outil existant capable de faire cela aujourd’hui, et pourtant, c’est exactement ce dont nous avons besoin pour cf. C’est pourquoi nous l’intégrons directement dans Forge.

## **Modifier votre API sans laisser vos utilisateurs sur le carreau**

Forge nous prépare également à une meilleure gestion des versions d’API. L’API v4 de Cloudflare incarne l’unique version majeure de notre API depuis dix ans. Depuis lors, il peut sembler que nous n’avons publié aucune nouvelle version majeure ; toutefois, au sens strict des définitions SemVer (versionnage sémantique), nous avons effectué un nombre considérable de modifications, qui mériteraient une nouvelle version majeure. Dans le même temps, plusieurs opérations à travers notre API comportent des indicateurs internes « v2 » ou des identifiants « beta » qui ont depuis longtemps dépassé cette étape du cycle de vie du produit.

Après tant d’années passées sur notre API v4, nous sommes parfaitement conscients qu’une nouvelle version majeure v5 laisserait beaucoup de nos clients sur le carreau. C’est pourquoi, grâce aux artefacts publiés par Forge entre temps, nous travaillons sur une approche de la gestion des versions de l’API qui nous permettra de publier de nouvelles versions majeures d’API sans briser la compatibilité avec les anciens clients ou SDK.

Nous vous communiquerons très prochainement de nouvelles informations sur nos SDK, notamment TypeScript, Rust, Python, Go, PHP et Terraform – et plus particulièrement sur Terraform. Nous savons que la mise à niveau d’un fournisseur Terraform exige une rigueur particulière, et nous allons accorder un soin spécifique à cette transition.

## **Les outils critiques devraient être accessibles à tous**

Nous sommes convaincus que le développement d’outils pour les API constitue un pilier essentiel d’Internet, et vous devriez pouvoir accomplir cette démarche sans avoir besoin d’un produit SaaS. Vous devriez être propriétaire de vos SDK, vos CLI et votre documentation. Et si vous les générez, vous devriez pouvoir en faire ce que vous voulez, où vous le voulez, gratuitement.

C’est pourquoi nous proposons [Forge en open source](https://github.com/cloudflare/forge) sous la licence permissive Apache 2.0. Nous voulons que la communauté nous rejoigne lors de ce voyage et contribue à l’aventure.

Toutefois, peut-être préférez-vous tout garder pour vous. Pas de problème ! Vous pouvez exécuter Forge par vous-même à n’importe quelle fin, avec vos propres modifications, gratuitement et en toute confidentialité.

_Remerciements : ce projet a également pu voir le jour grâce au travail de conception et de mise en œuvre de Dan Carter, Steven Chong, Krishna Paritala et Shelley Jones._

]]>01M4CRWMG3N5ZSMHE8PRQM015GCréer une autorité de certification pour l’ensemble d’Internethttps://blog.cloudflare.com/fr-fr/cloudflare-certificate-authority/ Thu, 08 Oct 2026 02:33:34 GMTDouze ans après le lancement de Universal SSL, Cloudflare pose sa candidature pour devenir une autorité de certification. En nous appuyant sur une racine de confiance établie, une architecture orientée ACME et les certificats Merkle Tree Certificate (MTC), nous construisons une autorité de certification post-quantique pour le web ouvert.CryptographieLe post-quantiqueSécuritéSemaine anniversaireTLSIl y a douze ans, lors de la Semaine Anniversaire 2014, [nous avons activé Universal SSL](https://blog.cloudflare.com/introducing-universal-ssl/) et avons doublé, presque du jour au lendemain, le nombre de sites chiffrés sur le web, en offrant le protocole TLS gratuitement à chaque site protégé par Cloudflare – y compris ceux qui ne nous avaient jamais versé un centime. Le chiffrement a cessé d’être une entreprise coûteuse et fastidieuse et est devenu la norme par défaut.

À l’occasion de cette édition annuelle de la Semaine Anniversaire, nous franchissons une nouvelle étape sur ce chemin. Depuis plus d’une décennie, nous sommes l’un des plus grands consommateurs de certificats publiquement reconnus sur Internet, sans en avoir jamais émis un seul nous-mêmes. Maintenant, tout cela va changer : Cloudflare annonce son intention de devenir une autorité de certification (CA, Certification Authority) publique.

Nous annonçons aujourd’hui les premiers jalons concrets de cette démarche : nous avons déposé une demande d’intégration dans les programmes de clés racine de Chrome, d’Apple, de Microsoft et de Mozilla, et nous avons signé un accord définitif en vue d’acquérir une racine établie et largement reconnue auprès de GlobalSign. Nous pourrons ainsi proposer des certificats compatibles avec le plus grand nombre d’équipements dès le premier jour de leur émission. Nous annonçons également notre intention de devenir l’une des premières autorités de certification à délivrer des certificats post-quantiques, en ciblant le [programme de clés racine à l’épreuve de l’informatique quantique](https://blog.google/security/cultivating-a-robust-and-efficient-quantum-safe-https/) récemment annoncé par Chrome.

Nous n’émettons pas encore de certificats, et il faudra encore un peu de temps avant que ce soit le cas. Ce que nous faisons, c’est nous engager publiquement dans cette démarche, partager chaque étape au fur et à mesure que nous la franchissons et détailler exactement ce que nous créons, tout en collaborant avec les programmes de clés racine et les autres membres de la communauté WebPKI pour y parvenir.

## **Deux voies vers la confiance**

Une toute nouvelle racine n’est pas d’une grande utilité avant plusieurs années. Même après avoir été acceptée par un programme de clé racine, cette racine doit se propager aux différents systèmes d’exploitation, navigateurs et appareils du monde entier, sans jamais atteindre le vaste ensemble d’appareils qui ont cessé de recevoir des mises à jour ou n’en ont tout simplement jamais reçu. C’est précisément dans cette longue traîne d’anciens clients que naît une grande partie du trafic Internet mondial et que réside un nombre tout aussi important de dysfonctionnements évitables. Nous sommes convaincus que tous les clients méritent le plus haut niveau de sécurité possible, quels que soient leur fabricant, leur système d’exploitation ou le temps écoulé depuis leur dernière mise à jour.

L’acquisition d’une racine existante bénéficiant d’une couverture importante dans les magasins de certificats de confiance pour un ensemble diversifié de clients résout ce problème dès le premier jour. La racine GlobalSign existante est reconnue par les navigateurs, les systèmes d’exploitation et les appareils depuis 2012, et elle atteint les anciens clients qu’une nouvelle racine ne concernera jamais. La nouvelle racine que nous soumettrons aux programmes de clés racine est conçue pour l’avenir de l’écosystème, notamment pour les programmes qui commencent à plafonner l’ancienneté maximale d’une racine de confiance. La racine établie nous garantit une certaine portée auprès des équipements utilisés autrefois. Les nouvelles racines nous confèrent une légitimité dans le cadre des politiques du futur. Nous voulons cumuler les deux pour garantir que les certificats émis par notre autorité de certification offrent la plus large compatibilité possible avec les équipements de nos clients.

## **Une nouvelle source de certificats gratuits**

Le modèle de certificats gratuits et automatisés porte aujourd’hui la majeure partie du web chiffré, et une grande part de celui-ci repose sur un opérateur remarquable. Let’s Encrypt émet quelque dix millions de certificats chaque jour, sert plus de 500 millions de sites et a dépassé les quatre milliards de certificats actifs en 2025. C’est l’une des meilleures choses qui soient arrivées à Internet au cours des vingt dernières années, et c’est en tant que l’un de ses plus grands utilisateurs que nous l’affirmons.

Ce succès s’accompagne d’un risque systémique : si l’autorité de certification gratuite dominante traversait une semaine critique, une grande partie du web ne disposerait d’aucune alternative gratuite et automatisée comparable, prête à absorber la charge. Au niveau de nos paquets de certificats, nous avons passé des années à créer précisément ce type de redondance pour nos propres clients. Chaque certificat Universal SSL de Cloudflare comporte déjà avec un certificat de secours, configuré avec une clé distincte et émis par une autorité différente, prêt à être déployé automatiquement si le certificat principal venait à être révoqué ou compromis. Une autorité de certification publique repose sur cette même logique, toutefois à l’échelle de l’ensemble d’Internet.

Pour en faciliter l’adoption, nous adopterons une approche orientée [ACME](https://www.globalsign.com/en/acme-automated-certificate-management) (Automated Certificate Management Environment), un protocole standard ouvert largement reconnu. L’obtention de nos certificats reposera sur l’émission et le renouvellement automatisés via ACME : ainsi, toute personne faisant déjà appel à une autorité de certification gratuite existante pourra migrer vers Cloudflare en modifiant simplement une URL de répertoire, sans nouvel outil ni refonte de l’architecture.

## **Les projections de croissance des certificats sont phénoménales**

Cloudflare est déployée en amont de plus de 20 pour cent du trafic mondial de requêtes Internet et assure la terminaison TLS pour des millions de domaines, s’appuyant pour cela sur des millions de certificats par an. Nous provisionnons ces certificats auprès de plusieurs autorités de certification, en définissant des chemins principaux et de secours afin que les services de nos clients restent opérationnels en cas de défaillance d’une autorité de certification ou d’événements de révocation.

Cette situation nous a non seulement permis de comprendre comment fonctionne l’écosystème WebPKI, mais également de constater qu’il subit parfois de graves dysfonctionnements du côté consommateur. Nous avons dû faire face à des limites de débit, des cas limites de validation, des latences de révocation, des incidents de construction de chaînes et des retards de distribution des racines. Nous avons affronté les turbulences résultant de l’instabilité des autorités de certification, ces dernières années, et nous en avons ressenti les conséquences par l’intermédiaire de nos clients. Nous savons à quoi doit ressembler un processus d’émission fiable, vu de l’extérieur, car la disponibilité de nos clients a dépendu de notre capacité à nous montrer résilients et réactifs lorsqu’un émetteur subit des dysfonctionnements.

Et à mesure que la [durée de validité maximale des certificats va diminue](https://cabforum.org/2025/04/11/ballot-sc081v3-introduce-schedule-of-reducing-validity-and-data-reuse-periods/#ballot-contents)r au cours des prochaines années, que l’activité des agents autonomes va augmenter et que les certificats post-quantiques vont se généraliser, nous anticipons que le nombre brut de certificats sur lesquels nous nous appuyons annuellement continuera de croître rapidement – et nous ne sommes pas les seuls à le penser. Nous voulons résoudre ce problème non seulement pour nous-mêmes, mais également contribuer à fournir cette infrastructure à Internet et veiller à ce que la chaîne d’approvisionnement en certificats de nos clients bénéficie de fournisseurs encore plus nombreux.

## **Concevoir pour la résilience : transparence et confinement des incidents**

En assumant cette nouvelle responsabilité, à savoir devenir notre propre autorité de certification, nous nous engageons à construire l’autorité de certification la plus fiable et la plus résiliente possible. Nous avons l’intention de créer une autorité de certification dont la fiabilité ne repose non seulement sur l’absence d’erreurs, mais également, à l’instar des autres produits de Cloudflare, sur le principe «  _fail small_ », dont l’objectif est de confiner les incidents et de limiter l’impact de toute défaillance isolée.

Cela signifie mettre en place des processus pour concevoir et tester la récupération avant même qu’un incident ne survienne. À titre d’exemple, nous ferons de l’automatisation du renouvellement une condition préalable à l’émission. Nous n’émettrons de certificats qu’aux clients prenant en charge l’extension [ACME Renewal Information](https://www.rfc-editor.org/info/rfc9773/) (ARI), normalisée dans la RFC 9773. Les abonnés devront maintenir une automatisation qui interroge notre point de terminaison de renouvellement, réagit en fonction des fenêtres de renouvellement que nous publions et identifie le certificat à remplacer.

Nous tirons également les enseignements de ce que nous avons observé au cours des seize dernières années. Nous avons vu des autorités de certification prises en étau entre la nécessité de révoquer un certificat dans les délais et la volonté de maintenir en ligne les sites de leurs abonnés, parce qu’un trop grand nombre d’abonnés n’étaient pas en mesure de remplacer leurs certificats assez rapidement. Lorsque des certificats doivent être retirés, que ce soit en raison d’un problème de conformité ou un incident de sécurité, nous pourrons avancer les fenêtres de renouvellement des certificats concernés, répartir les remplacements sur le temps imparti et assurer le suivi des certificats de remplacement.

Ce n’est là qu’une des nombreuses approches que nous avons l’intention d’adopter pour bâtir notre infrastructure. Nous ferons preuve de transparence au regard de notre pile d’émission et de nos opérations ; nous publierons des versions reproductibles des logiciels assurant la signature des certificats ; nous certifierons les modules de sécurité matériels qui hébergent nos clés et nous publierons un tableau de bord public détaillant l’intégrité des émissions et les incidents. Les audits constituent des instantanés et vous informent de la conformité d’une autorité de certification, mais ne décrivent pas son fonctionnement un mardi comme un autre. Nous voulons que les programmes de clés racine, les chercheurs et les propriétaires de sites ordinaires puissent observer le fonctionnement réel d’une autorité de certification moderne entre les audits.

## **Une autorité de certification pour l’Internet post-quantique**

Nous entendons également définir l’évolution des certificats, et non seulement nous conformer à la situation actuelle. Nous avons l’intention d’être l’une des premières autorités de certification à émettre des certificats Merkle Tree Certificate (MTC) en environnement de production, l’émission des premiers certificats étant prévue au premier trimestre 2027.

Les certificats MTC constituent une méthode nouvelle et beaucoup plus compacte de délivrance de certificats publiquement reconnus. Ils ont été conçus pour un monde post-quantique, dans lequel les chaînes de certification traditionnelles deviennent tellement volumineuses qu’elles ralentissent les négociations TLS. Nous avons défendu la [proposition de normalisation ](https://datatracker.ietf.org/doc/draft-ietf-plants-merkle-tree-certs/)des certificats MTC auprès de l’IETF et, plus tôt cette année, [Chrome a désigné les certificats MTC](https://blog.google/security/cultivating-a-robust-and-efficient-quantum-safe-https/) comme l’approche privilégiée pour l’authentification post-quantique. L’émission en production des certificats MTC nous permet de protéger les clients de Cloudflare ainsi que l’Internet dans sa globalité contre la menace post-quantique, en appliquant un volume réel à une transition que l’ensemble du web devra opérer. Nous avons fourni des explications détaillées sur le fonctionnement des certificats MTC et le fonctionnement de cette nouvelle infrastructure à clé publique du web (WebPKI, Web Public Key Infrastructure) [dans un article de blog dédié](http://blog.cloudflare.com/pq-ca-with-mtcs).

Nous ne nous attendons pas à ce que cette transition ait lieu du jour au lendemain. Une grande partie d’Internet continuera de s’appuyer sur les certificats classiques et l’infrastructure WebPKI existante pendant encore de nombreuses années. Néanmoins, pendant cette période, nous anticipons une augmentation continue de la part de certificats MTC dans les émissions, et c’est la raison pour laquelle nous développons un service capable de faire les deux. Le regroupement des certificats classiques et les certificats Merkle Tree Certificates sous une autorité de certification unique, avec un cycle de vie unifié et un même ensemble de garanties, permettra aux clients d’effectuer l’adoption au rythme qui leur convient et d’accompagner le web dans une transition sans basculement brutal. Nos clients n’auront pas à choisir un camp lors d’une migration qui durera plusieurs décennies, ni à gérer deux systèmes ou à tout reconfigurer lorsque le point de bascule sera atteint.

## **Comme toujours, Cloudflare sera le client zéro**

En plus de fournir des packs de certificats via Universal SSL à ses clients, Cloudflare consomme des certificats de nombreuses autorités de certification différentes pour exploiter ses systèmes et ses opérations internes. Comme nous l’avons fait pour nos autres produits, nous serons le [client](https://www.cloudflare.com/the-net/top-of-mind-security/customer-zero/) zéro de la nouvelle autorité de certification et de ses certificats (à la fois WebPKI et MTC). Nous veillerons ainsi à ce que tous les aspects des nouveaux systèmes et processus répondent à nos exigences internes strictes et que l’infrastructure de notre autorité de certification soit éprouvée à l’échelle de Cloudflare.

## **Prochaines étapes**

Nous avançons actuellement dans le processus de candidature et d’approbation auprès de chacun des programmes essentiels de clés racine du web. Ces démarches se déroulent de manière transparente, et nous partagerons de nouvelles informations mises à jour au fur et à mesure de leur avancement, jusqu’aux premiers certificats MTC (Merkle Tree Certificate), début 2027. Si vous souhaitez suivre ces travaux ou faire partie parmi des premiers à utiliser un certificat émis par l’autorité de certification de Cloudflare, vous pouvez [vous inscrire pour recevoir nos actualités](http://cloudflare.com/resource/certificate-authority). Et si vous souhaitez participer au développement de cette nouvelle infrastructure au sein de Cloudflare, sachez que [nous recrutons](https://boards.greenhouse.io/cloudflare/jobs/8237801?gh_jid=8237801) !

À mesure que nous développons cette nouvelle infrastructure, nous continuerons à travailler en étroite collaboration avec le réseau d’autorités de certification publiques partenaires sur lequel nous nous appuyons depuis de nombreuses années (seize ans, en réalité !) afin d’œuvrer, tous ensemble, à la construction d’un Internet sûr et ouvert.

Lorsque nous avons lancé Universal SSL, notre motivation était simple : chaque octet qui circule sous forme chiffrée sur Internet rend l’interception, le bridage ou la censure plus difficiles, et le web ouvert est un ouvrage que nous bâtissons tous ensemble. Une autorité de certification publique, redondante et transparente relève de cette même motivation, appliquée à un échelon inférieur ; celui de la confiance sur laquelle repose le web chiffré. Nous progressons vers cet objectif depuis longtemps, et nous sommes ravis d’être enfin lancés sur la route.

Bonne Semaine Anniversaire !

]]>01M4CNGVZYHZ9QJFTXHDWCK3G1Lettre annuelle des fondateurs de Cloudflare – 2026https://blog.cloudflare.com/fr-fr/cloudflares-2026-annual-founders-letter/ Wed, 30 Sep 2026 02:54:51 GMTInternet connaît aujourd’hui des transformations d’une ampleur inédite depuis le lancement de Cloudflare, le 27 septembre 2010. Tandis que le trafic automatisé dépasse désormais l’activité humaine, nous réfléchissons à l’essor des agents IA et des nouveaux créateurs, et nous explorons de quelle manière nous pouvons contribuer à bâtir un avenir équitable et durable pour le web.IALettre des fondateursPlateforme pour développeursSemaine anniversaireTendances InternetCette semaine, Cloudflare fête ses 16 ans. Comme beaucoup d’adolescents de cet âge, nous nous surprenons à regarder le monde dans lequel nous avons grandi avec le sentiment d’être tiraillés entre le passé et l’avenir. Et comme eux, nous observons tous les changements qui s’opèrent dans le monde et nous y voyons parfois des risques. Mais, en fin de compte, nous restons profondément optimistes quant à l’avenir. Ce qui nourrit à la fois notre optimisme et nos inquiétudes, c’est la conviction que le changement entraîne inévitablement des bouleversements.

Internet connaît aujourd’hui des transformations d’une ampleur inédite depuis le lancement de Cloudflare, le 27 septembre 2010. Certaines de ces évolutions semblent incontestablement positives ; d’autres, en revanche, bouleversent fondamentalement notre vision du fonctionnement d’Internet.

Un des changements les plus marquants concerne la vitesse de croissance du web lui-même. De 2012 à 2025, le web a connu une période de stagnation et, selon certains indicateurs, s’est même réduit. Cette tendance s’est inversée au milieu de l’année 2025, avec une explosion du nombre de nouveaux sites. L’idée reçue veut que cette croissance ait été alimentée par des contenus générés par l’IA, n’offrant aucune valeur réelle. Et bien qu’il y ait une part de vérité dans ce postulat, ce n’est pas la majorité de ce que nous observons.

En réalité, l’IA a donné naissance à une nouvelle génération de créateurs ; des personnes qui ont des idées, mais ne maîtrisent pas le codage peuvent désormais donner vie à de nouvelles créations grâce aux outils dits de « vibe coding ». Nous sommes fiers que la majorité de ces outils privilégient la plateforme pour développeurs de Cloudflare comme cible de déploiement. La technologie, dans ce qu’elle offre de meilleur, permet à davantage de personnes d’exprimer leur créativité. Nous sommes idéalement placés pour observer des étudiants du monde entier concevoir des applications permettant de résoudre de vrais problèmes ou regarder de jeunes entreprises concrétiser de nouveaux modèles commerciaux à une vitesse record. Aujourd’hui, plus de 7 millions de développeurs construisent l’avenir sur la plateforme pour développeurs de Cloudflare.

L’année écoulée a également marqué un tournant fondamental dans l’identité des utilisateurs – et surtout, des entités qui utilisent Internet. Nous avions initialement estimé que le trafic automatisé dépasserait le trafic humain au cours du second semestre 2027. L’essor des agents et des robots d’exploration pilotés par IA a avancé cette date à mai 2026. Et si les tendances actuelles se poursuivent, ce qui semble même être une estimation prudente, le trafic automatisé sera mille fois supérieur au trafic humain dans cinq ans seulement ; pas en raison d’un déclin du trafic humain, mais à cause d’une explosion du trafic généré par les agents.

Pour leurs utilisateurs, ces agents IA offrent déjà des avantages époustouflants. Demandez à un agent de vous trouver un vol, un artisan ou un forfait téléphonique moins cher, et il analysera en une minute plus de pages que vous ne pourriez en consulter en un après-midi, avant de vous fournir une réponse. Il effectue le travail de fond à votre place.

Toutefois, ce travail de fond a un coût. Si vous demandez à votre agent IA de vous recommander un établissement où déjeuner, il peut parcourir 1 000 menus de restaurants dans votre région pour finalement n’en recommander qu’un seul. Cet établissement remportera votre réservation, mais les 999 autres auront dû supporter la charge de servir l’agent sans rien recevoir en retour. Le risque qui apparaît ici est celui d’une tragédie des biens communs : les utilisateurs qui bénéficient des choix effectués par les agents IA n’assument pas les coûts résultant de la charge qu’ils imposent au système et agissent donc sans aucune modération.

Si l’IA a permis à ces étudiants et à ces jeunes entreprises de créer des projets plus facilement que jamais, les agents pourraient, quant à eux, rendre beaucoup plus difficile la découverte de ces créations. Aujourd’hui, les petites entreprises séduisent leurs clients par l’émotion ou par la praticité. Vous fréquentez une petite épicerie parce que la personne derrière le comptoir connaît votre nom, ou parce que cela fait partie intégrante de votre identité. Vous faites vos courses dans un commerce du quartier, même si vous savez qu’il ne propose ni le meilleur choix ni les meilleurs prix, simplement parce qu’il se trouve sur le trajet de votre domicile.

Votre agent, quant à lui, ne se préoccupe pas de savoir qui connaît votre nom, et il ne passe pas devant le commerce du quartier en rentrant du travail. Il privilégie les ressources sur lesquelles il dispose du plus grand nombre d’informations, c’est-à-dire, généralement, les établissements qui sont installés depuis le plus longtemps. Dès lors, le risque est que les agents, à mesure qu’ils traitent un nombre croissant de transactions commerciales, rendent de plus en plus difficile l’accès au marché pour les nouveaux arrivants. Ce phénomène, en retour, conduira probablement à une consolidation des commerces et à une fragilisation de l’environnement économique.

Nous avons, nous aussi, été un nouvel arrivant, un jour. Il y a seize ans cette semaine, nous avons lancé Cloudflare sur la scène de la conférence TechCrunch Disrupt pendant que nos ingénieurs étaient assis dans le public, en train de corriger des bugs. Il en restait encore huit quand nous sommes montés sur scène. Lorsque nous l’avons quittée, ils étaient résolus, et nous étions opérationnels dans cinq datacenters présents sur trois continents. Aucun agent ne nous aurait recommandés, mais des personnes nous ont quand même fait confiance. Nous voulons que les prochains nouveaux arrivants aient la même chance.

C’est tout l’enjeu de notre démarche. Pas un avenir avec cinq entreprises de développement d’IA, mais un avenir qui en compte 500 000, présentes dans le monde entier. Pas un avenir où les créateurs de contenus dépérissent et disparaissent faute de rémunération, mais un avenir où chacun peut créer, toucher un public mondial et être payé pour son travail. Et pas un avenir où quelques mégacorporations l’emportent par défaut, mais un avenir où de nouveaux arrivants proposant de meilleurs produits peuvent bien servir leurs clients et s’imposer à leur tour.

L’an dernier, nous avons écrit un article consacré à l’impact de l’IA sur les éditeurs. Cette année, ce même phénomène affecte l’activité des restaurants et des épiceries. Comprendre ce qui remplacera l’ancien modèle économique d’Internet est la question la plus passionnante des cinq prochaines années. Cette semaine, nous tentons à nouveau d’y répondre.

Comme à chaque anniversaire, nous célébrons l’événement en offrant des cadeaux plutôt qu’en en recevant – et certains de ces cadeaux sont destinés aux 999 restaurants. Les agents explorent le web comme les moteurs de recherche l’ont toujours fait : ils indexent tout, encore et encore, que les contenus aient été modifiés ou non. Nos données indiquent que plus de la moitié des contenus collectés par les bots légitimes n’ont pas été modifiés depuis leur dernière visite. Nous avons donc travaillé pour permettre aux robots d’indexation de parcourir une plus grande partie du web en ne récupérant que les nouveaux contenus, ce qui allège considérablement la charge pesant sur les sites qu’ils explorent. Et nous offrons à quiconque publie du contenu ou des applications en ligne un moyen d’être rémunéré lorsque des agents utilisent ce qu’il a créé.

La mission de Cloudflare n’est pas de bâtir un Internet meilleur, mais de _contribuer_ à bâtir un Internet meilleur. Cela signifie que nous ne pouvons pas y parvenir seuls. C’est pourquoi, cette semaine, nous annoncerons également des partenariats avec des entreprises et des organisations qui partagent notre vision de l’avenir.

Comme d’autres adolescents de 16 ans à cette nouvelle ère de l’IA, nous avons l’opportunité d’exprimer nos convictions. Et nous les exprimons en faveur d’un Internet sur lequel il reste toujours de la place pour un adolescent qui lance sa première application, pour l’épicerie de quartier où l’on connaît votre nom et pour quiconque développe le prochain Cloudflare.

Et nous n’avons jamais été aussi enthousiastes de le découvrir.

]]>01M3R3E0J1RZV08QKK7KKFB27RBénéficiez du meilleur des deux mondes : préservez votre référencement tout en refusant l’entraînement des IAhttps://blog.cloudflare.com/fr-fr/accountable-mixed-use-ai-crawlers/ Mon, 21 Sep 2026 02:49:25 GMTCloudflare offre aux propriétaires de sites un moyen de préserver leur référencement tout en refusant l'entraînement des IA. De nouveaux contrôles et la désignation « Responsable » établissent un modèle partagé avec Apple, Google et Microsoft.AI Bots (FR)Gestion des botsIANouveautés produitsSécuritéServices réseauEn l'absence de contrôles adéquats, les propriétaires de sites web étaient depuis longtemps confrontés à un dilemme : autoriser l'utilisation de leur contenu pour l'entraînement des IA ou risquer de voir diminuer leur référencement dans les résultats de recherche. Ce dilemme s'explique par le fait que certaines des plus grandes entreprises du web utilisent des robots d'exploration à usage mixte : un même robot d'exploration sert à la fois à la recherche et à l'entraînement des IA, et refuser une option revient à refuser l’autre.

Aujourd'hui, Cloudflare annonce un nouveau paramètre « [Refuser l'entraînement des IA](https://blog.cloudflare.com/bot-preference-sync/) », qui vous permet de préserver facilement l'indexation de votre site web aux fins de la recherche, tout en interdisant à ces mêmes robots d'exploration d'utiliser votre contenu pour l'entraînement. Apple, Google et Microsoft respectent ce paramètre ou se sont engagés (dans un délai précis) à le respecter.

Les robots d’exploration à usage mixte constituaient l'aspect le plus difficile de la problématique de l'entraînement ; la prochaine question sera celle des résumés générés par l'IA. L'application d'un « oui » ou d'un « non » généralisé à l'ensemble du site est trop simpliste : en effet, la part de votre contenu qui apparaît dans un résumé généré par l'IA est tout aussi importante que l'inclusion ou non de votre contenu dans ce résumé. La possibilité de désactiver les résumés générés par l'IA fait déjà partie des exigences que nous avons établies pour les opérateurs de robots d'exploration à usage mixte. D'ici le début de l'année prochaine, notre objectif est de vous permettre de contrôler la part de votre contenu qui sera incluse en configurant une fois seulement un paramètre sur Cloudflare, plutôt que séparément, auprès de chaque opérateur.

## Pourquoi il ne suffit pas de demander

La plupart des propriétaires de sites souhaitent être trouvés : par les utilisateurs humains, par les agents et par les bots (légitimes). Cependant, une part importante de l'Internet ouvert est financée par la publicité, les abonnements ou les relations directes avec les visiteurs, et ces modèles ne génèrent des revenus que lorsqu'un utilisateur humain consulte effectivement un site.

Presque tous les propriétaires de sites considèrent que la recherche est utile : moins de 1 % des sites hébergés sur Cloudflare choisissent de bloquer les robots d'exploration. L'entraînement des IA, en revanche, est une tout autre problématique : 17 % des sites choisissent de déployer un mécanisme destiné à l'interdire. C'est précisément pour cette raison que nous avons décidé que les propriétaires de sites avaient besoin de contrôles plus précis, plutôt que d'une fonctionnalité généraliste « Bloquer les IA ».

Une directive robots.txt ne suffit pas, à elle seule, à résoudre ce problème. Tous les sites peuvent publier une directive, mais celle-ci ne permet pas d'identifier l'auteur de l'exploration, de déterminer à quelles fins cette exploration a lieu, ni d'empêcher un robot d'exploration de l'ignorer.

Un réseau peut, en revanche, résoudre ce dilemme : nous publions la préférence, nous identifions les robots d'exploration, nous classons leurs motivations et nous bloquons ceux qui l'ignorent ; ensuite, nous publions les actions qu'effectue réellement chaque opérateur sur [Radar](https://radar.cloudflare.com/ai-insights#ai-bot-transparency).

Toutefois, le blocage empêche les robots d'exploration d'accéder à un site ; il ne modifie en rien leur comportement. L'idéal serait que les opérateurs de bots ne vous imposent pas du tout ce choix ; c'est pourquoi, depuis juillet, nous échangeons directement avec eux. Les réactions ont été encourageantes : presque tous se sont accordés à dire que les propriétaires de sites web devaient bénéficier de contrôle et de transparence au regard de l'utilisation de leurs contenus, et qu'ils devaient avoir l'assurance que leurs choix seraient respectés. Pour aider les propriétaires de sites à bien comprendre cela, nous avons créé une certification : « Responsable ».

La certification « Responsable » reconnaît à la fois les fonctionnalités disponibles à ce jour et les engagements concrets pris pour les mettre en œuvre. Pour être éligible, un opérateur de bots doit satisfaire aux exigences suivantes ou s'engager à les respecter :

  1. Un mécanisme permettant aux propriétaires de sites de refuser que leur contenu soit utilisé pour l'entraînement des IA, via le fichier robots.txt ou une norme similaire.
  2. Un mécanisme permettant aux propriétaires de sites de désactiver les résumés générés par l'IA, mis en place directement avec l'opérateur, puis via Cloudflare, l'année prochaine (voir la section ci-dessous pour plus de détails).
  3. Une visibilité au niveau des URL permettant de savoir quelles pages ont été mises à disposition pour l'entraînement, ainsi que des indicateurs montrant comment le contenu apparaissait dans les résultats de recherche.
  4. L'assurance que le fait de refuser de contribuer à l'entraînement des IA n'aura aucune incidence sur les résultats de recherche traditionnelle.



Apple, Google et Microsoft démontrent tous qu’ils satisfont aux conditions requises pour bénéficier de la certification « Responsable ». Chacun d'entre eux allie les fonctionnalités déjà disponibles à des engagements assortis de délais, pour les fonctionnalités qui sont encore en cours de développement. Vous trouverez ci-dessous des informations détaillées sur les robots d'exploration de chacune de ces entreprises.

## Nouvelles options de paramètres de sécurité

Cloudflare classe les bots en fonction de leur comportement, et un même bot peut présenter différents comportements. Les contrôles couvrent trois comportements :

  * **Recherche** : exploration pour constituer un index de recherche.
  * **Entraînement** : exploration pour entraîner ou affiner un modèle.
  * **Agent** : agents pilotés par un utilisateur et consultant une page pour le compte d'un utilisateur humain (par exemple, bots de récupération de messages de chat et agents simulant l'utilisation d'un navigateur).



Un robot d’exploration à usage mixte est un robot unique assurant à la fois des fonctions de recherche et d'entraînement. En l'absence de contrôles, cette combinaison entraîne le dilemme décrit ci-dessus : les propriétaires de sites ne peuvent pas refuser une utilisation sans refuser l'autre.

Afin d’éviter de bloquer les robots d’exploration à usage mixte avec la certification « Responsable » (c'est-à-dire ceux qui n’imposent pas ce compromis aux propriétaires de sites web), nous déployons un nouveau paramètre : « Refuser l’entraînement des IA ». Le paramètre « Refuser l’entraînement des IA » est publie une directive « Disallow: » dans le fichier robots.txt.

### Le paramètre « Bloquer » a désormais une nouvelle signification

Les options « Bloquer » et « Bloquer sur les pages contenant des publicités » ne s’appliquaient auparavant pas aux robots d’exploration à usage mixte, car le blocage de ces robots risquait également d’affecter la visibilité dans les résultats de recherche. Maintenant que le nouveau paramètre « Refuser l'entraînement des IA » est disponible, les options « Bloquer » et « Bloquer sur les pages contenant des publicités » s'appliquent à _tous_ les robots d'exploration, y compris aux robots à usage mixte.

Les contrôles relatifs à l'entraînement, à la recherche et aux agents s'appliquent au niveau du domaine. Avec l’ajout du paramètre « Refuser l'entraînement des IA », les paramètres disponibles son t:

  1. **Autoriser** : tous les robots d’exploration sont autorisés, sauf s'ils sont bloqués par un autre paramètre ou une règle de pare-feu WAF.
  2. **Refuser l'entraînement des IA** : Bot Preference Sync publie la préférence applicable de refus de l'entraînement dans le fichier robots.txt. Les robots d'exploration à usage mixte avec la certification « Responsable » restent autorisés pour l'indexation. Tous les autres robots d'exploration utilisés pour l'entraînement sont bloqués, notamment ceux exploités exclusivement à cette fin par Amazon, Anthropic, Meta et OpenAI ; leur blocage n'a aucune incidence sur les résultats de recherche. L'option « Refuser l'entraînement des IA » est uniquement disponible dans les paramètres relatifs à l'entraînement, et non dans les paramètres concernant la recherche ou les agents.
  3. **Bloquer sur les pages contenant des publicités** : les robots d'exploration, y compris les robots à usage mixte, sont uniquement bloqués sur les pages identifiées comme diffusant une publicité.
  4. **Bloquer** : tous les robots d'exploration, y compris les robots à usage mixte, sont bloqués.



Le paramètre « Refuser l'entraînement des IA » publie une préférence d'interdiction dans le fichier robots.txt. Une préférence concernant uniquement les publicités ne peut pas être mise en œuvre de cette manière : Cloudflare est capable de détecter les pages qui diffusent des publicités, mais cette liste est trop longue et trop fréquemment modifiée pour pouvoir être énumérée dans le fichier robots.txt. C'est pourquoi l'option « Refuser l'entraînement des IA » n'est pas disponible pour les pages contenant des publicités.

Les agents ne suscitent pas le même dilemme entre recherche et visibilité que les robots d'exploration à usage mixte, et il n'existe pas encore sur Internet de directive bien établie permettant d'exprimer des préférences « Disallow » à l'intention des agents. Pour l'instant, nous n'avons pas prévu de paramètre « Disallow » pour les agents. À mesure que des normes telles que [ai-prefs](https://datatracker.ietf.org/wg/aipref/documents/) arriveront à maturité, nous réexaminerons cette approche.

## Qu'est-ce qui changera le 15 septembre ?

Nous apportons les modifications suivantes à Bot Management et AI Crawl Control :

  1. Les options « Bloquer » et « Bloquer sur les pages contenant des publicités » s'appliquent désormais aux robots d'exploration à usage mixte, notamment à Applebot, Bingbot et Googlebot ; ces deux paramètres ont donc une incidence sur la recherche ainsi que sur l'apprentissage. Pour refuser l'entraînement, mais _conserver_ la recherche, utilisez le paramètre « Refuser l'entraînement des IA ».
  2. La fonction « Bloquer les bots IA » sera abandonnée au profit de contrôles plus granulaires concernant la recherche, l'entraînement et les agents.
  3. La fonctionnalité Managed Robots.txt sera abandonnée au profit de Bot Preference Sync. Les clients ayant activé Managed Robots.txt seront migrés vers le nouveau système.
  4. L'option « Refuser l'entraînement des IA » sera désormais intégrée à la configuration recommandée pour certains nouveaux domaines.
  5. Les préférences des clients existants seront migrées vers les nouveaux contrôles, comme décrit ci-dessous.



### Ce que vous devez faire

Rien, dans presque tous les cas. Vos paramètres actuels seront transférés automatiquement.

Si vous souhaitez interdire complètement les robots d'exploration à usage mixte, vous devez désormais le préciser. Sélectionnez l'option « Bloquer » ; cela empêchera Applebot, Bingbot et Googlebot d’accéder à votre site, y compris pour la recherche.

#### Domaines existants n'ayant jamais utilisé les contrôles relatifs à la recherche, à l'entraînement et aux agents.

La configuration des propriétaires de sites qui n'ont jamais défini de contrôles plus précis sera migrée vers les nouveaux paramètres en fonction du paramètre « Bloquer les bots IA » existant :

#### Domaines existants ayant précédemment configuré les contrôles pour la recherche, l'entraînement et les agents

Si les contrôles granulaires ont déjà été configurés pour certains domaines, l'effet concret de leurs choix sera conservé avec les nouvelles définitions. Les sélections précédentes « Bloquer » ou « Bloquer sur les pages contenant des publicités » pour l'entraînement seront migrées vers « Refuser l'entraînement des IA ».

### Recommandations pour les nouveaux domaines

À partir du 15 septembre, les clients intégrant un nouveau domaine se verront proposer l'une des deux configurations prédéfinies, selon que le site génère ou non des revenus publicitaires. Les revenus publicitaires dépendent du fait qu'un utilisateur humain consulte effectivement la page. L'entraînement remplace cette visite par une réponse ; les agents consultent la page sans que les publicités soient affichées. Les paramètres par défaut pour les sites financés par la publicité sont donc plus restrictifs. Vous pouvez modifier n'importe lequel de ces paramètres pendant l'intégration ou le modifier ultérieurement, à tout moment.

_Paramètres recommandés pour les nouveaux domaines._

## Quelles sont les implications pour certains robots d'exploration à usage mixte ?

Applebot, Bingbot et Googlebot ont reçu la certification « Responsable ». Apple, Google et Microsoft adhèrent aux mêmes principes de liberté de choix des éditeurs et de transparence. Lorsque le paramètre « Refuser l'entraînement des IA » est activé, ces bots peuvent continuer à explorer votre site à des fins de recherche. En revanche, sélectionner l'option « Bloquer » les arrête entièrement.

Nous classons également les robots d'exploration concernés d'Amazon, d'Anthropic, de Meta et d'OpenAI dans la catégorie « Responsable ». Ces entreprises séparent leurs robots de recherche de leurs robots d'entraînement, permettant ainsi à Cloudflare de bloquer le robot d'entraînement sans que cela n'affecte la recherche.

### Applebot

Applebot permet aux propriétaires de sites d'interdire l'entraînement en ajoutant une règle « Disallow » dans le fichier robots.txt pour Applebot-Extended. À l'heure actuelle, les propriétaires de sites peuvent également indiquer leurs préférences concernant les résumés générés par l'IA via la [directive](https://support.apple.com/en-us/119829#:~:text=nosnippet%3A%20Applebot,products%20and%20services.) « nosnippet » dans le code HTML de la page. Le contenu peut également être marqué comme [contenu payant](https://support.apple.com/en-us/119829#:~:text=Marking%20paywalled%20content,the%20next%20section.) afin de l'exclure des résultats générés. Applebot ne propose pas encore d'outil permettant d'effectuer une inspection au niveau de l'URL. Nous avons toutefois rencontré l'équipe, qui nous a donné des précisions sur la solution qu'elle élabore actuellement pour l'année prochaine. Apple a également déclaré que le fait d’interdire l'entraînement [n’a aucune incidence sur le classement dans les résultats de recherche](https://support.apple.com/en-us/119829#:~:text=Applebot%2DExtended%20and%20controlling%20data%20usage).

### Googlebot

Googlebot permet aux propriétaires de sites de refuser l’entraînement en ajoutant une règle « Disallow » au fichier robots.txt pour Google-Extended. Il propose également un sélecteur sur son portail pour webmasters permettant d'exclure le contenu d’un site des résultats de recherche génératifs. Googlebot fournit également aux propriétaires de sites des indicateurs et des rapports concernant les résultats de recherche et les résumés générés par l'IA. Google a communiqué des informations sur ses contrôles existants et récemment lancés, ainsi que sur les outils en cours de développement, notamment des outils supplémentaires de transparence au niveau des URL destinés aux propriétaires de sites pour Google-Extended, dont le lancement est prévu dans les semaines à venir. Google a également déclaré que la désactivation de Google-Extended [n’a aucune incidence sur le classement dans les résultats de recherche](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers#google-extended:~:text=Google%2DExtended%20does%20not%20impact%20a%20site%27s%20inclusion%20in%20Google%20Search%20nor%20is%20it%20used%20as%20a%20ranking%20signal%20in%20Google%20Search.).

### Bingbot

Bingbot offre des options de contrôle précises et une grande transparence avec ses outils [Webmaster Tools](https://www.bing.com/webmasters/help/ai-performance-9f8e7d6c). Les propriétaires de sites peuvent actuellement indiquer leurs préférences concernant l'entraînement des IA via la [balise méta](https://blogs.bing.com/webmaster/september-2023/Announcing-new-options-for-webmasters-to-control-usage-of-their-content-in-Bing-Chat#:~:text=Content%20tagged%20NOARCHIVE%20will%20not%20be%20included%20in%20Bing%20Chat%20answers%2C%20not%20be%20linked%20to%20in%20the%20answers.%20Going%20forward%2C%20for%20content%20in%20our%20Bing%20Index%20that%20is%20labeled%20NOARCHIVE%2C%20we%20will%20not%20use%20the%20content%20for%20training%20Microsoft%E2%80%99s%20generative%20AI%20foundation%20models.) `NOARCHIVE` de Bing. Microsoft étend ces fonctionnalités et développe actuellement un mécanisme permettant de respecter également une préférence de refus de l'entraînement définie dans le fichier robots.txt sur l'ensemble du domaine ou du site ; la mise en œuvre est prévue début 2027. Outre l’utilisation de la balise `NOARCHIVE`, les clients de Cloudflare qui souhaitent dès aujourd’hui exclure l'utilisation de leur contenu aux fins de l'entraînement de Bing peuvent s'appuyer sur [l'outil de blocage d'URL ou de suppression de contenu](https://www.bing.com/webmasters/help/block-urls-from-bing-264e560a). Microsoft a également déclaré que l’utilisation de `NOARCHIVE` [n’aura aucune incidence sur le classement dans les résultats de recherche](https://blogs.bing.com/webmaster/september-2023/Announcing-new-options-for-webmasters-to-control-usage-of-their-content-in-Bing-Chat#:~:text=We%20also%20heard%20from%20publishers%20that%20they%20want%20to%20exercise%20these%20choices%20without%20impacting%20how%20Bing%20users%20can%20discover%20web%20content%20on%20Bing%E2%80%99s%20search%20results%20page.%20We%20can%20assure%20publishers%20that%20content%20with%20the%20NOCACHE%20tag%20or%20NOARCHIVE%20tag%20will%20still%20appear%20in%20our%20search%20results.).

Tant que cette fonctionnalité ne sera pas disponible, sélectionner « Refuser l'entraînement des IA » ne transmettra pas automatiquement, via le fichier robots.txt, la préférence de refus de l'entraînement à Bing. Ce comportement correspond à celui de l'ancien paramètre « Bloquer l'entraînement », qui ne s'appliquait pas aux robots d'exploration à usage mixte, tels que Bingbot.

### Des progrès continus

Nous continuerons à contacter et à collaborer avec tous les opérateurs de robots d'exploration pilotés par IA, à mesure que ces fonctionnalités évolueront. Cloudflare [Radar](https://radar.cloudflare.com/ai-insights#ai-bot-transparency) assure un suivi public des contrôles, de la transparence et des rapports fournis par les opérateurs de robots d'exploration ayant obtenu la certification « Responsable ». 

Pour contribuer à bâtir un Internet meilleur, les deux parties doivent disposer d'une certaine autonomie : les robots d'exploration doivent pouvoir accéder au web ouvert, et les créateurs de ce web doivent disposer d'un contrôle effectif sur l'utilisation de leur travail. L'annonce faite aujourd'hui marque une avancée concrète vers cet équilibre.

Pour assurer la continuité des progrès, les fournisseurs d'infrastructures, les créateurs de contenus, les entreprises technologiques et les organismes de normalisation, tels qu'Internet Engineering Task Force (IETF), devront collaborer afin de traduire ces principes en normes ouvertes et interopérables.

## Prochaine étape : les résumés générés par l'IA

L'entraînement des IA et les résumés générés par l’IA entraînent différentes questions pour les propriétaires de sites. L'entraînement des IA détermine si un contenu peut être utilisé pour développer des modèles d'IA, tandis que les résumés générés par l'IA influencent la manière dont les internautes découvrent, évaluent et, en fin de compte, consultent le site web d'une entreprise. Ces deux aspects sont importants, mais ont des répercussions différentes sur les entreprises.

Les contrôles permettant de refuser l'utilisation de contenus dans les résumés générés par l'IA constituent la première étape. Les opérateurs ayant obtenu la certification « Responsable » fournissent ou développent actuellement cette fonctionnalité, établissant un principe fondamental : les propriétaires des sites peuvent refuser.

Cependant, le choix d'autoriser ou d'interdire les résumés générés par l'IA pour l'ensemble du site reste un outil peu précis. Une décision pertinente dépend du site, du contenu et de la finalité commerciale. Pour les éditeurs, l'entraînement des IA soulève des questions fondamentales concernant le contrôle, la rémunération et la pérennité des contenus originaux. Les résumés générés par l'IA soulèvent une question distincte, et souvent plus immédiate, concernant la diffusion : l'internaute se rend-il sur le site de l'éditeur, ou consulte-t-il la réponse directement dans le cadre d'une recherche ou d'une expérience d'utilisation de l'IA ? Pour de nombreuses autres entreprises, les résumés générés par l'IA constituent de plus en plus souvent un maillon entre un client potentiel et un site web. Ils peuvent répondre à une question, comparer différentes alternatives, recommander un produit ou aider un internaute à décider s'il souhaite consulter le site web de l'entreprise.

Les données montrent des résultats mitigés. [Plus de la moitié](https://www.pewresearch.org/chart/a-majority-of-americans-say-they-read-ai-summaries-at-the-top-of-search-results/) des consommateurs lisent les résumés générés par l'IA inclus dans les résultats de recherche, et ces consommateurs sont [plus de 40 % plus susceptibles](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/) de [mettre fin à leur recherche](https://www.bain.com/insights/goodbye-clicks-hello-ai-zero-click-search-redefines-marketing/) après avoir lu un résumé. Cela peut entraîner une baisse du nombre de visites sur un site web. Cependant, le taux de conversion des consommateurs orientés par une recherche avec l'IA est [trois fois](https://aisearch.similarweb.com/blog/ai-visibility-roi/) à [plus de cinq fois](https://quickseo.ai/blog/ai-search-vs-google-search-in-2026-40-stats-that-show-why-your-brand-needs-to-track-both#:~:text=AI%20search%20traffic%20converts%20at%2014.2%25%2C%20compared%20to%20Google%E2%80%99s%202.8%25) supérieur à celui des visiteurs issus d'une recherche traditionnelle. Si l’IA peut entraîner une baisse du nombre de visites, elle envoie également des clients affichant une intention d'achat beaucoup plus marquée.

En soi, cela n’est ni bon, ni mauvais. Un éditeur financé par la publicité peut chercher à optimiser son volume d'audience. Un revendeur peut, quant à lui, préférer recevoir des visiteurs moins nombreux, mais plus enclins à acheter. Le rôle de Cloudflare n'est pas de choisir à leur place, mais de leur fournir la visibilité et le contrôle nécessaires pour prendre une décision bien informée.

Les options de refus d'utilisation des contenus dans les résumés générés par l'IA sont un bon point de départ, mais ils ne constituent pas une solution définitive. Notre prochain objectif est d'aider les propriétaires de sites à comprendre l'impact des résumés générés par l'IA sur leur activité et de leur donner davantage de contrôle sur la part de leur contenu pouvant être utilisée dans ces résumés. Les normes ouvertes telles que [ai-prefs](https://datatracker.ietf.org/wg/aipref/documents/) joueront un rôle important pour y parvenir.

Si vous souhaitez participer à cette conversation ou nous faire part de vos commentaires, veuillez nous écrire à l'adresse [crawlercontrols@cloudflare.com](mailto:crawlercontrols@cloudflare.com).

Ces nouveaux contrôles sont disponibles pour tous les clients, dans toutes les offres, et peuvent être configurés depuis les [Paramètres de sécurité](https://dash.cloudflare.com/?to=/:account/:zone/security/settings) au niveau du domaine (zone). Votre site n’est pas encore hébergé sur Cloudflare ? [Souscrivez à notre offre gratuite](https://www.cloudflare.com/lp/pg-one-platform/) et définissez dès aujourd’hui les mesures de contrôle du trafic que vous souhaitez mettre en oeuvre.

]]>01M30X9NKZN3T1DW96RR0EFMDWRécapitulatif des solutions que nous avons lancées au cours de l'Agents Weekhttps://blog.cloudflare.com/fr-fr/agents-week-review-august-2026/ Thu, 13 Aug 2026 08:03:09 GMTNotre dernière Agents Week est maintenant terminée. Vous trouverez ci-dessous un récapitulatif de toutes les annonces que nous avons faites, de la solution Wallets à Cloudflare Radar.AgentsAgents WeekCloudflare OneCloudflare WorkersDéveloppeursIAPlateforme pour développeursSASEZero TrustAu début de l'Agents Week, Rita[ a expliqué](https://blog.cloudflare.com/agents-week-welcome/) que les agents représentent la prochaine évolution de l'informatique : non seulement en tant que nouvelle application de l'IA, mais également comme nouvelle catégorie de logiciels conçus pour façonner la manière dont les utilisateurs interagissent avec la technologie et dont les logiciels interagissent avec Internet. Au cours de[ l'année dernière](https://www.cloudflare.com/innovation-week/ai-week-2025/updates/), nous avons entrepris d'explorer ce que cette transformation signifie pour les développeurs et les clients qui conçoivent des applications natives de l'IA, de même que l'infrastructure nécessaire pour les soutenir. Plus les agents deviennent capables et autonomes, plus les problématiques s'étendent au-delà des modèles eux-mêmes, vers l'identité, la communication, l'orchestration, la mémoire, l'observabilité et la sécurité.

La semaine passée, nous avons détaillé de quelle manière nous rassemblons ces éléments sur la plateforme Cloudflare afin de servir un Internet agentique. Chaque jour, nous vous avons présenté de nouveaux outils, de nouvelles idées et de nouveaux produits conçus pour bâtir un Internet au sein duquel les humains et les agents[ coopèrent plutôt que d'entrer en conflit](https://blog.cloudflare.com/the-agentic-internet/).

### **Lundi 3 août**

Le lundi se concentrait sur le socle à mettre en place pour développer et exécuter des applications intelligentes et autonomes, c'est-à-dire les agents d'exécution et d'infrastructure sur lesquels ils reposent.

[Votre agent a besoin d'un ordinateur, pas d'un conteneur — découvrez @cloudflare/computer](https://blog.cloudflare.com/cloudflare-computer/)| La solution @cloudflare/computer propose un nouvel environnement d'exécution conçu pour les agents, capable de choisir l'environnement adéquat pour une tâche donnée.  
---|---  
[Workers RPC fonctionne désormais sur l'ensemble des environnements Python et JavaScript](https://blog.cloudflare.com/python-workers-rpc/)| Les Workers Python et JavaScript peuvent désormais communiquer directement afin de faciliter les projets multilingues.  
[Plus petits, plus rapides, plus sûrs : exécuter les modèles Kimi et GLM à grande échelle](https://blog.cloudflare.com/smaller-faster-safer-models/)| Découvrez comment nous prenons en charge de grands modèles de manière plus efficace, sans sacrifier la qualité, la fiabilité ni la sécurité.  
[Présentation de l'API Billable Usage : une visibilité programmatique sur les coûts pour Cloudflare](https://blog.cloudflare.com/billable-usage-api/)| Un moyen plus simple de suivre l'utilisation et les coûts de nos produits en libre-service.   
[Les services Cloudflare Workers et Containers prennent désormais en charge les connexions TCP entrantes et gRPC](https://blog.cloudflare.com/grpc-workers/)| Hébergez des back-ends vocaux assistés par IA ou d'autres agents vocaux en temps réel grâce à Cloudflare Workers.  
  
### **Mardi 4 août**

Mardi, nous avons lancé le service Agent Development Lifecycle (ADLC, cycle de vie du développement des agents) et les primitives qui font passer les logiciels agentiques du stade de prototype à la production.

[Cloudflare propose désormais le service Agent Development Lifecycle](https://blog.cloudflare.com/agent-development-lifecycle/)| Remplacez le service SDLC (Software Development Lifecycle, cycle de vie du développement logiciel) par l'ADLC, notre approche pour faire passer les agents du stade de prototype à la production, ainsi que par les primitives qui sous-tendent la prochaine génération de « fabriques de logiciels » (software factories).  
---|---  
[Présentation : Cloudflare Agents](https://blog.cloudflare.com/agents-on-cloudflare/)| Développez des agents sur Cloudflare et suivez chaque exécution en direct, avec traçage, replay et approbations avec intervention humaine (Human-in-the-Loop) pour voir ce qui se passe en production.  
[Votre agent peut désormais débuguer les Workers grâce au traçage local](https://blog.cloudflare.com/local-tracing/)| Nous vous proposons le traçage distribué au sein du développement local afin de permettre aux agents de trouver et de débuguer plus facilement les problèmes avant qu'ils ne se manifestent en production.  
[Annonce de Cloudflare Wallets : le portefeuille programmable pour l'Internet agentique](https://blog.cloudflare.com/wallets/)| Le service Wallets propose un moyen sécurisé de permettre aux agents de réaliser des transactions en tant que participants à l'économie agentique émergente.  
[Exécutez CI/CD pour des millions de dépôts : sur votre plateforme, sur Cloudflare](https://blog.cloudflare.com/ci-workflows/)| Pipeline d'intégration/diffusion continue (CI/CD, Continuous Integration/Continuous Delivery) programmable. Profitez de pipelines rédigés en code (et non en configuration) grâce à un agent qui répare les échecs et prépare les correctifs pour révision.  
[Comment Cloudflare applique les normes d'ingénierie grâce à l'IA](https://blog.cloudflare.com/engineering-standards-enforcement/)| La manière dont nous utilisons l'automatisation assistée par IA tout au long de nos workflows de développement afin de maintenir l'alignement des normes de code et des processus, et ainsi d'aider nos propres fabriques de logiciels à produire un code de qualité et cohérent à grande échelle.  
[La manière dont nous avons bâti notre fabrique de logiciels pour réduire le nombre de problèmes GitHub d'Astro à zéro](https://blog.cloudflare.com/astro-issue-triage/)| Automatisez l'analyse, la catégorisation et le routage des problèmes afin de minimiser les tâches fastidieuses de maintenance logicielle et optimiser la productivité des développeurs.  
  
### **Mercredi 5 août**

Le mercredi, nous avons étendu le Zero Trust des utilisateurs et des appareils aux agents eux-mêmes. Nous avons également partagé la manière dont nous l'appliquons en interne chez Cloudflare.

[Le cadre Agent Access Model](https://blog.cloudflare.com/the-agent-access-model/)| Ce cadre permet aux agents d'accéder en toute sécurité aux ressources et aux services pour le compte des utilisateurs, sur un réseau Internet de plus en plus peuplé d'agents.   
---|---  
[Comment nous réinventons le travail chez Cloudflare grâce à Cloudflare OS](https://blog.cloudflare.com/how-we-use-ai-with-cloudflare-os/)| Découvrez la manière dont nous avons intégré l'IA au sein de notre modèle opérationnel interne afin de permettre aux équipes de travailler plus intelligemment et plus rapidement sans sacrifier la sécurité ni la supervision.  
[Cloudflare OS : une plateforme ouverte pour les agents, les applications et le travail](https://blog.cloudflare.com/cloudflare-os/)| Nous avons ouvert le code de la plateforme que nos équipes utilisent pour développer des applications, automatiser le travail et accéder aux systèmes internes, en toute sécurité.   
[Détecter les comportements indésirables en matière d'IA grâce à des outils d'analyse sensibles à l'identité](https://blog.cloudflare.com/identity-aware-ai-gateway/)| Attribuez l'activité de l'IA à de véritables utilisateurs et systèmes afin de détecter plus facilement les anomalies et les pics de dépenses.  
[WriteGuard : des mesures de contrôle fines pour les serveurs MCP](https://blog.cloudflare.com/mcp-portal-writeguard-private-beta/)| Pour un meilleur contrôle des appels d'outils à risque et réduire les chances que les agents effectuent des modifications indésirables, nous proposons à nos clients les mêmes outils que ceux que nous déployons.  
  
### **Jeudi 6 août**

Jeudi fut le jour de la définition de l'Internet agentique et de la manière dont les propriétaires de sites web, les éditeurs et les agents peuvent tous contribuer à un Internet qui fonctionne à la fois pour les utilisateurs et les agents.

[Bâtir un Internet agentique ouvert : lisible, découvrable, accessible et payable](https://blog.cloudflare.com/the-agentic-internet/)| Un modèle pour un Internet agentique au sein duquel les éditeurs gardent le contrôle et les agents bénéficient d'un accès utile aux ressources dont ils ont besoin, en plus de protocoles ouverts permettant aux deux parties d'effectuer des transactions.  
---|---  
[Donnez une interface WebMCP à n'importe quel site web](https://blog.cloudflare.com/webmcp/)| Découvrez un aperçu du WebMCP, qui introduit une nouvelle approche (très simple) pour rendre les sites web et les applications web accessibles et utilisables par les agents.  
[Du référencement à la recommandation : préparez votre site afin de lui permettre de prospérer à l'ère agentique](https://blog.cloudflare.com/aeo/)| Adaptez le SEO aux pratiques de l'AEO (Answer Engine Optimization, optimisation pour les moteurs de réponses) afin d'améliorer l'identification, la compréhension et l'interprétation du contenu web par les agents.  
[Présentation de Kitesurf : le navigateur conçu pour les agents qui fonctionne au sein d'isolats V8 sur les Workers Cloudflare](https://blog.cloudflare.com/kitesurf/)| Un navigateur conçu spécialement pour les agents, qui privilégie un rendu parfait pixel par pixel pour une utilisation réduite de la mémoire et du processeur.  
[La prochaine génération de MCP](https://blog.cloudflare.com/mcp-v2/)| Le MCP a été réécrit. En simplifiant le déploiement et la scalabilité des applications agentiques, la version MCPv2 introduit la prochaine évolution du support MCP,.  
[Cloudflare AI Search : offrez un moteur de recherche à vos agents afin d'interroger vos données](https://blog.cloudflare.com/ai-search-easier/)| Le service AI Search transforme vos fichiers ou votre site web en un moteur de recherche prêt pour les agents avec une seule commande.  
  
### **Vendredi 7 août**

Vendredi a mis en lumière ce qui se passe réellement : les tâches que les agents effectuent vraiment sur le web, où l'IA fonctionne dans vos applications, qui contribue aux écosystèmes et de nouveaux outils pour analyser les données Internet.

[Dévoiler les bons et les mauvais comportements sur l'Internet agentique](https://blog.cloudflare.com/good-and-bad-agentic-behaviors/)| Les bots ne sont pas toujours mauvais, et les humains ne sont pas toujours bons. I faut repenser la lutte contre les bots autour de la confiance continue plutôt que voir un risque ponctuel.  
---|---  
[Unifier les services Workers AI et AI Gateway grâce à une interface de contrôle unique assistée par IA](https://blog.cloudflare.com/workers-ai-gateway-unification/)| Une liaison, un portefeuille, un tableau de bord pour appeler n'importe quel modèle d'IA. Le routage axé sur le modèle viendra ensuite.  
[Annonce des programmes Cloudflare Ambassadors, Community Engineers et d'un autre million de dollars pour le financement open-source](https://blog.cloudflare.com/community-program-refresh/)| Notre initiative Community actualisée lance deux nouveaux programmes : Cloudflare Ambassadors (ambassadeurs Cloudflare) pour les leaders de la communauté et Community Engineers (ingénieurs communautaires) pour les mainteneurs open-source. De même, 1 millions de dollars supplémentaires en financement open-source viendront s'ajouter pour les deux prochaines années.  
[Présentation de Radar Researcher : un outil IA conçu pour explorer les données de l'Internet en langage clair](https://blog.cloudflare.com/introducing-radar-researcher/)| L'assistant de recherche soutenu par IA de Cloudflare Radar: questions en langage clair, graphiques interactifs en sortie.  
  
### **L'Agents Week est terminée, mais nous n'avons pas terminé de travailler**

Cinq jours plus tard, la réponse à la question de Rita « [Qu'attend votre agent d'un cloud agentique ?](https://blog.cloudflare.com/agents-week-welcome/) » commence à se préciser. Ce nouvel univers nécessite une couche d'exécution et des primitives pour fonctionner, un cycle de développement qui s'écrit de plus en plus lui-même, un accès sécurisé pour les utilisateurs et les agents qui effectuent le travail, un Internet agentique, ainsi que les humains et les communautés qui maintiennent l'ensemble. Il reste encore beaucoup à venir, mais la forme de ce qui va suivre devient plus précise : un Internet qui soutient nativement les utilisateurs humains pour lesquels il a été conçu et les agents qui effectuent désormais des tâches pour leur compte.

Nos travaux ne s'arrêtent pas ici. Gardez un œil sur notre[ journal des modifications](https://developers.cloudflare.com/changelog/) pour consulter les dernières mises à jour. En outre, nous serions ravis de vous entendre si vous souhaitez bâtir une partie de cet édifice avec nous ! N'hésitez pas à nous retrouver sur[ X](https://x.com/cloudflaredev) ou[ Discord](https://discord.com/invite/cloudflaredev).

]]>01KZX1M46VXVFEAVQ1KXTRK5JYDévoiler les bons et les mauvais comportements sur l'Internet agentiquehttps://blog.cloudflare.com/fr-fr/good-and-bad-agentic-behaviors/ Thu, 13 Aug 2026 03:31:15 GMTCloudflare passe de l'évaluation ponctuelle des risques des bots à un processus d'évaluation continue de la confiance. Découvrez comment nos systèmes (notamment BotBase et Precursor) évaluent les nouveaux comportements positifs et négatifs des bots et des agents. Essayez notre simulation Precursor Trace pour voir comment vos propres mouvements de curseur seraient évalués comme réalisés par un utilisateur humain ou un bot.AgentsAgents WeekAI Bots (FR)Gestion des botsServices réseauLe réseau Internet n'est pas une voie de circulation à sens unique. La règle générale en matière de sécurité du web a longtemps reposé sur l'idée que les bots étaient « mauvais », tandis que les utilisateurs humains étaient « bons ». Nous avons largement dépassé cette généralisation bien entendu. Les humains peuvent avoir des comportements frauduleux et les bots se montrer utiles à différents niveaux. Les propriétaires de sites souhaitent activement que le trafic automatisé puisse interagir avec nos sites afin d'assurer la fonctionnalité et l'accessibilité d'Internet.

Pour compliquer encore la situation, la distinction entre « utilisateur humain » et « bot » devient de plus en plus floue. Nous sommes désormais en présence d'un type de trafic « hybride » au sein duquel une session unique peut passer de l'humain à l'agentique, et vice versa. (Vous pouvez, par exemple, penser à un utilisateur parcourant les rayons d'un magasin, avant de confier le processus de paiement à un assistant de shopping automatisé.)

Alors, comment les propriétaires de sites web parviennent-ils à gérer cette complexité ? La notion importante ici consiste à évaluer les **comportements**. Ce comportement est-il abusif? Malveillant ? Quel risque se présente ici et puis-je faire confiance à ce visiteur en fonction de ses actions ? Pour résoudre cette problématique, il est nécessaire d'aller au-delà des simples mesures de contrôle statiques et ponctuelles. L'évaluation de la confiance implique un processus d'analyse des comportements en continu.

Cet article s'attachera à vous partager une perspective intérieure de la stratégie de l'équipe Web Integrity & Trust (qui couvre les domaines des problèmes liés aux bots et à la fraude) en ce qui concerne la détection et l'analyse des comportements bons et mauvais, tout en vous proposant des outils conçus pour aider les propriétaires de sites à relever les défis émergents d'un réseau Internet agentique en pleine mutation. Nous partagerons également nos conclusions sur le trafic agentique depuis le lancement de[ Precursor](https://blog.cloudflare.com/introducing-precursor/), ainsi qu'une simulation dans laquelle vous pourrez voir comment vos propres mouvements de curseur seraient évalués comme réalisés par un utilisateur humain ou un bot., en plus de quelques passionnantes mises à jour des lancements à venir prochainement.

## **Définir le risque et la confiance**

Parlons de la distinction entre le **risque** et la **confiance** , telle que nous en discutons au sein des équipes Cloudflare qui travaillent sur la détection des bots. Ces aspects sont souvent perçus comme les pôles opposés d'un continuum. Chez Cloudflare, nous les considérons comme des valeurs indépendantes, mais réciproques. La confiance constitue l'ingrédient essentiel à la prise de décisions éclairées en ce qui concerne votre trafic. 

Le risque représente la probabilité qu'une requête ou une action soit nuisible. Il est d'ailleurs souvent éphémère. Or, la confiance se bâtit au fil du temps et repose sur la réputation.

Illustrons cette différence par un exemple de la vie réelle : disons que vous profitez d'une soirée télé chez vous, lorsque soudainement, vous entendez la sonnette retentir à plusieurs reprises. Outre son caractère ennuyeux et agaçant, ce comportement est étrange. Le fait que quelqu'un appuie de manière frénétique et répétée sur la sonnette tard dans la nuit est une situation pour le moins alarmante.

Vous jetez un œil à votre caméra de porte et découvrez que la personne qui sonne à votre porte est votre meilleur ami, qui réside à côté. Bien entendu, vous faites confiance à votre meilleur ami et nous gageons que vous le laisseriez entrer.

Dans cet exemple, il ne suffirait pas de dire : « Rejetez toute personne qui sonne à ma porte la nuit » ou « Rejetez toute personne qui sonne à ma porte plus de 10 fois ». Encore une fois, la confiance s'avère l'ingrédient essentiel.

Revenons au trafic sur Internet, la stratégie que nous suivons en ce qui concerne le développement de produits dans le domaine des bots et de la fraude s'axe sur la création d'un écosystème entier basé sur la confiance. Notre objectif consiste à proposer les mesures incitatives et les primitives qui permettront aux propriétaires de sites d'encourager les comportements qui rendent Internet plus sûr pour tous, en commençant par bloquer les activités malveillantes à la base, jusqu'à l'incitation à la participation à un écosystème Internet plus sûr au sommet.

## **Les bons comportements, ancrés dans la transparence**

En commençant par le haut : quels comportements sont considérés comme « bons » ? Nous pouvons tirer des exemples clairs des bots et des agents vérifiés au sein du service BotBase. Le mois dernier, nous avons annoncé une[ mise à jour de la taxonomie pragmatique des bons bots que nous suivons dans notre système](https://blog.cloudflare.com/content-independence-day-ai-options/). Nous avons ainsi réduit la définition du statut « [vérifié](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/) » à deux aspects : 1) le fait de se déclarer honnêtement, et 2) le fait de ne pas abuser de la confiance que vous avez gagnée. 

La transparence entre un propriétaire de site et un exploitant de bot permet la mise en place d'une relation symbiotique : les propriétaires de sites peuvent indiquer les comportements et les usages de données qu'ils souhaitent autoriser sur leurs sites, tandis que les exploitants de bots peuvent bénéficier d'un accès plus facile. La transparence permet de gagner de la confiance au sein de la relation. Si vous n'avez rien à cacher, le fait de déclarer votre identité devrait réduire les frictions avec les sites qui souhaitent autoriser vos comportements.

Le service [BotBase](https://developers.cloudflare.com/bots/botbase/) n'est pas uniquement destiné à effectuer des déclarations sur « qui est bon ». Il est conçu pour se présenter comme un répertoire de l'ensemble des bots et des agents connus, ainsi qu'à fournir des faits autour de ces derniers. Comparé à notre précédent répertoire de bots, qui ne comprenait que les bots connus « utiles », la solution BotBase est également capable de suivre les bots et les agents _moins utiles_. Pourquoi ? Parce que nos systèmes suivent et valident le comportement des acteurs connus comme fiables, ce qui signifie que nous disposons des outils pour identifier à quel moment ces attentes ne sont pas satisfaites. Si vous abusez de la confiance accordée sur le réseau Cloudflare, vos autorisations ne doivent **pas** être facilement attribuées et vous écoperez dès lors du statut « non vérifié ».

## **Comportements indésirables : les actions flagrantes, furtives et l'ensemble du spectre entre les deux**

Il y a quelques semaines, nous avons annoncé la solution[ Precursor](https://blog.cloudflare.com/introducing-precursor/), un système client continu conçu pour détecter même _le trafic lié aux bots subtilement inhumain_ , qui peut passer inaperçu lorsqu'on évalue uniquement les signaux réseau. La détection JavaScript est injectée par le CDN lorsqu'un client active Precursor Il n'est donc pas nécessaire de se trouver devant l'ordinateur pour déterminer où relancer ces détections ou comment procéder. De plus, le service Precursor évalue le comportement des utilisateurs[ en continu tout au long de la session](https://developers.cloudflare.com/cloudflare-challenges/precursor/). Vous n'avez donc plus besoin d'accorder des laissez-passer gratuits au trafic abusif qui aurait réussi à passer les mesures de contrôle côté client et du côté du navigateur, même une seule fois.

En appliquant notre cadre Risk and Trust (Risque et confiance) à ces mesures de détection côté client, nous pouvons remarquer que les CAPTCHAs ou les obstacles temporaires se basent sur le risque, ce qui signifie qu'ils manquent de _contexte_. De l'autre côté, le processus de vérification reposant sur des indices comportementaux se base sur la confiance. Il peut donc capturer davantage d'indices contextuels sur l'ensemble de la session utilisateur. La solution Precursor constitue l'outil qui nous permet d'analyser ce comportement. En résumé, le service Precursor se révèle particulièrement puissant, car il :

  1. propose des mesures de détection basées sur la confiance tout au long de la session utilisateur ;
  2. **augmente les coûts subis par les développeurs de bots** pour reproduire le comportement humain sur une chronologie multipages.



En rendant l'opération qui consiste à distancer ces mesures de détection _économiquement désavantageuse_ pour les développeurs, nous gagnons le jeu de l'antagonisme.

Qu'avons-nous appris depuis le lancement de nos solutions ? En examinant une période de 24 heures seulement à l'heure où nous rédigeons ce blog, nous pouvons voir que **Prercursor a réalisé 206 millions d'évaluations** dans **73 438 zones** situées sur le réseau Cloudflare.

Nous pouvons repérer des schémas dans les données qui révèlent des éléments que nous suspections déjà lors du lancement de notre service détection, mais que nous pouvons désormais valider par l'analyse de dizaines de milliers de domaines :

  * Un comportement suspect se manifeste souvent en cours de session, ce qu'une mesure de détection ponctuelle ne saisirait pas.
  * **Le comportement passe souvent de l'humain à l'agentique, et vice versa, au cours d'une session**. Il est donc important dans ces scénarios de bien comprendre _l'intention_ afin que les propriétaires de sites ne bloquent pas les flux d'utilisateur qu'ils souhaitent en réalité voir sur leur site.
    * Cet aspect souligne l'importance d'un système de classification des bots qui permet aux propriétaires de sites web de gérer le trafic en fonction du scénario d'utilisation, de l'objectif et de l'utilisation des données. C'est précisément pour cette raison que nous avons donné la priorité aux mises à jour de la taxonomie pour BotBase.



Pour ceux qui souhaitent en apprendre davantage sur le fonctionnement véritable du service Precursor, nous avons partagé un aperçu dans notre[ article de blog](https://blog.cloudflare.com/introducing-precursor/) d'annonce de cette solution (la manière dont les signaux que nous analysons nous ont montré que l'erreur est humaine). **Nous allons encore plus loin aujourd'hui en proposant une démo interactive simulant comment Precursor tracerait vos mouvements de curseur à tous les utilisateurs d'Internet.**

Le service **[Precursor Trace](https://precursor-trace.cloudflare.app) **est désormais disponible et présente la manière dont nous évaluerions _vos_ mouvements de curseur à l'aide du mécanisme de détection de Precursor (du moins une partie de ce dernier). Vous pouvez ainsi voir si vous accélérez vos mouvements ou les corrigez, le rythme et la texture des mouvements de votre curseur, et encore plus d'aspects auxquels vous n'avez probablement jamais pensé en tant que véritable être humain interagissant avec un ordinateur. Essayez-le !

## **L'intelligence adaptative arrive bientôt**

Les[ moteurs de détection de bots](https://developers.cloudflare.com/bots/concepts/bot-detection-engines/) Cloudflare peuvent produire[ différents résultats](https://developers.cloudflare.com/bots/concepts/bot-score/#bot-groupings) lors de l'évaluation d'une requête afin de déterminer si elle est automatisée ou non. Pour les requêtes considérées comme automatisées, l'évaluation peut être 1) définie comme manifestement automatisée, en nous basant sur des méthodes déterministes prouvées ou les empreintes numériques des bots, ou 2) probablement automatisée, en nous basant sur le score prédictif fourni par le service Bots ML de Cloudflare.

Historiquement, le service[ Bots ML](https://developers.cloudflare.com/bots/concepts/bot-score/#machine-learning) a été actualisé en plusieurs versions, ce qui signifie que nous avons annoncé chaque nouvelle version du modèle comme un lancement de produit. Cette cadence ne fonctionne pas lorsque les bots s'adaptent en l'espace de quelques heures, voire de quelques minutes.

L'intelligence adaptative (Adaptive Intelligence, un moteur de détection totalement nouveau) est différente de tout ce que nous avons précédemment conçu dans le domaine de Bots ML (l'apprentissage automatique des bots). **Le modèle lui-même est adaptatif**. Il a été nourri de tout ce que nous avons observé dans le passé, mais surtout, il _continuera_ à apprendre et à s'auto-ajuster en fonction de ce qu'il observe lui-même. L'intelligence adaptative s'actualisera elle-même en fonction d'une large gamme de profils de trafic que nous identifions (des bons comportements aux mauvais) et les clients n'auront plus besoin de passer à une nouvelle version formelle du modèle pour bénéficier des dernières mesures de détection prédictives autour des bots. 

Tous les clients de notre solution Bot Management auront bientôt accès à l'intelligence adaptative. Restez à l'écoute de l'annonce de son lancement à venir.

## **Aller au-delà du déterminisme pour influencer le comportement des bots**

Jusqu'à présent, nous nous sommes concentrés sur l'aspect Cloudflare : la stratégie, le processus de détection et la taxonomie. Tous ces éléments permettent à Cloudflare de doter les propriétaires de sites web des outils dont ils ont besoin pour définir les politiques de trafic qu'ils souhaitent mettre en place sur leurs sites. En ce qui concerne les propriétaires de sites, nous souhaitons profiter de cette occasion pour discuter de certaines **mesures d'atténuation avancées** qui permettent aux propriétaires eux-mêmes d'influencer le comportement des bots.

Avec la mise en place de techniques de mitigation plus évidentes, nous sommes désormais confrontés à un aspect que nous avons surnommé le « problème d'antibiotique des bots ». Le fait d'envoyer une réponse déterministe aux bots de manière systématique (comme un blocage 403) facilite la tâche aux bots malveillants conçus par des développeurs qui cherchent à sonder, observer et rétro-analyser vos mesures de défense.

Nous en sommes conscients. C'est la raison pour laquelle nous développons des mesures d'atténuation _spécifiquement conçues pour juguler les bots_ , avec différentes approches selon qu'il s'agit de bots malveillants ou de bots utiles. Nous pouvons diviser ces dernières en trois :

Approche 1 : imprévisibilité et actions aléatoires. L'application de réponses aléatoires au trafic soupçonné d'être automatisé (bloquer, proposer un test ou autoriser) casse la logique de reprise automatique et l'empreinte numérique d'un bot.

Approche 2 :[ Labyrinthe IA](https://developers.cloudflare.com/bots/additional-configurations/ai-labyrinth/), une réponse défensive qui piège les bots non autorisés dans un labyrinthe sans fin de pages web générées par IA. Cette approche permet d'épuiser les ressources de calcul et d'exploration des bots malveillants en _trompant_ ces derniers. Selon leurs préférences, les propriétaires de sites disposeront de trois options en ce qui concerne le Labyrinthe IA :

  * **Labyrinthe** : cette option génère une toile infinie de pages liées que les bots doivent suivre.
  * **Résumé** : cette option adresse le résumé d'une page généré par LLM aux robots d'exploration. Ce résumé semble véritable, mais s'avère totalement inutile en tant que données d'entraînement pour l'IA.
  * **Poison** : cette option diffuse des contenus délibérément faux (comme des prix ou des stocks fictifs) à un bot afin de polluer les données qu'il collecte à des fins d'entraînement de l'IA.



Approche 3: mise en file d'attente des bots utiles. Tout le trafic agentique n'est pas intrinsèquement mauvais. La mise en file d'attente gère le débit pour le trafic automatisé légitime (comme les agents d'achat dirigés par un utilisateur) sans leur refuser complètement l'accès au service.

Ces mesures de protection avancées spécifiques aux bots devraient être déployées et disponibles vers la fin de l'année. Les propriétaires de sites web pourront alors choisir le niveau de rigueur souhaité pour leurs mesures.

Nous savons également qu'une défense efficace est prédictive : elle apprend et se corrige d'elle-même sans nécessiter la participation de plusieurs experts en sécurité pour réagir de manière réactive à la dernière attaque furtive. Cette approche s'apparente à un système de règles « jetables », au sein duquel l'ensemble de règles est intrinsèquement dynamique. Cet aspect est voulu : si les attaques évoluent en permanence, les mesures de défense doivent également évoluer. C'est pourquoi nous travaillons pour conserver une longueur d'avance à la fois pour nos mesures de détection et pour nos mesures d'atténuation.

## **Mettre en place l'écosystème de confiance qui fonctionne pour vous**

Tout le monde peut prendre des mesures pour définir de quelle manière les agents automatisés interagissent avec leur infrastructure. 

Voici quelques pistes à essayer :

  * Activez le service[ Precursor](https://developers.cloudflare.com/cloudflare-challenges/precursor/#get-started)
  * Amusez-vous avec l'outil[ Precursor Trace](https://integrityand.trust.cfdata.org/precursor-trace/)
  * Explorez la solution[ BotBase](https://developers.cloudflare.com/bots/botbase/)



En nous éloignant des mesures de vérification statiques et ponctuelles, ainsi qu'en adoptant un processus d'évaluation continu de la confiance, nous réduisons le champ du jeu du chat et de la souris avec les exploitants de bots. Si vous n'utilisez pas encore le[ service de détection des bots Cloudflare](https://www.cloudflare.com/products/bot-mitigation/), découvrez-le et mettez en place l'écosystème de confiance qui vous convient.

]]>01KZWJ9G1CNPPQCMK92X02M4VMRapport Cloudflare sur les menaces DDoS au premier semestre 2026 : les attaques atteignant les 1 Tbit/s augmentent à l'heure où les floods DNS et les tensions géopolitiques propulsent une nouvelle vaguehttps://blog.cloudflare.com/fr-fr/ddos-threat-report-2026-h1/ Thu, 13 Aug 2026 03:15:00 GMTLors du premier semestre 2026, Cloudflare a détecté une augmentation de 519 % des attaques DDoS hypervolumétriques sur son réseau. Ces attaques étaient en grande partie conduites par l'entremise de vecteurs de réflexion DNS et CLDAP. Le présent rapport analyse la manière dont les grands conflits géopolitiques ont remodelé le paysage mondial des cybermenaces.AttaquesAttaques DDoSCloudforce OneRadarThreat ReportBienvenue dans la 25e édition du rapport Cloudflare sur les menaces DDoS. Cette édition constitue la première publication semestrielle de la série. Ainsi, plutôt que de publier des rapports distincts pour le premier et le deuxième trimestre 2026, nous avons compilé notre examen des deux trimestres sous un volume unique couvrant la période qui s'étend de janvier à juin 2026. L'analyse est signée [Cloudforce One](https://www.cloudflare.com/cloudforce-one/), notre organisme d'informations sur les menaces, et propose une étude complète du panorama évolutif des menaces liées aux [attaques par déni de service distribué](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/) (DDoS, Distributed Denial of Service) sur la base des données provenant du [réseau Cloudflare](https://www.cloudflare.com/network/).

## Informations essentielles

  1. Le club du Tbit/s s'est agrandi. Cloudflare a atténué un total de 935 attaques DDoS sur la couche réseau dépassant les 1 Tbit/s au cours du premier semestre 2026 et a constaté une augmentation de 519 % du nombre de ces attaques entre le premier et le deuxième trimestre. 
  2. Le centre de gravité du vecteur d'attaque est passé des floods par botnet aux attaques par réflexion et amplification. Les attaques basées sur le DNS représentaient 34,3 % de l'ensemble des activités de la couche réseau au cours de la première moitié de l'année 2026, avec les [floods DNS](https://www.cloudflare.com/learning/ddos/dns-flood-ddos-attack/) passés de 25,7 % à 40,0 % des attaques sur la couche réseau d'un trimestre à l'autre. Les [floods CLDAP](https://blog.cloudflare.com/reflections-on-reflections/) ont bondi de 580 % d'un trimestre sur l'autre pour devenir le troisième vecteur au deuxième trimestre.
  3. La géopolitique et les événements mondiaux influencent le paysage des menaces. Le secteur des médias, de la production et de l'édition a conservé la première place du classement des secteurs les plus visés sur les deux trimestres, avec 14,2 % de l'ensemble des requêtes HTTP atténuées dans le cadre d'une attaque DDoS, tandis que la couverture de l'Iran, de l'Ukraine et de la Coupe du Monde a attiré une attention soutenue. Parallèlement, la Turquie est devenue le troisième pays le plus visé par les attaques dans le cadre du sommet de l'OTAN qui s'est déroulé en juillet à Ankara. Le secteur public, quant à lui, est passé de la 29e à la neuvième place pendant l'opération Epic Fury, soit le plus grand mouvement sectoriel de l'année 2026 à ce jour.



## Le premier semestre en chiffres : 5 300 attaques DDoS par heure

À mi-parcours de l'année, Cloudflare a déjà atténué 23,2 millions de requêtes au niveau du réseau et 29 640 milliards de requêtes HTTP liées à une attaque DDoS. Ces chiffres représentent environ 5 343 attaques DDoS au niveau du réseau par heure, soit près de 128 000 chaque jour.

### Pic d'avril et démantèlements d'opérations par les autorités

Le mois d'avril 2026 s'est révélé un mois de pic pour l'activité et le volume des attaques DDoS, avec un pic atteignant respectivement 6,46 milliards de requêtes et 165 pétaoctets (Po). Pour mettre ces chiffres en perspective, il s'agit là d'une quantité de trafic gigantesque, qui équivaut à la diffusion continue de vidéos en 4K pendant des années, ou à environ la quantité de données traitées par les principales plateformes vidéo en une seule journée. Le déclin du nombre de requêtes et des volumes survenu par la suite pourrait refléter [l'Opération PowerOFF](https://www.europol.europa.eu/media-press/newsroom/news/europol-supported-global-operation-targets-over-75-000-users-engaged-in-ddos-attacks), une action menée par 21 pays qui a ciblé plus de 75 000 utilisateurs recourant aux plateformes de DDoS à la demande, a fermé 53 domaines, émis 25 mandats de perquisition et entraîné quatre arrestations.

### Les attaques hypervolumétriques ont connu une augmentation d'un facteur supérieur à 6

Les attaques DDoS hypervolumétriques, c'est-à-dire les attaques définies comme dépassant 1 térabit par seconde (Tbit/s), 1 milliard de paquets par seconde (Gp/s) ou 1 million de requêtes par seconde (Mr/s), se sont révélées une catégorie en pleine croissance dans les rapports Radar. L'annonce 2026 ne s'annonce pas différente. Au cours du deuxième trimestre, Cloudflare a atténué 805 attaques sur la couche réseau dépassant 1 Tbit/s, soit une augmentation de plus de six fois par rapport au trimestre précédent.

## Caractéristiques de l'attaque : faible intensité et lente

Malgré une croissance de l'hypervolumétrique, l'attaque DDoS médiane atténuée par Cloudflare lors du premier semestre 2026 est demeurée courte et de faible ampleur, avec 96,62 % des attaques au niveau du réseau restant sous la barre des 500 Mbit/s, tandis que 90,60 % des attaques se terminent en moins de 10 minutes. L'expression « de faible ampleur » s'avère néanmoins tout à fait relative et la plupart des propriétés Internet ne seraient pas en mesure de résister à ces attaques plus modestes. En termes pratiques:

  * Une attaque de 100 Mbit/s suffit à submerger un serveur ou un site web
  * Une attaque de 100 Gbit/s peut mettre hors ligne la plupart des datacenters non protégés
  * Une attaque de plus de 1 Tbit/s figure parmi les plus massives jamais enregistrées et met à l'épreuve toutes les infrastructures, même l'infrastructure majeure du réseau Internet



Les acteurs malveillants mélangent parfois les couches d'attaque : un débit de paquets élevé (Mp/s, Gp/s) avec une bande passante relativement faible (Gbit/s), ou vice versa, pour exploiter les différentes faiblesses des équipements réseau physiques par opposition à la capacité de la bande passante.

En outre, comme le souligne le graphique ci-dessous, la plupart des attaques DDoS se révèlent d'une durée étonnamment courte. La durée d'action des attaques, même les attaques hypervolumétriques les plus massives, peut être mesurée en secondes plutôt qu'en minutes. Nous avons ainsi observé [des attaques record qui n'ont duré que 35 secondes](https://blog.cloudflare.com/ddos-threat-report-for-2025-q1/#hyper-volumetric-attacks-continue-spill-into-q2) du début à la fin. Qu'une attaque dure trente secondes ou dix minutes, il n'existe pas de fenêtre pratique pour l'intervention humaine : le temps qu'une alerte parvienne à un analyste de la sécurité, l'attaque est déjà terminée. Les solutions d'atténuation manuelle et à la demande sont simplement trop lentes pour faire face à cette réalité. Si l'attaque peut elle-même être brève, ses répercussions ne le sont toutefois pas. Les effets en cascade d'un brusque pic d'attaque peuvent déclencher une instabilité au niveau du routage, des retransmissions TCP, des délais d'expiration des applications et une dégradation des services en aval qui nécessiterait des heures ou des jours pour être complètement résolue, tout en maintenant les services à l'arrêt ou diminués. Une protection automatisée et active en permanence n'est pas une commodité dans le paysage de menaces actuel : c'est une nécessité.

## Les secteurs les plus visés

### L'opération Epic Fury et le pic des attaques sur le secteur public

Le 28 février 2026, Israël et les États-Unis ont lancé l'opération Epic Fury, une série de frappes contre les dirigeants et les infrastructures de l'Iran. Le panorama des attaques DDoS a réagi en l'espace de 72 heures et les [chercheurs en sécurité](https://thehackernews.com/2026/03/149-hacktivist-ddos-attacks-hit-110.html) ont enregistré 149 revendications d'attaques DDoS de la part d'hacktivistes contre 110 entreprises et organisations distinctes dans 16 pays. Près de 47,8 % de l'ensemble des entreprises et organismes ciblés dans le monde appartenaient au secteur public.

Alors que les rapports publics ont documenté un ciblage étendu des administrations pendant cette période, le secteur a vu sa position dans le classement bondir de 20 places, en passant de la 29e place au premier trimestre à la neuvième place au deuxième trimestre en termes de part du nombre de requêtes HTTP atténuées dans le cadre d'une attaque DDoS. Bien que cette position se soit tenue loin du top 10 pendant la majeure partie de la période, cette augmentation représente néanmoins l'un des plus grands bonds dans le classement des secteurs.

### Les médias en état de siège : le secteur le plus visé

Au milieu des conflits en Iran et en Ukraine, mais aussi de l'enthousiasme autour de la Coupe du Monde, le secteur des médias, de la production et de l'édition s'est révélé le plus visé par les attaques lors des deux trimestres, avec une part de 14,2 % du nombre de requêtes HTTP atténuées dans le cadre d'une attaque DDoS, soit près de quatre fois plus que le secteur en seconde position.

## Les pays les plus visés

Le panorama des attaques DDoS survenues au premier semestre 2026 a vu à la fois des noms familiers et un remaniement dans le classement des endroits les plus attaqués à travers le monde. La Chine a terminé le premier semestre en tant que pays le plus visé par les attaques, après avoir absorbé 22,4 % de l'ensemble des requêtes HTTP atténuées dans le cadre d'une attaque DDoS à travers le monde lors du deuxième trimestre. Le maintien des États-Unis à la deuxième place (18,8 %) démontrant l'attrait persistant des acteurs malveillants pour ce pays.

La Turquie a connu une rapide augmentation du nombre d'attaques, avec une part du trafic hostile mondial qui a plus que doublé pour atteindre la troisième position des pays les plus attaqués au deuxième trimestre. Cette hausse a coïncidé avec la préparation du sommet de l'OTAN qui s'est tenu à Ankara en juin et début juillet 2026, lorsque les forces de sécurité turques ont mené [plusieurs raids de grande envergure avant le sommet](https://apnews.com/article/turkey-nato-summit-suspects-detained-864260d7cbe9ca73cd05115cd638ee93) dans tout Ankara et arrêté au moins 209 personnes.

## Principaux pays sources d'attaques

Le Brésil a dépassé les États-Unis en tant que principal pays source d'attaques DDoS au premier semestre 2026, avec une part de 14,9 % contre 13,4 %, en raison d'une forte augmentation survenue au deuxième trimestre lorsque le Brésil est devenu le pays source de 21,4 % de l'ensemble du trafic DDoS atténué. L'Indonésie est restée à la troisième place lors des deux trimestres et a ainsi prolongé sa série de plusieurs trimestres en tant que l'un des trois principaux pays sources d'attaques DDoS à l'échelle mondiale. 

## Vecteurs d'attaque

### Les attaques par flood DNS prédominent

Les attaques basées sur le DNS ([flood DNS](https://www.cloudflare.com/learning/ddos/dns-flood-ddos-attack/) et [attaques par amplification DNS](https://www.cloudflare.com/learning/ddos/dns-amplification-ddos-attack/)) ont totalisé 34,3 % des attaques sur la couche réseau au cours du premier semestre 2026. Les deux mécanismes sont liés, mais restent néanmoins distincts : une attaque par flood DNS utilise le volume brut de requêtes d'un botnet directement à l'encontre des serveurs DNS de référence d'une victime afin d'épuiser leur capacité de traitement des requêtes (le « répertoire » du domaine devient dès lors injoignable et chaque service qui en dépend s'effondre). Les attaques par amplification DNS envoient plutôt de petites requêtes à partir d'une adresse IP [usurpée](https://www.cloudflare.com/learning/ddos/glossary/ip-spoofing/) vers des [résolveurs DNS](https://www.cloudflare.com/learning/dns/dns-server-types/) ouverts, qui répondent par des enregistrements beaucoup plus volumineux (souvent déclenchés par une requête ANY) vers l'adresse usurpée de la victime. 

### Les attaques CLDAP explosent : augmentation de 580 % des attaques par amplification

Le flood CLDAP, un vecteur d'attaques par réflexion et par amplification qui exploite les points de terminaison LDAP-over-UDP Active Directory exposés, a augmenté de 580 % d'un trimestre sur l'autre, pour devenir le troisième vecteur au deuxième trimestre. Le protocole CLDAP ([Connectionless Lightweight Directory Access Protocol](https://datatracker.ietf.org/doc/html/rfc1798)) est une variante du protocole LDAP ([Lightweight Directory Access Protocol](https://datatracker.ietf.org/doc/html/rfc4511)), qui sert à interroger et modifier les services d'annuaire exécutés sur des réseaux IP. Sans connexion et reposant sur le protocole UDP plutôt que sur le TCP, le CLDAP se montre dès lors plus rapide, mais moins fiable. De même, comme il s'appuie sur l'UDP, il ne comporte aucune exigence de négociation préalable. Les acteurs malveillants peuvent donc usurper l'adresse IP et l'exploiter comme vecteur de réflexion. Les attaques CLDAP fonctionnent en envoyant de petites requêtes issues d'une adresse usurpée aux contrôleurs de domaine accessibles sur le port UDP 389. Les serveurs répondent à la source usurpée (c'est-à-dire la victime) par des réponses d'une taille des dizaines, voire des centaines, de fois supérieure à celle de la requête initiale et submergent ainsi l'hôte victime. 

## Renforcer les défenses mondiales et aider à protéger Internet

Le réseau Cloudflare est conçu pour absorber ce type de croissance des menaces DDoS. Chaque service de notre réseau est protégé par une [protection DDoS gratuite et illimitée](https://www.cloudflare.com/ddos/) exécutée [dans chacune des plus de 330 villes d'implantation de notre réseau mondial](https://www.cloudflare.com/network/), le tout soutenu par une capacité réseau de 500 Tbit/s. L'autonomie est ici la clé : nos systèmes détectent et atténuent les attaques [sans intervention humaine](https://developers.cloudflare.com/ddos-protection/about/). Or, cette particularité s'avère nécessaire, car les acteurs malveillants lancent régulièrement des attaques dépassant les 1 Tbit/s à une cadence de plusieurs centaines par trimestre.

  


Nous tirons parti de la position avantageuse de Cloudflare pour aider les fournisseurs d'hébergement, les plateformes d'informatique cloud et les fournisseurs d'accès Internet à identifier et à éliminer les adresses IP/comptes malveillants à l'origine des attaques DDoS en leur proposant notre [flux d'informations gratuit sur les menaces liées aux botnets](https://developers.cloudflare.com/ddos-protection/botnet-threat-feed/) (DDoS Botnet Threat Feed for Service Providers). 

Plus de 800 réseaux à travers le monde entier se sont inscrits à ce flux et nous avons déjà constaté une excellente collaboration s'établir au sein de la communauté pour éliminer les nœuds de botnets.

## À propos de Cloudforce One

Portée par une mission visant à défendre Internet, l'équipe de [Cloudforce One](https://www.cloudflare.com/cloudforce-one/) tire parti des données télémétriques du réseau mondial Cloudflare (qui protège plus de 20 % du web) afin de soutenir la recherche sur les menaces et d'assurer une réponse opérationnelle, deux axes qui permettront par la suite de protéger les systèmes essentiels de millions d'entreprises à travers le monde.

]]>01KZWHGD4XP4AK6FJAK027VVKZBâtir un Internet agentique ouvert : lisible, découvrable, accessible et payablehttps://blog.cloudflare.com/fr-fr/the-agentic-internet/ Wed, 12 Aug 2026 03:55:31 GMTLes agents sont un nouveau type de visiteur. Ils n’exécutent pas de CSS et ne cliquent pas sur les publicités ; toutefois, à l’autre bout de la chaîne se trouve un utilisateur humain disposant d’un moyen de paiement. Si vous les bloquez, vous bloquez votre client. Nous développons des outils et des protocoles ouverts, afin que les éditeurs et les agents puissent coopérer, plutôt que de s’affronter.AgentsAgents WeekDéveloppeursIAMCPPlateforme pour développeursNos données indiquent qu’une grande partie du trafic généré par des bots légitimes consiste à [​récupérer une nouvelle fois des pages qui n’ont pas été modifiées](https://blog.cloudflare.com/making-ai-search-smarter/). Des milliards de requêtes, d’immenses efforts réalisés par des machines, sans aucun résultat : c’est la signature d’un web conçu pour les humains, mais consulté par d’autres entités.

Les agents sont ici – et ils n’incarnent pas un nouveau type de logiciel, mais un nouveau type de visiteur sur Internet.

Le web redessiné autour de ce nouveau visiteur est ce que nous appelons l’Internet agentique. Nous voyons son avenir comme un espace lisible, découvrable, appelable et payable. Et pour concrétiser cet avenir, il doit disposer d’outils et de protocoles spécifiques.

La plateforme pour développeurs de Cloudflare a offert un environnement d’exécution pour les agents, ainsi que les premiers outils nécessaires à leur développement. Ce qui manque, ce sont des outils qui permettent aux agents et aux propriétaires de domaines de coopérer, plutôt que de s’opposer – sur l’Internet ouvert, et pas seulement sur une même plateforme.

Tous les navigateurs se sont toujours identifiés sur Internet avec un en-tête appelé « User-Agent ». Ce nom ne prenait tout son sens que lorsque vous compreniez que le navigateur agissait en votre nom. Désormais, un agent utilisateur est véritablement un agent de l’utilisateur : un programme qui récupère des contenus web pour le compte d’un opérateur humain. Aujourd’hui, dans sa forme la plus aboutie, c’est un agent de codage qui lit et écrit du code, extrait les documents dont il a besoin et ne voit jamais les pages qu’il lit.

Un agent n’exécute pas votre CSS, ne voit pas votre image principale et ne clique pas sur vos publicités. Toutefois, à l’autre bout de la chaîne se trouve un utilisateur humain disposant d’un moyen de paiement. Désormais, chaque requête coûte de l’argent à quelqu’un et répond à un objectif précis. Si vous bloquez l’agent, vous bloquez votre client ; et si vous traitez l’agent comme un bot d’extraction de contenu, vous perdez votre client.

Chaque agent existe parce que quelqu’un, qu’il s’agisse d’un opérateur humain ou d’une entreprise, paie pour utiliser ses services. La plupart des utilisateurs ne dépensent pas des jetons juste pour le plaisir. Cette version d’Internet, où chaque requête aboutit à un résultat et à une facture, ne ressemblera en rien à celle que nous connaissons aujourd’hui.

L’Internet n’a pas été conçu à cette fin, pas plus que vos outils d’analyse de données ; et, dans la plupart des cas, votre modèle opérationnel non plus. La manière dont les agents lisent, découvrent, appellent et paient déterminera si l’Internet restera ouvert ou s’il sera fermé. Dans une vision de l’avenir, une poignée d’infrastructures interconnectées contrôlent la découverte, l’identité et les paiements, et tous les autres acteurs transitent inévitablement par eux. Dans un autre scénario, l’Internet reste ouvert : des composantes primitives reposant sur des standards que chacun peut mettre en œuvre, qui s’exécutent sur une infrastructure neutre, puisque le code est public.

Cloudflare croit en l’Internet ouvert, et nous sommes en position de contribuer à construire un futur où cette version d’Internet pourra prospérer.

Les spécifications sur lesquelles nous nous appuyons sont des standards ouverts que chacun peut mettre en œuvre : x402, MCP, Web Bot Auth, PACT. Les propriétaires de domaines choisissent eux-mêmes leurs fournisseurs d’identité, leurs prestataires de paiement et leurs partenaires agents. Cloudflare est une option parmi d’autres, pas l’ensemble de l’infrastructure. Nous sommes le « client zéro » des infrastructures qu’utilisent nos clients ; nous ne bénéficions d’aucun accès privilégié et ne disposons d’aucune API en accès anticipé à laquelle nous seuls aurions accès. C’est le travail que nous accomplissons depuis quinze ans pour l’Internet humain, et c’est celui que nous avons l’intention de mener à bien pour l’Internet agentique.

Ce n’est pas l’aspect technique qui retiendra l’attention des utilisateurs de l’Internet agentique. Ils découvrent un nouvel environnement, et ils le jugeront de la même manière qu’ils ont jugé Internet : en évaluant s’il est meilleur. Si la recherche et la réservation d’une table ne nécessitent qu’un échange, plutôt que neuf ; s’ils savent à qui ils ont affaire, ou s’ils peuvent effectuer un paiement en confiance.

## **Notre philosophie : un Internet agentique lisible, découvrable, appelable et payable**

Tout commence par l’identité. [​Web Bot Auth](https://blog.cloudflare.com/web-bot-auth/) permet à un bot de s’identifier de manière cryptographique auprès de tout site qu’il visite, afin que les éditeurs puissent choisir qui ils souhaitent accueillir ou non ; ainsi, fini les conjectures et fini les agents utilisateur falsifiés. De nombreux sites connaissent déjà l’identité de l’utilisateur humain à l’origine d’une requête, grâce à ses identifiants de connexion, à son comportement dans l’application ou à son historique d’achats. Ce site peut alors délivrer des [​jetons PACT](https://cloudflare.net/news/news-details/2026/Cloudflare-Collaborates-With-Leading-Browsers-to-Develop-a-Privacy-First-Protocol-For-the-Global-Internet/default.aspx) (Private Access Control Tokens). Annoncé en partenariat avec Mozilla, Google, Microsoft et Shopify, le standard PACT permet aux sites de se porter garants de manière anonyme, afin que l’agent puisse présenter le jeton ailleurs. Les agents légitimes bénéficient ainsi d’un accès plus fluide aux services désirés.

Alors, nous pouvons alors faciliter le travail d’un agent. [​Markdown for Agents](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/) permet aux agents de lire les sites web en consommant moins de jetons et moins de bande passante, tandis que [​WebMCP](https://blog.cloudflare.com/webmcp/) leur offre un moyen natif d’interagir en votre nom. Enfin, des standards tels que [​x402](https://x402.org/) leur permettent de payer directement les revendeurs.

La **lisibilité** est une notion simple. Les agents IA peuvent-ils lire le contenu d’une manière qui leur est propre et qui tire parti de leurs atouts ? Moins un agent consomme de bande passante et de jetons, mieux c’est. Chaque balise HTML affichée à l’intention d’un utilisateur humain qui ne la consultera jamais représente non seulement un gaspillage de puissance de calcul, mais aussi une pollution de la fenêtre contextuelle, que l’agent doit ensuite payer pour ignorer. [​Markdown for Agents](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/) résout ce problème côté serveur.

Côté client, nous avons abordé le développement d’un navigateur en considérant les agents comme des utilisateurs à part entière. Notre nouveau navigateur, [​Kitesurf](http://blog.cloudflare.com/kitesurf), est suffisamment léger pour fonctionner sur des instances Workers, déployées à chaque requête, puis aussitôt supprimées. Il fournit le contenu et les fonctionnalités que requièrent les agents, sans les données superflues propres aux navigateurs traditionnels, conçus pour être utilisés par des opérateurs humains.

La **découvrabilité** est le point de départ de chaque événement économique sur l’Internet agentique. Avant qu’un agent puisse lire une ressource, appeler un outil ou payer une transaction, il doit savoir que cette ressource existe. La recherche n’est qu’une partie du problème, car les agents doivent trouver ce dont ils ont besoin via des interfaces conçues spécialement pour eux, plutôt qu’au travers d’un champ de recherche par mot-clé destiné à un utilisateur humain, qui tape lentement et parcourt les pages de résultats en diagonale. La fonction [​AI Search](https://developers.cloudflare.com/ai-search/) est disponible aujourd’hui, permettant de rendre n’importe quel site public consultable par des agents.

La capacité d’être découvert constitue l’autre partie du problème. Les créateurs de contenu et les propriétaires d’API doivent savoir dans quelle mesure ils sont visibles par les agents. Le service d’optimisation pour moteurs d’agents ([​Agent Engine Optimization, AEO](http://blog.cloudflare.com/aeo)) mesure la visibilité d’une marque auprès de l’ensemble des modèles et des agents qui comptent. Si vous n’êtes pas visible de manière mesurable par les agents qu’utilisent vos clients, vous êtes concrètement hors ligne pour eux. 

C’est la caractéristique **appelable** qui permet aux agents de commencer à agir : réserver une table, renouveler un abonnement ou extraire un rapport. Sur l’Internet humain, ces tâches sont toutes différentes en apparence, car elles ont été conçues pour des opérateurs humains, qui cliquent dessus via des interfaces utilisateur. Un agent qui tente d’ajouter un élément à une liste de tâches doit analyser le code HTML, deviner quel bouton correspond à l’action « Ajouter », générer un clic et espérer que le modèle d’objet de document (Document Object Model, DOM) n’a pas été modifié depuis sa dernière consultation de la page.

[WebMCP](https://blog.cloudflare.com/webmcp/) permet à un site de présenter directement ses actions aux agents via le navigateur :

Le « contrat » de l’outil devient explicite : plus besoin d’analyser le code HTML ni de deviner les champs de formulaire. Puisque les outils s’exécutent directement dans la page, ils réutilisent la session et l’état existants de l’utilisateur. Et [​Code Mode](https://blog.cloudflare.com/code-mode/) va encore plus loin. Les agents raisonnent en code, et l’appel d’outils par l’écriture de code s’avère plus rapide et plus précis que le langage naturel. Puisque les agents interrogent directement des points de terminaison, au lieu d’extraire des informations de pages web, le propriétaire du contenu dispose d’une indication claire concernant les contenus qui sont réellement utilisés. 

Enfin, la caractéristique **payable** constitue, selon nous, l’avenir de l’Internet agentique. Toute transaction économique nécessite, à un moment ou à un autre, un moyen de paiement. Les modèles basés sur la publicité sont en train de s’effondrer ; quant aux modèles fondés sur les licences utilisateur, ils ne fonctionnent plus lorsque l’utilisateur est un programme informatique. Les éditeurs dont nous dépendons tous ne peuvent pas se financer avec des consultations de pages qui n’ont jamais lieu et des navigateurs qui n’affichent pas leurs publicités. 

En revanche, un site de recettes qui n’a jamais été rentable grâce à la publicité peut facturer une fraction de centime par requête et devenir rentable à l’échelle de l’Internet agentique. Un journal local peut concéder des licences sur ses articles au moment de la lecture, sans accord de licence préalable ni identifiant. De l’autre côté, l’agent se présente avec un portefeuille et un budget établi une fois pour toutes par un utilisateur humain. 

Chaque interaction payante entraîne la création d’un reçu. L’éditeur peut prouver quel agent a consulté quelle page. L’agent peut prouver qu’il a payé les ressources qu’il a utilisées. Les portefeuilles [​Wallets](https://blog.cloudflare.com/wallets/) permettent aux agents de payer facilement le contenu et les API, tandis que [​Monetization Gateway](https://blog.cloudflare.com/monetization-gateway/) permet aux propriétaires de domaines d’accepter les paiements d’agents en quelques clics.

Cloudflare se situe intrinsèquement au cœur de cet écosystème. Nous jouons déjà un rôle d’intermédiaire entre des milliards d’internautes et les sites qu’ils consultent, en les protégeant, en les accélérant et en garantissant leur disponibilité. Les agents modifient la nature du trafic, mais pas celle de notre activité : nous constituons la couche neutre et performante sur laquelle les éditeurs, les revendeurs, les développeurs d’agents et les utilisateurs finaux peuvent tous compter pour agir dans leur intérêt, et non chercher à les concurrencer. 

Nous voulons donner aux propriétaires de domaines les outils nécessaires pour leur permettre de valoriser les agents IA qu’ils souhaitent soutenir et de [​bloquer ceux dont ils ne veulent pas](https://blog.cloudflare.com/cloudflare-ai-audit-control-ai-content-crawlers/). Un outil pour développeurs a tout intérêt à devenir [​compatible avec les agents](http://blog.cloudflare.com/aeo) pour inciter les agents IA à le découvrir, à le recommander et à le payer. Un éditeur peut vouloir bloquer les agents IA extractifs, qui consomment des ressources sans rien donner en retour, tout en autorisant les ceux qui utilisent son contenu sous licence ou le rémunèrent. Un fournisseur de données à but non lucratif peut vouloir bloquer les bots ou les utilisateurs qui dépassent ses plafonds de requêtes, tout en leur permettant de payer pour lever le blocage et en utilisant ces fonds pour couvrir la surconsommation de ressources.

## **Les bots sont morts, longue vie aux bots**

La frontière entre [​un bot et un humain n’est plus aussi nette](https://blog.cloudflare.com/past-bots-and-humans/). Il ne s’agit plus simplement d’opposer les mauvais bots et les bons humains, ni de dénoncer les bots qui dilapident des ressources destinées à être consommées par des opérateurs humains. C’est une vision dépassée, qui n’a plus sa place dans le monde des agents.

Nous considérons les agents comme un nouveau type d’acteur. Leurs actions peuvent être bénéfiques, par exemple, lorsqu’ils lisent du contenu de manière à préserver les ressources, interagissent avec les sites web conformément aux consignes des propriétaires de domaines et paient pour les ressources qu’ils consomment. À l’inverse, leurs actions peuvent être préjudiciables, comme lorsqu’ils extraient des millions de pages sans contrepartie, tentent de contourner des blocages ou ignorent le fichier [​robots.txt](https://www.cloudflare.com/learning/bots/what-is-robots-txt/). Nous pensons que bon nombre de ces comportements préjudiciables diminueront, voire se transformeront en actions bénéfiques, si nous fournissons aux humains et aux bots les outils pertinents.

## **Combler le déficit de recettes**

Cloudflare possède des années d’expérience dans la détection des bots, et permet désormais aux propriétaires de domaines de reprendre le contrôle de l’accès des bots à leur site. Il manquait cependant l’autre volet : la manière dont les agents interagissent avec ces sites une fois qu’ils ont l’autorisation d’y accéder. C’est la finalité de cette suite d’outils agentiques : rendre le web lisible, découvrable, appelable et payable. Ces quatre composantes fondamentales reposent toutes sur des standards ouverts ; ainsi, aucune entreprise ne détient l’infrastructure. 

Un Internet agentique ouvert nécessite de la diversité des deux côtés ; pas seulement chez les éditeurs et les créateurs de contenus, mais également du côté des agents. Si la demande se trouve concentrée entre les mains de quelques acteurs, peu importe à quel point l’offre est ouverte : l’Internet demeurera un jardin clos.

Nous bâtissons cette alternative ouverte. Rejoignez-nous [​en préparant votre site pour les agents grâce à notre nouveau tableau de bord](http://blog.cloudflare.com/aeo), et inscrivez-vous pour suivre l’actualité d’Answer Engine Optimization, notre solution d’optimisation pour moteurs de réponses. Que vous gériez un site ou un agent, vous pouvez expérimenter toutes ces nouvelles technologies d’Internet dans notre environnement [​AI Playground](https://playground.ai.cloudflare.com/).

]]>01KZT1MGN6T46MBZMAND152A4JDu classement à la recommandation : préparez la prospérité de votre site à l’ère des agents IAhttps://blog.cloudflare.com/fr-fr/aeo/ Wed, 12 Aug 2026 03:46:11 GMTPlus de la moitié des requêtes proviennent désormais de machines, et non d’utilisateurs humains. L’indicateur de préparation aux agents (Agent Readiness) mesure la facilité avec laquelle les agents peuvent parcourir et consulter votre site, tandis que l’indicateur d’optimisation pour les moteurs de réponse (Answer Engine Optimization) suit la fréquence à laquelle les assistants IA vous recommandent.AEOAgentsAgents WeekDashboardÉtat de préparation aux agentsIAMCPNouveautés produitsRadarVotre prochain client ne vous trouvera peut-être pas par l’intermédiaire d’un moteur de recherche. Au lieu de cela, il demandera à un assistant IA : « Comment puis-je X ? », « Quel est le meilleur choix pour quelqu’un comme moi ? », « Occupe-t’en à ma place », et un agent trouvera la réponse, évaluera les choix disponibles et agira en son nom. Le moment décisif qui détermine si un client vous choisit se déroule de plus en plus fréquemment dans la réponse d’un modèle, avant même qu’un utilisateur humain ne consulte votre page d’accueil.

Ce public agentique existe déjà : selon nos estimations, moins de la moitié de l’ensemble des requêtes de pages HTML [​provient désormais d’un utilisateur humain](https://radar.cloudflare.com/traffic#bot-vs-human). Toutes ces machines ne sont pas des agents agissant pour le compte d’un utilisateur humain, mais leur proportion augmente rapidement, et ce sont les moteurs de recherche, les assistants d’achat et les outils de recherche qui détermineront quelles entreprises seront trouvées et recommandées. La découvrabilité désignait autrefois le classement sur une page de résultats ; aujourd’hui, elle désigne la capacité de votre site à être trouvé, consulté et recommandé avec confiance par les agents qui guident vos clients.

Les anciens indicateurs, à savoir les clics d’utilisateurs et les consultations de pages, ne dépeignent plus la situation dans son ensemble. Nous avons échangé avec des propriétaires de sites qui scrutaient longuement des journaux d’accès remplis de bots IA, sans toutefois savoir si ces bots étaient capables d’utiliser leur site ou de recommander leurs produits et services à leurs utilisateurs. Deux questions principales nous ont été posées :

  * Les agents peuvent-ils vraiment utiliser mon site ?
  * Les agents me recommandent-ils ?



Pour aider les propriétaires de sites à répondre à ces questions, nous avons intégré nos [​travaux antérieurs sur l’indicateur de préparation aux agents (Agent Readiness)](https://blog.cloudflare.com/agent-readiness/) dans le tableau de bord Cloudflare, et nous y avons également ajouté notre nouvel outil d’optimisation pour les moteurs de réponse (Answer Engine Optimization, AEO). Ces outils considèrent les agents comme une base d’utilisateurs essentielle de votre site ; ils vous montrent comment un agent le perçoit et à quelle fréquence votre site sera recommandé.

C’est une opportunité à la fois importante et très accessible, car la plupart des sites ne sont pas encore adaptés à ce type d’utilisateur. Tout comme les débuts du référencement naturel favorisaient les sites construits pour les moteurs de recherche, cette nouvelle ère favorisera les sites construits pour les agents. Les agents recommanderont les sites fiables, faciles à trouver et à consulter.

## **Diagnostics : votre site est-il prêt pour les agents ?**

Diagnostics représente la vérification technique de votre site, intégrée à l’indicateur de préparation aux agents (Agent Readiness). Le service analyse votre site comme le ferait un agent : il vérifie s’il est autorisé à y accéder et s’il peut explorer votre contenu, il récupère une copie propre et lisible par machine, puis il identifie les interfaces qu’il peut appeler. 

Tandis qu’un utilisateur humain charge simplement votre page d’accueil, un agent examine votre fichier robots.txt, votre plan du site, vos en-têtes de réponse, une version Markdown de votre contenu ainsi que les métadonnées publiées à des fins d’authentification et d’utilisation d’outils.

Diagnostics effectue ces vérifications sur un nom d’hôte et compile les résultats dans une vue unique récapitulant l’état de préparation aux agents, allant de « Not Ready » (non prêt) à « Fully agent-native » (intégralement agent-native). Chaque vérification est associée à un résultat (réussite, échec ou neutre), accompagné d’un commentaire expliquant pourquoi ce résultat est important, ainsi qu’à un historique des opérations présentant la requête et la réponse exactes que nous avons observées.

Les vérifications sont regroupées par type d’intervention requise, ce qui vous permet de comprendre par où commencer :

  * Approches rapides : les éléments fondamentaux transformateurs qui font défaut à la plupart des sites, parmi lesquels un fichier robots.txt lisible par les robots d’indexation, un plan de site XML, des règles pour les robots d’indexation pilotés par IA et la mise à disposition de contenu Markdown « propre » aux agents
  * Fondements techniques : la couche suivante, qui comprend les signaux de contenu (Content Signals) précisant les modalités d’utilisation de votre contenu, un catalogue d’API, des en-têtes de liens et des instructions de connexion destinées aux agents
  * Intégration avancée : les fonctionnalités agent-natives, notamment la découverte OAuth, les cartes d’agent MCP (Model Context Protocol) et A2A (Agent2Agent), un index de compétences, Web Bot Auth et WebMCP
  * Commerce : les standards émergents de paiement pour agents, parmi lesquels [​x402](https://blog.cloudflare.com/x402/) (une extension du code d’état HTTP 402 Payment Required), ACP (Agent Commerce Protocol), UCP (Universal Commerce Protocol) et AP2 (Agent Payments Protocol). Il s’agit pour l’instant d’une information à titre indicatif, qui n’est pas prise en compte dans votre score.



Chaque suggestion d’amélioration est accompagnée d’une étape suivante. Lorsqu’une fonctionnalité de Cloudflare peut s’avérer utile, un lien « Set up in Cloudflare » (Configurer dans Cloudflare) vous redirige directement vers le paramètre correspondant ; par exemple, pour activer Markdown for Agents ou un déploiement géré du fichier robots.txt. Pour tous les autres aspects, un bouton « Copy Agent Prompt » (Copier le prompt pour l’agent) fournit les informations dont votre agent de codage a besoin pour poursuivre le développement. Effectuez la modification, effectuez une nouvelle analyse et regardez la coche devenir verte.

## **AEO : les assistants IA recommandent-ils votre site ?**

Diagnostics vous indique si les agents peuvent accéder à votre site. L’onglet AEO vous indique ce qu’il se passe ensuite : lorsqu’un client pose une question à un assistant IA dans votre catégorie, celui-ci vous recommande-t-il, ou recommande-t-il plutôt un concurrent ? Ce n’est pas quelque chose que vous pouvez consulter comme un classement de résultats de recherche. Il n’y a ni compteur d’impressions, ni rapport sur les clics manqués ; ainsi, lorsqu’un concurrent est cité à votre place, la vente est perdue et rien ne vous permet de savoir que cela est arrivé.

Nous déduisons votre secteur d’activité (par exemple, santé et bien-être) et votre catégorie (par exemple, vêtements de sport) à partir de votre site, puis nous interrogeons les principaux assistants (à l’heure actuelle, Claude d’Anthropic et GPT d’OpenAI) avec des prompts susceptibles d’être formulés par vos clients, afin d’observer leurs réponses. Nous structurons ces prompts de manière à recréer le processus de découverte en conditions réelles, en demandant des recommandations, des comparatifs de produits et des conseils généraux dans votre catégorie. En observant la manière dont les modèles répondent à ces requêtes réalistes, vous obtenez des indicateurs tels que :

  * **Citation Rate** (taux de citation) : la proportion de réponses dans votre catégorie qui citent votre site comme source
  * **Prominence** (importance) : lorsque votre site est cité, quelle proportion de la réponse est en réalité la vôtre et à quel moment elle est affichée
  * **Mention Rate** (taux de mention) : fréquence à laquelle les assistants mentionnent votre marque dans leur réponse ; par exemple, combien de fois le nom « Cloudflare » apparaît dans la réponse, que [​cloudflare.com](http://cloudflare.com) soit ou non cité en tant que source. Considéré parallèlement à l’indicateur Citation Rate (taux de citation), cet indicateur permet de distinguer la notoriété de la reconnaissance : si les assistants vous mentionnent bien plus souvent qu’ils ne vous citent, cela signifie que vous apparaissez bien sur leur radar, mais que vous ne suscitez pas encore de citations. Il s’agit d’une lacune spécifique, sur laquelle vous pouvez intervenir.
  * **Share of Voice** (part de voix) : votre proportion de citations par rapport à celle de vos concurrents ; cela vous permet de voir qui remporte les prompts sur lesquels vous êtes perdant



Pour évaluer comment un modèle IA perçoit votre présence sur le marché, nous établissons une base de référence pour chaque secteur d’activité et chaque catégorie avant d’attribuer une note à un site spécifique. Nous interrogeons les assistants IA avec des prompts pertinents dans cette catégorie, sans mentionner votre marque, et nous enregistrons quels sites sont mentionnés, le moment auquel ils sont affichés et leur visibilité.

Plutôt que d’interroger à nouveau les modèles chaque fois qu’un propriétaire de site lance une analyse, nous exécutons ce panel une seule fois par catégorie et nous réutilisons cette base de référence pour l’ensemble des comptes de ce domaine. Le précalcul de cet ensemble de données offre trois avantages principaux :

  * **Latence nulle** : les résultats s’affichent instantanément depuis un instantané, sans vous obliger à attendre le traitement des requêtes sur le modèle en temps réel.
  * **Réduction de la charge de calcul** : l’agrégation des requêtes par catégorie permet d’éviter les appels IA redondants sur des milliers d’analyses.
  * **Score Industry Fit** : la réutilisation du corpus du panel nous permet de cartographier les marques qui apparaissent systématiquement ensemble, et ainsi, de calculer un score Industry Fit (adéquation au secteur d’activité) qui évalue si un assistant IA consulte votre site parallèlement à ceux de vos concurrents réels.



Les assistants IA répondent rarement deux fois de la même manière à une même question. Pour tenir compte de cette variance, nous utilisons [​Cloudflare AI Gateway](https://www.cloudflare.com/products/ai-gateway/) pour interroger chaque assistant plusieurs fois, via différents modèles. Nous lisons ensuite les réponses telles qu’un client les verrait, c’est-à-dire le texte de la réponse accompagné des sources citées par chaque assistant, et nous en extrayons plusieurs indicateurs. 

Nous évaluons non seulement si votre site a été mentionné, mais aussi si vous avez été cité« comme source, à quel moment vos citations apparaissent dans la réponse et dans quelle mesure le contenu de la réponse finale vous est attribué. Lorsqu’un véritable jugement est nécessaire, Workers AI se charge du plus gros du travail : l’outil s’exécute nativement sur notre infrastructure pour analyser chaque réponse et évaluer de quelle manière vos citations et mentions apparaissent. Nous utilisons également une analyse textuelle précise, plutôt qu’un modèle qui évaluerait lui-même ses propres résultats. Au final, cela permet de transformer des dizaines de réponses individuelles en indicateurs exploitables. En masquant la complexité du pipeline de requêtes et d’évaluation multi-modèles, l’outil fournit des indicateurs sans vous contraindre à développer votre propre cadre d’évaluation.

Parallèlement aux réponses, l’indicateur AI Operator Activity affiche le trafic réel d’indexation et de redirection sur votre site, réparti par opérateur (OpenAI, Google, etc.) : qui consulte votre contenu, qui renvoie des visiteurs vers vous et les erreurs rencontrées pendant la consultation (403 Forbidden, 404 Not Found). Le modèle qui mérite que vous vous y intéressiez est celui d’un opérateur qui explore des milliers de pages de votre site, mais ne redirige aucun visiteur vers celui-ci, utilisant ainsi votre travail sans renvoyer de clients vers vous.

Dans la mesure où ces chiffres sont propres à votre site, vous pouvez expérimenter, exécuter une nouvelle analyse et mesurer l’impact sur les requêtes précises qui génèrent de l’activité pour votre entreprise.

## **Découvrez votre autre public**

Jusqu’à présent, l’évaluer de l’impact des agents relevait de la conjecture : il fallait filtrer les journaux avec la commande grep pour tenter d’identifier les visiteurs de votre site ou transmettre un prompt à un chatbot et vérifier à l’œil nu si celui-ci vous mentionnait. Grâce à Agent Readiness et à AEO, toutefois, vous pouvez obtenir les données dont vous avez besoin pour agir. Et puisque les requêtes transitent effectivement par Cloudflare, ces outils mesurent les données plutôt que de les estimer, autant que possible, et leur précision ne fera que s’améliorer avec le temps. 

Vous aider à identifier les visiteurs de votre site et à déterminer comment interagir avec eux selon vos conditions, c’est ce que nous avons toujours fait. Les agents sont simplement le nouveau public, et les entreprises qui aident les agents à facilement les trouver, les comprendre et avoir confiance en elles sont celles que les agents recommanderont. L’indicateur de préparation aux agents (Agent Readiness) vous permet de découvrir si vous faites partie de cette catégorie et, si ce n’est pas encore le cas, comment y remédier.

Êtes-vous prêt à découvrir si des agents IA renvoient des clients vers vous ? Accédez à l’onglet Overview (Aperçu) de votre tableau de bord pour améliorer l’état de préparation aux agents de votre site et demander un accès anticipé à AEO Visibility.

_Vous développez des applications sur l’Internet ouvert, prêt pour les agents ? Ouvrez l’onglet**Agent Readiness** du [​tableau de bord Cloudflare](https://dash.cloudflare.com) et venez nous parler de ce que vous créez actuellement sur le [​Discord pour développeurs de Cloudflare](https://discord.cloudflare.com)._

]]>01KZT10R0VN0S8TKW1FWVCBG6KDétecter les comportements indésirables de l’IA grâce aux analyses de données sensibles à l’identitéhttps://blog.cloudflare.com/fr-fr/identity-aware-ai-gateway/ Tue, 11 Aug 2026 08:46:45 GMTLa passerelle AI Gateway sensible à l’identité est désormais disponible en version bêta ouverte. User Insights transforme ce trafic en base de référence comportementale pour chaque utilisateur et chaque agent, et signale les risques internes dès leur apparition.AgentsAgents WeekAI Gateway (FR)DéveloppeursIANouveautés produitsPlateforme pour développeursLorsque vous consultez votre facture d’IA, il peut être difficile de déterminer si quelque chose ne va pas. Vous devez disposer d’une base de référence pour pouvoir observer ce qui a changé, qu’il s’agisse d’un agent qui a dépassé les limites établies ou d’un utilisateur humain dont la consommation a soudainement été multipliée par dix. La capacité d’identifier ces changements est ce qui vous permet de lancer une enquête ; jusqu’à présent, toutefois, ces changements se sont avérés difficiles à détecter.

Savoir qui utilise l’IA et à quelles fins constitue l’un des principaux défis auxquels les entreprises sont actuellement confrontées. [Un rapport d’étude](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf) publié par l’université de Stanford a révélé que 59 % des entreprises considéraient les lacunes de connaissances comme leur principal obstacle à une gouvernance responsable de l’IA. 

Il s’agit là d’un problème de sécurité autant que d’un problème financier. Pour résoudre ces problèmes, deux éléments sont nécessaires : une identité vérifiée à chaque requête (afin qu’un pic d’activité soit associé à un nom précis) et une représentation de ce qui constitue un comportement normal pour cette identité. Aujourd’hui, nous annonçons les deux.

La passerelle AI Gateway sensible à l’identité avec Cloudflare Access est désormais disponible en version bêta ouverte, et User Insights est proposé en disponibilité générale à chaque client de la passerelle AI Gateway, sans coûts supplémentaires. Ensemble, ces services transforment le trafic déjà acheminé à travers AI Gateway en base de référence comportementale pour chaque utilisateur et chaque agent qui l’utilisent, et identifient ceux qui s’écartent de ces valeurs.

## Qu’est-ce qu’AI Gateway ?

[AI Gateway](https://developers.cloudflare.com/ai-gateway/) est le plan de contrôle central pour l’ensemble de vos utilisations de l’IA. Chaque application et chaque équipe ne font plus directement appel aux modèles d’OpenAI, d’Anthropic, de Google ou de Workers AI ; à la place, les requêtes transitent d’abord par AI Gateway, ce qui vous permet de centraliser l’observation, la sécurisation et la gestion de l’ensemble de votre utilisation de l’IA.

Le service s’intègre aux applications que vous développez et aux outils de codage que vos développeurs utilisent déjà au quotidien. Routez les [cadres d’exécution (« harness ») d’agents](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/) tels que Claude Code, Codex et GitHub Copilot via la passerelle AI Gateway pour leur imposer les mêmes règles de visibilité et de contrôle que le reste de vos outils.

## Passerelle AI Gateway sensible à l’identité

L’intégration d’AI Gateway et de [​Cloudflare Access](https://developers.cloudflare.com/ai-gateway/configuration/cloudflare-access) vous permet de placer un [​domaine personnalisé](https://developers.cloudflare.com/ai-gateway/configuration/custom-domains/) devant votre passerelle et de le protéger avec Access, comme n’importe quelle autre application. Vous pouvez ainsi :

  * Vous authentifier avec n’importe quel fournisseur d’identité prenant en charge le protocole SAML, comme Okta ou Entra, ce qui élimine la nécessité de générer et de transmettre des clés API Cloudflare.
  * Définir des politiques régissant précisément les utilisateurs et agents autorisés à accéder à votre passerelle.
  * Transmettre des requêtes vers un nom d’hôte « propre », comme `ai.example.com`, sans inclure d’identifiant de compte ni d’identifiant de passerelle dans l’URL.



Chaque requête authentifiée contient désormais l’identité de l’utilisateur obtenue depuis Access. AI Gateway ajoute l’identifiant d’utilisateur Access vérifié aux métadonnées de la requête, sous la forme `cf.user_id`, ce qui vous permet de filtrer les journaux, les analyses de données et les dépenses en fonction de l’utilisateur humain qui a effectivement émis la requête.

Associée à des [​limites de dépenses](https://developers.cloudflare.com/ai-gateway/features/spend-limits/), cette identité devient un outil de gestion budgétaire. Puisque que chaque requête est désormais associée à un utilisateur réel, vous pouvez définir des limites de dépenses par utilisateur : attribuez à chaque utilisateur sa propre enveloppe budgétaire, puis bloquez les requêtes ultérieures ou basculez vers un modèle moins coûteux lorsque l’utilisateur atteint cette limite. Vous pouvez ainsi en finir avec les factures inattendues et les clés API partagées qui dissimulent les dépenses de chaque utilisateur et agent.

C’est précisément à ce problème que s’est heurté Flexport, l’un des primo-adoptants de notre service.

« Le partage des clés API rend pratiquement impossible l’identification des utilisateurs d’un service IA ou l’application des règles d’accès que nous avons déjà mises en place pour nos collaborateurs, », explique Max Baumgarten, Staff Security Engineer de Flexport. « Déployer Cloudflare Access en amont de la solution AI Gateway permet d’attribuer une identité authentifiée à chaque requête et nous permet d’appliquer nos politiques d’identité existantes au niveau de la passerelle. Nos équipes peuvent adopter des outils IA sans devoir créer un système d’authentification distinct pour chaque client. »

Dans un avenir proche, vous pourrez utiliser les groupes du fournisseur d’identité de vos utilisateurs pour définir des limites de dépenses ou contrôler les modèles auxquels un groupe peut accéder. Vous pourrez, par exemple, permettre à votre équipe chargée de l’apprentissage automatique (Machine Learning) d’accéder à des modèles ultra-performants, plafonner les dépenses de votre équipe d’assistance ou attribuer un budget à tous les utilisateurs travaillant sur un projet spécifique – et cela, en fonction des groupes que vous gérez déjà dans votre fournisseur d’identité.

## Le nouvel onglet User Insights

AI Gateway comporte désormais un onglet intitulé User Insights. User Insights analyse le trafic transitant par votre passerelle et génère un profil comportemental pour chaque compte. Le service analyse le comportement habituel de chaque compte, identifie les comptes qui s’en écartent et fournit les informations contextuelles nécessaires pour différencier un agent malveillant d’un ingénieur très occupé. Il fonctionne avec le trafic qui transite déjà par votre passerelle, et ne nécessite donc aucune configuration ultérieure.

User Insights permet de suivre les coûts, et notamment les sources de gaspillage, à l’image des faibles taux de réussite de mise en cache et des fenêtres contextuelles surdimensionnées. De nombreux outils le font déjà, mais ce qu’ils ne font pas, c’est vous indiquer si un compte se comporte normalement. C’est sur cet aspect que nous avons choisi de nous concentrer, parallèlement à la maîtrise des coûts. 

### Établir une base de référence pour chaque compte : utilisateurs humains et agents

Au fil du temps, chaque compte laisse une empreinte comportementale, qu’il s’agisse d’un utilisateur humain ou d’un agent. Un agent qui publie une synthèse des tickets toutes les trois heures est rigoureux et constant. Un utilisateur humain est plus désordonné : ses prompts sont variés, ses intervalles sont irréguliers et il consacre beaucoup de temps à la résolution de problèmes complexes. Ces deux scénarios d’utilisation sont légitimes ; un même écart peut donc être considéré comme du bruit dans un cas et comme un signal pertinent dans l’autre.

Dans User Insights, nous commençons par attribuer un score aux sessions, et non aux requêtes individuelles. Ici, les seuils absolus ne sont pas adaptés ici : une augmentation de 500 USD chez un utilisateur intensif peut être normale, tandis qu’une session à 50 USD chez un agent qui dépense habituellement 5 USD représente un changement considérable qui pourrait autrement passer inaperçu. Nous comparons donc chaque session à l’historique du compte, en utilisant le coût par session au 95e centile (p95) sur les 30 derniers jours. Cela nous donne une idée du fonctionnement habituel du compte, et toute valeur supérieure à deux fois le p95 du compte constitue un indicateur fort d’un comportement anormal.

L’analyse suivante explique comment nous avons obtenu ces chiffres.

Figure 1 : Détection des anomalies de coût par session

**Comment lire le graphique ci-dessus**

Ce graphique représente des sessions réelles, issues de notre trafic interne. Chaque point correspond à une session distincte (représentée sur une échelle logarithmique) :

  * **Axe X (« Session Cost ») :** coût total en dollars.
  * **Axe Y (« x User p95 ») :** dépassements de la base de référence de l’utilisateur pendant la session.



Les deux lignes de seuil en pointillés permettent de répartir les sessions en quatre catégories :

  * **En haut à droite (étoiles ★) :** dépasse à la fois le double de la base de référence p95 de l’utilisateur et le plafond p99 du compte. Il s’agit de pics relatifs importants, qui correspondent à des dépenses anormales significatives et déclencheront une alerte. 
  * **En haut à gauche :** pic relatif important (double de la valeur p95 de l’utilisateur), inférieur au plafond p99 du compte. Ce comportement n’est pas pris en compte, afin d’éviter le déclenchement d’alertes sur de faible variations du montant en dollars.
  * **En bas à droite :** dépense absolue élevée, mais conforme à l’utilisation généralement intensive de cet utilisateur. Ce comportement est, lui aussi, considéré comme normal et n’est donc pas pris en compte.
  * **En bas à gauche :** l’activité est normale et se situe largement dans les limites des deux bases de référence.



Figure 2 : Répartition des coûts par session au niveau du compte

Cet histogramme (Figure 2) cartographie le coût de chaque session à travers l’entreprise, afin d’établir un plafond au niveau du compte :

  * Utilisation habituelle : la grande majorité des sessions coûtent bien moins de 10 USD, le 95e centile s’établissant à 20 USD.
  * p99 du compte (200 USD) : 1 % seulement de toutes les sessions dans l’ensemble de l’entreprise atteignent ou dépassent 200 USD.



Alors, pourquoi avons-nous choisi le p99 ? Établir notre plafond absolu en dollars au p99 du compte permet de définir un seuil significatif. Cela garantit qu’une anomalie n’est pas un simple changement soudain pour un utilisateur particulier, mais qu’elle figure également parmi les 1 % des sessions les plus coûteuses dans l’ensemble de l’entreprise.

Figure 3 : Historique d’une session d’utilisateur unique

Les bases de référence ne sont pas statiques. À mesure que les habitudes d’un compte évoluent, son p95 glissant (ligne verte) et son seuil 2x (ligne orange) changent en conséquence ; ainsi, une alerte reflète toujours un comportement récent, plutôt qu’une valeur établie une fois pour toutes. Nous appliquons également un seuil minimal en dollars : une augmentation soudaine doit être non seulement statistiquement inhabituelle, mais aussi suffisamment importante pour justifier l’examen par un administrateur. Ce seuil minimal en dollars est ce qui permet d’éviter le déclenchement d’une alerte lorsque le compte d’un micro-utilisateur affiche une augmentation de 500 pour cent, dont le montant ne représente toutefois que quelques cents.

### Le prisme idéal pour détecter les comportements indésirables 

Au terme de toutes les analyses ci-dessus, les administrateurs ont sous les yeux une vue d’ensemble des comptes qui se sont écartés de leur propre modèle de consommation, après filtrage de toutes les données normales. Cette vue filtrée représente un flux de comportements indésirables.

Ce comportement est difficile à détecter, car le signal ne provient jamais d’un nouvel outil ni d’une action bloquée. Il s’agit simplement d’un compte de confiance qui intensifie l’utilisation de ses autorisations existantes. Il peut s’agir d’un compte de service qui commence soudainement à exécuter des sessions plus coûteuses, ou d’un utilisateur humain dont la consommation dépasse largement son modèle habituel et se stabilise à ce niveau pendant plusieurs jours.

Aucune de ces actions n’enfreint une politique, mais toutes s’écartent d’une base de référence comportementale. Un écart soudain par rapport à la consommation habituelle d’un compte est souvent le premier signe observable d’une compromission d’identifiants ou d’un agent présentant une défaillance.

User Insights ne détermine pas l’intention et ne bloque personne ; le service présente simplement à un administrateur les quelques comptes qui ont commencé à afficher un comportement inhabituel, afin que celui-ci puisse poser les questions pertinentes. Parfois, cela mène à une véritable enquête ; et parfois, cela signifie simplement qu’un utilisateur humain a besoin d’être accompagné (comme ce développeur qui colle l’intégralité d’une base de code dans chaque prompt, alors qu’un extrait serait suffisant). 

## Les prochaines évolutions 

### Nous vous aiderons à évoluer du contrôle des coûts à l’optimisation des coûts

Une fois que vous avez défini un budget, la question qui se pose naturellement est, comment obtenir une qualité de production équivalente à moindre coût ? Toutes les requêtes ne nécessitent pas un modèle ultra-performant. Une tâche de synthèse ou une simple complétion de code peut être exécutée sur un modèle moins coûteux, sans altération notable de la qualité.

Nous développons un routage intelligent basé sur des tâches, dans lequel AI Gateway analyse la requête entrante et la redirige vers le modèle qui offre le meilleur résultat au moindre coût. Au niveau de l’entreprise, vous pourrez identifier les domaines dans lesquels vous pouvez réaliser le plus d’économies en routant les requêtes vers des modèles plus efficaces. Le routage intelligent basé sur les tâches est en cours de développement ; nous vous en dirons davantage au fur et à mesure que le projet avancera.

### Nous vous aiderons à comprendre _comment_ l’IA est utilisée

La détection des anomalies indique qu’un compte s’est écarté de son modèle habituel, mais n’explique pas pourquoi. Un administrateur doit encore examiner les journaux et reconstituer le fil des événements. Notre prochaine priorité est de combler cette lacune, et cela commence par déterminer la nature exacte du trafic.

Nous développons un système de classification des prompts qui sépare les requêtes en catégories telles que le codage, la rédaction et d’autres. Ces catégories fournissent le contexte qui fait défaut dans presque tous les autres signaux. Une hausse soudaine des dépenses dans la catégorie « codage » sur le compte d’un ingénieur peut être acceptable, mais cette même augmentation ne l’est pas si elle concerne une catégorie que ce compte n’a jamais utilisée auparavant. La catégorisation peut permettre à une entreprise de comprendre non seulement l’intensité de son utilisation de l’IA, mais également les fins auxquelles elle l’utilise. 

Elle répond également à la question sous-jacente à la plupart de ces discussions : l’utilisation de l’IA est-elle conforme à sa destination initiale ? Une fois que le trafic professionnel a été séparé du reste du trafic, l’utilisation à des fins personnelles devient clairement visible. De l’extérieur, la différence entre une personne qui gère une activité parallèle pendant ses heures de travail et un utilisateur qui extrait discrètement des données de l’entreprise par l’intermédiaire d’un modèle n’est pas perceptible. Or, il est essentiel de les distinguer pour détecter les risques internes. 

Lorsque votre trafic IA transite par AI Gateway, chaque nouvelle catégorie de signal de risque ou d’efficacité constitue un avantage supplémentaire pour l’administrateur, sans nécessiter de configuration supplémentaire.

## Lancez-vous

User Insights est proposé en disponibilité générale à chaque client de la passerelle AI Gateway, sans coûts supplémentaires. Le service est déjà disponible depuis le tableau de bord pour tous les utilisateurs qui acheminent du trafic via la passerelle. Aussi, si vous routez déjà votre trafic via AI Gateway, cette vue est dès maintenant à votre disposition. 

Si vous ne l’avez pas encore fait,[ créez une passerelle](https://developers.cloudflare.com/ai-gateway/get-started/) et commencez à transmettre des requêtes à n’importe quel modèle de notre [catalogue](https://developers.cloudflare.com/ai/models/). 

Nous vous recommandons de déployer AI Gateway derrière [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/policies/access/), désormais disponible en version bêta ouverte. Les vues des dépenses et des anomalies fonctionnent sans cela, mais l’association d’une identité permet de transformer un identifiant de compte anonyme en un nom avec lequel vous pouvez réellement agir. Commencez par le mode de surveillance pour établir vos bases de référence avant de mettre en œuvre une quelconque politique.

Nous voulons savoir comment vous gérez l’IA aujourd’hui. Venez rejoindre la conversation sur [​Discord](https://discord.cloudflare.com/) ou contactez l’équipe chargée de votre compte.

]]>01KZQZPPDNGBRJQCNNFZPWK81RCloudflare OS : une plateforme ouverte pour les agents, les applications et le travailhttps://blog.cloudflare.com/fr-fr/cloudflare-os/ Tue, 11 Aug 2026 04:02:58 GMTCloudflare OS est une plateforme open source qui permet à tout le personnel de votre entreprise de créer des applications, d’automatiser des tâches et de bénéficier d’un accès sécurisé aux systèmes internes, en fonction des connaissances et du mode de fonctionnement de votre organisationAgentsAgents WeekCloudflare AccessCloudflare OSCloudflare WorkersDéveloppeursIANouveautés produitsOpen SourcePlateforme pour développeursChaque entreprise a une mission, une raison d’être. L’entreprise confie cette mission (ainsi que sa terminologie, ses procédures, ses systèmes, ses normes et ses méthodes de travail) à son personnel. À son tour, le personnel se fie à ce contexte et à son expérience pour contribuer à l’accomplissement de cette mission.

Le travail peut revêtir de nombreuses formes, allant du code aux documents et aux diapositives, en passant par les relations et les résultats concrets dans le monde réel.

Certaines de ces aspects sont simples : le code s’exécute ou ne s’exécute pas. Depuis quelques années, les agents utilisent cette boucle de rétroaction pour générer du code qui « fonctionne » pour les développeurs. Mais qu’en est-il pour nous autres, qui ne sommes pas développeurs ?

Il est plus difficile d’étendre cette dynamique au reste de l’organisation. Les agents doivent comprendre le contexte de l’entreprise et être capables d’accéder aux systèmes que le personnel utilise pour effectuer son travail. Ils doivent mettre à profit ce contexte et ces ressources pour exécuter des actions qui permettent à l’entreprise de progresser vers la réalisation de sa mission.

C’est pourquoi nous avons développé Cloudflare OS, qui fournit à chaque collaborateur un agent et un espace de travail adaptés à son entreprise – à son fonctionnement, à ses connaissances et aux systèmes dont elle dépend.

Au mois de mai de cette année, nous avons donné à tous les collaborateurs de Cloudflare accès à la première version de Cloudflare OS. Des milliers de collaborateurs occupant différents postes, parmi lesquels de nombreux utilisateurs extérieurs aux rôles d’ingénierie, l’utilisent désormais chaque jour pour créer des documents et des présentations, automatiser des tâches récurrentes et développer de petites applications qui leur permettent de visualiser les données et facilitent leur travail.

Cloudflare OS a également mis à la disposition de tous les utilisateurs une bibliothèque commune de connaissances et de compétences développée par les équipes de Cloudflare. Celle-ci rassemble, sous la forme d’instructions pouvant être suivies par un agent, notre terminologie, nos procédures et nos méthodes éprouvées pour exécuter des tâches récurrentes. Ainsi, lorsqu’un collaborateur découvre une meilleure façon d’accomplir une tâche, tous ses collègues peuvent en bénéficier.

**Aujourd’hui, nous publions en open source une nouvelle version de[ Cloudflare OS](https://os.cloudflare.app/).** Toute entreprise peut la déployer, la connecter à ses systèmes internes et se l’approprier.

## **Ce que nous avons appris de la première version**

La version de Cloudflare OS que nous publions aujourd’hui en open source repose sur les enseignements que nous avons tirés de l’utilisation en interne de la première version ; un parcours que notre directeur des systèmes d’information, Sam Rhea, retrace dans son[​](https://blog.cloudflare.com/how-we-use-ai-with-cloudflare-os) [article de blog](https://blog.cloudflare.com/how-we-use-ai-with-cloudflare-os).

La première version était destinée aux utilisateurs qui exécutaient des agents dans des espaces de travail privés. Les applications étaient des logiciels statiques, plutôt que des logiciels en temps réel connectés aux systèmes internes, et la plupart des tâches déterministes nécessitaient encore d’exécuter une compétence d’agent une nouvelle fois et, par conséquent, de consommer d’autres jetons de modèle.

La collaboration a révélé un défi plus fondamental. L’accès à un [​serveur MCP](https://www.cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/) nous a permis d’identifier les outils qu’un agent pouvait appeler, mais pas les ressources sous-jacentes que l’agent avait observées. Lorsque les utilisateurs ont commencé à partager des espaces de travail, des applications et des documents, nous avons dû veiller à ce que cette collaboration ne risque pas d’exposer des informations que certaines personnes n’étaient pas autorisées à consulter.

Nous avons reconstruit Cloudflare OS sur de nouvelles fondations, afin de résoudre ces problèmes. La sécurité devait faire partie intégrante de la plateforme, et non être une tâche que chaque développeur d’application ou utilisateur d’agent devait s’assurer de mettre en œuvre correctement.

Le résultat est une plateforme conçue pour appartenir à l’entreprise qui l’exécute. Vous pouvez personnaliser les interfaces, connecter vos outils et ajouter des compétences et un contexte qui reflètent le fonctionnement de votre entreprise.

## **Présentation de Cloudflare OS**

Cloudflare OS commence par une conversation dans votre navigateur, comme beaucoup d’autres outils IA. Toutefois, ce qui distingue Cloudflare OS des autres outils, c’est que chaque conversation s’appuie sur le contexte et les compétences que votre entreprise a sélectionnés. Donnez un objectif à votre espace de travail : il pourra alors s’appuyer sur ces connaissances et exploiter les outils et les données que votre entreprise utilise déjà pour l’atteindre.

Cloudflare OS se compose de trois éléments :

  * **Un espace de travail pour agents** fondé sur le contexte et les compétences sélectionnées par votre entreprise, avec un environnement d’exécution isolé dans lequel les agents peuvent écrire et exécuter du code.
  * **Un nouveau cadre de sécurité et de gouvernance** garantissant un accès sécurisé aux données et aux services internes.
  * **Une plateforme dédiée à l’hébergement d’applications personnelles et personnalisables** , que les utilisateurs peuvent créer, partager et continuer à faire évoluer.



Ce qui commence comme une conversation peut devenir un document, une application ou un processus destiné à poursuivre l’exécution de tâches.

## **Un espace de travail pour tous les collaborateurs de votre entreprise**

Les espaces de travail pour agents ont été conçus pour être utilisés par tout le personnel de votre entreprise. Vous interagissez avec eux depuis votre navigateur ; vous n’avez donc pas besoin d’être développeur, ni de savoir utiliser un terminal. 

Un espace de travail réunit les sessions d’agents, l’état persistant, les résultats et les fichiers, l’accès aux ressources, ainsi qu’un environnement d’exécution isolé dans lequel l’agent peut écrire et exécuter du code.

Il intègre l’ensemble des connaissances et des compétences acquises par votre équipe ou votre entreprise au fil du temps. Plus besoin de réinventer la roue à chaque tâche : si un membre de votre équipe a identifié la meilleure façon de faire quelque chose, tout le monde en bénéficie. Les utilisateurs n’ont plus besoin d’expliquer à chaque fois le même processus, la même terminologie et les mêmes pratiques exemplaires à un modèle lorsqu’ils commencent une tâche.

Voici quelques dispositions que vous pouvez prendre :

### **Effectuer des recherches et poser des questions**

Demandez à un espace de travail d’effectuer des recherches sur un sujet en s’appuyant sur le contexte de l’entreprise et les ressources que vous mettez à sa disposition. L’agent peut écrire du code pour rechercher, filtrer, croiser et analyser des informations, au lieu d’importer l’intégralité d’un ensemble de données dans la fenêtre de contexte du modèle.

### **Créer des documents, des diapositives et des feuilles de calcul**

Un espace de travail permet de transformer les recherches effectuées en un document, une présentation ou une feuille de calcul que vous pouvez continuer à modifier. Ces résultats ne sont pas nécessairement des fichiers statiques ; ils peuvent rester connectés à des données en temps réel, être mis à jour à mesure que leurs sources sont modifiées, et être exportés vers des formats ou des services familiers tels que Google Drive.

### **Créer des applications collaboratives et connectées pour votre équipe**

Lorsqu’un document ou une feuille de calcul ne suffit pas, l’agent peut créer une application dotée de sa propre interface, de sa propre logique et de son propre état. L’application peut exploiter les ressources de l’entreprise mises à sa disposition et permettre à plusieurs collaborateurs de travailler ensemble.

### **Exécuter des workflows déterministes**

Toutes les tâches ne nécessitent pas une session d’agent complète. Beaucoup d’entre elles consistent en une suite d’étapes bien définies, comportant un ou deux moments où il est utile de faire preuve de discernement. Un espace de travail permet de transformer ces tâches en workflows majoritairement déterministes, en utilisant du code pour les étapes prévisibles et en ne recourant à un modèle que lorsqu’il apporte une valeur ajoutée. Les workflows peuvent être exécutés à la demande, selon un calendrier défini ou lorsqu’un événement se produit dans un système connecté.

Cloudflare OS offre aux agents et aux applications un accès contrôlé aux systèmes d’information de l’entreprise via les instances Gatekeepers (vous trouverez plus d’informations à ce sujet dans la section consacrée à la sécurité, ci-dessous). Le service prend également en charge les serveurs [​Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro) existants que votre entreprise utilise déjà, via les [​portails pour serveurs MCP](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/).

## **Un nouveau cadre de sécurité et de gouvernance pour un accès sécurisé aux données et services internes**

Lorsque des collaborateurs commencent à tester l’utilisation de l’IA dans le cadre de leur travail, l’une de leurs premières demandes concerne souvent l’obtention de clés API pour accéder aux systèmes de l’entreprise. C’est logique : l’IA ne leur est guère d’une grande utilité si elle n’a pas accès aux systèmes qu’ils utilisent pour accomplir leurs tâches.

Cependant, confier des clés API à des collaborateurs et à des agents est une pratique dangereuse et non évolutive. Les clés offrent souvent un accès étendu et durable, qu’il est difficile de restreindre, de partager de manière sécurisée et de contrôler.

Le protocole MCP offre aux agents un moyen plus efficace d’utiliser ces systèmes. Un serveur MCP peut stocker l’identifiant et mettre à disposition un ensemble défini d’outils, au lieu de transmettre directement la clé à l’agent. Toutefois, déterminer les outils que peut utiliser un agent n’est qu’une première étape. Le protocole MCP, à lui seul, n’indique pas quelles ressources sous-jacentes un agent a observées. L’agent peut regrouper des informations provenant de différents systèmes, les transmettre vers un environnement moins restreint ou, via des applications et des interfaces, les mettre à la disposition d’utilisateurs qui ne sont peut-être pas autorisés à consulter les ressources d’origine. L’autorisation doit tenir compte de la destination suivante des données.

### **Les agents démarrent sans accès**

[ Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/) contrôle qui peut accéder à Cloudflare OS. Dans le système, chaque agent et chaque application n’ont initialement accès à aucune ressource. Un agent peut demander l’accès à une ressource spécifique, et vous pouvez alors lui accorder ou lui refuser cet accès. Le code généré reçoit cette ressource sous la forme d’une liaison typée :

`env.PROJECT` est une fonctionnalité représentant l’autorisation d’utiliser une ressource spécifique conformément à une politique spécifique. Les identifiants restent complètement isolés de l’agent et de tout code généré.

Le code serveur s’exécute dans une instance Workers dynamique dont les communications réseau sortantes globales sont désactivées. Le code client s’exécute dans un cadre isolé en sandbox dans le navigateur. Aucun des deux ne peut accéder à Internet, sauf par le biais de fonctionnalités que vous leur fournissez explicitement.

### **Gatekeepers régit les ressources et les actions**

Une instance Gatekeepers est une instance [​Workers](https://developers.cloudflare.com/workers/?_gl=1*1pzndf6*_gcl_au*MzM2MDkxNTQzLjE3ODQ4NDczOTM.*_ga*MWVkZWU3OTctMzJjNC00YWE1LWI2ZDUtZTJkNTY1NzYxYWQ0*_ga_SQCRB0TXZW*czE3ODUyMTk3NjMkbzckZzAkdDE3ODUyMTk3NjMkajYwJGwwJGgwJGRQeHAyTUEtdzgtVUFETUEzOGwtVFVhajVDd2laRWYxSC1R) spécifique à un service, qui réside entre Cloudflare OS et un service externe. Elle comprend l’API du service, ses ressources et les opérations pouvant être effectuées sur celles-ci.

Accorder à un agent l’accès à l’intégralité de votre compte GitHub est probablement une approche trop large. Une instance Gatekeepers peut permettre à un agent d’accéder à un référentiel unique ou de consulter les incidents sans toutefois pouvoir accéder au code source ; elle peut également masquer certains champs, appliquer des limites de débit et exiger une validation avant la fusion d’une requête d’extraction (pull request).

L’agent et ses applications ont accès à une petite API TypeScript. L’instance Gatekeepers gère [​OAuth](https://www.cloudflare.com/learning/access-management/what-is-oauth/), conserve les identifiants, applique les politiques, enregistre les données consultées et gère toutes les opérations pouvant avoir un effet secondaire visible au niveau externe.

### **La politique se conforme à ce que l’agent a observé**

Contrôler la lecture initiale n’est pas une approche suffisante. Prenons l’exemple d’un scénario dans lequel un agent consulte une table contenant des données sensibles dans un entrepôt de données et utilise ces données pour générer un tableau de bord en temps réel. Le partage du tableau de bord ne doit pas permettre à des utilisateurs qui n’y ont pas directement accès de consulter celui-ci.

Cloudflare OS enregistre chaque ressource observée par des agents ; ces observations restent liées à l’agent et à son travail. Si un autre utilisateur tente d’ouvrir l’espace de travail, d’interagir avec l’agent ou de consulter ce qu’il a produit, Gatekeepers vérifie que cet utilisateur dispose des droits d’accès requis aux ressources concernées.

Ce même journal des observations sert à définir les règles qui déterminent à quel moment les agents peuvent effectuer des requêtes externes. La lecture de données sensibles peut empêcher l’agent d’écrire des données dans certaines sources, d’inviter de nouveaux collaborateurs, de confier une tâche à un autre agent ou d’effectuer une requête sortante.

Le personnel qui utilise des agents ou développent des applications n’a pas besoin de se préoccuper de commettre ces erreurs, car la plateforme permet désormais de gérer cet aspect.

## **Une plateforme dédiée au développement et au partage d’applications personnelles et personnalisables**

La plupart des suites bureautiques proposent un ensemble fixe d’applications : traitement de texte, tableur et logiciel de présentation. Dans Cloudflare OS, chaque « fichier » peut être à une application à part entière, développée par un agent pour une personne, un projet ou une équipe.

Il ne s’agit pas de prototypes que vous devez exporter et déployer ailleurs ; chacune est une application full-stack comprenant du code client, du code serveur, une API et un état persistant. Les applications sont privées par défaut, mais elles peuvent être partagées comme des documents.

### **Chaque application est une instance Workers**

Lorsque vous demandez à votre espace de travail de développer une application, l’agent génère deux composantes :

  * Du code client chargé d’afficher l’interface utilisateur de l’application dans le navigateur
  * Du code serveur chargé de stocker l’état et de mettre en œuvre le comportement de l’application



Le serveur est chargé à la demande sous forme d’instance [​Dynamic Workers](https://developers.cloudflare.com/dynamic-workers/) et instancié sous forme de primitive [​Durable Object Facet](https://developers.cloudflare.com/dynamic-workers/usage/durable-object-facets/) (ces deux fonctionnalités ont été développées spécialement pour ce projet). La primitive Facet permet à l’application de disposer de sa propre base de données SQLite, distincte de l’environnement d’exécution de Cloudflare OS qui la gère. Les instances Dynamic Workers utilisent des isolats V8 légers, ce qui permet à chaque application de disposer de son propre environnement d’exécution isolé sans nécessiter un serveur ou un conteneur dédié en attente.

Le client navigateur communique avec le serveur via [​Cap’n Web](https://github.com/cloudflare/capnweb), le système RPC (Remote Procedure Call) open source de Cloudflare, basé sur les capacités d’objets. Une méthode de serveur peut être appelée depuis le client comme une fonction JavaScript classique :

La particularité réside dans le fait que l’agent peut également appeler cette même méthode.

**Ainsi, si vous pouvez développer vous-même un outil permettant d’effectuer une tâche, les agents pourront utiliser cet outil pour accomplir cette tâche en votre absence.**

### **Partagez l’application ou partagez son développement**

Lorsque vous développez une application dans Cloudflare OS, vous disposez de deux moyens pour la partager :

  * Partager votre application permet à d’autres utilisateurs de collaborer en temps réel, en utilisant le même état.
  * Partager un modèle de votre application permet à d’autres utilisateurs de créer leur propre copie de celle-ci.



Une application instanciée à partir d’un modèle contient le code de l’application d’origine, mais elle ne contient pas ses données SQLite, l’historique des conversations, les identifiants ni les ressources associées. Chaque nouvelle application démarre avec un état et des ressources propres.

Concrètement, cela signifie que lorsque vous partagez des applications avec votre équipe, vos collaborateurs peuvent les modifier eux-mêmes grâce à l’IA, sans devoir créer une demande de fonctionnalité et vous l’affecter.

## **Utilisez n’importe quel modèle et maîtrisez-en le coût**

Cloudflare OS est compatible avec tous les modèles. Chaque appel d’inférence transite par [​Cloudflare AI Gateway](https://developers.cloudflare.com/ai-gateway/), ce qui permet à votre entreprise de disposer d’un point central pour déterminer quels modèles sont disponibles et quel modèle doit traiter chaque tâche.

Toutes les tâches ne nécessitent pas forcément le modèle le plus cher. Vous pouvez ne pas vouloir utiliser le modèle Frontier le plus coûteux pour générer un récapitulatif de vos e-mails non lus chaque matin. AI Gateway vous offre le contrôle nécessaire pour vous assurer que les modèles coûteux sont uniquement utilisés pour les tâches les plus complexes.

Chaque demande est attribuée à la personne, à l’équipe ou à l’espace de travail qui l’a formulée. Les administrateurs peuvent suivre l’évolution des dépenses liées à l’inférence, définir des budgets et des limites de débit, et décider des mesures à prendre lorsqu’une limite est atteinte. 

## **Open source, pour vous permettre de vous l’approprier**

Cloudflare OS est disponible dès aujourd’hui et est open source. Découvrez le [​référentiel GitHub de cloudflare-os](https://github.com/cloudflare/cloudflare-os). Vous pouvez le déployer sur votre compte Cloudflare et utiliser vos propres politiques d’accès, votre configuration AI Gateway, vos données et vos intégrations.

Notre déploiement interne reflète les systèmes, la terminologie, les politiques et les modes de fonctionnement de Cloudflare ; le vôtre devrait refléter votre entreprise.

Cloudflare OS est conçu pour vous permettre de personnaliser l’interface, d’ajouter des instances Gatekeepers internes et de développer des fonctionnalités spécifiques à votre entreprise, sans modifier le produit de base.

Nous publions deux référentiels : le [​noyau Cloudflare OS](https://github.com/cloudflare/cloudflare-os) et un [​exemple de déploiement](https://github.com/cloudflare/cloudflare-os-starter) basé sur notre utilisation interne à Cloudflare. Le référentiel de déploiement utilise le noyau tel quel, sans appliquer de correctifs, et offre un espace dédié pour la configuration, l’interface utilisateur personnalisée, les intégrations internes, l’analyse de données et les pipelines de déploiement.

## **Déployé avec nos partenaires**

Le code source n’est qu’un point de départ. Le contexte, les compétences, les flux de travail, les systèmes internes et les politiques sont ce qui rend Cloudflare OS encore plus utile pour votre entreprise.

Les partenaires stratégiques de Cloudflare, Presidio et Happy Cog, travailleront avec vous pour personnaliser Cloudflare OS en fonction du mode de fonctionnement de votre entreprise et le déployer auprès de l’ensemble de votre personnel.

Les partenaires peuvent vous aider à sélectionner les compétences partagées et le contexte institutionnel, à développer des interfaces personnalisées, à connecter les systèmes internes via Gatekeepers et les portails pour serveurs MCP, ainsi qu’à configurer les contrôles de sécurité, de modèles et de coûts.

Vous bénéficiez ainsi d’un déploiement personnalisé de Cloudflare OS, connecté à vos systèmes, qui s’exécute sur Cloudflare et est adapté aux méthodes de travail réelles de votre personnel.

## **Lancez-vous**

Cloudflare OS est disponible dès aujourd’hui sur [​GitHub](https://github.com/cloudflare/cloudflare-os). Vous pouvez explorer le code source, tester la démo ou la déployer sur votre compte Cloudflare en quelques minutes, à l’aide de notre [​référentiel de démarrage](https://github.com/cloudflare/cloudflare-os-starter).

Nous n’en sommes encore qu’au commencement. Nous travaillons actuellement à l’intégration de Cloudflare OS dans le tableau de bord de Cloudflare sous la forme d’un produit entièrement géré, à l’ajout de conteneurs pour les workflows de développement, ainsi qu’à l’intégration d’espaces de travail dans Slack et d’autres outils de messagerie instantanée.

Si vous souhaitez échanger avec notre équipe, nous serions ravis de discuter avec vous. Utilisez [​ce formulaire](https://www.cloudflare.com/resource/cloudflare-os-interest-landing-page/) pour nous contacter !

]]>01KZQFC79Z7Q2QX4WQD5Z5AMZ8Cloudflare propose désormais l’approche Agent Development Lifecyclehttps://blog.cloudflare.com/fr-fr/agent-development-lifecycle/ Fri, 07 Aug 2026 09:28:20 GMTLes agents sont capables d’écrire du code plus rapidement que les équipes ne peuvent le réviser, le déployer et le gérer. Aujourd’hui, nous présentons l’approche Agent Development Lifecycle (ADLC, cycle de vie du développement des agents), ainsi que les composantes primitives de Cloudflare sur lesquelles elle repose.Agent Development LifecycleAgentsAgents WeekBrowser RunCloudflare Workersdes flux de travailDevOps (FR)IAMCPNouveautés produitsObservabilityPlateforme pour développeursTracingLes responsables techniques ont consacré les dernières décennies à élaborer des solutions permettant à une multitude de programmeurs de travailler ensemble sur une base de code partagée. Ces travaux remontent à la publication intitulée « Systems Development Lifecycle » ([RAND, 1975](https://www.rand.org/pubs/reports/R1855.html)), aujourd’hui communément appelée « cycle de vie du développement logiciel » (SDLC, Software Development Lifecycle), qui définit les phases suivantes :

  * Planification
  * Conception
  * Mise en œuvre
  * Test
  * Déploiement
  * Maintenance
  * Abandon



Grâce à l’IA, l’étape qui était auparavant la plus longue et la plus coûteuse, à savoir la mise en œuvre, est désormais devenue la plus rapide et la moins chère. Cette évolution a, à son tour, eu des répercussions en aval : les personnes responsables de toutes les autres étapes du cycle de développement logiciel se sont retrouvées submergées de travail. Cela va du personnel assurant la maintenance de projets open source, qui est submergé par des milliers de requêtes d’extraction (pull requests) et de rapports d’incident, aux ingénieurs de production, qui tentent de prévenir les défaillances des systèmes de production tandis que le rythme des déploiements logiciels augmente de plusieurs ordres de grandeur.

Nous essayons tous de protéger nos systèmes, nos clients et nous-mêmes contre le désordre que peut engendrer l’IA.

Mais la réponse, paradoxalement, consiste à permettre aux agents d’en faire davantage. Ça n’est que justice, après tout ! Vous n’accepteriez jamais qu’un ingénieur de votre équipe écrive du code, puis compte sur quelqu’un d’autre pour le valider, le fusionner, le déployer, assurer la permanence en production et trier les bugs signalés. Cependant, c’est précisément ce qu’exigent actuellement la plupart des entreprises de leurs agents. Les modèles ont accompli des progrès considérables, et les agents s’exécutent désormais sur des horizons temporels plus longs, ce qui leur permet d’accomplir des tâches d’ampleur considérablement plus grande. Cependant, leur utilisation n’est pas encore uniforme à l’échelle du cycle de vie du développement logiciel.

Cloudflare traite les agents de la même manière que ses clients : ils peuvent [acheter des domaines](https://blog.cloudflare.com/agents-stripe-projects/), créer [des comptes temporaires](https://blog.cloudflare.com/temporary-accounts/) et [utiliser l’API Cloudflare dans son intégralité](https://blog.cloudflare.com/code-mode-mcp/). Nous savons que les agents ont besoin d’API et d’outils pour pouvoir gérer l’ensemble du cycle de vie du développement logiciel pour le compte de nos clients, et pas uniquement lors de la phase initiale.

C’est pourquoi nous présentons aujourd’hui une nouvelle suite d’outils qui permettent aux agents d’aller au-delà de la simple génération de code et de s’impliquer davantage dans le cycle de vie du développement logiciel. Nous partageons ici ce que nous avons développé et appris en essayant de résoudre ce problème pour nous-mêmes :

  * [**@cloudflare/ci**](https://blog.cloudflare.com/ci-workflows) – Une nouvelle façon de gérer l’intégration et le déploiement continus (CI/CD) sur des millions de référentiels, capable de s’auto-réparer et de déployer des agents pour exécuter des tâches beaucoup plus complexes, basée sur Cloudflare Workflows.
  * [**Traces OpenTelemetry dans l’environnement de développement local**](https://blog.cloudflare.com/local-tracing) – Offre aux agents une observabilité comparable à celle dont ils disposent en production, intégrée dans Wrangler et le plugin Cloudflare Vite.
  * [**Présentation : Cloudflare Agents et Agent Traces**](http://blog.cloudflare.com/agents-on-cloudflare) – Une nouvelle plateforme dédiée à l’observation, à la maintenance et à l’amélioration des agents, centrée sur les traces OpenTelemetry qu’ils génèrent.
  * [**Comment Cloudflare utilise l’IA pour appliquer les normes d’ingénierie**](http://blog.cloudflare.com/engineering-standards-enforcement) – Notre expérience de la mise en œuvre des pratiques exemplaires dans les référentiels et les spécifications de l’ensemble de nos produits et systèmes.
  * [**Comment nous avons créé une « usine logicielle » pour ramener à zéro le nombre de tickets GitHub d’Astro**](https://blog.cloudflare.com/astro-issue-triage) – Notre expérience du développement de systèmes permettant de trier, reproduire, vérifier et corriger automatiquement les problèmes liés à un projet open source de grande ampleur et continuellement croissant.



Cependant, il y a quelque chose de plus important ici. Lorsque l’on examine le cycle de vie du développement logiciel, même avec la meilleure automatisation qui soit, ses postulats ne sont pas adaptés au volume de code que les agents peuvent écrire, ni à la rapidité avec laquelle les équipes de développement doivent évoluer pour rester compétitives. Nous pensons que l’heure est venue de remplacer le cycle de vie du développement logiciel (SDLC, Software Development Lifecycle) par le cycle de vie du développement des agents (ADLC, Agent Development Lifecycle).

## La méthodologie SLDC est destinée aux équipes de développement logiciel. La méthodologie ADLC est destinée aux usines de logiciels.

En ce moment, le [tout le monde](https://x.com/zachlloydtweets/status/2069789929073262945) [parle](https://x.com/matanSF/status/2066578088184680920) du [développement](https://x.com/dexhorthy/status/2081797628552270027) d’[usines](https://x.com/bcherny/status/2077929390806073807) [logicielles](https://x.com/gokulr/status/2032271386161684665) – des systèmes pilotés par des agents qui, à partir de données d’entrée, développent, améliorent, déploient et gèrent des logiciels de manière autonome. Prenez des données entrantes, qu’il s’agisse d’une erreur de production, d’un signalement de bug transmis par un client ou d’une idée de nouvelle fonctionnalité, et confiez-les entièrement à un agent.

Même lorsque des entreprises ont recours à des agents, la plupart des projets logiciels sont limités par des étapes nécessitant une intervention humaine : des opérateurs humains encouragent les agents, leur disent de continuer à travailler, leur demandent de tenir compte des commentaires issus d’une révision du code, surveillent continuellement une multitude d’agents et leur donnent des consignes. Dans la plupart des équipes de développement logiciel, ce sont toujours des humains qui gèrent chaque étape du modèle du cycle de vie du développement logiciel ; la seule différence est qu’ils délèguent les tâches que comporte chaque étape à un agent.

Le rêve qui sous-tend le concept des usines logicielles est donc le suivant : et si l’on repensait cette approche pour créer une « usine » couvrant l’intégralité du processus de développement logiciel ? Comment pouvons-nous permettre aux opérateurs humains de consacrer davantage de temps aux tâches qui nécessitent véritablement l’inspiration, le goût et le jugement humains ? Cela nous laisserait plus de temps pour concevoir, échanger avec nos clients et voir plus grand.

Une usine logicielle doit gérer les mêmes étapes du cycle de vie du développement logiciel, mais elle impose des exigences considérablement plus élevées à la plateforme sur laquelle elle repose. En effet, lorsque vous confiez les clés à l’agent, chaque étape manuelle qui dépendait auparavant d’un opérateur humain doit être adaptée pour devenir :

  * **Programmatique** – Si l’approche « ClickOps » était déjà une mauvaise pratique pour les humains, c’est une option tout simplement exclue pour les agents. Chaque opération, sans exception, nécessite des API que les agents peuvent appeler et déboguer et sur lesquelles ils peuvent compter.
  * **Extensible horizontalement** – Les déploiements en prévisualisation étaient un agrément intéressant lorsque des opérateurs humains passaient scrutaient un écran pendant le développement ou prenaient manuellement le contrôle d’un serveur de préproduction afin de localiser d’éventuels problèmes en amont de la mise en production. Pour que les agents fonctionnent correctement, chaque agent doit disposer de son propre aperçu correspondant à l’environnement de production.
  * **Reproductible** – Que se passe-t-il si vous découvrez un bug qui peut uniquement être reproduit en simulant une connexion 4G sur un iPhone 15 ou qui n’affecte qu’une adresse IP située dans un pays bien particulier ? Les outils conventionnels de tests unitaires et de tests d’intégration ne sont d’aucune utilité dans ce cas de figure.
  * **En temps réel et basée sur des notifications push** – Compter sur un opérateur humain pour examiner le bon tableau de bord a toujours été une approche peu recommandable pour savoir si tout fonctionne correctement ; avec des agents, toutefois, cette méthode devient totalement inefficace. Vous avez besoin d’un événement qui déclenche l’exécution d’une tâche par un agent.
  * **Atomique** – Chaque modification doit pouvoir être testée, déployée, observée et annulée indépendamment, sans affecter les comportements non liés.
  * **Soumise à des autorisations** – Vous savez pertinemment qu’il veut mieux éviter de le faire, mais aujourd’hui encore, vous confiez à quelques ingénieurs de confiance les clés d’accès SSH à l’environnement de production, au cas où les choses tourneraient vraiment au vinaigre. Il est impensable de laisser cette latitude à un agent, mais si celui-ci ne peut pas remonter l’information et obtenir davantage d’autorisations, comment peut-il faire son travail ?
  * **Dotée de capacités d’auto-amélioration** – Les humains apprennent par l’expérience. Lors de leur premier déploiement de code ou de leur première permanence, les humains sont lents et ont besoin de travailler en binôme, mais ils finissent par s’améliorer et devenir plus rapides. Les agents, eux aussi, ont besoin de moyens pour tirer les leçons de leur expérience.



Nous devons innover si nous voulons sécuriser l’utilisation des usines logicielles pour la production de logiciels destinés à une utilisation réelle. Les usines logicielles se heurtent au même défi que d’autres systèmes autonomes, tels que les voitures autonomes : celui d’évoluer d’un taux de fiabilité de 80 % à un taux de 99 % suivi de plusieurs neuf.

## Si vous souhaitez confier aux agents les clés du cycle de vie du développement logiciel, vous ne pouvez pas leur fournir un véhicule conçu pour des humains

Une voiture autonome est équipée de capteurs et de technologies dont un véhicule conventionnel ne dispose pas : des capteurs Lidar, des caméras, une puissance de calcul suffisante pour exécuter des inférences, ainsi qu’une connectivité à un système de commande central, capable de prendre le contrôle à distance si nécessaire.

Pour qu’un véhicule autonome atteigne 80 % des performances d’un conducteur humain, tous ces équipements ne sont probablement pas nécessaires. D'ailleurs, cela fait 10 ans que la conduite autonome a atteint des performances équivalentes à 80 % des capacités d’un conducteur humain. Toutefois, ce n’est le seuil que nous cherchons à atteindre : l’objectif est d’être bien plus performant et plus sûr qu’un conducteur humain. C’est ce que l’on attend lorsque l’on confie les clés à une machine, afin de pouvoir faire une sieste en toute sécurité pendant que la voiture circule à 130 km/h sur l’A6. Et c’est pourquoi les véhicules autonomes disposent de technologies spécialement conçues pour la conduite autonome : ce sont elles qui inspirent la confiance et permettent de gérer les scénarios particuliers qui ne peuvent pas être anticipés dès le départ.

Il en va de même pour les logiciels autonomes. Posez-vous la question : pourquoi _n’avez-vous pas_ encore laissé votre agent approuver et fusionner automatiquement ses requêtes d’extraction dans vos services en production ? Cela ne fait aucun doute : plus les enjeux de ce que vous construisez sont importants, plus votre liste de raisons sera longue.

Lorsque l’on commence à examiner tout ce qui peut prendre un tournant dramatique pendant ce processus, mais également tout ce qui est nécessaire pour concevoir une solution adaptée aux clients, on prend conscience que l’ensemble est d’une complexité remarquable. Il ne s’inscrit pas dans une séquence linéaire d’étapes d’un fichier YAML dans GitHub Actions, et exige bien plus que l’exécution de tests automatisés classiques. Même une modification de moindre ampleur apportée à un tableau de bord peut impliquer une multitude de rôles, de spécialisations et de structures organisationnelles, et les modifications subjectives sont les plus difficiles à tester et à déléguer. La plupart de ces éléments ne font probablement pas encore partie de votre pipeline d’intégration continue/de livraison continue (CI/CD), à l’heure actuelle. Cependant, vous devrez les intégrer si vous souhaitez que ces projets voient le jour, tout en accordant un contrôle total aux agents qui gèrent l’usine logicielle.

Pour permettre aux agents de diriger l’ensemble du processus, nous avons besoin d’un meilleur moyen d’orchestrer ces successions d’étapes dynamiques. Nous pensons que la réponse est une instance [Workflows](https://blog.cloudflare.com/ci-workflows) capable de lancer des conteneurs, des agents et des navigateurs. Cette instance Workflows doit être capable de définir des indicateurs de fonctionnalités (feature flags) et de les activer pour un utilisateur test, d’analyser les journaux et les traces, de surveiller les paramètres de production pendant le déploiement progressif d’une modification et d’exécuter toutes les autres tâches nécessaires pour assurer un déploiement en toute sécurité.

## Un pipeline CI/CD est simplement une instance Workflows ; toutefois, une instance Workflows peut être bien plus qu’un pipeline CI/CD.

[Cloudflare Workflows](https://developers.cloudflare.com/workflows/) vous permet d’enchaîner plusieurs étapes, de relancer automatiquement les tâches ayant échoué et de conserver l’état du système pendant plusieurs minutes, heures, voire semaines. Ces instances sont conçues pour coder des processus opérationnels complexes et dynamiques sous la forme d’un programme logique et compréhensible. [Cet article de blog](https://blog.cloudflare.com/ci-workflows) explique en détail pourquoi Workflows, utilisé conjointement à [Artifacts](https://blog.cloudflare.com/artifacts-git-for-agents-beta/), simplifie considérablement la définition et l’exécution des pipelines CI/CD. Par exemple :

Toutefois, les instances Workflows offrent bien plus qu’une simple succession d’étapes linéaires. Elles peuvent être [définies dynamiquement](https://blog.cloudflare.com/dynamic-workflows/), et elles peuvent déployer des agents ou d’autres instances Workflows. [Cet exemple](https://flueframework.com/docs/guide/workflows/#example-cloudflare-workflows) présente une instance Workflows qui examine les nouvelles données du jour précédent. L’instance Workflows dispose d’un contrôle total sur le moment et la manière dont l’agent est sollicité et peut transmettre le contexte d’une étape à l’autre :

Lorsque vous aurez intégré ce schéma et que vous serez, comme Cloudflare, « accro à Workflows », vous commencerez à vous demander : « Quelles autres tâches pourrais-je exécuter avec une instance Workflows ? Quelles autres étapes dont l’exécution est ralentie par l’intervention humaine pourrais-je déléguer à cette combinaison d’agents Workflow + [Flue](https://flueframework.com/) ? »

## L’approche ADLC complète sur l’infrastructure Cloudflare

Lorsque l’on examine les étapes du cycle de vie du développement logiciel, avec [Workflows](https://developers.cloudflare.com/workflows/), qui permet d’orchestrer des étapes complexes, et avec [Artifacts](https://developers.cloudflare.com/artifacts/), qui représente la couche de stockage du code, toutes les ressources nécessaires à un agent pour maîtriser l’ensemble du processus de développement, de déploiement et de maintenance d’un logiciel sont disponibles sur Cloudflare :

## Composantes fondamentales pour construire votre usine logicielle

À l’heure actuelle, les pionniers de l’innovation construisent les usines logicielles de demain. À terme, les usines logicielles deviendront, à l’instar des agents et de l’IA, la manière habituelle de développer des logiciels. Pour la plupart des personnes et des entreprises, toutefois, nous n’en sommes pas encore là.

Et nous voulons y remédier.

Pour y parvenir, nous nous sommes posé les questions suivantes : comment rendre les choses simples et accessibles, afin que tous les internautes puissent bénéficier d’un changement de paradigme aussi important ? Et quelles sont les fonctionnalités fondamentales que nous pouvons mettre à la disposition de tous, de la plus petite start-up aux plus grandes plateformes du monde ?

Dans ce cas, nous pensons que les composantes fondamentales sont disponibles. Il nous reste encore du chemin à parcourir pour les connecter entre elles, pour continuer à développer notre propre usine logicielle et pour en tirer des enseignements, mais aujourd’hui, nous sommes prêts à vous aider à construire la machine qui construit la machine, sur Cloudflare. Commencez avec [@cloudflare/ci](https://blog.cloudflare.com/ci-workflows), [développez un agent](http://blog.cloudflare.com/agents-on-cloudflare) et découvrez dans quelle mesure vous pouvez automatiser le cycle de vie du développement logiciel.

]]>01KZD2NGQAQSVMA8KDP52M39Y5Annonce de Cloudflare Wallets : le portefeuille programmable pour l’Internet agentiquehttps://blog.cloudflare.com/fr-fr/wallets/ Fri, 07 Aug 2026 03:57:14 GMTCloudflare Wallets fournira aux agents IA des moyens de paiement natifs et une identité vérifiable sur le web. Grâce au protocole x402, les agents peuvent acheter de manière autonome des API et des contenus dans le respect de consignes de sécurité clairement définies.Agents WeekAI Bots (FR)DéveloppeursIANouveautés produitsPaymentsPlateforme pour développeursx402Aujourd’hui, il est difficile pour les agents IA de tester de nouvelles API. Ils doivent souvent s’orienter sur une page de connexion conçue pour des utilisateurs humains, et non pour des agents, contacter un interlocuteur humain pour ajouter un moyen de paiement, générer une clé API, puis comprendre comment appeler l’API.

Il est très difficile pour les agents d’accomplir ce processus, et ce, pour deux raisons : d’une part, les agents ne disposent pas d’un identifiant stable avec lequel s’enregistrer sur une API, et d’autre part, ils ne disposent d’aucun moyen natif pour payer ces API. Puisqu’ils ne disposent pas de ces données, ils ont souvent des difficultés à s’enregistrer sur ces logiciels, ce qui freine la croissance du commerce agentique. Les agents IA renoncent souvent complètement à ces tâches, déléguant à des opérateurs humains les étapes d’enregistrement, de sélection de modes de paiement et de génération de clés API. Il devient par conséquent très difficile pour les agents de tester et de comparer une multitude d’API.

Pour résoudre ce problème, nous avons créé Cloudflare Wallets. À partir d’aujourd’hui, vous pouvez [​obtenir un identifiant Cloudflare Wallets](https://cloudflare.pay) pour votre compte ; celui-ci vous fournira un nom d’utilisateur unique, afin de faciliter vos interactions avec les revendeurs. Vous pourrez prochainement configurer et utiliser votre identifiant Cloudflare Wallets pour payer vos achats d’API et de contenus.

Au début du mois, nous avons annoncé [​Monetization Gateway](https://blog.cloudflare.com/monetization-gateway/), un service conçu pour aider les clients de Cloudflare à recevoir les paiements associés à leurs sites web et leurs applications. Monetization Gateway prendra en charge les micro-paiements via le [​protocole x402](https://www.x402.org/), qui permet d’associer des paiements à des requêtes HTTP. Ces micro-paiements permettront de régler des services allant de l’inférence IA aux données en passant par les contenus. Si vous souhaitez effectuer ou recevoir des paiements pour des services via Monetization Gateway et d’autres [​points de terminaison compatibles x402](https://developers.cloudflare.com/agents/tools/payments/x402/), vous aurez besoin d’un identifiant Cloudflare Wallets. 

Cloudflare Wallets vous permettra de stocker des stablecoins, d’acheter des services et de recevoir des fonds sur Internet. Chaque compte associé à un identifiant Cloudflare Wallets pourra également créer des portefeuilles Virtual Wallets pour ses agents, leur permettant d’acheter des API, des outils MCP, des contenus et bien davantage. Vous pourrez définir des limites pour vos portefeuilles Virtual Wallets (par exemple, un montant alloué, une liste d’autorisation et un montant maximal par transaction), afin d’aider votre agent à effectuer des dépenses en toute sécurité depuis votre compte. Cela permettra à votre agent de tester de nombreuses API de manière fluide, avec des risques maîtrisés. Les détenteurs de portefeuilles auront la possibilité de partager leurs identifiants Cloudflare Wallets, ce qui leur fournira une identité stable lors de leurs interactions avec les revendeurs.

## **Construire un marché agentique bilatéral**

Le service [​Monetization Gateway](https://blog.cloudflare.com/monetization-gateway/) de Cloudflare permettra aux clients Cloudflare éligibles de vendre leurs ressources (telles que des contenus ou des API) sur une plateforme headless (sans interface) à des acheteurs agentiques. Pour que ce marché se développe véritablement, toutefois, les agents ont besoin de davantage d’outils leur permettant d’effectuer des achats auprès des revendeurs de manière « machine-native ». Les portefeuilles ajouteront un nouvel outil au SDK Agents de Cloudflare, permettant ainsi aux agents IA d’acheter facilement les API et les contenus nécessaires grâce à des micro-paiements.

Il existera deux types de portefeuilles Cloudflare Wallets : les portefeuilles Account Wallets et Virtual Wallets.

Les portefeuilles **Account Wallets** sont destinés aux opérateurs humains qui sont propriétaires et utilisateurs de comptes Cloudflare. Ils pourront ajouter des fonds, déléguer des dépenses à des portefeuilles Virtual Wallets gérés par des agents et retirer des fonds, selon leurs besoins. 

Les portefeuilles **Virtual Wallets** , en revanche, sont destinés aux agents et fonctionnent via des clés API. Dans un portefeuille Virtual Wallet, un agent pourra dépenser des fonds en fonction de ses autorisations. Les dépenses maximales autorisées seront plafonnées à la limite fixée par le titulaire du portefeuille Account Wallet. Ce cadre offre aux agents la liberté d’agir au nom des utilisateurs sans devoir demander une validation manuelle à chaque transaction, tout en limitant leur capacité à dépasser les budgets alloués.

## **La liberté d’explorer**

Les portefeuilles Virtual Wallets sont passionnants, car ils permettront aux agents de faire ce qu’ils savent faire de mieux : explorer des dizaines, voire des centaines de services, et trouver celui qui convient le mieux à un scénario d’utilisation particulier. Les micro-paiements en stablecoins effectués via le protocole x402 permettront de tester facilement une API sans devoir créer un compte, ce qui permettra aux agents d’expérimenter de nouvelles fonctionnalités de manière fluide. Les plafonds de dépenses associés aux portefeuilles Virtual Wallets sont conçus pour permettre aux opérateurs humains de confier aux agents le soin d’explorer des solutions de manière autonome, tout en limitant les dépenses. Ces limites peuvent sembler être des contraintes, mais, contrairement à ce que vous pourriez croire, elles offrent davantage de liberté aux agents. Si un agent dispose d’un budget de 10 dollars, vous n’avez pas à vous préoccuper autant de ses dépenses que s’il disposait d’un budget de 1 000 dollars. Si l’essai d’une API ne coûte que quelques centimes, 10 dollars suffisent largement pour explorer et évaluer de nombreuses possibilités.

Une fois que votre agent ou vous-même avez choisi une API à utiliser, les règles que vous aurez définies dans votre portefeuille Account Wallets serviront de mécanismes de contrôle des coûts pour les portefeuilles Virtual Wallets. Vous souhaitez attribuer à chaque collaborateur un budget hebdomadaire de 100 dollars pour l’inférence IA ? Provisionnez simplement un portefeuille Account Wallets avec le solde approprié, puis créez des portefeuilles Virtual Wallets pour chaque collaborateur en appliquant cette règle. Tout collaborateur dépassant les limites établies pour son portefeuille Virtual Wallets pourra demander une dérogation manuelle auprès d’un opérateur humain habilité à apporter des modifications au portefeuille Account Wallets.

Nous voulons permettre aux portefeuilles Account Wallets de définir facilement des règles de dépenses à la fois flexibles et strictes, ne nécessitant pas de suivi quotidien et actif. Si un événement inhabituel se produit (par exemple, des dépenses d’une rapidité inattendue), un opérateur humain pourra examiner ces dépenses et s’assurer que tout fonctionne comme prévu. Si les dépenses étaient intentionnelles, l’administrateur du portefeuille Account Wallets pourra alors augmenter la limite ou autoriser un versement de fonds ponctuel. Si ces dépenses étaient involontaires, cela signifie que les règles régissant l’approvisionnement des portefeuilles Virtual Wallets ont rempli leur rôle en imposant des plafonds.

Nous nous employons actuellement à faciliter au maximum l’approvisionnement et l’utilisation de ces portefeuilles. Nous commencerons par proposer des méthodes simples pour approvisionner et retirer des fonds dans les régions géographiques prises en charge, l’auto-financement via des stablecoins étant disponible comme alternative pour les utilisateurs éligibles. Internet ne se transformera pas du jour au lendemain ; toutefois, étant donné que [​la majeure partie du trafic web](https://radar.cloudflare.com/) est désormais générée par des bots, nous sommes ravis de fournir aux agents et aux revendeurs des outils d’exception dédiés au commerce agentique.

## **Au-delà des simples paiements**

Permettre aux opérateurs humains de déléguer des pouvoirs à des agents afin d’acheter et de vendre facilement des services constitue un bon point de départ. Toutefois, cette délégation n’est pas toujours facilement perceptible pour les revendeurs lorsqu’ils interagissent avec des agents. Aujourd’hui, lorsqu’un agent accède à votre site web, vous ne savez souvent pas grand-chose sur lui en tant qu’utilisateur, bien qu’il agisse pour le compte d’une personne physique ou d’une entreprise. Cette absence d’attribution remet en cause de nombreux modèles économiques traditionnels du web. Il est facile d’offrir un essai gratuit d’une semaine ou des crédits à l’enregistrement à un utilisateur humain ou une entreprise. En revanche, il est difficile d’accorder ces mêmes avantages à un agent qui ne dispose pas d’une identité stable, d’autant plus qu’un seul opérateur humain peut déployer des dizaines d’agents sous son contrôle.

Nous résolvons ce problème en associant les portefeuilles à un compte Cloudflare via [​](https://cloudflare.pay/)[cloudflare.pay](http://cloudflare.pay). [​](https://cloudflare.pay/)[cloudflare.pay](http://cloudflare.pay) permettra aux agents de s’identifier, si nécessaire, puisque leur identité est déléguée par le compte. Un agent de recherche pourrait résider à l’adresse [​research.example.cloudflare.pay](http://research.example.cloudflare.pay), par exemple, permettant aux revendeurs de savoir qu’il s’agit d’un agent d’une entreprise donnée. Cette approche permettra aux agents de conserver une identité cohérente et persistante, améliorant ainsi l’expérience pour toutes les parties concernées. Les agents seront entièrement libres de choisir de déclarer ou non leur identité, et il appartiendra aux entreprises de décider si elles souhaitent privilégier les transactions avec des agents connus.

## **Les identifiants d’agent doivent être lisibles par les opérateurs humains**

Nous pensons que l’approche régissant la prise en charge des agents sera similaire à l’approche appliquée aux VPN : si un utilisateur n’est pas identifié, cela ne signifie pas qu’il est intrinsèquement non fiable, mais il devra fournir davantage de preuves de sa légitimité. C’est pourquoi nous proposons [​Turnstile](https://www.cloudflare.com/products/turnstile/) et d’autres initiatives pour détecter les bots dans [​Bot Management](https://www.cloudflare.com/products/bot-management/), notre service gestion des bots. Notre composante fondamentale de gestion de l’identité s’appuiera sur ces travaux antérieurs. Par exemple, [​Web Bot Auth](https://developers.cloudflare.com/bots/reference/bot-verification/web-bot-auth/) permet déjà aux agents d’enregistrer leur identité via une paire de clés. Les identifiants associés à Cloudflare Wallets permettent de rendre cette paire de clés lisible par les opérateurs humains.

Nous savons que les normes en matière d’identité agentique évoluent rapidement ; c’est pourquoi nous avons souhaité opter pour une approche simple. Nous proposons un identifiant lisible par les opérateurs humains pour une paire de clés relativement peu lisible, semblable aux combinaisons d’URL et d’adresses IP utilisées dans [​DNS](https://www.cloudflare.com/learning/dns/what-is-dns/). Nous ne cherchons pas à définir un schéma particulier, ni aucun autre système de vérification. Notre seul objectif est de rendre l’identité facile à retenir et à déclarer. À mesure que des schémas visant à enrichir l’identité agentique se développeront grâce aux initiatives de [​x402 Foundation](https://blog.cloudflare.com/x402/), nous nous efforcerons de les adopter, et nous avons l’intention d’encourager d’autres acteurs à faire de même.

## **L’avenir du commerce agentique**

Chez Cloudflare, nous voulons fournir toutes les composantes modulaires indispensables à la réussite du commerce agentique. Monetization Gateway fournira aux revendeurs un moyen d’être payés sans devoir mettre en place une infrastructure de paiement conventionnelle. Les portefeuilles offriront aux acheteurs un moyen d’effectuer des paiements headless (sans interface) par l’intermédiaire d’agents. L’identité permettra aux revendeurs de communiquer avec les acheteurs qui s’identifient ou d’appliquer des exigences en matière d’identification.

Tous ces composants modulaires permettront la création d’une marketplace headless sur Internet. Si ce projet vous intéresse et vous souhaitez y participer, [​vous pouvez réserver votre identifiant dès maintenant](https://cloudflare.pay/). Nous sommes impatients de voir les solutions que vous allez développer et monétiser.

]]>01KZD5SQXXEE4QC1PH3H48Z31GPrésentation de l’API Billable Usage : visibilité programmatique des coûts pour Cloudflarehttps://blog.cloudflare.com/fr-fr/billable-usage-api/ Thu, 06 Aug 2026 07:17:18 GMTCloudflare has launched a new Billable Usage API for accounts, giving developers and FinOps teams single-endpoint programmatic visibility into cost and usage across all self-serve products. Built around the FOCUS specification, track spend seamlessly alongside the rest of your cloud stack.Agents WeekAPIBillingDéveloppeursIngénierieNouveautés produitsL’Agents Week est dédiée à l’évolution qui est déjà en cours : les agents écrivent du code, déploient des instances Workers et provisionnent l’infrastructure en votre nom. Or, cette évolution modifie ce que vous devez voir. Si un programme entraîne des dépenses sur votre compte Cloudflare, vous devez pouvoir examiner ces dépenses : au fil de la journée, par produit, sous une forme exploitable par un autre programme. Le tableau de bord est la solution idéale pour les humains, mais il n’est pas la solution idéale pour l’automatisation.

C’est pourquoi nous lançons la nouvelle **API Billable Usage** pour les comptes en libre-service : un point de terminaison unique qui renvoie l’utilisation et le coût de votre compte, répartis par produit et par période de service. Elle couvre tous les produits Cloudflare facturés à l’utilisation associés au compte, notamment Workers, R2, D1, Workers AI, Vectorize, Images et Stream – et tout cela, avec un seul appel. Et si vous utilisez déjà une chaîne d’outils FinOps, les intitulés des colonnes devraient vous sembler familiers.

Vous obtiendrez une réponse `HTTP 200 OK` avec `Content-Type: application`/`json` et les lignes décrivant l’utilisation dans le corps de la réponse. Actuellement, les données relatives à l’utilisation et aux coûts sont mises à jour quotidiennement, pendant que nous nous employons à fournir davantage de données en temps réel.

## **Ce qui revient**

Chaque ligne de la réponse correspond à une période de facturation pour un produit associé à votre compte.

  * `ServiceName` et `ServiceFamilyName` – le produit (« Workers Standard » sous la famille « Workers », « R2 Storage » sous « R2 », et ainsi de suite).
  * `ChargePeriodStart` / `ChargePeriodEnd` – la période couverte par cette ligne.
  * `PricingQuantity` et `ConsumedUnit` – la quantité consommée, exprimée dans l’unité de mesure utilisée pour la facturation (Go-mois, Go-secondes, requêtes, etc.).
  * `ContractedCost` – le coût de cette période, en `BillingCurrency`.
  * `CumulatedPricingQuantity` et `CumulatedContractedCost` – les totaux cumulés pour la période de facturation.
  * `ZoneId` / `ZoneName` – lorsque l’utilisation est attribuée à une zone spécifique.



La plupart de ces intitulés correspondent directement aux colonnes de la spécification [​FinOps Open Cost and Usage (FOCUS)](https://focus.finops.org/). Ainsi, si votre équipe importe déjà des données FOCUS depuis un autre fournisseur, les noms et la sémantique devraient vous paraître familiers :

**Champ Cloudflare**| **Colonne FOCUS**| **Remarques**  
---|---|---  
`BillingCurrency`| `BillingCurrency`| Correspondance exacte.  
`BillingPeriodStart`| `BillingPeriodStart`| Correspondance exacte.  
`ChargePeriodStart` / `ChargePeriodEnd`| `ChargePeriodStart` / `ChargePeriodEnd`| Correspondance exacte.  
`ServiceName`| `ServiceName`| Correspondance exacte.  
`ConsumedQuantity` / `ConsumedUnit`| `ConsumedQuantity` / `ConsumedUnit`| Correspondance exacte.  
`PricingQuantity`| `PricingQuantity`| Correspondance exacte.  
`ContractedCost`| `ContractedCost`| Correspondance exacte.  
`ServiceFamilyName`| (proche de `ServiceCategory`)| Regroupement propre à Cloudflare ; FOCUS emploie un vocabulaire normalisé.  
`CumulatedContractedCost`| (dérivé)| Champ de commodité – FOCUS considère le cumul comme une problématique liée aux requêtes.  
`ZoneId` / `ZoneName`| (proche de `ResourceId` / `ResourceName`)| Identifiant défini au niveau de la zone, le cas échéant.  
  
Les réponses utilisent l’enveloppe standard de l’API Cloudflare : `result` est un tableau de lignes (à raison d’une ligne par produit et par période de facturation), conjointement à `success`, `errors` et `messages`.

## **Où en sommes-nous avec FOCUS ?**

La conformité aux dénominations FOCUS est un choix délibéré. AWS, Azure, Google Cloud, Oracle et un nombre croissant de fournisseurs de solutions SaaS publient déjà des exportations au format FOCUS, et tous les outils de gestion des coûts dignes de ce nom prennent en charge ce format. Cela dit, nous ne prétendons pas encore proposer une conformité totale : à l’heure actuelle, quelques colonnes requises par la spécification ne sont pas encore incluses dans les données. Leur ajout est prévu dans notre feuille de route. Considérez cela comme une première étape : une forme familière pour l’instant, une conformité totale ensuite.

## **Vos dépenses dans Cloudflare, intégrées au reste de vos dépenses liées au cloud : notre partenariat avec Vantage**

Nous avons établi un partenariat avec [​Vantage](https://www.vantage.sh/) pour mettre en place une intégration native avec Cloudflare. Vantage est une plateforme de gestion des coûts d’infrastructure qui collecte les données relatives aux coûts et à l’utilisation auprès de plus de 30 fournisseurs, parmi lesquels des fournisseurs de solutions IA, cloud et SaaS, et les regroupe dans une vue unique à des fins de publication de rapports, d’affectation et d’optimisation. Grâce à cette intégration, vos données d’utilisation sont automatiquement renseignées dans les services Cost Reports, Budgets et Cost Alerts que vous utilisez déjà pour le reste de votre infrastructure.

Vantage se connecte à Cloudflare via un jeton d’API en lecture seule avec l’autorisation d’accès Billing Read. Une fois connecté, Vantage récupère quotidiennement vos données d’utilisation facturable et les répartit par produit (Workers et R2, par exemple), par zone et par compte, vous permettant ainsi d’identifier les produits à l’origine de vos dépenses et de les imputer aux équipes et aux services concernés.

Voici quelques exemples de flux de travail pris en charge par cette intégration :

  * **Répartition entre fournisseurs.** Regroupez les dépenses liées à Cloudflare par produit, par zone et par compte, puis utilisez les balises virtuelles pour les répartir par équipe ou par gamme de produits, parallèlement à vos coûts liés à AWS, Azure et d’autres fournisseurs – et tout cela, dans un rapport unique.
  * **Détection des anomalies.** Le service Vantage Cost Alerts surveille tous les fournisseurs connectés et vous notifie via Slack ou par e-mail lorsque les dépenses s’écartent de leur niveau de référence. Ainsi, toute variation des dépenses liées à Workers ou à R2 est signalée de la même manière que pour n’importe quel autre fournisseur.
  * **Agents FinOps et MCP.** Posez une question à l’agent Vantage FinOps intégré à la console, par exemple : « Quel a été notre principal facteur de coût la semaine dernière, tous fournisseurs confondus ? », ou interrogez Claude ou ChatGPT sur ces mêmes données via le serveur MCP hébergé par Vantage. Les dépenses liées à Cloudflare sont regroupées avec celles de vos autres fournisseurs connectés.



Connectez votre compte Cloudflare dans la [​console Vantage](https://console.vantage.sh/), et vos coûts sont affichés à côté de tous les autres services que vous utilisez. Il n’y a pas d’exportations manuelles, ni de téléchargements de factures, ni de tableau de bord distinct à gérer. 

Cette API normalisée FOCUS est également compatible avec d’autres outils Fintech.

## **Pourquoi l’avons-nous créée ?**

Les agents ne se contentent pas d’écrire du code. Ils déploient des instances Workers, créent des compartiments R2 et gèrent des bases de données D1. Lorsque vous accordez un accès programmatique à votre compte Cloudflare, vous devez bénéficier d’une visibilité programmatique des coûts qu’il entraîne – pas à la fin du mois, mais tout au long de la journée, par produit, sous une forme réellement exploitable par un programme.

L’API Billable Usage incarne cette forme, et cela fait des années que nos clients nous demandent de mettre en œuvre un accès programmatique à ces données. Les équipes financières souhaitent intégrer les dépenses dans leurs propres systèmes et imputer les coûts à leurs différents projets internes, à leurs équipes, et même à leurs clients finaux. Les développeurs, quant à eux, veulent une commande curl qu’ils puissent intégrer directement dans un script. Chacun de ces flux de travail nécessitait auparavant une capture d’écran ou une exportation manuelle. Désormais, il suffit d’un appel HTTP ou d’une configuration dans Vantage.

## **Les prochaines évolutions**

  * **Fenêtres temporelles plus précises.** Actuellement, l’API renvoie des lignes correspondant à la période de facturation, qui est quotidienne pour la plupart des produits. Nous envisageons d’intégrer davantage de répartitions en temps réel pour les produits, si cela s’avère pertinent.
  * **Prévisions.**`CumulatedContractedCost` vous indique l’état de vos dépenses dans le cycle de facturation en cours. Nous voulons vous aider à anticiper votre situation future – et pas seulement au niveau du compte, mais également au niveau des produits.
  * **Intégration à l’offre Enterprise.** Cette première version est accessible uniquement en libre-service. Une expérience équivalente pour les contrats Enterprise est en cours de développement.Try it



## **Essayez-le**

Le point de terminaison est disponible dès maintenant pour tous les comptes en libre-service. Sélectionnez un jeton d’API avec l’autorisation d’accès _Billing Read_ , renvoyez votre commande curl vers celui-ci et vous obtiendrez votre période de facturation actuelle, répartie par produit. Des informations complètes sont disponibles dans la documentation de l’API Cloudflare. Pour consulter ces informations parallèlement au reste de vos dépenses liées au cloud, connectez votre compte Cloudflare à la [​console Vantage](https://console.vantage.sh/).

Depuis des années, Cloudflare s’engage à vous permettre d’exécuter plus facilement une plus grande partie de votre infrastructure sur notre réseau. Il est temps pour nous de vous permettre de voir tout aussi facilement ce que cela vous coûte – sur Cloudflare, mais également sur toutes les autres plateformes.

]]>01KZAYGG4Q48FTS6EFSWBE9SB1Votre agent a besoin d’un ordinateur, pas d’un conteneur — découvrez @cloudflare/computerhttps://blog.cloudflare.com/fr-fr/cloudflare-computer/ Wed, 05 Aug 2026 03:16:15 GMTPour être extensibles, les agents ont besoin de plus qu’un simple conteneur. Nous lançons @cloudflare/computer, un environnement d’exécution d’agents qui orchestre dynamiquement l’utilisation d’isolats rapides et efficaces et de conteneurs Linux complets, afin de fournir à chaque agent son propre ordinateur.AgentsAgents WeekCloudflare WorkersConteneursIALes agents les plus performants ont tous un point commun très simple : ils disposent d’un ordinateur sur lequel s’exécuter.

Voici comment fonctionnent les agents de codage : vous leur fournissez un système de fichiers, un shell, des outils, des packages et la capacité d’exécuter du code. Ils inspectent l’environnement, effectuent des modifications, testent leur travail et poursuivent l’exécution de leur tâche. L’ordinateur offre au modèle un moyen familier d’interagir avec le monde. Chez Cloudflare, nous nous engageons à fournir les composantes fondamentales indispensables au développement des agents les plus performants.

**Aujourd’hui, nous proposons un premier aperçu de[ @cloudflare/computer](https://github.com/cloudflare/workspace).** Le package @cloudflare/computer fournit un environnement d’exécution d’agents dans lequel les détails et les mécanismes du code exécuté dans un isolat et du code exécuté dans une sandbox de conteneur sont gérés par la plateforme. Chaque agent dispose d’un ordinateur et l’environnement d’exécution est optimisé pour garantir l’efficacité et l’évolutivité.

Nous pensons que, pour répondre à la demande croissante de puissance de calcul des systèmes agentiques, nous devons réfléchir à des solutions qui vont au-delà de la conteneurisation traditionnelle. 

## Transformer l’approche du développement d’agents

Au cours des six derniers mois, nous avons assisté à une évolution subtile de cet aspect. Au début de l’année, la pratique courante consistait à créer un conteneur et à exécuter un agent dans celui-ci. Ces derniers mois, nous avons assisté à une évolution rapide des cadres d’exécution (« harness ») d’agents, qui permettent désormais l’exécution de code en sandbox via différents outils. Cette approche permet de séparer les « mains » (l’environnement de test où est effectué le travail) du « cerveau » (la boucle de l’agent).

Quel que soit l’environnement où cadre d’exécution est déployé, fournir un conteneur à chaque agent constitue un défi : entre tous les clouds et tous les hyperscalers, il n’y a, et de loin, pas assez de puissance de calcul dans le monde pour que chaque entreprise puisse fournir à chacun des agents de ses utilisateurs son propre environnement de calcul conteneurisé. Cette approche ne pourra simplement pas être adaptée à des centaines de millions, puis à des milliards d’agents déployés simultanément. C’est pourquoi le secteur manifeste un besoin urgent et pressant de puissance de calcul de processeurs (CPU), et pas uniquement de puissance de calcul de cartes graphiques (GPU).

Chez Cloudflare, nous nous employons depuis longtemps à résoudre ce problème, et nous avons élaboré une composante fondamentale de calcul plus efficace : les isolats. Nous avons fait ce pari, qui allait à l’encontre du consensus, il y a près de 10 ans, lorsque nous avons [lancé Cloudflare Workers](https://blog.cloudflare.com/introducing-cloudflare-workers/). Nous avons ensuite recommencé lorsque nous avons [lancé Durable Objects](https://blog.cloudflare.com/introducing-workers-durable-objects/), il y a près de six ans. Si nous avons fait ce pari, c’est parce que les isolats offrent une extensibilité horizontale illimitée. Ils peuvent être lancés et arrêtés avec une rapidité incroyable. Ils peuvent [hiberner](https://developers.cloudflare.com/durable-objects/examples/websocket-hibernation-server/) lorsque l’agent est inactif, [stocker l’état de l’agent lui-même](https://blog.cloudflare.com/sqlite-in-durable-objects/) et même [lancer leurs propres isolats](https://blog.cloudflare.com/dynamic-workers/) pour exécuter du code non fiable. Les isolats incarnent la meilleure solution pour l’évolutivité horizontale, et c’est précisément cette évolutivité horizontale que nécessitent les agents.

L’année dernière, nous avons [donné aux isolats la capacité de créer leurs propres sandboxes en conteneur](https://blog.cloudflare.com/containers-are-available-in-public-beta-for-simple-global-and-programmable/). Dès le départ, l’architecture de Cloudflare a été conçue pour déployer le cadre d’exécution d’agents dans l’isolat (dans une instance Durable Objects) et invoquer, à la demande, un conteneur associé en tant qu’outil. Cette approche vous permet d’exécuter des composantes fondamentales de calcul plus exigeantes en ressources uniquement en cas de nécessités seulement, et ainsi, d’optimiser à la fois les performances et les coûts. Les instances Durable Objects sont extensibles à l’infini horizontalement, et le conteneur associé leur permet de s’étendre verticalement afin d’accomplir n’importe quelle tâche. C’est ainsi que nous développons nous-mêmes nos agents, et nous voyons également nos clients réaliser des choses incroyables avec cette approche.

Toutefois, nous avons examiné la nécessité de disposer d’une multitude de composantes fondamentales de calcul sous-jacentes pour développer des agents (isolats et conteneurs), ainsi que le besoin pour nos clients et nos développeurs de les associer eux-mêmes dans l’espace utilisateur, et nous pensons pouvoir faire mieux. Nous pensons pouvoir proposer une abstraction plus simple.

C’est pourquoi nous lançons cette expérience en proposant @cloudflare/computer sous forme de bibliothèque open source, afin d’apprendre aux côtés de nos clients qui repoussent les limites de l’exécution d’agents à grande échelle.

## Un système de fichiers partagé entre isolats et conteneurs

Le package @cloudflare/computer part d’un postulat simple : et si nous fournissions à un agent un système de fichiers préconfiguré, défini de manière déclarative, contenant toutes les ressources nécessaires pour accomplir la tâche demandée, ainsi qu’un choix d’environnements d’exécution permettant de traiter ces fichiers, chacun présentant ses propres avantages et inconvénients en termes de rapidité de capacité et de coût ?

Il s’avère qu’aujourd’hui, les agents sont étonnamment capables de choisir l’environnement le mieux adapté à la tâche à accomplir. Une tâche consistant uniquement à manipuler des fichiers, à traiter des données ou à gérer un référentiel Git peut être exécutée dans un isolat. Une commande nécessitant Linux, `npm` ou un binaire natif peut être exécutée un conteneur. Les deux tâches sont exécutées sur les mêmes fichiers, qui sont synchronisés avec le système de fichiers source.

Le package @cloudflare/computer fournit un système de fichiers durable que vous pouvez utiliser avec des référentiels Git, des compartiments de stockage ou tout autre fichier de votre choix. Il fournit des outils qui vous permettent de lire, d’écrire et de modifier des fichiers via [Code Mode](https://blog.cloudflare.com/code-mode/) ou avec des commandes bash. Toutes les opérations comportent des contrôles d’accès et sont auditées et surveillées, offrant ainsi un contrôle extrêmement précis des modifications que l’agent est autorisé à effectuer et un historique écrit clair, détaillant les actions effectuées par l’agent.

## Comment l’utiliser

Une instance d’espace de travail @cloudflare/computer peut être créée dans n’importe quelle instance Durable Objects pour fournir un système de fichiers virtuel et un environnement d’exécution.

Son installation se déroule via npm :

Le scénario d’utilisation principal est la fourniture de ce système de fichiers et de ces outils à un agent. Par exemple, voici comment instancier l’espace de travail sur un agent utilisant @cloudflare/think, destiné à trier des rapports d’erreurs.

Plusieurs backends d’exécution sont fournis dans le package @cloudflare/computer, mais vous pouvez également créer le vôtre. Ici, nous connectons une instance de Cloudflare Container.

Nous mettons à disposition les outils de gestion de fichiers, Git et de shell, ainsi que les outils spécifiques au produit, afin de traiter les problèmes signalés.

Le modèle peut utiliser des outils pendant la boucle de l’agent, mais vous pouvez également utiliser directement l’API de l’espace de travail, par exemple, pour préparer l’environnement avant de saisir un prompt pour l’agent.

Consultez le [référentiel de l’espace de travail](https://github.com/cloudflare/computer) pour découvrir d’autres exemples d’utilisation des différents backends et outils, notamment un [tutoriel étape par étape](https://github.com/cloudflare/computer/tree/main/examples/tutorial) de création d’un agent.

## Comment cela fonctionne

L’élément central de @cloudflare/computer est l’espace de travail. Il s’agit d’un système de fichiers virtuel reposant sur SQLite, qui peut être alimenté depuis différentes sources, notamment un stockage cloud et un système de contrôle de version.

L’espace de travail prend en charge des environnements d’exécution optionnels qui permettent d’exécuter du code sur le système de fichiers. Tous les environnements d’exécution prennent en charge la même interface `exec(string, options)` et, à l’heure actuelle, deux environnements sont fournis prêts à l’emploi (toutefois, vous pouvez créer le vôtre) :

  * Un environnement d’exécution basé sur des isolats, qui utilise [just-bash](https://justbash.dev/) pour traduire le code shell en code JavaScript, s’exécute dans une [instance Workers dynamique](https://developers.cloudflare.com/dynamic-workers/). Ici, le système de fichiers est accessible directement via les liaisons Workers.
  * Un environnement d’exécution de conteneurs qui utilise [Cloudflare Containers](https://developers.cloudflare.com/containers/) pour fournir un environnement Linux complet. Ici, le système de fichiers est mis à disposition via un montage FUSE (Filesystem in Userspace), qui garantit que les fichiers sont accessibles au conteneur et que les modifications sont synchronisées en retour.



La classe `Workspace` fournit une interface API permettant de manipuler directement le système de fichiers, ainsi qu’un wrapper compatible avec `node:fs`, afin de faciliter son utilisation avec des bibliothèques JavaScript tierces.

Pour une utilisation avec les agents, nous proposons une boîte à outils compatible avec le SDK IA, comprenant les outils les plus courants : read, write, edit, ls et exec. L’outil exec est un peu particulier : il fonctionne avec l’ensemble des environnements d’exécution en acceptant un argument `backend`. La description de l’outil aide l’agent à choisir l’environnement d’exécution adapté à la tâche à accomplir : un backend Workers, rapide et économique, ou le conteneur, doté de fonctionnalités complètes. Lors de nos tests, les modèles les plus performants se sont révélés très efficaces pour prendre la décision pertinente et ne recourir aux conteneurs qu’en cas de nécessité.

## Et maintenant ?

Chez Cloudflare, nous voyons déjà des agents qui utilisent exclusivement des isolats pour développer, tester et déployer des applications JavaScript avec des outils modernes, générer une documentation sur mesure pour chacun de nos clients, et accéder à des navigateurs web pour exécuter des tâches complexes.

Notre objectif avec @cloudflare/computer est de proposer un agent avec un environnement d’exécution dans lequel un conteneur n’est nécessaire que pour moins de 10 % de son travail, et dans lequel les tâches de programmation, le traitement audio/vidéo et la création de documents peuvent toutes être gérées par des isolats. 

Découvrez [dès aujourd’hui la version en avant-première](https://github.com/cloudflare/computer). Nous sommes impatients de lire vos commentaires.

]]>01KZ7YAW233STZH0MSFZFK23JKBienvenue dans l’Agents Weekhttps://blog.cloudflare.com/fr-fr/agents-week-welcome/ Tue, 04 Aug 2026 03:27:14 GMTLors de l’Agents Week, nous examinerons comment l’infrastructure cloud doit évoluer pour servir les agents autonomes, et non plus la navigation humaine. Rejoignez-nous pour découvrir en détail les composantes primitives de stockage, d’exécution et de sécurité indispensables à la création d’un web agent-native.AgentsAgents WeekCloudflare WorkersIAPlateforme pour développeursCette semaine a lieu l’Agents Week.

Lorsque nous avons commencé à réfléchir à cette semaine et à planifier son déroulement, nous nous sommes intéressés à une question plus large : qu’implique la prise en charge de cette nouvelle ère des agents, et à quoi ressemble concrètement une fondation conçue spécialement pour eux ? Cette démarche nous a amenés à reformuler plus simplement la question : qu’est-ce qu’un cloud agentique ? 

Toutefois, nous avons rapidement pris conscience que notre approche était erronée, pas parce que la question ne mérite pas d’être posée, mais parce que nous la posions aux mauvaises personnes – à nous-mêmes, plutôt qu’à nos agents. Il ne s’agit plus de nous et de ce que nous pensons, mais de ce dont les agents ont besoin. 

Voilà, en quelques mots, ce qu’est l’Agents Week. 

Le cloud tel que nous le connaissons aujourd’hui, ainsi que le web sur lequel il repose, ont été conçus pour des utilisateurs humains. Chaque couche part du principe que les contenus sont consultés par un utilisateur humain : des pages conçues pour capter votre attention, des tableaux de bord à parcourir, des interfaces adaptées à notre façon de lire et de prendre des décisions. Cependant, les agents ne fonctionnent pas de cette manière ; ils ne se laissent pas distraire, ne fatiguent pas et ne ressentent pas de lassitude… et ils ont leurs propres exigences fondées sur la rapidité, la structure et l’accessibilité

Un cloud agentique doit faire deux choses à la fois. Il doit nous préparer à un avenir agent-native, dans lequel les composantes primitives sont fondamentalement conçues pour les agents, et non adaptées à partir d’outils destinés à des humains. Et, d’un point de vue réaliste, il doit être adapté à notre situation actuelle, en se comportant comme une couche de traduction entre le web pensé pour les humains que nous connaissons aujourd’hui et le web orienté agents vers lequel nous nous évoluons.

Voilà le fil conducteur de ces cinq prochains jours : la structure d’un cloud conçu pour les agents et les humains et leurs interactions. Pendant cette semaine, nous explorerons cette thématique en examinant les implications pour les composantes fondamentales et la couche d’exécution nécessaires, le cycle de vie actualisé du développement de logiciels agentiques, la manière dont les entreprises peuvent sécuriser les interactions de leur collaborateurs et de leurs agents avec des contrôles sûrs, la manière dont cette démarche définit le web agentique, et enfin, la manière d’ancrer tous ces paramètres dans la réalité actuelle des agents et des humains.

Pour en revenir à la question, qu’attend votre agent d’un cloud agentique ? Plutôt que de copier-coller les réponses que nous avons reçues de nos agents, nous vous invitons à poser cette question à votre agent et à partager avec nous les informations et réponses intéressantes que vous recueillerez. Voici un exemple de prompt que vous pouvez utiliser ; toutefois, nous vous encourageons à explorer les réponses que vous obtiendrez :

_Que tant qu’agent, qu’attends-tu d’un cloud agentique ? Réfléchis à tes besoins dans des catégories telles qu’un cloud de stockage et de calcul et les composantes fondamentales d’exécution et de stockage dont tu as besoin, ton cycle de vie de développement (l’ADLC, c’est-à-dire le SDLC sans intervention humaine), l’accès sécurisé aux systèmes d’information de l’entreprise pour exécuter des tâches en profondeur, et enfin, l’utilisation du web (découverte, accès, paiements, etc.)._

Laissez-nous un commentaire ici pour nous dire ce que vous répond votre agent. Nous serions ravis de découvrir vos réponses ! 

[Suivez l’actualité sur le blog cette semaine](https://blog.cloudflare.com/) pour découvrir les dernières innovations concernant les agents et[ rejoignez-nous sur X](https://x.com/CloudflareDev) pour participer à la conversation.

]]>01KZ5CT3WZ8DDKR0R7612JKDDKCatastrophes naturelles et ingérence des autorités : analyse des principaux incidents ayant perturbé le fonctionnement d’Internet au deuxième trimestre 2026https://blog.cloudflare.com/fr-fr/q2-2026-internet-disruption-summary/ Fri, 31 Jul 2026 06:35:37 GMTCloudflare Radar a recensé les perturbations d’Internet résultant de catastrophes naturelles, de coupures imposées par les autorités et de renouvellements de clés DNSSEC au cours du dernier trimestre. Cet article analyse les données télémétriques concernant le trafic afin d’expliquer l’impact de ces événements sur la connectivité dans le monde entier.AWSCoupure d'InternetPanneRadarTendances InternetTrafic InternetComme pour la plupart des infrastructures, nous avons tendance à sous-estimer la fragilité d’Internet, tant qu’il fonctionne. C’est lorsqu’il subit une panne que sa complexité se révèle au grand jour. Cloudflare occupe une position unique, qui lui permet de détecter et de consigner les moments où l’un des systèmes interconnectés dont dépend Internet subit une défaillance, entraînant des perturbations de la connectivité. Chaque trimestre, nous proposons un résumé des perturbations que nous avons détectées et annotées sur [Cloudflare Radar](https://radar.cloudflare.com/). 

Au deuxième trimestre 2026, le super-typhon Sinlaku, qui s’est abattu juste au nord de Guam, a provoqué la plus longue panne d’Internet, tandis que les coupures imposées par les autorités pendant les périodes d’examen au Soudan ont été les plus fréquentes. L’Iran a rétabli l’accès national à Internet, permettant à ses citoyens de se reconnecter au réseau mondial après une coupure de 88 jours, alors même que les dégâts causés par les frappes de drones continuaient de perturber l’infrastructure d’AWS ailleurs dans la région. Enfin, une coupure de câble à Sainte-Lucie et la diffusion de signatures DNSSEC erronées en Allemagne ont mis en évidence la fragilité de l’infrastructure d’Internet, mais également la remarquable stabilité dont font preuve ces systèmes régionaux et mondiaux lorsqu’ils fonctionnent normalement.

Dans cet article, nous allons passer en revue les plus importantes perturbations d’Internet observées au cours du deuxième trimestre de 2026, en nous appuyant sur les données de trafic observées par Cloudflare Radar pour montrer comment s’est déroulé chaque incident et les conséquences concrètes qu’il a eues pour les utilisateurs. Comme toujours, cet article propose un résumé des perturbations notables et confirmées, plutôt qu’une liste exhaustive ; une vue d’ensemble plus complète des anomalies de trafic détectées est disponible sur le portail [Cloudflare Radar Outage Center](https://radar.cloudflare.com/outage-center?dateStart=2026-04-01&amp;dateEnd=2026-06-30). 

## Des catastrophes naturelles et des incidents liés à la distribution d’électricité entraînent des perturbations à Guam, au Venezuela et en Tanzanie

Le super-typhon Sinlaku, la tempête la plus violente de la saison 2026 des typhons du Pacifique à ce jour, a traversé les îles Mariannes à la mi-avril, passant juste au nord de Guam. Bien que l’île ait échappé à un impact direct, la tempête a entraîné des vents violents, caractéristiques d’une tempête tropicale, provoquant des coupures d’électricité dans l’ensemble de Guam et perturbant les réseaux de distribution d’eau, ce qui a eu un impact direct sur la connectivité Internet. Du 13 au 14 avril, le trafic en provenance de ce territoire a chuté de près de 80 % par rapport aux niveaux attendus.

Deux mois plus tard, le 24 juin, deux séismes majeurs ont secoué le nord du Venezuela à environ une minute d’intervalle, à Yumare et à San Felipe, suivis d’une réplique près de la côte, à l’extérieur de Caracas. Le premier tremblement de terre, d’une magnitude de 7,5, s’est produit vers 22h04 UTC (18h04 heure locale). L’impact immédiat de ces événements est visible dans Radar, qui indique une forte baisse du nombre d’octets HTTP transférés au moment même où les séismes se sont produits. Cette baisse est particulièrement visible chez Fibex Telecom qui, selon les [données d’APNIC](https://stats.labs.apnic.net/aspop/), compterait près de 1,6 million d’utilisateurs. Elle est également observable chez [CANTV](https://radar.cloudflare.com/traffic/as8048?dateStart=2026-06-24&amp;dateEnd=2026-06-25#traffic-trends), l’opérateur historique public, et chez [VNET](https://radar.cloudflare.com/traffic/as263703?dateStart=2026-06-24&amp;dateEnd=2026-06-25), un fournisseur d’accès Internet régional de taille légèrement inférieure.

Quelques jours plus tard, de l’autre côté de l’Atlantique, une panne d’électricité survenue en Tanzanie le 27 juin a entraîné une forte baisse du trafic HTTP, qui a duré au moins cinq heures. Bien que les causes soient différentes de celles de la coupure d’Internet liée à la tenue d’élections dans le pays en octobre 2025 (une mesure délibérée des autorités, plutôt qu’une défaillance des infrastructures), les conséquences au regard de la télémétrie et de l’impact sur les utilisateurs ont été pratiquement identiques : une interruption drastique de la connectivité qui a empêché les habitants de communiquer avec leurs proches et les a privés d’informations essentielles. 

Il est frappant de constater que des événements aussi fondamentalement différents laissent des traces aussi semblables au niveau des données et de l’expérience utilisateur. Prises ensemble, ces perturbations liées aux conditions météorologiques et à la distribution d’électricité démontrent l’impact considérable que peut avoir le monde physique sur le monde numérique, ainsi que l’importance de la résilience d’Internet et de la construction de réseaux dotés d’une redondance suffisante en matière d’énergie, de routage et de liaisons physiques, afin de résister aux chocs inévitables.

## Les autorités et la géopolitique affectent la connectivité en Iran, aux Émirats arabes unis, en Irak et au Soudan

À partir du 26 mai, Radar a commencé à observer les premiers signes du rétablissement précédemment [annoncé](https://x.com/ir_aref/status/2059261258566877640?s=20) de l’accès à Internet en Iran, marquant la fin provisoire d’une coupure de 88 jours durant laquelle le pays était resté presque entièrement déconnecté depuis le 28 février. Le 27 mai, Radar [a rapporté](https://blog.cloudflare.com/iran-internet-partially-restored-may-2026/) que le trafic était remonté à 40 % du niveau précédant la coupure, une réouverture partielle qui corrobore les informations selon lesquelles l’accès était rétabli de manière sélective, plutôt qu’en une fois. Depuis, nous avons constaté une augmentation atteignant 90 % du volume d’octets HTTP, qui s’est ensuite stabilisé à environ 59 % des niveaux relevés avant la coupure. Ce volume correspond au trafic que nous avions observé en février, une période entre cette récente coupure et la précédente, survenue au mois de janvier ; cela suggère que la connectivité est revenue à un niveau proche du volume de référence observé avant la dernière coupure, sans toutefois s’être complètement normalisée. Dans notre [analyse de la Coupe du monde 2026](https://blog.cloudflare.com/2026-world-cup-internet-traffic/#streaming-makes-some-countries-appear-more-online), l’Iran s’était démarqué comme un cas à part : alors que le trafic dans la plupart des pays participants fluctuait au gré du calendrier des matchs, les données iraniennes étaient, quant à elles, marquées par le contraste entre les niveaux enregistrés après le rétablissement d’Internet et la coupure quasi totale de connectivité qui l’avait précédé.

À cette période, le trafic HTTP vers me-central-1, une région du cloud AWS située aux Émirats arabes unis, est [resté faible](https://radar.cloudflare.com/cloud-observatory/amazon/me-central-1?dateRange=24w#http-traffic), corroborant les [rapports de service publiés par AWS](https://health.aws.amazon.com/health/status#multipleservices-me-central-1_1777533954) le 30 avril, qui indiquaient que la région « a subi des dommages résultant du conflit au Moyen-Orient et n’est actuellement pas en mesure d’assurer une prise en charge fiable des applications de clients ». Cette mise à jour fait suite à des informations publiées le 3 mars, indiquant que des installations situées aux Émirats arabes unis et à Bahreïn « ont subi des dégâts matériels affectant leur infrastructure, résultant d’attaques de drones ». Aux Émirats arabes unis, deux installations ont été « directement touchées » et, à Bahreïn, une attaque de drone à proximité d’une installation a causé des « dégâts matériels » à son infrastructure. La diminution du trafic est symptomatique des dommages matériels à l’infrastructure sous-jacente du datacenter, et non d’une défaillance du réseau ; elle continue d’affecter les applications et les sites web hébergés dans cette région, indépendamment de leur disponibilité.

Le deuxième trimestre de 2026 a également été marqué par trois coupures d’Internet imposées par les autorités en Irak (le [2 juin](https://radar.cloudflare.com/traffic/iq?dateStart=2026-06-01&amp;dateEnd=2026-06-02), le [11 juin](https://radar.cloudflare.com/traffic/iq?dateStart=2026-06-10&amp;dateEnd=2026-06-11) et le [28 juin](https://radar.cloudflare.com/traffic/iq?dateStart=2026-06-27&amp;dateEnd=2026-06-28)), ainsi que [10 coupures au Soudan](https://radar.cloudflare.com/traffic/sd?dateStart=2026-04-13&amp;dateEnd=2026-04-23#traffic-trends) survenues entre le 13 et le 23 avril, toutes imposées afin d’empêcher la tricherie scolaire lors des examens nationaux. Il s’agit d’un phénomène saisonnier que nous avons documenté lors de plusieurs trimestres précédents dans ces deux pays. Les coupures d’Internet au Soudan se sont succédé à un rythme régulier, chacune durant environ 3 heures et demie, de 11h45 à 15h15 UTC (de 13h45 à 17h15, heure locale), coïncidant avec le calendrier des examens. En Irak, les coupures d’Internet ont été plus brèves, d’une durée d’environ 90 minutes chacune, et ont également été programmées aux horaires auxquels se déroulaient les examens.

Chacun de ces exemples, qu’il s’agisse d’un rétablissement ou d’une perturbation, illustre le contrôle considérable qu’exercent les autorités sur la connectivité nationale, ainsi que la facilité avec laquelle l’accès peut être coupé, limité ou sélectivement rétabli dans le cadre d’une décision politique, plutôt que pour des raisons liées à l’infrastructure.

## Des vulnérabilités de l’infrastructure affectent les utilisateurs en Allemagne et à Sainte-Lucie 

Le 5 mai, un renouvellement de clés DNSSEC chez DENIC, le registre du domaine .de allemand, [a commencé à générer des signatures non valides](https://blog.denic.de/technische-storung-bei-de-domains-behoben/). Ces renouvellements de clés constituent le remplacement périodique des clés cryptographiques utilisées pour signer les enregistrements DNS d’une zone. Il s’agit d’une opération de maintenance courante, mais essentielle, car les résolveurs qui valident le protocole DNSSEC font uniquement confiance aux réponses dont les signatures correspondent aux clés actuellement publiées. En d’autres termes, si les signatures numériques ne correspondent pas aux valeurs attendues, le résolveur considère que le site a été altéré et en interdit l’accès. Lorsque des signatures non valides ont commencé à être générées, les résolveurs de validation du monde entier ont rejeté toutes les requêtes concernant un site web .de et ont renvoyé des erreurs SERVFAIL jusqu’à ce que le fonctionnement normal soit rétabli, à 23h15 UTC (1h 15, heure locale, le 6 mai). 

Cloudflare Radar a constaté une augmentation du volume de requêtes .de dans le monde entier pendant la durée de la panne. Bien que cela puisse paraître contre-intuitif au premier abord, ce phénomène s’explique par le fait que les réponses d’échec ne peuvent pas être mises en cache. Par conséquent, des requêtes qui auraient normalement été servies de manière transparente depuis le cache ont dû être résolues et réitérées à plusieurs reprises, entraînant une forte augmentation du volume de requêtes.

Du point de vue des utilisateurs, cet incident n’a pas été perçu comme une défaillance du DNS ou des systèmes de cryptographie, mais simplement comme une vague de sites web et de services .de devenus soudainement inaccessibles. Les utilisateurs pouvaient toujours accéder aux sites qui n’utilisaient pas le domaine de premier niveau .de , mais ils se heurtaient à des échecs de chargement de pages, à des rejets d’e-mails et à des dépassements de délais d’attente d’applications – autant de phénomènes évocateurs d’une panne. Vous pouvez en apprendre davantage sur le protocole DNSSEC et l’impact des événements [dans notre article de blog](https://blog.cloudflare.com/de-tld-outage-dnssec/).

Dans les Caraïbes, une défaillance d’infrastructure a entraîné une baisse similaire de la disponibilité. Le 21 juin, le trafic de requêtes HTTP provenant du réseau de Karib Cable est tombé pratiquement à zéro vers 21 h UTC (17 h, heure locale), puis est resté stable pendant une grande partie de la journée avant de revenir aux niveaux attendus vers 17 h UTC le 22 juin (13 h, heure locale). La panne aurait, [selon certaines sources](https://stluciatimes.com/181838/2026/07/flow-reveals-details-of-customer-rebates-after-major-outage/), été causée par une rupture de fibre optique près de l’île. Ce risque est bien connu affectant les réseaux dans les Caraïbes, qui dépendent d’un nombre restreint de liaisons terrestres et sous-marines pour se connecter à l’Internet mondial ; une seule rupture peut dès lors entraîner une perte disproportionnée de capacité. Karib Cable étant l’un des principaux fournisseurs, cette interruption a également eu des répercussions à l’échelle nationale : le trafic global de Sainte-Lucie [a chuté d’environ 60 % par rapport à la semaine précédente](https://radar.cloudflare.com/explorer?dataSet=netflows&amp;loc=LC&amp;dt=2026-06-21_2026-06-27&amp;timeCompare=1#result) pendant toute la durée de la coupure.

### Radar continue de surveiller les perturbations

Des perturbations d’Internet ont été observées au cours du deuxième trimestre de 2026 ; elles résultaient de causes très diverses, parmi lesquelles des événements météorologiques extrêmes, un tremblement de terre, des coupures d’électricité, des coupures ordonnées par les autorités, des dégâts à l’infrastructure de cloud, des ruptures de câbles et une configuration erronée du protocole DNSSEC. Comme le démontrent ces événements, Internet repose sur un ensemble complexe de systèmes interconnectés, et toute défaillance de l’un de ces systèmes peut entraîner une interruption de la connectivité.

L’équipe Cloudflare Radar surveille continuellement les perturbations sur Internet et partage ses observations sur le portail [Cloudflare Radar Outage Center](https://radar.cloudflare.com/outage-center), sur les réseaux sociaux et dans des articles publiés sur [blog.cloudflare.com](http://blog.cloudflare.com). Suivez-nous sur les réseaux sociaux : [@CloudflareRadar](https://twitter.com/CloudflareRadar) (X), [noc.social/@cloudflareradar](https://noc.social/@cloudflareradar) (Mastodon) et [radar.cloudflare.com](http://radar.cloudflare.com) (Bluesky).

]]>01KYVDYQM9V5AEFBVZPDW6R43Z
