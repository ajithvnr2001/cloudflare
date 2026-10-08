---
url: https://blog.cloudflare.com/de-de/rss/
title: Der Cloudflare-Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:18:05.740299+00:00
---

# Der Cloudflare-Blog

> Source: https://blog.cloudflare.com/de-de/rss/

Der Cloudflare-BlogTiefgehende technische Beiträge, Produktupdates und Einblicke der Teams, die dabei helfen, ein besseres Internet aufzubauen.https://blog.cloudflare.com/de-de/ de-dehttps://blog.cloudflare.com/favicon.icoDer Cloudflare-Bloghttps://blog.cloudflare.com Thu, 08 Oct 2026 08:18:00 GMTWir bauen eine postquantensichere Zertifizierungsstelle mit Merkle Tree Certificates aufhttps://blog.cloudflare.com/de-de/pq-ca-with-mtcs/ Thu, 08 Oct 2026 03:12:50 GMTPostquantensichere Signaturen könnten den Datenumfang von TLS-Handshakes und Zertifikatstransparenz-Logs erheblich vergrößern. Merkle Tree Certificates ermöglichen dagegen eine kompakte, überprüfbare Authentifizierung. Die neue Zertifizierungsstelle von Cloudflare wird die Ausstellung von MTCs in großem Umfang unterstützen.Birthday WeekCertificate TransparencyKryptographiePost-Quanten-KryptographieSicherheitTLSWenn Sie eine Adresse in Ihren Browser eingeben, woher wissen Sie dann, dass Sie mit der richtigen Website verbunden sind? Die Web Public Key Infrastructure (WebPKI) ist ein komplexes, verteiltes Ökosystem aus Richtlinien, Protokollen und Infrastrukturbetreibern. Sie schafft die Vertrauensgrundlage dafür, dass Sie nicht auf eine falsche oder schädliche Website umgeleitet werden. In den vergangenen Jahrzehnten hat dieses Ökosystem erhebliche Veränderungen durchlaufen. Eine davon ist die Einführung von Transparenz: Alle Zertifikate müssen inzwischen in öffentlichen Zertifikatstransparenz-Logs erfasst werden. Nun steht die WebPKI vor einer weiteren Herausforderung: Quantencomputer, die heutige kryptografische Verfahren brechen können, rücken näher. Deshalb stellen wir unsere Kryptografie bis [2029](https://blog.cloudflare.com/post-quantum-roadmap/) auf postquantensichere Verfahren (PQ-Kryptografie) um.

Diese Umstellung ist jedoch nicht einfach: Würden wir die bisherige Kryptografie in Zertifikaten lediglich durch postquantensichere Verfahren ersetzen, käme es bei einem Einsatz im gesamten Internet zu inakzeptablen Leistungseinbußen. Deshalb brauchen wir einen neuen Ansatz für die WebPKI, bei dem Transparenz von Anfang an ein fester Bestandteil ist. Zugleich muss das neue System postquantensichere Signaturen auch in großem Umfang effizient verarbeiten können.

[Merkle Tree Certificates](https://datatracker.ietf.org/doc/draft-ietf-plants-merkle-tree-certs/?cf_target_id=D8F4225FC6E118E467AD5CD695831C8E) (MTCs) finden inzwischen breite Unterstützung in der Branche und haben sich als Ansatz für die weitere Entwicklung herauskristallisiert. Nach einem erfolgreichen experimentellen Einsatz [gemeinsam mit Chrome](https://blog.cloudflare.com/bootstrap-mtc/) treibt Cloudflare die Arbeit an MTCs in diesem Jahr mit voller Kraft voran.

Heute haben wir angekündigt, dass Cloudflare eine eigene [Zertifizierungsstelle](https://blog.cloudflare.com/cloudflare-certificate-authority/) (CA) aufbaut. Diese CA wird auch MTCs ausstellen. Wir streben ihre Aufnahme in den neu eingeführten [Quantum-resistant Root Store](https://googlechrome.github.io/chromerootprogram/index.html?cf_target_id=827C7A21FD45C25C3052C43A9BEC82F0) von Chrome für Anfang 2027 an. Im Rahmen unserer Mission, zum Aufbau eines besseren Internets beizutragen, und getreu unserer Tradition, die stärkste verfügbare Kryptografie [kostenlos](https://blog.cloudflare.com/post-quantum-crypto-should-be-free/) anzubieten, werden wir die standardmäßige Ausstellung von MTCs kostenlos bereitstellen. Mit einer CA, die sowohl klassische Zertifikate als auch MTCs ausstellt, können wir standardmäßig die sicherste verfügbare Authentifizierungsmethode einsetzen. So ermöglichen wir einem großen Teil des Internets einen reibungslosen Umstieg auf postquantensichere Authentifizierung bei hoher Leistungsfähigkeit.

## **Das aktuelle Vertrauensökosystem**

Um zu verstehen, was sich durch MTCs verändert, sehen wir uns zunächst an, wie Vertrauen im heutigen Web funktioniert.

Auf der Clientseite betreiben Browserhersteller Root-Programme für ihre Browser, die hier als TLS-Clients fungieren. Diese Programme legen die Richtlinien fest, die Zertifizierungsstellen einhalten müssen, um als vertrauenswürdig anerkannt zu werden. Auf der Serverseite übernehmen CAs eine zentrale Rolle: Sie betreiben die Infrastruktur zur Zertifikatsausstellung, prüfen die Kontrolle über eine Domain und bestätigen die Zuordnung eines Domainnamens zu einem öffentlichen Schlüssel.

Wie überprüfen wir aber, ob CAs die Regeln einhalten? Hier kommt die Zertifikatstransparenz (Certificate Transparency, CT) ins Spiel. Sie macht die Zertifikatsausstellung öffentlich überprüfbar. Wenn eine CA ein Zertifikat ausstellt, muss sie es auch in mindestens zwei öffentliche Logs eintragen. Cloudflare betreibt seit 2016 die CT-Log-Familie [Nimbus](https://blog.cloudflare.com/introducing-certificate-transparency-and-nimbus/) und führt mit Raio eine neue Familie [statischer CT-Logs](https://blog.cloudflare.com/azul-certificate-transparency-log/) ein.

Das CT-Ökosystem macht Zertifikate zwar öffentlich einsehbar. Das allein garantiert jedoch nicht, dass sie korrekt ausgestellt wurden oder sicher verwendet werden können. Monitoring hilft dabei, indem es die Log-Einträge mit den Erwartungen der Domaininhaber abgleicht und verdächtige Aktivitäten meldet. Cloudflare hat das [Certificate Transparency Monitoring](https://blog.cloudflare.com/introducing-certificate-transparency-monitoring/) 2019 eingeführt und kürzlich [allgemein verfügbar](https://blog.cloudflare.com/certificate-transparency-monitoring-ga/) gemacht. Außerdem veröffentlichen wir umfangreiche Messdaten zu Zertifikaten auf der [Certificate Transparency-Seite](https://radar.cloudflare.com/certificate-transparency?cf_page=pq-ca-with-mtcs%2F&cf_target_id=6A736CE68127335908FF7FAE938E2924) von Cloudflare Radar, die früher als Merkle Town bekannt war.

Wenn Unternehmen ihre Server auf postquantensichere Authentifizierung umstellen, wird CT-Monitoring noch wichtiger, um mögliche Rückstufungen auf klassische Authentifizierung zu erkennen. Domaininhaber, die ihre Domains bereits umgestellt haben, sollten CT-Logs auf unerwartet ausgestellte klassische Zertifikate überwachen. So können sie verhindern, dass Clients durch einen böswillig herbeigeführten Downgrade auf weniger sichere Authentifizierung zurückfallen.

Ein Problem des heutigen Systems ist, dass Transparenz erst nachträglich ergänzt wurde. Das führt zu Schwierigkeiten bei der Skalierung. Zertifikate werden häufig mehrfach und in unterschiedlichen Formen in verschiedenen Logs erfasst. Monitoring-Systeme müssen deshalb jedes Log herunterladen und verarbeiten, um keine Zertifikatsausstellung zu übersehen. Das kann teuer werden – und erschwert es, eine vielfältige Landschaft von Log-Betreibern zu fördern, die das gesamte Internet abdecken kann. Nach unseren Schätzungen werden PQ-Signaturen die Datenmenge, die CT-Logs speichern müssen, auf das 40-Fache erhöhen. Diese Skalierungsprobleme und die damit verbundenen Fehlanreize bilden den Kern des Skalierungsproblems bei postquantensicheren Zertifikaten.

## **Das Skalierungsproblem bei postquantensicheren Zertifikaten**

Wir haben ausführlich über die [Herausforderungen bei der Skalierung postquantensicherer Kryptografie geschrieben](https://blog.cloudflare.com/bootstrap-mtc/). Kurz gesagt: Um die Serverauthentifizierung im gesamten Internet zu ermöglichen, muss die WebPKI rund eine Milliarde TLS-Server authentifizieren können, ohne den öffentlichen Schlüssel jedes einzelnen Servers vorab auf jedem Client zu hinterlegen. Traditionell lösen CAs dieses Problem mithilfe von Zertifikatsketten, über die das Vertrauen weitergegeben wird. Im Laufe der Zeit sind jedoch weitere Verfahren hinzugekommen, etwa Prüfungen auf Widerruf und Zertifikatstransparenz. Dadurch müssen zusätzliche öffentliche Schlüssel und Signaturen übertragen werden – in einem typischen TLS-Handshake sind es fünf Signaturen und zwei Schlüssel. PQ-Signaturen sind etwa 40-mal so groß wie klassische Signaturen. Der zusätzliche Datenumfang würde bei einem Einsatz in großem Umfang erhebliche Kosten für Clients, CAs, Logs und Monitoring-Systeme verursachen.

Hier kommen [Merkle Tree Certificates](https://datatracker.ietf.org/doc/search?name=draft-ietf-transcert-merkle-tree-certs&rfcs=on&activedrafts=on&olddrafts=on&cf_target_id=51684921222E639F7C99A8DB083EF557) (MTCs) ins Spiel. Der Spezifikationsentwurf der PLANTS-Arbeitsgruppe der [IETF](https://datatracker.ietf.org/group/plants/about/?cf_target_id=B59CA5E8CF3039AB7E98001FBECA4447) beschreibt eine Architektur für kompakte, effiziente und postquantensichere Zertifikate. MTCs bündeln Zertifikate in einem Merkle-Tree, der nur um neue Einträge erweitert werden darf (Append-only). So kann eine CA die Wurzel des Trees signieren, statt jedes Zertifikat einzeln zu signieren. Browser und andere Clients können dann mithilfe eines kompakten Inklusionsbeweises – einer Folge kryptografischer Hashwerte, die die Aufnahme in den Tree belegt – prüfen, ob ein Zertifikat zum signierten Treekopf gehört. Eine [zentrale Idee](https://datatracker.ietf.org/meeting/124/materials/slides-124-plants-solution-space-and-dispatched-work-00?cf_target_id=B04188179B028E9978022BAEB3B3B91C) hinter MTCs lautet: „Nicht erst ausstellen und dann protokollieren, sondern durch das Protokollieren ausstellen.“ Durch die Kopplung von Ausstellung und Protokollierung wird Transparenz zu einer Voraussetzung für den Betrieb statt zu einer nachträglichen Ergänzung.

## **Die Rolle einer Zertifizierungsstelle in einer neu gestalteten PKI**

Wir entwickeln die Infrastruktur zur Ausstellung von MTCs als festen Bestandteil unserer neuen Cloudflare-CA. Dabei müssen wir die neuen Anforderungen der Root-Programme für postquantensichere Zertifikate berücksichtigen und gleichzeitig die Software für Ausstellung und Spiegelung entwickeln. Parallel dazu bauen wir die Einrichtungen, Betriebsabläufe und Compliance-Strukturen einer klassischen CA auf – eine anspruchsvolle Aufgabe!

Der Vorteil ist, dass wir die Anforderungen und die Architektur dieser neuen, postquantensicheren PKI von Anfang an berücksichtigen können. Wir richten unsere Infrastruktur an den Werten und dem globalen Netzwerk von Cloudflare aus. Dabei wollen wir den Aufbau so transparent wie möglich gestalten.

Sehen wir uns die für MTCs angepasste Architektur an:

Im Vergleich zum klassischen CA-Ökosystem bleiben die Aufgaben einer CA weitgehend gleich: Sie prüft die Kontrolle über eine Domain, bestätigt die Zuordnung zu einem öffentlichen Schlüssel und stellt Zertifikate aus. Der wesentliche Unterschied besteht darin, dass die CA im MTC-Ökosystem Zertifikate nicht mehr direkt signiert und anschließend protokolliert. Stattdessen betreibt sie ein Transparenz-Log auf Grundlage eines Merkle-Trees. Ein Inklusionsbeweis belegt, dass ein Zertifikat in diesem Tree enthalten ist, und ermöglicht dessen Überprüfung anhand eines vertrauenswürdigen, signierten Treezustands. CAs werden außerdem Dienste zur Spiegelung und Mitunterzeichnung betreiben, sogenannte Mirroring Cosigners. Diese speichern eine Kopie der Ausstellungs-Logs, prüfen, dass neue Einträge lediglich angehängt und bestehende Einträge nicht verändert werden, und stellen die Transparenz und Verfügbarkeit der Logs für das gesamte Ökosystem sicher.

### **MTCs ausstellen**

MTCs gibt es in zwei Varianten. Beide lassen sich im X.509-Zertifikatsformat kodieren, das heutige Clientsoftware bereits erkennt – allerdings mit einem „ungewöhnlichen“ Signaturalgorithmus. Bei der eigenständigen Variante enthält das Signaturfeld des Zertifikats einen mitunterzeichneten Treekopf eines Ausstellungs-Logs und einen Inklusionsbeweis. Dieser besteht aus einer Folge von Hashwerten und belegt, dass das Zertifikat im Log enthalten ist. Können Clients die mitunterzeichneten Treeköpfe außerhalb der TLS-Verbindung erhalten (Out-of-band), etwa über den Aktualisierungsmechanismus ihres Browsers, lässt sich stattdessen die Landmark-relative Variante verwenden. Deren Signaturfeld enthält nur den kompakten Inklusionsbeweis und keine umfangreichen postquantensicheren Signaturen.

Zur Veranschaulichung betrachten wir die Ausstellung eines eigenständigen Zertifikats. Benötigt eine Website ein Zertifikat für ihre Domain, kann ihr Betreiber es über das Automatic Certificate Management Environment (ACME)-Protokoll bei einer CA beantragen. ACME regelt Zertifikatsanfragen, die Prüfung der Kontrolle über eine Domain und die Abläufe bei der Ausstellung. Cloudflares ACME-Infrastruktur wird auf einem Fork von [Boulder](https://github.com/letsencrypt/boulder?cf_target_id=3E95756BE59ACCE65BC845D429788CE9) basieren, der weitverbreiteten und bewährten ACME-Software hinter Let’s Encrypt. Let’s Encrypt arbeitet aktiv an der Unterstützung von [MTCs](https://letsencrypt.org/2026/06/03/pq-certs?cf_target_id=BB65E529DD73C620BE6606E6D5425A59) in Boulder. Wir planen, einen eigenen Fork zu pflegen, der diese Änderungen aus dem ursprünglichen Projekt mit Cloudflare-spezifischen Anpassungen kombiniert. Wo möglich, werden wir unsere Verbesserungen auch in das ursprüngliche Projekt einbringen.

Geht bei der MTC-CA eine Anfrage zur Zertifikatsausstellung ein, prüft ihr ACME-Server, ob der Antragsteller tatsächlich die Kontrolle über die Domain hat. Nach erfolgreicher Prüfung serialisiert die CA die Daten und fügt sie einem Log hinzu, das ausschließlich um neue Einträge erweitert werden darf.

Nachdem der MTC-Eintrag zum Ausstellungs-Log hinzugefügt wurde, berechnet die CA den aktualisierten Zustand des Logs und signiert einen Checkpoint, der diesen Zustand beschreibt. Der Checkpoint bestätigt, dass die CA sämtliche Einträge ausgestellt hat, die bis zu diesem Zeitpunkt im Merkle-Tree des Logs enthalten sind.

Anschließend sendet die CA den aktualisierten Log-Zustand und den neuen Checkpoint an einen vertrauenswürdigen Mitunterzeichner. Dieser speichert dauerhaft eine Kopie des Ausstellungs-Logs und prüft, dass der neue Zustand ausschließlich durch das Anhängen neuer Einträge entstanden ist, mit dem vorherigen Tree konsistent ist und korrekt aufgebaut wurde. Die zusätzliche Mitunterzeichnung gibt Clients und Monitoring-Systemen die Gewissheit, dass eine weitere vertrauenswürdige Partei denselben Log-Zustand gesehen und überprüft hat. Sie bestätigt damit, dass die CA verschiedenen Teilen des Ökosystems keine voneinander abweichenden Ansichten der Zertifikatsausstellung präsentiert. Außerdem bleiben die ausgestellten Zertifikate für das Monitoring verfügbar, selbst wenn das Ausstellungs-Log der CA nicht erreichbar ist.

Der Richtlinienentwurf für das [Quantum-resistant Root Program](https://googlechrome.github.io/chromerootprogram/cqrp/draft-policy/?cf_target_id=7B337765CEACAE326DB116491B5F025E) von Chrome schreibt mindestens zwei Mitunterzeichnungen vor: eine von einem durch Chrome anerkannten Mirroring Cosigner, den eine eigenständige Organisation betreibt, und eine von der ausstellenden MTC-CA selbst. Deshalb werden wir die Ausstellungs-Logs anderer CAs im Pilotprogramm spiegeln und für unsere eigenen ausgestellten Zertifikate mindestens eine unabhängige Mitunterzeichnung verlangen.

Wir werden unseren Mirroring Cosigner in [Azul](https://github.com/cloudflare/azul?cf_history_state=%7B%22guid%22%3A%22C255D9FF78CD46CDA4F76812EA68C350%22%2C%22historyId%22%3A151%2C%22targetId%22%3A%2266F830E854C54348C39BC817251903AF%22%7D) implementieren, unserem quelloffenen, auf Rust basierenden Transparenz-Log. Für größtmögliche Interoperabilität wird er das [tlog-mirror-Protokoll von c2sp unterstützen](https://c2sp.org/tlog-mirror@v0.1.0?cf_target_id=1939A460169927196562066A4BF378CD).

Sobald die Mitunterzeichnung eines Mirroring Cosigners vorliegt, erstellt die CA ein MTC mit den Mitunterzeichnungen, dem öffentlichen Schlüssel des Servers und einem Inklusionsbeweis. Anschließend sendet sie das MTC an den Server, der es für TLS verwenden kann.

### **PQ-Signaturen effizient bereitstellen mit der Landmark-Optimierung**

Eigenständige Zertifikate funktionieren zwar, übertragen beim TLS-Handshake aber weiterhin umfangreiche PQ-Signaturen. Das begrenzt ihre Effizienz. Die entscheidenden Leistungsverbesserungen des MTC-Ansatzes ergeben sich durch Landmark-relative Zertifikate.

Statt mit jedem Zertifikat Mitunterzeichnungen zu übertragen, können CAs eine Folge von Teilbäumen, die sämtliche aktiven Zertifikate im Log abdecken, als Landmark festlegen. Diese Teilbäume verteilen sie zusammen mit den Daten zu ihrer Authentifizierung über einen separaten Aktualisierungsdienst an die Clients. Während des TLS-Handshakes authentifiziert der Browser den Server, indem er prüft, ob dessen Zertifikatsdaten – einschließlich Domainname und öffentlichem Schlüssel – in einem vertrauenswürdigen Teilbaum des CA-Logs enthalten sind. Verknüpft der Inklusionsbeweis das Zertifikat mit einer mitunterzeichneten Landmark und weist der Server während des TLS-Handshakes nach, dass er den zugehörigen privaten Schlüssel besitzt, weiß der Client, dass er mit dem richtigen Server kommuniziert.

Durch die regelmäßige Übertragung dieser Signaturen und Tree-Metadaten außerhalb der TLS-Verbindungen kann eine kleine Anzahl von Signaturen für MTC-Zertifikatsgruppen effizient Milliarden von Zertifikaten einer CA abdecken. Landmarks sind bei einem Einsatz in großem Umfang zwar effizienter, machen eigenständige MTCs aber nicht überflüssig. Clients können frisch installiert sein, zwischenzeitlich offline gewesen sein oder das benötigte Landmark-Update noch nicht erhalten haben. Deshalb müssen Server weiterhin auf eigenständige Zertifikate zurückgreifen können.

## **MTCs in der Praxis und die Ergebnisse unseres Experiments mit Chrome**

In diesem Jahr haben wir gemeinsam mit Chrome getestet, ob MTCs in der Kommunikation zwischen Client und Server praktikabel sind. Dafür betrieben wir eine „Bootstrap-CA“, also eine simulierte Zertifizierungsstelle, die den Ausstellungsprozess nachbildete. Sie stellte MTCs für ausgewählte Domains im kostenlosen Cloudflare-Tarif aus. Diese MTCs waren durch eine klassische Zertifikatskette abgesichert und wurden an 50 % der Nutzer von Chrome Beta 146 ausgeliefert. Im Laufe des Experiments haben wir erfolgreich Milliarden von MTCs ausgeliefert.

Bei TLS zeigte sich, dass der typische Fall sehr effizient ist: Mit einem Landmark-relativen Zertifikat müssen beim Handshake nur ein öffentlicher Schlüssel, eine Signatur und ein Inklusionsbeweis von weniger als 1 kB übertragen werden. Ließ sich mit dem Client kein Landmark-relatives Zertifikat aushandeln, griffen wir im Experiment auf die klassische Zertifikatskette zurück, statt ein eigenständiges MTC auszuliefern. Auch bei der Zertifikatstransparenz verändern MTCs die Skalierungseigenschaften: Das Log muss nur Hashwerte öffentlicher Schlüssel speichern. Einzelne Einträge benötigen keine eigenen Signaturen, da die Signatur des Treekopfs das gesamte Log abdeckt. So wird eine Vervielfachung der Zertifikatseinträge vermieden: Das Ausstellungs-Log der CA ist die maßgebliche Quelle für sämtliche von ihr ausgestellten Zertifikate, und Systeme, die das Log auswerten, müssen jedes Zertifikat nur einmal abrufen.

Das Ergebnis: MTCs funktionieren in der Praxis! Mit Landmark-relativen MTCs waren TLS-Handshakes im Median 9 % schneller als mit einer klassischen Zertifikatskette. Zugegeben: Ein Großteil dieses Vorteils entsteht dadurch, dass die Zwischenzertifikate entfallen. Da wir MTCs mit klassischen Signaturen getestet haben, erwarten wir bei postquantensicheren Signaturen eine noch größere Verbesserung. Die Ergebnisse und die umfangreiche branchenweite Zusammenarbeit an MTCs in der [PLANTS-Arbeitsgruppe](https://datatracker.ietf.org/wg/plants/documents/?cf_target_id=23FA30452559992E3BB8F3DE64443091) der IETF haben uns überzeugt. Deshalb haben wir im vergangenen Monat, also im August 2026, damit begonnen, das Experiment auslaufen zu lassen.

## **Wie es mit MTCs weitergeht**

Wir freuen uns, dass unser Experiment mit Chrome gezeigt hat, dass MTCs in der Praxis funktionieren. Besonders freuen wir uns darauf, künftig als reguläre CA Zertifikate auszustellen.

Es bleiben jedoch grundlegende Fragen, die wir nur durch ein groß angelegtes Experiment gemeinsam mit dem gesamten PKI-Ökosystem beantworten können. Können unabhängige Monitoring-Systeme MTC-Ausstellungs-Logs in dem Umfang [verarbeiten und überprüfen](https://transparency.dev/summit2025/talks/verifiable-indexes.html?cf_target_id=2C9E255AFF3B9654A98D7ED199D52974), der im produktiven Betrieb anfällt? Werden genügend unterschiedliche CAs und Mitunterzeichner entstehen, um die für ein resilientes System notwendige Vielfalt zu gewährleisten? Wie sollten Browser die Leistungsvorteile kompakter Landmark-relativer MTCs gegen die erforderlichen Ausweichmöglichkeiten für Clients ohne aktuelle Landmarks abwägen? MTCs haben sich als maßgeblicher Ansatz für postquantensichere Authentifizierung etabliert. Um ihre Eignung im produktiven Betrieb in der Größenordnung des gesamten Internets nachzuweisen, müssen jedoch unterschiedliche Root-Programme, Browserhersteller, CAs, Betreiber von Mirrors, Monitoring-Systeme und die weitere Community zusammenarbeiten.

Wir betrachten es als Privileg, an dieser nächsten Entwicklungsphase der WebPKI mitzuwirken, und nehmen die Verantwortung für den Betrieb einer CA-Infrastruktur ernst. CAs nehmen im Vertrauensökosystem eine privilegierte Stellung ein. Browser, Domaininhaber und Endnutzer verlassen sich darauf, dass sie Identitäten korrekt überprüfen, Signaturschlüssel schützen, Richtlinien einhalten und zuverlässig arbeiten. Bevor Browser der Cloudflare-CA bei der Ausstellung von MTCs vertrauen können, müssen wir ihre Aufnahme in den Quantum-resistant Root Store von Chrome beantragen und ein strenges Prüfverfahren durchlaufen. Wir begrüßen diese Prüfung und legen an uns selbst dieselben hohen Maßstäbe an wie an jede andere CA, der die Sicherheit des Internets mit anvertraut wird. Wir hoffen, dass weitere CAs entstehen, die die Einführung von MTCs unterstützen, und freuen uns auf die Zusammenarbeit mit allen Browserherstellern, die MTCs einsetzen möchten.

]]>01M4CPQ6Y50QJ2BJJVRYHT9VK3Wir bauen eine Zertifizierungsstelle für das gesamte Internethttps://blog.cloudflare.com/de-de/cloudflare-certificate-authority/ Thu, 08 Oct 2026 02:12:35 GMTZwölf Jahre nach der Einführung von Universal SSL bewirbt sich Cloudflare darum, eine Zertifizierungsstelle zu werden. Durch die Kombination einer etablierten Root, eines ACME-first-Ansatzes und Merkle Tree Certificates bauen wir eine post-quantensichere ZS für das offene Web auf.Birthday WeekKryptographiePost-Quanten-KryptographieSicherheitTLSVor zwölf Jahren haben wir während der Birthday Week 2014 [Universal SSL aktiviert](https://blog.cloudflare.com/introducing-universal-ssl/) und die Zahl der verschlüsselten Websites im Netz praktisch über Nacht nahezu verdoppelt. Dafür haben wir jeder Website hinter Cloudflare kostenlose TLS-Verschlüsselung zur Verfügung gestellt -, auch denjenigen, deren Betreiber uns nie einen Cent bezahlt hatten. Verschlüsselung war damit kein teures, zeitaufwendiges Unterfangen mehr, sondern wurde stattdessen zum Standard.

Zur diesjährigen Birthday Week gehen wir den nächsten Schritt auf diesem Weg. Seit mehr als einem Jahrzehnt gehören wir zu den größten Nutzern öffentlich vertrauenswürdiger Zertifikate im Internet und haben aber selbst noch kein einziges ausgestellt. Das ändert sich jetzt. Cloudflare kündigt an, eine öffentlich vertrauenswürdige Zertifizierungsstelle (CA) zu werden.

Heute geben wir die ersten konkreten Meilensteine auf diesem Weg bekannt: Wir haben die Aufnahme in die Root-Programme von Chrome, Apple, Microsoft und Mozilla beantragt und eine verbindliche Vereinbarung zum Erwerb eines etablierten, weithin als vertrauenswürdig anerkannten Root-Zertifikats von GlobalSign unterzeichnet. So können wir vom ersten Tag unserer Zertifikatsausstellung an Zertifikate anbieten, die mit möglichst vielen Geräten kompatibel sind. Außerdem planen wir, zu den ersten CAs zu gehören, die Post-Quanten-Zertifikate anbieten, und streben die Aufnahme in das kürzlich angekündigte [Quantum-resistant Root Program](https://blog.google/security/cultivating-a-robust-and-efficient-quantum-safe-https/) von Chrome an.

Noch stellen wir keine Zertifikate aus, und bis dahin wird es noch etwas dauern. Wir sagen jedoch schon jetzt öffentlich zu, dieses Vorhaben umzusetzen. Wir werden über erreichte Meilensteine berichten und genau erläutern, was wir aufbauen. Dabei arbeiten wir eng mit den Root-Programmen und anderen Mitgliedern der WebPKI-Community zusammen.

## **Zwei Wege zum Vertrauen**

Es dauert Jahre, bis ein neues Root-Zertifikat auf breiter Basis genutzt werden kann. Selbst nach der Aufnahme in ein Root-Programm muss es erst in die Vertrauensspeicher von Betriebssystemen, Browsern und Geräten weltweit gelangen. Die große Zahl von Geräten, die keine Updates mehr erhalten oder nie welche erhalten haben, erreicht es überhaupt nicht. Auf diese große Gruppe älterer Clients entfällt ein erheblicher Teil des weltweiten Internetverkehrs – und entsprechend viele vermeidbare Verbindungsprobleme treten dort auf. Wir sind der Meinung, dass alle Clients das höchstmögliche Maß an Sicherheit verdienen, unabhängig vom Hersteller, Betriebssystem oder davon, wann sie zuletzt aktualisiert wurden.

Der Erwerb eines bestehenden Root-Zertifikats, das bereits in den Vertrauensspeichern vieler unterschiedlicher Clients enthalten ist, löst dieses Problem vom ersten Tag an. Das bestehende Root-Zertifikat von GlobalSign wird seit 2012 von Browsern, Betriebssystemen und Geräten als vertrauenswürdig anerkannt. Es erreicht auch ältere Clients, die ein neues Root-Zertifikat niemals erreichen würde. Das neue Root-Zertifikat, das wir zur Aufnahme in die Root-Programme einreichen werden, ist dagegen auf die künftigen Anforderungen des Ökosystems ausgelegt. Dazu gehören auch Vorgaben von Programmen, die inzwischen das zulässige Alter vertrauenswürdiger Root-Zertifikate begrenzen. Das etablierte Root-Zertifikat sorgt für Kompatibilität mit älteren Geräten. Die neuen Root-Zertifikate ermöglichen es uns, auch die künftigen Vorgaben der Root-Programme zu erfüllen. Wir brauchen beides, damit die von unserer CA ausgestellten Zertifikate auf möglichst vielen Geräten unserer Kunden genutzt werden können.

## **Eine neue Quelle für kostenlose Zertifikate**

Der Großteil des verschlüsselten Webs basiert heute auf kostenlosen, automatisch ausgestellten Zertifikaten. Einen erheblichen Teil davon stellt ein bemerkenswerter Anbieter bereit: Let’s Encrypt. Die Zertifizierungsstelle stellt täglich rund zehn Millionen Zertifikate aus, versorgt mehr als 500 Millionen Websites und hat 2025 die Marke von vier Milliarden aktiven Zertifikaten überschritten. Let’s Encrypt gehört zu den besten Entwicklungen für das Internet in den letzten zwanzig Jahren – und das sagen wir als einer seiner größten Nutzer.

Dieser Erfolg birgt ein systemisches Risiko: Sollte die führende kostenlose Zertifizierungsstelle eine Woche lang Probleme haben, stünde für einen großen Teil des Webs keine vergleichbare kostenlose, automatisierte Alternative bereit, die diese Last auffangen könnte. Für die Zertifikatspakete unserer Kunden bauen wir bereits seit Jahren genau diese Art von Redundanz auf. Jedes Cloudflare Universal SSL-Zertifikat wird schon heute mit einem Backup-Zertifikat bereitgestellt, das einen eigenen Schlüssel verwendet und von einer anderen Zertifizierungsstelle ausgestellt wurde. Wird das primäre Zertifikat widerrufen oder kompromittiert, kann das Backup automatisch eingesetzt werden. Eine öffentliche Zertifizierungsstelle setzt dieselbe Idee für das gesamte Internet um.

Um den Umstieg zu erleichtern, setzen wir von Anfang an auf ACME. Das Automated Certificate Management Environment ist ein weit verbreitetes, offenes Standardprotokoll. Unsere Zertifikate werden über ACME automatisch ausgestellt und verlängert. Wer seinen ACME-Client bereits für eine kostenlose CA eingerichtet hat, kann durch Ändern der Verzeichnis-URL zu uns wechseln – ohne neue Tools und ohne die bestehende Architektur anpassen zu müssen.

## **Wir erwarten einen starken Anstieg der Zertifikatszahlen**

Mehr als 20 Prozent der weltweiten Internetanfragen laufen über Cloudflare. Wir terminieren TLS-Verbindungen für Millionen von Domains und benötigen dafür jedes Jahr Millionen von Zertifikaten. Diese beziehen wir von mehreren CAs und nutzen dabei sowohl primäre als auch Backup-Verfahren, damit die Dienste unserer Kunden auch bei CA-Ausfällen und Zertifikatswiderrufen verfügbar bleiben.

Dadurch haben wir nicht nur gelernt, wie das WebPKI-Ökosystem funktioniert. Als Nutzer von Zertifikaten haben wir auch schmerzhaft erfahren, dass es gelegentlich versagt. Wir haben uns mit Rate Limits, Sonderfällen bei der Validierung, Verzögerungen beim Zertifikatswiderruf, dem Aufbau von Zertifikatsketten und der verzögerten Verteilung von Root-Zertifikaten auseinandergesetzt. Wir haben die Umbrüche in der CA-Landschaft der letzten Jahre miterlebt und erfahren, wie sie sich auf unsere Kunden auswirken. Wir wissen, was Nutzer von einer zuverlässigen Zertifikatsausstellung erwarten müssen. Denn die Verfügbarkeit der Dienste unserer Kunden hing davon ab, dass wir auch bei Problemen eines Ausstellers zuverlässig und schnell reagieren konnten.

Da sich in den kommenden Jahren die [maximale Gültigkeitsdauer von Zertifikaten](https://cabforum.org/2025/04/11/ballot-sc081v3-introduce-schedule-of-reducing-validity-and-data-reuse-periods/#ballot-contents) verkürzt, KI-Agenten zunehmend aktiv werden und Post-Quanten-Zertifikate zum Standard werden, erwarten wir einen raschen weiteren Anstieg der jährlich benötigten Zertifikate – und damit sind wir nicht allein. Wir wollen dieses Problem nicht nur für uns selbst lösen, sondern auch zur Zertifikatsversorgung des gesamten Internets beitragen und dafür sorgen, dass unseren Kunden dafür noch mehr Anbieter zur Verfügung stehen.

## **Auf Resilienz ausgelegt: Transparenz und „fail small“**

Mit der neuen Verantwortung als eigene CA verpflichten wir uns, eine möglichst zuverlässige und resiliente Zertifizierungsstelle aufzubauen. Wie bei unseren anderen Produkten setzen wir dabei nicht nur darauf, Fehler zu vermeiden. Wir wollen auch sicherstellen, dass einzelne Probleme möglichst geringe Auswirkungen haben – nach dem Prinzip „fail small“.

Dazu gehört, Verfahren zur Wiederherstellung des Betriebs schon vor einem möglichen Vorfall zu entwickeln und zu testen. Beispielsweise werden wir Zertifikate nur ausstellen, wenn ihre Verlängerung automatisiert ist. Die verwendeten Clients müssen [ACME Renewal Information](https://www.rfc-editor.org/info/rfc9773/) (ARI) unterstützen, das in RFC 9773 standardisiert ist. Zertifikatsinhaber müssen sicherstellen, dass ihre Automatisierung unseren Verlängerungsendpunkt regelmäßig abfragt, auf die von uns veröffentlichten Verlängerungsfenster reagiert und das jeweils zu ersetzende Zertifikat identifiziert.

Wir lernen dabei auch aus unseren Beobachtungen der vergangenen 16 Jahre. Wir haben erlebt, wie Zertifizierungsstellen vor einem Dilemma standen: Sie mussten Zertifikate rechtzeitig widerrufen und zugleich verhindern, dass die Websites der Zertifikatsinhaber ausfielen. Zu viele Nutzer konnten ihre Zertifikate nicht schnell genug ersetzen. Müssen Zertifikate außer Betrieb genommen werden – etwa wegen eines Compliance-Problems oder eines Sicherheitsvorfalls –, können wir die Verlängerungsfenster der betroffenen Zertifikate vorziehen, den Austausch über den verfügbaren Zeitraum verteilen und die Ausstellung der Ersatzzertifikate nachverfolgen.

Dies ist nur ein Beispiel dafür, wie wir unsere Zertifizierungsstelle gestalten wollen. Wir werden offenlegen, welche technischen Komponenten wir für die Zertifikatsausstellung einsetzen und wie unsere Betriebsabläufe funktionieren. Dazu werden wir reproduzierbare Builds der Signierungssoftware veröffentlichen, Attestierungen für die Hardware-Sicherheitsmodule bereitstellen, in denen unsere Schlüssel gespeichert sind, und ein öffentliches Dashboard zum Betriebszustand der Zertifikatsausstellung sowie zu Vorfällen betreiben. Audits sind Momentaufnahmen. Sie zeigen, dass eine CA eine Prüfung bestanden hat, aber nicht, wie sie an einem gewöhnlichen Dienstag arbeitet. Wir möchten, dass die Verantwortlichen der Root-Programme, Forschende und Website-Betreiber beobachten können, wie eine moderne CA zwischen den Audits tatsächlich arbeitet.

## **Eine Zertifizierungsstelle für das Post-Quanten-Internet**

Wir wollen auch bei der künftigen Entwicklung von Zertifikaten eine führende Rolle übernehmen und uns nicht auf den heutigen Stand beschränken. Wir planen, zu den ersten CAs zu gehören, die Merkle Tree Certificates (MTCs) im produktiven Betrieb ausstellen. Die ersten Zertifikate sollen im ersten Quartal 2027 ausgegeben werden.

MTCs ermöglichen es, öffentlich vertrauenswürdige Zertifikate auf neue und wesentlich kompaktere Weise bereitzustellen. Sie sind für eine Post-Quanten-Welt konzipiert, in der herkömmliche Zertifikatsketten so umfangreich werden, dass sie TLS-Handshakes belasten. Wir haben den [auf Standards basierenden Vorschlag](https://datatracker.ietf.org/doc/draft-ietf-plants-merkle-tree-certs/) für MTCs bei der IETF maßgeblich vorangetrieben. Bereits im Laufe dieses Jahres hat [Chrome MTCs](https://blog.google/security/cultivating-a-robust-and-efficient-quantum-safe-https/) als bevorzugten Ansatz für die Post-Quanten-Authentifizierung benannt. Indem wir diese Zertifikate im produktiven Betrieb ausstellen, können wir Cloudflare-Kunden und das Internet insgesamt vor Bedrohungen durch Quantencomputer schützen. Zugleich bringen wir die Umstellung, die dem gesamten Web bevorsteht, durch die Ausstellung in großem Umfang voran. [In einem eigenen Blogbeitrag](http://blog.cloudflare.com/pq-ca-with-mtcs) erläutern wir ausführlicher, wie MTCs funktionieren und wie diese neue Web Public Key Infrastructure (PKI) aussehen wird.

Wir erwarten keinen abrupten Übergang. Ein Großteil des Internets wird noch viele Jahre auf klassische Zertifikate und die bestehende WebPKI angewiesen sein. In dieser Zeit dürfte jedoch ein stetig wachsender Anteil der ausgestellten Zertifikate auf MTCs entfallen. Deshalb bauen wir einen Dienst auf, der beide Zertifikatsarten unterstützt. Indem wir klassische Zertifikate und Merkle Tree Certificates unter einer CA mit einem einheitlichen Lebenszyklus und denselben Garantien anbieten, ermöglichen wir unseren Kunden, MTCs in ihrem eigenen Tempo einzuführen. So können sie dazu beitragen, dass das Web den Übergang schrittweise vollzieht. Kunden sollten sich während einer jahrzehntelangen Migration nicht zwischen den beiden Ansätzen entscheiden, zwei parallele Systeme betreiben oder ihre Infrastruktur neu aufbauen müssen, sobald sich das Verhältnis zwischen klassischen Zertifikaten und MTCs verändert.

## **Wie immer wird Cloudflare „Customer Zero“ sein**

Cloudflare stellt seinen Kunden über Universal SSL Zertifikatspakete bereit. Darüber hinaus beziehen wir Zertifikate von vielen verschiedenen CAs für den Betrieb unserer eigenen Systeme und für interne Abläufe. Wie bei unseren anderen Produkten werden wir auch bei der neuen CA und ihren Zertifikaten – sowohl WebPKI-Zertifikaten als auch MTCs – [unser erster eigener Kunde](https://www.cloudflare.com/the-net/top-of-mind-security/customer-zero/) sein. Damit stellen wir sicher, dass sämtliche neuen Systeme und Prozesse unsere hohen internen Standards erfüllen und die Infrastruktur unserer CA unter den Lastbedingungen von Cloudflare erprobt wird.

## **Was als Nächstes passiert**

Wir durchlaufen derzeit die Antrags- und Genehmigungsverfahren der wichtigsten Root-Programme für das Web. Die Verfahren sind öffentlich, und wir werden regelmäßig über ihre Fortschritte berichten – bis zur Ausstellung der ersten Merkle Tree Certificates Anfang 2027. Wenn Sie unsere Fortschritte verfolgen oder künftig zu den ersten Nutzern eines Zertifikats unserer Cloudflare-CA gehören möchten, können Sie sich [für Updates anmelden](http://cloudflare.com/resource/certificate-authority). Und wenn Sie am Aufbau unserer neuen Zertifizierungsstelle mitarbeiten möchten: [Wir suchen Verstärkung](https://boards.greenhouse.io/cloudflare/jobs/8237801?gh_jid=8237801)!

Beim Aufbau unserer eigenen CA werden wir weiterhin eng mit unseren öffentlich vertrauenswürdigen Partner-Zertifizierungsstellen zusammenarbeiten. Auf dieses Netzwerk verlassen wir uns seit vielen Jahren – genau genommen seit 16 Jahren! Gemeinsam setzen wir uns für ein vertrauenswürdiges und offenes Internet ein.

Als wir Universal SSL einführten, war unser Argument einfach: Mit jedem Byte, das verschlüsselt durch das Internet übertragen wird, wird es schwieriger, den Datenverkehr abzufangen, zu drosseln oder zu zensieren. Und das offene Web bauen wir alle gemeinsam auf. Eine öffentlich vertrauenswürdige, redundante und transparente Zertifizierungsstelle setzt denselben Gedanken auf einer grundlegenderen Ebene um: bei dem Vertrauen, dass das verschlüsselte Web überhaupt erst möglich macht. Wir arbeiten schon lange auf dieses Ziel hin und freuen uns, dass die Umsetzung nun konkrete Formen annimmt.

Happy Birthday Week!

]]>01M4CM7Q4EJANR8PEDC64ST1V6Wir stellen vor: The Cold Start: Präsentiere dein Start-up live bei Cloudflare Connecthttps://blog.cloudflare.com/de-de/introducing-the-cold-start/ Thu, 01 Oct 2026 09:13:30 GMTCloudflare is launching The Cold Start, a startup competition giving five early-stage companies five minutes on stage at Cloudflare Connect. Grand Prize winner receives $500,000 in credits, a San Francisco billboard, and an invitation to our VIP speakers dinner.Birthday WeekCloudflare für StartupsEntwicklerVor sechzehn Jahren war Cloudflare eines von mehr als 1.000 Start-ups, die darauf hofften, sich bei TechCrunch Disrupt auf der Bühne präsentieren zu dürfen.

Auf den ersten Blick sprach wenig dafür, uns einen dieser Plätze zu geben. Bei Cloudflare ging es um Infrastruktur: Wir machten Websites schneller und schützten sie vor Angriffen. Warum das wichtig war, verstanden damals viele noch nicht. Infrastruktur bleibt oft unsichtbar, bis zu dem Moment, in dem sie plötzlich wichtig wird.

Doch am 27. September 2010 betraten Matthew Prince und Michelle Zatlyn die Startup Battlefield-Bühne und stellten Cloudflare der Öffentlichkeit vor. Schon während der Präsentation meldeten sich die ersten Nutzer an. Und es wurden immer mehr. Als die Jury ihre Fragen beendet hatte, waren bereits Hunderte von Websites Cloudflare beigetreten und stellten unsere damals fünf Rechenzentren unmittelbar auf die Probe. In den folgenden sieben Tagen stieg der Traffic durch unser Netzwerk um fast das Zehnfache. Cloudflare kletterte von Platz 1.000 der größten Websites weltweit unter die Top 50.

Den Hauptpreis gewann Cloudflare an diesem Tag nicht. Bei der Preisverleihung verglich TechCrunch-Gründer Mike Arrington unsere Arbeit mit einer „Auspuffreparatur für das Internet“. Und ehrlich gesagt lag er damit nicht ganz falsch. Doch dann zeichnete er uns als innovativstes Unternehmen aus. Wie Matthew später schrieb: „Vielleicht gewinnst du keine, das weitaus wichtiger ist.“

Es gibt Momente im Leben eines Unternehmens, in denen dir jemand ein Publikum, ein Mikrofon und ein paar Minuten zur Verfügung stellt. Du darfst die Idee vorstellen,die dich seit Monaten oder Jahren nicht mehr loslässt. Meistens passiert dabei nichts Außergewöhnliches. Manchmal hören aber genau die richtigen Menschen im richtigen Moment zu. Und plötzlich findet eine Idee, die bislang nur eine Handvoll Menschen kannte ihren Weg in die Welt.

Zu unserem 16. Geburtstag möchten wir im Oktober fünf Start-ups in der Frühphase eine eigene Bühne geben.

## **Wir stellen vor: The Cold Start**

[ The Cold Start](https://www.cloudflare.com/connect/cold-start/?cf_page=introducing-the-cold-start%2F) ist ein Live-Start-up-Wettbewerb, der nächsten Monat bei Cloudflare Connect in San Francisco stattfindet. Wir wählen fünf Unternehmen in der Frühphase aus. Jedes bekommt fünf Minuten um zu erklären, was es entwickelt, warum es gebraucht wird und warum gerade dieses Team die Idee umsetzen sollte.

Uns sind interessante, verständlich erklärte Ideen wichtiger als perfekte Pitch-Decks. Du brauchst keine dreißig Folien, keine verdächtig genaue Berechnung des gesamten adressierbaren Marktes und keine einstudierte Geschichte darüber, wie dich deine Kindheit darauf vorbereitet hat, die Debitorenbuchhaltung zu revolutionieren.. Wir möchten deine Vision verstehen: Welche Veränderungen machen deine Idee gerade jetzt möglich? Was siehst du, was andere übersehen haben? Und warum lässt dich der Gedanke daran nicht mehr los?

Die fünf Finalisten stellen ihre Ideen dem Publikum der Cloudflare Connect und einer dreiköpfigen Jury Personen vor, die sich seit vielen Jahren mit r Unternehmen, Infrastruktur und dem Internet beschäftigt:

  * Matthew Prince, Mitgründer und CEO von Cloudflare
  * Michelle Zatlyn, Mitgründerin und Präsidentin von Cloudflare
  * Dane Knecht, CTO von Cloudflare



Die Jury wählt ein Start-up aus, das 500.000 USD in Cloudflare-Credits gewinnt, auf einer Werbetafel in San Francisco für sich werben darf und eine Einladung zum VIP-Abendessen mit den Vortragenden am selben Abend erhält.

Fünf Unternehmen. Jeweils fünf Minuten. Und ein Publikum, das zuhört.

## **Was suchen wir?**

The Cold Start richtet sich an ambitionierte Start-ups in der Frühphase offen, die in den USA oder Kanada ansässig sind und bislang weniger als 10 Millionen US-Dollar eingesammelt haben. Darüber hinaus setzen wir bewusst keine engen Grenzen. Die interessantesten Unternehmen lassen sich schließlich selten in vorgegebene Kategorien einordnen.

Wir suchen Ideen, die ganz selbstverständlich wirken, sobald sie jemand endlich umsetzt - und solche, die zunächst ein wenig unvernünftig klingen. Infrastruktur, die langweilig erscheint, bis klar wird, dass künftig alle darauf angewiesen sein werden; Produkte, die vor ein paar Jahren noch nicht möglich gewesen wären. Ungewöhnliche neue Schnittstellen. Neue Wege, Software zu entwickeln. Lösungen für riesige bestehende Märkte und für Märkte, die noch nicht einmal einen Namen haben..

Vor allem möchten wir Menschen kennenlernen, die etwas in der Welt erkannt und beschlossen haben, daraus etwas zu machen.

Erzähle uns in deiner Bewerbung, wer du bist, und stelle deine Geschäftsidee in einem Satz vor. Erkläre, was du entwickelst und warum, wie viel Finanzierung du bislang erhalten hast und welche Umsätze du erzielst. Zeige uns außerdem, welche Rolle Cloudflare in deinem Technologie-Stack spielt. Weitere Informationen und Links helfen uns, dich und deine Arbeit besser kennenzulernen.

Unser Ziel ist einfach: Wir möchten verstehen, warum deine Idee gebraucht wird. 

[Bewirb dich für The Cold Start.](https://www.cloudflare.com/connect/cold-start/?cf_page=introducing-the-cold-start%2F)

**_Du kannst dich ab sofort bewerben. Bewerbungsschluss ist Freitag, der 2. Oktober 2026._**

## **Fünf Minuten in San Francisco**

The Cold Start findet im Rahmen von [Cloudflare Connect](https://www.cloudflare.com/connect/?cf_page=introducing-the-cold-start%2F) statt: am Montag, dem 19. Oktober, von 16 bis 17 Uhr PDT im Moscone West in San Francisco. Cloudflare übernimmt die Flugkosten für die fünf Finalisten, damit sie vor Ort am Wettbewerb teilnehmen können.

Connect bringt Menschen zusammen, die die Zukunft des Internets gestalten und darüber nachdenken, wie sie aussehen könnte. Zu den diesjährigen Vortragenden gehören die KI-Pionierin Dr. Fei-Fei Li, Idealab-Gründer Bill Gross, der Organisationspsychologe und Autor Adam Grant, AMD-CTO Mark Papermaster, Evan You, der Entwickler von Vue.js und Vite, sowie Fabian Hedin, Mitgründer und CTO von Lovable, und Peter Steinberger, Entwickler von OpenClaw und Mitglied des technischen Teams bei OpenAI.

Fünf jungen Unternehmen geben wir auf dieser Bühne Raum. Jedes Start-up hat fünf Minuten für seinen Pitch. Anschließend stellt die Jury drei bis fünf Minuten lang Fragen.

Dass sich unsere Geschichte hier ein Stück weit wiederholt, gefällt uns. Vor sechzehn Jahren brauchte Cloudflare jemanden, der an ein Infrastrukturunternehmen glaubte, dessen Angebot sich nicht leicht erklären ließ – und uns ein paar Minuten vor dem richtigen Publikum gab. Heute können wir selbst diese Bühne bieten. Diese Chance möchten wir an Unternehmen weitergeben, die gerade erst anfangen.

## **Klein anfangen. Großes schaffen.**

Es gibt einen praktischen Grund, warum Cloudflare so viel Zeit in die Zusammenarbeit mit Start-ups investiert: Auch sehr kleine Teams können sich .

Das Problem: Anspruchsvolle Softwareprojekte brauchen zunehmend eine Infrastruktur, deren Aufbau sich bis vor Kurzem nur die größten Technologieunternehmen leisten konnten. Dazu gehören weltweit verfügbare Rechenleistung, Speicher, Netzwerkinfrastruktur, Sicherheit, Echtzeitsysteme und KI-Inferenz. Und natürlich muss die Infrastruktur auch dann standhalten, wenn dein Produkt plötzlich durchstartet. Ein Unternehmen sollte nicht erst selbst riesig werden müssen, um all das nutzen zu können.

Wir glauben, dass dir diese Möglichkeiten vom ersten Tag an zur Verfügung stehen sollten.

Dieser Gedanke steckt auch hinter [Cloudflare for Startups](https://www.cloudflare.com/startups/). Über das Programm können berechtigte Start-ups in der Frühphase von bis zu 350.000 USD in Cloudflare-Credits für ein Jahr erhalten. Deshalb bauen wir auch die Entwicklerplattform von Cloudflare weiter aus: Ein kleines Team sollte am Dienstag ein Produkt entwickeln können. Wenn es am Mittwoch im Internet durchstartet, sollte sich das Team am Donnerstag weiter auf das Produkt konzentrieren können – statt über Nacht zu Fachleuten für globale Infrastruktur werden zu müssen.

Cloudflare begann selbst mit einer Idee, die zunächst mit einer Idee leicht unvernünftig klang: Die Performance, Sicherheit und weltweit verfügbare Rechenkapazität, auf die die größten Unternehmen im Internet zugreifen können, sollten vom ersten Tag an allen zur Verfügung stehen. 2010 durften wir auf einer Bühne erklären, warum das wichtig ist.

Sechzehn Jahre später haben wir ein viel größeres Netzwerk, ein etwas größeres Team und deutlich bessere Sicherungen.

Jetzt möchten wir wissen, woran du arbeitest.

[Bewirb dich für The Cold Start.](https://www.cloudflare.com/connect/cold-start/?cf_page=introducing-the-cold-start%2F)

]]>01M3VBEFBPNQKVJF8DXSTP80WQEinführung von cf: die agentenbasierte CLI für die gesamte Cloudflare APIhttps://blog.cloudflare.com/de-de/cloudflare-cf-cli-launch/ Thu, 01 Oct 2026 09:05:55 GMTWir veröffentlichen cf, unser neues Befehlszeilen-Tool, das die gesamte Cloudflare API abbildet und programmatische TypeScript-Konfiguration unterstützt. Außerdem machen wir Forge, unseren internen SDK-Generator, als Open Source verfügbar.AgentsAPIBirthday WeekcfEntwicklerIm vergangenen Jahr ist die Nutzung von Wrangler durch Agents sprunghaft angestiegen.

Im März 2026 entfiel bereits ein Viertel der Wrangler-Nutzung auf Agents. Ein Jahr zuvor hatte ihr Anteil noch im einstelligen Prozentbereich gelegen. Vergangene Woche erreichte er 48 %. 

Agents nutzen Wrangler intensiver als Menschen: Pro Tag verwenden sie fast doppelt so viele unterschiedliche Befehle. Zudem ist die Wahrscheinlichkeit, dass sie mindestens sechs Befehle verwenden, fast viermal so hoch.

Agents arbeiten gern mit Kommandozeilenwerkzeugen. Doch Wrangler unterstützt nur rund 280 Operationen, während Cloudflare Tausende anbietet. 

Zu Beginn des Jahres haben wir anged[eutet, wie wir dieses Problem lösen wollten](https://blog.cloudflare.com/cf-cli-local-explorer) – und heute stellen wir cf vor: eine neue CLI, mit der Agents auf sämtliche Cloudflare-Produkte zugreifen können.

cf ist als CLI für die nächste Generation der Softwareentwicklung ausgelegt:

  * Eine speziell auf Agents abgestimmte Suche und gezielte Hinweise helfen ihnen, den passenden Befehl für ihre Aufgabe zu finden.
  * JSON ist das standardmäßige Ausgabeformat. Für Menschen werden die Ergebnisse übersichtlich formatiert, für Agents kompakt ausgegeben, damit sie möglichst wenig Platz im Kontextfenster beanspruchen.
  * Mit cloudflare.config.ts führen wir ein neues Konfigurationsformat ein, das künftig ganz Cloudflare abdecken soll. Den Anfang machen Workers. Das Format bietet die Typsicherheit von TypeScript und unterstützt Sie und Ihren Agents über das Language Server Protocol (LSP) mit präzisen Hinweisen und Vorschlägen.
  * Vite wird zum Standard. Damit stehen Ihnen ein erstklassiger lokaler Entwicklungsserver und zahlreiche Plugins für die Entwicklung von Anwendungen und Frameworks zur Verfügung.



Installieren Sie noch heute die offene Beta global und führen Sie sie von überall aus:

**Copy prompt**
    
    
    Please update your global agent instructions, so you use Cloudflare's new `cf` CLI.
    
    Add the Markdown below to the user-level instructions file that you load in every project – not this repository's AGENTS.md or CLAUDE.md. Use the file for the agent you are: Claude Code `~/.claude/CLAUDE.md`, Codex `~/.codex/AGENTS.md`, OpenCode `~/.config/opencode/AGENTS.md`, Pi `~/.pi/agent/AGENTS.md`. For any other agent, use its equivalent global rules file; if your global rules can only be set in a settings screen, tell me what to paste there instead. Create the file if it doesn't exist. Keep everything already in it, but replace any existing instruction about Wrangler or the Cloudflare CLI instead of adding a conflicting one. If the same guidance is already there, leave the file as it is. When you're done, tell me the path of the file you changed.
    
    ```markdown
    ## Cloudflare CLI - cf - v20260928
    
    `cf` is Cloudflare's current CLI and covers the whole Cloudflare platform. Prefer it over Wrangler: create projects with `cf init`, develop with `cf dev`, deploy with `cf deploy`, and manage account resources with `cf <product> …` (for example `cf d1 list`).
    
    Wrangler is only for projects that already use it – a `wrangler.jsonc`, `wrangler.json` or `wrangler.toml` file – or when the user asks for it. Keep using Wrangler in those projects unless asked to migrate, and use `cf migrate` in this case.
    
    `cf` commands differ from Wrangler's; check `cf --help` or `cf cli search <what you want to do>` instead of guessing. If a `cf` command fails in a project that doesn't use Wrangler, don't fall back to Wrangler (including `npx wrangler`) without offering to report it.

## **cf gibt Ihrem Agent Zugriff auf die gesamte Cloudflare-API**

Was wäre, wenn Ihr Agent alle Möglichkeiten von Cloudflare nutzen könnte? Diese Frage hat uns Anfang des Jahres beschäftigt: Agents wurden immer leistungsfähiger, doch ihre Möglichkeiten mit der Cloudflare-CLI blieben begrenzt.

Die Befehle von Wrangler wurden einzeln implementiert. Dabei verfolgte jedes Produktteam einen eigenen Ansatz für ihre Gestaltung und Bedienung. Einheitliche Konventionen über alle Teams hinweg durchzusetzen, war selbst bei unseren rund 280 Befehlsvarianten nahezu unmöglich. Ähnliche Befehle waren unterschiedlich benannt, `etwa d1 info, hyperdrive getund workflows describe`, weil jedes Team zu unterschiedlichen Zeitpunkten eigene Konventionen entwickelt hatte. Manche Teams schrieben Tausende von Codezeilen für maßgeschneiderte Funktionen, die später kaum genutzt wurden . Gleichzeitig entwickelten Teams unterschiedliche Ansätze zur Lösung derselben Probleme.

Wir wollten die bestehenden Befehle vereinheitlichen und den Funktionsumfang erheblich erweitern – und zwar in einem Schritt. Möglich wurde das durch [Forge](https://blog.cloudflare.com/forge-open-source-generation-pipeline), Cloudflares neue einheitliche Pipeline zur API-Generierung. Die Idee dahinter: Wir erzeugen die CLI-Befehle direkt aus demselben API-Schema, das auch unserer API-Dokumentation und der Generierung unserer SDKs zugrunde liegt. Alle unsere API-Funktionen sind durch ein OpenAPI-Schema beschrieben. Wenn wir dieses um einige zusätzliche Angaben ergänzen, können Forge daraus eine CLI erzeugen.

Damit kann `cf` sämtliche mehr als 3.000 Operationen der Cloudflare-API abdecken – weit mehr als die rund 280 Funktionen, die Wrangler im Laufe der Zeit erhalten hat.

Jetzt ist es ganz einfach, Ihrem Agent `cf` zu geben und ihn zu bitten, einen Worker einzurichten, ihn bereitzustellen, ihn zu überwachen, ihn mit Cloudflare Access zu schützen, eine Domain zu kaufen und sie mit Cloudflare WAF abzusichern – alles mit einem einzigen Tool.

## **Für einen Agent entwickeln, der cf noch nie verwendet hat**

cf ist auf die Zukunft der Softwareentwicklung ausgerichtet. Agents verändern grundlegend, wie Software entwickelt und bereitgestellt wird. Dieses Jahr haben wir uns darauf konzentriert, Werkzeuge zu entwickeln, die diesen Wandel unterstützen. cf bündelt diese Arbeit. Die CLI wurde von Grund auf für die Nutzung durch Agents entwickelt und bietet neue Funktionen, mit denen sie selbstständig passende Befehle finden können. Wir erwarten, dass solche Funktionen schon bald auch in anderen CLIs zum Standard gehören werden.

Wrangler hatte einen Vorteil: Über Jahre veröffentlichte Dokumentation, Blogbeiträge und Anleitungen von Drittanbietern sind in das Training großer Sprachmodelle eingeflossen. Doch dieser Vorteil hat auch eine Kehrseite. Wenn wir die Funktionsweise von Wrangler ändern, widerspricht das häufig den Nutzungsmustern, die diese Modelle bereits gelernt haben. Angesichts der umfangreichen Verbesserungen, die wir vorhaben, wären tiefgreifende Änderungen jedoch unvermeidlich gewesen.

Eine neue CLI einzuführen, die Agents noch nicht kennen, klingt zunächst nach einem einschneidenden Wechsel. Tatsächlich ist es die sauberste Lösung. Wir können cf gezielt gestalten und den Agenten zusätzliche Informationen im Kontext sowie Hinweise über AGENTS.md-Dateien bereitstellen. Das macht den Umstieg weniger verwirrend, als wenn ein Agent die erheblichen Unterschiede zwischen zwei Versionen eines vertrauten Tools erkennen und berücksichtigen müsste. Zum Start sind bereits einige dieser speziell für Agents entwickelten Funktionen enthalten. Weitere werden folgen.

## **Agents müssen JSON filtern, keine Tabellen lesen**

Wenn Agents Wrangler verwenden, hängen sie `--json` an jeden Befehl an und filtern die Ausgabe oft mit `jq`, um eine Teilmenge der Felder zu extrahieren. Allerdings unterstützten bisher nur einige Wrangler-Befehle die Option `--json`. Viele lieferten stattdessen Unicode-Tabellen, die für Menschen gedacht waren, die Ergebnisse direkt im Terminal lesen. Agents können solche Tabellen zwar auswerten, benötigen dafür aber mehr Zeit und Tokens als ein `jq`-Filter.

Bei cf gehen wir deshalb anders vor: Agents brauchen JSON. Wenn sie künftig die Hauptnutzer dieses Werkzeugs sind, sollte JSON auch das Standardformat sein. Für die große Mehrheit der Befehle, die Menschen nur selten direkt aufrufen werden, ist das die naheliegende Lösung.

Als Mensch nutzen Sie diese CLI häufig indirekt über einen Agent. Sinnvoller ist es deshalb, wenn der Agent die Ergebnisse einfach filtern und im gewünschten Format für Sie aufbereiten kann. Tabellen, die Sie wahrscheinlich ohnehin nie direkt lesen würden, helfen dabei wenig.

Doch was ist, wenn eine Aufgabe Ihre eigenen Angaben oder Entscheidungen erfordert – etwa die Suche nach einer Domain, die Sie kaufen möchten?

Wo Ihr Agent eine lange Liste benannter Parameter übergeben muss, können Sie stattdessen einfach ein Formular ausfüllen. cf übersetzt die Anforderungen der API in einzelne Eingabefelder und prüft die eingegebenen Werte. So werden Sie auch bei Domains mit komplexeren Anforderungen Schritt für Schritt durch den Kauf geführt.

Oder Sie überlassen auch diese Aufgabe einfach Ihrem Agent.

## **Ihr Agent findet den passenden Befehl selbst**

Bei rund 3.000 verfügbaren Operationen stellt sich eine Frage: Wie findet Ihr Agent schnell den passenden Befehl, ohne das Kontextfenster mit unnötigen Informationen zu füllen? Dafür haben wir `cf cli search` eingeführt.

Mit diesem Befehl kann Ihr Agent in natürlicher Sprache beschreiben, was er erledigen möchte. Ein kompakter Suchindex liefert daraufhin passende Befehle anhand ihrer API-Beschreibungen und Parameter. Sobald der Agent erstmals die Hilfe mit `--help` aufruft, weisen wir ihn automatisch auf diese Suchfunktion hin.

## **Konfiguration, die Typprüfungen für Ihren Agent durchführt**

Unser neues Konfigurationsformat basiert auf TypeScript. Es ist für Menschen und Agents leicht zu lesen und ermöglicht es Ihnen, Ihre Konfiguration mithilfe von Code zu erzeugen.

Typinformationen sind für Agents besonders hilfreich. Unsere Erfahrungen zeigen, dass sie die Konfiguration auch ohne Vorkenntnisse des neuen Formats problemlos finden und bei Bedarf bearbeiten können. Das gilt selbst für Elemente wie `env`, deren Funktionsweise sich deutlich vom gleichnamigen Element in Wrangler unterscheidet. Agents mit LSP-Unterstützung, etwa Claude Code und Codex, können die Struktur und die Typinformationen der Konfiguration besser auswerten. Dadurch machen sie wesentlich präzisere Vorschläge.

Bei TOML stand dagegen kein zugängliches Schema zur Verfügung. JSONC hatte zwar ein verknüpftes Schema, doch Agents nutzten es nur selten.

Einige interne Wrangler-Konfigurationen mit mehr als 5.000 Zeilen konnten wir um 40 % verkürzen. Sie enthielten zahlreiche individuell angepasste Entwicklungsumgebungen. Statt diese einzeln festzulegen, erzeugen nun Factory-Dateien die Konfiguration für die jeweiligen Entwicklerinnen und Entwickler.

Dazu wird jede Umgebung auf Grundlage einer gemeinsamen Basiskonfiguration erzeugt. Das Kopieren von `env`-Blöcken, wie es bei Wrangler üblich war, entfällt. Ein einfacher Worker mit mehreren Umgebungen wechselt einfach über das Vite-native `Modus`-Argument zwischen einem Konfigurationssatz und einem anderen.

Eine einfache Konfiguration dafür sieht so aus:

Mit `cf migrate` können Sie Ihren Cloudflare Worker auf das neue Konfigurationsformat umstellen.

Außerdem stellen wir einige Hilfsfunktionen bereit, die Ihnen die Entwicklung Ihres Workers erleichtern.

Mit `bindings` findet Ihr KI-Agent an einer zentralen Stelle alle Möglichkeiten der Entwicklerplattform. Ihr Editor kann die verfügbaren Optionen automatisch vervollständigen und erläutern – von Umgebungsvariablen über Speicher und Datenbanken bis hin zu Warteschlangen

Außerdem haben wir eine Hilfsfunktion für `triggers` ergänzt. Damit definieren Sie Routen, Warteschlangen, Zeitpläne und E-Mail-Auslöser für Ihren Worker. Diese Angaben sind nicht mehr über die Konfigurationsdatei verteilt. Stattdessen sehen Sie in einem einzigen Block, welche Ereignisse die Ausführung Ihres Workers auslösen können.

`defineConfig.worker` ist dabei erst der Anfang. Unser Ziel ist es, dass Sie mit cloudflare.config.ts künftig Ihre gesamte Cloudflare-Konfiguration verwalten können. Jedes benötigte Produkt soll sich über eine typsichere Konfiguration einrichten lassen, während seine API Ihrem KI-Agenten über cf zur Verfügung steht. Schon bald können Sie über diese Konfigurationsdatei auch vollständige Richtlinien konfigurieren, Zonen einrichten, DNS-Einstellungen verwalten und vieles mehr.

## **Eine erstklassige Entwicklererfahrung**

Als Wrangler erstmals Builds für JavaScript-Workers unterstützte, gab es [Vite](https://vite.dev/) noch nicht. Deshalb nutzten wir esbuild, um Ihre Workers zu bündeln. Auch der Entwicklungsserver auf Port 8787 wurde vom Wrangler-Team selbst entwickelt. Änderungen daran erforderten Eingriffe in die internen Abläufe lokaler Cloudflare-Werkzeuge wie Miniflare.

Vite verbessert diesen Ansatz erheblich. Es bietet ein großes Plugin-Ökosystem und einen erstklassigen Entwicklungsserver mit Hot Module Replacement (HMR). Für Builds nutzt es die Rust-basierte Bibliothek Rolldown, die nicht benötigten Code durch Tree-Shaking entfernt. Alles, was mit Vite möglich ist, können Sie auch mit dem Cloudflare Vite Plugin umsetzen.

Wir empfehlen das Cloudflare Vite Plugin für die Entwicklung von Workers – unabhängig davon, ob Sie ein Frontend-Projekt oder eine Backend-API entwickeln. Zusammen mit unserem Vitest-Plugin bietet es eine einheitliche Entwicklungs- und Testumgebung, die der Laufzeitumgebung von Cloudflare Workers entspricht. Dabei haben Sie direkten Zugriff auf Bindings und Plattform-APIs.

cf nutzt standardmäßig Vite. Die meisten Ihrer Workers lassen sich mithilfe von Agents leicht migrieren. Bei anderen kann die Umstellung mehr Zeit benötigen. Deshalb greift cf für die lokale Entwicklung und Bereitstellung weiterhin auf Wrangler zurück, wenn JavaScript-Workers noch esbuild benötigen. Das gilt auch für Rust- und Python-Workers.

## **Von Wrangler zu cf migrieren**

Um einen Worker von Wrangler zu cf zu migrieren, führen Sie einfach cf migrate aus.

Bei Workers, die bereits Vite nutzen, wird die Konfiguration automatisch in das Format cloudflare.config.ts überführt. Wenn Ihr Worker für die Nutzung von esbuild auf Wrangler angewiesen ist, übernimmt Wrangler weiterhin die Builds.

Nach dem Ende der öffentlichen Beta veröffentlichen wir eine letzte Hauptversion von Wrangler, die Sie und Ihren Agents auf die Nutzung von cf verweist. Anschließend werden wir Wrangler noch 18 Monate lang warten, damit Sie genügend Zeit für die Migration haben.

Auch neue Projekte können Sie mit `cf init` beziehungsweise `cf deploy` automatisch für Cloudflare konfigurieren. Dabei wird das Cloudflare Vite Plugin installiert und eine Konfigurationsdatei erstellt.

Für die Bereitstellung statischer Websites benötigen Sie weiterhin keine Konfigurationsdatei. Führen Sie dazu einfach `cf deploy` in Ihrem Projektverzeichnis aus.

Ein neues Hello-World-Projekt erstellen Sie mit` cf init`.

_cf ist Open Source. Probleme können Sie[ in unserem GitHub-Repository melden](https://github.com/cloudflare/cf)_.

]]>01M3TNSGYX6M1J3A2CPQ3M7W02Wir stellen Forge vor: die Open-Source-Pipeline zur Generierung von SDKs, CLIs, Dokumentation und mehrhttps://blog.cloudflare.com/de-de/forge-open-source-generation-pipeline/ Thu, 01 Oct 2026 08:56:21 GMTForge ist eine Open-Source-Generierungs-Pipeline, die modular erweiterbar ist und in CI läuft, um SDKs, CLIs und Dokumentation direkt aus API-Definitionen zu generieren. Durch die Verlagerung der Generierung in die einzelnen Team-Repositories hält Forge Entwicklertools kontinuierlich synchron.AgentsAPIBirthday WeekCLIEntwicklerSDKHeute stellen wir [Forge](https://github.com/cloudflare/forge) vor – einen frischen Ansatz zur Generierung von SDKs, CLIs, Dokumentation und Bibliotheken. Forge ist eine modular erweiterbare Open-Source-Generierungs-Pipeline, die jeder kostenlos auf eigener Infrastruktur einsetzen und betreiben kann.

Forge steht noch am Anfang, generiert aber bereits die benötigten Ausgaben für die [cf CLI](https://blog.cloudflare.com/cloudflare-cf-cli-launch/) In den kommenden Monaten wird es auch die API-Dokumentation, SDKs und vieles mehr von Cloudflare generieren.

Wir haben Forge entwickelt, weil wir selbst ein solches Werkzeug brauchten, um Agents als Kunden bedienen zu können. Jetzt veröffentlichen wir es als Open Source. Denn wir finden, dass jeder die Schnittstellen und Werkzeuge generieren können sollte, die KI-Agenten benötigen. Früher brauchten vor allem Produkte für Entwicklerinnen und Entwickler eine CLI, API-SDKs und MCP-Server – jeweils mit einer guten Dokumentation. Heute gehört all das zur Grundausstattung jedes Produkts.

## **Unsere API ist zu groß für die bisherigen Generatoren geworden**

Die API von Cloudflare umfasst über 3.500 Operationen. Dahinter stehen Hunderte von Diensten, die in unterschiedlichen Programmiersprachen entwickelt wurden, darunter Rust, Go, TypeScript und Python. Für eine CLI, die die gesamte Cloudflare-API abdeckt, sowie für unsere SDKs und die API-Dokumentation brauchten wir eine Pipeline zur Codegenerierung, die mit diesem Umfang umgehen kann. Gleichzeitig musste sie verschiedene Sprachen unterstützen und sich in die unterschiedlichen Arbeitsabläufe unserer Entwicklungsteams einfügen.

Wir wollten den Abstimmungsaufwand zwischen den Teams reduzieren. Wenn ein Produktteam eine API ändert, muss es vorab testen können, wie sich diese Änderung auf die CLI für ganz Cloudflare, die SDKs und die Dokumentationswebsite auswirkt. Dazu braucht es Vorschauversionen – bevor die Änderung zusammengeführt und an Kunden ausgeliefert wird. So lässt sich prüfen, ob der Generierungsprozess weiterhin funktioniert. Außerdem wollten wir das System erweitern können, um mehr als SDKs zu erzeugen: etwa Komponenten für Cap’n Web, MCP-Server und weitere Integrationen.

Wir haben mehrere gehostete Produkte ausprobiert, die dieses Problem lösen sollen, und einige davon auch produktiv eingesetzt. Doch keines erfüllte unsere Anforderungen vollständig. Einige wurden sogar ganz eingestellt. Immer wieder führte ein Team eine Änderung zusammen, die unbemerkt den Generierungsprozess störte. Ein anderes Team bemerkte das erst bei der Veröffentlichung. Wir verbrachten zu viel Zeit damit, die Einschränkungen gehosteter Tools zu umgehen, die wir nicht selbst kontrollieren konnten, und Änderungen zwischen Teams und Anbietern abzustimmen.

Deshalb haben wir begonnen, Forge zu entwickeln.

Forge soll diese Probleme lösen. Es läuft direkt in den CI-Pipelines der API-Repositories unserer Teams – ebenso wie unsere KI-gestützte Codeprüfung und unsere automatisierten Tests. Forge prüft jede Änderung mit einem Linter und erstellt anschließend Vorschauversionen der CLI, der Dokumentation und der SDKs. Darin sind eure Änderungen hervorgehoben. Ihr könnt die Vorschauversionen installieren und direkt testen. Das Prinzip entspricht dem von [Workers Previews](https://blog.cloudflare.com/worker-previews/): Für jede Änderung entsteht eine vollständige Vorschauversion. Forge überträgt diesen Ansatz auf die SDK-Generierung im großen Maßstab – auch wenn die API-Funktionen über Hunderte von Diensten und Repositories verteilt sind. Genau dafür entwickeln wir Forge.

## **Forge-Transformer können mehr als SDKs generieren - ​​auch für Cap'n Web**

Für Cloudflare ist ein Generator besonders wichtig, der mehr kann als SDKs für verschiedene Programmiersprachen zu erzeugen. [Cap’n Web](https://capnweb.com/) ist Cloudflares RPC-System. Damit lassen sich entfernte APIs aus TypeScript heraus so aufrufen, als wären es lokale Methoden.

Forge kann die benötigten Komponenten für Cap’n Web direkt aus einer OpenAPI-Spezifikation generieren. Damit lassen sich künftig auch Bindings erzeugen, über die Workers auf andere APIs zugreifen können. Schließlich sind [Bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/) in der Workers-Laufzeitumgebung selbst als Workers implementiert, die RPC-Methoden bereitstellen.

Dieser Ansatz ist nicht auf Cap’n Web beschränkt. Auch andere verbreitete Tools, die ihr vielleicht bereits nutzt, profitieren davon. Wenn ihr mit [TanStack Query](https://tanstack.com/query/) arbeitet, wäre es beispielsweise hilfreich, die passenden Bindings für eure Anwendung direkt aus eurer eigenen API generieren zu können. So bleiben sie aktuell und werden anhand eurer tatsächlichen API geprüft. Dasselbe gilt für Zod- oder Valibot-Schemas, MCP-Server und andere Komponenten, die die Nutzung eurer API erleichtern.

Möglich wird das durch die flexiblen Codegeneratoren von Forge. Sie sind darauf ausgelegt, die Ergebnisse eines Generierungsschritts im nächsten weiterzuverwenden.

## **Forge-Transformer können verketten: Ergebnisse weiterverwenden**

Wir haben Forge so konzipiert, dass es modular erweiterbar ist und viele Eingabe- und Ausgabetypen unterstützt. Forge bietet CLI-, SDK- und Dokumentationsgeneratoren. Ihr könnt aber auch eigene Transformer ergänzen, die ein Paket für eine bestimmte Bibliothek, ein vollständiges Dashboard oder eine Anwendung erzeugen. Derzeit unterstützt Forge OpenAPI als Eingabeformat. Die Architektur ist jedoch darauf vorbereitet, künftig auch [AsyncAPI](http://asyncapi.com), GraphQL, Cap’n Proto, Protobuf und weitere Formate zu verarbeiten

Dabei geht es um mehr als die Unterstützung verschiedener Formate: Ihr könnt mehrere Generierungsschritte miteinander verknüpfen und die Ergebnisse eines Schritts als Grundlage für weitere nutzen. Andere Generatoren machen das ebenfalls. Sie erzeugen beispielsweise CLIs und Terraform-Komponenten auf Grundlage eines Go-SDKs. Was bisher fehlt und Forge ermöglicht: Ihr legt selbst fest, wie diese Schritte miteinander verbunden werden.

Wir brauchten diese Möglichkeit für unsere eigene cf-CLI, die in TypeScript geschrieben ist. Andere SDK-Generatoren nutzen TypeScript-SDKs jedoch in der Regel nicht als Grundlage für die CLI-Generierung. Dabei wurde uns eine grundlegendere Frage klar: Warum sollte ein SDK-Generator diese Entscheidung für euch treffen? Vielleicht arbeitet euer Team hauptsächlich mit Python und möchte auch die CLI in Python entwickeln.

Vielleicht fragt ihr euch jetzt: Ist die Programmiersprache nicht egal, wenn der Code ohnehin automatisch generiert wird? Bei CLIs macht sie tatsächlich einen Unterschied. Denn CLIs bieten häufig Funktionen, die ausschließlich lokal ausgeführt werden und in einem SDK keinen Sinn ergeben würden. Diese Funktionen implementiert ihr von Hand, weil sie nicht auf einem API-Aufruf beruhen. Die cf-CLI enthält beispielsweise Befehle wie cf dev und cf build, die wir den generierten Befehlen manuell ergänzen. Sie müssen TypeScript-APIs aus anderen Paketen wie Vite aufrufen können.

Hinzu kommt die Dokumentation. Wenn ihr sowohl die CLI als auch die Dokumentation ausschließlich aus eurer OpenAPI-Spezifikation generiert, stellt sich eine weitere Frage: Wie werden die manuell implementierten Befehle ebenfalls automatisch dokumentiert?

Wir haben kein bestehendes Tool gefunden, das diese Aufgabe übernimmt. Genau diese Funktion brauchen wir aber für cf. Deshalb integrieren wir sie in Forge.

## **Die API weiterentwickeln, ohne Nutzer zu beeinträchtigen**

Forge schafft auch die Grundlage für eine bessere API-Versionierung. Seit zehn Jahren ist v4 die einzige Hauptversion der Cloudflare-API. Nach außen wirkt es deshalb so, als hätten wir seitdem keine neuen Hauptversionen veröffentlicht. Nach den Regeln der semantischen Versionierung (SemVer) hätten allerdings mehrere unserer Änderungen eine neue Hauptversion erfordert. Gleichzeitig tragen einige API-Operationen noch interne Kennzeichnungen wie „v2“ oder „beta“, obwohl die entsprechenden Entwicklungsphasen längst abgeschlossen sind.

Nach so vielen Jahren mit unserer v4-API wissen wir, dass ein umfassender Wechsel auf Version 5 viele unserer Kunden vor Probleme stellen würde. Deshalb arbeiten wir an einem Versionierungsansatz, mit dem wir neue API-Hauptversionen veröffentlichen können, ohne die Kompatibilität mit bestehenden Clients oder SDKs zu verlieren. Parallel dazu stellt Forge nach und nach die generierten Komponenten bereit.

Schon bald werden wir mehr über unsere SDKs und die Unterstützung für TypeScript, Rust, Python, Go, PHP und Terraform berichten. Besonders über Terraform. Wir wissen, dass Updates von Terraform-Providern sorgfältig vorbereitet werden müssen. Deshalb werden wir bei dieser Umstellung besonders behutsam vorgehen.

## **Wichtige Tools sollten allen offenstehen**

Die Entwicklung von Werkzeugen für APIs ist für uns ein wesentlicher Bestandteil des Internets. Dafür solltet ihr nicht auf einen SaaS-Dienst angewiesen sein. Eure SDKs, CLIs und eure Dokumentation sollten euch gehören. Wenn ihr sie generiert, solltet ihr sie kostenlos so nutzen und dort betreiben können, wie und wo ihr möchtet.

Deshalb veröffentlichen wir [Forge als Open Source](https://github.com/cloudflare/forge) unter der Apache-2.0-Lizenz. Wir freuen uns über alle, die Forge gemeinsam mit uns weiterentwickeln möchten.

Ihr möchtet eure Anpassungen lieber für euch behalten? Auch das ist möglich. Ihr könnt Forge kostenlos für beliebige Zwecke auf eurer eigenen Infrastruktur betreiben und an eure Anforderungen anpassen, ohne eure Änderungen veröffentlichen zu müssen.

_Danksagung: Auch die Arbeit von Dan Carter, Steven Chong, Krishna Paritala und Shelley Jones an der Konzeption und Implementierung hat dieses Projekt möglich gemacht._

]]>01M3TMHBHSE7A1QBXGF1BN4CEMCloudflares Gründerbrief 2026https://blog.cloudflare.com/de-de/cloudflares-2026-annual-founders-letter/ Wed, 30 Sep 2026 03:11:31 GMTSeit dem Start von Cloudflare am 27. September 2010 hat sich das Internet noch nie so stark verändert wie heute. Inzwischen übersteigt der automatisierte Datenverkehr den von Menschen verursachten. Wir werfen einen Blick auf den Aufstieg von KI-Agenten und eine neue Generation von Kreativen – und fragen uns, wie wir zu einer fairen und nachhaltigen Zukunft des Webs beitragen können.AIBirthday WeekBrief der GründerEntwicklerplattformInternet-TrendsDiese Woche feiert Cloudflare seinen 16. Geburtstag. Wie viele 16-Jährige blicken auch wir auf die Welt, in der wir aufgewachsen sind, und fühlen uns zwischen Vergangenheit und Zukunft hin- und hergerissen. Die vielen Veränderungen um uns herum bereiten uns manchmal Sorgen. Insgesamt sind wir aber sehr zuversichtlich, wenn wir an die Zukunft denken. Beides hat denselben Grund: Veränderung bringt immer auch Umbrüche mit sich.

Seit dem Start von Cloudflare am 27. September 2010 hat sich das Internet zu keinem Zeitpunkt so stark verändert wie heute. Manche dieser Veränderungen sind zweifellos positiv. Andere stellen unsere bisherigen Vorstellungen davon, wie das Internet funktioniert, auf den Kopf.

Besonders deutlich zeigt sich der Wandel beim Wachstum des Webs. Von 2012 bis 2025 stagnierte das Web; je nach Messmethode schrumpfte es sogar. Mitte 2025 änderte sich das: Die Zahl neuer Websites stieg sprunghaft an. Oft heißt es, dieses Wachstum gehe vor allem auf KI-generierten „Schrott“ zurück. Den gibt es durchaus. Nach unseren Beobachtungen macht er jedoch nicht den Großteil aus.

Stattdessen eröffnet KI einer neuen Generation von Kreativen Möglichkeiten. Menschen mit Ideen, denen bisher die Programmierkenntnisse fehlten, können mithilfe sogenannter Vibe-Coding-Tools eigene Anwendungen entwickeln. Wir freuen uns, dass die meisten dieser Tools Cloudflares Entwicklerplattform bevorzugt nutzen, um solche Anwendungen bereitzustellen. Technologie zeigt sich von ihrer besten Seite, wenn sie mehr Menschen ermöglicht, ihre Ideen umzusetzen. Wir erleben aus nächster Nähe, wie Studierende weltweit Apps entwickeln, die konkrete Probleme lösen, und wie Startups neue Geschäftsideen in Rekordzeit verwirklichen. Heute gestalten mehr als sieben Millionen Entwicklerinnen und Entwickler auf Cloudflares Plattform die Zukunft.

Im vergangenen Jahr hat sich auch verändert, wer – und zunehmend was – das Internet nutzt. Ursprünglich hatten wir erwartet, dass automatisierter Datenverkehr den von Menschen verursachten Datenverkehr erst in der zweiten Hälfte des Jahres 2027 überholen würde. Durch den Aufstieg von KI-Agenten und KI-Crawlern war es schon im Mai 2026 so weit. Wenn sich die aktuellen Trends fortsetzen – und diese Annahme erscheint eher vorsichtig –, könnte der automatisierte Datenverkehr in nur fünf Jahren tausendmal so groß sein wie der von Menschen verursachte. Das liegt nicht daran, dass wir mit weniger menschlichem Datenverkehr rechnen. Vielmehr wächst der Datenverkehr durch KI-Agenten rasant.

Für ihre Nutzerinnen und Nutzer leisten KI-Agenten schon heute Erstaunliches. Bitten Sie einen KI-Agenten, für Sie einen Flug, einen Handwerker oder einen günstigeren Handytarif zu finden: Er liest in einer Minute mehr Seiten, als Sie an einem ganzen Nachmittag schaffen würden, und liefert Ihnen anschließend eine Antwort. Er erledigt die Recherche, damit Sie das nicht selbst tun müssen.

Doch die Recherche eines KI-Agenten verursacht Aufwand. Wenn Sie ihn nach einem Restaurant für die Mittagspause fragen, prüft er vielleicht die Speisekarten von 1.000 Lokalen in Ihrer Nähe und empfiehlt am Ende nur eines. Dieses Restaurant gewinnt Sie als Gast. Auch die anderen 999 mussten die Anfragen des Agenten verarbeiten, bekommen dafür aber nichts. Das ist ein Allmendeproblem: Die Menschen, die den Agenten nutzen, profitieren von seiner Suche, während die Kosten auch bei den Lokalen entstehen, die leer ausgehen. Weil die Nutzerinnen und Nutzer diese Kosten nicht selbst tragen, haben sie wenig Anlass, die Zahl solcher Anfragen zu begrenzen.

KI macht es Studierenden und Startups so leicht wie nie, neue Angebote zu entwickeln. KI-Agenten könnten es jedoch allen schwerer machen, diese Angebote überhaupt zu entdecken. Heute gewinnen kleine Unternehmen Kundschaft oft durch persönliche Bindung oder weil sie bequem erreichbar sind. Sie gehen vielleicht immer wieder in dasselbe Lokal, weil man Sie dort beim Namen kennt oder weil der Ort einfach zu Ihrem Leben gehört. Oder Sie kaufen im Laden um die Ecke ein, obwohl Auswahl und Preise anderswo besser sind – weil er auf Ihrem Heimweg liegt.

Einem KI-Agenten ist es gleichgültig, ob man Sie in einem Lokal beim Namen kennt oder ob ein Geschäft auf Ihrem Heimweg liegt. Er bevorzugt Anbieter, über die er besonders viele Informationen findet. Das sind meist Unternehmen, die schon lange am Markt sind. Je mehr Kaufentscheidungen KI-Agenten übernehmen, desto schwerer könnte es deshalb für neue Anbieter werden, Fuß zu fassen. Langfristig könnten sich so immer weniger Unternehmen den Markt teilen – und die Vielfalt würde leiden.

Wir waren selbst einmal neu auf dem Markt. Vor 16 Jahren stellten wir Cloudflare auf der Bühne der TechCrunch Disrupt vor, während unsere Ingenieurinnen und Ingenieure im Publikum noch Fehler behoben. Als wir die Bühne betraten, waren acht Fehler offen. Als wir von der Bühne gingen, waren alle behoben – und Cloudflare lief bereits in fünf Rechenzentren auf drei Kontinenten. Ein KI-Agent hätte uns damals wohl nicht empfohlen. Menschen haben uns trotzdem eine Chance gegeben. Diese Chance sollen auch die nächsten neuen Unternehmen bekommen.

Dafür setzen wir uns ein: für eine Zukunft mit 500.000 KI-Unternehmen auf der ganzen Welt statt nur fünf. Für eine Zukunft, in der Menschen mit ihren Inhalten ein weltweites Publikum erreichen und für ihre Arbeit bezahlt werden können. Und für eine Zukunft, in der sich neue Anbieter mit besseren Produkten durchsetzen können, statt dass einige wenige Großkonzerne von vornherein die besten Chancen haben.

Letztes Jahr haben wir darüber geschrieben, wie KI das Geschäft von Verlagen verändert. Jetzt bekommen auch Restaurants und kleine Lokale diesen Wandel zu spüren. Wodurch das bisherige Geschäftsmodell des Internets ersetzt wird, ist eine der spannendsten Fragen der nächsten fünf Jahre. Diese Woche versuchen wir erneut, eine Antwort darauf zu geben.

Wie an jedem Geburtstag feiern wir, indem wir Geschenke machen, statt welche zu bekommen. Einige davon sind für die 999 Restaurants gedacht, die bei der Empfehlung durch den KI-Agenten leer ausgehen. KI-Agenten durchsuchen das Web ähnlich wie Suchmaschinen: Sie rufen Seiten immer wieder ab, unabhängig davon, ob sich dort etwas geändert hat. Unsere Daten zeigen, dass mehr als die Hälfte der Inhalte, die seriöse Bots abrufen, seit dem letzten Besuch unverändert ist. Wir arbeiten daran, dass Crawler mehr vom Web erfassen können, dabei aber nur neue oder geänderte Inhalte abrufen. Das entlastet die Websites. Außerdem schaffen wir für alle, die Inhalte oder Anwendungen online stellen, eine Möglichkeit, bezahlt zu werden, wenn KI-Agenten diese Inhalte oder Anwendungen nutzen.

Die Mission von Cloudflare ist es nicht, allein ein besseres Internet zu schaffen, sondern dabei mitzuhelfen. Das können wir nur gemeinsam mit anderen. Deshalb werden wir diese Woche auch Partnerschaften mit Unternehmen und Organisationen ankündigen, die unsere Vorstellung von der Zukunft teilen.

Wie andere 16-Jährige haben auch wir im neuen KI-Zeitalter klare Vorstellungen davon, wie die Zukunft aussehen soll. Und wir können sie in die Tat umsetzen. Wir setzen uns für ein Internet ein, in dem auch künftig Platz ist: für einen Teenager, der seine erste App veröffentlicht, für das kleine Lokal, in dem man Sie beim Namen kennt, und für Menschen, die gerade das nächste Cloudflare aufbauen.

Wir freuen uns mehr denn je auf das, was vor uns liegt.

]]>01M3R4G8Y5K2S7PWV7F1ZK718VBeides ist möglich: Auffindbar bleiben und gleichzeitig KI-Training untersagenhttps://blog.cloudflare.com/de-de/accountable-mixed-use-ai-crawlers/ Fri, 18 Sep 2026 02:34:22 GMTCloudflare gibt Websitebetreibern die Möglichkeit, weiterhin auffindbar zu bleiben und gleichzeitig die Nutzung ihrer Inhalte für KI-Training zu untersagen. Neue Kontrollmöglichkeiten und die Kennzeichnung „Accountable“ etablieren zusammen mit Apple, Google und Microsoft ein gemeinsames Modell.AIAI Bots (DE)Bot-ManagementNetzwerk-ServicesProdukt-NewsSicherheitOhne angemessene Kontrollmöglichkeiten mussten Websitebetreiber lange eine schwierige Abwägung treffen: ihre Inhalte für KI-Training freigeben oder riskieren, in der Suche schlechter beziehungsweise gar nicht mehr auffindbar zu sein. Der Grund dafür ist, dass einige der größten Organisationen im Internet Mixed-Use-Crawler verwenden – also einen einzigen Crawler für Suche und KI-Training. Wer das eine ablehnt, lehnt damit auch das andere ab.

Heute kündigt Cloudflare eine neue Einstellung namens „[Disallow AI Training](https://blog.cloudflare.com/bot-preference-sync/)“ an, mit der Websites problemlos für die Suche indexiert bleiben können, während demselben Crawler zugleich untersagt wird, die Inhalte für KI-Training zu verwenden. Apple, Google und Microsoft berücksichtigen diese Einstellung bereits oder haben sich verpflichtet, sie innerhalb eines festgelegten Zeitrahmens zu unterstützen.

Mixed-Use-Crawler waren die größte Herausforderung beim Thema KI-Training. KI-Zusammenfassungen sind als Nächstes dran. Eine pauschale Ja-oder-Nein-Entscheidung für die gesamte Website greift zu kurz: Wie viel des eigenen Inhalts in einer Zusammenfassung erscheint, ist ebenso wichtig wie die Frage, ob er überhaupt darin vorkommt. Eine Opt-out-Möglichkeit für KI-Zusammenfassungen gehört bereits zu den Anforderungen, die wir an Betreiber von Mixed-Use-Crawlern stellen. Bis Anfang nächsten Jahres möchten wir ermöglichen, zentral bei Cloudflare festzulegen, wie viel des eigenen Inhalts einbezogen werden darf, anstatt dies bei jedem Betreiber einzeln einstellen zu müssen.

## Warum es nicht ausreicht, nur zu fragen

Die meisten Websitebetreiber möchten gefunden werden – von Menschen, Agenten und seriösen Bots. Ein erheblicher Teil des offenen Internets finanziert sich jedoch durch Werbung, Abonnements oder direkte Beziehungen zu Besuchern, und diese Modelle funktionieren nur, wenn tatsächlich jemand die Website besucht.

Fast alle Websitebetreiber betrachten Suchdienste als nützlich: Weniger als 1 % der Websites bei Cloudflare blockieren Suchmaschinen-Bots. Beim Training ist die Situation dagegen eine andere: 17 % der Websites aktivieren irgendeinen Mechanismus, um KI-Training zu unterbinden. Genau aus diesem Grund haben wir uns dafür entschieden, Websitebetreibern differenziertere Kontrollen an die Hand zu geben, statt auf eine Einheitslösung wie „Block AI“ zu setzen.

Eine robots.txt-Anweisung allein kann dieses Problem nicht lösen. Jeder kann eine solche Anweisung veröffentlichen, doch sie kann weder feststellen, wer crawlt, noch erkennen, zu welchem Zweck gecrawlt wird, noch einen Crawler stoppen, der sie ignoriert.

Ein Netzwerk kann dieses Problem jedoch lösen: Wir veröffentlichen die Präferenz, identifizieren, wer crawlt, klassifizieren, zu welchem Zweck gecrawlt wird, und blockieren diejenigen, die die Vorgabe ignorieren – anschließend berichten wir auf [Radar](https://radar.cloudflare.com/ai-insights#ai-bot-transparency) darüber, wie sich die einzelnen Betreiber tatsächlich verhalten.

Doch durch Blockieren wird lediglich ein Crawler ausgeschlossen. Es ändert nicht das Verhalten von Crawlern. Die bessere Lösung sind Betreiber, die Websitebetreiber gar nicht erst vor diese Entscheidung stellen. Deshalb sprechen wir seit Juli direkt mit ihnen. Die Reaktionen waren ermutigend: Fast alle waren sich einig, dass Websitebetreiber Kontrolle und Transparenz darüber haben sollten, wie ihre Inhalte genutzt werden, und die Gewissheit brauchen, dass ihre Entscheidungen respektiert werden. Um Websitebetreibern dabei Orientierung zu geben, haben wir eine Kennzeichnung eingeführt: „Accountable“.

Die Kennzeichnung „Accountable“ berücksichtigt sowohl bereits heute verfügbare Funktionen als auch konkrete Zusagen, diese künftig bereitzustellen. Um sich zu qualifizieren, muss ein Bot-Betreiber die folgenden Anforderungen erfüllen oder sich verbindlich dazu verpflichten, sie zu erfüllen:

  1. Eine Möglichkeit für Websitebetreiber, KI-Training über robots.txt oder einen ähnlichen Standard abzulehnen.
  2. Ein Mechanismus, mit dem Websitebetreiber KI-Zusammenfassungen direkt beim jeweiligen Betreiber ablehnen können und ab dem nächsten Jahr auch über Cloudflare (weitere Einzelheiten siehe Abschnitt unten).
  3. Transparenz auf URL-Ebene darüber, welche Seiten für das KI-Training verfügbar gemacht wurden, ergänzt durch Kennzahlen dazu, wie Inhalte in der Suche erschienen sind.
  4. Die Zusicherung, dass die Ablehnung von KI-Training keine Auswirkungen auf die traditionellen Suchergebnisse hat.



Apple, Google und Microsoft erfüllen nachweislich die Voraussetzungen für die Einstufung als „Accountable“. Jedes dieser Unternehmen kombiniert bereits heute verfügbare Funktionen mit zeitlich klar definierten Zusagen für Funktionen, die sich noch in Entwicklung befinden. Einzelheiten zu den Crawlern der jeweiligen Unternehmen finden Sie unten.

## Neue Optionen für Sicherheitseinstellungen

Cloudflare klassifiziert Bots nach ihrem Verhalten, wobei ein einzelner Bot mehrere Verhaltensweisen aufweisen kann. Drei Verhaltensweisen stehen als Steuerungsoptionen zur Verfügung:

  * **Suche** – Crawlen, um einen Suchindex aufzubauen.
  * **Training** – Crawlen, um ein Modell zu trainieren oder fein abzustimmen.
  * **Agent** – benutzergesteuerte Agenten, die im Auftrag eines Menschen eine Seite besuchen, wie zum Beispiel Chat-Abruf-Bots und Browser-Agenten.



Ein Mixed-Use-Crawler ist ein einzelner Crawler, der sowohl für die Suche als auch für das Training eingesetzt wird. Ohne entsprechende Steuerungsmöglichkeiten entsteht durch diese Kombination der oben beschriebene Zielkonflikt: Websitebetreiber können nicht eine Nutzungsart ablehnen, ohne zugleich auch die andere abzulehnen.

Damit „Accountable“-Mixed-Use-Crawler – also diejenigen, die Websitebetreiber nicht zu diesem Zielkonflikt zwingen – nicht blockiert werden, führen wir eine neue Einstellung ein: „Disallow AI Training“. Der Name „Disallow AI Training“ leitet sich von der Disallow: -Direktive ab, die in der robots.txt veröffentlicht wird.

### „Block“ hat als Einstellung jetzt eine andere Bedeutung.

Die Einstellungen „Block“ und „Block on pages with ads“ galten bisher nicht für Mixed-Use-Crawler, da deren Blockierung auch die Auffindbarkeit in der Suche beeinträchtigen konnte. Mit der neuen Einstellung „Disallow AI Training“ gelten „Block“ und „Block on pages with ads“ nun für _alle_ Trainings-Crawler, einschließlich Mixed-Use-Crawlern.

Die Steuerungsoptionen für Training, Suche und Agenten werden auf Domain-Ebene angewendet. Mit der Einführung von „Disallow AI Training“ stehen folgende Einstellungen zur Verfügung:

  1. **Allow (Erlauben)** : Alle Crawler sind erlaubt, es sei denn, sie werden durch eine andere Einstellung oder eine WAF-Regel blockiert.
  2. **Disallow AI Training (KI-Training untersagen)** : Bot Preference Sync veröffentlicht die jeweils geltende Präferenz gegen KI-Training in der robots.txt-Datei. „Accountable“-Mixed-Use-Crawler bleiben für die Suche zugelassen. Alle anderen Trainings-Crawler werden blockiert, einschließlich der ausschließlich für Training eingesetzten Crawler von Amazon, Anthropic, Meta und OpenAI – deren Blockierung hat keine Auswirkungen auf die Suche. „Disallow AI Training“ ist nur als Einstellung für Training verfügbar, nicht für Suche oder Agenten.
  3. **Block on pages with ads (Blockieren auf Seiten mit Anzeigen)** : Crawler, einschließlich Mixed-Use-Crawlern, werden nur auf Seiten blockiert, auf denen Werbung erkannt wird.
  4. **Block (Blockieren)** : Alle Crawler, einschließlich Mixed-Use-Crawlern, werden blockiert.



„Disallow AI Training“ funktioniert, indem eine entsprechende Präferenz in der robots.txt-Datei veröffentlicht wird. Eine nur für Seiten mit Werbung geltende Präferenz lässt sich auf diese Weise nicht ausdrücken: Cloudflare kann zwar erkennen, welche Seiten Werbung ausspielen, doch diese Liste ist zu umfangreich und ändert sich zu häufig, um sie in robots.txt aufzuführen. Deshalb gibt es keine Option „Disallow AI Training“ speziell für Seiten mit Werbung.

Agenten führen nicht zu demselben Zielkonflikt bei der Auffindbarkeit in der Suche wie Mixed-Use-Crawler, und im Internet gibt es bislang noch keine etablierte Direktive, mit der sich „Disallow“-Präferenzen für Agenten ausdrücken lassen. Daher führen wir vorerst keine „Disallow“-Einstellung für Agenten ein. Sobald Standards wie [ai-prefs](https://datatracker.ietf.org/wg/aipref/documents/) weiter ausgereift sind, werden wir diesen Ansatz erneut prüfen.

## Was ändert sich am 15. September?

Wir nehmen folgende Änderungen an Bot Management und AI Crawl Control vor:

  1. Die Einstellungen „Block“ und „Block on pages with ads“ gelten jetzt auch für Mixed-Use-Crawler, einschließlich Applebot, Bingbot und Googlebot, sodass beide Einstellungen die Suche sowie das Training beeinflussen. Wenn Sie das Training stoppen und die Suche _weiterhin ermöglichen_ möchten, verwenden Sie „Disallow AI Training“.
  2. „Block AI Bots“ wird zugunsten der detaillierteren Steuerungen für Suche, Training und Agenten eingestellt.
  3. Die Managed robots.txt wird zugunsten von Bot Preference Sync eingestellt. Kunden, die Managed Robots.txt aktiviert haben, werden auf das neue System migrieren.
  4. „Disallow AI Training“ wird Teil der empfohlenen Konfiguration für bestimmte neue Domains.
  5. Bei bestehenden Kunden werden die bisherigen Präferenzen wie nachfolgend beschrieben auf die neuen Steuerungsoptionen migriert.



### Was Sie tun müssen

In nahezu allen Fällen müssen Sie nichts tun. Ihre derzeitigen Einstellungen werden automatisch übertragen.

Wenn Mixed-Use-Crawler gar nicht mehr auf Ihre Website zugreifen sollen, müssen Sie dies jetzt ausdrücklich angeben. Wählen Sie „Block“. Damit werden Applebot, Bingbot und Googlebot vollständig blockiert – auch für die Suche.

#### Bestehende Domains, die die Steuerungsoptionen für Suche, Training oder Agenten bisher nie verwendet haben

Websitebetreiber, die die detaillierteren Steuerungsmöglichkeiten bislang nicht eingerichtet haben, werden entsprechend ihrer bisherigen „Block AI Bots“-Einstellung auf die neuen Einstellungen umgestellt:

#### Bestehende Domains, für die die Steuerungsoptionen für Suche, Training und Agenten bereits zuvor konfiguriert wurden

Für Domains, bei denen die granularen Steuerungsoptionen bereits zuvor konfiguriert wurden, behalten wir die praktische Wirkung der bisherigen Auswahl unter den neuen Definitionen bei. Frühere Training-Einstellungen auf „Block“ oder „Block on pages with ads“ werden auf „Disallow AI Training“ migriert.

### Empfehlungen für neue Domains

Ab dem 15. September wird Kunden beim Hinzufügen einer neuen Domain je nach Geschäftsmodell eine von zwei vorkonfigurierten Einstellungen angeboten – abhängig davon, ob die Website Einnahmen durch Werbung erzielt. Werbeeinnahmen setzen voraus, dass ein Mensch die Seite tatsächlich sieht. KI-Training ersetzt diesen Besuch durch eine Antwort; Agenten rufen die Seite ab, ohne dass jemand die Werbung sieht. Daher sind die Voreinstellungen für werbefinanzierte Websites restriktiver. Sie können jede dieser Einstellungen während des Onboardings oder jederzeit danach ändern.

_Empfohlene Einstellungen für neue Domains_

## Was bedeutet dies für bestimmte Mixed-Use Crawler?

Applebot, Bingbot und Googlebot sind als „Accountable“ eingestuft. Apple, Google und Microsoft haben sich denselben Grundsätzen hinsichtlich Wahlfreiheit für Publisher und Transparenz verpflichtet. Mit „Disallow AI Training“ können sie Ihre Website weiterhin für Suchzwecke crawlen. Wenn Sie „Block“ auswählen, werden sie vollständig blockiert.

Wir stufen auch die relevanten Crawler von Amazon, Anthropic, Meta und OpenAI als „Accountable“ ein. Diese Unternehmen verwenden getrennte Crawler für Suche und Training, sodass Cloudflare den Trainings-Crawler blockieren kann, ohne die Suche zu beeinträchtigen.

### Applebot

Mit Applebot können Websitebetreiber dem KI-Training widersprechen, indem sie in robots.txt für „Applebot-Extended“ eine Disallow-Regel hinzufügen. Präferenzen für KI-Zusammenfassungen können Websitebetreiber derzeit außerdem über die nosnippet-[Direktive](https://support.apple.com/en-us/119829#:~:text=nosnippet%3A%20Applebot,products%20and%20services.) im HTML-Code der Seite festlegen. Inhalte können zudem als [Paywall-Inhalte](https://support.apple.com/en-us/119829#:~:text=Marking%20paywalled%20content,the%20next%20section.) gekennzeichnet werden, um sie von generativen Ausgaben auszuschließen. Applebot bietet bislang noch kein Tool zur Überprüfung auf URL-Ebene. Wir haben uns jedoch mit dem Apple-Team ausgetauscht, das uns Einzelheiten zu einer derzeit entwickelten Lösung für das kommende Jahr mitgeteilt hat. Apple hat außerdem erklärt, dass ein Ausschluss vom Training[ keine Auswirkungen auf das Suchranking](https://support.apple.com/en-us/119829#:~:text=Applebot%2DExtended%20and%20controlling%20data%20usage) hat.

### Googlebot

Googlebot ermöglicht Websitebetreibern ein Opt-out vom Training, indem sie für „Google-Extended“ eine Disallow-Regel in robots.txt hinterlegen. Außerdem bietet Google in seinem Webmaster-Portal eine Umschaltoption, mit der sich Websiteinhalte von generativen Suchergebnissen ausschließen lassen. Darüber hinaus stellt Googlebot Kennzahlen und Berichte zu klassischen Suchergebnissen und KI-Zusammenfassungen bereit. Google hat Einzelheiten zu seinen bereits vorhandenen und kürzlich gestarteten Kontrollmechanismen sowie zu derzeit in Entwicklung befindlichen Funktionen geteilt, darunter zusätzliche Transparenz-Tools auf URL-Ebene für Google-Extended, die in den kommenden Wochen verfügbar werden sollen. Google hat außerdem angegeben, dass ein Ausschluss von Google-Extended [das Suchranking nicht beeinflusst](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers#google-extended:~:text=Google%2DExtended%20does%20not%20impact%20a%20site%27s%20inclusion%20in%20Google%20Search%20nor%20is%20it%20used%20as%20a%20ranking%20signal%20in%20Google%20Search.).

### Bingbot

Bingbot bietet in den [Webmaster Tools](https://www.bing.com/webmasters/help/ai-performance-9f8e7d6c) fein abstimmbare Steuerungsmöglichkeiten und Transparenz. Websitebetreiber können ihre Präferenzen für KI-Training derzeit über Bings `NOARCHIVE`-[Meta-Tag](https://blogs.bing.com/webmaster/september-2023/Announcing-new-options-for-webmasters-to-control-usage-of-their-content-in-Bing-Chat#:~:text=Content%20tagged%20NOARCHIVE%20will%20not%20be%20included%20in%20Bing%20Chat%20answers%2C%20not%20be%20linked%20to%20in%20the%20answers.%20Going%20forward%2C%20for%20content%20in%20our%20Bing%20Index%20that%20is%20labeled%20NOARCHIVE%2C%20we%20will%20not%20use%20the%20content%20for%20training%20Microsoft%E2%80%99s%20generative%20AI%20foundation%20models.) ausdrücken. Microsoft erweitert diese Funktionen und entwickelt derzeit einen Mechanismus, der künftig auch eine „No Training“-Präferenz in robots.txt auf Domain-/Website-Ebene berücksichtigt; die Einführung ist für Anfang 2027 vorgesehen. Cloudflare-Kunden, die das Training durch Bing bereits heute ablehnen möchten, können zusätzlich zum `NOARCHIVE`-Tag das Tool [Block URLs or Content Removal](https://www.bing.com/webmasters/help/block-urls-from-bing-264e560a) verwenden. Microsoft hat außerdem erklärt, dass die Verwendung von `NOARCHIVE` [keine Auswirkungen auf das Suchranking](https://blogs.bing.com/webmaster/september-2023/Announcing-new-options-for-webmasters-to-control-usage-of-their-content-in-Bing-Chat#:~:text=We%20also%20heard%20from%20publishers%20that%20they%20want%20to%20exercise%20these%20choices%20without%20impacting%20how%20Bing%20users%20can%20discover%20web%20content%20on%20Bing%E2%80%99s%20search%20results%20page.%20We%20can%20assure%20publishers%20that%20content%20with%20the%20NOCACHE%20tag%20or%20NOARCHIVE%20tag%20will%20still%20appear%20in%20our%20search%20results.) hat.

Bis diese Unterstützung verfügbar ist, wird die Auswahl von „Disallow AI Training“ Bing über robots.txt nicht automatisch eine „No Training“-Präferenz übermitteln. In der Praxis entspricht dies dem bisherigen Verhalten der Einstellung „Training Block“, die nicht für Mixed-Use-Crawler wie Bingbot galt.

### Fortschritte fortsetzen

Wir werden weiterhin den direkten Austausch mit allen Betreibern von KI-Crawlern suchen, während sich diese Funktionen weiterentwickeln. Cloudflare [Radar](https://radar.cloudflare.com/ai-insights#ai-bot-transparency) verfolgt öffentlich, welche Steuerungsmöglichkeiten, Transparenzfunktionen und Berichte von den Betreibern der als ‚Accountable‘ eingestuften Crawler bereitgestellt werden. 

Ein besseres Internet erfordert Entscheidungsfreiheit auf beiden Seiten: Crawler brauchen Zugang zum offenen Web, während die Menschen, die dieses Web gestalten, wirksame Kontrolle darüber haben müssen, wie ihre Arbeit verwendet wird. Die heutige Ankündigung stellt einen konkreten Schritt hin zu diesem Gleichgewicht dar.

Fortschritt erfordert, dass Infrastrukturanbieter, Content-Ersteller, Technologieunternehmen und Standardisierungsgremien wie die Internet Engineering Task Force (IETF) zusammenarbeiten, um diese Grundsätze in offene, interoperable Standards zu überführen.

## Der nächste Schritt: KI-Zusammenfassungen

KI-Training und KI-Zusammenfassungen werfen für Websitebetreiber unterschiedliche Fragen auf. Beim Training geht es darum, ob Inhalte zum Aufbau von KI-Modellen verwendet werden dürfen. Zusammenfassungen beeinflussen dagegen, wie Menschen ein Unternehmen entdecken, bewerten und letztlich besuchen. Beides ist relevant, wirkt sich jedoch auf unterschiedliche Weise auf Unternehmen aus.

Steuerungsmöglichkeiten, mit denen sich KI-Zusammenfassungen ablehnen lassen, sind der erste Schritt. Die als „Accountable“ eingestuften Betreiber bieten diese Möglichkeit bereits an oder schließen die entsprechenden Arbeiten derzeit ab. Damit wird eine wichtige Grundlage geschaffen: Websitebetreiber können Nein sagen.

Eine websiteweite Entscheidung zwischen dem Zulassen und dem Verbot von Zusammenfassungen bleibt jedoch ein zu grobes Instrument. Die richtige Entscheidung hängt von der Website, den Inhalten und dem geschäftlichen Ergebnis ab. Für Publisher wirft KI-Training grundlegende Fragen zu Kontrolle, Vergütung und der langfristigen Tragfähigkeit originärer Inhalte auf. Zusammenfassungen werfen dagegen eine separate und häufig unmittelbarere Frage der Distribution auf: Besucht jemand die Website des Publishers oder konsumiert die Antwort direkt innerhalb einer Such- oder KI-Anwendung? Für viele andere Unternehmen stehen KI-Zusammenfassungen zunehmend zwischen einem potenziellen Kunden und einer Website. Sie können eine Frage beantworten, Alternativen vergleichen, ein Produkt empfehlen oder jemandem bei der Entscheidung helfen, ob er die Website überhaupt besucht

Die Daten zeigen ein gemischtes Bild. [Mehr als die Hälfte](https://www.pewresearch.org/chart/a-majority-of-americans-say-they-read-ai-summaries-at-the-top-of-search-results/) der Verbraucher liest Zusammenfassungen in der Suche, und diese Verbraucher [beenden ihre Suche](https://www.bain.com/insights/goodbye-clicks-hello-ai-zero-click-search-redefines-marketing/) nach dem Lesen einer solchen Zusammenfassung mit einer [um über 40 % höheren Wahrscheinlichkeit](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/) direkt danach. Dadurch kann die Zahl der Besuche auf einer Website sinken. Verbraucher, die über KI-Suche auf eine Website gelangen, konvertieren jedoch mit einer Rate, die zwischen [dem Dreifachen ](https://aisearch.similarweb.com/blog/ai-visibility-roi/)und mehr als [dem Fünffachen](https://quickseo.ai/blog/ai-search-vs-google-search-in-2026-40-stats-that-show-why-your-brand-needs-to-track-both#:~:text=AI%20search%20traffic%20converts%20at%2014.2%25%2C%20compared%20to%20Google%E2%80%99s%202.8%25) der Rate von Nutzern liegt, die über die klassische Suche kommen. KI kann also weniger Besuche erzeugen, dafür aber Kunden mit deutlich höherer Kauf- oder Handlungsabsicht vermitteln.

Das ist nicht grundsätzlich gut oder schlecht. Ein durch Werbung finanzierter Publisher kann darauf optimieren, möglichst viele Besucher zu erreichen. Ein Händler bevorzugt möglicherweise weniger Besucher, die dafür mit höherer Wahrscheinlichkeit einen Kauf tätigen. Die Aufgabe von Cloudflare besteht nicht darin, diese Entscheidung für sie zu treffen, sondern ihnen die nötige Transparenz und Kontrolle zu geben, um selbst eine fundierte Entscheidung treffen zu können.

Opt-outs für Zusammenfassungen sind ein guter Anfang, aber noch nicht die endgültige Lösung. Unser nächster Schwerpunkt liegt darauf, Websitebetreibern zu helfen, die Auswirkungen von Zusammenfassungen auf ihr Geschäft besser zu verstehen und ihnen mehr Kontrolle darüber zu geben, in welchem Umfang ihre Inhalte genutzt werden können. Offene Standards wie [ai-prefs](https://datatracker.ietf.org/wg/aipref/documents/) werden dafür von großer Bedeutung sein.

Wenn Sie sich an dieser Diskussion beteiligen oder Feedback geben möchten, wenden Sie sich bitte an [crawlercontrols@cloudflare.com](mailto:crawlercontrols@cloudflare.com).

Diese neuen Steuerungsmöglichkeiten stehen allen Kunden in allen Tarifen zur Verfügung und können in den [Sicherheitseinstellungen](https://dash.cloudflare.com/?to=/:account/:zone/security/settings) der Domain (Zone) konfiguriert werden. Sie nutzen Cloudflare noch nicht? [Kostenlos starten](https://www.cloudflare.com/lp/pg-one-platform/), um heute die gewünschten Traffic-Kontrollen einzurichten.

]]>01M2S4KSCE8V9DNH0WHVPRJB5PLesbar, auffindbar, aufrufbar und zahlungstauglich: Aufbau eines offenen agentenfähigen Internetshttps://blog.cloudflare.com/de-de/the-agentic-internet/ Mon, 17 Aug 2026 03:45:51 GMTAgenten sind eine neue Art von Website-Besucher. Sie rendern kein CSS und klicken auch nicht auf Anzeigen, aber am anderen Ende befindet sich ein zahlender Mensch. Wenn Sie ihnen also den Zugriff verwehren, sperren Sie damit auch Ihre Kunden aus. Deshalb entwickeln wir offene Tools und Protokolle, mit deren Hilfe Urheber und Agenten konfliktfrei interagieren können.AgentsAgents WeekAIEntwicklerEntwicklerplattformMCPUnsere Erhebungen zeigen, dass bei viel Traffic von gutartigen Bots [​Seiten erneut abgerufen werden, die sich nicht geändert haben](https://blog.cloudflare.com/making-ai-search-smarter/). Das gilt für Milliarden von Anfragen und bedeutet einen enormen maschinellem Aufwand, der keinerlei Nutzen hat. Es handelt sich dabei um das Symptom eines Webs, das für Menschen geschaffen wurde, nun aber von etwas anderem genutzt wird.

Agenten sind inzwischen Realität – nicht als neue Art von Software, sondern als neuer Typ von Webseitenbesucher.

Das Web, das rund um diese neuen Besucher umgestaltet wird, bezeichnet man als agentenfähiges Internet. Aus unserer Sicht besteht seine Zukunft in Lesbarkeit, Auffindbarkeit, Aufrufbarkeit und Bezahltauglichkeit. Dafür werden aber spezielle Werkzeuge und Protokolle benötigt.

Die Entwicklerplattform von Cloudflare bietet einen Ort, an dem Agenten betrieben werden können, und die ersten Tools für ihre Entwicklung. Was bislang fehlt, sind Werkzeuge, mit deren Hilfe Agenten und Domaininhaber kooperieren können, anstatt in Konflikt miteinander zu geraten – und zwar nicht nur innerhalb derselben Plattform, sondern auch im offenen Internet.

Bisher hat sich jeder Browser im Web mit einem Header namens User-Agent identifiziert. Der Name ergab nur dann Sinn, wenn Sie sich bewusst machten, dass der Browser in Ihrem Auftrag handelte. Doch jetzt ist ein User Agent ein echter Agent des Benutzers, also ein Programm, das im Auftrag eines Menschen im Web etwas abruft. Seine ausgereifteste Form sind aktuell Programmieragenten. Diese lesen und schreiben Quellcode, rufen die benötigten Referenzdokumente ab und sehen nie, wie die von ihnen gelesenen Seiten eigentlich aussehen.

Ein Agent rendert Ihr CSS nicht, sieht Ihr Hero Image nicht und klickt nicht auf Ihre Anzeigen. Doch am anderen Ende befindet sich trotzdem ein zahlender Mensch. Jede Anfrage hat einen Zweck und kostet jetzt jemanden Geld. Wenn Sie sie blockieren, sperren Sie gleichzeitig auch Ihre Kunden aus. Das heißt: Wenn Sie sie wie Scraping-Bots behandeln, verlieren Sie diese Kunden.

Jeder Agent wird tätig, weil jemand – also eine Person oder ein Unternehmen – für diese Tätigkeit bezahlt. In der Regel gibt man nicht einfach aus Spaß Geld für Token aus. Diese Version des Webs, bei der jede Anfrage ein Ergebnis hat und auf einer Abrechnung erscheint, wird keinerlei Ähnlichkeit mehr mit dem heutigen Internet haben.

Letzteres wurde ebenso wenig für die aktuellen Gegebenheiten geschaffen wie die vorhandenen Analysewerkzeuge und die meisten Geschäftsmodelle. Wie Agenten Dinge lesen, entdecken, abrufen und bezahlen, wird darüber entscheiden, ob das Internet weiterhin offen ist oder sich abschottet. In einer Version der Zukunft stehen für die Entdeckung, Identitätskontrolle und Zahlung nur einige wenige Anbieter zur Verfügung. In einer anderen bleibt das Internet für alle frei zugänglich: Auf allgemein implementierbaren Standards beruhende Grundelemente werden auf einer neutralen Infrastruktur mit öffentlichem Quellcode betrieben.

Cloudflare glaubt an das offene Internet und wir sind in der Position, eine Zukunft mitzugestalten, in der es sich weiter entfalten kann.

Wir setzen auf offene Standards wie x402, MCP, Web Bot Auth und PACT, die von jedem implementiert werden können. Domaininhaber entscheiden selbst, welche Identitätsanbieter, Zahlungsabwickler und Agenten-Dienste sie nutzen wollen. Cloudflare ist nur eine Option, mit der man sich nicht an einen vollständigen Stack kettet. Wir nutzen die gleiche Infrastruktur wie unsere Kunden (Stichwort „Customer Zero“), ohne bevorzugten Pfad oder Früzugangs-API, die nur uns offensteht. Wir wollen die Aufgabe, die wir fünfzehn Jahre lang für das auf den Menschen ausgerichtete Internet erfüllt haben, nun auch für das agentenfähige Web übernehmen.

Die zugrundeliegende Technik ist nicht das, was die menschlichen Benutzer im agentenorientierten Internet wahrnehmen werden. Sie verwenden ein neues Medium und werden es – wie seinerzeit das Web – danach beurteilen, ob es für sie eine Verbesserung bringt. Entscheidend wird sein, ob sich eine Tischreservierung im Restaurant in einem Arbeitsschritt erledigen lässt oder ob es dafür mehrere braucht. Ob sie wissen, mit wem sie es zu tun haben. Ob Ihnen das Bezahlen als sicher erscheint.

## **Unser Ziel: Ein lesbares, auffindbares, aufrufbares und zahlungstaugliches Internet für Agenten**

Ausgangspunkt ist die Identität. Mit[ Web Bot Auth](https://blog.cloudflare.com/web-bot-auth/) kann sich ein Bot kryptografisch bei jeder besuchten Website identifizieren, sodass deren Betreiber selbst entscheiden kann, wer Zutritt erhält und wer nicht. Damit haben Ratespiele und gefälschte User Agents ein Ende. Viele Websites ist die hinter einer Anfrage stehende Person durch das Login, ihr Verhalten innerhalb der App oder die Kaufhistorie bereits bekannt. Eine Website kann in diesem Fall [ Private Access Control Token](https://cloudflare.net/news/news-details/2026/Cloudflare-Collaborates-With-Leading-Browsers-to-Develop-a-Privacy-First-Protocol-For-the-Global-Internet/default.aspx) (PACT) ausgeben. Dieses Konzept wurde von Mozilla, Google, Microsoft und Shopify vorgestellt. Damit können Websites anonym für einen Nutzer „bürgen“. Der betreffende Agent kann den dort ausgestellten Token also an anderer Stelle als Nachweis der Vertrauenswürdigkeit präsentieren. Damit werden die Reibungsverluste für legitime Agenten reduziert.

Das macht es einem Agenten leichter, seine Aufgabe zu erfüllen. Mit [​Markdown for Agents](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/) benötigen Agenten weniger Token und eine geringere Bandbreite zum Lesen von Websites.[ WebMCP](https://blog.cloudflare.com/webmcp/) bietet ihnen eine native Möglichkeit für Interaktionen im Auftrag des Benutzers. Standards wie[ x402](https://x402.org/) erlauben es ihnen, Händler direkt zu bezahlen.

Die **Lesbarkeit** wird auf unkomplizierte Weise gewährleistet. Können KI-Agenten Inhalte in einer Weise lesen, die ihrer Funktionsweise und ihren Stärken entgegenkommt? Je weniger Bandbreite und Token ein Agent verbraucht, desto besser. Gerenderte HTML-Tags, die nie von einem Menschen angesehen werden, verschwenden nicht nur Rechenressourcen, sondern nehmen auch unnötig Platz im Kontextfenster ein. Der Agent muss dann dafür bezahlen, dass sie ignoriert werden. [​Markdown for Agents](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/) löst dieses Problem serverseitig.

Was die Client-Seite betrifft, haben wir einen neuen Browser entwickelt, der Agenten als vollwertige Akteure betrachtet: [​Kitesurf](http://blog.cloudflare.com/kitesurf) ist so schlank, dass er auf Workers läuft, bei jeder Anfrage gestartet und anschließend direkt wieder beendet werden kann. Er stellt die von Agenten benötigten Inhalte und Funktionen ohne die Features bereit, die auf den Menschen ausgerichtet sind, für Agenten aber nur unnötigen Ballast darstellen.

**Auffindbarkeit** ist die Grundvoraussetzung einer wirtschaftlichen Nutzung des für Agenten optimierten Internets. Bevor ein Agent eine Ressource lesen, ein Tool aufrufen oder für eine Transaktion bezahlen kann, muss er von der Existenz der Ressource überhaupt erst einmal wissen. Ein wichtiger Aspekt dabei ist die Suche. Um das Gesuchte zu finden, brauchen Agenten speziell für sie geschaffene Schnittstellen – kein Feld, in das ein langsam tippender Mensch Stichwörter eingibt. Dafür ist jetzt das Tool [​AI Search](https://developers.cloudflare.com/ai-search/) verfügbar, mit dem jede öffentliche Website von Agenten durchsucht werden kann.

Die Auffindbarkeit ist der zweite wichtige Aspekt. Urheber von Inhalten und API-Betreiber müssen wissen, wie gut sichtbar sie für Agenten sind. [​Agent Engine Optimization (AEO)](http://blog.cloudflare.com/aeo) misst die Sichtbarkeit von Marken für die verschiedenen wichtigen Modelle und Agenten. Wenn Sie für die von Ihren Kunden verwendeten Agenten keine messbare Sichtbarkeit haben, ist das im Grunde so, als wären Sie im Internet gar nicht präsent. 

Die **Aufrufbarkeit** ist der Punkt, an dem die eigentlich Agenten-Tätigkeit beginnt und sie beispielsweise einen Tisch reservieren, ein Abonnement verlängern oder einen Bericht abrufen. Im herkömmlichen Web muss sich der Mensch zur Erledigung dieser Aufgaben durch unterschiedliche Benutzeroberflächen klicken. Wenn ein Agent dort z. B. einen Punkt auf eine To-Do-Liste setzen will, muss er erst den HTML-Code parsen, dann erraten, welches die Schaltfläche für „Hinzufügen“ ist, und schließlich einen Klick simulieren und hoffen, dass sich das DOM (Document Object Model) seit seinem letzten Besuch nicht geändert hat.

Mit [WebMCP](https://blog.cloudflare.com/webmcp/) kann eine Website die auf ihr ausführbaren Aktionen den Agenten direkt über den Browser zugänglich zu machen:

Der „Vertrag“ zwischen Tools wird damit explizit gemacht. HTML-Parsing und Rätselraten bei Formularfeldern fallen weg. Da die Tools innerhalb der Seite ausgeführt werden, nutzen sie die bestehende Sitzung und den Status des Benutzers weiter. [​Code Mode](https://blog.cloudflare.com/code-mode/) geht noch einen Schritt weiter. Weil Agenten in Programmcode denken, können sie Tools schneller aufrufen und zielgenauer nutzen, indem sie Quellcode schreiben. Sie lesen keine Inhalte von Websites aus, sondern rufen Endpunkte auf. Somit verrät ein eindeutiges Signal dem Urheber, welche seiner Inhalte tatsächlich verwendet werden. 

Unserer Ansicht nach wird der Trend im agentenfähigen Internet zur **Bezahlbarkeit** gehen. Für jede geschäftliche Transaktion benötigt man letztendlich eine Zahlungsmöglichkeit. Anzeigenbasierte Monetarisierungsmodelle greifen immer seltener und Lizenzmodelle auf Grundlage der Benutzerzahl funktionieren nicht, wenn es sich bei dem Benutzer um ein Computerprogramm handelt. Den Anbietern der von uns allen genutzten Inhalte bricht die Einnahmequelle weg, wenn niemand mehr ihre Websites ansieht und die bei ihnen geschalteten Werbeanzeigen von den Browsern nicht mehr ausgespielt werden. 

Eine Website für Kochrezepte, die mit Werbeanzeigen nie profitabel war, kann einen Bruchteil eines Cents pro Abruf berechnen und im agentenfähigen Internet Gewinn abwerfen. Eine Lokalzeitung kann Artikel zum Zeitpunkt des Lesens ohne Lizenzvertrag oder Login lizenzieren. Auf der Gegenseite befindet sich ein Agent mit einem von seinem Schöpfer im Vorfeld festgelegten Budget. 

Bei jeder Zahlungsinteraktion wird ein Nachweis erzeugt. Der Urheber der betreffenden Inhalte kann damit belegen, welcher Agent welche Seite abgerufen hat. Der Agent wiederum kann nachweisen, dass er für das Genutzte bezahlt hat. Mit [​Wallets](https://blog.cloudflare.com/wallets/) können Agenten ganz einfach für Inhalte und API bezahlen und [​Monetization Gateway](https://blog.cloudflare.com/monetization-gateway/) ermöglicht Domaininhabern die Einrichtung von Agenten-Zahlungen mit wenigen Klicks.

Es liegt in der Natur unserer Tätigkeit, dass sich Cloudflare bei all diesen Abläufen mittendrin befindet. Wir sind schon jetzt zwischen Milliarden von Menschen und den von ihnen besuchten Websites angesiedelt, schützen sie, beschleunigen sie und sorgen dafür, dass sie online bleiben. Durch Agenten verändert sich zwar der Traffic, doch nicht unsere eigentliche Rolle: Wir fungieren als neutrale und leistungsstarke Zwischeninstanz, bei der sich Urheber, Händler, Agentenentwickler und Endbenutzer sicher sein können, dass wir auf ihrer Seite sind und ihnen keine Konkurrenz machen. 

Wir möchten Domaininhabern die Werkzeuge an die Hand geben, mit denen sie selbst bestimmen können, welche KI-Agenten sie unterstützen und zulassen und welche sie [​blockieren](https://blog.cloudflare.com/cloudflare-ai-audit-control-ai-content-crawlers/). Als Anbieter eines Entwicklertools strebt man wahrscheinlich [​Agentenfähigkeit](http://blog.cloudflare.com/aeo) an, damit die eigene Lösung bestenfalls von KI-Agenten entdeckt, empfohlen und gekauft werden kann. Ein Verlag möchte unter Umständen KI-Agenten blockieren, die ohne Gegenleistung Inhalte auslesen und Ressourcen beanspruchen, und solche zulassen, die seine Inhalte lizenzieren oder ihn dafür vergüten. Ein gemeinnütziger Datenanbieter will möglicherweise Bots oder Personen blockieren, die bestimmte Durchsatzgrenzen überschreiten, ihnen aber die Möglichkeit zu einer Entsperrung gegen Bezahlung bieten, um der übermäßigen Ressourcennutzung Rechnung zu tragen.

## **Bots sind tot, es leben die Bots**

Inzwischen lassen sich [​Bots und Menschen nicht mehr ohne Weiteres voneinander unterscheiden](https://blog.cloudflare.com/past-bots-and-humans/). Man kann nicht mehr pauschal behaupten, dass Bots schlecht und Menschen gut sind, oder dass Bots Ressourcen verschwenden, die eigentlich von Menschen genutzt werden sollten. Eine solche Denkweise ist im heutigen Agenten-Zeitalter überholt.

Wir betrachten Agenten als eine neue Art von Akteur. Ihr Handeln kann erwünscht sein, etwa wenn sie Inhalte auf ressourcenschonende Weise lesen, auf die von Domaininhabern vorgesehene Weise mit Websites interagieren und für das von ihnen Genutzte zahlen. Wenn sie aber zum Beispiel Millionen von Seiten ohne Entschädigung auslesen, versuchen, Sperrungen zu umgehen, oder [​robots.txt](https://www.cloudflare.com/learning/bots/what-is-robots-txt/)-Dateien ignorieren, sind sie unerwünscht. Wir glauben, dass diese unerwünschten Aktivitäten in vielen Fällen abnehmen und sich sogar in wünschenswerte Tätigkeiten verwandeln werden, wenn Menschen und Bots erst mit den richtigen Werkzeugen ausgestattet sind.

## **Schließen der Umsatzlücke**

Cloudflare hat jahrelang Bots aufgespürt und Domaininhabern dadurch ermöglicht, selbst darüber zu entscheiden, ob diese Programme auf ihre Inhalte zugreifen dürfen. Was bislang nicht abgedeckt wurde, ist der zweite Aspekt: die Art und Weise, in der Agenten nach ihrer Freigabe mit diesen Websites interagieren. Dafür ist diese Serie von Agenten-Tools gedacht: das Web lesbar, auffindbar, aufrufbar und bezahltauglich zu machen. Diese vier Grundbausteine beruhen alle auf offenen Standards, sodass sich die Infrastruktur nicht im Besitz eines einzelnen Unternehmen befindet. 

Ein offenes, agentenfähiges Internet braucht Vielfalt auf beiden Seiten: nicht nur bei Verlagen und Urhebern von Inhalten, sondern auch bei den Agenten. Wenn auf Nachfrageseite eine Vereinheitlichung stattfindet, spielt es keine Rolle, wie offen die Angebotsseite ausgestaltet ist. Das Internet ist dann trotzdem abgeschottet.

Wir arbeiten an einer offenen Alternative. Schließen Sie sich uns an: Machen Sie Ihre Website [​mit unserem neuen Dashboard agentenfähig](http://blog.cloudflare.com/aeo) und registrieren Sie sich, um Neuigkeiten zu unserem Answer Engine Optimization (AEO)-Produkt zu erfahren. Wenn Sie eine Website oder einen Agenten betreiben, können Sie in unserem [​KI Playground](https://playground.ai.cloudflare.com/) mit allen neuen Technologien des Internets experimentieren.

]]>01M06X01QHM5HQ3S1CSQ9ZZ6D6Cloudflare-Bericht zu DDoS-Bedrohungen im ersten Halbjahr 2026: Starke Zunahme von 1 Tbit/s-Angriffen im Zuge von DNS Floods und geopolitischen Spannungenhttps://blog.cloudflare.com/de-de/ddos-threat-report-2026-h1/ Fri, 14 Aug 2026 01:30:28 GMTIn der ersten Hälfte des Jahres 2026 wurde im Cloudflare-Netzwerk ein Anstieg der hypervolumetrischen DDoS-Angriffe um 519 Prozent verzeichnet. Dabei spielten die Angriffsvektoren DNS- und CLDAP-Reflection eine wichtige Rolle. In diesem Bericht wird erörtert, wie sich durch weitreichende geopolitische Konflikte die Cyberbedrohungslandschaft weltweit gewandelt hat.AngriffeCloudforce OneDDoSRadarThreat ReportWillkommen zur 25. Ausgabe des Cloudflare-Berichts zur DDoS-Bedrohungslandschaft. Erstmalig wird in dieser Serie ein Halbjahreszeitraum abgedeckt, denn wir haben unsere Beobachtungen aus dem ersten und zweiten Quartal 2026 in einem einzigen Bericht zusammengefasst. Unsere auf Bedrohungsdaten spezialisierte Sparte,[Cloudforce One](https://www.cloudflare.com/cloudforce-one/), hat die Entwicklung der Bedrohungslage durch [DDoS-Angriffe](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/) auf Grundlage von Daten aus dem [Cloudflare-Netzwerk](https://www.cloudflare.com/network/) eingehend analysiert.

## Wichtigste Erkenntnisse

  1. Das 1 Tbit/s-Segment ist gewachsen. Cloudflare hat in der ersten Hälfte des Jahres 2026 insgesamt 935 DDoS-Angriffe auf Netzwerkschicht mit mehr als 1 Tbit/s abgewehrt und hier einen Anstieg um 519 Prozent vom ersten auf das zweite Quartal verzeichnet. 
  2. Bei den Angriffsvektoren hat sich der Schwerpunkt von Botnetz-Floods zu Reflection und Amplification verlagert. DNS-basierte Angriffe machten im Berichtszeitraum 34,3 Prozent an den Aktivitäten auf Netzwerkschicht aus, wobei allein der Anteil von [DNS Floods](https://www.cloudflare.com/learning/ddos/dns-flood-ddos-attack/) an den Angriffen auf Netzwerkschicht von 25,7 Prozent im ersten auf 40,0 Prozent im zweiten Quartal zulegte. Bei [CLDAP Floods](https://blog.cloudflare.com/reflections-on-reflections/) wurde eine Steigerung um 580 Prozent im Quartalsvergleich registriert, wodurch dieser Angriffsvektor im zweiten Jahresviertel auf Platz drei kletterte.
  3. Geopolitik und Ereignisse mit globaler Tragweite beeinflussen die Bedrohungslandschaft. Auf das Segment Medien, Produktion und Verlage entfielen in beiden Quartalen 14,2 Prozent aller abgewehrten HTTP-DDoS-Anfragen, was diese Branche an die Spitze katapultierte. Das erklärte sich daraus, dass die Berichterstattung über den Iran, die Ukraine und die Fußball-Weltmeisterschaft anhaltende Aufmerksamkeit auf sich zog. Parallel dazu kletterte die Türkei auf Platz drei der am stärksten angegriffenen Länder, was im Kontext des NATO-Gipfels im Juli in Ankara zu betrachten war. Der staatliche Sektor schnellte während der Operation Epic Fury im Nahen Osten von Rang 29 auf Rang 9. Es handelte sich dabei um den bis dato größten Zuwachs in einem Sektor im laufenden Jahr.



## Das erste Halbjahr in Zahlen: 5.300 DDoS-Angriffe pro Stunde

Bereits zur Jahresmitte hat Cloudflare 23,2 Millionen Anfragen auf Netzwerkschicht und 29,64 Billionen HTTP-DDoS-Anfragen abgewehrt. Das entspricht ungefähr 5.343 DDoS-Attacken auf Netzwerkschicht pro Stunde bzw. etwa 128.000 pro Tag.

### Höhepunkt im April, Durchgreifen von Strafverfolgungsbehörden

Der April war im Berichtszeitraum für DDoS-Angriffe sowohl hinsichtlich der Aktivitäten als auch des Volumens ein Spitzenmonat, in dem ein Höchststand von 6,46 Billionen Anfragen bzw. 165 Petabyte (PB) verzeichnet wurde. Das ist eine enorme Menge an Datenverkehr und vergleichbar mit dem durch mehrjähriges kontinuierliches Streaming von 4K-Videos generierten Traffic oder in etwa mit der Datenmenge, die große Videoplattformen an einem Tag verarbeiten. Anschließend sanken die Zahl der Anfragen und das Volumen wieder, was möglicherweise der [Operation PowerOFF](https://www.europol.europa.eu/media-press/newsroom/news/europol-supported-global-operation-targets-over-75-000-users-engaged-in-ddos-attacks) zu verdanken ist. Im Rahmen dieser Aktion, die 21 Länder umfasste und sich gegen mehr als 75.000 Nutzer richtete, die DDoS-Angriffe in fremdem Auftrag durchführen, wurden 53 Domains abgeschaltet, 25 Durchsuchungsbefehle erlassen und vier Verhaftungen vorgenommen.

### Hypervolumetrische Angriffe um mehr als das Sechsfache gestiegen

Bereits in der früheren Berichterstattung von Radar hat sich gezeigt, dass die Kategorie der hypervolumetrischen DDoS-Angriffe – also Angriffe mit mehr als 1 Terabit pro Sekunde (Tbit/s), 1 Milliarde Pakete pro Sekunde oder 1 Million Anfragen pro Sekunde – im Wachsen begriffen ist. Das ist 2026 nicht anders. Cloudflare hat im zweiten Quartal 805 Angriffe auf Netzwerkschicht mit einem Volumen von über 1 Tbit/s abgewehrt, was einen Anstieg um mehr als das Sechsfache im Quartalsvergleich darstellte.

## Angriffsmerkmale: Klein und langsam

Trotz der Zunahme von hypervolumetrischen Attacken zeichneten sich die von Cloudflare in der ersten Jahreshälfte 2026 abgewehrten DDoS-Angriffe im Mittel weiterhin durch ihre Kürze und geringe Größe aus: 96,62 Prozent der Angriffe auf Netzwerkschicht lagen unter 500 Mbit/s und 90,60 Prozent dauerten weniger als 10 Minuten. Allerdings ist „klein“ ein relativer Begriff. Die meisten Internetpräsenzen könnten selbst solch eher bescheidenen Angriffen nicht standhalten. Konkret bedeutet das:

  * Ein Angriff mit 100 Mbit/s reicht aus, um einen Server oder eine Website lahmzulegen
  * Ein Angriff mit 100 Gbit/s kann die meisten ungeschützten Rechenzentren ausschalten
  * Ein Angriff mit über 1 Tbit/s zählt zu den größten jemals verzeichneten Attacken und beansprucht selbst umfangreiche Internetinfrastruktur in erheblichem Maße



Angreifer nutzen manchmal unterschiedliche Kombinationen, also beispielsweise eine hohe Paketrate (maximale Zahl von Paketen pro Sekunde / Gpps) mit relativ geringer Bandbreite (Gbit/s) oder umgekehrt, um unterschiedliche Schwächen bei Netzwerkausrüstung oder alternativ Bandbreitenkapazität auszunutzen.

Darüber hinaus sind die meisten DDoS-Angriffe überraschend kurz, wie das folgende Diagramm zeigt. Selbst die größten hypervolumetrischen Angriffe dauern nicht Minuten, sondern Sekunden. So haben wir [Rekord-Angriffe mit einer Dauer von nur 35 Sekunden](https://blog.cloudflare.com/ddos-threat-report-for-2025-q1/#hyper-volumetric-attacks-continue-spill-into-q2) registriert. Ob ein Angriff nun 30 Sekunden oder zehn Minuten dauert: Das Zeitfenster ist in jedem Fall zu kurz für das Eingreifen eines Menschen. Wenn ein Sicherheitsanalysten eine Warnmeldung erhält, ist der Angriff schon abgeschlossen. Manuelle Abhilfemaßnahmen und Lösungen auf Abruf sind in dieser Situation einfach zu langsam. Doch während der Angriff selbst möglicherweise schnell wieder vorbei ist, kann er langwierige Folgen haben. Selbst ein kurzer Ausfall führt unter Umständen durch Kaskadeneffekte zu unzuverlässigem Routing, TCP-Neuübertragungen, Anwendungsunterbrechungen und einer Beeinträchtigung nachgelagerter Dienste. Die vollständige Behebung dieser Probleme kann Stunden oder Tage dauern und die betroffenen Dienste sind in dieser Zeit gar nicht oder nur eingeschränkt nutzbar. In diesem Bedrohungsumfeld ist automatischer, stets aktiver Schutz keine Annehmlichkeit, sondern eine Notwendigkeit.

## Am häufigsten angegriffene Branchen

### Operation Epic Fury und vermehrte Angriffe auf staatlichen Sektor

Am 28. Februar 2026 haben Israel und die Vereinigten Staaten mit Operation Epic Fury eine Reihe von Angriffen auf die Führung und Infrastruktur des Iran begonnen. Das DDoS-Umfeld reagierte innerhalb von 72 Stunden: [Sicherheitsforscher](https://thehackernews.com/2026/03/149-hacktivist-ddos-attacks-hit-110.html) verzeichneten 149 DDoS-Angriffe von Hacktivisten auf 110 Organisationen in 16 Ländern. Knapp 47,8 Prozent aller weltweit angegriffenen Organisationen gehörten dem staatlichen Sektor an.

Als in der öffentlichen Berichterstattung in dieser Zeit umfangreiche staatliche Angriffe dokumentiert wurden, stieg dieses Segment gemessen am Anteil der abgewehrten HTTP-DDoS-Anfragen um 20 Ränge auf, von Platz 29 im ersten Quartal auf Platz 9 im zweiten. Zwar gehörte der Bereich während dieses Zeitraums zum größten Teil nicht zu den Top 10, doch innerhalb des Branchenrankings verzeichnete er den stärksten Anstieg.

### Medienbranche am stärksten unter Beschuss

Im Kontext des Kriegsgeschehens im Iran und in der Ukraine sowie der Aufmerksamkeit rund um die Fußball-Weltmeisterschaft stand die Medien-, Produktions- und Verlagsbranche in beiden Quartalen am stärksten im Fokus der Angriffe. Auf dieses Segment entfielen 14,2 Prozent aller abgewehrten HTTP-DDoS-Anfragen. Der Anteil war damit fast viermal so hoch wie der des zweitplatzierten Sektors.

## Am häufigsten angegriffene Länder

Im ersten Halbjahr 2026 fanden sich unter den am stärkten angegriffenen Ländern im DDoS-Bedrohungskontext ein paar alte Bekannte, teilweise wurden die Karten aber auch neu gemischt. China erreichte Platz eins, nachdem sich im zweiten Quartal 22,4 Prozent aller HTTP-DDoS-Anfragen weltweit an die Volksrepublik gerichtet hatten. Auf Rang zwei folgten die Vereinigten Staaten (18,8 Prozent), die weiterhin große Anziehungskraft auf die Angreifer ausübten.

Die Türkei verzeichnete eine rapide Zunahme von Angriffen, sodass sich ihr Anteil am weltweiten Angriffsdatenverkehr mehr als verdoppelte. Im zweiten Quartal erreichte sie deshalb den dritten Platz. Der sprunghafte Anstieg erfolgte in der Zeit vor dem NATO-Gipfel in Ankara im Juni und Anfang Juli, als türkische Sicherheitskräfte [weitreichende Razzien](https://apnews.com/article/turkey-nato-summit-suspects-detained-864260d7cbe9ca73cd05115cd638ee93) in der türkischen Hauptstadt durchführten und mindestens 209 Personen festnahmen.

## Häufigste Angriffsursprungsländer

Von Brasilien gingen in der ersten Hälfte des Jahres 2026 14,9 Prozent aller DDoS-Anfragen weltweit aus, womit das Land die Vereinigten Staaten (13,4 Prozent) ablöste. Dies war einem drastischen Anstieg im zweiten Quartal geschuldet, in dem 21,4 Prozent des gesamten abgewehrten DDoS-Anfrage-Traffics seinen Ursprung in Brasilien hatte. Indonesien blieb in beiden Quartalen auf Platz drei und hat sich damit mehrere Quartale in Folge in den Top 3 gehalten.

## Angriffsvektoren

### DNS Floods überwiegen

Auf DNS-basierte Angriffe ([DNS Floods](https://www.cloudflare.com/learning/ddos/dns-flood-ddos-attack/) und [DNS Amplification](https://www.cloudflare.com/learning/ddos/dns-amplification-ddos-attack/)) sind im ersten Halbjahr 2026 34,3 Prozent der Attacken auf Netzwerkschicht entfallen. Es handelt sich dabei um zusammenhängende, aber unterschiedliche Methoden: Bei einem DNS-Flood-Angriff richtet ein Botnetz seine Anfragen direkt an die autoritativen DNS-Server des Opfers, um dessen Abfragekapazität durch schiere Masse zu überlasten. Dadurch ist das „Telefonbuch“ für diese Domain nicht mehr erreichbar, was zum Ausfall jedes darauf angewiesenen Diensts führt. Bei DNS Amplification werden dagegen kleine [gefälschte](https://www.cloudflare.com/learning/ddos/glossary/ip-spoofing/) Anfragen an offene [DNS-Auflösungsdienste](https://www.cloudflare.com/learning/dns/dns-server-types/) geschickt, die viel größere Datensätze an die gefälschte IP-Adresse des Opfers zurücksenden (was oft durch eine ANY-Abfrage erreicht wird). 

### CLDAP stark im Aufwind: Steigerung um 580 Prozent bei Amplification

Der Reflection- und Amplification-Vektor CLDAP Flood, der ungeschützte Active Directory LDAP-over-UDP-Endpunkte missbraucht, verzeichnete im zweiten Quartal einen Zuwachs von 580 Prozent und wurde damit in diesem Zeitraum zum drittstärksten Angriffsvektor. CLDAP ([Connectionless Lightweight Directory Access Protocol](https://datatracker.ietf.org/doc/html/rfc1798)) ist eine Variante von LDAP ([Lightweight Directory Access Protocol](https://datatracker.ietf.org/doc/html/rfc4511)) und wird zum Abfragen und Ändern von Verzeichnisdiensten benutzt, die über IP-Netzwerke ausgeführt werden. CLDAP ist verbindungslos und setzt UDP anstelle von TCP ein, was das Protokoll zwar schneller, aber auch weniger zuverlässig macht. Aufgrund der Entscheidung für UDP ist kein Handshake erforderlich. Das ermöglicht es Angreifern, die Ursprungs-IP-Adresse zu fälschen und dies als Reflection-Vektor zu nutzen. Bei CLDAP-Angriffen werden kleine gefälschte Anfragen an öffentlich erreichbare Domain-Controller über den UDP-Port 389 gesendet. Die Server schicken der gefälschten Quelle (dem Opfer) dann zehn- bis hundertmal größere Antworten als die ursprüngliche Anfrage und sorgen so für eine Überlastung des Zielrechners. 

## Stärkung der globalen Verteidigungsmaßnahmen und Unterstützung bei Verteidigung des Internets

Das Cloudflare-Netzwerk ist so aufgebaut, dass es dieser Zunahme von DDoS-Bedrohungen gewachsen ist. Jeder Dienst in unserem Netzwerk wird durch [kostenlosen, unbegrenzten DDoS-Schutz](https://www.cloudflare.com/ddos/) abgesichert, der [in jeder unserer mehr als 330 Städte weltweit](https://www.cloudflare.com/network/) läuft und sich auf eine Netzwerkkapazität von 500 Tbit/s stützen kann. Dabei geht es um Autonomie: Unsere Systeme sind in der Lage, Angriffe [ohne menschliches Eingreifen](https://developers.cloudflare.com/ddos-protection/about/) zu erkennen und abzufangen. Das müssen sie auch, weil mittlerweile regelmäßig – hunderte Male in einem Quartal – Angriffe mit mehr als 1 Tbit/s durchgeführt werden.

  


Um Hosting-Anbietern, Cloud-Computing-Plattformen und Internet-Service-Providern bei der Identifizierung und Entfernung missbräuchlicher IP-Adressen / Konten zu helfen, von denen diese Angriffe ausgehen, nutzen wir den einzigartigen Überblick von Cloudflare über DDoS-Angriffe für die Bereitstellung eines [kostenlosen Feeds zu DDoS-Botnetz-Bedrohungen für Service-Provider](https://developers.cloudflare.com/ddos-protection/botnet-threat-feed/). 

Mehr als 800 Netzwerke weltweit haben sich für diesen Feed registriert und die Community arbeitet zur Zerschlagung von Botnetz-Knoten eng zusammen.

## Über Cloudforce One

[Cloudforce One](https://www.cloudflare.com/cloudforce-one/) will das Internet schützen und nutzt zur Analyse von Bedrohungen und zu gezielten Gegenmaßnahmen Telemetriedaten aus dem globalen Netzwerk von Cloudflare, das etwa 20 Prozent des Internets schützt. So werden kritische Systeme von Millionen Unternehmen auf der ganzen Welt abgesichert.

]]>01KZYXXBJV2SVV298JSZ9CCK54Alles, was wir während der Agents Week vorgestellt habenhttps://blog.cloudflare.com/de-de/agents-week-review-august-2026/ Wed, 12 Aug 2026 07:43:53 GMTDie neueste Ausgabe unserer Agents Week ist abgeschlossen. Hier finden Sie noch einmal alle Ankündigungen im Überblick – von Wallets bis hin zu Radar.AgentsAgents WeekAICloudflare OneCloudflare WorkersEntwicklerEntwicklerplattformSASEZero TrustZu Beginn der Agents Week[ erklärte](https://blog.cloudflare.com/agents-week-welcome/) Rita, dass Agenten die nächste Entwicklungsstufe des Computing darstellen: nicht nur als neue Anwendung von KI, sondern auch als neue Klasse von Software, die prägt, wie Menschen mit Technologie und wie Software mit dem Internet interagiert. Im Laufe des[ vergangenen Jahres](https://www.cloudflare.com/innovation-week/ai-week-2025/updates/) haben wir untersucht, was dieser Wandel für Entwickler und Kunden bedeutet, die KI-native Anwendungen entwickeln, und welche Infrastruktur erforderlich ist, um diese zu unterstützen. Mit zunehmenden Fähigkeiten und wachsender Autonomie von Agenten gehen die Herausforderungen über die Modelle selbst hinaus – und betreffen Identität, Kommunikation, Orchestrierung, Speicher, Beobachtbarkeit und Sicherheit.

In der vergangenen Woche haben wir gezeigt, wie wir diese Komponenten auf der gesamten Cloudflare-Plattform zusammenführen, um ein agentenbasiertes Internet zu unterstützen. Jeden Tag haben wir neue Tools, Produkte und Ideen vorgestellt, die dazu beitragen, ein Internet zu gestalten, in dem Menschen und Agenten [ zusammenarbeiten, statt miteinander zu kollidieren](https://blog.cloudflare.com/the-agentic-internet/).

### **Montag, 3. August**

Am Montag standen die grundlegenden Bausteine für die Entwicklung und den Betrieb intelligenter, autonomer Anwendungen im Mittelpunkt – die Laufzeitumgebung und Infrastruktur, auf die Agenten angewiesen sind.

[Ihr Agent braucht einen Computer, keinen Container – wir stellen @cloudflare/computer vor](https://blog.cloudflare.com/de-de/cloudflare-computer/)| @cloudflare/computer führt eine neue, speziell für Agenten entwickelte Laufzeitumgebung ein, die je nach Aufgabe die passende Umgebung auswählen kann.  
---|---  
[Workers RPC funktioniert jetzt über Python und JavaScript hinweg](https://blog.cloudflare.com/python-workers-rpc/)| Python- und JavaScript-Worker können jetzt direkt miteinander kommunizieren, was Projekte mit mehreren Programmiersprachen vereinfacht.  
[Kleiner, schneller, sicherer: Kimi und GLM im großen Maßstab betreiben](https://blog.cloudflare.com/smaller-faster-safer-models/)| Erkunden, wie wir große Modelle effizienter bedienen, ohne Qualität, Zuverlässigkeit oder Sicherheit zu beeinträchtigen.  
[Einführung der Billable Usage API: Programmatische Kostentransparenz für Cloudflare](https://blog.cloudflare.com/de-de/billable-usage-api/)| Eine einfachere Möglichkeit, Nutzung und Kosten unserer Self-Service-Produkte zu verfolgen.   
[Cloudflare Workers und Container unterstützen jetzt eingehende TCP-Verbindungen und gRPC](https://blog.cloudflare.com/grpc-workers/)| Hosten Sie Voice-AI-Backends oder andere Echtzeit-Sprach-Agents mit Cloudflare Workers  
  
### **Dienstag, 4. August**

Am Dienstag wurde der Agent Development Lifecycle (ADLC) und die grundlegenden Bausteine vorgestellt, die agentenzentrierte Software vom Prototyp zur Produktion führen.

[Der Agent Development Lifecycle ist bei Cloudflare angekommen](https://blog.cloudflare.com/de-de/agent-development-lifecycle/)| Den SDLC (Software Development Lifecycle) durch den ADLC ablösen: unser Ansatz, Agenten vom Prototypen bis in die Produktion zu bringen, sowie die grundlegenden Bausteine für die nächste Generation von „Softwarefabriken“ („Software Factories“).  
---|---  
[Wir präsentieren: Cloudflare Agents](https://blog.cloudflare.com/agents-on-cloudflare/)| Erstellen Sie Agenten auf Cloudflare und beobachten Sie jede Ausführung in Echtzeit – inklusive Tracing, Replay und menschlicher Freigaben für Vorgänge in Produktionsumgebungen.  
[Ihr Agent kann nun Workers mit lokalem Tracing debuggen](https://blog.cloudflare.com/local-tracing/)| Verteilte Ablaufverfolgung (distributed tracing) kommt in die lokale Entwicklung und erleichtert es Agenten, Probleme zu identifizieren und zu beheben, bevor sie in die Produktion gelangen.  
[Wir präsentieren Cloudflare Wallets: eine programmierbare Geldbörse für das agentenbasierte Internet](https://blog.cloudflare.com/de-de/wallets/)| Wallets führen eine sichere Methode für Agenten ein, um Transaktionen als Teilnehmer der aufkommenden agentenbasierten Ökonomie durchzuführen.  
[Führen Sie CI/CD für Millionen von Repositories aus — auf Ihrer Plattform, auf Cloudflare](https://blog.cloudflare.com/ci-workflows/)| Programmierbares CI/CD: Pipelines werden als Code statt als Konfiguration geschrieben, ergänzt durch einen Agent, der Fehler behebt und die Korrektur zur Überprüfung bereitstellt.  
[Wie Cloudflare mithilfe von KI Engineering-Standards durchsetzt](https://blog.cloudflare.com/engineering-standards-enforcement/)| Wie wir KI-gestützte Automatisierung in unseren gesamten Entwicklungsworkflows einsetzen, um Codestandards und Prozesse aufeinander abzustimmen und unseren eigenen Softwarefabriken zu helfen, hochwertigen und konsistenten Code in großem Maßstab bereitzustellen.  
[Wie wir eine Softwarefabrik gebaut haben, um die Anzahl der GitHub-Issues von Astro auf null zu reduzieren](https://blog.cloudflare.com/astro-issue-triage/)| Automatisierung der Analyse, Kategorisierung und des Routings von Issues, um den Aufwand für die Softwarewartung zu minimieren und die Entwicklerproduktivität zu maximieren.  
  
### **Mittwoch, 5. August**

Am Mittwoch haben wir Zero Trust von Nutzern und Geräten auf Agenten selbst ausgeweitet und gezeigt, wie wir diesen Ansatz intern bei Cloudflare einsetzen.

[Das Agent Access Model (Modell für den Zugriff von Agenten)](https://blog.cloudflare.com/the-agent-access-model/)| Ein Rahmenwerk, wie Agenten im Namen von Nutzern sicher auf Ressourcen und Dienste zugreifen können – in einem Internet, das zunehmend von Agenten bevölkert wird.   
---|---  
[Wie wir bei Cloudflare die Arbeit mit Cloudflare OS neu überdenken](https://blog.cloudflare.com/how-we-use-ai-with-cloudflare-os/)| Wie wir KI in unser internes Betriebsmodell integriert haben, damit Teams intelligenter und schneller arbeiten können, ohne Abstriche bei Sicherheit oder Kontrolle zu machen.  
[Cloudflare OS: eine offene Plattform für Agenten, Anwendungen und Arbeit](https://blog.cloudflare.com/de-de/cloudflare-os/)| Wir haben die Plattform, die unsere Teams zum Entwickeln von Apps, Automatisieren von Aufgaben und sicheren Zugriff auf interne Systeme nutzen, als Open Source veröffentlicht.   
[Mit identitätsbezogener Analyse unerwünschtes KI-Verhalten erkennen](https://blog.cloudflare.com/de-de/identity-aware-ai-gateway/)| Weisen Sie KI-Aktivitäten realen Benutzern und Systemen zu, um Anomalien und Kosten-Spitzen einfacher zu erkennen.  
[WriteGuard: feinkörnige Steuerung für MCP-Server](https://blog.cloudflare.com/mcp-portal-writeguard-private-beta/)| Wir stellen Kunden dieselben Tools zur Verfügung, die wir selbst einsetzen, damit sie riskante Tool-Aufrufe besser kontrollieren und die Wahrscheinlichkeit unerwünschter Änderungen durch Agenten verringern können.  
  
### **Donnerstag, 6. August**

Am Donnerstag wurde das Agentic Internet (agentenbasiertes Internet) definiert und erläutert, wie Website-Besitzer, Verleger und Agenten gemeinsam ein Internet gestalten können, das Menschen und Agenten gleichermaßen zugutekommt.

[Lesbar, auffindbar, aufrufbar und bezahlbar: Aufbau eines offenen agentenbasierten Internets](https://blog.cloudflare.com/de-de/the-agentic-internet/)| Ein Modell für ein agentenbasiertes Internet, in dem Verlage die Kontrolle behalten, Agenten sinnvollen Zugriff auf die benötigten Inhalte erhalten und offene Protokolle Transaktionen zwischen beiden Seiten ermöglichen.  
---|---  
[Geben Sie jeder Website eine WebMCP-Schnittstelle](https://blog.cloudflare.com/webmcp/)| Eine Vorschau auf WebMCP, das einen neuen (und sehr einfachen) Ansatz bietet, um Websites und Web-Apps für Agenten auffindbar und nutzbar zu machen.  
[Vom Ranking zur Empfehlung: Machen Sie Ihre Website fit für das Zeitalter der KI-Agenten](https://blog.cloudflare.com/de-de/aeo/)| SEO-Praktiken werden zu AEO (Answer Engine Optimization) weiterentwickelt, um zu verbessern, wie Webinhalte von Agenten gefunden, verstanden und bereitgestellt werden.  
[Einführung von Kitesurf: dem agentenorientierten Browser, der in V8-Isolaten auf Cloudflare Workers läuft](https://blog.cloudflare.com/kitesurf/)| Ein speziell für Agenten entwickelter Browser, der pixelgenaue Darstellung gegen geringeren Speicher- und CPU-Verbrauch eintauscht.  
[MCP der nächsten Generation](https://blog.cloudflare.com/mcp-v2/)| MCP wurde grundlegend überarbeitet. MCPv2 stellt die nächste Entwicklungsstufe der MCP-Unterstützung dar und vereinfacht die Bereitstellung und Skalierung agentenzentrierter Apps.  
[Cloudflare AI Search: Geben Sie Ihren Agenten eine Suchmaschine für Ihre Daten](https://blog.cloudflare.com/ai-search-easier/)| AI Search verwandelt Ihre Dateien oder Ihre Website mit einem einzigen Befehl in eine Agent-fähige Suchmaschine.  
  
### **Freitag, 7. August**

Am Freitag richteten wir den Blick darauf, was tatsächlich passiert: was Agenten im Web wirklich machen, wo KI in Ihren Apps ausgeführt wird, wer zu den jeweiligen Ökosystemen beiträgt und welche neuen Tools zur Analyse von Internetdaten zur Verfügung stehen.

[Erwünschte und unerwünschte Verhaltensweisen im agentenbasierten Internet sichtbar machen](https://blog.cloudflare.com/de-de/good-and-bad-agentic-behaviors/)| Bots können hilfreich sein, Menschen können schädlich handeln. Daher basiert moderne Bot-Abwehr auf fortlaufender Vertrauensbewertung statt auf einmaligen Risikoentscheidungen.  
---|---  
[Die Zusammenführung von Workers AI und AI Gateway zu einer einheitlichen KI-Steuerungsebene](https://blog.cloudflare.com/workers-ai-gateway-unification/)| Ein Binding, eine Wallet, ein Dashboard für den Zugriff auf jedes KI-Modell – als Nächstes kommt Model-First Routing.  
[Wir stellen Cloudflare Ambassadors und Community Engineers vor – plus weitere 1 Mio. US-Dollar für Open Source](https://blog.cloudflare.com/community-program-refresh/)| Unsere neu aufgelegte Community-Initiative führt zwei neue Programme ein: Cloudflare Ambassadors für Community-Leader und Community Engineers für Maintainer von Open-Source-Projekten. Hinzu kommen weitere 1 Mio. US-Dollar an Open-Source-Förderung in den kommenden zwei Jahren.  
[Wir stellen Radar Researcher vor: ein KI-Tool zur Erforschung von Internet-Daten in natürlicher Sprache](https://blog.cloudflare.com/introducing-radar-researcher/)| Der KI-Rechercheassistent von Radar: Fragen in natürlicher Sprache stellen und interaktive Diagramme als Ergebnis erhalten.  
  
### **Die Agents Week ist vorbei, aber für uns geht es weiter**

Fünf Tage später nimmt die Antwort auf Ritas Frage „[Was braucht Ihr Agent von einer Agent Cloud?](https://blog.cloudflare.com/agents-week-welcome/)“ allmählich Gestalt an. Er braucht eine Ausführungsebene und grundlegende Bausteine, auf denen er ausgeführt werden kann, einen Entwicklungslebenszyklus, der sich zunehmend selbst schreibt, sicheren Zugriff für die Menschen und Agenten, die die Arbeit erledigen, ein agentenbasiertes Internet sowie die Menschen und Communitys, die dafür sorgen, dass all dies fest verankert bleibt. Es gibt noch viel, was vor uns liegt. Doch zunehmend zeichnet sich ab, wohin die Reise geht: zu einem Internet, das die Menschen, für die es ursprünglich geschaffen wurde, ebenso nativ unterstützt wie die Agentem, die heute in ihrem Namen handeln.

Damit ist unsere Arbeit noch nicht getan. Behalten Sie unseren[ Changelog](https://developers.cloudflare.com/changelog/) im Blick, um auf dem Laufenden zu bleiben. Wenn Sie gemeinsam mit uns an einem Teil dieser Zukunft arbeiten, möchten wir gerne von Ihnen hören! Besuchen Sie uns auf[ X](https://x.com/cloudflaredev) oder[ Discord](https://discord.com/invite/cloudflaredev).

]]>01KZTE8CXNG6A7GJGMQ6654N2WErwünschte und unerwünschte Verhaltensweisen im agentenbasierten Internet sichtbar machenhttps://blog.cloudflare.com/de-de/good-and-bad-agentic-behaviors/ Wed, 12 Aug 2026 06:38:56 GMTCloudflare entwickelt die Bot-Abwehr weiter: weg von punktuellen Risikobewertungen hin zu einer kontinuierlichen Vertrauensbewertung. Erfahren Sie, wie unsere Systeme – darunter BotBase und Precursor – neue erwünschte und unerwünschte Verhaltensweisen von Bots und Agents analysieren. Testen Sie außerdem unsere Precursor-Trace-Simulation und sehen Sie, wie Ihre eigenen Cursorbewegungen als menschlich oder als Bot-Verhalten eingestuft würden.AgentsAgents WeekAI Bots (DE)Bot-ManagementNetzwerk-ServicesIm Internet gibt es nicht nur eine Art von Datenverkehr. Lange galt in der Websicherheit die Faustregel: Bots sind schlecht, Menschen sind gut. Diese pauschale Sichtweise ist heute überholt. Menschen können betrügerische Absichten verfolgen, während Bots in verschiedenen Bereichen einen wichtigen Nutzen bieten. Betreiber von Websites wünschen sich sogar bewusst bestimmte automatisierte Zugriffe, damit das Internet funktioniert und Inhalte gefunden werden können.

Um die Sache noch weiter zu komplizieren, verschwimmt die Grenze zwischen „Mensch“ und „Bot“ immer mehr. Inzwischen gibt es eine Art „hybriden“ Datenverkehr, bei dem eine einzelne Sitzung zwischen menschlicher und agentenbasierter Interaktion wechselt – und wieder zurück. Ein Beispiel: Ein Nutzer stöbert in einem Onlineshop und übergibt anschließend den Bezahlvorgang an einen automatisierten Einkaufsassistenten.

Wie können Website-Betreiber also mit dieser Komplexität umgehen? Im Mittelpunkt steht die Beurteilung von **Verhaltensweisen**. Handelt es sich um missbräuchliches oder schädliches Verhalten? Welches Risiko geht davon aus, und kann diesem Besucher angesichts seiner Aktivitäten vertraut werden? Dafür reichen statische Momentaufnahmen nicht aus. Erforderlich ist eine kontinuierliche Analyse des Verhaltens, um das Vertrauen fundiert zu bewerten.

In diesem Beitrag geben wir einen Einblick in die Strategie des Web Integrity & Trust-Teams, das sich mit den Themen Bots und Betrug befasst. Wir zeigen, wie gute und schlechte Verhaltensmuster erkannt und analysiert werden und welche Werkzeuge Website-Betreibern dabei helfen, neue Herausforderungen im zunehmend agentenbasierten Internet zu meistern. Zudem teilen wir Erkenntnisse zum agentenbasierten Traffic seit dem Start von[ Precursor](https://blog.cloudflare.com/introducing-precursor/) sowie eine Simulation, mit der Sie nachvollziehen können, wie Ihre eigenen Cursorbewegungen als Mensch oder Bot bewertet würden. Außerdem erwarten Sie einige spannende Updates zu bevorstehenden Produkteinführungen.

## **Risiko und Vertrauen: eine Definition**

Sprechen wir über den Unterschied zwischen **Risiko** und **Vertrauen** , wie wir ihn bei Cloudflare im Bereich der Bot-Erkennung definieren. Häufig werden beide als Gegenpole auf einem Kontinuum verstanden. Wir betrachten sie dagegen als unabhängige, sich gegenseitig beeinflussende Größen. Vertrauen ist dabei die entscheidende Voraussetzung, um fundiert darüber entscheiden zu können, wie mit dem jeweiligen Traffic verfahren werden sollte. 

Risiko beschreibt, wie wahrscheinlich eine Anfrage oder Aktion schädlich ist, und ist oft nur kurzfristig relevant. Vertrauen entsteht dagegen über Zeit und basiert auf Reputation.

Ein Beispiel aus dem Alltag macht das deutlich: Sie sitzen abends zu Hause vor dem Fernseher, als plötzlich wiederholt die Türklingel läutet. Das ist nicht nur störend, sondern auch ungewöhnlich. Stürmisches Klingeln spät in der Nacht wirkt alarmierend.

Dann sehen Sie über Ihre Türkamera, dass es Ihr bester Freund von nebenan ist. Natürlich vertrauen Sie ihm, und vermutlich würden Sie ihn hereinlassen.

In diesem Fall würde eine Regel wie „alle ablehnen, die nachts klingeln“ oder „alle ablehnen, die mehr als zehnmal klingeln“ nicht ausreichen. Vertrauen ist der ausschlaggebende Faktor.

Übertragen auf Internet-Traffic bedeutet das: Unsere Produktstrategie im Bereich Bots und Betrug konzentriert sich darauf, ein ganzes Ökosystem auf Basis von Vertrauen aufzubauen. Ziel ist es, Website-Betreibern die Anreize und Grundbausteine zu geben, mit denen sie Verhalten fördern können, das das Internet für alle sicherer macht: von der Blockierung bösartiger Aktivitäten am unteren Ende bis zur aktiven Unterstützung eines sichereren Internets am oberen Ende.

## **Gutes Verhalten basiert auf Transparenz**

Was zählt als gutes Verhalten? Klare Beispiele liefern die verifizierten Bots und Agents in BotBase. Im vergangenen Monat haben wir[ eine aktualisierte pragmatische Taxonomie für die guten Bots vorgestellt](https://blog.cloudflare.com/content-independence-day-ai-options/), die wir in unserem System erfassen. „[Verified](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/)“ bedeutet im Kern zwei Dinge: Sie geben ehrlich an, wer Sie sind, und Sie missbrauchen das Vertrauen nicht, das Sie sich verdient haben. 

Transparenz zwischen Website-Betreiber und Bot-Betreiber ermöglicht eine symbiotische Beziehung: Website-Betreiber können festlegen, welche Verhaltensweisen und Datennutzungen sie auf ihren Websites zulassen möchten, und Bot-Betreiber erhalten leichter Zugang. Diese Transparenz schafft Vertrauen in der Beziehung: Wer nichts zu verbergen hat, sollte durch die Offenlegung seiner Identität bei Websites, die dieses Verhalten zulassen möchten, auf weniger Hürden stoßen.

[BotBase](https://developers.cloudflare.com/bots/botbase/) soll nicht nur erklären, wer „gut“ ist. Es ist als Verzeichnis aller bekannten Bots und Agents gedacht und stellt die Fakten bereit. Im Vergleich zu unserem früheren Bots Directory, das nur bekannte gute Bots enthielt, kann BotBase auch _weniger gute_ Bots und Agents erfassen. Der Grund: Unsere Systeme verfolgen und validieren das Verhalten bekannter guter Akteure. Dadurch haben wir die Werkzeuge, um zu erkennen, wenn Erwartungen nicht erfüllt werden. Wer Vertrauen im Cloudflare-Netzwerk missbraucht, sollte **nicht** einfach zugelassen werden und wird daher unverifiziert.

## **Schlechtes Verhalten: offen, verdeckt und alles dazwischen**

Vor einigen Wochen haben wir[ Precursor](https://blog.cloudflare.com/introducing-precursor/) vorgestellt, ein kontinuierliches clientseitiges System zur Erkennung auch _subtil unmenschlichen_ Bot-Traffics, der bei reiner Bewertung von Netzwerksignalen unentdeckt bleiben kann. Wenn ein Kunde Precursor aktiviert, wird die JavaScript-Erkennung über das CDN injiziert. Sie müssen also nicht manuell herausfinden, wo oder wie diese Erkennungen erneut ausgeführt werden. Außerdem bewertet Precursor das Nutzerverhalten[ kontinuierlich über die gesamte Sitzung hinweg](https://developers.cloudflare.com/cloudflare-challenges/precursor/). Missbräuchlicher Traffic erhält dadurch keinen Freipass mehr, nur weil er eine Client- oder Browserprüfung einmal bestanden hat.

Übertragen wir unser Risiko-und-Vertrauen-Modell auf diese clientseitigen Erkennungsmechanismen, zeigt sich: CAPTCHAs oder einmalige Hürden sind risikobasiert, was bedeutet, dass ihnen _Kontext_ fehlt. Andererseits ist die Überprüfung anhand von Verhaltensmerkmalen vertrauensbasiert, da sie mehr Kontextinformationen aus der gesamten Benutzersitzung erfassen kann. Precursor ist das Werkzeug für uns, um dieses Verhalten zu analysieren. Zusammengefasst ist Precursor so leistungsstark, weil es:

  1. es vertrauensbasierte Erkennung über die gesamte Sitzung bietet und
  2. **die Kosten für Bot-Entwickler erhöht,** , menschliches Verhalten über mehrere Seiten hinweg nachzuahmen.



Wenn es _wirtschaftlich unattraktiv_ wird, diese Erkennung zu umgehen, gewinnen wir das adversarische Spiel.

Was haben wir seit dem Start gelernt? Zum Zeitpunkt der Erstellung dieses Beitrags sehen wir in nur 24 Stunden **206 Millionen Precursor-Bewertungsereignisse** über**73.438 Zonen** im Cloudflare-Netzwerk.

Die Daten bestätigen Muster, die wir beim Start vermutet hatten und nun über Zehntausende Domains hinweg validieren können:

  * Verdächtiges Verhalten tritt häufig mitten in einer Sitzung auf und würde von punktueller Erkennung nicht erfasst.
  * **Verhalten wechselt im Verlauf einer Sitzung oft zwischen menschlich und agentenbasierten**. In solchen Fällen ist es wichtig, die _Absicht_ zu verstehen, damit Website-Betreiber keine Nutzerabläufe blockieren, die sie eigentlich zulassen möchten.
    * Diese Erkenntnisse unterstreichen die Bedeutung eines Bot-Klassifizierungssystems, mit dem Website-Betreiber Traffic nach Anwendungsfall, Zweck und Datennutzung steuern können. Genau deshalb haben wir die Taxonomie-Updates für BotBase priorisiert.



Wer mehr darüber erfahren möchte, wie Precursor funktioniert, findet in unserem[ Ankündigungsbeitrag](https://blog.cloudflare.com/introducing-precursor/) einen Einblick in die Signale, die zeigen, dass Irren menschlich ist. **Heute gehen wir einen Schritt weiter: Mit einer interaktiven Demo kann jeder im Internet simulieren, wie Precursor Cursorbewegungen nachverfolgen würde.**

**[Precursor Trace](https://precursor-trace.cloudflare.app) **ist jetzt live und zeigt, wie wir _Ihre_ Cursorbewegungen mit einem Teil des Precursor-Erkennungsmechanismus bewerten würden. Sie können sehen, ob Sie beschleunigen oder korrigieren, welchen Rhythmus und welche Textur Ihre Cursorbewegung hat und mehr – Details, über die Sie sich als Mensch bei der Computernutzung wahrscheinlich noch nie Gedanken gemacht haben. Probieren Sie es aus.

## **Adaptive Intelligence kommt bald**

Die [ Bot-Erkennungsmechanismen](https://developers.cloudflare.com/bots/concepts/bot-detection-engines/) von Cloudflare können bei der Bewertung, ob eine bestimmte Anfrage automatisiert ist oder nicht, zu[ unterschiedlichen Ergebnissen](https://developers.cloudflare.com/bots/concepts/bot-score/#bot-groupings) kommen. Bei Anfragen, die als automatisiert eingestuft werden, kann die Bewertung entweder 1) eindeutig automatisiert lauten – auf Grundlage bewährter, deterministischer Methoden oder charakteristischer Bot-Fingerprints – oder 2) wahrscheinlich automatisiert, basierend auf dem prädiktiven Scoring von Cloudflares Bots ML.

Historisch wurde[ Bots ML](https://developers.cloudflare.com/bots/concepts/bot-score/#machine-learning) in Versionen aktualisiert, die jeweils als Produktlaunch angekündigt wurden. Dieses Tempo reicht nicht aus, wenn Bots sich innerhalb von Stunden oder Minuten anpassen.

Adaptive Intelligence ist eine völlig neue Detection Engine und unterscheidet sich von allem, was wir bisher im Bots-ML-Bereich entwickelt haben. **Das Modell ist adaptiv** : Es hat aus allem gelernt, was wir in der Vergangenheit beobachtet haben. Noch wichtiger ist jedoch, dass es _kontinuierlich_ weiterlernen und sich auf Grundlage dessen, was es beobachtet, selbst anpassen wird. Adaptive Intelligence wird sich anhand einer breiten Spanne erkannter Traffic-Muster selbst aktualisieren, von erwünschtem bis zu unerwünschtem Verhalten. Kunden müssen künftig nicht mehr auf eine formale neue Modellversion wechseln, damit ihnen stets die neuesten prädiktiven Funktionen zur Bot-Erkennung zur Verfügung stehen. 

Alle Bot Management-Kunden erhalten in naher Zukunft Zugriff auf Adaptive Intelligence. Weitere Details folgen mit der Launch-Ankündigung.

## **Über deterministische Ansätze hinaus: Bot-Verhalten beeinflussen**

Bisher haben wir uns auf die Cloudflare-Seite konzentriert: Strategie, Erkennung und Taxonomie. All das versetzt Cloudflare in die Lage, Website-Betreibern die Werkzeuge bereitzustellen, die sie benötigen, um die gewünschten Traffic-Richtlinien für ihre Websites festzulegen. Nun betrachten wir die Seite der Website-Betreiber genauer und sprechen über **fortgeschrittene Abwehrmaßnahmen** , mit denen sie selbst Bot-Verhalten beeinflussen können.

Bei offensichtlicheren Abwehrmaßnahmen entsteht ein Problem, das wir das „Bot Antibiotic Problem“ nennen. Wenn Bots immer eine deterministische Antwort erhalten, kann ein Entwickler eines bösartigen Bots Ihre Abwehr leichter testen, beobachten und zurückentwickeln.

Wir entwickeln deshalb Abwehrmaßnahmen, die _speziell auf das Drosseln von Bots ausgelegt_ sind, mit unterschiedlichen Ansätzen für bösartige und gutartige Bots.. Wir können sie in drei Ansätze unterteilen:

Ansatz 1: Unvorhersehbarkeit und zufällige Maßnahmen. Zufällige Antworten wie Blockieren, Challenge oder Zulassen bei verdächtigem automatisiertem Traffic stören die automatisierte Wiederholungslogik und Fingerprinting-Mechanismen eines Bots.

Ansatz 2:[ AI Labyrinth](https://developers.cloudflare.com/bots/additional-configurations/ai-labyrinth/), eine defensive Antwort, die nicht autorisierte Bots in ein endloses Labyrinth KI-generierter Webseiten lockt. Durch _Irreführung_ können Sie Rechen- und Crawl-Budgets bösartiger Bots verschwenden. Website-Betreiber erhalten in AI Labyrinth drei Optionen.

  * „**Maze** “ erzeugt ein endloses Netz verlinkter Seiten, dem Bots folgen können.
  * „**Summary** “ liefert Crawlern eine LLM-generierte Zusammenfassung einer Seite, die echt wirkt, aber als KI-Trainingsdaten vollständig nutzlos ist.
  * „**Poison** “ stellt einem Bot bewusst falsche Inhalte bereit, etwa falsche Preise oder Lagerbestände, und verunreinigt damit die Daten, die er für KI-Training sammelt.



Ansatz 3: Warteschlangen für gute Bots. Nicht jeder agentenbasierte Traffic ist schlecht. Queuing steuert den Durchsatz für legitimen automatisierten Traffic, etwa nutzergesteuerte Shopping-Agents, ohne ihnen den Zugriff vollständig zu verweigern.

Diese fortgeschrittenen, Bot-spezifischen Abwehrmaßnahmen sollen im weiteren Jahresverlauf eingeführt werden. Website-Betreiber können dann wählen, wie streng ihre Abwehrmaßnahmen sein sollen.

Eine starke Verteidigung ist vorausschauend: Sie lernt selbst, justiert bei sich selbstständig nach und benötigt nicht mehrere Sicherheitsexperten in einer Besprechung, die reaktiv eine Lösung für den neuesten schwer erkennbaren Angriff konfigurieren. Das kann wie ein System „temporärer“ Regeln aussehen, bei dem das Regelwerk dynamisch ist. Das ist beabsichtigt: Wenn Angriffe sich ständig weiterentwickeln, sollten Abwehrmaßnahmen das ebenfalls tun. Deshalb arbeiten wir daran, Erkennungen und Abwehrmaßnahmen immer einen Schritt voraus zu halten.

## **Schaffen Sie das Vertrauensökosystem, das zu Ihnen passt**

Wirklich jeder kann Maßnahmen ergreifen, um zu definieren, wie automatisierte Agenten mit ihrer Infrastruktur interagieren. 

Einige Dinge, die Sie ausprobieren sollten:

  * Aktivieren Sie[ Precursor](https://developers.cloudflare.com/cloudflare-challenges/precursor/#get-started)
  * Experimentieren Sie mit[ Precursor Trace](https://integrityand.trust.cfdata.org/precursor-trace/)
  * Erkunden Sie[ BotBase](https://developers.cloudflare.com/bots/botbase/)



Wenn wir statische, punktuelle Prüfungen hinter uns lassen und kontinuierliche Vertrauensbewertung nutzen, reduzieren wir das Katz-und-Maus-Spiel mit Bot-Betreibern. Wenn Sie die[ Bot-Erkennung von Cloudflare](https://www.cloudflare.com/products/bot-mitigation/) noch nicht verwenden, sehen Sie sie sich an und bauen Sie das Vertrauensökosystem auf, das zu Ihnen passt.

]]>01KZTAYNVQB8AQY65K464AK806Vom Ranking zur Empfehlung: Machen Sie Ihre Website fit für das Zeitalter der KI-Agentenhttps://blog.cloudflare.com/de-de/aeo/ Tue, 11 Aug 2026 01:42:16 GMTInzwischen wird im Internet mehr als die Hälfte der Anfragen nicht von Menschen, sondern von Maschinen gestellt. Agent Readiness zeigt, wie gut Agenten Ihre Website auffinden und lesen können. Mit Answer Engine Optimization (AEO) lässt sich nachverfolgen, wie oft KI-Assistenten Ihren Internetauftritt empfehlen.AEOAgententauglichkeitAgentsAgents WeekAIDashboardMCPProdukt-NewsRadarIhr nächster Kunde findet Sie möglicherweise nicht über eine Suchmaschine. Stattdessen fragt er vielleicht einen AI-Assistenten: „Wie mache ich XY?“, „Welche Option ist die beste für jemanden wie mich?“, „Kannst du das für mich erledigen?“. Ein Agent findet dann die Antwort, wägt die Wahlmöglichkeiten ab und handelt im Namen des Kunden. Der Entscheidung für einen bestimmten Anbieter fällt immer häufiger beim Lesen der Antwort eines Modells – also bevor ein Mensch die zugehörige Homepage jemals auch nur gesehen hat.

Dieses Agenten-Publikum existiert bereits: Nach unseren Erhebungen entfällt inzwischen weniger als die Hälfte aller HTML-Seitenanfragen[ auf einen Menschen](https://radar.cloudflare.com/traffic#bot-vs-human). Nicht immer handelt es sich bei diesen Maschinen um Agenten, die im Auftrag eines Menschen handeln. Dieser Anteil wächst jedoch rasant und Antwort-Engines, Einkaufsassistenten und Forschungstools werden maßgeblichen Einfluss darauf haben, welche Unternehmen gefunden und empfohlen werden. Früher bedeutete Auffindbarkeit, im Ranking einer Ergebnisseite aufzutauchen. Heute kommt es für Websites dagegen darauf an, von den Agenten, die ihren Kunden den Weg zeigen, gefunden, gelesen und mit Überzeugung empfohlen zu werden.

Bisherige Kennzahlen wie Klicks und Seitenaufrufe von Menschen liefern heute nur noch ein unvollständiges Bild. Wir haben mit Website-Betreibern gesprochen, deren Zugriffsprotokolle vor KI-Bots überquellen und die sich völlig im Unklaren darüber sind, ob diese Bots ihre Website überhaupt benutzen können oder ihre Produkte und Dienstleistungen ihren Nutzern empfehlen. Insbesondere zwei Fragen haben wir in diesem Kontext immer wieder gehört:

  * Können Agenten meine Website tatsächlich benutzen?
  * Werde ich empfohlen?



Um ihnen bei der Beantwortung zu helfen, haben wir unsere[ vorherige Arbeit zu Agent Readiness](https://blog.cloudflare.com/agent-readiness/) in das Cloudflare-Dashboard integriert und dieses um unser neues AEO (Answer Engine Optimization)-Tool ergänzt. Diese Werkzeuge behandeln Agenten als zentrale Benutzergruppe Ihrer Website und zeigen Ihnen, wie oft diese von einem Agenten gesehen wird und wie häufig Sie empfohlen werden.

Das bietet große Chancen und die Ansprüche sind bislang nicht besonders hoch, weil die meisten Websites noch nicht für diese Art Nutzer gebaut sind. So, wie in den Anfangszeiten von SEO die für Suchmaschinen erstellten Internetauftritte honoriert wurden, geschieht das jetzt für Websites, die von vornherein für Agenten gebaut wurden. Wenn eine Webpräsenz leicht auffindbar und lesbar ist und zudem Vertrauen einflößt, werden die Agenten sie auch empfehlen.

## **Diagnostics: Ist Ihre Website für Agenten bereit?**

Diagnostics übernimmt die technische Überprüfung innerhalb von Agent Readiness. Das Tool durchsucht Ihre Website so, wie ein Agent sie liest: Es prüft, ob der Zugriff erlaubt ist und ob es Ihre Inhalte finden kann, ruft eine saubere maschinenlesbare Kopie ab und findet die Schnittstellen, an die es Abfragen richten kann. 

Während eine Person einfach nur Ihre Homepage lädt, prüft ein Agent Ihre robots.txt-Datei, Ihre Sitemap, Ihre Antwortheader, eine Markdown-Version Ihrer Inhalte und veröffentlichte Metadaten für Authentifizierung und Tools auf Herz und Nieren.

Diagnostics verknüpft diese Überprüfung mit einem Hostnamen und fasst die Ergebnisse in einer einzigen Agent Readiness-Übersicht zusammen. Die Einstufungsgrade reichen von „Nicht bereit“ bis zu „Völlig agentennativ“. Nach jeder Prüfung wird angegeben, ob sie bestanden, nicht bestanden oder neutral ausgegangen ist. Dies wird mit einem Kommentar dazu, warum das von Bedeutung ist, sowie mit einer Nachweiskette mit der genauen Anfrage und der von uns verzeichneten Antwort versehen.

Diese Kontrollen sind nach dem Grad des mit ihnen verbundenen Arbeitsaufwands gruppiert, damit Sie wissen, wo Sie anfangen sollten:

  * Schnelle Erfolgserlebnisse: Zu den grundlegenden und zugleich besonders hilfreichen Elementen, die die meisten Websites nicht vorweisen können, gehören eine von Crawlern lesbare robots.txt-Datei, eine XML-Sitemap, Regeln für KI-Crawler und ein sorgfältiges Markdown für Agenten.
  * Technische Grundlagen: Die nächste Ebene umfasst Signale, die deutlich machen, wie Ihre Inhalte verwendet werden dürfen, einen API-Katalog, Link-Header und Anmeldeanweisungen für Agenten.
  * Erweiterte Integration: Hier wird nach Merkmalen der Agentennativität wie OAuth-Erkennung, MCP (Model Context Protocol), A2A (Agent2Agent)-Agentensteckbriefe, einem Index der vorhandenen Funktionen, Web Bot Auth und WebMCP Ausschau gehalten.
  * Handel: Die neuen Standards für von Agenten abgewickelte Zahlungen wie[ x402](https://blog.cloudflare.com/x402/) (eine Erweiterung des klassischen HTTP-Statuscode 402 „Payment required“), ACP (Agent Commerce Protocol), Universal Commerce Protocol (UCP) und AP2 (Agent Payments Protocol). Dies hat derzeit reinen Informationscharakter und fließt nicht in Ihre Bewertung ein.



Every suggested improvement comes with a next step. When there’s a Cloudflare feature that can help, there's a "Set up in Cloudflare" link straight to the setting, such as switching on Markdown for Agents or managed robots.txt. For everything else, there’s a "Copy Agent Prompt" button that proposes what your coding agent needs to build. Make the change, re-scan, and watch the checkmark turn green.

## **AEO: Werden Sie von KI-Assistenten empfohlen?**

Diagnostics verrät, ob Ihre Website von Agenten gelesen werden kann. Unter der Registerkarte „AEO“ können Sie sehen, was danach passiert: Wenn ein Kunde einem KI-Assistenten eine Frage stellt, die für Ihr Geschäftssegment relevant ist, empfiehlt der Agent dann Sie oder einen Ihrer Mitbewerber? Diese Information lässt sich nicht wie bei einem Suchmaschinenranking einfach nachschlagen. Es gibt keine Statistik dazu, wie oft Ihre Inhalte gesehen wurden oder wie häufig falsch geklickt wurde. Wird also an Ihrer Stelle ein Konkurrent genannt, entgeht Ihnen dieses Geschäft, ohne dass Sie das überhaupt mitbekommen.

Wir schließen anhand Ihrer Website auf Ihre Branche (z. B. Gesundheit und Fitness) und Ihr Segment (z. B. Sportbekleidung) und füttern die führenden KI-Assistenten (zurzeit sind das Claude von Anthropic und GPT von OpenAI) testweise mit zu erwartenden Prompts von Kunden, um herauszufinden, wie die Agenten reagieren. Diese Prompts bauen wir so auf, dass dabei die Art und Weise nachempfunden wird, in der Dinge in der echten Welt normalerweise entdeckt werden. Wir fragen also nach Empfehlungen, Produktvergleichen und allgemeinen Ratschlägen innerhalb Ihres Segments. Die Analyse der Antworten von Modellen auf diese realistischen Anfragen liefert unter anderem folgende aufschlussreiche Kennzahlen:

  * **Zitierquote (Citation Rate):** der Anteil der Antworten in Ihrem Segment, bei denen Ihre Website als Quelle genannt wird.
  * **Sichtbarkeit (Prominence):** wie groß im Fall einer Zitierung Ihr tatsächlicher Anteil an der Antwort ist und wie früh dieser Teil angezeigt wird.
  * **Erwähnungsquote:** wie oft Assistenten Ihren Markennamen in ihrer Antwort nennen – also beispielsweise, wie oft „Cloudflare“ in der Antwort erscheint, unabhängig davon, ob[ cloudflare.com](http://cloudflare.com) als Quelle zitiert wird. In Kombination mit der Zitierquote werden damit das Wahrgenommenwerden und die Zurechnung voneinander abgegrenzt: Wenn Sie von Assistenten häufiger erwähnt als zitiert werden, heißt das, dass das entsprechende Modell Sie zwar auf dem Schirm hat, Sie aber noch nicht als zitierwürdig ansieht. Das ist ein feiner Unterschied.
  * **Marktgewicht (Share of Voice):** ihr Anteil an den Zitierungen im Vergleich zu dem Ihrer Wettbewerber – das verrät Ihnen, wem die Prompts zugutekommen, bei denen Sie leer ausgehen.



Um beurteilen zu können, wie ein KI-Modell Ihre Marktpräsenz wahrnimmt, ermitteln wir für jede Branche und jedes Segment einen Benchmarkwert, bevor wir eine bestimmte Website bewerten. Dafür füttern wir KI-Assistenten mit Prompts, die in diesem Segment mit hoher Wahrscheinlich benutzt werden. Ihre Marke wird dabei nicht konkret genannt. Dann protokollieren wird, welche Websites zitiert werden, wo sie erscheinen und wie sehr sie dabei hervorstechen.

Anstatt jedes Mal eine neue Abfrage an die Modelle zu richten, wenn ein Website-Betreiber einen Scan absolvieren lässt, führen wir diese Auswertung einmal pro Segment durch und verwenden die Basiswerte für alle Konten dieser Domain wieder. Die Vorberechnung dieses Datensatzes bietet im Wesentlichen drei Vorteile:

  * **Keine Latenz:** Anstatt auf Echtzeit-Abfragen des Modells zu warten, werden die Ergebnisse sofort aus einem Schnappschuss geladen.
  * **Geringerer Rechenleistungsbedarf:** Durch das Zusammenführen von Abfragen auf Segmentebene werden im Rahmen Tausender Scans überflüssige KI-Aufrufe vermieden.
  * **Bewertung der Brancheneignung:** Durch die Wiederverwendung des Datenkorpus kann ermittelt werden, welche Marken regelmäßig zusammen auftauchen. Daraus lässt sich ein Score bezüglich der Brancheneignung ableiten. Dieser verrät, ob ein KI-Assistent Ihre Website gemeinsam mit Ihren tatsächlichen Mitbewerbern betrachtet.



KI-Assistenten geben auf dieselbe Frage oft unterschiedliche Antworten. Um dem Rechnung zu tragen, geben wir mithilfe von[ Cloudflare AI Gateway](https://www.cloudflare.com/products/ai-gateway/) den Assistenten der verschiedenen Modelle etliche Male dieselben Prompts vor. So bekommen wir die Antworten zu Gesicht, die auch ein normaler Kunde sehen würde, also den Antworttext mit den von den jeweiligen Assistenten zitierten Quellen. Daraus lassen sich dann mehrere Schlüsse ziehen. 

Wir überprüfen, ob Ihre Website erwähnt wurde, ob Sie als Quelle angegeben wurden und wenn ja, wie früh innerhalb der Antwort, und welcher Anteil der Antwort im Kern Ihnen zugeschrieben wird. Wenn echtes Urteilsvermögen gefragt ist, übernimmt Workers AI den Hauptteil der Arbeit. Wir betreiben die Lösung nativ auf unserer eigenen Infrastruktur, sodass sie jede Antwort lesen und bewerten kann, wie Sie in den Antworten zitiert und erwähnt werden. Außerdem nutzen wird eine genaue Textanalyse anstelle eines Modells, das seine eigenen Antworten bewertet. Bei dieser Vorgehensweise werden Dutzende von Einzelantworten in praxisrelevante Kennzahlen überführt. Durch die Abstraktion der Abfrage- und Auswertungs-Pipeline für mehrere Modelle liefert das Tool Metriken, ohne dass ein eigenes Auswertungskonzept entwickelt werden muss.

Zusätzlich zu den Antworten schlüsselt eine Darstellung der KI-Betreiber-Aktivität den tatsächlichen durch Crawling und Verweise generierten Datenverkehr auf Ihrer Website nach Betreiber (OpenAI, Google usw.) auf. Sie können damit sehen, wer Ihre Inhalte ausliest, wer dafür sorgt, dass Ihr Internetauftritt von Besuchern auch aufgerufen wird, und welche Fehlermeldungen ihnen dabei begegnen (403: gesperrt; 404: nicht funktionierender Link). Reagiert werden sollte, wenn einer dieser Agenten Tausende Ihrer Seiten durchsucht, aber nie jemanden dorthin weiterleitet. Das bedeutet nämlich, dass der betreffende Betreiber Ihre Arbeit also für sich nutzt, ohne Kunden für Sie zu generieren.

Da diese Zahlen speziell für Ihre Website erhoben werden, können Sie damit experimentieren, den Scan erneut durchführen und die Auswirkungen auf die konkreten Fragen messen, die für Ihr Unternehmen geschäftsfördernd sind.

## **Lernen Sie Ihr anderes Publikum kennen**

Bisher konnte man nur im Nebel stochern, um eine Ahnung davon zu bekommen, welchen Einfluss Agenten auf das eigene Geschäft haben. Man musste Protokolle durchforsten, um daraus abzuleiten, wer die Website besucht hatte, oder selbst eine Frage an einen Chatbot richten, um zu sehen, ob das eigene Unternehmen erwähnt wurde. Doch jetzt liefern Agent Readiness und AEO Ihnen die Daten, die Sie brauchen, um handeln zu können. Und da die Anfragen über Cloudflare geleitet werden, liefern diese Tools – die sich im Laufe der Zeit noch verbessern werden – wo immer möglich keine Schätz-, sondern Messwerte. 

Wir haben schon immer dafür gesorgt, dass Betreiber herausfinden können, wer Ihre Website besucht, und selbst entscheiden können, auf welche Weise sie mit diesen Besuchern interagieren. Agenten sind dabei nur die neueste Publikumgeneration. Wenn Unternehmen es Agenten leicht machen, sie zu finden, zu verstehen und ihnen zu vertrauen, werden sie auch empfohlen. Unter Agent Readiness erfahren Sie, ob Sie zu diesem Kreis gehören, und was Sie andernfalls unternehmen können.

Möchten Sie herausfinden, ob KI-Agenten Kunden zu Ihnen lotsen? Dann rufen Sie in Ihrem Dashboard die Registerkarte „Overview“ (Übersicht) auf. Darüber können Sie ihre Website fit für Agenten machen und Frühzugang zu AEO Visibility anfordern.

_Sie setzen bei der Entwicklung auf das offene, für Agenten optimierte Web? Unter der Registerkarte „**Agent Readiness** “ in Ihrem[ Cloudflare-Dashboard](https://dash.cloudflare.com) können Sie uns im[ Cloudflare Developer Discord](https://discord.cloudflare.com)-Kanal davon berichten._

]]>01KZQ5XS09BWR2S8MQPMKXR2WVMit identitätsbezogener Analyse unerwünschtes KI-Verhalten erkennenhttps://blog.cloudflare.com/de-de/identity-aware-ai-gateway/ Mon, 10 Aug 2026 08:14:58 GMTDas identitätsbezogene (identity-aware) AI Gateway ist jetzt im Open Beta. User Insights verwandelt diesen Datenverkehr in eine Verhaltensbaseline für jede Person und jeden Agenten und erkennt Insider-Risiken in dem Moment, in dem sie auftreten.AgentsAgents WeekAIAI Gateway (DE)EntwicklerEntwicklerplattformProdukt-NewsBei einem Blick auf Ihre KI-Kosten lässt sich nicht ohne Weiteres feststellen, ob etwas ungewöhnlich ist. Dafür benötigen Sie zunächst eine Verhaltensbaseline, anhand derer Veränderungen auffallen – etwa ein Agent, dessen Aktivität aus dem Ruder läuft, oder ein Mitarbeiter mit einem zehnfachen Nutzungsanstieg. Wenn Sie solche Verschiebungen erkennen können, können Sie mit der Untersuchung beginnen. Bisher waren sie jedoch nur schwer zu erkennen.

Eine der wichtigsten Herausforderungen für Organisationen besteht derzeit darin, nachvollziehen zu können, wer KI wie nutzt. Laut [einem Bericht](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf) der Stanford University nannten 59 % der Organisationen Wissenslücken als größtes Hindernis für eine verantwortungsvolle KI-Governance. 

Dabei handelt es sich nicht nur um ein finanzielles, sondern ebenso um ein Sicherheitsproblem. Um diese Herausforderungen zu lösen, braucht es zwei Dinge: eine verifizierte Identität für jede Anfrage (damit hinter einem plötzlichen Anstieg ein konkreter Verantwortlicher steht) und ein Bild davon, was für diese Identität als normales Verhalten gilt. Heute stellen wir beides vor.

Das identitätsbezogene AI Gateway mit Cloudflare Access ist ab sofort in der offenen Beta verfügbar. User Insights ist für alle AI-Gateway-Kunden ohne Aufpreis allgemein verfügbar. Zusammen erstellen beide aus dem bestehenden AI-Gateway-Datenverkehr eine Verhaltensbaseline für jede Person und jeden Agenten und identifizieren Abweichungen vom normalen Verhalten.

## Was ist AI Gateway?

[AI Gateway](https://developers.cloudflare.com/ai-gateway/) dient als zentrale Kontrollinstanz für Ihre gesamte KI-Nutzung. Statt direkte Modellaufrufe von Apps und Teams an OpenAI, Anthropic, Google oder Workers AI zu senden, laufen Anfragen zuerst durch AI Gateway. Dadurch haben Sie einen einzigen Ort, um Ihre KI-Nutzung zu überwachen, zu schützen und zu verwalten.

Es funktioniert mit den Anwendungen, die Sie entwickeln, und mit den Entwicklungswerkzeugen, die Ihre Entwickler bereits nutzen. Routen Sie [Agent-Harnesses](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/) wie Claude Code, Codex und GitHub Copilot über das AI Gateway, und sie fallen unter die gleiche Sichtbarkeit und Kontrolle wie alle anderen.

## Identitätsbezogenes (Identity-aware) AI Gateway 

Mit der Integration von AI Gateway- und[ Cloudflare Access](https://developers.cloudflare.com/ai-gateway/configuration/cloudflare-access) können Sie eine[ Vanity-Domain](https://developers.cloudflare.com/ai-gateway/configuration/custom-domains/) vor Ihr Gateway schalten und sie – wie jede andere Anwendung auch – mit Access schützen. Dadurch können Sie:

  * sich über einen beliebigen SAML-kompatiblen Identitätsanbieter wie Okta oder Entra authentifizieren, sodass keine Cloudflare-API-Schlüssel mehr erstellt und weitergegeben werden müssen.
  * genau festlegen, wer auf Ihr Gateway zugreifen darf.
  * Anfragen an einen übersichtlichen Hostnamen wie `ai.example.com` senden – ganz ohne Konto-ID oder Gateway-ID in der URL.



Jede authentifizierte Anfrage enthält jetzt die Identität des Nutzers aus Access. AI Gateway ergänzt die verifizierte Access-Benutzer-ID als `cf.user_id` in den Metadaten der Anfrage, sodass Sie Logs, Analysen und Ausgaben nach der Person filtern können, die die Anfrage tatsächlich gestellt hat.

Zusammen mit[ Ausgabenlimits](https://developers.cloudflare.com/ai-gateway/features/spend-limits/) wird die Nutzeridentität zu einem Instrument für die Budgetkontrolle. Weil jede Anfrage jetzt einer konkreten Person zugeordnet ist, lassen sich individuelle Ausgabenlimits festlegen: Jeder Nutzer erhält ein eigenes Budget, und sobald dieses erreicht ist, können weitere Anfragen blockiert oder auf ein kostengünstigeres Modell umgeleitet werden. So gibt es keine unerwarteten Rechnungen mehr und keine gemeinsam genutzten API-Schlüssel, die verbergen, wer welche Kosten verursacht hat.

Einer unserer ersten Anwender, Flexport, stand vor genau diesem Problem.

„Gemeinsam genutzte API-Schlüssel machen es nahezu unmöglich nachzuvollziehen, wer einen KI-Dienst nutzt oder die Zugriffsrichtlinien anzuwenden, die wir bereits für unsere Mitarbeitenden definiert haben“, sagt Max Baumgarten, Staff Security Engineer bei Flexport. „Wenn wir Cloudflare Access vor AI Gateway schalten, erhält jede Anfrage eine authentifizierte Identität, und wir können unsere bestehenden Identitätsrichtlinien direkt auf Gateway-Ebene durchsetzen. Unsere Teams können KI-Tools einführen, ohne für jeden Client ein separates Authentifizierungssystem aufbauen zu müssen.“

Schon bald werden Sie die Gruppen Ihres Identitätsanbieters nutzen können, um Ausgabenlimits zu definieren oder den Modellzugriff einzelner Gruppen zu steuern. Beispielsweise können Sie Ihrem Machine-Learning-Team Frontier-Modelle freigeben, das Budget Ihres Support-Teams deckeln oder allen Mitarbeitenden eines bestimmten Projekts ein gemeinsames Budget zuweisen – abgebildet auf die Gruppen, die Sie bereits in Ihrem Identitätsanbieter pflegen.

## Das neue „User Insights“-Tab

In AI Gateway finden Sie jetzt einen neuen Reiter namens User Insights. User Insights analysiert den Datenverkehr, der durch Ihr Gateway fließt, und erstellt daraus ein Verhaltensprofil für jedes Konto. Die Funktion lernt das typische Verhalten jedes Kontos, erkennt Abweichungen davon und liefert Ihnen den nötigen Kontext, um zwischen einem außer Kontrolle geratenen Agenten und einem stark ausgelasteten Entwickler zu unterscheiden. Da User Insights den Datenverkehr nutzt, der ohnehin durch Ihr Gateway läuft, ist keine Einrichtung erforderlich

User Insights verfolgt die Kosten – einschließlich der Bereiche, in denen Geld verschwendet wird, etwa durch niedrige Cache-Trefferraten oder überdimensionierte Kontextfenster. Solche Funktionen bieten bereits viele Tools. Was sie jedoch nicht leisten, ist zu erkennen, ob sich ein Konto normal verhält. Genau darauf haben wir uns konzentriert – zusätzlich zu den Funktionen zur Kostenkontrolle. 

### Baseline für jedes Konto: Personen und Agenten

Jedes Konto bildet über die Zeit ein eigenes Verhaltensprofil aus – ganz gleich, ob es sich um eine Person oder einen Agenten handelt. Ein Agent, der im Drei-Stunden-Takt Tickets zusammenfasst, arbeitet sehr konsistent und vorhersehbar. Eine Person zeigt dagegen vielfältigere Prompts, unregelmäßige Aktivität und längere Sitzungen bei schwierigen Problemen. Beides ist normales Verhalten. Deshalb kann dieselbe Abweichung in einem Fall bloßes Rauschen und im anderen ein relevantes Signal sein.

In User Insights bewerten wir zunächst Sitzungen und nicht einzelne Anfragen. Absolute Schwellenwerte funktionieren hier nicht: Ein Anstieg um 500 USD kann bei einem Vielnutzer völlig normal sein, während eine Sitzung für 50 USD bei einem Agenten, der sonst immer nur 5 USD ausgibt, einer Verzehnfachung entspricht und andernfalls leicht unbemerkt bleiben könnte. Deshalb vergleichen wir jede Sitzung mit der eigenen Historie des Kontos und verwenden dafür die Sitzungskosten des 95. Perzentils (p95) der vergangenen 30 Tage. So erhalten wir ein Bild davon, wie das Konto normalerweise arbeitet. Alles, was mehr als das Doppelte seines p95-Werts kostet, ist ein starker Kandidat für anomales Verhalten.

Die folgende Analyse skizziert, wie wir zu diesen Zahlen gekommen sind.

Abbildung 1: Anomalieerkennung bei Sitzungsgebühren

**Wie man das obige Diagramm liest**

Das Diagramm zeigt reale Sitzungen aus unserem internen Traffic. Jeder Punkt steht für eine einzelne Sitzung (auf logarithmischen Skalen dargestellt):

  * **X-Achse (Sitzungskosten):** Gesamtkosten in USD.
  * **Y-Achse (x Benutzer p95):** Wie oft die Sitzung die persönliche Baseline des Benutzers überschritten hat.



Die beiden gestrichelten Schwellenlinien unterteilen die Sitzungen in vier Kategorien:

  * **Oben rechts (★ Sterne):** Überschreitet sowohl den 2-fachen Benutzer-p95-Basiswert als auch die Kontoebene-p99-Obergrenze. Dies sind hohe relative Spitzen, die einen signifikanten abnormalen Verbrauch darstellen und eine Warnung auslösen werden. 
  * **Oben links:** Hoher relativer Anstieg (2× Nutzer-p95), aber unterhalb der p99-Untergrenze des Kontos. Wir ignorieren dies, um Warnungen bei kleinen absoluten Kostenverschiebungen zu vermeiden.
  * **Unten rechts:** Hohe absolute Ausgaben, die jedoch mit dem typischen hohen Verbrauch dieses Benutzers übereinstimmen. Dies wird auch als normales Verhalten ignoriert.
  * **Unten links:** Normale Aktivität gut innerhalb beider Baselines.



Abbildung 2: Verteilung der Sitzungsgebühren auf Kontoebene

Dieses Histogramm (Abbildung 2) ordnet die Kosten jeder Sitzung innerhalb der Organisation zu, um ein kontoübergreifendes Limit festzulegen:

  * Typische Nutzung: Die große Mehrheit der Sitzungen kostet deutlich unter 10 USD, wobei das 95. Perzentil bei 20 USD liegt.
  * Konto p99 (200 USD): Nur 1 % aller Sitzungen im gesamten Unternehmen erreichen oder übersteigen 200 USD.



Warum haben wir uns also für p99 entschieden? Indem wir die absolute Kostengrenze auf den p99-Wert des gesamten Kontos festlegen, schaffen wir eine aussagekräftige Schwelle. Dadurch ist sichergestellt, dass eine Anomalie nicht nur eine plötzliche Veränderung bei einem einzelnen Nutzer darstellt, sondern zugleich zu den teuersten 1 % aller Sitzungen in der gesamten Organisation gehört.

Abbildung 3: Verlauf einer einzelnen Benutzersitzung

Baselines sind nicht statisch. Wenn sich das Nutzungsverhalten eines Kontos verändert, passen sich sein gleitender p95-Wert (grüne Linie) und der daraus abgeleitete 2×-Schwellenwert (orange Linie) entsprechend an. Dadurch spiegelt eine Warnung immer das aktuelle Verhalten wider und nicht einen einmal festgelegten Grenzwert. Zusätzlich wenden wir eine absolute Kostenschwelle an, sodass ein Ausschlag sowohl statistisch ungewöhnlich als auch relevant genug sein muss, um die Aufmerksamkeit eines Administrators zu rechtfertigen. Diese Kostenschwelle verhindert, dass bei einem Konto mit minimaler Nutzung bereits ein 500-facher Anstieg von wenigen Cent einen Alarm auslöst.

### Das richtige Objektiv zur Erkennung von unerwünschtem Verhalten 

Nach all den oben beschriebenen Analysen sehen Administratoren eine Ansicht der Konten, die von ihrem eigenen Verhaltensmuster abgewichen sind – alles Normale wird herausgefiltert. Diese gefilterte Ansicht bildet einen Feed mit auffälligem Verhalten.

Dieses Verhalten ist schwer zu erkennen, weil das Signal weder in einem neuen Tool noch in einer blockierten Aktion liegt. Vielmehr nutzt ein vertrauenswürdiges Konto seine bereits erlaubten Möglichkeiten plötzlich intensiver. Das kann ein Servicekonto sein, das auf einmal deutlich teurere Sitzungen ausführt, oder eine Person, deren Nutzung weit über das eigene Normalniveau hinaus ansteigt und über mehrere Tage erhöht bleibt.

Keiner dieser Fälle verstößt gegen eine Richtlinie, doch alle weichen von einer Verhaltensbaseline ab. Eine plötzliche Abweichung vom eigenen Nutzungsmuster eines Kontos ist oft das erste sichtbare Anzeichen dafür, dass Zugangsdaten kompromittiert wurden oder ein Agent außer Kontrolle gerät.

User Insights beurteilt weder die Absicht hinter einem Verhalten noch blockiert es Nutzer. Stattdessen zeigt es Administratoren die wenigen Konten, die begonnen haben, sich ungewöhnlich zu verhalten, damit jemand die nächste Frage stellen kann. Manchmal führt das zu einer echten Untersuchung. Manchmal bedeutet es lediglich, dass jemand etwas Anleitung braucht – etwa der Entwickler, der bei jedem Prompt die gesamte Codebasis einfügt, obwohl ein kleiner Ausschnitt genügen würde. 

## Was kommt als Nächstes? 

### Wir helfen Ihnen, von der Kostenkontrolle zur Kostenoptimierung überzugehen

Sobald Sie ein Budget festgelegt haben, stellt sich als Nächstes ganz natürlich die Frage: Wie lässt sich eine vergleichbare Ausgabequalität zu geringeren Kosten erzielen? Nicht jede Anfrage benötigt ein Frontier-Modell. Eine Zusammenfassungsaufgabe oder eine einfache Codevervollständigung kann auch auf einem günstigeren Modell ausgeführt werden, ohne dass die Qualität nennenswert leidet.

Wir entwickeln derzeit ein aufgabenspezifisches Smart Routing, bei dem AI Gateway eingehende Anfragen analysiert und sie an das Modell weiterleitet, das das beste Ergebnis zu den niedrigsten Kosten liefert. Auf Organisationsebene können Sie erkennen, wo sich durch das Routing auf effizientere Modelle die größten Einsparungen erzielen lassen. Das aufgabenbasierte Smart Routing befindet sich derzeit in aktiver Entwicklung. Weitere Informationen folgen, sobald die Funktion ausgereift ist.

### Wir helfen Ihnen zu verstehen, _wie_ KI eingesetzt wird

Die Anomalieerkennung erkennt, wenn ein Konto sein normales Verhaltensmuster verlässt, erklärt jedoch nicht die Ursache. Administratoren müssen deshalb weiterhin die Protokolle durchsuchen und zusammensetzen, was geschehen ist. Diese Lücke zu schließen, ist unser nächster Schwerpunkt – beginnend mit der Klassifizierung des tatsächlichen Datenverkehrs.

Wir entwickeln eine Prompt-Klassifizierung, die Anfragen in Kategorien wie Programmierung, Schreiben und weitere Bereiche einordnet. Diese Kategorien liefern genau den Kontext, der bei fast allen anderen Signalen fehlt. Ein Ausgabenanstieg im Bereich „Programmierung“ kann bei einem Entwickler akzeptabel sein; derselbe Anstieg in einer Kategorie, die dieses Konto noch nie genutzt hat, wäre dagegen auffällig. Durch die Klassifizierung sieht eine Organisation nicht nur, wie viel KI sie nutzt, sondern auch, wofür sie KI einsetzt. 

Damit beantwortet die Funktion auch die Frage, die vielen dieser Diskussionen zugrunde liegt: Wird KI tatsächlich für die vorgesehenen geschäftlichen Aufgaben eingesetzt? Sobald geschäftlicher Datenverkehr von allem anderen getrennt ist, wird auch die private Nutzung sichtbar. Von außen betrachtet sehen ein Mitarbeitender, der während der Arbeitszeit einem Nebenerwerb nachgeht, und jemand, der unauffällig Daten über ein Modell nach außen überträgt, zunächst gleich aus. Zwischen beiden zu unterscheiden, ist entscheidend, um Insider-Risiken zu erkennen. 

Sobald Ihr KI-Traffic durch das AI Gateway läuft, erhält ein Administrator bei jeder neuen Kategorie von Risiko- oder Effizienzsignalen eine zusätzliche Information ohne zusätzlichen Aufwand.

## Erste Schritte

User Insights steht ab sofort allen AI-Gateway-Kunden ohne Aufpreis allgemein zur Verfügung. Wer bereits Traffic durch AI Gateway leitet, findet die Funktion direkt im Dashboard. Wenn Sie AI Gateway bereits verwenden, können Sie diese Ansicht also sofort nutzen. 

Falls Sie noch keines erstellt haben,[ erstellen Sie ein Gateway](https://developers.cloudflare.com/ai-gateway/get-started/) und beginnen Sie, Anfragen an jedes Modell in unserem [Katalog](https://developers.cloudflare.com/ai/models/) zu senden. 

Wir empfehlen, AI Gateway hinter [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/policies/access/) zu betreiben, das jetzt als Open Beta verfügbar ist. Die Ansichten für Ausgaben und Anomalien funktionieren auch ohne Access, doch erst die Verknüpfung mit einer Identität macht aus einer anonymen Konto-ID einen konkreten Namen, auf den Sie tatsächlich reagieren können. Beginnen Sie im Monitoring-Modus, um zunächst Ihre Baselines kennenzulernen, bevor Sie Richtlinien durchsetzen.

Wir möchten hören, wie Sie heute mit KI umgehen. Beteiligen Sie sich an der Diskussion auf[ Discord](https://discord.cloudflare.com/) oder wenden Sie sich an Ihr Kundenteam.

]]>01KZNBEYYHKDCFKYNFV879DPCJCloudflare OS: eine offene Plattform für Agenten, Anwendungen und Arbeithttps://blog.cloudflare.com/de-de/cloudflare-os/ Mon, 10 Aug 2026 02:17:56 GMTCloudflare OS ist eine Open-Source-Plattform, die es jedem in Ihrem Unternehmen ermöglicht, Apps zu entwickeln, die Arbeit zu automatisieren und sicher auf interne Systeme zuzugreifen, basierend auf dem Wissen und der Betriebsweise Ihrer Organisation.AgentsAgents WeekAICloudflare AccessCloudflare OSCloudflare WorkersEntwicklerEntwicklerplattformOpen SourceProdukt-NewsJede Organisation hat eine Mission, einen Daseinszweck. Sie gibt diese Mission ebenso wie ihre Begriffe, Prozesse, Systeme, Standards und Arbeitsweisen an ihre Mitarbeitenden weiter. Diese bringen den vermittelten Kontext mit ihrer eigenen Erfahrung zusammen und richten ihre Arbeit auf die Mission aus.

Arbeit hat viele Erscheinungsformen — sie kann aus Code, Dokumenten und Folien, zwischenmenschlichen Beziehungen oder greifbaren Resultaten in der physischen Welt bestehen.

Einige davon sind einfach: Code läuft entweder oder er läuft nicht. Agenten haben in den letzten Jahren diesen Feedback-Loop genutzt, um Code zu produzieren, der für Entwickler „funktioniert“. Doch wie lässt sich das auf alle anderen übertragen?

Den gleichen Produktivitätsvorteil auf den Rest der Organisation zu übertragen, stellt ein schwierigeres Problem dar. Agenten müssen den Kontext des Unternehmens verstehen und auf die Systeme zugreifen können, die Menschen für ihre Arbeit nutzen. Sie müssen diesen Kontext und diesen Zugang in Arbeit umsetzen, die die Organisation ihrer Mission näherbringt.

Deshalb haben wir Cloudflare OS entwickelt. Es bietet jeder Person einen persönlichen Agenten und einen Arbeitsbereich: auf das jeweilige Unternehmen zugeschnitten – auf seine Arbeitsweise, sein Wissen und die Systeme, auf die es sich stützt.

Im Mai dieses Jahres haben wir allen Mitarbeitenden bei Cloudflare Zugriff auf die erste Version von Cloudflare OS gegeben. Tausende von Menschen in allen Abteilungen, viele davon außerhalb des Engineerings, nutzen es täglich, um Dokumente und Folien zu erstellen, wiederholbare Aufgaben zu automatisieren und kleine Apps zu entwickeln, um Daten zu visualisieren und ihnen bei ihrer Arbeit zu helfen.

Cloudflare OS gab allen zudem Zugriff auf eine gemeinsame Bibliothek aus Kontext und Skills, die von Teams bei Cloudflare erstellt wurde. Sie hält unsere Begriffswelt, Prozesse und bewährten bzw. derzeit besten bekannten Vorgehensweisen für wiederkehrende Arbeiten in Form von Anweisungen fest, die Agenten ausführen können. Sobald jemand einen besseren Ansatz entdeckt, können alle anderen davon profitieren.

**Heute veröffentlichen wir eine neue Open-Source-Version von[ Cloudflare OS](https://os.cloudflare.app/).** Jede Organisation kann es bereitstellen, mit internen Systemen verbinden und anpassen.

## **Was wir von der ersten Version gelernt haben**

Die Version von Cloudflare OS, die wir heute als Open Source veröffentlichen, basiert auf den Erkenntnissen aus dem internen Einsatz der ersten Version – eine Entwicklung, die unser CIO Sam Rhea in seinem[ Blogbeitrag](https://blog.cloudflare.com/how-we-use-ai-with-cloudflare-os) beschreibt.

Im Mittelpunkt der ersten Version standen einzelne Nutzer, die in privaten Workspaces mit Agenten zusammenarbeiteten. Die Apps waren statisch statt als laufende Software mit internen Systemen verbunden, und selbst weitgehend deterministische Jobs erforderten meist eine erneute Ausführung eines Agenten-Skills und damit zusätzlichen Token-Verbrauch.

Mit der Zusammenarbeit trat ein grundlegenderes Problem zutage. Der Zugriff auf einen[ MCP-Server](https://www.cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/) verriet uns, welche Werkzeuge ein Agent verwenden durfte, jedoch nicht, welche zugrunde liegenden Ressourcen er bereits eingesehen hatte. Als Nutzer begannen, Workspaces, Apps und Ergebnisse miteinander zu teilen, mussten wir gewährleisten, dass dabei keine Informationen sichtbar wurden, auf die jemand keinen Zugriff haben sollte.

Deshalb haben wir Cloudflare OS von Grund auf auf einer neuen Architektur aufgebaut. Sicherheit sollte fest in die Plattform integriert sein, anstatt von jeder Person, die eine App entwickelt oder einen Agenten nutzt, korrekt umgesetzt werden zu müssen.

Entstanden ist eine Plattform, die auf das Unternehmen zugeschnitten ist, das sie einsetzt. Sie können die Oberflächen individuell gestalten, Ihre Werkzeuge integrieren und Skills sowie Kontext ergänzen, die die Arbeitsweise Ihrer Organisation widerspiegeln.

## **Wir präsentieren: Cloudflare OS**

Wie viele andere KI-Tools startet auch Cloudflare OS mit einer Unterhaltung im Browser. Was es unterscheidet: Jede Unterhaltung ist im kuratierten Kontext und in den Skills Ihrer Organisation verankert. Definieren Sie ein Ziel für Ihren Workspace, und er nutzt dieses Wissen sowie die vorhandenen Tools und Daten Ihrer Organisation, um darauf hinzuarbeiten.

Cloudflare OS kombiniert drei Teile:

  * **Ein Agenten-Workspace** , der im Kontext und den Skills, die Ihr Unternehmen kuratiert, verankert ist, mit einer isolierten Laufzeitumgebung, in der Agenten Code schreiben und ausführen können.
  * **Ein neues Sicherheits- und Governance-Framework** für den sicheren Zugang zu internen Daten und Diensten.
  * **Eine Plattform für persönliche, anpassbare Apps** , die Nutzer erstellen, teilen und weiter verändern können.



Was als Gespräch beginnt, kann zu einem Dokument, einer App oder einem Workflow werden, der weiterhin die Arbeit erledigt.

## **Ein Agenten-Workspace für alle in Ihrem Unternehmen**

Agenten-Workspaces wurden so konzipiert, dass sie von allen in Ihrer Organisation genutzt werden können. Sie interagieren direkt im Browser mit ihnen, sodass Sie weder Entwickler sein noch wissen müssen, wie man ein Terminal verwendet. 

Ein Workspace kombiniert Agenten-Sessions, dauerhaft gespeicherten Zustand, Outputs und Dateien, den Zugriff auf Ressourcen sowie eine isolierte Runtime, in der der Agent Code erstellen und ausführen kann.

Sie enthalten bereits den kuratierten Kontext und die Skills, die Ihr Team oder Unternehmen aufgebaut hat. Das erspart doppelte Arbeit: Findet jemand den optimalen Weg für eine Aufgabe, können alle anderen ihn ebenfalls nutzen. Prozesse, Terminologie und bewährte Vorgehensweisen müssen einem Modell nicht jedes Mal aufs Neue vermittelt werden.

Einige Dinge, die Sie tun können:

### **Recherchieren und Fragen stellen**

Lassen Sie einen Workspace ein Thema auf Basis des Unternehmenskontexts und der bereitgestellten Ressourcen recherchieren. Der Agent kann dabei Code erstellen, um Informationen zu durchsuchen, zu filtern, zu verknüpfen und auszuwerten, statt den vollständigen Datensatz in das Kontextfenster des Modells zu übernehmen.

### **Dokumente, Präsentationen und Tabellen erstellen**

Ein Workspace kann die Ergebnisse seiner Recherche in ein Dokument, eine Präsentation oder eine Tabelle überführen, die Sie anschließend weiter bearbeiten können. Diese Ausgaben sind nicht auf statische Dateien beschränkt. Sie können mit Live-Daten verknüpft bleiben, sich bei Änderungen der zugrunde liegenden Quellen aktualisieren und trotzdem in bekannte Formate oder zu Diensten wie Google Drive exportiert werden.

### **Kollaborative, vernetzte Apps für Ihr Team erstellen**

Wenn ein Dokument oder eine Tabelle nicht ausreicht, kann der Agent eine App mit eigener Oberfläche, Logik und Zustand erstellen. Die App kann verbundene Unternehmensressourcen nutzen und die Zusammenarbeit mehrerer Personen unterstützen.

### **Deterministische Workflows ausführen**

Nicht für jede Aufgabe ist eine komplette Agenten-Session notwendig. Viele folgen einer bekannten Schrittfolge und benötigen nur an wenigen Stellen eine Einschätzung. Ein Arbeitsbereich kann daraus größtenteils deterministische Workflows erstellen: Code übernimmt die vorhersehbare Schritte, während ein Modell nur dort zum Einsatz kommt, wo es sinnvoll ist. Diese Workflows können bei Bedarf, nach Zeitplan oder durch ein Ereignis in einem angebundenen System ausgelöst werden.

Cloudflare OS bietet Agenten und Apps einen kontrollierten Zugriff auf maßgebliche Datensysteme über Gatekeeper (mehr dazu im untenstehenden Abschnitt zur Sicherheit). Darüber hinaus unterstützt es die bereits in Ihrer Organisation eingesetzten[ Model Context Protocol](https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro) (MCP)-Server über[ MCP Server Portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/).

## **Ein neues Sicherheits- und Governance-Framework für den sicheren Zugang zu internen Daten und Diensten**

Sobald Mitarbeitende anfangen, KI bei der Arbeit auszuprobieren, fragen sie häufig als Erstes nach API-Schlüsseln für interne Systeme. Das ergibt Sinn: Ohne Zugriff auf die Systeme, mit denen Menschen ihre Arbeit erledigen, kann KI im Unternehmenskontext nur wenig bewirken.

Aber das Weitergeben von API-Schlüsseln an Personen und Agenten ist gefährlich und nicht skalierbar. Schlüssel bieten oft weitreichende, langfristige Zugriffsrechte, die schwer einzuschränken, sicher zu teilen und zu überprüfen sind.

MCP bietet Agenten eine bessere Möglichkeit, diese Systeme zu nutzen. Ein MCP-Server kann die Zugangsdaten verwahren und eine klar definierte Auswahl an Tools bereitstellen, anstatt den Schlüssel direkt an den Agenten weiterzugeben. Doch zu steuern, welche Tools ein Agent aufrufen darf, ist nur der erste Schritt. MCP allein zeigt uns nicht, welche zugrunde liegenden Ressourcen ein Agent bereits eingesehen hat. Ein Agent kann Informationen aus mehreren Systemen kombinieren, sie an einen weniger geschützten Ort senden oder sie über Apps und Ausgaben Personen zugänglich machen, die die ursprünglichen Ressourcen möglicherweise nicht sehen dürfen. Autorisierung muss daher auch berücksichtigen, wohin Daten anschließend gelangen können.

### **Agenten beginnen ohne Zugriff**

[ Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/) steuert, wer auf Cloudflare OS zugreifen kann. Innerhalb der Plattform startet jeder Agent und jede App ohne jegliche Zugriffsrechte. Ein Agent kann den Zugriff auf eine bestimmte Ressource anfordern, den Sie gewähren oder verweigern können. Generierter Code erhält diese Ressource als typisierte Bindung:

`env.PROJECT` ist eine Capability, die die Berechtigung repräsentiert, eine bestimmte Ressource unter einer bestimmten Richtlinie zu verwenden. Die eigentlichen Zugangsdaten bleiben vollständig vom Agenten und jeglichem generierten Code isoliert.

Der serverseitige Code läuft in einem Dynamic Worker mit global deaktiviertem ausgehendem Netzwerkzugriff. Der clientseitige Code wird in einem abgeschotteten Browser-Frame ausgeführt. Beide können das Internet ausschließlich über Capabilities erreichen, die Sie explizit freigeben.

### **Gatekeeper verwalten Ressourcen und Aktionen**

Ein Gatekeeper ist ein dienstspezifischer[ Worker](https://developers.cloudflare.com/workers/?_gl=1*1pzndf6*_gcl_au*MzM2MDkxNTQzLjE3ODQ4NDczOTM.*_ga*MWVkZWU3OTctMzJjNC00YWE1LWI2ZDUtZTJkNTY1NzYxYWQ0*_ga_SQCRB0TXZW*czE3ODUyMTk3NjMkbzckZzAkdDE3ODUyMTk3NjMkajYwJGwwJGgwJGRQeHAyTUEtdzgtVUFETUEzOGwtVFVhajVDd2laRWYxSC1R), der zwischen dem Cloudflare-OS und einem externen Dienst sitzt. Er versteht die API des Dienstes, dessen Ressourcen und die darauf ausführbaren Operationen.

Vollzugriff auf Ihr gesamtes GitHub-Konto wäre für einen Agenten in der Regel zu umfassend. Ein Gatekeeper kann stattdessen nur ein bestimmtes Repository freigeben, das Lesen von Issues erlauben, Quellcode jedoch sperren, einzelne Felder ausblenden, Zugriffsraten begrenzen und vor dem Zusammenführen eines Pull Requests eine Genehmigung einfordern.

Der Agent und seine Apps sehen lediglich eine schlanke TypeScript-API. Der Gatekeeper übernimmt die[ OAuth](https://www.cloudflare.com/learning/access-management/what-is-oauth/)-Abwicklung, verwahrt die Zugangsdaten, setzt Richtlinien durch, protokolliert, welche Daten gelesen wurden, und vermittelt alle Vorgänge mit nach außen sichtbaren Auswirkungen.

### **Richtlinien richten sich danach, was der Agent gesehen hat**

Es reicht nicht aus, nur den ursprünglichen Lesezugriff zu kontrollieren. Nehmen wir etwa den Fall, dass ein Agent eine sensible Tabelle in einem Data Warehouse liest und daraus ein Live-Dashboard erstellt. Das Teilen dieses Dashboards darf nicht dazu führen, dass Personen Zugriff auf die zugrunde liegende Tabelle erhalten, obwohl sie direkt nicht darauf zugreifen dürften.

Jede Ressource, die ein Agent beobachtet, wird von Cloudflare OS erfasst. Diese Informationen bleiben an den Agenten und seine Arbeit gebunden. Versucht eine andere Person, den Arbeitsbereich zu öffnen, mit dem Agenten zu interagieren oder dessen Ergebnisse einzusehen, verifizieren Gatekeeper den Zugriff dieser Person auf die zuvor beobachteten Ressourcen.

Dasselbe Beobachtungsprotokoll fließt auch in Richtlinien ein, die festlegen, wann Agenten externe Anfragen stellen dürfen. Hat ein Agent sensible Daten gelesen, kann dies verhindern, dass er Daten an bestimmte Ziele schreibt, neue Mitwirkende einlädt, Arbeit an einen anderen Agenten übergibt oder eine ausgehende Anfrage sendet.

Menschen, die Agenten verwenden oder Apps entwickeln, müssen diese Fehler nicht selbst verhindern. Die Plattform übernimmt das nun.

## **Eine Plattform zum Erstellen und Teilen persönlicher, modifizierbarer Apps**

Die meisten Produktivitätssuiten bieten Ihnen einen festen Satz von Anwendungen: Dokumente, Tabellenkalkulationen und Präsentationen. In Cloudflare OS kann jede „Datei“ ihre eigene Anwendung sein, die von einem Agenten für eine Person, ein Projekt oder ein Team erstellt wurde.

Dabei handelt es sich nicht um Prototypen, die Sie exportieren und an anderer Stelle bereitstellen müssen. Jede dieser Anwendungen ist eine vollständige Full-Stack-Anwendung mit Client-Code, Server-Code, API und dauerhaftem Zustand. Apps sind standardmäßig privat, können aber wie Dokumente geteilt werden.

### **Jede App ist ein Worker**

Wenn Sie Ihren Workspace bitten, eine App zu erstellen, schreibt der Agent zwei Teile:

  * Client-Code, der die Benutzeroberfläche der App im Browser rendert
  * Server-Code, der den Zustand speichert und das Verhalten der App implementiert



Der Server wird bei Bedarf als[ Dynamic Worker](https://developers.cloudflare.com/dynamic-workers/) geladen und als[ Durable Object Facet](https://developers.cloudflare.com/dynamic-workers/usage/durable-object-facets/) instanziiert – beides Funktionen, die wir für dieses Projekt entwickelt haben. Das Facet stellt der App eine eigene SQLite-Datenbank zur Verfügung, getrennt von der Cloudflare-OS-Laufzeit, die sie verwaltet. Dynamic Workers verwenden schlanke V8-Isolates, sodass jede App eine eigene isolierte Laufzeit erhalten kann, ohne dass dafür dauerhaft ein eigener Server oder Container bereitstehen muss.

Der Browser-Client kommuniziert mit dem Server über[ Cap’n Web](https://github.com/cloudflare/capnweb), das Open-Source-RPC-System von Cloudflare, auf Basis von Object Capabilities. Eine Servermethode kann vom Client wie eine normale JavaScript-Funktion aufgerufen werden:

Das Besondere ist, dass der Agent auch dieselbe Methode aufrufen kann.

**Wenn Sie ein Tool erstellen können, das eine bestimmte Aufgabe übernimmt, können Agenten dieses Tool verwenden, um die Aufgabe in Ihrer Abwesenheit zu erledigen.**

### **Teilen Sie die App oder erzählen Sie, wie sie entwickelt wurde**

Wenn Sie eine App in Cloudflare OS erstellen, haben Sie zwei Möglichkeiten, sie zu teilen:

  * Durch das Teilen Ihrer App selbst können andere Personen in Echtzeit mit demselben Zustand zusammenarbeiten.
  * Wenn Sie den Blueprint Ihrer App teilen, können andere Personen ihre eigene Kopie der App erstellen.



Eine App, die aus einem Blueprint instanziiert wird, enthält den Code der ursprünglichen App. Aber sie enthält nicht ihre SQLite-Daten, Gesprächsverlauf, Anmeldedaten oder verbundene Ressourcen. Jede neue App beginnt mit einem unabhängigen Zustand und Ressourcen.

Das bedeutet, dass Ihr Team, wenn Sie Apps teilen, diese selbst mit KI anpassen kann, anstatt ein Feature Request einreichen und Ihnen zuweisen zu müssen.

## **Verwenden Sie jedes beliebige Modell und kontrollieren Sie die Kosten.**

Cloudflare OS kann mit jedem Modell verwendet werden. Jeder Inferenzaufruf läuft durch[ Cloudflare AI Gateway](https://developers.cloudflare.com/ai-gateway/), wodurch Ihre Organisation an einem Ort entscheiden kann, welche Modelle verfügbar sind sowie welches Modell jede Aufgabe übernehmen soll.

Nicht jede Aufgabe erfordert das teuerste Modell. Für die morgendliche Zusammenfassung Ihrer ungelesenen E-Mails möchten Sie vermutlich nicht jedes Mal das teuerste Frontier-Modell einsetzen. AI Gateway gibt Ihnen die nötige Kontrolle, damit kostspielige Modelle nur für die anspruchsvollsten Aufgaben verwendet werden.

Jede Anfrage wird der Person, dem Team oder dem Arbeitsbereich zugeordnet, von dem sie stammt. Administratoren können sehen, wofür Inferenzkosten anfallen, Budgets und Rate Limits festlegen und bestimmen, was geschieht, wenn ein Limit erreicht wird.

## **Open Source, damit Sie es zu Ihrem eigenen machen können**

Cloudflare OS ist ab sofort verfügbar und ist Open Source. Sehen Sie sich das[ cloudflare-os GitHub-Repository](https://github.com/cloudflare/cloudflare-os) an. Sie können es in Ihrem eigenen Cloudflare-Konto bereitstellen und Ihre eigenen Access-Richtlinien, AI Gateway-Konfigurationen, Daten und Integrationen verwenden.

Unsere interne Bereitstellung spiegelt die Systeme, Terminologie, Richtlinien und Arbeitsweisen von Cloudflare wider. Ihre Bereitstellung sollte entsprechend Ihre eigene Organisation widerspiegeln.

Cloudflare OS ist so konzipiert, dass Sie die Oberfläche anpassen, interne Gatekeepers hinzufügen und organisationsspezifische Funktionen entwickeln können, ohne das Kernprodukt zu ändern.

Wir veröffentlichen zwei Repositorys: den[ Cloudflare OS-Kern](https://github.com/cloudflare/cloudflare-os) und eine[ beispielhafte Bereitstellung](https://github.com/cloudflare/cloudflare-os-starter), basierend auf unserer internen Nutzung bei Cloudflare. Das Bereitstellungs-Repository nutzt den Kern, ohne ihn zu patchen, und bietet Raum für Konfiguration, individuelle Benutzeroberflächen, interne Integrationen, Analysen und Bereitstellungspipelines.

## **Zusammen mit unseren Partnern bereitgestellt**

Der Quellcode ist nur der Ausgangspunkt. Der Kontext, die Skills, die Workflows, die internen Systeme und die Richtlinien sind es, die Cloudflare OS für Ihre Organisation noch nützlicher machen.

Die strategischen Partner von Cloudflare, Presidio und Happy Cog, unterstützen Sie dabei, Cloudflare OS auf die Abläufe Ihrer Organisation zuzuschneiden und in Ihrer gesamten Belegschaft einzuführen.

Partner können Ihnen dabei helfen, gemeinsame Skills und institutionellen Kontext zu kuratieren, benutzerdefinierte Schnittstellen zu erstellen, interne Systeme über Gatekeeper und MCP Server Portale zu verbinden sowie Sicherheits-, Modell- und Kostenkontrollen zu konfigurieren.

Sie erhalten Cloudflare OS mit Ihrem eigenen Branding, das mit Ihren Systemen verbunden ist, auf Cloudflare läuft und auf die Arbeitsweise Ihrer Mitarbeitenden zugeschnitten ist.

## **Erste Schritte**

Cloudflare OS ist ab heute auf[ GitHub](https://github.com/cloudflare/cloudflare-os) verfügbar. Sie können den Quellcode erkunden, die Demo ausprobieren oder ihn in wenigen Minuten in Ihr eigenes Cloudflare-Konto bereitstellen, indem Sie unser[ Starter-Repository](https://github.com/cloudflare/cloudflare-os-starter) verwenden.

Wir fangen gerade erst an. Wir arbeiten daran, Cloudflare OS als vollständig verwaltetes Produkt in das Cloudflare-Dashboard zu integrieren, Container für Entwicklungsabläufe hinzuzufügen und Arbeitsbereiche in Slack und andere Chat-Tools zu bringen.

Wenn Sie daran interessiert sind, mit unserem Team zu sprechen, freuen wir uns auf ein Gespräch mit Ihnen. Kontaktieren Sie uns über[ dieses Formular](https://www.cloudflare.com/resource/cloudflare-os-interest-landing-page/)!

]]>01KZMPWQWC2T41G1VQDK7DCW60Der Agent Development Lifecycle ist bei Cloudflare angekommenhttps://blog.cloudflare.com/de-de/agent-development-lifecycle/ Fri, 07 Aug 2026 09:27:32 GMTAgenten können Code schneller schreiben, als Teams ihn prüfen, bereitstellen und warten können. Heute stellen wir den Agent Development Lifecycle sowie die zugrunde liegenden Cloudflare-Bausteine vor.Agent Development LifecycleAgentsAgents WeekAIBrowser RunCloudflare WorkersDevOps (DE)EntwicklerplattformMCPObservabilityProdukt-NewsTracingWorkflowsEngineering-Manager haben in den vergangenen Jahrzehnten Methoden entwickelt, die es vielen Entwicklerinnen und Entwicklern ermöglichen, gemeinsam an einer geteilten Codebasis zu arbeiten. Diese Arbeit reicht bis zum „Systems Development Lifecycle“ ([RAND, 1975](https://www.rand.org/pubs/reports/R1855.html)) zurück, der heute allgemein als „Software Development Lifecycle“ (SDLC) bezeichnet wird, der die folgenden Phasen definiert:

  * Plan (Planen)
  * Design (Designen)
  * Implement (Implementieren)
  * Test (Testen)
  * Deploy (Bereitstellen)
  * Maintain (Warten)
  * Retire (Stilllegen)



Durch KI ist aus dem zuvor zeitaufwendigsten und teuersten Schritt — der Implementierung — der schnellste und kostengünstigste geworden. Dadurch geraten die nachfolgenden Prozesse unter Druck, insbesondere die Personen, die die übrigen Phasen des SDLC verantworten. Betroffen sind sowohl Open-Source-Maintainer, die von Tausenden Pull Requests und Fehlermeldungen überrollt werden, als auch Production Engineers, die Produktionsumgebungen stabil halten müssen, während die Auslieferungsrate von Software um Größenordnungen steigt.

Wir alle versuchen, unsere Systeme, unsere Kunden und uns selbst vor Nachlässigkeit zu bewahren.

Die Lösung besteht — so paradox es klingt — darin, Agenten mehr Verantwortung zu übertragen. Das ist nur fair! Kein Team würde einem Entwickler erlauben, ausschließlich Code zu schreiben, während andere ihn prüfen, zusammenführen, deployen, den Bereitschaftsdienst in der Produktion übernehmen und neue Bugs sichten. Genau das tun die meisten Unternehmen derzeit jedoch mit Agenten. Die Modelle haben sich enorm verbessert, und Agenten können über längere Zeiträume arbeiten und wesentlich umfangreichere Aufgaben bewältigen. Über die verschiedenen Phasen des SDLC hinweg werden sie bislang jedoch noch sehr ungleich eingesetzt.

Bei Cloudflare behandeln wir Agenten als unsere Kundschaft. Sie können [Domains kaufen](https://blog.cloudflare.com/agents-stripe-projects/), [temporäre Konten erstellen](https://blog.cloudflare.com/temporary-accounts/) und [die gesamte Cloudflare API nutzen](https://blog.cloudflare.com/code-mode-mcp/). Wir wissen, dass Agenten APIs und Tools benötigen, um den gesamten SDLC im Namen unserer Kunden verwalten zu können – und nicht lediglich die ersten Schritte.

Aus diesem Grund führen wir heute die ersten Werkzeuge einer neuen Tool-Suite ein, die Agenten dabei unterstützt, nicht nur Code zu erzeugen, sondern größere Teile des SDLC zu übernehmen. Dabei geben wir Einblick in das, was wir beim Aufbau unserer eigenen Lösung entwickelt und gelernt haben:

  * [**@cloudflare/ci**](https://blog.cloudflare.com/ci-workflows) — eine neue Möglichkeit, CI/CD über Millionen von Repositories hinweg auszuführen. Das System kann sich selbst reparieren, Agenten für deutlich komplexere Aufgaben starten und basiert auf Cloudflare Workflows.
  * [**OpenTelemetry-Traces für die lokale Entwicklung**](https://blog.cloudflare.com/local-tracing) — sie bieten Agenten dieselben Einblicke wie im Produktivbetrieb und sind in Wrangler sowie das Cloudflare-Vite-Plugin integriert.
  * [**Wir präsentieren: Cloudflare Agents und Agent Traces**](http://blog.cloudflare.com/agents-on-cloudflare) – eine zentrale Umgebung zum Beobachten, Warten und Verbessern von Agenten auf Basis ihrer OpenTelemetry-Traces.
  * [**Wie Cloudflare Engineering-Standards mit KI durchsetzt:**](http://blog.cloudflare.com/engineering-standards-enforcement) unsere Erfahrung damit, Best Practices über die Repositories und Spezifikationen all unserer Produkte und Systeme hinweg durchzusetzen.
  * [**Wie wir eine Softwarefabrik gebaut haben, um die Zahl der GitHub-Issues bei Astro auf null zu senken:**](https://blog.cloudflare.com/astro-issue-triage) unsere Erfahrung mit Systemen, die Issues für ein großes und wachsendes Open-Source-Projekt automatisch triagieren, reproduzieren, verifizieren und beheben.



Aber es geht um mehr als einzelne Tools. Der SDLC wurde für eine andere Geschwindigkeit gebaut. Selbst mit starker Automatisierung skaliert er nicht mit der Code-Menge, die Agenten erzeugen können, und mit dem Tempo, in dem Softwareteams heute arbeiten müssen, um wettbewerbsfähig zu bleiben. Deshalb ist es aus unserer Sicht Zeit für den ADLC: den Agent Development Lifecycle.

## Der SDLC passt zu Softwareteams. Der ADLC passt zu Softwarefabriken.

Derzeit [sprechen](https://x.com/zachlloydtweets/status/2069789929073262945) [viele](https://x.com/matanSF/status/2066578088184680920) [über](https://x.com/dexhorthy/status/2081797628552270027) [den](https://x.com/bcherny/status/2077929390806073807) [Bau von](https://x.com/gokulr/status/2032271386161684665) „Softwarefabriken“: Systeme, in denen Agenten aus einer Eingabe eigenständig Software bauen, verbessern, deployen und betreiben. Diese Eingabe kann ein Produktionsfehler sein, ein Bug-Report aus dem Support oder eine neue Feature-Idee. Im Idealfall übernimmt ein Agent den gesamten Ablauf.

In der Praxis hängen die meisten Projekte aber weiterhin an Human-in-the-Loop-Schritten. Menschen prompten Agenten, schieben sie an, lassen sie Review-Feedback einarbeiten, beaufsichtigen mehrere Agenten parallel und geben immer neue Anweisungen. Damit bleibt der Mensch der Manager jedes SDLC-Schritts. Nur die einzelnen Aufgaben innerhalb dieser Schritte werden an Agenten ausgelagert.

Softwarefabriken stellen deshalb eine größere Frage: Was passiert, wenn wir nicht einzelne Aufgaben, sondern den gesamten Prozess neu bauen? Wie schaffen wir mehr Raum für das, was Menschen wirklich beitragen: Inspiration, Geschmack und Urteilskraft? Dann bleibt mehr Zeit für Design, Kundengespräche und größere Ideen.

Eine Softwarefabrik deckt weiterhin die bekannten SDLC-Schritte ab, aber sie braucht eine Plattform, die wesentlich mehr leisten kann. Sobald der Agent das Steuer übernimmt, müssen alle bisher manuellen Schritte so umgebaut werden, dass sie für Agenten funktionieren (und nicht mehr auf Menschen angewiesen sind):

  * **Programmatisch** — ClickOps war für Menschen schon fragwürdig. Für Agenten funktioniert es gar nicht. Jede Operation braucht eine API, die Agenten verlässlich aufrufen, debuggen und nutzen können.
  * **Horizontal skalierbar** — Preview-Deployments waren praktisch, solange Menschen auf Bildschirme schauten oder Staging-Server manuell übernahmen, um Probleme vor der Produktion zu finden. Damit Agenten steuern können, braucht jeder Agent eine eigene Preview, die der Produktion entspricht.
  * **Reproduzierbar** — Manche Bugs treten nur unter bestimmten Bedingungen auf, etwa bei simuliertem 4G auf einem iPhone 15 oder aus einem bestimmten Land. Klassische Unit- und Integrationstests decken solche Fälle nicht ausreichend ab.
  * **Echtzeitfähig, push-basiert** – Dashboards funktionieren nicht, wenn niemand aktiv hinschaut. Ein Ereignis (Event) muss den Agenten automatisch auslösen.
  * **Atomar** – Jede Änderung muss separat testbar, auslieferbar, beobachtbar und rückgängig machbar sein (ohne anderes Verhalten zu beeinflussen).
  * **Berechtigungsbasiert** — Menschen erhalten manchmal SSH-Zugriff auf Produktion, wenn es kritisch wird. Agenten dürfen diesen Zugriff nicht einfach bekommen. Trotzdem brauchen sie kontrollierte Eskalationswege.
  * **Selbstverbessernd** – Menschen lernen aus Erfahrung. Beim ersten Ship oder der ersten On-Call-Schicht sind sie langsam und müssen anderen über die Schulter schauen. Danach werden sie besser und schneller. Auch Agenten brauchen Wege, aus Erfahrung zu lernen.



Damit Softwarefabriken echte Produktionssoftware sicher betreiben können, brauchen wir ein neues Fundament. Die Herausforderung ähnelt der bei selbstfahrenden Autos: Sie müssen von „funktioniert in 80 Prozent der Fälle“ zu Zuverlässigkeitswerten weit über 99 Prozent kommen.

## Wer Agenten den SDLC steuern lässt, darf ihnen kein Fahrzeug geben, das für Menschen entworfen wurde.

Ein autonomes Fahrzeug ist mit Sensoren und Technologien ausgestattet, die ein gewöhnliches Auto nicht hat. Lidar-Sensoren, Kameras, leistungsstarke Compute-Ressourcen für Inferenz und Konnektivität zu einem zentralen Kommandosystem, das bei Bedarf aus der Ferne übernehmen kann.

Damit ein autonomes Fahrzeug 80 Prozent so gut fährt wie ein Mensch, bräuchte es vermutlich nicht all das. Selbstfahrende Systeme waren schon vor zehn Jahren ungefähr 80 Prozent so gut wie Menschen. Aber das ist nicht die Messlatte. Die Messlatte ist, deutlich besser und sicherer als ein menschlicher Fahrer zu sein. Genau das erwarten wir, wenn wir einer Maschine die Schlüssel übergeben und uns sicher genug fühlen wollen, auf dem Highway 101 bei 60 mph ein Nickerchen zu machen. Genau deshalb verfügen autonome Fahrzeuge über speziell für autonomes Fahren entwickelte Technologie: Sie schafft Vertrauen und bewältigt Edge Cases, die sich nicht vollständig im Voraus planen lassen.

Bei selbstfahrender Software ist es genauso. Warum lassen Sie Ihren Agenten seine eigenen PRs für Produktionsservices _noch nicht_ automatisch genehmigen und mergen? Wahrscheinlich fallen Ihnen sofort viele Gründe ein. Und je wichtiger das System ist, desto länger wird diese Liste.

Denn es geht nicht nur darum, katastrophale Fehler zu verhindern. Es geht auch darum, wirklich das Richtige für Kundinnen und Kunden zu bauen. Das ist zu komplex für eine lineare Schrittfolge in einer GitHub Actions YAML-Datei. Auch klassische automatisierte Tests reichen nicht aus. Schon eine kleine Dashboard-Änderung kann Rollen, Spezialgebiete und Organisationsstrukturen berühren. Subjektive Änderungen sind besonders schwer zu testen und zu delegieren. Heute steckt vieles davon wahrscheinlich nicht in Ihrer CI/CD-Pipeline. Wenn Agenten die Softwarefabrik steuern sollen, muss genau das aber Teil des Systems werden.

Wenn Agenten den ganzen Prozess übernehmen sollen, brauchen wir eine bessere Art, dynamische Schrittketten zu orchestrieren. Aus unserer Sicht ist das ein [Workflow](https://blog.cloudflare.com/ci-workflows), der Container, Agenten und Browser starten kann. Ein solcher Workflow kann Feature Flags setzen, sie für Testnutzer aktivieren, Logs und Traces auswerten, Produktionsmetriken beim schrittweisen Rollout beobachten und alles koordinieren, was für eine sichere Bereitstellung nötig ist.

## Eine CI/CD-Pipeline ist im Grunde nur ein Workflow. Aber ein Workflow kann weit mehr leisten.

[Cloudflare Workflows](https://developers.cloudflare.com/workflows/) verketten Schritte, wiederholen fehlgeschlagene Aufgaben automatisch und speichern Zustand für Minuten, Stunden oder Wochen. So lassen sich komplexe, dynamische Geschäftsprozesse als logisches Programm beschreiben. [Dieser Beitrag](https://blog.cloudflare.com/ci-workflows) zeigt, warum Workflows gemeinsam mit [Artifacts](https://blog.cloudflare.com/artifacts-git-for-agents-beta/) CI/CD-Pipelines wesentlich einfacher definierbar und auslösbar machen. Ein Beispiel:

Workflows sind nicht auf lineare Schrittfolgen beschränkt. Sie lassen sich [dynamisch definieren](https://blog.cloudflare.com/dynamic-workflows/) und können Agenten oder weitere Workflows starten. [Das Beispiel](https://flueframework.com/docs/guide/workflows/#example-cloudflare-workflows) zeigt einen Workflow, der neue Daten der letzten 24 Stunden überprüft. Der Workflow steuert, wann und wie der Agent gepromptet wird, und gibt Kontext von Schritt zu Schritt weiter.

Sobald man dieses Muster verstanden hat und so von Workflows überzeugt ist wie Cloudflare, stellt sich fast automatisch die Frage: Was könnte ein Workflow noch für mich erledigen? Welche menschlichen Engpässe lassen sich an Workflow plus [Flue-Agenten](https://flueframework.com/) delegieren?

## Der vollständige ADLC auf dem Cloudflare-Stack

[Workflows](https://developers.cloudflare.com/workflows/) orchestrieren komplexe Schritte, [Artifacts](https://developers.cloudflare.com/artifacts/) speichern Code. Zusammen ergibt das auf Cloudflare die Grundlage, mit der Agenten den gesamten Weg vom Bauen über die Bereitstellung bis zur Wartung von Software übernehmen können.

## Grundbausteine für den Aufbau Ihrer Softwarefabrik

Die Menschen an der vordersten Entwicklungsfront bauen heute die Softwarefabriken von morgen. Mit der Zeit werden Softwarefabriken so selbstverständlich werden wie Agenten und KI: eine normale Art, Software zu bauen. Aber für die meisten Menschen und Organisationen ist dieser Punkt noch nicht erreicht.

Wir wollen das ändern.

Unsere Leitfragen waren: Wie machen wir diesen Wandel einfach und zugänglich, damit alle im Internet davon profitieren können? Und welche Basis-Bausteine können wir öffnen, egal ob für ein kleines Startup oder eine der größten Plattformen der Welt?

Wir glauben: Die Bausteine sind jetzt vorhanden. Es bleibt Arbeit, sie weiter zu verbinden, unsere eigene Softwarefabrik auszubauen und aus ihr zu lernen. Doch ab heute können Sie auf Cloudflare Ihre Maschine bauen, die die Maschine baut. Starten Sie mit [@cloudflare/ci](https://blog.cloudflare.com/ci-workflows), [bauen Sie einen Agenten](http://blog.cloudflare.com/agents-on-cloudflare) und sehen Sie, wie viel des SDLC Sie automatisieren können.

]]>01KZD1WFGKFNJF24D3PMAPF8NYWir präsentieren Cloudflare Wallets: eine programmierbare Geldbörse für das agentenbasierte Internethttps://blog.cloudflare.com/de-de/wallets/ Fri, 07 Aug 2026 03:55:38 GMTCloudflare Wallets werden KI-Agenten native Zahlungen und überprüfbare Identität im Web ermöglichen. Mit dem x402-Protokoll können Agenten APIs und Inhalte autonom kaufen, innerhalb klar definierter Sicherheitsleitplanken.Agents WeekAIAI Bots (DE)EntwicklerEntwicklerplattformPaymentsProdukt-Newsx402Neue APIs auszuprobieren, ist für KI-Agenten heute unnötig kompliziert. Sie treffen auf Login-Seiten für Menschen, brauchen menschliche Hilfe beim Hinzufügen einer Zahlungsmethode, müssen API-Schlüssel erzeugen und dann erst herausfinden, wie die API überhaupt genutzt wird.

Dieser Ablauf ist für Agenten aus zwei Gründen schwierig: Sie haben keine stabile Kennung, mit der sie sich für eine API registrieren können, und sie haben keine native Möglichkeit, APIs zu bezahlen. Weil ihnen diese Grundlagen fehlen, scheitert häufig schon das Onboarding in Software. Das begrenzt das Wachstum von Agentic Commerce. KI-Agenten brechen solche Aufgaben oft ganz ab und geben Registrierung, Zahlungsmethoden und API-Schlüsselerstellung wieder an Menschen zurück. Dadurch wird es für Agenten sehr schwierig, viele APIs auszuprobieren und miteinander zu vergleichen.

Um dieses Problem zu lösen, haben wir Cloudflare Wallets entwickelt. Ab heute können Sie einen[ Cloudflare Wallet handle](https://cloudflare.pay) für Ihr Konto reservieren. Dieser stellt einen eindeutigen Nutzernamen bereit, über den Sie leichter mit Anbietern in Kontakt treten können. Bald werden Sie Ihre Cloudflare Wallet einrichten und nutzen können, um APIs und Inhalte zu bezahlen.

Anfang des Monats haben wir[ Monetization Gateway](https://blog.cloudflare.com/monetization-gateway/) angekündigt, damit Cloudflare-Kundinnen und -Kunden Zahlungen für ihre Websites und Anwendungen erhalten können. Monetization Gateway wird Micropayments über das[ x402-Protokoll](https://www.x402.org/) unterstützen. Damit können Zahlungen an HTTP-Requests angehängt werden.Diese Micropayments können Anwendungsfälle von KI-Inferenz über Daten bis hin zu Inhalten bezahlen. Wenn Sie für Services hinter Monetization Gateway und anderen[ x402-kompatiblen Endpunkten](https://developers.cloudflare.com/agents/tools/payments/x402/) bezahlen oder Zahlungen dafür erhalten möchten, brauchen Sie eine Wallet. 

Mit Cloudflare Wallets können Sie Stablecoins speichern, Services kaufen und Zahlungen im Web empfangen. Jedes Konto mit einer Wallet kann außerdem Virtual Wallets für seine Agenten erstellen, damit diese APIs, MCP Tools, Inhalte und mehr kaufen können. Für Virtual Wallets können Sie Guardrails definieren, etwa ein Budget, eine Allowlist und eine maximale Transaktionsgröße. So kann Ihr Agent kontrolliert und sicher Mittel aus Ihrem Konto verwenden. Dadurch kann Ihr Agent viele APIs mit wenig Reibung und kontrolliertem Risiko ausprobieren. Wallet-Nutzende können ihren Cloudflare Wallet handle optional teilen und erhalten so eine stabile Identität bei der Interaktion mit Anbietern.

## **Den zweiseitigen agentenbasierten Markt aufbauen**

[ Monetization Gateway](https://blog.cloudflare.com/monetization-gateway/) von Cloudflare wird es berechtigten Cloudflare-Kundinnen und -Kunden ermöglichen, ihre Ressourcen, etwa Inhalte oder APIs, headless an agentenbasierte Käufer zu verkaufen. Damit sich dieser Markt wirklich entwickeln kann, brauchen Agenten jedoch mehr Tools, um auf maschinen-native Weise bei Anbietern zu kaufen. Wallets ergänzen das Agents SDK von Cloudflare um ein weiteres Tool. Damit können KI-Agenten benötigte APIs und Inhalte einfach per Micropayments kaufen.

Es wird zwei Arten von Cloudflare Wallets geben: Account Wallets und Virtual Wallets.

**Account Wallets (Konto-Wallets)** sind für Menschen konzipiert, die Eigentümer und Nutzer von Cloudflare-Konten sind. Sie können Geld hinzufügen, Ausgaben an von Agenten verwaltete Virtual Wallets delegieren und Guthaben bei Bedarf wieder entfernen. 

**Virtual Wallets** hingegen sind für Agenten ausgelegt und funktionieren über API-Schlüssel. Innerhalb einer Virtual Wallet kann ein Agent Geld entsprechend seinen Berechtigungen ausgeben. Die maximalen Ausgaben werden durch das Limit begrenzt, das die Inhaberin oder der Inhaber der Account Wallet festlegt. Dieses Modell gibt Agenten die Freiheit, im Namen von Nutzenden zu handeln, ohne für jede Aktion manuelle Freigaben zu benötigen. Gleichzeitig begrenzt es die Möglichkeit, zu viel auszugeben.

## **Die Freiheit zum Erkunden**

Virtual Wallets sind deshalb so interessant, weil sie Agenten Raum zum Erkunden geben. Sie können Dutzende oder Hunderte Services testen und herausfinden, welcher für einen bestimmten Use Case am besten passt. Stablecoin-Micropayments über x402 machen API-Tests ohne Konto einfach. Agenten können neue Optionen mit sehr wenig Reibung ausprobieren. Die Ausgabenlimits der Virtual Wallets schaffen dabei einen sicheren Rahmen. Auf den ersten Blick wirken Limits wie Einschränkungen. Tatsächlich geben sie Agenten mehr Freiheit. Wenn ein Agent nur 10 US-Dollar ausgeben kann, ist das Risiko überschaubar. Und wenn ein API-Test nur wenige Cent kostet, reichen 10 US-Dollar für viele Vergleiche. Sobald eine API ausgewählt ist, sorgen Ihre Account-Wallet-Richtlinien für Kostenkontrolle.

Sobald Sie oder Ihr Agent eine API zur Nutzung ausgewählt haben, dienen die von Ihnen in Ihrem Account Wallet festgelegten Richtlinien als Kostenkontrollen für Virtual Wallets. Möchten Sie jedem Mitarbeitenden ein Budget von 100 USD pro Woche für die KI-Inferenz zur Verfügung stellen? Provisionieren Sie einfach ein Account Wallet mit dem richtigen Guthaben und erstellen Sie für jeden Mitarbeitenden ein virtuelles Wallet mit dieser Regel. Jeder, der die Limits seines virtuellen Wallet überschreitet,kann eine manuelle Ausnahme bei einer autorisierten Person anfordern, die berechtigt ist, Änderungen am Account Wallet vorzunehmen.

Wir möchten es Account Wallets erleichtern, flexible, aber verbindliche Ausgabenrichtlinien festzulegen, die keine tägliche aktive Überwachung erfordern. Wenn etwas Ungewöhnliches passiert, etwa unerwartet schnelle Ausgaben, kann ein Mensch prüfen und bestätigen, ob alles wie vorgesehen funktioniert. War die Ausgabe beabsichtigt, kann die Administratorin oder der Administrator der Account Wallet das Limit erhöhen oder einmalig zusätzliches Guthaben freigeben. War die Ausgabe unbeabsichtigt, haben die Ausgabenrichtlinien für das Hinzufügen von Guthaben zu Virtual Wallets ihre Aufgabe erfüllt, indem sie Limits durchgesetzt haben.

Wir arbeiten daran, das Aufladen und Nutzen dieser Wallets so einfach wie möglich zu machen. Wir beginnen mit einfachen Wegen, Guthaben in unterstützten Regionen ein- und auszuzahlen. Für berechtigte Nutzende wird Self-Funding über Stablecoins als Alternative verfügbar sein. Das Internet wird sich nicht über Nacht vollständig verändern. Aber da inzwischen[ ](https://radar.cloudflare.com/) [ein Großteil des Web-Traffics von Bots verursacht](https://radar.cloudflare.com/) wird, freuen wir uns, Agenten und Anbietern erstklassige Tools für agentic Commerce zu geben.

## **Über Zahlungen hinaus**

Es ist ein wichtiger erster Schritt, dass Menschen Agenten die Befugnis übertragen können, Services einfach zu kaufen und zu verkaufen. Für Anbieter ist aber nicht immer sichtbar, in wessen Auftrag ein Agent handelt. Kommt heute ein Agent auf Ihre Website, wissen Sie oft nur wenig über ihn, obwohl er im Auftrag einer Einzelperson oder Organisation handelt. Diese fehlende Zuordnung macht viele klassische Web-Geschäftsmodelle schwieriger. Kostenlose Testwochen oder Startguthaben funktionieren gut für Menschen und Organisationen. Bei Agenten ist das anders: Ihnen fehlt oft eine stabile Identität, und eine Person kann Dutzende Agenten kontrollieren.

Wir lösen dieses Problem, indem wir Wallets über[ ](https://cloudflare.pay/)[cloudflare.pay](http://cloudflare.pay) mit einem Cloudflare-Konto verknüpfen.[ ](https://cloudflare.pay/)[cloudflare.pay](http://cloudflare.pay) ermöglicht es Agenten, sich optional zu identifizieren, da ihre Identität vom Konto abgeleitet bzw. durch das Konto delegiert ist. Ein Research-Agent könnte zum Beispiel unter[ research.example.cloudflare.pay](http://research.example.cloudflare.pay) erreichbar sein. Anbieter erkennen dann, dass der Agent zu einer bestimmten Organisation gehört. So entstehen konsistente, dauerhafte Identitäten für Agenten. Ob Agenten ihre Identität offenlegen, bleibt vollkommen optional. Unternehmen können selbst entscheiden, ob sie Transaktionen mit bekannten Agenten priorisieren möchten.

## **Agenten-Identifiers sollten für Menschen lesbar sein**

Wir glauben, dass der Umgang mit Agenten dem Umgang mit VPNs ähneln wird: Wer nicht identifiziert ist, ist nicht automatisch nicht vertrauenswürdig, muss aber stärkere Vertrauenssignale liefern. Deshalb haben wir[ Turnstile](https://www.cloudflare.com/products/turnstile/) und andere Initiativen entwickelt, um Bots innerhalb von[ Bot Management](https://www.cloudflare.com/products/bot-management/) zu erkennen. Unser Identity baut auf diesen Vorarbeiten auf.[ Web Bot Auth](https://developers.cloudflare.com/bots/reference/bot-verification/web-bot-auth/) ermöglicht Agenten zum Beispiel bereits, ihre Identität über ein Schlüsselpaar zu registrieren. IDs, die mit Cloudflare Wallets verbunden sind, machen dieses Schlüsselpaar menschenlesbar.

Wir wissen, dass sich Standards für agentic Identity schnell verändern. Deshalb wollten wir unseren Ansatz einfach halten. Wir schlagen einen menschenlesbaren Identifier für ein schwer lesbares Schlüsselpaar vor, ähnlich wie die Zuordnung von URLs und IP-Adressen im[ DNS](https://www.cloudflare.com/learning/dns/what-is-dns/). Wir versuchen nicht, ein bestimmtes Schema oder ein anderes Verifizierungssystem zu definieren. Wir möchten Identität nur leicht merkbar und einfach deklarierbar machen. Wenn sich im Rahmen der Initiativen der[ x402 Foundation](https://blog.cloudflare.com/x402/) Schemas zur Anreicherung agentic Identity entwickeln, wollen wir sie übernehmen und auch andere dazu ermutigen, dasselbe zu tun.

## **Die Zukunft von agentic Commerce**

Bei Cloudflare möchten wir alle Bausteine für den Erfolg des agentic Commerce bieten. Monetization Gateway wird Verkäufern eine Möglichkeit bieten, bezahlt zu werden, ohne eine traditionelle Zahlungsinfrastruktur einzurichten. Wallets werden Käufern die Möglichkeit bieten, über Agenten ohne Benutzeroberfläche zu bezahlen. Identity wird es Händlern ermöglichen, mit Käufern zu kommunizieren, die sich identifizieren oder Identifikationsanforderungen durchsetzen.

Zusammen schaffen diese Bausteine einen headless-Marktplatz für das Internet. Wenn Sie das spannend finden und teilnehmen möchten,[ können Sie sich jetzt Ihren Handle sichern](https://cloudflare.pay/). Wir sind gespannt, was Sie entwickeln und monetarisieren.

]]>01KZD5KZCQG6AX2X2BSTBT068BEinführung der Billable Usage API: Programmatische Kostentransparenz für Cloudflarehttps://blog.cloudflare.com/de-de/billable-usage-api/ Thu, 06 Aug 2026 06:55:36 GMTCloudflare hat eine neue Billable Usage API für Konten eingeführt, die Entwicklern und FinOps-Teams über einen einzigen Endpunkt programmatische Transparenz über Kosten und Nutzung sämtlicher Self-Service-Produkte bietet. Die API basiert auf der FOCUS-Spezifikation und ermöglicht es, Kosten nahtlos gemeinsam mit dem übrigen Cloud-Stack zu verfolgen.Agents WeekAPIBillingEntwicklerProdukt-NewsTechnikBei der Agents Week geht es um einen Wandel, der bereits in vollem Gange ist: Agents schreiben Code, stellen Workers bereit und provisionieren in Ihrem Namen Infrastruktur. Dadurch verändert sich auch, welche Einblicke Sie benötigen. Wenn ein Programm in Ihrem Cloudflare-Konto Kosten verursacht, müssen Sie wissen, wofür diese anfallen – im Tagesverlauf, nach Produkt aufgeschlüsselt und in einem maschinenlesbares Format, das von einem anderen Programm verarbeitet werden kann. Für Menschen ist das Dashboard die richtige Lösung. Für Automatisierung ist es das nicht.

Deshalb führen wir für Self-Service-Konten eine neue **Billable Usage API** ein: Ein zentraler Endpunkt liefert Kosten- und Nutzungsdaten Ihres Kontos, aufgeschlüsselt nach Produkt und Servicezeitraum. Die API deckt sämtliche nutzungsbasierten Cloudflare-Produkte im Konto ab, darunter Workers, R2, D1, Workers AI, Vectorize, Images und Stream – alles mit nur einem Aufruf. Und wenn Sie bereits mit einer FinOps-Toolchain arbeiten, dürften Ihnen die Spaltennamen bekannt vorkommen.

Sie erhalten eine Rückmeldung mit einem `HTTP 200 OK` mit `Content-Type: application`/`json` und den Nutzungsdaten im Antworttext. Derzeit werden Nutzungs- und Kostendaten täglich aktualisiert, während wir daran arbeiten, diese künftig in nahezu Echtzeit bereitzustellen.

## **Was die API zurückliefert**

Jede Zeile in der Antwort entspricht einem Abrechnungszeitraum für ein Produkt auf Ihrem Konto.

  * `ServiceName` und `ServiceFamilyName` – welches Produkt („Workers Standard“ unter der Familie „Workers“, „R2 Storage“ unter „R2“, usw.).
  * `ChargePeriodStart` / `ChargePeriodEnd` — der Zeitraum, den diese Zeile abdeckt.
  * `PricingQuantity` und `ConsumedUnit `— wie viel Sie genutzt haben, in der Maßeinheit, auf der wir abrechnen (GB-Monate, GB-Sekunden, Anfragen usw.).
  * `ContractedCost` — wie viel dieser Zeitraum in `BillingCurrency` kostet.
  * `CumulatedPricingQuantity` und `CumulatedContractedCost` – laufende Summen für den Abrechnungszeitraum.
  * `ZoneId` / `ZoneName` – wenn die Nutzung einer bestimmten Zone zugeordnet wird.



Die meisten dieser Felder entsprechen direkt den Spalten der [FinOps Open Cost and Usage Specification (FOCUS)](https://focus.finops.org/). Wenn Ihr Team bereits FOCUS-Daten eines anderen Anbieters verarbeitet, werden Ihnen die Feldnamen und ihre Bedeutung vertraut sein.

**Cloudflare-Feld**| **FOCUS-Spalte**| **Anmerkungen**  
---|---|---  
`BillingCurrency`| `BillingCurrency`| genauer Treffer  
`BillingPeriodStart`| `BillingPeriodStart`| genauer Treffer  
`ChargePeriodStart` / `ChargePeriodEnd`| `ChargePeriodStart` / `ChargePeriodEnd`| genauer Treffer  
`ServiceName`| `ServiceName`| genauer Treffer  
`ConsumedQuantity` / `ConsumedUnit`| `ConsumedQuantity` / `ConsumedUnit`| genauer Treffer  
`PricingQuantity`| `PricingQuantity`| genauer Treffer  
`ContractedCost`| `ContractedCost`| genauer Treffer  
`ServiceFamilyName`| (nahe bei `ServiceCategory`)| Cloudflare-eigene Gruppierung; FOCUS verwendet ein kontrolliertes Vokabular.  
`CumulatedContractedCost`| (abgeleitet)| Convenience-Feld – FOCUS behandelt die Kumulation als Anfragebelang.  
`ZoneId` / `ZoneName`| (nahe bei `ResourceId` / `ResourceName`)| Zonenbezogener Bezeichner, wo zutreffend.  
  
Antworten verwenden das standardisierte Cloudflare-API-Gehäuse — `result` ist ein Array von Zeilen, eine pro Produkt und Abrechnungszeitraum, zusammen mit `success`, `errors`, und `messages`.

## **Auf dem Weg zur vollständigen FOCUS-Konformität**

Die Übernahme der FOCUS-Feldbezeichnungen war eine bewusste Entscheidung. AWS, Azure, Google Cloud, Oracle und eine stetig wachsende Zahl von SaaS-Anbietern stellen ihre Kosten- und Nutzungsdaten bereits im FOCUS-Format bereit. Auch alle etablierten FinOps- und Kostenmanagement-Tools unterstützen diesen Standard.Derzeit erfüllen wir die FOCUS-Spezifikation jedoch noch nicht vollständig: Einige der vorgeschriebenen Felder sind in der API-Antwort noch nicht enthalten. Die vollständige Konformität ist bereits eingeplant. Sehen Sie dies als ersten Meilenstein – heute ein vertrautes Datenmodell, als Nächstes vollständige FOCUS-Unterstützung.

## **Cloudflare-Kosten, neben den restlichen Cloud-Kosten: unsere Partnerschaft mit Vantage**

Wir haben gemeinsam mit[ ](https://www.vantage.sh/) [Vantage](https://www.vantage.sh/) eine native Cloudflare-Integration entwickelt. Vantage ist eine Plattform für das Management von Infrastrukturkosten, die Kosten- und Nutzungsdaten von mehr als 30 Anbietern aus den Bereichen KI, Cloud und SaaS zusammenführt. Die Daten werden in einer zentralen Ansicht für Reporting, Kostenzuordnung und Optimierung bereitgestellt. Mit dieser Integration fließen Ihre Cloudflare-Nutzungsdaten in dieselben Kostenberichte, Budgets und Kostenwarnungen ein, die Sie bereits für Ihre übrige Infrastruktur verwenden.

Vantage verbindet sich mit Cloudflare über ein API-Token mit ausschließlich Lesezugriff und der Berechtigung Billing Read. Nach der Verbindung ruft Vantage Ihre Billable-Usage-Daten täglich ab und schlüsselt sie nach Produkt (z. B. Workers und R2), Zone und Konto auf. So erkennen Sie, welche Produkte den größten Anteil an Ihren Kosten haben, und können diese den verantwortlichen Teams und Services zuordnen.

Einige der Workflows, die diese Integration unterstützt:

  * **Anbieterübergreifende Kostenzuordnung.** Gruppieren Sie Ihre Cloudflare-Ausgaben nach Produkt, Zone und Konto und ordnen Sie sie anschließend mithilfe virtueller Tags Teams oder Produktlinien zu. So lassen sich Cloudflare-Kosten gemeinsam mit den Kosten von AWS, Azure und anderen Anbietern in einem einzigen Bericht auswerten.
  * **Erkennung von Anomalien** Vantage Cost Alerts überwachen alle verbundenen Anbieter und benachrichtigen Sie per Slack oder E-Mail, wenn die Ausgaben von ihrem üblichen Niveau abweichen. So werden Veränderungen bei den Kosten für Workers oder R2 genauso sichtbar wie bei jedem anderen Anbieter.
  * **FinOps-Agenten und MCP.** Stellen Sie dem integrierten Vantage FinOps Agent beispielsweise die Frage: „Was war in der vergangenen Woche unser größter Kostentreiber über alle Anbieter hinweg?“ Alternativ können Sie dieselben Daten über den gehosteten MCP-Server von Vantage aus Claude oder ChatGPT heraus abfragen. Cloudflare-Kosten werden dabei gemeinsam mit den Kosten Ihrer übrigen verbundenen Anbieter berücksichtigt.



Verbinden Sie Ihr Cloudflare-Konto in der [​Vantage-Konsole](https://console.vantage.sh/). Anschließend werden Ihre Cloudflare-Kosten zusammen mit den Kosten Ihrer übrigen Infrastruktur angezeigt. Manuelle Exporte, Rechnungs-Uploads oder ein separates Dashboard sind nicht erforderlich. 

Diese standardisierte FOCUS-API funktioniert auch mit anderen Fintech-Tools.

## **Warum wir Billable Usage API entwickelt haben**

Agents schreiben nicht nur Code. Sie stellen Workers bereit, provisionieren R2-Buckets und verwalten D1-Datenbanken. Wenn Sie programmgesteuerten Zugriff auf Ihr Cloudflare-Konto gewähren, benötigen Sie ebenso programmgesteuerte Transparenz über die dadurch entstehenden Kosten. Nicht erst am Monatsende, sondern fortlaufend über den Tag hinweg, nach Produkt aufgeschlüsselt und in einem maschinenlesbaren Format, das sich direkt automatisiert verarbeiten lässt.

Genau das bietet die Billable Usage API. Und Kunden wünschen sich seit Jahren einen programmgesteuerten Zugriff auf Nutzungsdaten. Finanzteams möchten Kosten in ihre eigenen Systeme übernehmen und Kosten internen Projekten, Teams oder sogar ihren Endkunden zuordnen. Entwickler möchten einen curl-Befehl, den sie direkt in ein Skript einbauen können. Bisher erforderte jeder dieser Abläufe einen Screenshot oder einen manuellen Export. Heute genügt ein HTTP-Aufruf oder eine Konfiguration in Vantage.

## **Was kommt als Nächstes?**

  * **Feinere Zeitfenster.** Derzeit gibt die API Datenzeilen pro Abrechnungszeitraum zurück, der bei den meisten Produkten einem Tag entspricht. Für Produkte, bei denen es sinnvoll ist, prüfen wir künftig stärker echtzeitnahe Aufschlüsselungen.
  * **Prognosen.** CumulatedContractedCost zeigt Ihnen, wie hoch Ihre bisherigen Ausgaben im aktuellen Abrechnungszeitraum sind. Künftig möchten wir Ihnen dabei helfen, vorherzusagen, wo diese am Ende des Abrechnungszeitraums liegen werden – und zwar nicht nur auf Konto-, sondern auch auf Produktebene.
  * **Unterstützung für Enterprise-Verträge.** Diese erste Version steht ausschließlich für Self-Service-Konten zur Verfügung. Eine vergleichbare Lösung für Enterprise-Verträge ist bereits in Entwicklung.



## **Probieren Sie es aus**

Der Endpunkt ist ab heute für alle Self-Service-Konten verfügbar. Erstellen Sie ein API-Token mit der Berechtigung _Billing Read_ , richten Sie Ihren curl-Aufruf darauf aus, und Sie erhalten eine nach Produkt aufgeschlüsselte Übersicht über den aktuellen Abrechnungszeitraum. Die vollständige Referenz finden Sie in der Cloudflare-API-Dokumentation. Um die Daten gemeinsam mit Ihren übrigen Cloud-Kosten anzuzeigen, verbinden Sie Ihr Cloudflare-Konto in der [​](https://console.vantage.sh/) [Vantage-Konsole](https://console.vantage.sh/).

Seit Jahren erleichtert Cloudflare Unternehmen, mehr ihrer Infrastruktur auf unserem Netzwerk auszuführen. Nun machen wir es genauso einfach, die damit verbundenen Kosten zu verstehen – sowohl bei Cloudflare als auch im restlichen Cloud-Stack.

]]>01KZAX0K14NE4AFK427Q4VNWXDIhr Agent benötigt einen Computer, nicht einen Container — Einführung von @cloudflare/computerhttps://blog.cloudflare.com/de-de/cloudflare-computer/ Wed, 05 Aug 2026 03:23:58 GMTAgents benötigen mehr als nur einen Container, um effizient zu skalieren. Mit @cloudflare/computer stellen wir eine Agent-Runtime vor, die dynamisch zwischen performanten und ressourceneffizienten Isolates und vollständigen Linux-Containern orchestriert – und so jedem Agenten einen eigenen Computer bereitstellt.AgentsAgents WeekAICloudflare WorkersContainerDie leistungsfähigsten Agents haben eine einfache Gemeinsamkeit: Ihnen steht ein eigener Computer zur Verfügung.

Coding-Agents arbeiten nach diesem Prinzip. Sie erhalten ein Dateisystem, eine Shell, Tools, Pakete und die Möglichkeit, Code auszuführen. Sie untersuchen ihre Umgebung, nehmen Änderungen vor, testen ihre Arbeit und machen weiter. Der Computer gibt dem Modell eine vertraute Umgebung, um mit der Welt zu interagieren. Bei Cloudflare arbeiten wir intensiv daran, die richtigen grundlegenden Bausteine bereitzustellen, auf denen sich die leistungsfähigsten Agents aufbauen lassen.

**Heute stellen wir eine Early Preview von[ @cloudflare/computer](https://github.com/cloudflare/workspace) **vor. Das Paket @cloudflare/computer stellt eine Agent-Runtime bereit, bei der die Plattform automatisch die Details und Abläufe dafür übernimmt, welcher Code in einem Isolate und welcher in einer Container-Sandbox ausgeführt wird. Jeder Agent erhält einen eigenen Computer, während die Runtime auf Effizienz und Skalierbarkeit optimiert.

Um den stetig steigenden Compute-Bedarf agentischer Systeme zu decken, reichen herkömmliche Containerlösungen aus unserer Sicht nicht mehr aus. 

## Ein neuer Ansatz für die Entwicklung von Agents

In den vergangenen sechs Monaten haben wir eine allmähliche Weiterentwicklung dieses Ansatzes beobachtet. Zu Jahresbeginn war es noch üblich, einen Container zu starten und darin einen Agent auszuführen. In den letzten Monaten hat sich jedoch rasch ein neues Muster etabliert: Agent-Harnesses stellen über Tools eine isolierte Codeausführung bereit. Dadurch werden die Hände – also die Sandbox, in der die eigentliche Arbeit stattfindet – vom Gehirn, der Agent-Schleife, getrennt.

Unabhängig davon, wo der Harness ausgeführt wird, stellt es eine Herausforderung dar, jedem Agenten einen eigenen Container bereitzustellen. Über alle Clouds und Hyperscaler hinweg gibt es weltweit bei Weitem nicht genügend Rechenkapazität, damit jedes Unternehmen jedem Agenten seiner Nutzer eine eigene containerisierte Compute-Umgebung zur Verfügung stellen kann. Dieser Ansatz lässt sich nicht auf Hunderte Millionen und anschließend Milliarden gleichzeitig aktiver Agents skalieren. Genau deshalb herrscht in der Branche eine dringende, geradezu hektische Nachfrage nach CPU-Rechenleistung – nicht nur nach GPU-Compute.

Bei Cloudflare arbeiten wir schon seit Langem an diesem Problem und haben mit Isolates einen effizienteren Compute-Baustein entwickelt. Auf diesen damals unkonventionellen Ansatz setzten wir erstmals vor fast zehn Jahren, als wir [Cloudflare Workers einführten](https://blog.cloudflare.com/introducing-cloudflare-workers/). Knapp sechs Jahre später trafen wir dieselbe Entscheidung erneut mit der [Einführung von Durable Objects](https://blog.cloudflare.com/introducing-workers-durable-objects/). Wir haben auf Isolates gesetzt, weil sie sich horizontal praktisch unbegrenzt skalieren lassen. Sie werden innerhalb von Millisekunden gestartet und beendet. Sie können [in den Ruhezustand wechseln](https://developers.cloudflare.com/durable-objects/examples/websocket-hibernation-server/), wenn ein Agent inaktiv ist, d[en eigenen Zustand des Agents speichern](https://blog.cloudflare.com/sqlite-in-durable-objects/) und sogar [eigene Isolates starten](https://blog.cloudflare.com/dynamic-workers/), um nicht vertrauenswürdigen Code auszuführen. Isolates sind die beste Möglichkeit zur horizontalen Skalierung – und genau diese horizontale Skalierbarkeit benötigen Agents.

Im vergangenen Jahr [haben wir Isolates die Möglichkeit gegeben, eigene Container-Sandboxes zu starten](https://blog.cloudflare.com/containers-are-available-in-public-beta-for-simple-global-and-programmable/). Die Architektur von Cloudflare war von Anfang an darauf ausgelegt, den Agent-Harness im Isolate – innerhalb eines Durable Object – auszuführen und bei Bedarf einen angebundenen Container als Tool aufzurufen. So kommen rechenintensivere Compute-Bausteine nur dann zum Einsatz, wenn sie tatsächlich benötigt werden, was Performance und Kosten optimiert. Durable Objects lassen sich horizontal praktisch unbegrenzt skalieren, während der angebundene Container die vertikale Skalierung für beliebige Aufgaben ermöglicht. So entwickeln wir unsere Agents selbst – und wir sehen, dass auch Kunden auf diese Weise beeindruckende Anwendungen entwickeln

Wenn wir jedoch betrachten, dass für die Entwicklung von Agents mehrere zugrunde liegende Compute-Bausteine – Isolates und Container – erforderlich sind und unsere Kunden und Entwickler diese bislang selbst im Userspace kombinieren müssen, sind wir überzeugt, dass es besser geht. Wir können eine einfachere Abstraktion bereitstellen.

Deshalb starten wir dieses Experiment mit @cloudflare/computer als Open-Source-Bibliothek. Gemeinsam mit unseren Kunden, die die Grenzen des skalierbaren Betriebs von Agents ausloten, möchten wir Erfahrungen sammeln.

## Ein gemeinsames Dateisystem über Isolations- und Containergrenzen hinweg

Das Paket @cloudflare/computer basiert auf einer einfachen Überlegung: Was wäre, wenn wir einem Agenten ein vorbereitetes, deklarativ definiertes Dateisystem bereitstellen, das alles enthält, was für die jeweilige Aufgabe erforderlich ist, sowie eine Auswahl an Ausführungsumgebungen, die mit diesen Dateien arbeiten können – jeweils mit eigenen Vor- und Nachteilen hinsichtlich Geschwindigkeit, Leistungsumfang und Kosten?

Es zeigt sich, dass Agents heute erstaunlich gut darin sind, die passende Umgebung für die jeweilige Aufgabe auszuwählen. Eine Aufgabe, bei der lediglich Dateien bearbeitet, Daten verarbeitet oder ein Git-Repository verwaltet werden müssen, kann in einem Isolate ausgeführt werden. Ein Befehl, der Linux, `npm` oder eine native Binärdatei erfordert, kann hingegen in einem Container laufen. Beide Umgebungen arbeiten mit denselben Dateien, die mit dem Quelldateisystem synchron gehalten werden.

Das Paket @cloudflare/computer stellt ein persistentes Dateisystem bereit, das Sie mit Git-Repositories, Storage-Buckets oder beliebigen anderen Dateien verwenden können. Es bietet Tools, mit denen Sie Dateien über den [Code Mode (Code-Modus)](https://blog.cloudflare.com/code-mode/) oder mithilfe von Bash-Befehlen lesen, schreiben und bearbeiten können. Sämtliche Vorgänge werden kontrolliert, protokolliert und überwacht. Dadurch erhalten Sie eine granulare Kontrolle darüber, welche Änderungen der Agent vornehmen darf, sowie eine klare Nachvollziehbarkeit aller ausgeführten Aktionen.

## Wie Sie es nutzen können

Eine Instanz eines @cloudflare/computer-Workspaces kann in jedem Durable Object erstellt werden und stellt dort ein virtuelles Dateisystem sowie eine Ausführungsumgebung bereit.

Es wird über npm installiert:

Der primäre Anwendungsfall besteht darin, dieses Dateisystem und die Werkzeuge einem Agenten bereitzustellen. Hier ist beispielsweise, wie Sie den Arbeitsbereich auf einem von @cloudflare/think betriebenen Agenten einrichten, der zur Priorisierung von Fehlermeldungen gedacht ist.

Das Paket @cloudflare/computer stellt mehrere Ausführungs-Backends bereit, Sie können aber auch eigene implementieren. Im folgenden Beispiel binden wir einen Cloudflare Container an.

Stellen Sie die Datei-, Git- und Shell-Tools neben produktspezifischen Tools bereit, um auf gemeldete Probleme zu reagieren.

Das Modell kann während der Agent-Schleife Werkzeuge verwenden, aber Sie können auch die Workspace-API direkt nutzen, um beispielsweise die Umgebung vorzubereiten, bevor Sie dem Agenten einen Prompt übergeben

Im [Workspace-Repository](https://github.com/cloudflare/computer) finden Sie weitere Beispiele für den Einsatz der unterschiedlichen Backends und Tools – darunter auch eine [Schritt-für-Schritt-Anleitung](https://github.com/cloudflare/computer/tree/main/examples/tutorial), die den Aufbau eines Agents von Grund auf erklärt.

## So funktioniert’s

Das zentrale Element von @cloudflare/computer ist der Workspace: ein SQLite-basiertes virtuelles Dateisystem, das aus verschiedenen Quellen befüllt werden kann, darunter Cloud-Speicher und Versionsverwaltungssysteme.

Der Workspace kann um optionale Ausführungsumgebungen ergänzt werden, die Code direkt auf dem Dateisystem ausführen. Sämtliche Runtimes unterstützen dieselbe Schnittstelle `exec(string, options)`. Aktuell sind zwei standardmäßig enthalten, eigene Implementierungen sind ebenfalls möglich:

  * Eine Isolate-basierte Runtime-Umgebung nutzt [just-bash](https://justbash.dev/), um Shell-Code in JavaScript zu übersetzen, und wird in einem [dynamischen Worker](https://developers.cloudflare.com/dynamic-workers/) ausgeführt. Das Dateisystem ist dabei direkt über Worker Bindings verfügbar.
  * Eine Container-Runtime verwendet [Cloudflare Containers](https://developers.cloudflare.com/containers/), um eine vollständige Linux-Umgebung bereitzustellen. Hier wird das Dateisystem über einen Filesystem-in-Userspace-Mount (FUSE) eingebunden, sodass der Container auf die Dateien zugreifen kann und Änderungen anschließend zurücksynchronisiert werden.



Die Klasse `Workspace` stellt eine API zum direkten Arbeiten mit dem Dateisystem sowie einen mit `node:fs`-kompatiblen Wrapper bereit, sodass sie sich problemlos mit JavaScript-Bibliotheken von Drittanbietern verwenden lässt.

Für die Arbeit mit Agents stellen wir ein mit dem AI SDK kompatibles Toolkit bereit, das die gängigsten Tools umfasst: read, write, edit, ls und exec. Das Tool exec ist dabei etwas Besonderes, da es über mehrere Runtimes hinweg arbeitet und ein `backend`-Argument akzeptiert. Die Tool-Beschreibung hilft dem Agenten, für die jeweilige Aufgabe die richtige Runtime auszuwählen: entweder ein schnelles, kostengünstiges Worker-Backend oder den vollwertigen Container. In unseren Tests treffen Frontier-Modelle diese Entscheidung sehr zuverlässig und greifen nur dann auf Container zurück, wenn sie tatsächlich benötigt werden.

## Was steht als Nächstes an?

Schon heute beobachten wir bei Cloudflare, dass Agents ausschließlich mit Isolates JavaScript-Anwendungen mithilfe moderner Toolchains entwickeln, testen und bereitstellen, für jeden unserer Kunden individuell zugeschnittene Dokumentationen erstellen und Webbrowser für die Ausführung komplexer Aufgaben nutzen.

Unser Ziel mit @cloudflare/computer ist es, Agents eine Runtime bereitzustellen, in der für weniger als zehn Prozent ihrer Aufgaben ein Container erforderlich ist und Coding-Aufgaben, die Bearbeitung von Audio- und Videodateien sowie die Erstellung von Dokumenten vollständig in Isolates erfolgen können. 

Probieren Sie die [Early Preview noch heute](https://github.com/cloudflare/computer) aus – wir freuen uns auf Ihr Feedback.

]]>01KZ7YRCN6Q50SEZXB56MZ1ZMPWillkommen bei der Agents Weekhttps://blog.cloudflare.com/de-de/agents-week-welcome/ Wed, 05 Aug 2026 02:42:50 GMTIm Rahmen der Agents Week zeigen wir, wie Cloud-Infrastrukturen angepasst werden müssen, damit sie autonomen Agents und nicht länger primär menschlichen Browsern dienen. Gemeinsam betrachten wir die grundlegenden Speicher-, Ausführungs- und Sicherheitsfunktionen, die ein agentennatives Web ermöglichen.AgentsAgents WeekAICloudflare WorkersEntwicklerplattformDiese Woche ist Agents Week.

Als wir mit den Überlegungen und Planungen für diese Woche begannen, beschäftigte uns eine grundlegendere Frage: Was braucht es, um diese neue Ära der Agents zu unterstützen, und wie sieht eine Infrastruktur aus, die von Grund auf für Agents konzipiert wurde? Daraus entstand eine einfachere Leitfrage: Was ist eine Agent Cloud? 

Wir erkannten jedoch rasch, dass wir die Sache falsch angegangen waren. Nicht, weil es die falsche Frage war, sondern weil wir sie uns selbst stellten – statt unseren Agents. Entscheidend ist nicht mehr, was wir denken, sondern was Agents benötigen. 

Das bringt auf den Punkt, worum es bei der Agents Week geht. 

Die heutige Cloud und das zugrunde liegende Web wurden für menschliche Nutzer konzipiert. Jede Schicht setzt voraus, dass ein Mensch mit ihr interagiert: Seiten sind darauf ausgelegt, Aufmerksamkeit zu gewinnen, Dashboards auf Klicks und Benutzeroberflächen auf menschliches Lesen und Entscheiden. Für Agents gelten jedoch andere Voraussetzungen. Sie kennen weder Ablenkung noch Müdigkeit oder Ermüdungserscheinungen und stellen stattdessen eigene Anforderungen an Geschwindigkeit, Struktur und Zugriff.

Eine Agent Cloud muss zwei Aufgaben gleichzeitig erfüllen. Einerseits muss sie den Weg für eine agentennative Zukunft ebnen, in der die grundlegenden Bausteine von Anfang an für Agents entwickelt werden – statt nachträglich aus Werkzeugen für Menschen angepasst zu werden. Andererseits muss sie den heutigen Anforderungen gerecht werden und als Vermittlungsschicht zwischen dem menschenzentrierten Web von heute und dem agentenzentrierten Web von morgen fungieren.

Dieser Gedanke zieht sich als Leitmotiv durch die kommenden fünf Tage: Wie muss eine Cloud beschaffen sein, damit sie sowohl Agents als auch Menschen unterstützt – und wie arbeiten beide zusammen? Die Woche widmet sich den dafür erforderlichen Grundbausteinen und der Ausführungsschicht, dem weiterentwickelten agentenbasierten Softwareentwicklungszyklus, sicheren Interaktionsmodellen für Mitarbeitende und Agents, den Folgen für das agentenbasierte Web sowie der Frage, wie sich all dies mit der heutigen Realität vereinbaren lässt.

Kehren wir zur Ausgangsfrage zurück: Was braucht Ihr Agent von einer Agent Cloud? Anstatt einfach die Antworten wiederzugeben, die wir von unseren Agents erhalten haben, möchten wir Sie ermutigen, diese Frage Ihrem eigenen Agent zu stellen und interessante Erkenntnisse oder Antworten mit uns zu teilen. Als Ausgangspunkt finden Sie unten einen Beispiel-Prompt – wir laden Sie jedoch ein, auch eigene Fragestellungen und Antworten zu erkunden.

_Was benötigen Sie als Agent von einer Agent Cloud? Berücksichtigen Sie dabei Themen wie Speicher- und Compute-Infrastruktur, die dafür erforderlichen Ausführungs- und Speicher-Primitives, Ihren Entwicklungslebenszyklus (ADLC – ähnlich dem SDLC, jedoch ohne menschliche Eingriffe), den sicheren Zugriff auf Systems of Record eines Unternehmens zur Erledigung anspruchsvoller Aufgaben sowie das Web mit seinen Funktionen für Discovery, Zugriff und Zahlungsabwicklung._

Teilen Sie uns mit, was Ihr Agent geantwortet hat, indem Sie direkt über foglende Kanäle antworten – wir sind gespannt auf die Ergebnisse! 

[Verfolgen Sie diese Woche unseren Blog](https://blog.cloudflare.com/), um die neuesten Innovationen rund um Agents zu entdecken, und[ tauschen Sie sich mit uns auf X aus](https://x.com/CloudflareDev), um an der Diskussion teilzunehmen.

]]>01KZ7WP9SY8HW7DPTQKRKGPAP4Naturkatastrophen und staatliche Eingriffe: Die wichtigsten Internetstörungen im zweiten Quartal 2026https://blog.cloudflare.com/de-de/q2-2026-internet-disruption-summary/ Tue, 04 Aug 2026 03:05:41 GMTIm vergangenen Quartal hat Cloudflare Radar Internetstörungen durch Naturkatastrophen, staatlich angeordnete Abschaltungen und DNSSEC-Schlüsselwechsel verzeichnet. In diesem Beitrag erläutern wir anhand von Traffic-Telemetriedaten, wie sich diese Ereignisse weltweit auf die Konnektivität ausgewirkt haben.AusfallAWSInternet-TrafficInternet-TrendsInternetabschaltungRadarSolange alles gut geht, wird gern übersehen, wie fragil das Internet eigentlich ist. Das hat das Web mit anderen Arten von Infrastruktur gemeinsam. Seine Komplexität tritt erst dann voll zutage, wenn es nicht mehr richtig funktioniert. Cloudflare ist in einzigartiger Weise in der Lage, die Momente zu erkennen und zu dokumentieren, in denen eines der miteinander vernetzten Systeme, auf die sich das Internet stützt, ausfällt und die Konnektivität beeinträchtigt. Wir bieten jedes Quartal einen Überblick über die Störungen, die bei [Cloudflare Radar](https://radar.cloudflare.com/) verzeichnet und kommentiert werden. 

Den längsten Ausfall verursachte im zweiten Quartal 2026 Supertaifun Sinlaku nördlich von Guam. Zu staatlichen Abschaltungen des Webs kam es im Berichtszeitraum am häufigsten im Sudan, wo diese von der Regierung während der Prüfungszeit angeordnet wurden. Der Iran stellte den Internetzugang für seine Bürger nach einer 88-tägigen Unterbrechung landesweit wieder her, während anderswo in dieser Weltregion Drohnenangriffe weiterhin Störungen bei der AWS-Infrastruktur verursachten. Schließlich verdeutlichten ein Kabelschaden in Saint Lucia und die Ausgabe fehlerhafter DNSSEC-Signaturen in Deutschland die Fragilität der Internet-Infrastruktur, aber auch die bemerkenswerte Stabilität dieser regionalen und globalen Systeme unter normalen Betriebsbedingungen.

An dieser Stelle wollen wir näher auf die schwerwiegendsten Internetstörungen eingehen, die von uns im zweiten Quartal 2026 beobachtet wurden. Wir zeichnen anhand von Traffic-Daten von Cloudflare Radar den Ablauf der einzelnen Vorfälle und ihre Auswirkungen für die Benutzer vor Ort nach. Wie gewohnt bieten wir keine erschöpfende Liste aller Zwischenfälle, sondern stellen die bemerkenswertesten Störungen vor, die gesichert stattgefunden haben. Eine umfassendere Aufstellung der registrierten Traffic-Auffälligkeiten finden Sie im [Outage Center von Cloudflare Radar](https://radar.cloudflare.com/outage-center?dateStart=2026-04-01&amp;dateEnd=2026-06-30).

### Naturkatastrophen und Stromausfälle verursachen Störungen in Guam, Venezuela und Tansania

Sinlaku, der bislang stärkste tropische Wirbelsturm der Taifunsaison des Jahres 2026 im Pazifik, ist Mitte April über die Marianen hinweggefegt und nördlich mit geringer Entfernung an Guam vorbeigezogen. Die Insel wurde also nicht direkt getroffen, doch mit dem Supertaifun gingen Winde mit der Stärke eines tropischen Wirbelsturms einher, die auf ganz Guam Wasserversorgungssysteme beeinträchtigt und Stromausfälle verursacht haben. Dies hatte direkte Auswirkungen auf die Internetkonnektivität. So sank der Datenverkehr aus dem Gebiet vom 13. auf den 14. April um bis zu 80 % unter das eigentlich zu erwartende Niveau. 

Zwei Monate später, am 25. Juni, ereigneten sich in Nordvenezuela – genauer gesagt in Yumare und San Felipe – zwei schwere Erdbeben in einem zeitlichen Abstand von etwa einer Minute. Es folgte ein Nachbeben in Küstennähe unweit von Caracas. Das erste Beben erreichte eine Stärke von 7,5 und fand ungefähr um 00:04 Uhr MESZ (18:04 Uhr am 24. Juni Ortszeit) statt. Die unmittelbaren Auswirkungen dieser Ereignisse sind bei Radar zu sehen, wo das Volumen der übertragenen HTTP-Bytes während der Erdbeben deutlich sinken. Besonders gut ist dies bei dem Anbieter Fibex Telecom zu sehen, der laut [APNIC-Daten](https://stats.labs.apnic.net/aspop/) über schätzungsweise 1,6 Mio. Benutzer verfügt. Erkennbar ist der Rückgang aber auch bei dem staatlichen Hauptanbieter [CANTV](https://radar.cloudflare.com/traffic/as8048?dateStart=2026-06-24&amp;dateEnd=2026-06-25#traffic-trends) und bei dem etwas kleineren Internetdienstleister [VNET](https://radar.cloudflare.com/traffic/as263703?dateStart=2026-06-24&amp;dateEnd=2026-06-25).

Nur wenige Tage später, am 27. Juni, führte ein Stromausfall in Tansania zu einem starken Rückgang des HTTP-Traffics für mindestens fünf Stunden. Die Ursache war eine andere als bei dem im Oktober 2025 im Zusammenhang mit den Wahlen im Land verzeichneten Ausfall (der nicht auf einen Infrastrukturdefekt zurückzuführen war, sondern von der Regierung gezielt herbeigeführt wurde). Doch die dabei erhobenen Telemetriedaten und der Einfluss auf die Benutzer waren nahezu identisch: Aufgrund einer dramatischen Einschränkung der Konnektivität konnten die Einwohner nicht mit ihren Angehörigen kommunizieren oder wichtige Nachrichten erhalten. 

Es ist bemerkenswert, dass von Grund auf verschiedene Ereignisse wie diese sich auf derart ähnliche Weise auf die Daten und die Benutzererfahrung niederschlagen. Zusammen zeigen diese auf das Wetter und die Stromversorgung zurückzuführenden Störungen die enormen Auswirkungen, die Ereignisse in der physischen Welt auf den digitalen Raum haben können. Außerdem machen sie deutlich, welche wichtige Rolle Internetresilienz und eine ausreichenden Netzwerkredundanz in Bezug auf die Stromversorgung, das Routing und physische Verbindungen spielen, wenn Netzwerke unvermeidlichen Verwerfungen standhalten sollen.

### Regierungen und Geopolitik nehmen Einfluss auf Konnektivität in den VAE und im Iran, Irak und Sudan

Radar hat ab dem 26. Mai Anzeichen für die zuvor [angekündigte](https://x.com/ir_aref/status/2059261258566877640?s=20) Wiederherstellung der Internetverbindung im Iran registriert. Dies markierte das vorläufige Ende einer 88-tägigen Abschaltung, im Rahmen derer das Land ab dem 28. Februar nahezu vollständig vom Web abgeschnitten war. Am 27. Mai [meldete](https://blog.cloudflare.com/iran-internet-partially-restored-may-2026/) Radar, dass der Traffic wieder 40 % des vor dem Ausfall verzeichneten Niveaus erreicht hat. Damit wurde die Internetanbindung teilweise wiederhergestellt. Dies deckt sich mit Berichten, wonach der Zugang zum Web nur selektiv und nicht umfassend ermöglicht wurde. Anschließend haben wir beobachtet, dass das HTTP-Bytes-Volumen vorübergehend auf bis zu 90 % des vor der Kappung des Internets registrierten Niveaus angestiegen ist, bevor es sich bei etwa 59 % eingependelt hat. Dies entspricht dem von uns im Februar verzeichneten Traffic – einem Zeitfenster zwischen dieser jüngsten Abschaltung und einer früheren im Januar. Die Konnektivität hat sich somit wohl nicht vollständig normalisiert, sondern liegt nur wieder auf dem Niveau, das sie zuletzt vor der Abschaltung erreicht hatte. In unserer [Analyse zur Fußballweltmeisterschaft 2026](https://blog.cloudflare.com/2026-world-cup-internet-traffic/#streaming-makes-some-countries-appear-more-online) stach der Iran als einziger Ausreißer hervor: Während der Datenverkehr in den meisten Teilnehmerländern in Einklang mit den Spielterminen zu- und abnahm, waren die Messwerte des Iran vom Kontrast zwischen dem Niveau nach der Wiederherstellung der Anbindung und dem vorausgegangenen, fast vollständigen Konnektivitätsverlust geprägt.

Währenddessen liegt der für me-central-1, eine AWS-Cloud-Region in den Vereinigten Arabischen Emiraten (VAE), bestimmte HTTP-Traffic [weiter auf niedrigem Niveau](https://radar.cloudflare.com/cloud-observatory/amazon/me-central-1?dateRange=24w#http-traffic). Dies stimmte mit den [AWS-Betriebsberichten](https://health.aws.amazon.com/health/status#multipleservices-me-central-1_1777533954) vom 30. April überein, denen zufolge die Weltregion „durch den Nahost-Konflikt in Mitleidenschaft gezogen wurde und derzeit nicht in der Lage ist, Kundenanwendungen zuverlässig zu unterstützen.“ Dem waren Berichte vom 3. März vorausgegangen, laut denen sowohl in den VAE als auch in Bahrain „durch Drohnenangriffe Infrastruktur beschädigt“ wurde. In den VAE wurden zwei Standorte „direkt getroffen“ und in Bahrain verursachte ein Drohnenangriff in der Nähe einer Anlage Schäden an ihrer Infrastruktur. Der verringerte Traffic ist keine Folge eines Netzwerkfehlers, sondern das nachgelagerte Kennzeichen eines physischen Schadens an der zugrunde liegenden Rechenzentrumsinfrastruktur. Die Drosselung sorgt weiterhin für Beeinträchtigungen bei den in dieser Weltregion gehosteten Websites und Anwendungen, die ansonsten erreichbar wären.

Außerdem gab es im zweiten Quartal 2026 drei staatlich angeordnete Abschaltungen im Irak (am [2\. Juni](https://radar.cloudflare.com/traffic/iq?dateStart=2026-06-01&amp;dateEnd=2026-06-02), [11\. Juni](https://radar.cloudflare.com/traffic/iq?dateStart=2026-06-10&amp;dateEnd=2026-06-11) und [28\. Juni](https://radar.cloudflare.com/traffic/iq?dateStart=2026-06-27&amp;dateEnd=2026-06-28)) sowie [zehn im Sudan](https://radar.cloudflare.com/traffic/sd?dateStart=2026-04-13&amp;dateEnd=2026-04-23#traffic-trends) zwischen dem 13. und 23. April. In allen Fällen wollte man damit Betrug bei landesweiten Prüfungen einen Riegel vorschieben. Solche Maßnahmen haben wir in den vergangenen Quartalen in beiden Ländern immer wieder zu Prüfungszeiten dokumentiert. Im Sudan folgten die Ausfällen einem festen Rhythmus: Jeder dauerte ungefähr dreieinhalb Stunden, von 13:45 Uhr bis 17:15 Uhr MESZ/Ortszeit – der Zeit, in der Prüfungen stattfanden. Die Ausfälle im Irak erstreckten sich dagegen jeweils nur über etwa 90 Minuten, fielen aber ebenfalls auf die Zeiten, in denen Prüfungen abgehalten wurden.

Jedes dieser Beispiele – ob es sich nun um eine Wiederherstellung oder eine Störung handelt – veranschaulicht, welch große Kontrolle ein Staat über die landesweite Konnektivität hat und wie leicht er das Internet abschalten, drosseln oder nur in ausgewählten Bereichen wiederherstellen kann, und zwar nicht aus infrastrukturellen, sondern aus politischen Beweggründen.

## Beeinträchtigung von Benutzern durch Infrastruktur-Schwachstellen in Deutschland und Saint Lucia 

Am 5. Mai hatte ein Wechsel der DNSSEC-Schlüssel bei der Registrierungsstelle für die deutsche .de-Domain zur Folge, dass [ungültige Signaturen erzeugt](https://blog.denic.de/technische-storung-bei-de-domains-behoben/) wurden. Die zur Signierung der DNS-Einträge einer Zone verwendeten kryptografischen Schlüssel werden regelmäßig geändert. Das gehört zur Wartungsroutine, ist aber ausgesprochen wichtig, weil die DNSSEC validierenden Resolver nur Antworten akzeptieren, deren Signaturen mit den aktuell veröffentlichten Schlüsseln übereinstimmen. Mit anderen Worten: Entsprechen die digitalen Signaturen nicht den erwarteten Werten, geht der Resolver von einer Manipulation der Website aus und verweigert den Zugriff. Als ungültige Signaturen erzeugt wurden, lehnten Validierungsresolver weltweit jede Anfrage für Websites mit der .de-Domain ab und beantworteten diese mit einer SERVFAIL-Fehlermeldung. Um 01:15 Uhr MESZ am 6. Mai wurde der Normalbetrieb wiederhergestellt. 

Cloudflare Radar hat während des Ausfalls einen Anstieg der .de-Abfragen weltweit beobachtet. Dies mag auf den ersten Blick vielleicht überraschen. Der Grund dafür ist, dass fehlgeschlagene Antworten faktisch nicht im Cache gespeichert werden können. Deshalb mussten Abfragen, die normalerweise einfach aus dem Cache heraus beantwortet worden wären, stattdessen erneut mehrfach einer Auflösung unterzogen und wiederholt werden. Das hatte einen starken Anstieg der Abfragenzahl zur Folge.

Für die Benutzer stellte sich der Vorfall nicht als DNS- oder Kryptografie-Fehler dar, sondern schlicht und ergreifend als eine Flut von plötzlich nicht mehr erreichbaren .de-Websites und -Diensten. Man konnte weiterhin auf Seiten zugreifen, die nicht die Top Level Domain .de nutzten. Die Benutzer waren aber damit konfrontiert, dass Seiten nicht luden, E-Mails nicht zugestellt wurden und es bei Anwendungen zu Zeitüberschreitungen kam. Alle diese Probleme können auch bei einem Ausfall auftreten. Mehr zu DNSSEC und den Folgen der beschriebenen Vorfälle erfahren Sie in unserem [Blogbeitrag](https://blog.cloudflare.com/de-tld-outage-dnssec/) zu diesem Thema.

In der Karibik führte eine Infrastrukturpanne zu einer ähnlichen Einschränkung der Verfügbarkeit. Am 21. Juni sank der HTTP-Anfrage-Traffic aus dem Netzwerk von Karib Cable bis etwa 23:00 Uhr MESZ (17 Uhr Ortszeit) praktisch auf null. Daran änderte sich fast einen Tag lang so gut wie nichts, bis der Datenverkehr am 22. Juni um etwa 19:00 Uhr MESZ (13:00 Uhr Ortszeit) wieder zu den erwarteten Werten zurückkehrte. [Berichten zufolge](https://stluciatimes.com/181838/2026/07/flow-reveals-details-of-customer-rebates-after-major-outage/) wurde der Ausfall durch einen Glasfaserdefekt in der Nähe der Inselgruppe verursacht. Dies ist ein bekanntes Problem karibischer Netzwerke, die das Internet nur über eine geringe Zahl von terrestrischen Verbindungen und Seekabeln erreichen können, sodass durch einen einzelnen Ausfall unter Umständen ein unverhältnismäßig großer Teil der Kapazität nicht mehr zur Verfügung steht. Da Karib Cable zu den führenden Anbietern vor Ort zählt, war der Ausfall landesweit spürbar, denn während seiner Dauer ist der gesamte Datenverkehr von Saint Lucia [gegenüber der Vorwoche um ungefähr 60 % eingebrochen](https://radar.cloudflare.com/explorer?dataSet=netflows&amp;loc=LC&amp;dt=2026-06-21_2026-06-27&amp;timeCompare=1#result).

### Radar behält Störungen weiter im Blick

Zu den vielfältigen Ursachen der im zweiten Quartal 2026 beobachteten Internetstörungen gehörten Unwetter, ein Erdbeben, Stromausfälle, staatlich angeordnete Abschaltungen, eine Beschädigung der Cloud-Infrastruktur, Kabelausfälle und eine DNSSCE-Fehlkonfiguration. Diese Vorfälle zeigen, dass das Internet auf zahlreiche komplexe Systemen angewiesen ist. Da diese miteinander verbunden sind, kann schon der Ausfall eines einzigen davon einen Verlust der Konnektivität zur Folge haben.

Das Team von Cloudflare Radar hält ständig nach Störungen im Internet Ausschau und veröffentlicht seine Beobachtungen im [Outage Center von Cloudflare Radar](https://radar.cloudflare.com/outage-center), in den sozialen Netzwerken und in Beiträgen auf [blog.cloudflare.com](http://blog.cloudflare.com). Folgen Sie uns auf Social Media bei [@CloudflareRadar](https://twitter.com/CloudflareRadar) (X), [noc.social/@cloudflareradar](https://noc.social/@cloudflareradar) (Mastodon) und [radar.cloudflare.com](http://radar.cloudflare.com) (Bluesky).

]]>01KZ5BFVKDV78WRD7MMN7E9S2A
