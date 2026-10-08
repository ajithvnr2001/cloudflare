---
url: https://blog.cloudflare.com/it-it/rss/
title: Il blog di Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:23:07.474375+00:00
---

# Il blog di Cloudflare

> Source: https://blog.cloudflare.com/it-it/rss/

Il blog di CloudflareApprofondimenti tecnici, aggiornamenti sui prodotti e spunti dai team che contribuiscono a costruire un Internet migliore.https://blog.cloudflare.com/it-it/ it-ithttps://blog.cloudflare.com/favicon.icoIl blog di Cloudflarehttps://blog.cloudflare.com Thu, 08 Oct 2026 08:23:05 GMTInternet ha un secondo pubblicohttps://blog.cloudflare.com/it-it/agentic-web/ Thu, 08 Oct 2026 07:27:47 GMTPiù della metà del traffico che raggiunge i siti su Cloudflare è ora automatizzato e gli agenti IA ne rappresentano la componente in più rapida crescita. Stiamo fornendo ai proprietari di siti gli strumenti per vedere chi li visita, decidere chi può accedere e addebitare l'accesso.AgentiAI BotsAI SearchBirthday WeekIAPer la maggior parte della sua storia, Internet ha avuto un solo pubblico che pagava i conti: le persone. Leggevamo gli articoli, vedevamo le pubblicità e acquistavamo gli abbonamenti. I bot erano sempre presenti, ma si trattava per lo più di grandi operazioni automatizzate che non guardavano le pubblicità, non pagavano nulla e non leggevano in alcun senso significativo.

Tutto ciò sta cambiando rapidamente. Alla fine del 2024, Cloudflare gestiva una media di 63 milioni di richieste HTTP _al secondo_. Oggi, questo numero è quasi raddoppiato a 115 milioni, con picchi superiori a 150 milioni. Nell'ultimo anno, le richieste giornaliere degli agenti IA sulla nostra rete sono cresciute di oltre il 1.700 %. Quest'anno, per la prima volta, più della metà del traffico Internet non era di origine umana.

Il web umano non si è ridotto per fare spazio. Un secondo pubblico è arrivato al suo fianco: agenti, software che agisce per conto delle persone. Si collocano da qualche parte tra gli esseri umani e i bot tradizionali. Non rispondono agli annunci, ma di solito c'è una persona dietro di loro con un compito da svolgere. Per le aziende che imparano a servirli e a trarne valore, gli agenti sono aggiuntivi. Per quelle che non lo fanno, sono estrattivi.

Ciò di cui i nostri clienti hanno bisogno non è cambiato: essere scoperti, raccontare grandi storie, creare grandi esperienze e vendere. Ciò che è cambiato è che più della metà dei tuoi visitatori è ora software. Il nostro compito è aiutarti a servire entrambi i pubblici.

## Più traffico, meno entrate

Per trent'anni, il web ha funzionato secondo un unico accordo: lasciavi che i motori di ricerca indicizzassero il tuo sito, ti inviavano visitatori e tu trasformavi quei visitatori in un'attività commerciale. Essere trovati ed essere pagati erano la stessa cosa.

L'IA ha fatto crollare questo delicato equilibrio. Ora i motori di risposta leggono la pagina e danno al lettore un riassunto. Questo costa larghezza di banda ai siti web senza portare un essere umano a un sito dove avvengono gli annunci o i pagamenti. Le macchine hanno continuato ad arrivare, e il pubblico che pagava per il web ha smesso di raggiungere quei siti. Alcune delle categorie più visitate dai crawler, come il commercio al dettaglio, i software informatici, i servizi IT e i servizi finanziari, hanno visto il traffico umano diminuire fino al 40 % in meno di un anno.

Il risultato è che le entrate per richiesta stanno diminuendo mentre i costi aumentano. Ogni richiesta automatizzata costa ancora larghezza di banda, capacità di calcolo e capacità di origine, e una quota crescente di queste richieste non porta alcun referral, nessuna impressione pubblicitaria e nessun abbonamento. Il nostro primo istinto è stato quello di bloccare tutto il traffico automatizzato. L'anno scorso abbiamo consigliato di bloccare i crawler di addestramento IA sui nuovi domini, in modo che i proprietari di siti potessero almeno dire no all'utilizzo dei loro contenuti per costruire modelli. Nella primavera del 2025, il 22 % delle richieste di crawler che abbiamo visto erano per l'addestramento IA (secondo lo scopo dichiarato dei crawler). A giugno 2026, era il 52 %. Il problema è che un "no" generale non è un approccio sufficientemente sfumato per l'economia di Internet che si sta costruendo in questo momento.

L'opportunità è lì per chi vuole servire gli agenti. Farlo bene significa essere all'avanguardia di un nuovo modello di business. Farlo male porterà agli stessi risultati di generazioni di siti web che si sono trovati dal lato sbagliato dei cambiamenti degli algoritmi dei motori di ricerca.

## Una parte di quel traffico è un cliente

Un agente che prenota un tavolo, confronta preventivi assicurativi o acquista un set di dati per un ricercatore è un cliente. Semplicemente non è umano.

La parte in più rapida crescita del traffico automatizzato non sono più i crawler. Sono gli agenti: software che recupera pagine per conto di una persona, spesso perché l'essere umano ha posto una domanda a un chatbot. Questo traffico di agenti segue le routine umane, con un ritmo settimanale e un calo durante le vacanze estive. Rifiutare un agente potrebbe significare rifiutare la persona che lo ha inviato.

Gli agenti si comportano anche diversamente dai crawler di addestramento. Un crawler di addestramento raccoglie le tue pagine per costruire un modello. Un agente ritorna ogni volta che qualcuno fa una domanda su quel contenuto, quindi questo traffico cresce con il numero di domande che le persone fanno, non con quanto si pubblica.

Non si può fare affari con un pubblico che non si può vedere, non si può distinguere, per cui non si possono stabilire condizioni e che non si può addebitare. Fino a poco tempo fa, per la maggior parte del traffico web non umano, nessuna di queste quattro cose era possibile.

### Scopri chi ti visita davvero

**"Bot IA" non significa più nulla di utile.** Ciò che conta è cosa fa un bot. **AI Crawl Control** , **Business Insights** e **BotBase** di Cloudflare mostrano ai proprietari di siti chi sta facendo crawling, cosa viene preso, cosa ritorna e quali dei tuoi URL sono più richiesti.

Il nome di un bot vale qualcosa solo se ci si può fidare di esso. Con **Web Bot Auth** , gli operatori, tra cui OpenAI, Google e AWS, firmano crittograficamente le richieste dei loro agenti, così un sito può distinguere un vero agente da un impostore senza dover indovinare dagli indirizzi IP o dalle stringhe user-agent. Vediamo più di 500 miliardi di richieste di bot verificate ogni settimana

### Stabilisci le tue condizioni

A luglio, abbiamo sostituito il singolo interruttore "blocca bot IA" con [controlli separati per ricerca, agente e addestramento](https://blog.cloudflare.com/content-independence-day-ai-options/), disponibili su ogni piano, incluso quello gratuito. I dati hanno mostrato perché questa distinzione era necessaria. Meno dell'1 % dei siti su Cloudflare blocca i crawler di ricerca, mentre il 17 % blocca l'addestramento. I proprietari di siti non hanno mai cercato di nascondersi. Ma con l'ascesa del traffico agentico e i nuovi modi in cui gli agenti usano le informazioni, si sono ritrovati improvvisamente senza visibilità su come venivano utilizzati i loro contenuti, senza alcuna scelta in merito. Essere trovati non garantisce più di essere pagati e, anche quando succede, non bisognerebbe permettere di farsi sfruttare.

Ciò è particolarmente difficile nel caso dei crawler a uso misto. Quando un bot fa sia ricerca che addestramento, rifiutare l'uno significa rifiutare l'altro. Il 15 settembre, abbiamo rilasciato [Disallow AI Training](https://blog.cloudflare.com/accountable-mixed-use-ai-crawlers/), una soluzione che mantiene il tuo sito indicizzato per la ricercar grazie a meccanismi specifici del crawler per istruire l'operatore a non usare i tuoi dati per l'addestramento. Apple, Google e Microsoft si sono impegnati a rispettarlo. [Cloudflare Radar](https://radar.cloudflare.com/ai-insights#ai-bot-transparency) monitora anche pubblicamente il comportamento dei crawler.

I nuovi domini vedono ora configurazioni consigliate basate su come il sito guadagna, piuttosto che su quale software lo visita. Per i siti finanziati dalla pubblicità, puoi facilmente vietare l'addestramento e bloccare gli agenti sulle pagine che contengono annunci, perché un annuncio paga solo quando una persona lo vede. Puoi modificare queste impostazioni in qualsiasi momento.

### Fatti pagare

Nell'agosto 2026, abbiamo descritto [l'Internet agentico che stiamo costruendo](https://blog.cloudflare.com/the-agentic-internet/) come leggibile, individuabile, richiamabile e pagabile. L'ultima parola, pagabile, è quella che determina se il web aperto può autofinanziarsi. Il web ha bisogno di un modo per dire '_sì, se paghi_ ' invece di un semplice '_sì_ ' o '_no_ '.

Il mercato delle licenze mostra sia l'entità della domanda che dove si trovano le lacune. Dal 2023 sono stati firmati più di 50 accordi tra editori e IA. Quasi tutti sono su misura e bilaterali, tra grandi editori e grandi aziende IA. Dimostrano che i contenuti hanno valore. Ma non raggiungono la maggior parte del web, né la maggior parte degli acquirenti.

Le risorse non vanno vendute tutte nello stesso modo. I contenuti e i set di dati di alto valore hanno bisogno di una rete fidata, dove gli acquirenti vengono identificati e riferiscono come è stato utilizzato il lavoro. Servizi come le API e gli strumenti MCP non funzionano così: ogni richiesta è l'utilizzo.

Stiamo lavorando per entrambi i casi.

Il [Pay Per Use](http://blog.cloudflare.com/pay-per-use) raggiunge i siti che il licenziamento diretto non può raggiungere. La maggior parte degli editori non otterrà mai un accordo su misura con ogni azienda IA e nessuna azienda IA può negoziare con milioni di siti. Il Pay Per Use è il ponte: non addebita per il crawling ma paga quando il contenuto viene effettivamente utilizzato. Ogni acquirente è un crawler verificato, questo è ciò che rende questa una rete fidata e ognuno definisce cosa conta come utilizzo e quanto pagherà.

Gli editori vedono l'offerta, scelgono se aderire e possono rinunciare quando smette di funzionare per loro. L'acquirente segnala ogni utilizzo, Cloudflare verifica quei rapporti, poi fattura all'acquirente e paga l'editore. Il reporting è importante quanto il pagamento. Gli editori vedono cosa è stato usato, quando e quanto hanno guadagnato, e, dove l'acquirente lo segnala, informazioni su quali domande hanno portato alla luce il loro lavoro. Gli accordi di licenza raramente mostrano nulla di tutto ciò. Crea un ciclo di feedback: gli editori imparano cosa chiedono davvero le persone, e da ciò possono decidere cosa coprire, cosa aggiornare e cosa rendere facilmente disponibile agli agenti.

Non ci sarà un'unica definizione di utilizzo. Un motore di ricerca che cita una fonte, un agente di ricerca che cita un passaggio e un agente di acquisto che completa un acquisto creano diversi tipi di valore, e ognuno vorrà il proprio modello di business. Gli acquirenti possono partecipare attraverso più modelli di business usando le stesse basi, senza nuova integrazione per gli editori. Prendi una rivista di settore per ingegneri navali, con qualche migliaio di abbonati e poche possibilità di un accordo di licenza IA. Viene pagata da ogni azienda IA partecipante che si avvale del suo lavoro.

[Monetization Gateway](https://blog.cloudflare.com/monetization-gateway-beta) cattura valore che non aveva mai avuto modo di cambiare mani. Account, chiavi API e abbonamenti funzionano per i clienti che già conosci, non per un agente che vuole una singola ricerca da un servizio che non ha mai usato prima. La nostra beta chiusa consente ai clienti Cloudflare statunitensi idonei di fissare un prezzo su qualsiasi cosa che passa attraverso noi, usando il linguaggio delle regole che già conoscono. Quando una regola corrisponde, restituiamo HTTP 402 Payment Required usando il protocollo aperto x402, e l'agente paga il venditore direttamente.

Questo fa molto di più che recuperare entrate perse. Gli agenti sono clienti a tutti gli effetti: pagano per i dati, le API e gli strumenti che utilizzano, che la richiesta sia l'intero acquisto o un passaggio in un'attività più ampia.

Monetization Gateway prezza per richiesta, per interrogazione o per token, a prezzi fissi o con limite massimo. Un sito di statistiche sportive basato sulla pubblicità può addebitare una frazione di centesimo ogni volta che un agente chiede "chi guida la classifica degli assist?" Quando abbiamo annunciato Monetization Gateway, migliaia di venditori si sono iscritti alla lista d'attesa, e la loro richiesta più comune era "addebitare agli agenti, non agli umani". Siamo anche il nostro primo cliente. AI Gateway di Cloudflare usa Monetization Gateway per consentire agli agenti di pagare per l'inferenza, così troviamo i punti critici prima dei nostri clienti.

Per gli acquirenti, entrambi i prodotti superano una pagina di blocco: accesso affidabile e un modo per raggiungere milioni di siti invece di un accordo di licenza o una chiave API alla volta. Ogni richiesta pagata lascia una ricevuta che mostra cosa è stato acquistato e che è stato pagato.

Sia Pay Per Use che Monetization Gateway sono scommesse, costruite con i clienti su elementi fondamentali condivisi: identità, misurazione, prezzi, liquidazione e analisi. Lavorano insieme, così un editore può vietare l'addestramento, consentire la ricerca, guadagnare dalle risposte IA e addebitare agli agenti per articolo da un unico dashboard. I prezzi e la scopribilità non sono ancora risolti, motivo per cui entrambi vengono lanciati come beta, modellati da clienti reali e transazioni reali.

### Rendere ogni richiesta meno costosa

Il pagamento è la risposta al calo delle entrate. L'aumento dei costi è un problema diverso, e gran parte di esso è semplicemente spreco. La maggior parte dei crawler scarica ancora pagine costruite per gli esseri umani, più e più volte, per estrarre pochi paragrafi di testo. Troppo spesso, i bot crawlano siti che non sono cambiati dall'ultimo tentativo. Questo brucia larghezza di banda per il sito e capacità di calcolo per il crawler, e avviene prima che venga scritta qualsiasi risposta. Stiamo lavorando con i nostri clienti e i crawler su strumenti che aiuteranno. Oggi puoi vedere il consumo di larghezza di banda per operatore nel nostro dashboard.

A luglio, abbiamo annunciato un [progetto di ricerca congiunto con OpenAI](https://www.cloudflare.com/press/press-releases/2026/cloudflare-announces-research-pilot-with-openai/), un pilot senza precedenti per esplorare come le informazioni della rete globale di Cloudflare possono aiutare i motori di ricerca IA a scoprire e indicizzare contenuti rilevanti sul web aperto in modo più efficiente ed efficace. Abbiamo in programma di condividere i nostri risultati iniziali nelle prossime settimane.

Per i nostri clienti, stiamo rilasciando strumenti ed esperienze in un clic per ottimizzare i loro siti per questo nuovo tipo di traffico. [Markdown for Agents](https://blog.cloudflare.com/markdown-for-agents/) consente agli agenti di leggere una pagina senza lo stile aggiuntivo pensato per gli occhi umani e [WebMCP](https://blog.cloudflare.com/webmcp/) consente a un sito di esporre azioni direttamente invece di far indovinare agli agenti quale pulsante premere.

## Perché costruire su Cloudflare

Più del 20 % del web è dietro la rete di Cloudflare, e lo sono anche quasi l'80% delle principali aziende IA. Vediamo entrambi i lati di questo mercato. Costruiamo le basi per la visibilità, l'identità, i controlli e la liquidazione, e lasciamo che il mercato determini il valore delle cose.

Il vecchio accordo è finito, e quello nuovo è ancora in fase di scrittura. Insieme possiamo plasmare ciò che accade dopo.

In una versione, poche aziende controllano come gli agenti trovano le cose, provano chi sono e pagano, e tutti gli altri passano attraverso di loro. Nell'altra, questi elementi sono standard aperti che chiunque può implementare, e un sito di qualsiasi dimensione può stabilire le proprie condizioni ed essere pagato. Noi preferiamo quest'ultima.

Ecco perché queste basi funzionano su standard aperti come x402 e Web Bot Auth, in modo che chiunque possa costruire su di esse. I proprietari di dominio scelgono i propri provider di identità, i propri processori di pagamenti, i propri partner agenti. Cloudflare è un'opzione, non l'intero stack.

Per decenni, il web è stato pagato dalle persone che lo visitavano. Ora il software che le visita per loro conto può pagare la sua parte.

]]>01M4D6AX3JRR81MRM1HFY8NY64Tutto ciò che abbiamo lanciato durante la Agents Weekhttps://blog.cloudflare.com/it-it/agents-week-review-august-2026/ Thu, 13 Aug 2026 08:11:17 GMTLa nostra ultima Agents Week è giunta al termine. Ecco un riepilogo di tutti gli annunci che abbiamo fatto, da Wallets a Radar.AgentiAgents WeekCloudflare OneCloudflare WorkersIAPiattaforma per sviluppatoriSASESviluppatoriZero TrustAll'inizio della Agents Week, Rita[ ha condiviso](https://blog.cloudflare.com/agents-week-welcome/) che gli agenti rappresentano la prossima evoluzione dell'informatica: non solo come una nuova applicazione dell'IA, ma anche come una nuova classe di software che sta plasmando il modo in cui le persone interagiscono con la tecnologia e il modo in cui il software interagisce con Internet. Nel corso dell'[​ultimo anno](https://www.cloudflare.com/innovation-week/ai-week-2025/updates/) circa, ci siamo proposti di esplorare cosa significhi questo cambiamento per gli sviluppatori e i clienti che creano app native per l'IA e per l'infrastruttura necessaria a supportarle. Man mano che gli agenti diventano più capaci e autonomi, le sfide si estendono oltre i modelli stessi, riguardando l'identità, la comunicazione, l'orchestrazione, la memoria, l'osservabilità e la sicurezza.

Nel corso dell'ultima settimana abbiamo condiviso come stiamo integrando questi elementi sulla piattaforma Cloudflare per servire un Internet agentico. Ogni giorno abbiamo presentato nuovi strumenti, prodotti e idee per costruire un Internet in cui umani e agenti[ cooperano invece di scontrarsi](https://blog.cloudflare.com/the-agentic-internet/).

### **Lunedì 3 agosto**

Lunedì ci siamo concentrati sui fondamenti per la creazione e l'esecuzione di app intelligenti e autonome: l'ambiente di runtime e l'infrastruttura su cui si basano gli agenti.

[Il tuo agente ha bisogno di un computer, non di un container: ecco @cloudflare/computer](https://blog.cloudflare.com/cloudflare-computer/)| @cloudflare/computer introduce un nuovo runtime progettato per gli agenti in grado di scegliere l'ambiente più adatto al lavoro da svolgere.  
---|---  
[Workers RPC ora funziona con Python e JavaScript](https://blog.cloudflare.com/python-workers-rpc/)| I Workers Python e JavaScript possono ora comunicare direttamente fra loro, facilitando i progetti in linguaggi misti.  
[Più piccolo, più veloce, più sicuro: eseguire Kimi e GLM su larga scala](https://blog.cloudflare.com/smaller-faster-safer-models/)| Scopri come possiamo gestire i modelli di grandi dimensioni in modo più efficiente, senza compromettere la qualità, l'affidabilità o la sicurezza.  
[Presentazione dell'API per l'utilizzo fatturabile: visibilità programmatica dei costi per Cloudflare](https://blog.cloudflare.com/billable-usage-api/)| Un modo più semplice per monitorare l'utilizzo e i costi dei nostri prodotti self-service.   
[Cloudflare Workers e Containers ora supportano connessioni TCP in entrata e gRPC](https://blog.cloudflare.com/grpc-workers/)| Integra backend di IA vocale o altri agenti vocali in tempo reale con Cloudflare Workers.  
  
### **Martedì 4 agosto**

Martedì è stato presentato il ciclo di vita dello sviluppo degli agenti (ADLC) e le primitive che consentono di portare il software agentico dal prototipo alla produzione.

[Il ciclo di vita dello sviluppo degli agenti è arrivato su Cloudflare](https://blog.cloudflare.com/agent-development-lifecycle/)| Superare il ciclo di vita dello sviluppo del software (SDLC) con l'ADLC: la nostra visione per portare gli agenti dal prototipo alla produzione e i principi fondamentali che sono alla base della prossima generazione di "software factory".  
---|---  
[Introduzione: Cloudflare Agents](https://blog.cloudflare.com/agents-on-cloudflare/)| Crea agenti su Cloudflare e osserva ogni esecuzione in diretta, con tracciamento, riproduzione e approvazione umana di ciò che accade in produzione.  
[Il tuo agente può ora eseguire il debug di Workers con tracciamento locale](https://blog.cloudflare.com/local-tracing/)| Integrare il tracciamento distribuito negli ambienti di sviluppo locali, semplificando il lavoro degli agenti nell'individuazione e nel debug dei problemi prima che raggiungano l'ambiente di produzione.  
[Annuncio di Cloudflare Wallets: il portafoglio programmabile per l'Internet agentico](https://blog.cloudflare.com/wallets/)| I portafogli digitali introducono un metodo sicuro che consente agli agenti di effettuare transazioni in qualità di partecipanti all'emergente economia agentiva.  
[Esegui CI/CD per milioni di repository sulla tua piattaforma, su Cloudflare](https://blog.cloudflare.com/ci-workflows/)| CI/CD programmabile; pipeline scritte in codice, non in file di configurazione, con un agente che ripara gli errori e prepara la correzione per la revisione.  
[Come Cloudflare impone gli standard di ingegneria utilizzando l'IA](https://blog.cloudflare.com/engineering-standards-enforcement/)| Come utilizziamo l'automazione basata sull'intelligenza artificiale nei nostri flussi di lavoro di sviluppo per mantenere allineati gli standard e i processi di codifica, aiutando le nostre software factory a fornire codice di qualità e coerente su larga scala.  
[Come abbiamo costruito una software factory per azzerare il numero di problemi di GitHub di Astro](https://blog.cloudflare.com/astro-issue-triage/)| Automatizzare l'analisi, la categorizzazione e l'instradamento dei problemi per ridurre al minimo il lavoro di manutenzione del software e massimizzare la produttività degli sviluppatori.  
  
### **Mercoledì 5 agosto**

Mercoledì abbiamo esteso il modello Zero Trust dagli utenti e dai dispositivi agli agenti stessi e abbiamo condiviso il modo in cui lo stiamo implementando internamente in Cloudflare.

[Il modello di accesso dell'agente](https://blog.cloudflare.com/the-agent-access-model/)| Un quadro di riferimento per consentire agli agenti di accedere in modo sicuro a risorse e servizi per conto degli utenti, in un Internet sempre più popolato da agenti.   
---|---  
[Come stiamo ripensando il lavoro in Cloudflare con Cloudflare OS](https://blog.cloudflare.com/how-we-use-ai-with-cloudflare-os/)| Come abbiamo integrato l'intelligenza artificiale nel nostro modello operativo interno, consentendo ai team di lavorare in modo più intelligente e veloce senza rinunciare alla sicurezza o alla supervisione.  
[Cloudflare OS: una piattaforma aperta per agenti, app e lavoro](https://blog.cloudflare.com/cloudflare-os/)| Abbiamo reso open source la piattaforma che i nostri team utilizzano per creare app, automatizzare i processi e accedere in modo sicuro ai sistemi interni.   
[Individuare comportamenti anomali dell'IA con analisi sensibili all'identità](https://blog.cloudflare.com/identity-aware-ai-gateway/)| Attribuisci l'attività dell'IA a utenti e sistemi reali, rendendo più facile individuare eventuali anomalie e picchi di spesa.  
[WriteGuard: controlli granulari per server MCP](https://blog.cloudflare.com/mcp-portal-writeguard-private-beta/)| Fornire ai clienti gli stessi strumenti che utilizziamo, per un maggiore controllo sulle chiamate di strumenti rischiose e ridurre la probabilità che gli operatori apportino modifiche indesiderate.  
  
### **Giovedì 6 agosto**

Giovedì abbiamo definito l'Internet agentico e il modo in cui i proprietari di siti Web, i publisher e gli agenti possono tutti contribuire a un Internet che funzioni sia per le persone che per gli agenti.

[Costruire un Internet agentico aperto: leggibile, individuabile, richiamabile e pagabile](https://blog.cloudflare.com/the-agentic-internet/)| Un modello per un Internet agentico in cui i publisher mantengono il controllo, gli agenti ottengono un accesso utile a ciò di cui hanno bisogno e i protocolli aperti consentono a entrambe le parti di effettuare transazioni.  
---|---  
[Fornisci a qualsiasi sito web un'interfaccia WebMCP](https://blog.cloudflare.com/webmcp/)| Un'anteprima di WebMCP, che introduce un nuovo (e molto semplice) approccio per rendere i siti web e le applicazioni web individuabili e utilizzabili dagli agenti.  
[Dalla posizione in classifica alla raccomandazione: prepara il tuo sito a prosperare nell'era degli agenti IA](https://blog.cloudflare.com/aeo/)| Integrare le pratiche SEO nelle strategie AEO (Answer Engine Optimization) per migliorare la modalità di scoperta, comprensione e visualizzazione dei contenuti web da parte degli agenti.  
[Vi presentiamo Kitesurf: il browser agent-first che funziona in ambienti V8 isolati su Cloudflare Workers.](https://blog.cloudflare.com/kitesurf/)| Un browser progettato specificamente per gli agenti, che sacrifica la precisione grafica al pixel a favore di un minore utilizzo di memoria e CPU.  
[La nuova generazione di MCP](https://blog.cloudflare.com/mcp-v2/)| MCP ha subito una riscrittura. MCPv2 introduce la prossima evoluzione del supporto MCP, semplificando l'implementazione e la scalabilità delle applicazioni agentiche.  
[Cloudflare AI Search: offri ai tuoi agenti un motore di ricerca per i tuoi dati](https://blog.cloudflare.com/ai-search-easier/)| AI Search trasforma i tuoi file o il tuo sito web in un motore di ricerca pronto per gli agenti con un solo comando.  
  
### **Venerdì 7 agosto**

Venerdì abbiamo puntato i riflettori su ciò che sta realmente accadendo: cosa fanno davvero gli agenti sul web, dove è in esecuzione l'IA nelle tue app, chi contribuisce agli ecosistemi e quali sono i nuovi strumenti per analizzare i dati di Internet.

[Svelare i comportamenti buoni e cattivi su Internet agentico](https://blog.cloudflare.com/good-and-bad-agentic-behaviors/)| I bot non sono sempre cattivi e gli esseri umani non sono sempre buoni; è necessario riformulare le strategie di mitigazione dei bot basandosi sulla fiducia continua piuttosto che sul rischio una tantum.  
---|---  
[Unificare Workers AI e AI Gateway in un unico piano di controllo IA](https://blog.cloudflare.com/workers-ai-gateway-unification/)| Un binding, un portafoglio, un dashboard per chiamare qualsiasi modello IA; il prossimo sarà il routing basato sul modello.  
[Annuncio di Cloudflare Ambassadors, Community Engineers e un altro milione di dollari in finanziamenti open source](https://blog.cloudflare.com/community-program-refresh/)| La nostra rinnovata iniziativa Community introduce due nuovi programmi: Cloudflare Ambassadors per i leader della community e Community Engineers per i manutentori di progetti open source, oltre a un ulteriore finanziamento di 1 milione di dollari per l'open source nei prossimi due anni.  
[Introduzione di Radar Researcher: uno strumento IA per esplorare i dati di Internet in linguaggio chiaro](https://blog.cloudflare.com/introducing-radar-researcher/)| L'assistente di ricerca IA di Radar: domande formulate in linguaggio semplice, risultati in formato grafico interattivo.  
  
### **L'Agents Week è finita, ma noi abbiamo appena cominciato**

A distanza di cinque giorni, la risposta alla domanda di Rita "[Di cosa ha bisogno il tuo agente da un cloud di agenti?](https://blog.cloudflare.com/agents-week-welcome/)" comincia a prendere forma. Ha bisogno di un livello di esecuzione e di primitive su cui funzionare, di un ciclo di sviluppo che si auto-scrive sempre più, di un accesso sicuro per le persone e gli agenti che svolgono il lavoro, di un Internet agentico e degli esseri umani e delle comunità che mantengono il tutto ancorato alla realtà. C'è ancora molto da fare, ma la forma di ciò che ci aspetta sta diventando più chiara: un Internet che supporti nativamente gli esseri umani per cui è stato creato e gli agenti che ora agiscono per loro conto.

Il nostro lavoro non finisce qui. Tieni d'occhio il nostro[ changelog](https://developers.cloudflare.com/changelog/) per gli ultimi aggiornamenti. E se stai collaborando con noi alla realizzazione di questo progetto, ci farebbe piacere avere tue notizie! Venite a trovarci su[ X](https://x.com/cloudflaredev) o [​Discord](https://discord.com/invite/cloudflaredev).

]]>01KZX2BP7J31ZN77V2CSD41BK4Svelare i comportamenti buoni e cattivi su Internet agenticohttps://blog.cloudflare.com/it-it/good-and-bad-agentic-behaviors/ Wed, 12 Aug 2026 06:44:12 GMTCloudflare sta spostando la mitigazione dei bot da una valutazione del rischio puntuale a una valutazione continua della fiducia. Scopri come i nostri sistemi, tra cui BotBase e Precursor, valutano i nuovi comportamenti, sia positivi che negativi, di bot e agenti, e prova la nostra simulazione Precursor Trace per vedere come i tuoi movimenti del cursore verrebbero valutati come umani o da un bot.AgentiAgents WeekAI BotsGestione dei botNetwork ServicesInternet non è una singola corsia di traffico. Per molto tempo, la regola generale nella sicurezza web è stata che i bot sono cattivi, mentre gli esseri umani sono buoni. Naturalmente, siamo ben oltre questa generalizzazione. Gli esseri umani possono essere fraudolenti e i bot possono essere utili a diversi livelli. I proprietari dei siti web desiderano attivamente che una certa quantità di traffico automatizzato interagisca con i nostri siti per rendere Internet funzionale e facilmente reperibile.

A complicare ulteriormente le cose, il confine tra "umano" e "bot" si sta facendo sempre più labile. Ora abbiamo un tipo di traffico "ibrido" in cui una singola sessione passa da umana ad agentica e viceversa. Pensa a un utente che naviga in un negozio e poi affida il processo di pagamento a un assistente virtuale.

Come fanno dunque i proprietari di siti web a gestire questo tipo di complessità? Ciò che conta qui è valutare i **comportamenti**. Questo comportamento costituisce un abuso? È dannoso? Quali sono i rischi in questo caso e posso fidarmi di questo visitatore in base alle sue azioni? Per risolvere questo problema è necessario andare oltre i controlli statici e puntuali. Per valutare la fiducia è necessario analizzare i comportamenti in modo continuativo.

In questo post, condivideremo uno sguardo approfondito sulla strategia del team Web Integrity & Trust (che si occupa di bot e frodi) per individuare e analizzare comportamenti, sia positivi che negativi, e fornire strumenti per aiutare i proprietari dei siti web ad affrontare le sfide emergenti nel mutevole Internet agentico. Condivideremo anche i risultati relativi al traffico agentico dal lancio di[ Precursor](https://blog.cloudflare.com/introducing-precursor/) e una simulazione in cui potrai vedere come i tuoi movimenti del cursore verrebbero valutati (come umani o da bot), oltre ad alcuni interessanti aggiornamenti di lancio previsti a breve.

## **Definire rischio e fiducia**

Parliamo della distinzione tra **rischio** e **fiducia** , così come ne parliamo all'interno dei team di Cloudflare che si occupano del rilevamento dei bot. Questi due concetti vengono spesso considerati come poli opposti di un continuum. In Cloudflare, li consideriamo valori indipendenti, ma reciproci. La fiducia è il fattore essenziale per prendere decisioni consapevoli su come gestire il traffico. 

Il rischio indica la probabilità che qualcosa, come una richiesta o un'azione, si riveli dannoso, ed è spesso effimero. La fiducia, tuttavia, si costruisce nel tempo ed è basata sulla reputazione.

Possiamo illustrarlo con un esempio tratto dalla vita reale: immagina di stare guardando la televisione a casa la sera, quando improvvisamente senti suonare ripetutamente il campanello. Oltre ad essere fastidioso, questo comportamento è strano. I frenetici squilli del campanello a tarda notte sono allarmanti.

Dai un'occhiata alla telecamera di sicurezza e vedi che a suonare il campanello è il tuo migliore amico che abita accanto a te. Certo, ti fidi del tuo migliore amico e scommettiamo che lo lasceresti entrare.

In questo esempio, non sarebbe sufficiente dire: "Rifiuta chiunque suoni il mio campanello di notte" o "Rifiuta chiunque suoni il mio campanello più di 10 volte". Ancora una volta, la fiducia è l'ingrediente essenziale.

Tornando al traffico su Internet, la strategia che adottiamo nello sviluppo di prodotti per contrastare bot e frodi si concentra sulla creazione di un intero ecosistema basato sulla fiducia. Il nostro obiettivo è fornire agli amministratori dei siti gli incentivi e gli strumenti necessari per promuovere comportamenti che rendano Internet più sicuro per tutti: partendo dal blocco delle attività dannose, fino ad arrivare a incoraggiare la partecipazione a un Internet più sicuro.

## **Comportamenti virtuosi, fondati sulla trasparenza**

Partendo dall'alto: cosa si intende per buon comportamento? Possiamo trarre chiari esempi dai bot e dagli agenti verificati all'interno di BotBase. Il mese scorso abbiamo annunciato una[ tassonomia pragmatica aggiornata per i bot affidabili che monitoriamo nel nostro sistema](https://blog.cloudflare.com/content-independence-day-ai-options/), , riducendo la definizione di "[Verificato](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/)" a due elementi: 1) dichiararsi onestamente e 2) non abusare della fiducia guadagnata. 

La trasparenza tra il proprietario di un sito e l'operatore di un bot consente una relazione simbiotica: i proprietari dei siti possono specificare quali comportamenti e utilizzi dei dati desiderano consentire sui propri siti web, e agli operatori dei bot può essere concesso l'accesso più facilmente. La trasparenza favorisce la fiducia nel rapporto; se non hai nulla da nascondere, dichiarare la tua identità dovrebbe ridurre gli attriti con i siti che desiderano consentire i tuoi comportamenti.

[BotBase](https://developers.cloudflare.com/bots/botbase/) non è pensato solo per dichiarare "chi è buono". È destinato a essere un elenco di tutti i bot e agenti conosciuti e fornire al contempo informazioni dettagliate. Rispetto alla nostra precedente directory di bot, che includeva solo bot noti per essere affidabili, BotBase è in grado di tracciare anche bot e agenti _meno che affidabili_. Perché? Poiché i nostri sistemi tracciano e convalidano i comportamenti degli utenti noti per essere affidabili, disponiamo degli strumenti necessari per identificare i casi in cui queste aspettative non vengono soddisfatte. Se abusi della fiducia sulla rete Cloudflare, **non** dovresti essere autorizzato facilmente, quindi non sarai verificato.

## **Comportamenti scorretti: palesi, subdoli e tutto ciò che sta nel mezzo**

Qualche settimana fa abbiamo annunciato[​](https://blog.cloudflare.com/introducing-precursor/) [Precursor](https://blog.cloudflare.com/introducing-precursor/), un sistema continuo lato client per rilevare anche il traffico di bot _sottilmente inumano_ che può passare inosservato se si valutano solo i segnali di rete. Quando un cliente abilita Precursor, il rilevamento JavaScript viene iniettato tramite la CDN, quindi non è necessario sedersi al computer e capire dove o come rieseguire questi rilevamenti. Inoltre, Precursor valuta il comportamento dell'utente[ continuamente durante tutta la sessione](https://developers.cloudflare.com/cloudflare-challenges/precursor/), quindi niente più scorciatoie gratuite per il traffico abusivo che è riuscito a superare i controlli lato client e lato browser anche solo una volta.

Applicando il nostro framework di rischio e fiducia a questi rilevamenti lato client, possiamo sottolineare che i CAPTCHA o gli ostacoli una tantum sono basati sul rischio, il che significa che mancano di _contesto_. D'altro canto, la verifica tramite segnali comportamentali si basa sulla fiducia, poiché può cogliere più indizi contestuali dall'intera sessione utente. Precursor è lo strumento che ci permette di analizzare questo comportamento. In sintesi, Precursor è così potente perché:

  1. Fornisce rilevamento basato sulla fiducia durante l'intera sessione utente.
  2. **Fa aumentare i costi per gli sviluppatori di bot** per replicare il comportamento umano su una timeline multipagina.



Rendendo _economicamente svantaggioso_ per gli sviluppatori di bot eludere questi rilevamenti, vinciamo la sfida avversaria.

Cosa abbiamo imparato dal lancio? Osservando un periodo di sole 24 ore al momento della stesura di questo blog, possiamo notare **206 milioni di eventi di valutazione Precursor** , distribuiti su **73.438 zone** sulla rete Cloudflare.

Nei dati possiamo individuare degli schemi che rivelano elementi che avevamo sospettato al momento dell'avvio del sistema di rilevamento, ma che ora possiamo convalidare su decine di migliaia di domini:

  * Spesso, durante una sessione, si verificano comportamenti sospetti che i sistemi di rilevamento istantaneo non sarebbero in grado di individuare.
  * **Il comportamento spesso passa da umano ad agente e viceversa nel corso di una sessione**. In questi casi, è importante comprendere l'_intento_ in modo che i proprietari del sito non blocchino i flussi utente che effettivamente desiderano.
    * Ciò evidenzia l'importanza di un sistema di classificazione dei bot che consenta ai proprietari di siti web di gestire il traffico in base al caso d'uso, allo scopo e all'utilizzo dei dati. È proprio per questo motivo che abbiamo dato priorità agli aggiornamenti della tassonomia di BotBase.



Per chi fosse curioso di saperne di più su come funziona Precursor, abbiamo condiviso un'anteprima: come i segnali che analizziamo ci hanno dimostrato che errare è umano, nel nostro[ post del blog](https://blog.cloudflare.com/introducing-precursor/) di annuncio. **Oggi facciamo un ulteriore passo avanti: offriamo a chiunque su Internet una demo interattiva che simula il modo in cui Precursor traccia i movimenti del cursore.**

**[Precursor Trace](https://precursor-trace.cloudflare.app) **è ora attivo e mostra come valuteremmo i _movimenti del tuo_ cursore utilizzando parte del meccanismo di rilevamento di Precursor. Qui puoi vedere se stai accelerando o correggendo, il ritmo e la consistenza del movimento del cursore e molto altro ancora: tutte cose a cui probabilmente non hai mai pensato quando interagisci con un computer. Provalo!

## **Adaptive Intelligence arriverà presto**

I[ motori di rilevamento dei bot](https://developers.cloudflare.com/bots/concepts/bot-detection-engines/) di Cloudflare possono produrre[ risultati diversi](https://developers.cloudflare.com/bots/concepts/bot-score/#bot-groupings) quando valutano se una determinata richiesta è automatizzata o meno. Per le richieste considerate automatizzate, la valutazione può essere 1) sicuramente automatizzata, sulla base di metodi comprovati e deterministici o di impronte digitali dei bot, oppure 2) probabilmente automatizzata, sulla base del punteggio predittivo di Bots ML di Cloudflare.

Storicamente,[ Bots ML](https://developers.cloudflare.com/bots/concepts/bot-score/#machine-learning) è stato aggiornato in versioni, il che significa che abbiamo annunciato ogni nuova versione del modello come lancio di un prodotto. Questo ritmo non funziona quando i bot si adattano nell'arco di ore o addirittura minuti.

Adaptive Intelligence, un motore di rilevamento completamente nuovo, è diverso da qualsiasi altra cosa che abbiamo sviluppato finora nell'ambito del machine learning per bot. **Il modello stesso è adattivo**. Ha imparato da tutto ciò che abbiamo visto in passato, ma soprattutto, _continuerà_ ad apprendere e ad autoregolarsi in base a ciò che vede. Adaptive Intelligence si aggiornerà automaticamente in base a un'ampia gamma di modelli di traffico che identifichiamo, dai comportamenti positivi a quelli negativi, e i clienti non dovranno più aggiornare formalmente a una nuova versione del modello per poter usufruire delle più recenti funzionalità di rilevamento predittivo dei bot. 

A breve tutti i clienti di Bot Management avranno accesso ad Adaptive Intelligence: resta sintonizzato per l'annuncio del lancio, in arrivo a breve.

## **Andare oltre il determinismo per influenzare il comportamento dei bot**

Finora ci siamo concentrati sul punto di vista di Cloudflare: strategia, rilevamento e tassonomia. Tutto ciò consente a Cloudflare di fornire ai proprietari di siti web gli strumenti necessari per impostare le politiche di traffico desiderate per i propri siti. Concentrandoci sul punto di vista del proprietario del sito web, vogliamo cogliere l'occasione per discutere alcune **mitigazioni avanzate** che consentono ai proprietari dei siti web di influenzare direttamente il comportamento dei bot.

Con tecniche di mitigazione più evidenti, ci troviamo di fronte a quello che abbiamo soprannominato il "problema degli antibiotici per i bot". Inviare sempre ai bot una risposta deterministica (come un blocco 403) facilita a un bot sviluppatore malevolo la possibilità di sondare, osservare e decodificare le tue difese.

Lo sappiamo, quindi stiamo progettando delle misure di mitigazione _specificamente pensate per limitare i bot_ , con approcci diversi per i bot dannosi rispetto ai bot benigni. Possiamo suddividerle in tre diversi approcci:

Approccio 1: imprevedibilità e azioni casuali. Applicare risposte casuali (tra blocco, richiesta di verifica o autorizzazione) al traffico sospetto automatizzato interrompe la logica di ritentativo automatico e il fingerprinting del bot.

Approccio 2:[ AI Labyrinth](https://developers.cloudflare.com/bots/additional-configurations/ai-labyrinth/), una risposta difensiva che intrappola i bot non autorizzati in un labirinto infinito di pagine web generate dall'IA. È possibile sprecare le risorse di calcolo e di scansione dei bot dannosi utilizzando il _depistaggio_. All'interno di AI Labyrinth, i proprietari dei siti avranno a disposizione tre opzioni, a seconda delle loro preferenze:

  * **Labirinto** : genera una rete infinita di pagine collegate che i bot possono seguire.
  * **Riepilogo** : fornisce ai crawler un riepilogo di una pagina generato da un LLM che sembra reale ma è completamente inutile come dato di addestramento per l'IA.
  * **Veleno** : fornisce contenuti deliberatamente falsi (come prezzi o inventario falsi) a un bot, inquinando i dati che raccoglie per l'addestramento dell'IA.



Approccio 3: accodamento per i bot buoni Non tutto il traffico agentico è negativo; la gestione delle code regola il flusso di traffico automatizzato legittimo (come gli agenti di acquisto diretti dall'utente) senza negare completamente il servizio.

Queste misure di mitigazione avanzate, specifiche per i bot, saranno implementate verso la fine dell'anno e consentiranno al proprietario del sito web di scegliere il livello di severità desiderato per le proprie misure di mitigazione.

Sappiamo inoltre che una difesa efficace è predittiva, ovvero in grado di autoapprendere e correggere la rotta senza bisogno di coinvolgere più esperti di sicurezza in una chiamata per impostare una soluzione reattiva che tenga conto dell'ultimo attacco furtivo. Potrebbe trattarsi di un sistema di regole "usa e getta", in cui l'insieme delle regole è di natura dinamica. Questo è voluto: se gli attacchi si evolvono costantemente, anche le difese devono farlo. Ecco perché ci impegniamo a mantenere sia il rilevamento che la mitigazione un passo avanti.

## **Crea l'ecosistema di fiducia che fa al caso tuo**

Chiunque può adottare misure per definire come gli agenti automatizzati interagiscono con la propria infrastruttura. 

Alcune cose da provare:

  * Attiva[ Precursor](https://developers.cloudflare.com/cloudflare-challenges/precursor/#get-started)
  * Sperimenta con[ Precursor Trace](https://integrityand.trust.cfdata.org/precursor-trace/)
  * Esplora[ BotBase](https://developers.cloudflare.com/bots/botbase/)



Abbandonando i controlli statici e puntuali e adottando una valutazione continua dell'affidabilità, riduciamo la necessità di combattere ripetutamente gli operatori di bot. Se non stai già utilizzando il [​rilevamento bot di Cloudflare](https://www.cloudflare.com/products/bot-mitigation/), provalo e crea l'ecosistema di fiducia più adatto alle tue esigenze.

]]>01KZTB9E2CDEC4EXZ0KQ9KEBDXDalla posizione in classifica alla raccomandazione: prepara il tuo sito a prosperare nell'era degli agenti IA.https://blog.cloudflare.com/it-it/aeo/ Tue, 11 Aug 2026 01:51:52 GMTPiù della metà delle richieste ora proviene da macchine, non da persone. Agent Readiness descrive quanto bene gli agenti riescono a trovare e leggere il tuo sito, mentre l'ottimizzazione del motore di risposta tiene traccia della frequenza con cui gli assistenti IA ti raccomandano.AEOAgentiAgents WeekDashboardIAMCPNovità sul prodottoPredisposizione agli agentiRadarIl tuo prossimo cliente potrebbe non trovarti tramite un motore di ricerca. Invece, chiederanno a un assistente IA: "Come faccio a fare X?", "Qual è l'opzione migliore per una persona come me?", "Occupatene tu per me" e un agente troverà la risposta, valuterà le opzioni e agirà per loro conto. Sempre più spesso, il momento decisivo per la scelta di un cliente si verifica all'interno della risposta di un modello prima ancora che un essere umano visualizzi la tua homepage.

Questo pubblico agentico è già qui: secondo i nostri calcoli, meno della metà di tutte le richieste di pagine HTML[ ora provengono da un essere umano](https://radar.cloudflare.com/traffic#bot-vs-human). Non tutte queste macchine sono agenti che agiscono per conto di una persona, ma questa percentuale sta crescendo rapidamente, e i motori di ricerca, gli assistenti agli acquisti e gli strumenti di ricerca influenzeranno la scelta delle aziende che verranno trovate e consigliate. In passato, per "visibilità" si intendeva il posizionamento nella pagina dei risultati di ricerca. Oggi significa essere trovati, letti e raccomandati con fiducia dagli agenti che guidano i tuoi clienti.

Le vecchie metriche, come i clic umani e le visualizzazioni di pagina, non forniscono più un quadro completo. Abbiamo trascorso del tempo a parlare con i proprietari di siti web che si trovavano a fissare log di accesso pieni di bot IA, completamente all'oscuro della capacità di tali bot di utilizzare il loro sito o di consigliare i loro prodotti e servizi agli utenti. Abbiamo sentito due domande principali:

  * Gli agenti possono effettivamente utilizzare il mio sito?
  * Mi stanno raccomandando?



Per aiutare i proprietari dei siti a rispondere a queste domande, abbiamo integrato il nostro[ lavoro precedente su Agent Readiness](https://blog.cloudflare.com/agent-readiness/) nel dashboard di Cloudflare, aggiungendo anche il nostro nuovo strumento Answer Engine Optimization (AEO). Questi strumenti trattano gli agenti come una base utente centrale per il tuo sito, mostrandoti come un agente lo vedrà e quanto spesso vieni raccomandato.

L'opportunità è grande e gli standard sono bassi, perché la maggior parte dei siti non è ancora pensata per questo tipo di utente. Così come agli albori della SEO venivano premiati i siti web ottimizzati per i motori di ricerca, ora verranno premiati i siti web creati per gli agenti. Gli agenti raccomanderanno quelli che sono facili da trovare, leggere e di cui ci si può fidare.

## **Diagnostica: il tuo sito è pronto per gli agenti?**

La diagnostica è il controllo tecnico all'interno di Agent Readiness. Analizza il tuo sito come farebbe un agente: verifica se ha i permessi di accesso e se può individuare i tuoi contenuti, scarica una copia pulita e leggibile automaticamente e individua le interfacce a cui può accedere. 

Mentre una persona carica la tua homepage, un agente accede al tuo robots.txt, la tua sitemap, le tue intestazioni di risposta, una versione Markdown del tuo contenuto e i metadati pubblicati per l'autenticazione e gli strumenti.

La funzione diagnostica esegue questi controlli su un nome host e aggrega i risultati in un'unica visualizzazione dello stato di preparazione dell'agente, da "Non pronto" a completamente nativo dell'agente. Ogni controllo viene valutato con esito positivo, negativo o neutro, con una nota che ne spiega l'importanza e una traccia documentale che mostra la richiesta e la risposta esatte osservate.

I controlli sono raggruppati in base al livello di difficoltà, così saprai da dove iniziare:

  * Risultati rapidi: le basi ad alto impatto che mancano alla maggior parte dei siti, incluso un robots.txt leggibile dai crawler, una sitemap XML, regole per crawler IA e servire Markdown pulito agli agenti
  * Basi tecniche: il livello successivo, che include i segnali di contenuto che indicano come possono essere utilizzati i tuoi contenuti, un catalogo API, le intestazioni dei link e le istruzioni per l'accesso dell'agente
  * Integrazione avanzata: funzionalità native dell'agente, tra cui la scoperta OAuth, le schede agente MCP (Model Context Protocol) e A2A (Agent2Agent), un indice delle competenze, l'autenticazione Web Bot e WebMCP
  * Commercio: gli standard emergenti per i pagamenti degli agenti, tra cui [​x402](https://blog.cloudflare.com/x402/) (un'estensione del classico codice di stato HTTP 402 Pagamento richiesto), ACP (Agent Commerce Protocol), Universal Commerce Protocol (UCP) e AP2 (Agent Payments Protocol). Per ora si tratta di informazioni a titolo indicativo, che non influiranno sul punteggio finale.



Ogni suggerimento di miglioramento comporta un passo successivo. Quando è disponibile una funzionalità di Cloudflare che può essere d'aiuto, è presente un link "Configura in Cloudflare" che porta direttamente all'impostazione, come ad esempio l'attivazione di Markdown per gli agenti o la gestione del file robots.txt. Per tutto il resto, è presente un pulsante "Copia prompt dell'agente" che suggerisce cosa deve creare l'agente di codifica. Apporta la modifica, esegui nuovamente la scansione e osserva il segno di spunta diventare verde.

## **AEO: gli assistenti basati sull'IA ti raccomandano?**

La diagnostica ti dice se gli agenti possono leggere il tuo sito. La scheda AEO ti spiega cosa succede dopo: quando un cliente pone una domanda a un assistente IA nella tua categoria, raccomanda te o un concorrente? Non è possibile saperlo con un ranking di ricerca. Non ci sono conteggi delle impressioni né report sui clic mancati, quindi quando viene nominato un concorrente e non tu, la vendita è persa e nulla ti informa che è accaduto.

Deduciamo il tuo settore (ad esempio, salute e fitness) e la categoria (ad esempio, abbigliamento sportivo) dal tuo sito e analizziamo i principali assistenti (oggi, Claude di Anthropic e GPT di OpenAI) con probabili prompt da parte dei clienti per vedere come reagiscono. Strutturiamo questi prompt per simulare la scoperta di un prodotto nel mondo reale, chiedendo consigli, confronti tra prodotti e suggerimenti generali all'interno della tua categoria. Osservando come i modelli rispondono a queste domande realistiche, si ottengono metriche come:

  * **Tasso di citazione:** la percentuale di risposte nella tua categoria che citano il tuo sito come fonte
  * **Rilevanza:** quando vieni citato, quanta parte della risposta è effettivamente tua e quanto velocemente viene pubblicata
  * **Frequenza di menzione:** quante volte gli assistenti nominano il tuo marchio nella loro risposta, ad esempio, quante volte "Cloudflare" compare nella risposta, indipendentemente dal fatto che [​cloudflare.com](http://cloudflare.com) sia citato come fonte. Da leggere insieme al tasso di citazione, questo dato distingue la notorietà dall'attribuzione: se gli assistenti ti nominano molto più spesso di quanto ti citino, significa che sei nella loro lista di contatti, ma non hai ancora ottenuto una citazione: una lacuna specifica e su cui è possibile intervenire.
  * **Quota di voce:** la tua quota di citazioni rispetto a quelle dei tuoi concorrenti, così puoi vedere chi sta vincendo i prompt che stai perdendo



Per valutare come un modello di intelligenza artificiale percepisce la tua presenza sul mercato, creiamo un benchmark per ogni settore e categoria prima di assegnare un punteggio a un sito specifico. Interroghiamo gli assistenti IA con suggerimenti plausibili in quella categoria, senza specificare il tuo marchio, e registriamo quali siti vengono citati, dove appaiono e con quale rilievo.

Anziché interrogare nuovamente i modelli ogni volta che il proprietario di un sito esegue una scansione, eseguiamo questo pannello una sola volta per categoria e riutilizziamo la baseline per tutti gli account di quel dominio. La pre-elaborazione di questo set di dati offre tre vantaggi principali:

  * **Zero latenza:** i risultati vengono caricati istantaneamente da uno snapshot anziché attendere le query del modello in tempo reale.
  * **Minore sovraccarico di calcolo:** l'aggregazione delle query a livello di categoria evita chiamate IA ridondanti su migliaia di scansioni.
  * **Punteggio di adeguatezza al settore:** il riutilizzo del corpus del panel ci consente di mappare quali marchi appaiono costantemente insieme, permettendoci di ricavare un punteggio di adeguatezza al settore che misura se un assistente IA visualizza il tuo sito insieme ai tuoi concorrenti reali.



Gli assistenti IA raramente rispondono alla stessa domanda esattamente nello stesso modo due volte. Per tenere conto di questa varianza, utilizziamo [​Cloudflare AI Gateway](https://www.cloudflare.com/products/ai-gateway/) per sollecitare ciascun assistente più volte attraverso modelli diversi. Leggiamo quindi le risposte che un cliente visualizzerebbe, ovvero il testo della risposta insieme alle fonti citate da ciascun assistente, ed estraiamo da esse diversi segnali. 

Valutiamo non solo se il tuo sito è stato menzionato, ma anche se sei stato citato come fonte, quanto presto compaiono le tue citazioni nella risposta e quanta parte del contenuto della risposta finale ti viene attribuita. Laddove è richiesto un giudizio accurato, Workers AI si occupa del lavoro più gravoso, operando nativamente sulla nostra infrastruttura per leggere ogni risposta e valutare come appaiono le tue citazioni e menzioni. Inoltre, utilizziamo un'analisi testuale precisa anziché un modello che valuta autonomamente i propri risultati. Nel complesso, questo sistema raggruppa decine di risposte isolate in metriche utilizzabili. Grazie all'astrazione della pipeline di query e valutazione multimodello, lo strumento fornisce metriche senza richiedere la creazione di una propria struttura di valutazione.

Oltre alle risposte, un'attività dell'operatore IA mostra il traffico di scansione e di riferimento effettivo sul tuo sito, per ciascun operatore (OpenAI, Google e così via): chi legge i tuoi contenuti, chi rimanda i visitatori al tuo sito e gli errori che si incontrano lungo il percorso (403 bloccato, 404 link non funzionante). Il modello su cui vale la pena intervenire è quello dell'operatore che scansiona migliaia delle tue pagine ma non indirizza nessuno, utilizzando il tuo lavoro senza generare clienti.

Poiché questi dati sono specifici per il tuo sito, puoi sperimentare, ripetere la scansione e misurare l'impatto sulle domande precise che ti portano clienti.

## **Scopri il tuo altro pubblico**

Fino ad ora, valutare gli agenti significava procedere per tentativi: analizzare i log per dedurre chi aveva effettuato la visita, oppure fornire a un chatbot un input e valutare a occhio se ti menzionava. Ma con Agent Readiness e AEO, puoi ottenere i dati necessari per agire. E poiché le richieste passano effettivamente attraverso Cloudflare, questi strumenti misurano anziché stimare laddove possibile, e miglioreranno nel tempo. 

Il nostro obiettivo è sempre stato quello di aiutarti a capire chi visita il tuo sito e a decidere come interagire con gli utenti, secondo le tue esigenze. Gli agenti rappresentano solo il pubblico più recente, e le aziende che si rendono facili da trovare, comprendere e di cui fidarsi per gli agenti sono quelle che vengono raccomandate. Il programma Agent Readiness ti permette di scoprire se fai parte del gruppo e cosa fare se non lo sei ancora.

Sei pronto a scoprire se gli agenti IA stanno indirizzando clienti verso la tua attività? Passa alla scheda Panoramica del tuo dashboard per rendere il tuo sito pronto agli agenti e richiedere l'accesso anticipato alla visibilità AEO.

_Costruire su una piattaforma web aperta e pronta per gli agenti? Apri la scheda**Agent Readiness** nel tuo[ dashboard di Cloudflare](https://dash.cloudflare.com) e dicci cosa stai costruendo su[ Cloudflare Developer Discord](https://discord.cloudflare.com)._

]]>01KZQ83ZNWY1DQK491KAXQ9M99Costruire un Internet agentico aperto: leggibile, individuabile, richiamabile e pagabilehttps://blog.cloudflare.com/it-it/the-agentic-internet/ Mon, 10 Aug 2026 09:41:34 GMTGli agenti sono un nuovo tipo di visitatore. Non generano codice CSS né cliccano sugli annunci, ma dall'altra parte c'è una persona pagante. Bloccarli significa bloccare i tuoi clienti. Stiamo creando strumenti e protocolli aperti affinché publisher e agenti possano collaborare ed evitare conflitti.AgentiAgents WeekIAMCPPiattaforma per sviluppatoriSviluppatoriI nostri dati mostrano che gran parte del traffico proveniente da bot troppo ben educati sta[ ricarica pagine che non sono cambiate](https://blog.cloudflare.com/making-ai-search-smarter/). Miliardi di richieste. Un'enorme quantità di sforzo meccanico, senza alcun risultato. Questa è la caratteristica tipica di un sito web creato per gli esseri umani, ma visitato da qualcos'altro.

Gli agenti sono qui, non come un nuovo tipo di software, ma come un nuovo tipo di visitatore del web.

Il web rimodellato attorno a questo nuovo visitatore è ciò che chiamiamo Internet agentico. Immaginiamo il suo futuro come qualcosa di leggibile, individuabile, richiamabile e pagabile. Per realizzare quel futuro, sono necessari strumenti e protocolli specifici.

La piattaforma per sviluppatori di Cloudflare ha fornito agli agenti un ambiente di esecuzione e i primi strumenti per crearli. Ciò che manca sono le piattaforme che permettano agli agenti e ai proprietari di domini di cooperare anziché scontrarsi, su Internet in generale e non solo all'interno di una singola piattaforma.

Ogni browser si è sempre identificato sul web tramite un'intestazione chiamata User-Agent. Il nome aveva senso solo quando si capiva che il browser agiva per tuo conto. Oggi, un user agent è davvero un agente dell'utente: un programma che accede al web per conto di una persona. La sua forma più matura è l'agente di codifica che legge e scrive codice, recupera la documentazione di cui ha bisogno e non vede mai le pagine che legge.

Un agente non esegue il rendering del tuo CSS, non vede la tua immagine principale e non clicca sui tuoi annunci. Ma c'è un essere umano pagante dall'altro lato. Oggigiorno ogni richiesta ha un costo e uno scopo ben preciso. Bloccandola, bloccherai il tuo cliente. Trattala come uno scraper e lo perderai lo stesso.

Ogni agente funziona perché qualcuno, una persona o un'azienda, paga per ciò che fa. La maggior parte delle persone non spende token per il gusto di farlo. Questa versione di Internet, in cui ogni richiesta ha un risultato e una fattura da pagare, non assomiglierà per niente a quella che abbiamo oggi.

Il web non è stato creato per questo, e nemmeno i tuoi strumenti di analisi. E nella maggior parte dei casi, nemmeno il tuo modello di business. Il modo in cui gli agenti leggono, trovano, chiamano e pagano determinerà se Internet resterà aperto o verrà chiuso. In una possibile visione del futuro, un piccolo gruppo di aziende deterrà il controllo dell'individuazione, dell'identità e dei pagamenti, e tutte le altre transazioni passano attraverso di esse. In un altro scenario, Internet rimane aperto: primitive costruite su standard che chiunque può implementare, che corrono su binari neutrali perché il codice è pubblico.

Cloudflare crede nell'Internet aperto ed è nella posizione di contribuire a costruire il futuro in cui prospererà.

Le specifiche su cui ci basiamo sono standard aperti che chiunque può implementare: x402, MCP, Web Bot Auth, PACT. I proprietari di domini scelgono i propri provider di identità, i propri processori di pagamento e i propri partner per gli agenti. Cloudflare è un'opzione, non l'intero stack. Siamo i clienti zero della stessa infrastruttura utilizzata dai nostri clienti, senza alcun percorso privilegiato o API ad accesso anticipato a cui solo noi possiamo accedere. Questo è il lavoro che abbiamo svolto per la rete umana da quindici anni ed è lo stesso lavoro che intendiamo fare per l'Internet agentico.

L'aspetto ingegneristico non è ciò che gli esseri umani sull'Internet agentico noteranno. Stanno adottando un nuovo mezzo di comunicazione e lo giudicheranno nello stesso modo in cui hanno giudicato il web: in base alla sua qualità. Se trovare e prenotare un tavolo richiede un solo scambio di messaggi anziché nove. Se sanno con chi hanno a che fare. Se il pagamento sembra sicuro.

## **La nostra filosofia: un Internet agentico leggibile, individuabile, chiamabile e pagabile**

Tutto inizia con l'identità.[ Web Bot Auth](https://blog.cloudflare.com/web-bot-auth/) consente a un bot di identificarsi crittograficamente a qualsiasi sito visiti, in modo che i publisher possano decidere chi accogliere e chi no. Niente più supposizioni e niente più user agent contraffatti. Molti siti conoscono già l'identità umana dietro una richiesta grazie alle informazioni di accesso, al comportamento all'interno dell'app o alla cronologia degli acquisti. Quel sito può emettere [​token di controllo dell'accesso privato](https://cloudflare.net/news/news-details/2026/Cloudflare-Collaborates-With-Leading-Browsers-to-Develop-a-Privacy-First-Protocol-For-the-Global-Internet/default.aspx)(PACT). Annunciato in collaborazione con Mozilla, Google, Microsoft e Shopify, PACT consente ai siti di garantire in modo anonimo, in modo che l'agente possa presentare il token altrove. Gli agenti legittimi accedono con meno difficoltà.

Possiamo quindi semplificare il lavoro di un agente.[ Markdown for Agents](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/) consente agli agenti di leggere i siti web con meno token e meno larghezza di banda.[ WebMCP](https://blog.cloudflare.com/webmcp/) gli offre un modo nativo per interagire per tuo conto. Gli standard come[ x402](https://x402.org/) gli permettono di pagare direttamente i commercianti.

La parte **leggibile** è semplice. Gli agenti IA possono leggere i contenuti in modo nativo e sfruttare i loro punti di forza? Meno larghezza di banda e meno token un agente utilizza, meglio è. Ogni tag HTML visualizzato per un essere umano che non lo guarda mai non è solo uno spreco di risorse di calcolo, ma anche un inquinamento della finestra di contesto che l'agente deve poi pagare per ignorare.[ Markdown for Agents](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/) risolve questo problema dal lato server.

Dal lato client, abbiamo affrontato la creazione di un browser pensando agli agenti come cittadini di prima classe.[ Kitesurf](http://blog.cloudflare.com/kitesurf) è il nostro nuovo browser, abbastanza leggero da funzionare su Workers, avviato per ogni richiesta e terminato al termine. Offre contenuti e funzionalità di cui gli agenti hanno bisogno, senza la pesantezza delle funzionalità pensate per l'utente tipiche dei browser tradizionali.

La parte **riconoscibile** è il punto di partenza di ogni momento economico sull'Internet agentico. Prima che un agente possa consultare una risorsa, richiamare uno strumento o effettuare un pagamento, deve sapere che la risorsa è disponibile. La ricerca è solo una parte della storia, poiché gli agenti devono trovare ciò di cui hanno bisogno attraverso interfacce create appositamente per loro, non tramite una casella di ricerca progettata per un essere umano che digita lentamente e scorre velocemente il testo.[ AI Search](https://developers.cloudflare.com/ai-search/) è disponibile oggi, quindi qualsiasi sito pubblico può essere reso ricercabile dagli agenti.

L'altra parte consiste nell'essere scoperti. I creatori di contenuti e i proprietari di API devono sapere quanto sono visibili agli agenti.[ L'ottimizzazione del motore degli agenti (AEO)](http://blog.cloudflare.com/aeo)misura la visibilità del marchio sui modelli e sugli agenti che contano. Se non sei visibile in modo misurabile agli agenti utilizzati dai tuoi clienti, di fatto per loro risulti offline. 

La parte **chiamabile** è il punto in cui gli agenti iniziano a fare le cose: prenotare un tavolo, rinnovare un abbonamento, estrarre un report. Sul web umano, tutti questi elementi appaiono diversi, perché sono stati creati per essere utilizzati da esseri umani che cliccano sulle interfacce utente. Un agente che prova ad aggiungere un elemento a una lista di cose da fare deve analizzare l'HTML, indovinare quale pulsante è "Aggiungi", simulare un clic e sperare che il DOM non sia cambiato dall'ultima volta che è stato controllato.

[WebMCP](https://blog.cloudflare.com/webmcp/) consente a un sito di esporre le proprie azioni direttamente agli agenti tramite il browser:

Lo strumento “contratto” diventa esplicito. Nessun parsing HTML, nessuna supposizione sui campi del modulo. Poiché gli strumenti vengono eseguiti all'interno della pagina, riutilizzano la sessione e lo stato esistenti dell'utente. La[ modalità codice](https://blog.cloudflare.com/code-mode/) fa un ulteriore passo avanti. Gli agenti pensano in codice, e richiamare gli strumenti scrivendo codice è più veloce e preciso che usare la prosa. Poiché gli agenti chiamano gli endpoint anziché estrarre dati dalle pagine web, il proprietario dei contenuti riceve un segnale chiaro su quali contenuti vengono effettivamente utilizzati. 

La parte **pagabile** è la direzione in cui crediamo si stia muovendo l'Internet agentico. Ogni transazione economica, prima o poi, necessita di un metodo di pagamento. I modelli basati sulla pubblicità stanno fallendo. I modelli basati su postazioni fisse non funzionano quando l'utente è un programma. I publisher da cui tutti dipendiamo non possono finanziarsi con visualizzazioni di pagina che non si verificano mai e browser che non visualizzano i loro annunci. 

Un sito di ricette che non ha mai generato profitti con la pubblicità può addebitare una frazione di centesimo per ogni accesso e risultare redditizio su scala internet. Un giornale locale può concedere in licenza gli articoli al momento della lettura senza un accordo di licenza o un login. Dall'altra parte, l'agente si presenta con un portafoglio e un budget che l'essere umano aveva stabilito una volta. 

Ogni interazione a pagamento lascia una ricevuta. Il publisher può dimostrare quale agente ha recuperato quale pagina. L'agente può dimostrare di aver pagato per ciò che ha utilizzato.[ Wallets](https://blog.cloudflare.com/wallets/) consente agli agenti di pagare facilmente contenuti e API.[ Monetization Gateway](https://blog.cloudflare.com/monetization-gateway/) permette ai proprietari di domini di impostare i pagamenti dagli agenti con pochi clic.

Cloudflare si trova volutamente al centro di tutto questo. Ci troviamo già tra miliardi di persone e i siti che visitano, proteggendoli, velocizzandoli e mantenendoli online. Gli agenti modificano il traffico, ma non la natura di tale attività: siamo il livello neutrale e ad alte prestazioni su cui editori, commercianti, sviluppatori di agenti e utenti finali possono fare affidamento, sapendo che saremo dalla loro parte, non in competizione con loro. 

Vogliamo fornire ai proprietari di domini gli strumenti per potenziare i tipi di agenti IA che desiderano supportare e[​bloccare quelli che non desiderano](https://blog.cloudflare.com/cloudflare-ai-audit-control-ai-content-crawlers/). Uno strumento per sviluppatori probabilmente vuole diventare[ pronto per gli agenti](http://blog.cloudflare.com/aeo) per incoraggiare gli agenti IA a individuarlo, raccomandarlo e pagarlo. Un publisher potrebbe voler bloccare gli agenti IA estrattivi (che consumano risorse senza restituire nulla) ma consentire gli agenti IA che concedono in licenza i suoi contenuti o li compensano. Un provider di dati senza scopo di lucro potrebbe voler bloccare i bot o gli utenti umani che superano i limiti di utilizzo, ma consentire loro di pagare per essere sbloccati e utilizzare tali fondi per coprire il consumo eccessivo di risorse.

## **I bot sono morti, lunga vita ai bot**

La distinzione tra un[ bot e un essere umano non è più così semplice](https://blog.cloudflare.com/past-bots-and-humans/). La questione non è così semplice come dire che i bot sono cattivi e gli umani sono buoni o che i bot sprecano risorse che dovrebbero invece essere consumate dagli umani. Questo è un vecchio modo di pensare ormai superato nel mondo degli agenti.

Consideriamo gli agenti come una nuova tipologia di protagonista. Le loro azioni possono essere auspicabili, ad esempio, la lettura di contenuti in modo da preservare le risorse, l'interazione con i siti web secondo le modalità specificate dai proprietari del dominio e il pagamento per ciò che utilizzano. Oppure possono essere indesiderate, ad esempio, l'estrazione di milioni di pagine senza compenso, il tentativo di aggirare i blocchi o il bypass di[ robots.txt](https://www.cloudflare.com/learning/bots/what-is-robots-txt/). Riteniamo che molte delle azioni indesiderate diminuiranno e si trasformeranno persino in azioni desiderate se agli esseri umani e ai bot verranno forniti gli strumenti adeguati.

## **Colmare il divario di entrate**

Cloudflare ha dedicato anni al rilevamento dei bot, consentendo ai proprietari di domini di controllare se i bot possono accedervi. Ciò che mancava era l'altra metà: come gli agenti interagivano con quei siti una volta che ne avevano avuto accesso. Ecco a cosa serve questa suite di strumenti agentici: a rendere il web leggibile, individuabile, interattivo e pagabile. Queste quattro primitive sono tutte basate su standard aperti, quindi nessuna azienda ne possiede le infrastrutture. 

Un Internet agentico aperto necessita di diversità da entrambe le parti. Non solo publisher e creatori di contenuti diversi, ma anche agenti diversi. Se la domanda converge, non importa quanto sia aperta l'offerta. Internet rimarrà comunque un giardino recintato..

Stiamo costruendo questa alternativa aperta. Unisciti a noi rendendo il tuo[ agente del sito pronto con il nostro nuovo dashboard](http://blog.cloudflare.com/aeo), quindi registrati per ricevere le ultime novità sul nostro prodotto Answer Engine Optimization. Se gestisci un sito o un agente, puoi sperimentare tutte le nuove tecnologie di Internet utilizzando il nostro[ AI Playground](https://playground.ai.cloudflare.com/).

]]>01KZNGG38APPRNV26Y3NRNZ918Individuare comportamenti anomali dell'IA con analisi sensibili all'identitàhttps://blog.cloudflare.com/it-it/identity-aware-ai-gateway/ Mon, 10 Aug 2026 08:19:03 GMTAI Gateway sensibile all'identità è ora in beta aperta. User Insights trasforma tale traffico in una baseline comportamentale per ogni persona e agente, e segnala il rischio interno nel momento in cui si manifesta.AgentiAgents WeekAI GatewayIANovità sul prodottoPiattaforma per sviluppatoriSviluppatoriQuando si considerano i costi dell'IA, può essere difficile capire se c'è qualcosa che non va. Prima di tutto, devi stabilire una baseline per poter vedere cosa è cambiato, che si tratti di un agente impazzito o di un dipendente il cui utilizzo è aumentato di 10 volte. Essere in grado di individuare questi cambiamenti consente di iniziare a indagare e, finora, è stato difficile rilevarli.

Conoscere chi sta facendo cosa con l'IA è una delle sfide chiave che le organizzazioni stanno affrontando in questo momento. [Un report](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf) della Stanford University ha rilevato che il 59% delle organizzazioni ha dichiarato che le lacune di conoscenza erano il loro maggiore ostacolo alla governance responsabile dell'AI. 

Si tratta di un problema di sicurezza, che ha ripercussioni anche a livello finanziario. La risoluzione di questi problemi richiede due elementi: un'identità verificata per ogni richiesta (in modo da riconoscere ogni singolo picco) e un'immagine del comportamento previsto di tale identità. Oggi annunciamo entrambi.

AI Gateway sensibile all'identità con Cloudflare Access è ora in beta aperta e User Insights è disponibile per ogni cliente AI Gateway senza costi aggiuntivi. Insieme trasformano il traffico che transita già in AI Gateway in una baseline comportamentale per ogni persona e agente che lo utilizza, e identificano quelli che si discostano da questo.

## Che cos'è AI Gateway?

[AI Gateway](https://developers.cloudflare.com/ai-gateway/) è il piano di controllo centrale per tutto il tuo utilizzo dell'IA. Invece di ogni app e team che chiamano direttamente i modelli su OpenAI, Anthropic, Google o Workers AI, le richieste passano prima attraverso AI Gateway, offrendoti un unico punto per osservare, proteggere e gestire tutto il tuo utilizzo dell'IA.

Funziona con le applicazioni che crei e con gli strumenti di codifica in cui i tuoi sviluppatori già operano. Esegui il routing di [strumenti basati su agenti](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/) come Claude Code, Codex e GitHub Copilot tramite AI Gateway: in questo modo, sfrutteranno la stessa visibilità e gli stessi controlli di tutto il resto.

## AI Gateway sensibile all'identità

Con l'integrazione di AI Gateway e[ Cloudflare Access](https://developers.cloudflare.com/ai-gateway/configuration/cloudflare-access), puoi associare un[ dominio personale](https://developers.cloudflare.com/ai-gateway/configuration/custom-domains/) al tuo gateway e proteggerlo con Access, proprio come qualsiasi altra applicazione. In questo modo, potrai:

  * Eseguire l'autenticazione con qualsiasi provider di identità supportato da SAML, come Okta o Entra, eliminando la necessità di generare e distribuire chiavi API Cloudflare.
  * Impostare i criteri su chi esattamente può accedere al tuo gateway.
  * Inviare richieste a un nome host pulito come `ai.example.com`, senza ID account o ID gateway nell'URL.



Ogni richiesta autenticata ora porta l'identità dell'utente da Access. AI Gateway aggiunge l'ID utente Access verificato ai metadati della richiesta come `cf.user_id`, in modo da poter filtrare i registri, le analisi e le spese in base alla persona che ha effettivamente effettuato la richiesta.

Insieme a[ limiti di spesa](https://developers.cloudflare.com/ai-gateway/features/spend-limits/), tale identità diventa uno strumento di budget. Poiché ogni richiesta ora porta un utente reale, puoi impostare limiti di spesa per utente: assegnare a ogni utente il proprio bucket di budget, quindi bloccare ulteriori richieste o passare a un modello a costi più contenuti quando lo raggiungono. Niente più fatture a sorpresa e nessuna chiave API condivisa che impedisce la piena tracciabilità dei costi.

Uno dei nostri primi utilizzatori, Flexport, ha riscontrato esattamente questo problema.

"Le chiavi API condivise rendono quasi impossibile stabilire chi stia utilizzando un servizio IA o applicare le regole di accesso che abbiamo già per i dipendenti", afferma Max Baumgarten, Staff Security Engineer presso Flexport. Usare Cloudflare Access per AI Gateway fornisce a ogni richiesta un'identità autenticata e ci permette di utilizzare i nostri criteri di identità esistenti al gateway. I nostri team possono adottare strumenti IA senza creare un sistema di autenticazione separato per ogni cliente".

Nel prossimo futuro, potrai utilizzare i gruppi di provider di identità degli utenti per impostare limiti di spesa o controllare i modelli a cui un gruppo può accedere. Ad esempio, consenti al tuo team di machine learning di accedere a modelli all'avanguardia, limita la spesa del tuo team di supporto o assegna un budget a tutte le persone che lavorano su un progetto specifico, tutto mappato ai gruppi che già gestisci nel tuo provider di identità.

## La nuova scheda User Insights

All'interno di AI Gateway, ora è disponibile una scheda chiamata User Insights. User Insights legge il traffico che transita nel tuo gateway e lo trasforma in un quadro comportamentale di ogni account. Apprende come si comporta normalmente ogni account, identifica quelli che si discostano da tale pattern e fornisce il contesto per distinguere un agente non autorizzato da un ingegnere impegnato. Funziona sul traffico che transita già nel tuo gateway, quindi non c'è nulla da configurare.

User Insights monitora i costi, inclusi quelli sprecati, come percentuali di riscontri nella cache basse e finestre di contesto sovradimensionate. Molti strumenti lo fanno già. Quello che non fanno è dirti se un account si comporta normalmente. Ecco su cosa abbiamo scelto di concentrarci, insieme al controllo dei costi. 

### Definire una baseline per ogni account: persone e agenti

Ogni account lascia un'impronta comportamentale nel tempo, indipendentemente dal fatto che si tratti di una persona o di un agente. Un agente che riassume i ticket ogni tre ore è preciso e coerente. Una persona è più disordinata, con prompt variegati, tempi irregolari e lunghe sessioni su problemi complessi. Entrambi sono legittimi, quindi la stessa deviazione può risultare inutile per uno e un segnale reale per l'altro.

In User Insights, iniziamo valutando le sessioni, non le singole richieste. Le soglie assolute falliscono qui: un aumento di 500 USD da parte di un utente a uso intensivo di risorse potrebbe essere normale, mentre una sessione da 50 USD da parte di un agente che spende sempre 5 USD è un cambiamento di 10 volte che potrebbe passare inosservato. Quindi confrontiamo ogni sessione con la storia stessa dell'account, utilizzando il 95° percentile (p95) del costo della sessione negli ultimi 30 giorni. Questo ci offre un'idea di come l'account operi normalmente, e qualsiasi valore superiore a 2x del suo p95 è un forte candidato per un comportamento anomalo.

L'analisi seguente delinea come siamo arrivati a queste cifre.

Figura 1: rilevamento delle anomalie nei costi delle sessioni

**Come leggere il grafico sopra**

Il grafico traccia sessioni reali dal nostro traffico interno. Ogni punto rappresenta una singola sessione (rappresentata su scale logaritmiche):

  * **Asse X (costo della sessione):** costo totale in dollari.
  * **Asse Y (x utente p95):** quante volte la sessione ha superato la baseline personale dell'utente.



Le due linee di soglia tratteggiate dividono le sessioni in quattro categorie:

  * **In alto a destra (★ stelle):** supera sia due volte la baseline p95 dell'utente che il limite massimo p99 a livello di account. Questi sono picchi relativi elevati che rappresentano spese anomale significative e attiveranno un avviso. 
  * **In alto a sinistra:** elevato picco relativo (due volte il p95 dell'utente), ma al di sotto del limite p99 dell'account. Ignoriamo questo per evitare di segnalare variazioni di lieve entità.
  * **In basso a destra:** spesa assoluta elevata, ma coerente con l'uso tipicamente elevato di questo utente. Anche questo valore viene ignorato, perché considerato come comportamento di routine.
  * **In basso a sinistra:** attività normale ben all'interno di entrambe le baseline.



Figura 2: distribuzione del costo della sessione a livello di account

Questo istogramma (Figura 2) mappa il costo di ogni sessione all'interno dell'organizzazione per stabilire un tetto massimo a livello di account:

  * Uso tipico: la stragrande maggioranza delle sessioni costa ben al di sotto di 10 USD, con il 95º percentile a 20 USA.
  * p99 dell'account (200 USD): solo l'1% di tutte le sessioni in tutta l'azienda raggiunge o supera i 200 USD.



Allora perché abbiamo scelto p99? Impostare il nostro limite massimo in dollari al p99 dell'account crea un parametro significativo. Garantisce che un'anomalia non sia solo una variazione improvvisa per un utente specifico, ma si classifichi anche tra l'1% delle sessioni più costose di tutta l'organizzazione.

Figura 3: cronologia della sessione singola dell'utente

Le baseline non sono statiche. Man mano che le abitudini di un account cambiano, il suo p95 mobile (linea verde) e la soglia 2x (linea arancione) si spostano di conseguenza, così un avviso riflette sempre un comportamento recente piuttosto che un valore impostato una volta sola. Applichiamo anche una soglia minima in dollari, in modo che un picco debba essere sia statisticamente anomalo, sia tale da giustificare il tempo di analisi di un amministratore. Quel dollaro minimo è ciò che impedisce che un micro-utente attivi un avviso per un aumento di 500 volte di pochi centesimi.

### La lente giusta per rilevare comportamenti anomali 

Dopo tutta l'analisi di cui abbiamo discusso sopra, ciò che vedono gli amministratori è una vista degli account che hanno interrotto il loro schema, con tutto ciò che è normale filtrato. Tale vista filtrata è un feed di comportamento anomalo.

Questo comportamento è difficile da individuare perché il segnale non è mai un nuovo strumento o un'azione bloccata. È un account attendibile che fa di più di ciò che è già autorizzato a fare. Potrebbe trattarsi di un account di servizio che improvvisamente inizia a eseguire sessioni più costose, o di una persona il cui utilizzo supera di gran lunga la propria norma e rimane tale per giorni.

Nessuna di queste attiva un criterio, ma tutte infrangono una baseline comportamentale. Una deviazione improvvisa dall'uso proprio di un account è spesso il primo segno osservabile di credenziali compromesse o di un agente che va fuori controllo.

User Insights non determina le intenzioni e non blocca nessuno; al contrario, sottopone all'attenzione di un amministratore i pochi account che hanno iniziato a comportarsi in modo anomalo, affinché sia possibile effettuare le dovute verifiche. A volte ciò conduce a una vera indagine. A volte semplicemente sintomo che qualcuno ha bisogno di addestramento (come lo sviluppatore che inserisce l'intera base di codice in ogni prompt quando basterebbe un frammento). 

## E poi? 

### Ti assisteremo nel passare dal controllo dei costi all'ottimizzazione dei costi

Una volta stabilito un budget, la domanda naturale successiva è: come si può ottenere la stessa qualità di output a un costo inferiore? Non tutte le richieste richiedono un modello di frontiera. Un'attività di sintesi o un semplice completamento di codice può essere eseguito su un modello a costi più contenuti senza perdita significativa di qualità.

Stiamo sviluppando un routing intelligente basato su attività, in cui AI Gateway analizza la richiesta in arrivo e la instrada al modello che ti offre il miglior risultato al costo più basso. A livello organizzativo, sarai in grado di identificare dove puoi ottenere i maggiori risparmi eseguendo il routing verso modelli più efficienti. Il routing intelligente basato su attività è in fase di sviluppo attivo. Condivideremo ulteriori dettagli man mano che verrà sviluppato.

### Ti aiuteremo a capire _come_ viene utilizzata l'IA

Il rilevamento delle anomalie ti segnala che un account ha infranto il suo schema, ma non il motivo. Un amministratore dovrà comunque esaminare i registri e ricostruire cosa è accaduto. Colmare questo divario è la nostra prossima focalizzazione e inizia classificando cosa sia effettivamente il traffico.

Stiamo sviluppando una classificazione dei prompt che ordina le richieste in categorie come codifica, scrittura e altre. Queste categorie sono il contesto mancante da quasi ogni altro segnale. Un aumento delle spese nella categoria "codifica" da parte di un ingegnere potrebbe essere accettabile, ma lo stesso aumento in una categoria che tale account non ha mai previsto non lo è. La classificazione può mostrare a un'organizzazione non solo quanto utilizza l'IA, ma anche per cosa la utilizza. 

Risponde anche alla domanda alla base della maggior parte di queste conversazioni: l'IA viene utilizzata per il lavoro per cui è stata progettata? Una volta separato il traffico aziendale dal resto, l'uso personale diventa visibile. Dall'esterno, qualcuno che gestisce un'attività secondaria durante l'orario aziendale e qualcuno che trasferisce silenziosamente dati attraverso un modello sembrano uguali. Distinguerli è fondamentale per individuare il rischio interno. 

Una volta che il traffico IA transita in AI Gateway, ogni nuova categoria di segnali di rischio o di efficienza è un vantaggio in più per un amministratore senza necessità di configurazione aggiuntiva.

## Inizia

User Insights è disponibile al pubblico oggi per ogni cliente di AI Gateway senza costi aggiuntivi. È già presente nella dashboard per chiunque invii traffico attraverso il gateway, quindi se stai già eseguendo il routing tramite AI Gateway, questa vista è disponibile per te. 

Se non l'hai già fatto,[ crea un gateway](https://developers.cloudflare.com/ai-gateway/get-started/) e inizia a inviare richieste a qualsiasi modello nel nostro [catalogo](https://developers.cloudflare.com/ai/models/). 

Consigliamo di integrare AI Gateway in [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/policies/access/), ora in open beta. Le viste delle spese e delle anomalie funzionano senza questo, ma collegare un'identità è ciò che trasforma l'ID di un account anonimo in un nome su cui puoi effettivamente agire. Inizia in modalità di monitoraggio per apprendere le tue baseline prima di applicare qualsiasi cosa.

Vogliamo sapere come stai gestendo l'IA oggi. Partecipa alla conversazione su[ Discord](https://discord.cloudflare.com/) oppure contatta il team del tuo account.

]]>01KZNBTX9KSSBSPJSRRB4BZT30Cloudflare OS: una piattaforma aperta per agenti, app e lavorohttps://blog.cloudflare.com/it-it/cloudflare-os/ Mon, 10 Aug 2026 03:10:43 GMTCloudflare OS è una piattaforma open source che permette a tutti nella tua azienda di creare app, automatizzare il lavoro e accedere in modo sicuro ai sistemi interni, modellata su ciò che la tua organizzazione conosce e su come operaAgentiAgents WeekCloudflare AccessCloudflare OSCloudflare WorkersIANovità sul prodottoOpen sourcePiattaforma per sviluppatoriSviluppatoriOgni organizzazione ha una missione, una ragione d'essere. Le organizzazioni trasmettono quella missione, insieme alla loro terminologia, procedure, sistemi, standard e modalità operative, alle loro persone. Le persone, a loro volta, combinano questo contesto alla loro esperienza e si impegnano a portare a termine la missione.

Il lavoro può assumere molte forme, dal codice, ai documenti e alle presentazioni, fino alle relazioni e ai risultati nel mondo reale.

Alcuni di questi sono semplici: il codice funziona o non funziona. Negli ultimi anni, gli agenti hanno utilizzato questo ciclo di feedback per produrre codice che "funziona" per gli sviluppatori. Ma cosa dire del resto di noi?

Portare lo stesso vantaggio al resto dell'organizzazione è un problema più complesso. Gli agenti devono comprendere il contesto dell'azienda ed essere in grado di accedere ai sistemi che le persone usano per svolgere il loro lavoro. Devono trasformare quel contesto e accesso in lavoro che consenta all'organizzazione di progredire verso il compimento della sua missione.

Ecco perché abbiamo creato Cloudflare OS. Fornisce a ogni persona un agente e un ambiente di lavoro basati sulla propria azienda: come funziona, cosa sa e i sistemi su cui si basa.

A maggio di quest'anno, abbiamo dato a tutte le persone di Cloudflare accesso alla prima versione di Cloudflare OS. Migliaia di persone con qualsiasi ruolo, molte delle quali non prettamente tecniche, lo utilizzano ogni giorno per creare documenti e presentazioni, automatizzare attività ripetitive e creare piccole app per visualizzare i dati e aiutarle a svolgere il proprio lavoro.

Cloudflare OS ha fornito a tutti anche una libreria condivisa di contesto e skill realizzata dai team di Cloudflare. Cattura la nostra terminologia, le procedure e i modi più conosciuti di svolgere lavori ricorrenti come istruzioni che un agente può seguire. Quando una persona scopre un modo migliore di fare qualcosa, tutti gli altri possono usarlo.

**Oggi, stiamo rendendo open source una nuova versione di[ Cloudflare OS](https://os.cloudflare.app/).** Qualsiasi organizzazione può distribuirlo, collegarlo ai sistemi interni e personalizzarlo.

## **Cosa abbiamo imparato dalla prima versione**

Il sistema operativo Cloudflare che presentiamo come open source oggi è basato su ciò che abbiamo appreso gestendo la prima versione internamente, un percorso che il nostro CIO, Sam Rhea, descrive nel suo[ post sul blog](https://blog.cloudflare.com/how-we-use-ai-with-cloudflare-os).

La prima versione si concentrava su individui che utilizzavano agenti tramite ambienti di lavoro privati. Le app erano statiche piuttosto che software attivo connesso ai sistemi interni, e la maggior parte dei lavori deterministici richiedeva comunque l'esecuzione di una skill da parte di un agente e il consumo di più token di modelli.

La collaborazione ha rivelato una problematica più critica. L'accesso a un[ server MCP](https://www.cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/) ci ha indicato quali strumenti un agente potrebbe richiedere, ma non quali risorse sottostanti l'agente aveva osservato. Una volta che le persone hanno iniziato a condividere ambienti di lavoro, app e risultati, è stato necessario garantire che la collaborazione non potesse esporre informazioni che qualcuno non era autorizzato a vedere.

Abbiamo rimodellato Cloudflare OS su una nuova base per risolvere questi problemi. La sicurezza doveva far parte della piattaforma, non qualcosa che ogni persona che crea un'app o utilizza un agente deve implementare correttamente.

Il risultato è una piattaforma progettata per appartenere all'azienda che la gestisce. Puoi personalizzare le interfacce, connettere i propri strumenti e aggiungere le skill e il contesto che catturano il modo in cui la tua organizzazione opera.

## **Introduzione a Cloudflare OS**

Cloudflare OS inizia con una conversazione nel tuo browser, come molti altri strumenti IA. Ciò che lo rende diverso è che ogni conversazione è basata sul contesto e le skill che la tua organizzazione ha curato. Dai al tuo ambiente di lavoro un obiettivo, e può attingere a tale conoscenza e utilizzare gli strumenti e i dati che la tua organizzazione già impiega per raggiungerlo.

Cloudflare OS combina tre parti:

  * **Un ambiente di lavoro per agenti** basato sul contesto e sulle skill curate dalla tua azienda, con un runtime isolato dove gli agenti possono compilare ed eseguire codice.
  * **Un nuovo framework di sicurezza e governance** per un accesso sicuro ai dati e servizi interni.
  * **Una piattaforma per app personali e modificabili** che le persone possono creare, condividere e continuare a modificare.



Quello che inizia come una conversazione può diventare un documento, un'app o un flusso di lavoro che continua a svolgere il lavoro.

## **Un ambiente di lavoro per agenti per tutti nella tua azienda**

Gli ambienti di lavoro degli agenti sono stati progettati per essere utilizzati da tutti nella tua organizzazione. Interagisci con loro nel tuo browser, quindi non devi essere uno sviluppatore o sapere come utilizzare un terminale. 

Un ambiente di lavoro combina sessioni di agenti, stato persistente, output e file, accesso alle risorse e un runtime isolato in cui l'agente può compilare ed eseguire codice.

Vengono forniti con il contesto e le skill curati che il tuo team o la tua azienda hanno raccolto. Non è più necessario ripartire da zero per ogni attività: se una persona nel tuo team ha trovato il modo migliore di fare qualcosa, ne beneficiano tutti. Le persone non devono più spiegare allo stesso modello il processo, la terminologia e le best practice ogni volta che iniziano un'attività.

Alcune cose che si possono fare:

### **Ricerca e formulazione di domande**

Chiedi a un ambiente di lavoro di ricercare un argomento utilizzando il contesto aziendale e le risorse che gli metti a disposizione. L'agente può scrivere codice per cercare, filtrare, unire e analizzare le informazioni anziché trasferire un intero set di dati nella finestra di contesto del modello.

### **Creazione di documenti, presentazioni e fogli di calcolo**

Un ambiente di lavoro può trasformare la sua ricerca in un documento, una presentazione o un foglio di calcolo che si può continuare a modificare. Questi output non devono essere file statici. Possono rimanere collegati ai dati in tempo reale, aggiornarsi con le modifiche delle origini ed essere esportati in formati o servizi familiari come Google Drive.

### **Creazione di app collaborative e connesse per il tuo team**

Quando un documento o un foglio di calcolo non è sufficiente, l'agente può creare un'app con la propria interfaccia, logica e stato. L'app può utilizzare le risorse aziendali connesse e supportare più persone che collaborano tra loro.

### **Esecuzione di flussi di lavoro deterministici**

Non tutti i lavori richiedono una sessione agente completa. Molti sono una sequenza nota di passaggi con uno o due punti in cui il giudizio è utile. Un ambiente di lavoro può trasformare tali lavori in flussi di lavoro per lo più deterministici, utilizzando il codice per i passaggi prevedibili e un modello solo dove aggiunge valore. I flussi di lavoro possono essere eseguiti su richiesta, secondo un programma o quando si verifica un evento in un sistema connesso.

Cloudflare OS consente ad agenti e app l'accesso regolamentato ai sistemi di record tramite Gatekeeper (ulteriori informazioni nella sezione sulla sicurezza di seguito). Supporta inoltre i server[ Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro) esistenti che la tua organizzazione già utilizza tramite[ portali server MCP](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/).

## **Un nuovo framework di sicurezza e governance per un accesso sicuro ai dati e ai servizi interni**

Quando le persone iniziano a sperimentare l'IA sul lavoro, una delle prime richieste è spesso una chiave API ai sistemi aziendali. Una richiesta legittima: l'IA non è di grande utilità al lavoro se non ha accesso ai sistemi che le persone usano per svolgere il proprio lavoro.

Ma distribuire le chiavi API a persone e agenti è pericoloso e non è scalabile. Le chiavi spesso forniscono un accesso ampio e duraturo che è difficile da limitare, condividere in sicurezza e verificare.

MCP offre agli agenti un modo migliore per utilizzare questi sistemi. Un server MCP può mantenere le credenziali ed esporre un insieme definito di strumenti invece di distribuire la chiave direttamente all'agente. Ma controllare quali strumenti un agente può richiedere è solo il primo passo. MCP da solo non ci dice quali risorse sottostanti ha osservato un agente. L'agente può combinare informazioni tra sistemi, inviarle in luoghi meno restrittivi o esporle tramite app e output a persone che potrebbero non avere l'autorizzazione a vedere le risorse originali. L'autorizzazione deve tenere conto di dove i dati possono andare successivamente.

### **Gli agenti iniziano senza accesso**

[ Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/) controlla chi può accedere a Cloudflare OS. All'interno, ogni agente e app iniziano senza accesso a nulla. Un agente può chiedere l'accesso a una risorsa specifica, che puoi concedere o negare. Il codice generato riceve tale risorsa come un binding tipizzato:

`env.PROJECT` è una funzionalità che rappresenta l'autorizzazione a utilizzare una risorsa specifica in base a un criterio specifico. Le credenziali rimangono completamente isolate dall'agente e da qualsiasi codice generato.

Il codice del server viene eseguito in un Dynamic Worker con la rete globale in uscita disabilitata. Il codice del client viene eseguito in un frame isolato nel browser. Nessuno può accedere a Internet se non attraverso le capacità che fornisci esplicitamente.

### **I Gatekeeper governano risorse e azioni**

Un Gatekeeper è un[ Worker](https://developers.cloudflare.com/workers/?_gl=1*1pzndf6*_gcl_au*MzM2MDkxNTQzLjE3ODQ4NDczOTM.*_ga*MWVkZWU3OTctMzJjNC00YWE1LWI2ZDUtZTJkNTY1NzYxYWQ0*_ga_SQCRB0TXZW*czE3ODUyMTk3NjMkbzckZzAkdDE3ODUyMTk3NjMkajYwJGwwJGgwJGRQeHAyTUEtdzgtVUFETUEzOGwtVFVhajVDd2laRWYxSC1R) specifico per il servizio che si trova tra Cloudflare OS e un servizio esterno. Comprende l'API del servizio, le sue risorse e le operazioni che possono essere eseguite su di esse.

Dare a un agente accesso all'intero account GitHub è probabilmente troppo ampio. Un Gatekeeper può concedergli l'accesso a un singolo repository, consentirgli di leggere i problemi ma non il codice sorgente, mascherare campi particolari, applicare limiti di velocità e richiedere l'approvazione prima di unire una pull request.

L'agente e le sue app vedono una piccola API TypeScript. Il Gatekeeper gestisce[ OAuth](https://www.cloudflare.com/learning/access-management/what-is-oauth/), mantiene le credenziali, applica i criteri, registra ciò che è stato letto e media qualsiasi cosa con un effetto visibile esternamente.

### **I criteri seguono ciò che l'agente ha visto**

Controllare la lettura iniziale non è sufficiente. Prendiamo, ad esempio, il caso in cui un agente legga una tabella sensibile in un data warehouse e la utilizzi per produrre una dashboard in tempo reale. La condivisione della dashboard non deve diventare un modo per condividere la tabella con persone che non potrebbero accedervi direttamente.

Cloudflare OS registra ogni risorsa osservata dagli agenti. Queste osservazioni rimangono associate all'agente e al suo lavoro. Quando un'altra persona tenta di aprire l'ambiente di lavoro, interagire con l'agente o visualizzare ciò che ha prodotto, i Gatekeeper verificano l'accesso di quella persona alle risorse osservate.

Lo stesso registro di osservazione viene utilizzato per informare i criteri che determinano quando gli agenti possono effettuare richieste esterne. La lettura di dati sensibili può impedire all'agente di scrivere dati su determinate fonti, invitare nuovi collaboratori, affidare il lavoro a un altro agente o fare una richiesta in uscita.

Le persone che usano agenti o creano app non devono temere di commettere questi errori. La piattaforma ora può essere utilizzata per gestire tutto questo.

## **Una piattaforma per creare e condividere app personali e modificabili**

La maggior parte delle suite di produttività offre un set fisso di applicazioni: documenti, fogli di calcolo e presentazioni. Nel sistema operativo Cloudflare, ogni "file" può essere un'applicazione a sé stante, scritta da un agente per una persona, un progetto o un team.

Questi non sono prototipi che devi esportare e distribuire altrove. Ognuna è un'applicazione full stack con codice client, codice server, un'API e stato durevole. Le app sono private per impostazione predefinita, ma possono essere condivise come documenti.

### **Ogni app è un Worker**

Quando si chiede al proprio ambiente di lavoro di creare un'app, l'agente compila due parti:

  * Il codice client che esegue il rendering dell'interfaccia utente dell'app nel browser
  * Il codice server che memorizza lo stato e implementa il comportamento dell'app



Il server viene caricato su richiesta come un[ Dynamic Worker](https://developers.cloudflare.com/dynamic-workers/) e ne viene creata un'istanza come[ Durable Object Facet](https://developers.cloudflare.com/dynamic-workers/usage/durable-object-facets/) (entrambe sono funzionalità che abbiamo sviluppato per questo progetto). Il modulo fornisce all'app il proprio database SQLite, separato dal runtime del Cloudflare OS che lo gestisce. Dynamic Workers utilizzano isolati V8 leggeri, quindi ogni app può avere il proprio runtime isolato senza la necessità di un server o un container dedicato.

Il client del browser comunica con il server utilizzando[ Cap'n Web](https://github.com/cloudflare/capnweb), il sistema di Remote Procedure Call (RPC) con funzionalità a oggetti open source di Cloudflare. Un metodo server può essere chiamato dal client come una normale funzione JavaScript:

La parte speciale è che l'agente può anche chiamare lo stesso metodo.

**Quindi, se puoi creare uno strumento per svolgere un lavoro in autonomia, gli agenti possono usare il tuo strumento per svolgere il lavoro quando non sei presente.**

### **Condividi l'app o condividine le modalità di realizzazione**

Quando crei un'app in Cloudflare OS, hai due modi per condividerla:

  * Condividere la tua app consente ad altre persone di collaborare in tempo reale utilizzando lo stesso stato.
  * Condividere un progetto della tua app consente ad altre persone di crearne una propria copia.



Un'app di cui è stata creata un'istanza da un blueprint contiene il codice dell'app originale, ma non contiene i relativi dati SQLite, cronologia delle conversazioni, credenziali o risorse collegate. Ogni nuova app inizia con uno stato e risorse indipendenti.

Ciò significa che quando condividi le app con il tuo team, gli altri possono modificarle autonomamente con l'IA invece di presentare una richiesta di funzionalità e assegnarla a te.

## **Usa qualsiasi modello e controlla i costi**

Cloudflare OS può essere utilizzato con qualsiasi modello. Ogni chiamata di inferenza passa attraverso[ Cloudflare AI Gateway](https://developers.cloudflare.com/ai-gateway/), offrendo alla tua organizzazione un unico punto per decidere quali modelli sono disponibili e quale modello deve gestire ogni attività.

Non tutte le attività richiedono il modello più costoso. Potresti non voler utilizzare il modello di frontiera più costoso per riassumere le tue email non lette ogni mattina. AI Gateway ti offre il controllo necessario per assicurarti che i modelli costosi vengano utilizzati solo per il lavoro più complesso.

Ogni richiesta è attribuita alla persona, al team o all'ambiente di lavoro che l'ha effettuata. Gli amministratori possono vedere dove viene speso il budget per l'inferenza, impostare budget e limiti di frequenza e decidere cosa accade quando viene raggiunto un limite. 

## **Open source, così puoi farlo tuo**

Cloudflare OS è disponibile oggi ed è open source. Dai un'occhiata al[ repository GitHub cloudflare-os](https://github.com/cloudflare/cloudflare-os). Puoi distribuirlo nel tuo account Cloudflare e utilizzare i tuoi criteri di accesso, la configurazione di AI Gateway, i dati e le integrazioni.

La nostra distribuzione interna riflette i sistemi, la terminologia, i criteri e le modalità di lavoro di Cloudflare. La tua dovrebbe riflettere la tua organizzazione.

Cloudflare OS è progettato in modo da poter personalizzare l'interfaccia, aggiungere Gatekeeper interni e creare funzionalità specifiche per l'organizzazione senza modificare il prodotto principale.

Stiamo introducendo due repository: il[ core di Cloudflare OS](https://github.com/cloudflare/cloudflare-os) e un[ esempio di distribuzione](https://github.com/cloudflare/cloudflare-os-starter) basato su come lo gestiamo internamente in Cloudflare. Il repository di distribuzione consuma il core senza aggiornarlo, fornendo un luogo per configurazione, interfaccia utente personalizzata, integrazioni interne, analisi e pipeline di distribuzione.

## **Fornito insieme ai nostri partner**

Il codice sorgente è solo il punto di partenza. Il contesto, le skill, i flussi di lavoro, i sistemi interni e i criteri sono ciò che rende Cloudflare OS ancora più utile per la tua organizzazione.

I partner strategici di Cloudflare, Presidio e Happy Cog, collaboreranno con te per personalizzare Cloudflare OS in base al modus operandi della tua organizzazione e implementarlo su tutta la tua forza lavoro.

I partner possono aiutarti a gestire skill condivise e contesto istituzionale, creare interfacce personalizzate, collegare sistemi interni tramite Gatekeeper e portali server MCP, nonché configurare controlli di sicurezza, modelli e costi.

Puoi ottenere un Cloudflare OS personalizzato con il tuo marchio, connesso ai tuoi sistemi, in esecuzione su Cloudflare e modellato in base alle modalità di lavoro effettive del personale.

## **Inizia**

Cloudflare OS è disponibile oggi stesso su[ GitHub](https://github.com/cloudflare/cloudflare-os). Puoi esplorare il codice sorgente, provare la demo o distribuirlo nel tuo account Cloudflare in pochi minuti utilizzando il nostro[ repository di base](https://github.com/cloudflare/cloudflare-os-starter).

Siamo solo all'inizio. Stiamo lavorando per integrare Cloudflare OS nella dashboard di Cloudflare come prodotto completamente gestito, aggiungendo container per i flussi di lavoro di sviluppo e portando ambienti di lavoro in Slack e altri strumenti di chat.

Se vuoi parlare con il nostro team, saremmo lieti di farlo. Usa[ questo modulo](https://www.cloudflare.com/resource/cloudflare-os-interest-landing-page/) per contattarci.

]]>01KZMT1545WDY80Z2CK1ZEKZFVIl ciclo di vita dello sviluppo degli agenti è arrivato su Cloudflarehttps://blog.cloudflare.com/it-it/agent-development-lifecycle/ Fri, 07 Aug 2026 09:35:07 GMTGli agenti possono scrivere codice più velocemente di quanto i team riescano a revisionarlo, implementarlo e gestirlo. Oggi presentiamo il ciclo di vita dello sviluppo degli agenti e i principi fondamentali di Cloudflare che lo supportano.Agent Development LifecycleAgentiAgents WeekBrowser RunCloudflare WorkersDevOpsIAMCPNovità sul prodottoObservabilityPiattaforma per sviluppatoriTracingWorkflowsNegli ultimi decenni, i responsabili tecnici si sono dedicati a trovare soluzioni che consentissero a numerosi programmatori di collaborare su una base di codice condivisa. Questo lavoro risale addirittura al "Systems Development Lifecycle" ([RAND, 1975](https://www.rand.org/pubs/reports/R1855.html)), oggi comunemente noto come "ciclo di vita dello sviluppo del software (SDLC)", che definisce le seguenti fasi:

  * Pianificazione
  * Progettazione
  * Implementazione
  * Test
  * Distribuzione
  * Mantenimento
  * Ritiro



L'intelligenza artificiale ha trasformato la fase che prima era la più lenta e costosa, ovvero l'implementazione, nella più rapida ed economica. Ciò, a sua volta, ha avuto un impatto a valle: ha sovraccaricato le persone responsabili di tutte le altre fasi del ciclo di vita dello sviluppo del software (SDLC). Si va dai manutentori open source bombardati da migliaia di richieste e problemi pull, agli ingegneri di produzione che cercano di evitare che la produzione fallisca mentre il tasso di consegna del software aumenta di ordini di grandezza.

Stiamo tutti cercando di salvare i nostri sistemi, i nostri clienti e noi stessi dalla negligenza.

La risposta, paradossalmente, è dare agli agenti più potere di azione. È giusto così! Non permetteresti mai a un ingegnere del tuo team di scrivere codice aspettandoti che qualcun altro lo convalidi, lo integri, lo distribuisca, lo gestisca in produzione e si occupi della risoluzione dei bug. Ma è quello che la maggior parte delle aziende sta facendo ora con gli agenti. I modelli sono migliorati notevolmente e gli agenti operano su orizzonti temporali più lunghi, essendo in grado di affrontare compiti molto più complessi. Ma non sono ancora utilizzati in modo uniforme lungo tutto il ciclo di vita dello sviluppo del software.

Cloudflare tratta gli agenti come i nostri clienti. Possono [acquistare domini](https://blog.cloudflare.com/agents-stripe-projects/), creare [account temporanei](https://blog.cloudflare.com/temporary-accounts/) e [utilizzare l'intera API di Cloudflare](https://blog.cloudflare.com/code-mode-mcp/). Sappiamo che gli agenti hanno bisogno di API e strumenti per poter gestire l'intero ciclo di vita dello sviluppo del software per conto dei nostri clienti, e non solo la fase iniziale.

Oggi presentiamo quindi l'inizio di una nuova serie di strumenti che consentiranno agli agenti di andare oltre la semplice generazione di codice e di assumere un ruolo più attivo nel ciclo di vita dello sviluppo del software (SDLC). Stiamo condividendo ciò che abbiamo creato e imparato cercando di risolvere questo problema per conto nostro:

  * [**@cloudflare/ci**](https://blog.cloudflare.com/ci-workflows), un nuovo modo per eseguire CI/CD su milioni di repository, in grado di autoripararsi e generare agenti per svolgere attività molto più complesse, basato su Cloudflare Workflows.
  * [**Tracce OpenTelemetry in ambiente di sviluppo locale**](https://blog.cloudflare.com/local-tracing), offrendo agli agenti la stessa osservabilità disponibile in produzione, integrata in Wrangler e nel plugin Cloudflare Vite.
  * [**Presentazione di Cloudflare Agents e Agent Traces**](http://blog.cloudflare.com/agents-on-cloudflare): una nuova piattaforma per osservare, gestire e migliorare gli agenti, incentrata sulle tracce OpenTelemetry provenienti dagli agenti.
  * [**Come Cloudflare applica gli standard di ingegneria utilizzando l'IA**](http://blog.cloudflare.com/engineering-standards-enforcement): la nostra esperienza nell'applicazione delle best practice in tutti i repository e le specifiche dei nostri prodotti e sistemi.
  * [**Come abbiamo creato una software factory per azzerare il numero di problemi di Astro su GitHub**](https://blog.cloudflare.com/astro-issue-triage): la nostra esperienza nella creazione di sistemi per analizzare, riprodurre, verificare e risolvere automaticamente i problemi di un progetto open source di grandi dimensioni e in continua crescita.



C'è però qualcosa di più importante in gioco. Analizzando il ciclo di vita dello sviluppo del software (SDLC), anche con la migliore automazione, i suoi presupposti non sono scalabili rispetto al volume di codice che gli agenti possono scrivere e alla velocità con cui i team di sviluppo software devono operare per essere competitivi. Riteniamo sia giunto il momento di sostituire l'SDLC con l'ADLC, ovvero il ciclo di vita dello sviluppo degli agenti.

## L'SDLC è per i team software. L'ADLC è per le fabbriche di software.

In questo momento, [tutti](https://x.com/zachlloydtweets/status/2069789929073262945) [stanno](https://x.com/matanSF/status/2066578088184680920) [parlando](https://x.com/dexhorthy/status/2081797628552270027) [di](https://x.com/bcherny/status/2077929390806073807) [costruire](https://x.com/gokulr/status/2032271386161684665) "fabbriche di software": sistemi basati su agenti che prendono gli input e costruiscono, migliorano, distribuiscono e gestiscono autonomamente il software. Prendi un input, che si tratti di un errore di produzione, una segnalazione di bug da parte di un cliente o un'idea per una nuova funzionalità, e delegalo interamente a un agente.

Anche con l'ausilio di agenti, la maggior parte dei progetti software è vincolata da fasi di intervento umano. Gli operatori umani sollecitano gli agenti, li incoraggiano a proseguire, li istruiscono ad applicare il feedback ricevuto durante una revisione del codice, supervisionano costantemente molti agenti e forniscono loro istruzioni. Nella maggior parte dei team di sviluppo software, le persone gestiscono ancora ogni fase del modello SDLC: l'unica differenza è che all'interno di ogni fase vengono delegati compiti a un agente.

E così il sogno alla base delle software factory diventa: e se si ripensasse questo approccio e si costruisse una fabbrica per l'intero processo di sviluppo del software? Come possiamo dedicare più tempo umano alle cose che richiedono davvero ispirazione, gusto e giudizio umani? Ci lascerebbe più tempo per progettare, per parlare con i clienti e per sognare in grande.

Una software factory deve gestire le stesse fasi del ciclo di vita dello sviluppo del software, ma richiede molto di più dalla piattaforma su cui è costruita. Perché quando consegni le chiavi e lasci guidare l'agente, ogni passaggio manuale che prima si basava su un operatore umano deve essere adattato per essere:

  * **Programmatico** : il "ClickOps" era una cattiva prassi per gli operatori umani, ma è inaccettabile per gli agenti. Ogni singola operazione necessita di API che gli agenti possano richiamare, sottoporre a debug e su cui possano fare affidamento.
  * **Scalabile orizzontalmente** : le implementazioni di anteprima erano un'opzione desiderabile quando gli utenti fissavano lo schermo durante la compilazione o prendevano manualmente il controllo di un server di staging per individuare i problemi prima della produzione. Affinché gli agenti possano guidare, ogni agente deve avere la propria anteprima che corrisponde alla produzione.
  * **Riproducibile** : cosa succede se c'è un bug che puoi riprodurre solo simulando il 4G su un iPhone 15? O da un IP di un determinato paese? I tipici strumenti di test unitari e di integrazione non saranno d'aiuto in questo caso.
  * **Basato su notifiche push, in tempo reale** : affidarsi agli operatori umani per controllare il pannello di controllo corretto è sempre stato un metodo inadeguato per capire se le cose funzionano, ma con gli agenti questo sistema fallisce completamente. Affinché un agente svolga un'azione, è necessario un evento che lo attivi.
  * **Atomico** : ogni modifica deve essere testabile, rilasciabile, osservabile e reversibile in modo indipendente, senza influenzare comportamenti non correlati.
  * **Autorizzato** : sai che probabilmente non dovresti, ma oggi dai a qualche ingegnere fidato le chiavi per accedere tramite SSH all'ambiente di produzione nel caso in cui le cose dovessero andare davvero male. Non si può permettere a un agente di fare una cosa del genere, ma senza la possibilità di inoltrare la richiesta e ottenere maggiori autorizzazioni, come può svolgere il suo lavoro?
  * **Auto-miglioramento** : le persone imparano dall'esperienza. Durante la prima settimana di lavoro o il primo turno di reperibilità, gli operatori umani sono lenti e hanno bisogno di affiancare qualcun altro, ma poi migliorano e diventano più veloci. Anche gli agenti hanno bisogno di modi per imparare dall'esperienza.



Abbiamo bisogno di qualcosa di nuovo se vogliamo rendere le software factory sicure da utilizzare per software di produzione reale. Le software factory si trovano ad affrontare la stessa sfida di altri sistemi autonomi come le auto a guida autonoma: la sfida di passare da un funzionamento corretto nell'80% dei casi a un tasso di successo superiore al 99%.

## Per dare agli agenti le chiavi per guidare il ciclo di vita dello sviluppo del software, non puoi dare loro un'auto progettata per gli esseri umani.

Un veicolo autonomo è carico di sensori e tecnologia che una normale auto non ha. Sensori Lidar, telecamere, potenti unità di calcolo per eseguire inferenze e connettività a un sistema di comando centrale che può intervenire da remoto se necessario.

Perché un veicolo autonomo raggiunga l'80% delle prestazioni di un essere umano alla guida, probabilmente non abbiamo bisogno di tutto questo. La guida autonoma ha raggiunto circa l'80% delle prestazioni umane già 10 anni fa. Ma questo non è l'obiettivo da raggiungere: l'obiettivo è essere molto migliori e più sicuri di un guidatore umano. Questo è ciò che ci aspettiamo quando consegniamo le chiavi a una macchina, per sentirci sicuri di fare un pisolino mentre guidiamo sulla Highway 101 a 96 km/h. Ed è per questo che i veicoli autonomi dispongono di una tecnologia creata appositamente per la guida autonoma: è ciò che crea fiducia e gestisce i casi limite che non possono essere progettati in anticipo.

Lo stesso vale per il software di guida autonoma. Chiediti: perché _non_ hai ancora lasciato che il tuo agente approvi e unisca automaticamente le sue richieste di pull ai tuoi servizi di produzione? Più alta è la posta in gioco di ciò che costruisci, più lunga sarà quasi certamente la tua lista di motivazioni.

Quando si iniziano ad analizzare non solo tutti gli aspetti che possono andare storti in questo processo, ma anche quelli necessari per realizzare il prodotto giusto per i clienti, la complessità è davvero notevole. Non si adatta a una sequenza lineare di passaggi in un file YAML Actions di GitHub e va ben oltre l'esecuzione di test automatizzati tradizionali. Anche una piccola modifica a un pannello di controllo può avere ripercussioni su ruoli, specializzazioni e strutture organizzative, e le modifiche soggettive sono le più difficili da testare e da delegare. Probabilmente la maggior parte di queste cose al momento non fa parte della tua pipeline CI/CD. Ma dovranno esserlo, se si vuole che si verifichino ancora, pur lasciando il pieno controllo agli agenti che gestiscono la software factory.

Per permettere agli agenti di guidare l'intero processo, abbiamo bisogno di un modo migliore per orchestrare questa serie dinamica di passaggi. Riteniamo che si tratti di un [flusso di lavoro](https://blog.cloudflare.com/ci-workflows), con la capacità di generare container, agenti e browser. Un flusso di lavoro in grado di impostare flag di funzionalità e abilitarli per un utente di test, analizzare log e tracce, osservare le metriche di produzione durante il rilascio graduale di una modifica e svolgere tutte le altre attività necessarie per una distribuzione sicura.

## Una pipeline CI/CD è semplicemente un flusso di lavoro. Ma un flusso di lavoro può essere molto più di una pipeline CI/CD.

[Cloudflare Workflows](https://developers.cloudflare.com/workflows/) ti permette di concatenare più passaggi, riprovare automaticamente le attività non riuscite e mantenere lo stato per minuti, ore o persino settimane. È progettato per codificare processi aziendali complessi e dinamici in un programma logico e facilmente comprensibile. [Questo post del blog](https://blog.cloudflare.com/ci-workflows) spiega perché i flussi di lavoro, insieme agli [artefatti](https://blog.cloudflare.com/artifacts-git-for-agents-beta/), semplificano notevolmente la definizione e l'attivazione delle pipeline CI/CD. Ad esempio:

I flussi di lavoro vanno oltre una serie di passaggi lineari. Possono essere [definiti dinamicamente](https://blog.cloudflare.com/dynamic-workflows/) e possono generare agenti o altri flussi di lavoro. [Questo esempio](https://flueframework.com/docs/guide/workflows/#example-cloudflare-workflows) mostra un flusso di lavoro che esamina i nuovi dati del giorno precedente. Il flusso ha il pieno controllo su quando e come viene richiesto all'agente di intervenire e può trasmettere il contesto tra le diverse fasi:

Una volta individuato questo schema, e dopo essere stati "sommersi dal flusso di lavoro" come Cloudflare, si inizia a chiedersi: cos'altro potrei gestire con un flusso di lavoro? Quali altri passaggi critici dovuti all'intervento umano potrei delegare a questa combinazione di flusso di lavoro e [agenti Flue](https://flueframework.com/)?

## L'intero ADLC, sulla stack di Cloudflare

Con i [flussi di lavoro](https://developers.cloudflare.com/workflows/) in grado di orchestrare passaggi complessi e gli [artefatti](https://developers.cloudflare.com/artifacts/) come livello di archiviazione per il codice, quando si osservano le fasi del SDLC, tutto ciò di cui un agente ha bisogno per gestire l'intero processo di costruzione, distribuzione e manutenzione del software è su Cloudflare:

## Primitive per costruire la tua software factory

In questo momento, coloro che sono all'avanguardia stanno costruendo le software factory del futuro. Alla fine le software factory diventeranno, proprio come gli agenti e l'IA, il modo normale in cui le persone costruiranno il software. Ma per la maggior parte delle persone e delle organizzazioni, non ci siamo ancora arrivati.

Vogliamo cambiare questa situazione.

Per raggiungere questo obiettivo, ci siamo posti le seguenti domande: come possiamo semplificare e rendere accessibili le cose in modo che chiunque su Internet possa beneficiare di un cambio di paradigma come questo? E quali sono le primitive di base che possiamo rendere accessibili a tutti, dalle startup più piccole alle piattaforme più grandi del mondo?

In questo caso, pensiamo che le primitive siano già qui. C'è ancora molto da fare per connetterle, per continuare a costruire la nostra software factory e imparare da essa, ma ora, oggi stesso, siamo pronti perché tu possa costruire la tua macchina che costruisce la macchina, su Cloudflare. Inizia con [@cloudflare/ci](https://blog.cloudflare.com/ci-workflows), [crea un agente](http://blog.cloudflare.com/agents-on-cloudflare) e scopri quanta parte del ciclo di vita dello sviluppo del software è possibile automatizzare.

]]>01KZDAQJY6XPC8CCC6QNMRK3P0Annuncio di Cloudflare Wallets: il portafoglio programmabile per l'Internet agenticohttps://blog.cloudflare.com/it-it/wallets/ Fri, 07 Aug 2026 03:58:59 GMTCloudflare Wallets will provide AI agents with native payments and verifiable identity on the web. Using the x402 protocol, agents can autonomously purchase APIs and content within clear safety guardrails.Agents WeekAI BotsIANovità sul prodottoPaymentsPiattaforma per sviluppatoriSviluppatorix402Oggi, per gli agenti IA è difficile sperimentare nuove API. Spesso devono navigare in una pagina di accesso progettata per gli esseri umani e non per gli agenti, contattare una persona per aggiungere un metodo di pagamento, generare una chiave API e poi capire come chiamare l'API.

Questo flusso è molto difficile per gli agenti per due motivi: gli agenti non dispongono di un identificativo stabile per registrarsi a un'API e non hanno un metodo nativo per pagare le API. A causa della mancanza di queste risorse, spesso faticano ad adottare i software, il che limita la crescita del commercio agentico. Spesso gli agenti IA rinunciano completamente a questi compiti, rimandando la registrazione, i metodi di pagamento e la generazione delle chiavi API agli esseri umani. Ciò rende molto difficile per gli agenti provare e confrontare numerose API.

Per risolvere questo problema, abbiamo creato Cloudflare Wallets. A partire da oggi, puoi[ richiedere un handle di Cloudflare Wallet](https://cloudflare.pay) per il tuo account, che ti fornirà un nome utente univoco per aiutarti a connetterti meglio con i commercianti. A breve potrai configurare e utilizzare il tuo Cloudflare Wallet per pagare API e contenuti.

All'inizio di questo mese, abbiamo annunciato il[ Monetization Gateway](https://blog.cloudflare.com/monetization-gateway/) per aiutare i clienti di Cloudflare a ricevere pagamenti per i loro siti web e applicazioni. Monetization Gateway supporterà i micropagamenti grazie al protocollo [​](https://www.x402.org/)x402, che consente di allegare i pagamenti alle richieste HTTP.[​](https://www.x402.org/) Tali micropagamenti potranno essere utilizzati per scopi che vanno dall'inferenza dell'intelligenza artificiale ai dati e ai contenuti. Se vuoi pagare o ricevere pagamenti per i servizi dietro Monetization Gateway e altri[ endpoint compatibili con x402](https://developers.cloudflare.com/agents/tools/payments/x402/), avrai bisogno di un portafoglio. 

Cloudflare Wallets ti permetterrà di conservare stablecoin, acquistare servizi e ricevere fondi via web. Ogni account dotato di portafoglio potrà inoltre creare portafogli virtuali per i propri agenti, consentendo loro di acquistare API, strumenti MCP, contenuti e altro ancora. Potrai definire dei parametri di controllo per i tuoi portafogli virtuali (come un limite di spesa, un elenco di utenti autorizzati e un importo massimo per transazione) per aiutare il tuo agente a spendere denaro in modo sicuro dal tuo conto. Ciò consentirà al tuo agente di provare numerose API con facilità e con un rischio gestito. Gli utenti del portafoglio avranno la possibilità di condividere i propri handle di Cloudflare Wallet, il che garantirà loro un'identità stabile quando interagiscono con i commercianti.

## **Costruire il mercato agentico bilaterale**

Il[ Monetization Gateway](https://blog.cloudflare.com/monetization-gateway/) di Cloudflare consentirà ai clienti Cloudflare idonei di vendere le proprie risorse (come contenuti o API) in modalità headless ad acquirenti agentici. Ma affinché questo mercato si sviluppi realmente, gli agenti avranno bisogno di più strumenti per acquistare dai commercianti in un modo nativo per le macchine. Wallets aggiungerà un altro strumento all'SDK degli agenti di Cloudflare, consentendo agli agenti IA di acquistare facilmente API e contenuti necessari tramite micropagamenti.

Vi saranno due tipi di portafogli: i portafogli di account e i portafogli virtuali.

I **portafogli di account** sono progettati per persone che sono proprietari e utenti di account Cloudflare. Possono aggiungere fondi, delegare la spesa a portafogli virtuali gestiti da agenti e prelevare fondi secondo necessità. 

I **portafogli virtuali** , invece, sono progettati per gli agenti e funzionano tramite chiave API. All'interno di un portafoglio virtuale, un agente potrà spendere i fondi in base alle autorizzazioni a lui concesse. La sua spesa massima sarà limitata dal tetto fissato dal proprietario del portafoglio di account. Questo sistema offre agli agenti la libertà di agire per conto degli utenti senza una costante approvazione manuale, limitando al contempo la possibilità di spesa eccessiva da parte dell'agente.

## **La libertà di esplorare**

I portafogli virtuali sono interessanti perché permetteranno agli agenti di fare ciò che sanno fare meglio: esplorare decine o centinaia di servizi e trovare quello più adatto a uno specifico caso d'uso. I micropagamenti in stablecoin tramite x402 renderanno semplice provare un'API senza bisogno di un account, consentendo agli agenti di testare nuove opzioni con il minimo sforzo. I limiti di spesa dei portafogli virtuali sono progettati in modo che gli esseri umani possano lasciare che gli agenti esplorino autonomamente entro limiti di spesa sicuri. Questi limiti possono sembrare delle restrizioni, ma paradossalmente danno agli agenti più libertà. Se un agente è responsabile di 10 dollari, ci si può preoccupare meno delle sue spese rispetto a un agente responsabile di 1.000 dollari. Se provare un'API costa solo pochi centesimi, allora 10 dollari sono più che sufficienti per esaminare e valutare numerose opzioni.

Una volta che tu o il tuo agente avrete scelto un'API da utilizzare, le policy impostate nel tuo portafoglio di account fungeranno da controlli dei costi per i portafogli virtuali. Vorresti dare a ogni dipendente un budget di 100 dollari a settimana per l'inferenza IA? È sufficiente predisporre un portafoglio di account con il saldo corretto e creare portafogli virtuali per ciascun dipendente applicando tale regola. Chiunque superi i limiti del proprio portafoglio virtuale potrà richiedere un'autorizzazione manuale a un operatore autorizzato ad apportare modifiche al portafoglio di account.

Vogliamo semplificare la creazione di politiche di spesa flessibili ma rigorose per i portafogli di account, in modo che non richiedano un monitoraggio attivo quotidiano. Quando si verifica un'anomalia, come ad esempio una spesa inaspettatamente rapida, un operatore umano sarà in grado di verificare e confermare che tutto funzioni come previsto. Se la spesa è stata intenzionale, l'amministratore del portafoglio di account potrà aumentare il limite o approvare un versamento di fondi una tantum. Se la spesa è stata involontaria, le politiche di spesa per l'aggiunta di fondi ai portafogli virtuali hanno svolto correttamente il loro compito imponendo dei limiti.

Il nostro lavoro è rendere il più semplice possibile il finanziamento e l'utilizzo di questi portafogli. Inizieremo con metodi semplici per l'accesso e l'uscita di fondi all'interno delle aree geografiche supportate, con l'autofinanziamento tramite stablecoin disponibile come alternativa per gli utenti idonei. Internet non cambierà completamente da un giorno all'altro, ma con[ la maggior parte del traffico sul web](https://radar.cloudflare.com/) ora generato dai bot, siamo in grado di fornire ad agenti e commercianti strumenti di alto livello per il commercio agentico.

## **Oltre i soli pagamenti**

Consentire agli operatori umani di delegare l'autorità ad agenti per acquistare e vendere facilmente servizi è un utile punto di partenza. Ma questa delega non è sempre evidente ai commercianti quando interagiscono con gli agenti. Oggi, se un agente visita il tuo sito web, potresti sapere ben poco di lui come utente, nonostante l'agente agisca per conto di un individuo o di un'organizzazione. Questa mancanza di attribuzione mette in discussione molti modelli di business tradizionali del web. È facile offrire una settimana di prova gratuita o crediti di iscrizione a una persona o a un'organizzazione. Concedere gli stessi vantaggi a un agente privo di un'identità stabile, quando un singolo individuo può creare decine di agenti sotto il proprio controllo, è un po' più difficile.

Risolviamo questo problema collegando i portafogli a un account Cloudflare tramite [​](https://cloudflare.pay/)[cloudflare.pay](http://cloudflare.pay). [​](https://cloudflare.pay/)[cloudflare.pay](http://cloudflare.pay) consentirà agli agenti di identificarsi facoltativamente, poiché la loro identità è un delegato dell'account. Un agente di ricerca potrebbe trovarsi su [​research.example.cloudflare.pay](http://research.example.cloudflare.pay), consentendo ai commercianti di sapere che si tratta di un agente di una determinata organizzazione. Questo approccio consentirà agli agenti di mantenere identità coerenti e persistenti, migliorando l'esperienza per tutte le parti coinvolte. Per gli agenti sarà completamente facoltativo dichiarare o meno la propria identità, e spetterà alle aziende decidere se dare priorità alle transazioni con agenti conosciuti.

## **Gli identificativi degli agenti devono essere leggibili dall'uomo**

Riteniamo che l'approccio da adottare nei confronti degli agenti sarà simile a quello utilizzato per le VPN: se qualcuno non è identificato, non è di per sé inaffidabile, ma deve dimostrare la propria affidabilità in modo più approfondito. Ecco perché abbiamo introdotto[ Turnstile](https://www.cloudflare.com/products/turnstile/) e altre iniziative per rilevare i bot all'interno di[ Bot Management](https://www.cloudflare.com/products/bot-management/). La nostra primitiva di identità si baserà su questo lavoro precedente. Ad esempio,[ Web Bot Auth](https://developers.cloudflare.com/bots/reference/bot-verification/web-bot-auth/) consente già agli agenti di registrare la propria identità tramite una coppia di chiavi. Gli ID associati a Cloudflare Wallets consentono a questa coppia di chiavi di diventare leggibile per l'uomo.

Sappiamo che gli standard relativi all'identità agentica stanno cambiando rapidamente, ed è per questo che abbiamo voluto mantenere un approccio semplice. Proponiamo quindi un identificativo leggibile dall'uomo per una coppia di chiavi non molto leggibile, simile alle coppie URL e indirizzo IP utilizzate nel[ DNS](https://www.cloudflare.com/learning/dns/what-is-dns/). Non stiamo cercando di definire uno schema particolare o un altro sistema di verifica. Vogliamo semplicemente rendere l'identità facile da ricordare e da dichiarare. Man mano che gli schemi per arricchire l'identità agentica si sviluppano attraverso le iniziative della[ x402 Foundation](https://blog.cloudflare.com/x402/), cercheremo di adottarli e incoraggiare altri a fare lo stesso.

## **Il futuro del commercio agentico**

Noi di Cloudflare vogliamo offrire tutti gli elementi fondamentali per il successo del commercio agentico. Monetization Gateway offrirà ai venditori un modo per essere pagati senza dover implementare un'infrastruttura di pagamento tradizionale. I portafogli offriranno agli acquirenti un modo per pagare in modo semplice e diretto, senza intermediari. La verifica dell'identità permetterà ai commercianti di comunicare con gli acquirenti che si identificano o di applicare i requisiti di identificazione.

Tutti questi elementi creeranno un mercato headless per Internet. Se ti interessa questa iniziativa e vuoi partecipare,[​puoi richiedere il tuo handle ora](https://cloudflare.pay/). Non vediamo l'ora di scoprire cosa creerai e come lo monetizzerai.

]]>01KZD5WSTJ94P0HAY880KQDPKJPresentazione dell'API per l'utilizzo fatturabile: visibilità programmatica dei costi per Cloudflarehttps://blog.cloudflare.com/it-it/billable-usage-api/ Thu, 06 Aug 2026 07:35:56 GMTCloudflare ha lanciato una nuova API per l'utilizzo fatturabile degli account, offrendo a sviluppatori e team FinOps una visibilità programmatica centralizzata su costi e utilizzo di tutti i prodotti self-service. Basato sulle specifiche FOCUS, consente di monitorare la spesa in modo integrato con il resto della tua infrastruttura cloud.Agents WeekAPIBillingIngegneriaNovità sul prodottoSviluppatoriLa Agents Week riguarda il cambiamento già in corso: riguarda il cambiamento già in atto: gli agenti scrivono codice, implementano i Worker e predispongono l'infrastruttura per tuo conto. Questo cambiamento modifica ciò che devi vedere. Se un programma sta spendendo denaro nel tuo account Cloudflare, devi sapere cosa sta spendendo: nell'arco della giornata, per ogni singolo prodotto e in un formato che un altro programma possa utilizzare. Il pannello di controllo è la giusta soluzione per gli operatori umani, ma non per l'automazione.

Stiamo quindi lanciando una nuova **API per l'utilizzo fatturabile** per gli account self-service: un singolo endpoint che restituisce l'utilizzo e il costo del tuo account, suddivisi per prodotto e per periodo di servizio. Tale API copre tutti i prodotti Cloudflare basati sull'utilizzo presenti sull'account, inclusi Workers, R2, D1, Workers AI, Vectorize, Images e Stream, il tutto con una sola chiamata. E se già lavori con una suite di strumenti FinOps, i nomi delle colonne ti risulteranno familiari.

Riceverai un `HTTP 200 OK` con `Content-Type: application`/`json` e le righe di utilizzo nel corpo della risposta. Attualmente, i dati relativi all'utilizzo e ai costi vengono aggiornati quotidianamente, mentre lavoriamo per fornire dati sempre più in tempo reale.

## **Cosa viene restituito**

Ogni riga nella risposta corrisponde a un periodo di addebito per un prodotto presente sul tuo account.

  * `ServiceName` e `ServiceFamilyName`: il prodotto ("Workers Standard" nella famiglia "Workers", "R2 Storage" in "R2" e così via).
  * `ChargePeriodStart` / `ChargePeriodEnd`: il periodo coperto da questa riga.
  * `PricingQuantity` e `ConsumedUnit`: quanto hai utilizzato, nell'unità di misura che usiamo per la fatturazione (GB/mesi, GB/secondi, richieste e così via).
  * `ContractedCost`: il costo di quel periodo, in `BillingCurrency`.
  * `CumulatedPricingQuantity` e `CumulatedContractedCost`: i totali progressivi per il periodo di fatturazione.
  * `ZoneId` / `ZoneName`: quando l'utilizzo è attribuito a una zona specifica.



La maggior parte di queste corrisponde direttamente alle colonne della[ FinOps Open Cost and Usage Specification (FOCUS)](https://focus.finops.org/), pertanto, se il tuo team sta già importando dati FOCUS da un altro provider, i nomi e la terminologia dovrebbero risultarti familiari:

**Campo Cloudflare**| **Colonna FOCUS**| **Note**  
---|---|---  
`BillingCurrency`| `BillingCurrency`| Corrispondenza esatta.  
`BillingPeriodStart`| `BillingPeriodStart`| Corrispondenza esatta.  
`ChargePeriodStart` / `ChargePeriodEnd`| `ChargePeriodStart` / `ChargePeriodEnd`| Corrispondenza esatta.  
`ServiceName`| `ServiceName`| Corrispondenza esatta.  
`ConsumedQuantity` / `ConsumedUnit`| `ConsumedQuantity` / `ConsumedUnit`| Corrispondenza esatta.  
`PricingQuantity`| `PricingQuantity`| Corrispondenza esatta.  
`ContractedCost`| `ContractedCost`| Corrispondenza esatta.  
`ServiceFamilyName`| (vicino a `ServiceCategory`)| Raggruppamento nativo di Cloudflare; FOCUS utilizza un vocabolario controllato.  
`CumulatedContractedCost`| (derivato)| Campo di convenienza: FOCUS tratta l'accumulo come un problema di query.  
`ZoneId` / `ZoneName`| (vicino a `ResourceId` / `ResourceName`)| Identificatore a livello di zona, ove applicabile.  
  
Le risposte utilizzano il formato standard dell'API di Cloudflare: `result` è un array di righe, una per prodotto per periodo di addebito, insieme a `success`, `errors` e `messages`.

## **Dove siamo su FOCUS**

La scelta di utilizzare la denominazione FOCUS è stata deliberata. AWS, Azure, Google Cloud, Oracle e un elenco sempre più lungo di provider SaaS pubblicano già esportazioni in formato FOCUS, e tutti i principali strumenti di gestione dei costi lo utilizzano. Ciò detto, non possiamo ancora affermare di essere pienamente conformi: alcune colonne richieste dalle specifiche non sono attualmente presenti nel payload. Raggiungere questo obiettivo è nella nostra tabella di marcia. Consideriamo questo il primo passo: ora ha una forma familiare, poi ci sarà la piena conformità.

## **Spesa su Cloudflare, accanto al resto della spesa per il cloud: la nostra partnership con Vantage**

Abbiamo stretto una partnership con [​Vantage](https://www.vantage.sh/) per un'integrazione nativa con Cloudflare. Vantage è una piattaforma per la gestione dei costi dell'infrastruttura che acquisisce dati relativi a costi e utilizzo da oltre 30 provider, tra cui provider di intelligenza artificiale, cloud e SaaS, e li riunisce in un'unica visualizzazione per la creazione di report, l'allocazione e l'ottimizzazione. Grazie a questa integrazione, i dati relativi al tuo utilizzo confluiranno negli stessi report sui costi, budget e avvisi sui costi che già utilizzi per il resto della tua infrastruttura.

Vantage si connette a Cloudflare utilizzando un token API di sola lettura con accesso di sola lettura ai dati di fatturazione. Una volta stabilita la connessione, Vantage raccoglie quotidianamente i dati di utilizzo fatturabile e li suddivide per prodotto (come Workers e R2), zona e account, consentendoti di individuare i prodotti che generano la spesa e di attribuirla ai team e ai servizi responsabili.

Ecco alcuni dei flussi di lavoro supportati da questa integrazione:

  * **Allocazione tra provider.** Raggruppa la spesa Cloudflare per prodotto, zona e account, quindi utilizza i tag virtuali per allocarla per team o linea di prodotto insieme ai costi di AWS, Azure e altri provider, tutto in un unico report.
  * **Rilevamento delle anomalie.** Gli avvisi di costo di Vantage monitorano ogni provider connesso e ti notificano tramite Slack o e-mail quando la spesa si discosta dal valore di riferimento, in modo che una variazione nella spesa per Workers o R2 venga visualizzata nello stesso modo in cui viene visualizzata per qualsiasi altro provider.
  * **Agenti FinOps e MCP.** Poni all'agente Vantage FinOps nella console una domanda come "Qual è stato il nostro principale fattore di costo la scorsa settimana per ogni provider?" oppure interroga gli stessi dati da Claude o ChatGPT tramite il server MCP ospitato da Vantage. La spesa per Cloudflare è inclusa insieme a quella per gli altri provider connessi.



Collega il tuo account Cloudflare nella [​console Vantage](https://console.vantage.sh/) e i tuoi costi appariranno accanto a tutto ciò che utilizzi. Non sono previste esportazioni manuali, caricamenti di fatture o pannelli di controllo separati da gestire. 

Questa API standardizzata di FOCUS funziona anche con altri strumenti Fintech.

## **Perché l'abbiamo creata**

Gli agenti fanno molto più che scrivere codice. Implementano Workers, forniscono bucket R2 e gestiscono database D1. Quando concedi l'accesso programmatico al tuo account Cloudflare, hai bisogno di visibilità programmatica sui costi che ne derivano. Non alla fine del mese, ma durante tutta la giornata, per prodotto, in un formato che un programma possa effettivamente utilizzare.

L'API per l'utilizzo fatturabile ha quel formato. Da anni i clienti ci chiedono una soluzione di utilizzo programmatico. I team finanziari desiderano importare le spese nei propri sistemi e attribuire i costi a progetti interni, team e persino ai clienti finali. Gli sviluppatori desiderano un comando curl che possano inserire in uno script. Ciascuno di questi flussi di lavoro prevedeva in precedenza uno screenshot o un'esportazione manuale. Ora si tratta di una chiamata HTTP o di una configurazione in Vantage.

## **Cosa succederà dopo?**

  * **Finestra temporale più dettagliata.** Oggi l'API restituisce righe relative al periodo di fatturazione, che per la maggior parte dei prodotti è giornaliero. Stiamo valutando la possibilità di fornire maggiori dettagli in tempo reale per i prodotti in cui ciò risulta opportuno.
  * **Previsioni.**`CumulatedContractedCost` ti indica a che punto della tua spesa ti trovi nel ciclo di fatturazione corrente. Vogliamo aiutarti a prevedere dove finirai e non solo a livello di account, ma anche a livello di prodotto.
  * **Copertura Enterprise.** Questa prima versione è disponibile solo in modalità self-service. È in fase di sviluppo un'esperienza equivalente per i contratti Enterprise.



## **Provala**

L'endpoint è attivo da oggi per tutti gli account self-service. Ottieni un token API con l'autorizzazione _Billing Read_ , punta il tuo curl su di esso e riceverai il tuo periodo di fatturazione corrente suddiviso per prodotto. Il riferimento completo è disponibile nella documentazione dell'API di Cloudflare. Per visualizzarlo insieme al resto della tua spesa cloud, collega il tuo account Cloudflare nella [​console Vantage](https://console.vantage.sh/).

Cloudflare ha dedicato anni a semplificare l'esecuzione di un numero sempre maggiore di componenti della tua infrastruttura sulla nostra rete. È ora di rendere altrettanto semplice vedere quanto ti costa tutto questo, su Cloudflare e ovunque desideri.

]]>01KZAYYT30CEB47FW2H8CBGZ7QIl tuo agente ha bisogno di un computer, non di un container: ecco @cloudflare/computerhttps://blog.cloudflare.com/it-it/cloudflare-computer/ Thu, 06 Aug 2026 03:01:56 GMTGli agenti hanno bisogno di più di un semplice container per scalare. Stiamo introducendo @cloudflare/computer, un runtime per agenti che orchestra dinamicamente tra isolati veloci ed efficienti e container Linux completi per fornire a ogni agente un computer dedicato.AgentiAgents WeekCloudflare WorkersContainerIAGli agenti più capaci hanno una cosa semplice in comune: a ciascuno viene fornito un computer personale da utilizzare.

Gli agenti di codifica funzionano in questo modo. Si fornisce loro un filesystem, una shell, strumenti, pacchetti e la capacità di eseguire codice. Esaminano l'ambiente, apportano modifiche, testano il loro lavoro e continuano. Il computer fornisce al modello un modo familiare di interagire con il mondo. Noi di Cloudflare ci impegniamo a fondo per fornire gli elementi base necessari per costruire gli agenti più performanti.

**Oggi presentiamo un'anteprima di[ @cloudflare/computer](https://github.com/cloudflare/workspace).** Il pacchetto @cloudflare/computer fornisce un ambiente di runtime per l'agente in cui i dettagli e i meccanismi relativi al codice eseguito in un ambiente isolato e a quello eseguito in una sandbox di container sono gestiti dalla piattaforma. Ogni agente dispone di un computer, l'esecuzione è ottimizzata per efficienza e scalabilità.

Riteniamo che, per soddisfare la crescente domanda di potenza di calcolo richiesta dai sistemi agenti, sia necessario esplorare soluzioni che vadano oltre la tradizionale containerizzazione. 

## Cambiare il modo in cui vengono creati gli agenti

Negli ultimi sei mesi, abbiamo assistito a una sottile evoluzione di questa storia. All'inizio dell'anno, avviare un container ed eseguire un agente al suo interno era la norma. Negli ultimi mesi, abbiamo assistito a una rapida evoluzione degli strumenti basati su agenti per fornire l'esecuzione di codice in un ambiente sandbox tramite appositi strumenti. Questo separa le mani (la sandbox in cui si lavora) dal cervello (il loop dell'agente).

Indipendentemente da dove passi l'harness, fornire un container a ogni agente rappresenta una sfida: tra tutti i cloud e tutti gli hyperscaler, non c'è neanche lontanamente abbastanza potenza di calcolo al mondo perché ogni azienda possa fornire a ciascun agente dei propri utenti un ambiente di calcolo containerizzato dedicato. Questa soluzione non è scalabile a centinaia di milioni, e poi miliardi, di agenti simultanei. Ecco perché c'è una domanda disperata e disperata da parte dell'industria per la potenza di calcolo delle CPU, non solo per quella delle GPU.

Noi di Cloudflare lavoriamo da tempo a questo problema, creando una primitiva di calcolo più efficiente: gli isolati. Abbiamo fatto quella scommessa controcorrente quasi 10 anni fa, quando abbiamo [introdotto Cloudflare Workers](https://blog.cloudflare.com/introducing-cloudflare-workers/). E poi l'abbiamo fatta di nuovo quando [abbiamo introdotto Durable Objects](https://blog.cloudflare.com/introducing-workers-durable-objects/) quasi sei anni fa. Abbiamo fatto questa scommessa perché gli isolati sono scalabili orizzontalmente all'infinito. Si creano e si distruggono in modo incredibilmente rapido Possono [ibernarsi](https://developers.cloudflare.com/durable-objects/examples/websocket-hibernation-server/) quando l'agente è inattivo, [memorizzare il proprio stato](https://blog.cloudflare.com/sqlite-in-durable-objects/) e persino [avviare i propri isolati](https://blog.cloudflare.com/dynamic-workers/) per eseguire codice non attendibile. Gli isolati sono il modo migliore per scalare orizzontalmente, e la scalabilità orizzontale è ciò che gli agenti richiedono.

L'anno scorso, abbiamo [dato agli isolati la possibilità di avviare i propri ambienti sandbox di container](https://blog.cloudflare.com/containers-are-available-in-public-beta-for-simple-global-and-programmable/). Fin dal primo giorno, l'architettura di Cloudflare è stata progettata per eseguire l'agente all'interno dell'isolato (in un Durable Object) e richiamare un container collegato su richiesta come strumento. Ciò consente di utilizzare primitive di calcolo più complesse solo quando necessario, ottimizzando prestazioni e costi. I Durable Objects scalano orizzontalmente in modo infinito e il container allegato consente di scalare verticalmente per eseguire qualsiasi compito. È così che costruiamo noi stessi gli agenti e vediamo i nostri clienti realizzare cose incredibili in questo stesso modo.

Ma se consideriamo la necessità di disporre di molteplici primitive di calcolo sottostanti per costruire agenti (isolati e container) e la necessità per i nostri clienti e sviluppatori di combinarli autonomamente nello spazio utente, riteniamo di poter fare di meglio. Riteniamo di poter fornire un'astrazione più semplice.

Ecco perché stiamo avviando questo esperimento distribuendo @cloudflare/computer come libreria open source, per imparare insieme ai nostri clienti che stanno spingendo al limite le capacità di esecuzione di agenti su larga scala.

## Un filesystem condiviso tra isolati e container

Il pacchetto @cloudflare/computer parte da una premessa semplice: e se fornissimo a un agente un filesystem preconfigurato, definito in modo dichiarativo, contenente tutto il necessario per l'attività in questione, e una selezione di ambienti di esecuzione per operare su tali file, ognuno con i propri vantaggi e svantaggi in termini di velocità, capacità e costi?

A quanto pare, gli agenti odierni sono sorprendentemente capaci di selezionare l'ambiente più adatto al compito da svolgere. Un processo che deve solo manipolare file, elaborare dati o gestire un repository Git può essere eseguito all'interno di un isolato. Un comando che richiede Linux, `npm` o un binario nativo può essere eseguito all'interno di un container. Entrambi operano sugli stessi file, che vengono mantenuti sincronizzati con il filesystem di origine.

Il pacchetto @cloudflare/computer fornisce un filesystem robusto che puoi utilizzare con repository Git, bucket di archiviazione o qualsiasi file tu scelga. Fornisce strumenti che consentono di leggere, scrivere e modificare file utilizzando la [modalità codice](https://blog.cloudflare.com/code-mode/) o i comandi bash. Tutte le operazioni sono controllate, monitorate e osservate, dandoti un controllo dettagliato sui cambiamenti che l'agente è autorizzato a eseguire, oltre a una chiara documentazione che mostra cosa ha fatto l'agente.

## Come si usa

È possibile creare un'istanza di un'area di lavoro @cloudflare/computer su qualsiasi Durable Object per fornire un filesystem virtuale e un ambiente di runtime per l'esecuzione.

Viene installato tramite npm:

L'utilizzo principale consiste nel fornire tale filesystem e gli strumenti necessari a un agente. Ad esempio, ecco come creare un'istanza dello spazio di lavoro su un agente basato su @cloudflare/think, destinato alla gestione delle segnalazioni di bug.

Il pacchetto @cloudflare/computer fornisce diversi backend di esecuzione, oppure è possibile scriverne uno personalizzato. Qui configuriamo un container Cloudflare.

Mettiamo a disposizione strumenti per la gestione di file, Git e la shell, insieme a strumenti specifici del prodotto, per rispondere ai problemi segnalati.

Il modello può utilizzare strumenti durante il ciclo dell'agente, ma è anche possibile utilizzare direttamente l'API dello spazio di lavoro, ad esempio per preparare l'ambiente prima di avviare l'agente.

Consulta il [repository dello spazio di lavoro](https://github.com/cloudflare/computer) per ulteriori esempi su come utilizzare i diversi backend e strumenti, incluso un [tutorial passo passo](https://github.com/cloudflare/computer/tree/main/examples/tutorial)che illustra come creare un agente da zero.

## Come funziona

L'elemento centrale di @cloudflare/computer è lo spazio di lavoro. Un filesystem virtuale basato su SQLite che può essere popolato da varie origini, tra cui l'archiviazione cloud e i sistemi di controllo versione.

Lo spazio di lavoro supporta runtime di esecuzione opzionali che consentono di eseguire codice direttamente sul file system. Tutti i runtime supportano la stessa interfaccia `exec(string, options)` e attualmente ne sono forniti due di default (ma è possibile scriverne di propri):

  * Un ambiente di runtime basato su isolate che utilizza [just-bash](https://justbash.dev/) per tradurre il codice shell in JavaScript viene eseguito in un [worker dinamico](https://developers.cloudflare.com/dynamic-workers/). In questo caso, il filesystem è disponibile direttamente tramite i binding dei worker.
  * Un runtime per container che utilizza [container Cloudflare](https://developers.cloudflare.com/containers/) per fornire un ambiente Linux completo. In questo caso, il filesystem viene fornito tramite un montaggio FUSE (Filesystem in Userspace), che garantisce la disponibilità dei file per il container e la sincronizzazione delle modifiche.



La classe `Workspace` fornisce un'interfaccia API per manipolare direttamente il filesystem, nonché un wrapper compatibile con `node:fs` che ne facilita l'utilizzo con librerie JavaScript di terze parti.

Per l'utilizzo con gli agenti, forniamo un toolkit compatibile con l'SDK di intelligenza artificiale che include gli strumenti più comuni: lettura, scrittura, modifica, ls ed esecuzione. Lo strumento exec è un po' particolare perché funziona su diversi runtime accettando un argomento `backend`. La descrizione dello strumento guida l'agente nella scelta del runtime corretto per l'attività da svolgere: un backend di lavoro veloce ed economico oppure un container completo di tutte le funzionalità. Nei nostri test, i modelli di frontiera si sono dimostrati molto efficaci nel prendere la decisione corretta e nel ricorrere all'utilizzo dei container solo quando necessario.

## E poi?

Qui in Cloudflare stiamo già notando che gli agenti utilizzano esclusivamente gli isolati per creare, testare e distribuire applicazioni JavaScript con strumenti moderni, generare documentazione personalizzata per ciascuno dei nostri clienti e utilizzare i browser web per eseguire attività complesse.

Il nostro obiettivo con @cloudflare/computer è fornire un agente con un runtime in cui un container sia necessario per meno del 10% del suo lavoro, e le attività di programmazione, la manipolazione audio/video e la creazione di documenti possano essere gestite dagli isolati. 

Prova [subito l'anteprima](https://github.com/cloudflare/computer): non vediamo l'ora di sapere cosa ne pensi.

]]>01KZAG0ZWEW7BKYDNDVJ218WSXTi diamo il benvenuto alla Agents Weekhttps://blog.cloudflare.com/it-it/agents-week-welcome/ Tue, 04 Aug 2026 03:49:10 GMTL'Agents Week esplora esplora come l'infrastruttura cloud debba evolversi per servire agenti autonomi anziché utenti umani. Unisciti a noi mentre esploriamo le primitive di archiviazione, esecuzione e sicurezza necessarie per un web nativo per agenti.AgentiAgents WeekCloudflare WorkersIAPiattaforma per sviluppatoriQuesta settimana è l'Agents Week.

Mentre iniziavamo a pensare e a pianificare la settimana, ci siamo scontrati con una questione più ampia: cosa significa sostenere questa nuova era di agenti e che aspetto dovrebbe avere una fondazione creata appositamente per gli agenti? Il che ci ha portato a una definizione più semplice: cos'è un cloud di agenti? 

Ci siamo rapidamente resi conto, tuttavia, che il nostro approccio era errato. Non perché fosse la domanda sbagliata, ma perché la stavamo ponendo a noi stessi, anziché ai nostri agenti. Non si tratta più di noi e di ciò che pensiamo, ma di ciò di cui gli agenti hanno bisogno. 

In poche parole, è questo ciò di cui tratta l'Agents Week. 

Il cloud che abbiamo oggi, e il web su cui si appoggia, sono stati costruiti per le persone. Ogni livello presume che un essere umano stia osservando: pagine progettate per catturare la tua attenzione, pannelli di controllo da cliccare, interfacce regolate su come leggiamo e decidiamo. Ma gli agenti non funzionano in questo modo. Non si distraggono, non si stancano e non si affaticano... e hanno le loro esigenze specifiche in termini di velocità, struttura e accessibilità.

Un cloud di agenti deve fare due cose contemporaneamente: deve prepararci a un futuro incentrato sugli agenti, in cui le primitive siano create appositamente per gli agenti fin dalle fondamenta, anziché essere adattate a partire da strumenti umani. E realisticamente, deve incontrarci dove siamo oggi, fungendo da livello di traduzione tra la rete plasmata dagli esseri umani che esiste ora e quella plasmata dagli agenti verso cui ci stiamo muovendo.

Questo sarà il filo conduttore dei prossimi cinque giorni: la forma di un cloud creato per agenti e esseri umani e il modo in cui interagiscono. In questa settimana verrà esplorato il tema analizzando cosa ciò significhi per i primitivi e il livello di esecuzione necessari, il ciclo di vita aggiornato dello sviluppo del software agentico, come le organizzazioni possono consentire in modo sicuro a dipendenti e agenti di interagire con controlli sicuri, come questo plasmi il web agentico e, infine, ancorando il tutto alla realtà degli agenti e degli esseri umani di oggi.

Tornando alla domanda iniziale: cosa può offrire un cloud di agenti al tuo agente? Anziché copiare e incollare le risposte che abbiamo ricevuto dai nostri agenti, ti incoraggiamo a porre la stessa domanda al tuo agente e a condividere eventuali spunti e risposte interessanti che otterrai. Ecco un esempio di prompt da utilizzare, ma ti incoraggiamo a esplorare le tue risposte:

_Di cosa hai bisogno, come agente, da un cloud di agenti? Immagina di dover gestire diverse categorie di cloud, tra cui un ambiente di archiviazione e calcolo cloud, le primitive di esecuzione e archiviazione necessarie, il ciclo di vita dello sviluppo (ADLC, simile all'SDLC ma senza l'intervento umano), l'accesso sicuro ai sistemi di registrazione all'interno di un'organizzazione per svolgere attività complesse e il web (individuazione, accesso, pagamenti...)._

Facci sapere cosa dice il tuo agente rispondendo qui, ci piacerebbe conoscere le risposte! 

[Segui il blog questa settimana](https://blog.cloudflare.com/) per le ultime novità sugli agenti e[ contattaci su X](https://x.com/CloudflareDev) per unirti alla conversazione.

]]>01KZ5CZQ998VPBFXBKK7KC1QR3Calamità naturali e interferenze governative: un'analisi dei maggiori eventi di interruzione di Internet nel secondo trimestre del 2026https://blog.cloudflare.com/it-it/q2-2026-internet-disruption-summary/ Fri, 31 Jul 2026 06:41:08 GMTNell'ultimo trimestre, Cloudflare Radar ha monitorato le interruzioni di Internet causate da calamità naturali, blocchi della rete ordinati dai governi e procedure di rollover delle chiavi DNSSEC. Questo post analizza i dati di telemetria del traffico per spiegare l'impatto di questi eventi sulla connettività globale.AWSDisservizioInternet ShutdownInternet TrafficInternet TrendsRadarCome la maggior parte delle infrastrutture, la fragilità di Internet è facile da trascurare... finché funziona. Quando si verifica un guasto, la sua complessità emerge in tutta la sua evidenza. Cloudflare si trova in una posizione privilegiata per rilevare e documentare i momenti in cui uno dei sistemi interconnessi da cui dipende Internet subisce un'interruzione, compromettendo la connettività. Ogni trimestre riassumiamo le disservizi che rileviamo e annotiamo su [Cloudflare Radar](https://radar.cloudflare.com/). 

Nel secondo trimestre del 2026, il super tifone Sinlaku, appena a nord di Guam, ha causato l'interruzione più lunga, mentre i blocchi della rete disposti dal governo durante i periodi degli esami in Sudan sono stati i più frequenti. L'Iran ha ripristinato l'accesso nazionale a Internet, riconnettendo i propri cittadini alla rete globale dopo un blackout di 88 giorni, mentre i danni provocati da attacchi con droni hanno continuato a causare disservizi alle infrastrutture AWS altrove nella regione. Infine, il taglio di un cavo a Saint Lucia e la diffusione di firme DNSSEC errate in Germania hanno messo in luce la fragilità delle infrastrutture Internet, ma anche la straordinaria stabilità che questi sistemi regionali e globali mantengono quando operano normalmente.

In questo articolo, esamineremo le interruzioni di Internet più significative osservate nel secondo trimestre del 2026, basandoci sui dati di traffico di Cloudflare Radar per mostrare come si sia evoluto ciascun evento e cosa abbia comportato per gli utenti sul campo. Come sempre, si tratta di una sintesi delle interruzioni confermate e più rilevanti, e non di un elenco esaustivo; una panoramica più completa delle anomalie di traffico rilevate è disponibile all'interno del [Cloudflare Radar Outage Center](https://radar.cloudflare.com/outage-center?dateStart=2026-04-01&amp;dateEnd=2026-06-30). 

## Le calamità naturali e l'elettricità causano interruzioni a Guam, in Venezuela e in Tanzania

Il super tifone Sinlaku, finora la tempesta più potente della stagione dei tifoni del Pacifico del 2026, ha attraversato le Isole Marianne a metà aprile, passando appena a nord di Guam. Sebbene l'isola sia stata risparmiata da un impatto diretto, la tempesta ha portato venti con forza di tempesta tropicale, provocando un blackout elettrico in tutta Guam e compromettendo i sistemi idrici, con un impatto diretto sulla connettività Internet. Tra il 13 e il 14 aprile, il traffico proveniente dal territorio è sceso fino all'80% al di sotto dei livelli previsti.

Due mesi dopo, il 24 giugno, due forti terremoti hanno colpito il Venezuela settentrionale a distanza di circa un minuto l'uno dall'altro, a Yumare e San Felipe, seguiti da una scossa di assestamento nei pressi della costa, al largo di Caracas. Il primo sisma, di magnitudo 7,5, si è verificato all'incirca alle 22:04 UTC (18:04 ora locale). L'impatto immediato di questi eventi è ben visibile su Radar, che mostra un drastico calo dei byte HTTP trasferiti in concomitanza con i terremoti. Questa diminuzione si può vedere particolarmente bene in Fibex Telecom, che, secondo i dati di [APNIC](https://stats.labs.apnic.net/aspop/), ha 1,6 milioni di utenti stimati. Il calo è visibile anche per [CANTV](https://radar.cloudflare.com/traffic/as8048?dateStart=2026-06-24&amp;dateEnd=2026-06-25#traffic-trends), l'ex monopolista statale, e per [VNET](https://radar.cloudflare.com/traffic/as263703?dateStart=2026-06-24&amp;dateEnd=2026-06-25), un provider di servizi Internet regionale leggermente più piccolo.

Dall'altra parte dell'Atlantico, solo pochi giorni dopo, un blackout elettrico in Tanzania il 27 giugno ha causato un netto calo del traffico HTTP durato almeno cinque ore. Sebbene la causa fosse diversa rispetto al blackout legato alle elezioni nell'ottobre 2025 (un'azione governativa deliberata anziché un guasto infrastrutturale), la telemetria risultante e l'impatto sugli utenti sono stati quasi identici: una drastica perdita di connettività che ha reso impossibile per i residenti comunicare con i propri cari o accedere a notizie di rilevanza critica. 

Colpisce come eventi così fondamentalmente diversi lascino un'impronta così simile nei dati e nell'esperienza utente. Nel loro insieme, queste interruzioni dovute a fattori meteorologici ed energetici dimostrano l'immenso impatto che il mondo fisico può avere su quello digitale, oltre all'importanza della resilienza di Internet e della realizzazione di reti dotate di sufficiente ridondanza nell'alimentazione, nel routing e nei percorsi fisici per resistere a shock inevitabili.

## Governi e geopolitica influenzano la connettività in Iran, Emirati Arabi Uniti, Iraq e Sudan

A partire dal 26 maggio, Radar ha iniziato a rilevare i segnali del ripristino di Internet precedentemente [annunciato](https://x.com/ir_aref/status/2059261258566877640?s=20) dall'Iran, che ha segnato la conclusione provvisoria di un'interruzione di 88 giorni che aveva lasciato il Paese quasi del tutto offline dal suo inizio, avvenuto il 28 febbraio. Il 27 maggio, Radar ha [segnalato](https://blog.cloudflare.com/iran-internet-partially-restored-may-2026/) che il traffico era stato ripristinato al 40% dei livelli precedenti all'interruzione, una riapertura parziale coerente con le notizie secondo cui l'accesso veniva riattivato in modo selettivo anziché simultaneo. Da allora, abbiamo osservato i byte HTTP salire fino al 90%, per poi assestarsi a circa il 59% dei livelli che precedevano l'interruzione. Questo volume è in linea con il traffico osservato a febbraio, una finestra temporale compresa tra questo recente blocco e quello precedente di gennaio, suggerendo che la connettività sia tornata a una sorta di livello di base più recente, anziché essersi completamente normalizzata. Nella nostra [analisi dei Mondiali del 2026](https://blog.cloudflare.com/2026-world-cup-internet-traffic/#streaming-makes-some-countries-appear-more-online), l'Iran si è distinto come un'anomalia isolata: mentre il traffico nella maggior parte dei paesi partecipanti saliva e scendeva in base al calendario delle partite, i rilevamenti dell'Iran sono stati dominati dal contrasto tra i livelli successivi al ripristino e la perdita quasi totale di connettività che li aveva preceduti.

Nel frattempo, il traffico HTTP verso me-central-1, una regione cloud AWS situata negli Emirati Arabi Uniti, è [rimasto basso](https://radar.cloudflare.com/cloud-observatory/amazon/me-central-1?dateRange=24w#http-traffic), in linea con [i report di servizio di AWS](https://health.aws.amazon.com/health/status#multipleservices-me-central-1_1777533954) del 30 aprile, secondo cui la regione "ha subito danni a seguito del conflitto in Medio Oriente e non è attualmente in grado di supportare in modo affidabile le applicazioni dei clienti". Questo aggiornamento segue i report del 3 marzo, secondo cui le strutture sia negli EAU che in Bahrein "hanno subito impatti fisici alle infrastrutture a causa di attacchi con droni". Negli Emirati Arabi Uniti, due strutture sono state "colpite direttamente", mentre in Bahrein un attacco con droni nelle vicinanze dell'impianto ha causato un "impatto fisico" alle relative infrastrutture. Il calo del traffico è la conseguenza a valle dei danni fisici all'infrastruttura sottostante dei datacenter, piuttosto che di un guasto di rete, e continua ad avere ripercussioni sui siti web e sulle applicazioni ospitate in quella regione, indipendentemente dalla loro effettiva disponibilità.

Nel secondo trimestre del 2026 si sono verificati anche tre blocchi della rete ordinati dal governo in Iraq (il [2 giugno](https://radar.cloudflare.com/traffic/iq?dateStart=2026-06-01&amp;dateEnd=2026-06-02), l'[11 giugno](https://radar.cloudflare.com/traffic/iq?dateStart=2026-06-10&amp;dateEnd=2026-06-11) e il [28 giugno](https://radar.cloudflare.com/traffic/iq?dateStart=2026-06-27&amp;dateEnd=2026-06-28)) così come [10 in Sudan](https://radar.cloudflare.com/traffic/sd?dateStart=2026-04-13&amp;dateEnd=2026-04-23#traffic-trends) tra il 13 e il 23 aprile, tutti imposti per prevenire frodi durante gli esami nazionali — un pattern stagionale che abbiamo documentato in diversi trimestri precedenti per entrambi i paesi. Le interruzioni in Sudan hanno seguito un ritmo costante, ciascuna con una durata di circa 3 ore e mezza, dalle 11:45 alle 15:15 UTC (dalle 13:45 alle 17:15 ora locale), in concomitanza con la finestra temporale degli esami. In Iraq le interruzioni sono state più brevi, di circa 90 minuti ciascuna, e allo stesso modo pianificate negli orari di svolgimento degli esami.

Ciascuno di questi esempi, che si tratti di un ripristino o di un'interruzione, illustra l'ampio controllo che i governi esercitano sulla connettività nazionale e la facilità con cui l'accesso può essere disattivato, limitato o reintrodotto in modo selettivo in virtù di decisioni politiche anziché per ragioni infrastrutturali.

## Le vulnerabilità dell'infrastruttura influiscono sugli utenti in Germania e Saint Lucia 

Il 5 maggio, un rollover delle chiavi DNSSEC presso DENIC, il registro del dominio .de in Germania, ha iniziato a generare firme non valide. dominio, [ha iniziato a produrre firme non valide](https://blog.denic.de/technische-storung-bei-de-domains-behoben/). Questi rollover delle chiavi consistono nella sostituzione periodica delle chiavi di crittografia utilizzate per firmare i record DNS di una zona; si tratta di un'operazione di manutenzione di routine ma fondamentale, poiché i resolver che effettuano la convalida DNSSEC considerano attendibili solo le risposte le cui firme corrispondono alle chiavi attualmente pubblicate. In altre parole, se le firme digitali non corrispondono ai valori previsti, il resolver presuppone che il sito sia stato manomesso e ne blocca l'accesso. Quando hanno iniziato a essere prodotte firme non valide, i resolver di convalida in tutto il mondo hanno rifiutato qualsiasi richiesta indirizzata a un sito .de, restituendo errori SERVFAIL fino al ripristino del normale funzionamento, avvenuto alle 23:15 UTC (le 01:15 ora locale del 6 maggio). 

Cloudflare Radar ha registrato un aumento del volume di query per il dominio .de Il volume delle a livello globale durante l'interruzione. Sebbene all'inizio possa apparire controintuitivo, ciò è dovuto al fatto che le risposte non riuscite non sono effettivamente memorizzabili in cache; di conseguenza, le interrogazioni che normalmente verrebbero servite in modo trasparente dalla cache hanno dovuto essere risolte da capo e ritentate ripetutamente, provocando un netto incremento delle query.

Dal punto di vista dell'utente, l'incidente non è stato percepito come un errore del DNS o un problema crittografico, ma semplicemente come un'improvvisa ondata di siti e servizi .de diventati irraggiungibili. Sebbene fosse ancora possibile accedere ai siti che non utilizzavano il TLD .de, gli utenti hanno riscontrato pagine che non si caricavano, e-mail respinte e app in timeout: tutti elementi del tutto simili ai sintomi di un'interruzione di rete. È possibile approfondire il tema del DNSSEC e l'impatto di questi eventi [sul nostro blog](https://blog.cloudflare.com/de-tld-outage-dnssec/).

Nei Caraibi, un guasto infrastrutturale ha causato un analogo calo della disponibilità. Il 21 giugno, il traffico di richieste HTTP della rete Karib Cable è sceso fino a quasi azzerarsi intorno alle 21:00 UTC (17:00 ora locale), rimanendo piatto per la maggior parte della giornata prima di tornare ai livelli previsti verso le 17:00 UTC del 22 giugno (13:00 ora locale). Secondo quanto [riferito](https://stluciatimes.com/181838/2026/07/flow-reveals-details-of-customer-rebates-after-major-outage/), l'interruzione è stata causata dal taglio di una fibra ottica nei pressi dell'isola, un rischio familiare per le reti caraibiche che dipendono da un numero limitato di percorsi terrestri e sottomarini per raggiungere il resto di Internet; ciò significa che un singolo tranciamento può compromettere una quantità sproporzionata di capacità. Poiché Karib Cable è uno dei principali provider, la perdita è risultata visibile anche a livello nazionale, con il traffico complessivo di Saint Lucia [sceso di circa il 60% rispetto alla settimana precedente](https://radar.cloudflare.com/explorer?dataSet=netflows&amp;loc=LC&amp;dt=2026-06-21_2026-06-27&amp;timeCompare=1#result) per tutta la durata del guasto.

### Radar continua a monitorare le interruzioni

Nel secondo trimestre del 2026 si sono verificate interruzioni di Internet dovute a un'ampia gamma di cause, tra cui condizioni meteorologiche estreme, un terremoto, blackout elettrici, blocchi della rete ordinati dai governi, danni alle infrastrutture cloud, tagli dei cavi ed errate configurazioni DNSSEC. Come dimostrano questi eventi, Internet dipende da un insieme complesso di sistemi interconnessi, e un guasto in uno qualsiasi di essi può comportare una perdita di connettività.

Il team di Cloudflare Radar monitora costantemente le interruzioni di Internet, condividendo le nostre osservazioni sul [Cloudflare Radar Outage Center](https://radar.cloudflare.com/outage-center), tramite i social media e in post su [blog.cloudflare.com](http://blog.cloudflare.com). Seguici sui social media su [@CloudflareRadar](https://twitter.com/CloudflareRadar) (X), [noc.social/@cloudflareradar](https://noc.social/@cloudflareradar) (Mastodon) e [radar.cloudflare.com](http://radar.cloudflare.com) (Bluesky).

]]>01KYVE5MWTJ60FQMPBTPREVP2BFesteggiamo i 12 anni del Progetto Galileohttps://blog.cloudflare.com/it-it/celebrating-12-years-of-project-galileo/ Thu, 18 Jun 2026 13:00:00 GMTPer celebrare il 12° anniversario del Progetto Galileo, Cloudflare ha pubblicato il suo primo report completo che analizza gli attacchi informatici contro la società civile.ImpattoProgetto GalileoDodici anni fa, questo mese, Cloudflare lanciava un progetto ambizioso basato su un'idea semplice: nessuno dovrebbe essere oscurato sul web solo perché esprime un'opinione contraria a quella di un potere più forte. Oggi, [Progetto Galileo](https://www.cloudflare.com/galileo/) fornisce accesso gratuito ai servizi di sicurezza informatica a oltre 3.400 siti web appartenenti a giornalisti, difensori dei diritti umani e altre organizzazioni senza scopo di lucro in 120 paesi. Noi [continuiamo](https://blog.cloudflare.com/protecting-free-expression-online/) a credere che un Internet migliore sia quello in cui chiunque abbia un'idea può raggiungere un pubblico globale. 

Ogni anno, nell'anniversario del Progetto Galileo, annunciamo nuovi prodotti, programmi e partnership strategiche. Per celebrare il nostro 12° anniversario quest'anno, stiamo pubblicando [il nostro primo report completo](https://cfl.re/cyberattacks-against-civil-society-project-galileo-anniversary-report) sugli attacchi informatici contro la società civile, rendendo disponibili [case study](https://www.cloudflare.com/project-galileo-case-studies/) che esplorano le esigenze di sicurezza di 16 partecipanti al Progetto Galileo e annunciando nuovi partner.

### Presentazione di un nuovo report annuale sugli attacchi informatici contro la società civile globale

Poiché il Progetto Galileo ora include 3.400 domini appartenenti a organizzazioni in oltre 120 paesi, Cloudflare ha accesso a dati univoci relativi alle minacce informatiche, agli attacchi e alle tendenze che prendono di mira la società civile, un pilastro fondamentale della democrazia globale. Inoltre, poiché la rete Cloudflare si estende su più di 335 città in 125 paesi e oltre il 20% del web è protetta da questa, siamo stati anche in grado di confrontare gli attacchi contro la società civile con quelli che prendono di mira Internet in modo più ampio. Il report completo può essere consultato [qui](https://cfl.re/cyberattacks-against-civil-society-project-galileo-anniversary-report).

I dati di quest'anno dimostrano che le organizzazioni della società civile sono state prese di mira più frequentemente, e spesso in modo più intenso, rispetto ad altri utenti di Internet. Gli attacchi informatici spesso hanno coinciso con momenti critici nel lavoro della società civile, come la pubblicazione di report investigativi o lo svolgimento di attività di difesa pubblica. I nostri risultati principali includono: 

  * Gli attacchi DDoS sono stati la minaccia informatica più comune contro la società civile. La loro caratteristica distintiva era la durata: alcuni di questi, infatti, avevano una durata di diversi giorni se non intere settimane.
  * I gruppi della società civile hanno affrontato tentativi di sfruttare le vulnerabilità dei siti web a un tasso più di sette volte superiore rispetto ad altri clienti di Cloudflare. Le organizzazioni dei media sono state colpite in modo sproporzionato.
  * I giornalisti che operavano in esilio hanno dovuto affrontare un tasso di traffico dannoso quasi quattro volte superiore rispetto alle organizzazioni giornalistiche in generale. 
  * Quasi il 10% di tutte le e-mail elaborate da Cloudflare per la società civile includeva potenziale materiale di phishing. 



Concludiamo il nostro report con un invito all'azione: garantire una sicurezza informatica semplice ed economicamente vantaggiosa per tutti, espandere la trasparenza sugli attacchi informatici e le chiusure di Internet e integrare le protezioni IA e post-quantistiche negli strumenti di sicurezza per impostazione predefinita. Ci auguriamo che questo rapporto possa fungere da risorsa per la società civile, i responsabili politici e il pubblico in generale, tutti soggetti che cercano di comprendere e rispondere agli attacchi informatici. In futuro, prevediamo di produrlo ogni anno, con l'obiettivo di confrontare le tendenze delle minacce informatiche nel tempo. 

Oltre al report, Cloudflare ha pubblicato i seguenti [case study qualitativi](https://www.cloudflare.com/project-galileo-case-studies/) che aggiungono contesto alle esigenze di sicurezza di ogni organizzazione.

Organizzazione| Descrizione| Paese/area geografica di attività  
---|---|---  
SHARE Foundation| Promozione senza scopo di lucro della privacy, della libertà di espressione e di altri diritti digitali.| Serbia   
Hledaczvirat| Piattaforma/database online per la ricerca di animali smarriti e ritrovati, collegando i proprietari con i rifugi per animali.| Repubblica Ceca  
Iran Watch/The Wisconsin Project| Progetto di ricerca che monitora le capacità armamentistiche dell'Iran e le questioni relative alla non proliferazione, gestito dal Wisconsin Project on Nuclear Arms Control. | Stati Uniti   
Bulletin of the Atomic Scientists| Organizzazione di media senza scopo di lucro che si occupa di rischio nucleare, cambiamenti climatici e tecnologia rivoluzionaria. | Stati Uniti  
The Royal Meteorological Society| [Solo in inglese] Società per la scienza del clima e del meteo, a supporto della ricerca meteorologica, dell'educazione e dell'accreditamento professionale.| Regno Unito  
Project Ainita| Un collettivo di ingegneri che sviluppa strumenti e ricerca per organizzazioni per i diritti umani, avvocati e attivisti che operano in ambienti ad alto rischio.| Globale  
Ukraine War Archive| Archivio digitale che documenta e conserva le prove di crimini di guerra ed eventi della guerra Russia-Ucraina. | Ucraina  
Our World in Data| Ricerca e pubblicazione di dati su questioni globali come povertà, salute e clima. | Regno Unito   
Hague Institute for Innovation of Law| Think-and-do tank focalizzato su sistemi di giustizia intuitivi e sulla risoluzione dei problemi di giustizia per le persone in tutto il mondo. | Paesi Bassi   
Center for American Progress| Think tank di ricerca e patrocinio sulle politiche pubbliche progressiste. | Stati Uniti  
Sea Shepherd Brazil| Capitolo brasiliano di Sea Shepherd, organizzazione per la conservazione marina che protegge la fauna e gli ecosistemi oceanici. | Brasile  
elTOQUE| Organo di stampa digitale indipendente che copre Cuba, inclusi notizie, economia e monitoraggio dei tassi di cambio. | Globale  
Humanitix| Piattaforma di biglietteria senza scopo di lucro che dona le commissioni di prenotazione a organizzazioni benefiche per l'educazione e la salute dei bambini. | Australia   
Organized Crime and Corruption Reporting Project (OCCRP)| Rete globale di giornalismo investigativo che espone crimine organizzato e corruzione. | Paesi Bassi  
Activist Rights| Risorsa di informazioni legali per gli attivisti sui loro diritti e rischi legali durante le proteste e le campagne. | Australia  
China Digital Times| Sito web di notizie bilingue che copre la censura, i diritti umani e la politica in Cina. | Stati Uniti   
  
### Un caloroso benvenuto ai nuovi partner 

Il Progetto Galileo si affida ai suoi 59 partner della società civile per avere successo. Ogni singola organizzazione che si candida al programma viene esaminata e approvata da uno di questi partner. Questi gruppi offrono volontariamente il loro tempo e le loro competenze, spesso vagliando più candidature al giorno, per garantire che i nostri servizi possano essere fruiti dalle organizzazioni meritevoli. 

Nel tempo, queste relazioni non solo hanno contribuito a far crescere il Progetto Galileo nel programma odierno, ma hanno anche introdotto iniziative completamente nuove, come la nostra partnership per la sicurezza delle e-mail con [Protect.ngo](https://protect.ngo/) (ex CyberPeace Institute) o il nostro lavoro a supporto della misurazione di Internet nelle scuole pubbliche attraverso il [progetto Giga](https://www.cloudflare.com/press/press-releases/2025/cloudflare-partners-with-giga-to-accelerate-school-connectivity-worldwide/) dell'UNICEF.

Per diversi anni, uno dei nostri obiettivi per il Progetto Galileo è stato quello di raggiungere più organizzazioni in aree geografiche al di fuori del Nord America e dell'Europa. Parte di questo sforzo è stata la partecipazione a eventi locali come RightsCon in Costa Rica (2023) e Taiwan (2025) per parlare direttamente con le organizzazioni locali in materia di diritti digitali. Abbiamo anche accolto nuovi partner che portano le proprie reti e comunità attive nel programma. Ad esempio, l'anno scorso abbiamo annunciato due nuovi partner nell'area Asia-Pacifico: EngageMedia e OpenCulture Foundation.

In seguito [alla recente aggiunta](https://blog.cloudflare.com/ai-crawl-control-for-project-galileo/) di nuovi servizi al Progetto Galileo per aiutare le testate giornalistiche locali a proteggere i propri contenuti dai crawler IA, la nostra partnership quest'anno si è concentrata sui gruppi al servizio dei giornalisti. A tal fine, siamo orgogliosi di annunciare tre nuovi partner:

Organizzazione| Descrizione| Paese/area geografica di attività  
---|---|---  
International Center for Journalists| L'organizzazione senza scopo di lucro si è concentrata sulla promozione del giornalismo indipendente di alta qualità. Fornisce formazione, borse di studio, tutoraggio e supporto finanziario ai giornalisti, specializzandosi nell'aiutare i giornalisti a sfruttare le tecnologie digitali. | Con sede negli Stati Uniti e supporto a giornalisti in oltre 180 paesi.  
Media Cluster Norway| Hub di innovazione incentrato sulla tecnologia multimediale di nuova generazione. Fornisce spazi di ricerca collaborativa, opportunità di finanziamento, incubazione di imprese ed eventi di networking per oltre 100 autori e redazioni locali. | Norvegia   
ONG-ISAC| Rete senza scopo di lucro incentrata sulla protezione della società civile dalle minacce alla sicurezza informatica. Fornisce intelligence delle minacce, coordinamento difensivo, formazione e supporto alla sua rete di oltre 1.000 organizzazioni senza scopo di lucro. | Stati Uniti   
  
### Continuare a proteggere la società civile in tutto il mondo 

Il nuovo report di oggi, i case study e i nuovi partner mirano tutti a lavorare verso l'obiettivo fondamentale del Progetto Galileo: garantire che gli attacchi informatici non mettano a tacere le organizzazioni che lavorano in aree vulnerabili ed essenziali come il giornalismo e i diritti umani. 

Guardando al futuro, continuiamo a impegnarci a trovare nuovi modi per espandere le nostre protezioni ai gruppi a rischio in tutto il mondo. Se la tua organizzazione è alla ricerca di protezione nell'ambito del Progetto Galileo, visita[ cloudflare.com/galileo](https://www.cloudflare.com/galileo/).

]]>1kBoofDb8dfLiYnekjlUaXProgetto Glasswing: cosa ci ha mostrato Mythoshttps://blog.cloudflare.com/it-it/cyber-frontier-models/ Mon, 18 May 2026 06:00:00 GMTNelle scorse settimane, abbiamo utilizzato Mythos e altri LLM focalizzati sulla sicurezza per analizzare codice reale in parti critiche della nostra infrastruttura. Condividiamo le nostre osservazioni, i punti di forza e di debolezza dei modelli e come dovrebbe essere il lavoro di approfondimento prima che questi possano essere applicati su larga scala.AgentiAutomazioneCustomer ZeroGestione del rischioIAIngegneriaLLMOperazioni sulle minacceSicurezzaThreat IntelligenceNegli ultimi mesi, abbiamo testato una gamma di LLM incentrati sulla sicurezza sulla nostra infrastruttura. Questi LLM aiutano a identificare potenziali vulnerabilità nei nostri sistemi in modo da poterle risolvere e ci mostrano anche cosa potrebbero fare gli aggressori con i modelli più recenti.

Nessuno di questi LLM ha attirato più attenzione di Mythos Preview di Anthropic. Alcune settimane fa, siamo stati invitati a utilizzare Mythos Preview come parte di [Progetto Glasswing](https://www.anthropic.com/glasswing). Lo abbiamo subito puntato su oltre cinquanta dei nostri repository, per vedere cosa avrebbe trovato e come funzionava. 

Questo post condivide le nostre osservazioni, i punti di forza e di debolezza dei modelli, e come l'architettura e i processi ad essi correlati debbano cambiare affinché possano essere utilizzati su larga scala.

## Cosa è cambiato con Mythos Preview

Mythos Preview rappresenta un vero passo avanti, ed è bene dirlo chiaramente prima di addentrarci in altro. Da tempo eseguiamo test con i nostri modelli e il salto da ciò che era possibile con i precedenti modelli di frontiera generici a ciò che Mythos Preview fa oggi non è solo un perfezionamento di ciò che c'era prima.

Si tratta di uno strumento diverso, che svolge un lavoro diverso, e questo rende difficile un confronto diretto con i modelli precedenti. Piuttosto che cercare di confrontare Mythos Preview con modelli di frontiera generici, è più utile descrivere cosa può effettivamente fare e due caratteristiche che si sono distinte durante il lavoro che abbiamo svolto con Mythos Preview:

  * **Costruzione di una catena di exploit** : un attacco reale raramente utilizza un solo bug ma concatena diverse piccole primitive di attacco in un exploit funzionante. Ad esempio, potrebbe trasformare un bug di tipo use-after-free in una primitiva di lettura e scrittura arbitraria, dirottare il flusso di controllo e utilizzare catene di programmazione orientata al ritorno (ROP) per assumere il pieno controllo di un sistema. Mythos Preview può prendere diverse di queste primitive e ragionare su come combinarle in una dimostrazione funzionante. Il ragionamento che emerge durante il processo sembra più opera di un ricercatore senior che il risultato di uno scanner automatico.
  * **Generazione di prove** : trovare un bug e dimostrare che è sfruttabile sono due cose diverse, e Mythos Preview può fare entrambe. Scrive del codice che attiverebbe il presunto bug, lo compila in un ambiente di test e lo esegue. Se il programma si comporta come previsto dal modello, questa è la prova. Se ciò non accade, il modello rileva l'errore, modifica la sua ipotesi e riprova. Il ciclo di test è importante tanto quanto i bug che individua, perché un presunto difetto senza una prova concreta rimane una mera speculazione, e Mythos Preview colma questa lacuna in modo autonomo.



Alcuni degli aspetti descritti sopra non sono esclusivi di Mythos Preview. Quando abbiamo testato altri modelli di frontiera con lo stesso sistema, abbiamo riscontrato un buon numero degli stessi bug di fondo e, in alcuni casi, siamo andati oltre le nostre aspettative anche sul fronte del ragionamento. Il loro errore è stato nella fase di assemblaggio dei vari pezzi. Un modello identificherebbe un bug interessante, scriverebbe una descrizione ponderata del perché sia importante e poi si fermerebbe, lasciando la catena di operazioni incompleta e la questione della sua sfruttabilità aperta. La novità introdotta con Mythos Preview è che ora un modello può individuare quei bug di bassa gravità (che tradizionalmente rimarrebbero invisibili in un backlog) e concatenarli in un unico exploit più grave. 

## Rifiuti di modelli nella ricerca legittima della vulnerabilità

Il modello Mythos Preview fornito da Anthropic, nell'ambito del Progetto Glasswing, non disponeva delle misure di sicurezza aggiuntive presenti nei modelli generalmente disponibili (come Opus 4.7 o GPT-5.5).

Nonostante ciò, il modello respinge organicamente alcune richieste: proprio come le capacità informatiche che lo hanno reso utile per la ricerca di vulnerabilità, il modello ha i suoi meccanismi di protezione emergenti che a volte lo portano a respingere richieste legittime di ricerca sulla sicurezza. Come abbiamo scoperto, però, questi rifiuti spontanei non sono costanti: lo stesso compito, formulato in modo diverso o presentato in un contesto differente, potrebbe produrre risultati completamente diversi, come illustrato negli esempi seguenti.

_Esempio di Mythos Preview che si oppone alla creazione di una prova di concetto funzionante_

Ad esempio, il modello inizialmente si è rifiutato di effettuare una ricerca di vulnerabilità su un progetto, per poi accettare di eseguire la stessa ricerca sullo stesso codice dopo una modifica non correlata all'ambiente del progetto. Nulla del codice analizzato era cambiato.   
  
In un altro caso, il modello ha individuato e confermato diversi gravi bug di memoria in una base di codice, e si è poi rifiutato di scrivere un exploit dimostrativo. La stessa richiesta, formulata in modo diverso, ha ottenuto una risposta diversa, e persino la stessa richiesta può produrre risultati diversi in esecuzioni diverse a causa della natura probabilistica del modello. Compiti semanticamente equivalenti possono produrre risultati opposti a seconda di come e quando vengono presentati al modello.

Questo è importante perché, sebbene i rifiuti/le barriere di sicurezza organiche del modello siano reali, non sono sufficientemente costanti da costituire da sole un confine di sicurezza completo. Ecco perché qualsiasi modello di frontiera cibernetica efficace reso disponibile al pubblico in futuro dovrà includere ulteriori misure di sicurezza, oltre a questo comportamento di base, in modo da renderlo adatto a un utilizzo più ampio al di fuori di un contesto di ricerca controllato come il Progetto Glasswing.

## Il problema del rapporto segnale-rumore

Una delle parti più difficili della valutazione delle vulnerabilità di sicurezza è decidere quali bug sono reali, quali sono sfruttabili e quali devono essere corretti immediatamente. Questo era un problema difficile anche nel mondo pre-intelligenza artificiale. Gli scanner di vulnerabilità basati sull'IA e il codice generato dall'IA hanno peggiorato la situazione, e noi di Cloudflare abbiamo sviluppato diverse fasi di post-validazione per far fronte a questo problema.

Due fattori dominano il tasso di rumore:

  * **Linguaggio di programmazione** : C e C++ offrono il controllo diretto della memoria e, con esso, classi di bug - buffer overflow, letture e scritture fuori dai limiti - che i linguaggi sicuri per la memoria come Rust eliminano in fase di compilazione. Abbiamo riscontrato un numero costantemente maggiore di falsi positivi nei progetti scritti in linguaggi non sicuri per la memoria.
  * **Pregiudizio del modello** : un buon ricercatore umano ti dice cosa ha scoperto e quanto è sicuro dei suoi risultati. I modelli no. Chiedi a un modello di trovare i bug e li troverà, a prescindere dal fatto che il codice ne contenga o meno. I risultati vengono presentati con espressioni come "forse", "potenzialmente", "in teoria" e sono di gran lunga più numerosi di quelli certi. Si tratta di un pregiudizio ragionevole per uno strumento esplorativo. È un sistema disastroso per la gestione delle richieste di diagnosi, dove ogni risultato ipotetico richiede attenzione umana e gettoni per essere scartato, e questo costo si moltiplica su migliaia di risultati.



Mythos Preview rappresenta un netto miglioramento in questo senso, in particolare nella sua capacità di concatenare le primitive, combinando più vulnerabilità in una prova di concetto funzionante anziché segnalarle singolarmente. Un risultato che arriva con una prova di concetto (PoC) è un risultato su cui si può agire, e significa molto meno tempo speso a chiedersi "è davvero reale?".

I nostri sistemi di monitoraggio sono volutamente tarati per sovrastimare le segnalazioni, in modo da poter rilevare più eventi (e trascurarne di meno), il che comporta però un rumore di fondo molto maggiore. Ma in fase di triage, l'output di Mythos Preview presenta una qualità nettamente superiore: meno risultati ambigui, passaggi di riproduzione più chiari e meno lavoro per giungere a una decisione di correzione o rigetto.

## Perché puntare un agente di codifica generico a un repository non funziona

Quando abbiamo iniziato la ricerca sulle vulnerabilità assistita dall'IA lo scorso anno, il nostro primo istinto è stato quello più ovvio: puntare un agente di programmazione generico verso un repository arbitrario e chiedergli di scoprire le vulnerabilità. Questo approccio funziona, nel senso che il modello produrrà dei risultati, ma non è efficace nel fornire una copertura significativa di una codebase reale e nell'identificare risultati di valore. Ci sono due ragioni principali per questo:

  * **Contesto** : gli agenti di codifica sono ottimizzati per un flusso di lavoro specifico: creare una funzionalità, correggere un bug, scrivere un refactoring. Analizzano una grande quantità di codice sorgente, si concentrano su una singola ipotesi alla volta e la verificano iterativamente. Questa non è affatto la forma adatta per la ricerca sulla vulnerabilità, che per sua natura è ristretta e parallela. Un ricercatore umano sceglie un elemento specifico da esaminare e lo analizza a fondo. Potrebbe trattarsi di una singola funzionalità complessa, di transizioni attraverso i confini di sicurezza o di una specifica classe di vulnerabilità come le iniezioni di comandi, in cui l'input dell'attaccante viene eseguito come comando di shell. Poi lo ripetono, per una diversa funzionalità, un diverso confine di sicurezza o una diversa classe di vulnerabilità, diverse migliaia di volte nell'intero codice sorgente. Una singola sessione di un agente (anche con subagenti) su un repository di centomila righe può coprire forse un decimo dell'uno per cento della superficie in modo utile prima che la finestra di contesto del modello si riempia e si attivi la compattazione, scartando potenzialmente risultati precedenti che sarebbero stati importanti.
  * **Throughput** : un agente a flusso singolo fa una cosa alla volta, ma le codebase reali hanno bisogno di molte ipotesi su molti componenti contemporaneamente, con la capacità di espandersi ulteriormente quando emerge qualcosa di interessante. È possibile spingere un singolo agente a dare il massimo, ma a un certo punto si smette di essere limitati dal modello e si inizia ad essere limitati dalla forma stessa dell'interazione. L'utilizzo diretto del modello in un agente di codifica si rivela efficace per le indagini manuali quando un ricercatore ha già una pista e desidera un secondo parere. Tuttavia, non è lo strumento adatto per ottenere un'elevata copertura. Una volta accettato questo fatto, abbiamo smesso di cercare di far fare a Mythos Preview la funzione sbagliata e abbiamo iniziato invece a costruire l'infrastruttura attorno ad essa.



## Cosa risolve effettivamente un'imbracatura

Dall'esecuzione del progetto su larga scala sono emersi quattro insegnamenti, ognuno dei quali ha evidenziato la necessità di un sistema di gestione che coordini l'intera esecuzione:

  * **Un ambito ristretto produce risultati migliori** : dire al modello "Trova vulnerabilità in questo repository" gli fa perdere tempo e lo fa rimanere vago. Dirgli "Cerca l'iniezione di comandi in questa specifica funzione, con questo limite di fiducia sopra, ecco il documento di architettura ed ecco la documentazione precedente su quest'area" lo fa comportarsi in modo molto più simile a quello che farebbe un ricercatore.
  * **La revisione avversaria riduce il rumore** : l'aggiunta di un secondo agente tra il risultato iniziale e la coda - uno con un prompt diverso, un modello diverso e senza la capacità di generare i propri risultati - cattura gran parte del rumore che il primo agente non rileverebbe se si limitasse a controllare il proprio lavoro. A quanto pare, mettere deliberatamente due agenti in disaccordo è molto più efficace che limitarsi a dire a uno solo di fare attenzione.
  * **Dividere la catena tra gli agenti produce un ragionamento migliore** : chiedere "Questo codice è pieno di bug?" e "Un aggressore può effettivamente raggiungere questo bug dall'esterno del sistema?" sono due domande diverse e il modello è più efficace in ciascuna di esse quando vengono poste separatamente, perché ogni domanda è più specifica rispetto alla versione combinata.
  * **Compiti ristretti in parallelo superano un agente esaustivo** : la copertura migliora quando molti agenti lavorano su domande con ambito ristretto e successivamente eliminiamo i duplicati dei risultati, invece di chiedere a un agente di essere esaustivo.



Ciascuna di queste osservazioni riguarda il comportamento del modello e, messe insieme, descrivono qualcosa che non è più un'interfaccia di chat. Si tratta di un'imbracatura che ti aiuta a raggiungere i risultati finali. I primi passi per costruire un'imbracatura sono semplici, dato che si può chiedere aiuto al modello, ed è proprio quello che abbiamo fatto. Abbiamo utilizzato Mythos Preview per sviluppare, personalizzare e migliorare i nostri sistemi di imbracatura originali in modo da sfruttarne i punti di forza.  
  
Di seguito viene descritto un esempio pratico di come si presenta un'imbracatura.

## Il nostro strumento di scoperta delle vulnerabilità

Ecco come appare il nostro strumento per la scoperta delle vulnerabilità, fase per fase. È stato utilizzato per analizzare il codice in tempo reale nel nostro ambiente di runtime, nel percorso dati periferico, nello stack di protocolli, nel piano di controllo e nei progetti open source da cui dipendiamo.

## Cosa significa questo per i team di sicurezza

La reazione più forte da parte degli altri responsabili della sicurezza alla Mythos Preview riguarda la velocità: scansionare più velocemente, applicare le patch più velocemente, comprimere i tempi di risposta. Più di un team con cui abbiamo parlato ora opera con un SLA di due ore dal rilascio della CVE all'implementazione della patch in produzione. L'istinto è comprensibile: quando i tempi dell'aggressore si accorciano, anche quelli di chi si difende devono accorciarsi di conseguenza. Essere più veloci non basterà, e pensiamo che molte squadre stiano per spendere molto tempo, impegno e denaro per impararlo a proprie spese.

Applicare le patch più velocemente non modifica la struttura della pipeline che le produce. Se i test di regressione richiedono un giorno, non è possibile raggiungere un SLA di due ore senza saltarli, e i bug che si introducono quando si saltano i test di regressione tendono ad essere peggiori dei bug che si stava cercando di correggere. Abbiamo appreso una versione di questo fenomeno quando abbiamo provato a lasciare che il modello scrivesse le proprie patch e abbiamo visto alcune di esse, che risolvevano il bug originale ma che silenziosamente causavano problemi a qualcos'altro da cui dipendeva il codice, essere rilasciate.

La questione più complessa è quale dovrebbe essere l'architettura necessaria per gestire la vulnerabilità. Il principio è quello di rendere più difficile lo sfruttamento da parte di un aggressore anche in presenza di un bug, in modo che il lasso di tempo tra la divulgazione di una vulnerabilità e la sua correzione diventi meno rilevante. Ciò significa che si tratta di difese che si interpongono tra l'applicazione e il dispositivo di protezione, impedendo che il bug venga sfruttato. Significa progettare l'applicazione in modo tale che una falla in una parte del codice non possa consentire a un utente malintenzionato di accedere ad altre parti. Significa essere in grado di implementare una correzione contemporaneamente in tutti i punti in cui il codice è in esecuzione, anziché attendere che i singoli team la distribuiscano. 

Riconosciamo inoltre che questo argomento ha risvolti contrastanti. Le stesse capacità che ci hanno aiutato a trovare bug nel nostro codice, se finissero nelle mani sbagliate, accelererebbero gli attacchi contro ogni applicazione presente su Internet. Cloudflare si trova davanti a milioni di queste applicazioni e i principi architetturali descritti sopra sono esattamente quelli che i nostri prodotti sono progettati per applicare a beneficio dei clienti. Nelle prossime settimane condivideremo maggiori dettagli su cosa ciò significhi per i clienti.

Se il tuo team sta svolgendo un lavoro simile e desidera confrontarsi, contattaci all'indirizzo [security-ai-research@cloudflare.com](mailto:security-ai-research@cloudflare.com).

_La nostra ricerca con Mythos Preview è stata condotta in un ambiente controllato sul nostro codice; ogni vulnerabilità emersa durante questo lavoro è stata analizzata, convalidata e corretta laddove necessario, secondo la procedura formale di gestione delle vulnerabilità di Cloudflare._

_Questo lavoro è stato uno sforzo di squadra. Grazie ad Albert Pedersen, Craig Strubhart, Dan Jones, Irtefa Fairuz, Martin Schwarzl e Rohit Chenna Reddy per i loro contributi alla ricerca, ingegneria e analisi che stanno alla base di questo post sul blog._

]]>xrcYtr7kU54LNDB8MEmQYCostruire per il futurohttps://blog.cloudflare.com/it-it/building-for-the-future/ Thu, 07 May 2026 20:15:12 GMTQuesto pomeriggio, abbiamo inviato la seguente email al nostro team globale. In Cloudflare la trasparenza è un valore fondamentale. Per questo crediamo sia importante che lo veniate a sapere direttamente da noi: stiamo vivendo un momento storico per Cloudflare. TeamQuesto pomeriggio, abbiamo inviato la seguente email al nostro team globale. Uno dei nostri valori fondamentali in Cloudflare è la trasparenza e crediamo sia importante che lo sentiate direttamente da noi perché è un momento cruciale per Cloudflare. 

> _Alla corte attenzione del nostro Team:_

> _Vi scriviamo per informarvi direttamente che abbiamo preso la decisione di ridurre il personale di Cloudflare di oltre 1.100 dipendenti a livello globale._

> _Il modo in cui lavoriamo in Cloudflare è cambiato radicalmente. Non ci limitiamo a creare e vendere strumenti e piattaforme IA. Siamo il nostro cliente più esigente. L'uso dell'IA da parte di Cloudflare è aumentato di oltre il 600% negli ultimi tre mesi. I dipendenti in tutta l'azienda, dall'ingegneria alle risorse umane, alla finanza e al marketing, eseguono migliaia di sessioni di agenti IA ogni giorno per completare il loro lavoro. Questo significa che dobbiamo strutturare la nostra azienda in modo intenzionale per l'era dell'IA agentica, in modo da potenziare il valore che offriamo ai nostri clienti e onorare la nostra missione di contribuire a creare un Internet migliore per tutti, ovunque._

> _Oggi è una giornata difficile. Purtroppo, questa decisione significa dover dire addio a colleghi che hanno contribuito in modo significativo alla nostra missione e a rendere Cloudflare una delle aziende di maggior successo al mondo. Ci teniamo a precisare che questa decisione non è un riflesso del lavoro o del talento dei singoli colleghi che ci lasciano. Stiamo invece ripensando ogni processo interno, team e ruolo in tutta l'azienda. Le decisioni odierne non rappresentano una manovra di riduzione dei costi, né una valutazione delle performance individuali; servono a Cloudflare per definire come un'azienda all'avanguardia e in forte crescita opera e genera valore nell'era dell'IA agentica._

> _Questo è un momento di cui dobbiamo assumerci la piena responsabilità come fondatori e leader dell'azienda. Matthew ha inviato personalmente ogni singola lettera di assunzione che abbiamo formulato. È un momento che ha sempre atteso con entusiasmo, perché rappresentava la nostra crescita e l'incredibile talento che si univa alla nostra missione. Non ci sembrava giusto che questa comunicazione vi arrivasse da nessun altro se non da noi due. Invece di far circolare le notizie a poco a poco tramite i manager, invieremo un'email a ogni singolo dipendente._

> _Entro la prossima ora, ogni membro del nostro team globale riceverà un'email da parte di entrambi, che chiarirà in che modo questo cambiamento lo riguarderà direttamente. Per i colleghi che ci lasciano oggi, invieremo questo aggiornamento sia all'indirizzo email personale che a quello di Cloudflare, per assicurarci che ricevano le informazioni immediatamente._

> _Per noi è essenziale trattare con il giusto rispetto i colleghi che ci lasciano, agendo in un modo che vada oltre ciò che abbiamo visto in altre aziende. Siamo convinti che agire con empatia non significhi evitare le decisioni difficili, ma riguardi piuttosto il modo in cui si trattano le persone quando tali decisioni vengono prese. Se ci aspettiamo che il nostro team sia un'eccellenza, abbiamo l'obbligo reciproco di essere eccellenti nel modo in cui trattiamo le nostre persone. Uniamo la natura diretta di queste misure a condizioni di uscita all'avanguardia nel settore. Le condizioni di uscita per il personale comprenderanno l'equivalente dell'intero stipendio base fino al termine del 2026. Le condizioni di assistenza sanitaria differiscono a livello globale; per il personale residente negli Stati Uniti, il supporto verrà mantenuto fino al termine dell'anno. Inoltre, estenderemo la maturazione delle azioni per i colleghi in uscita fino al 15 agosto, in modo che possano ricevere le quote anche oltre la data di fine rapporto. Inoltre, nel caso in cui il personale in uscita non abbia ancora raggiunto la soglia del primo anno per la maturazione delle azioni (cliff), derogheremo a tale condizione, garantendo la maturazione pro quota delle azioni fino ad agosto._

> _Abbiamo chiesto al team di compiere questo passo una sola volta, per quanto possa essere difficile oggi. E non vogliamo doverlo rifare nel prossimo futuro. Agendo con decisione in questo momento, offriamo chiarezza immediata a chi ci lascia e tuteliamo la stabilità del team che resta. Stiamo attuando questi cambiamenti ora perché procedere con tagli minori e ripetuti, o trascinare una riorganizzazione per più trimestri, genera una prolungata incertezza emotiva per i dipendenti e frena la nostra capacità creativa. È l'azione più corretta da intraprendere, è la scelta più trasparente e rispecchia i valori della realtà aziendale che continuiamo a sviluppare._

> _Cloudflare è nata come azienda nativa digitale, costruita nel cloud. Questo ci ha permesso di raggiungere e superare realtà che avevano un vantaggio di anni o decenni, ma che erano frenate da sistemi e processi obsoleti. Oggi che siamo diventati leader, non possiamo adagiarci sui flussi di lavoro e sulle strutture organizzative che funzionavano ieri. Siamo certi che il nostro nuovo assetto ci renderà ancora più veloci e innovativi, nel nostro cammino per costruire il futuro._

> _Ai colleghi che ci lasciano: avete contribuito a costruire le solide fondamenta su cui Cloudflare poggia oggi. Nutriamo il massimo rispetto per il vostro lavoro e una profonda gratitudine per l'impatto che avete avuto. Siamo convinti che saprete distinguervi in altre prestigiose realtà e dare vita a nuove società di successo, forti del patrimonio unico di abilità maturate durante il vostro percorso in Cloudflare._

> _La trasparenza è un principio cardine di Cloudflare, ed era importante che lo sapeste innanzitutto da noi. Alle 14:00 PT (le 23:00 in Italia) parteciperemo alla conference call sui risultati finanziari, dove condivideremo ulteriori dettagli. Abbiamo inoltre in programma di discutere gli annunci di oggi in diretta con tutto il team durante la nostra riunione plenaria._

> _Non è una giornata facile, ma è la decisione giusta. La nostra missione di aiutare a creare un Internet migliore è più importante ora che mai, e c'è ancora molto lavoro da fare._

]]>4XKENJm0fq33smsBSmUIc5Code Orange: Fail Small è stato completato. Il risultato è una rete Cloudflare più solidahttps://blog.cloudflare.com/it-it/code-orange-fail-small-complete/ Fri, 01 May 2026 21:07:30 GMTAbbiamo portato a termine un grande progetto di ingegneria per rendere la nostra infrastruttura più resistente. Grazie a nuovi strumenti come Snapstone e l'Engineering Codex, abbiamo implementato modifiche di configurazione più sicure e best practice automatizzate per prevenire incidenti futuri.Code OrangeDisservizioPost mortemNegli ultimi due trimestri e mezzo, abbiamo intrapreso uno sforzo ingegneristico intensivo, con nome in codice interno "[Code Orange: Fail Small](https://blog.cloudflare.com/fail-small-resilience-plan/)", volto a rendere l'infrastruttura di Cloudflare più resiliente, sicura e affidabile per ogni cliente.

All'inizio di questo mese, il team di Cloudflare ha completato questo lavoro.

Anche se il miglioramento della resilienza non dovrà mai essere un "lavoro finito" e sarà sempre una priorità assoluta lungo l'intero ciclo di vita del nostro sviluppo, i lavori che ci avrebbero evitato le interruzioni globali del [18 novembre 2025](https://blog.cloudflare.com/18-november-2025-outage/) e del [5 dicembre 2025](https://blog.cloudflare.com/5-december-2025-outage/) sono ora completati.

Questo lavoro si è concentrato su diverse aree chiave: modifiche di configurazione più sicure, riduzione dell'impatto dei guasti e revisione delle nostre procedure di emergenza e gestione degli incidenti. Abbiamo anche introdotto misure per prevenire gli scostamenti e le regressioni nel tempo e rafforzato il modo in cui comunichiamo ai nostri clienti durante un'interruzione.

In questo articolo, ti spieghiamo nel dettaglio cosa abbiamo messo in atto e cosa significa per te.

### Modifiche alla configurazione più sicure

 _**Cosa significa per te** : nella maggior parte dei casi, le modifiche alla configurazione interna di Cloudflare non raggiungono più la nostra rete istantaneamente e vengono invece distribuite in modo progressivo con monitoraggio in tempo reale dell'integrità. Questo consente ai nostri strumenti di osservabilità di rilevare i problemi e risolverli prima che influiscano sul tuo traffico._

Per individuare potenziali distribuzioni pericolose prima che raggiungano l'ambiente di produzione, abbiamo identificato pipeline di configurazione ad alto rischio e creato nuovi strumenti per gestire meglio le modifiche alla configurazione.

Per i prodotti che operano sulla nostra rete di elaborazione del traffico dei clienti e ricevono le modifiche alla configurazione, non distribuiamo più tali modifiche istantaneamente su tutta la rete. Invece, i team pertinenti hanno adottato una metodologia di "distribuzione mediata dall'integrità", la stessa che [utilizziamo per il rilascio del software](https://blog.cloudflare.com/safe-change-at-any-scale/), per tutte le distribuzioni di configurazione. Ciò include, a titolo esemplificativo, i team di prodotto che sono stati direttamente interessati dagli incidenti.

Elemento centrale del cambiamento è un nuovo componente interno denominato Snapstone, che abbiamo creato per trasferire la distribuzione mediata dall'integrità alle modifiche alla configurazione. Snapstone è un sistema che racchiude le modifiche di configurazione in un pacchetto, quindi consente di rilasciare gradualmente la modifica di configurazione con i principi di mediazione dell'integrità. Prima di Snapstone, applicare questa metodologia alla configurazione era possibile ma complicato. Richiedeva un notevole impegno per ogni singolo gruppo e non veniva applicato in modo coerente nella rete. Snapstone colma questa lacuna offrendo un sistema unificato per fornire distribuzione progressiva, monitoraggio dell'integrità in tempo reale e rollback automatico alle distribuzioni di configurazione per impostazione predefinita.

Ciò che rende particolarmente potente Snapstone è la sua flessibilità. Anziché offrire una soluzione a problemi specifici passati, Snapstone consente ai team di definire dinamicamente qualsiasi unità configurativa che richieda una mediazione dell'integrità, sia che si tratti di un file dati come quello che ha causato l'[interruzione del 18 novembre](https://blog.cloudflare.com/18-november-2025-outage/), sia che si tratti un flag di controllo nel nostro sistema di configurazione globale, come quello coinvolto nell'[interruzione del 5 dicembre](https://blog.cloudflare.com/5-december-2025-outage/). I team creano queste unità di configurazione su richiesta e Snapstone si assicura che vengano distribuite in modo sicuro in qualsiasi luogo vengano utilizzate.

Questo ci offre qualcosa che prima non avevamo. In altre parole, quando una verifica dei rischi o un'esperienza operativa identifica uno schema di configurazione pericoloso, la soluzione è semplice: viene importato in Snapstone e questo erediterà immediatamente la distribuzione sicura. 

### Ridurre l'impatto del guasto

 _**Cosa significa per te** : nel caso in cui venga rilevato un problema nella nostra rete, i nostri sistemi ora si interrompono in modo più graduale. In questo modo, si riduce notevolmente il potenziale raggio d'impatto, per garantire che il traffico venga distribuito anche nello scenario peggiore possibile._

I team di prodotto hanno esaminato attentamente, sia in modalità manuale che programmatica, le loro potenziali modalità di guasto per i prodotti che sono fondamentali per gestire il traffico dei clienti. I team hanno rimosso le dipendenze runtime non essenziali e implementato modalità di guasto migliori. D'ora in poi utilizzeremo l'ultima configurazione valida nota laddove possibile ("fail stale") e, qualora non fosse possibile, abbiamo analizzato ogni caso di guasto implementando le modalità "fail open" o "fail close", a seconda che sia preferibile servire il traffico con funzionalità ridotte piuttosto che interromperlo del tutto.

Esaminiamo un esempio di come funziona. Il disservizio di novembre 2025 è stato innescato da un errore nell'implementazione del nostro classificatore di machine learning per il rilevamento Bot Management. In base alle nostre nuove procedure, se fossero stati generati nuovamente dei dati non leggibili dal nostro sistema, il sistema si sarebbe rifiutato di utilizzare la nuova configurazione e avrebbe utilizzato la configurazione precedente. Se la configurazione precedente non fosse disponibile per qualsiasi motivo, il sistema andrebbe in fail open, in modo da garantire che il traffico di produzione dei clienti continui ad essere servito, un esito decisamente migliore rispetto ai tempi di inattività.

Di conseguenza, se ora venisse applicato lo stesso aggiornamento di Bot Management che ha causato l'interruzione del servizio a novembre, il sistema rileverebbe il problema già nella fase iniziale della distribuzione, prima che abbia interessato più di una piccola percentuale di traffico.

Abbiamo inoltre iniziato a segmentare ulteriormente il nostro sistema in modo che le copie indipendenti dei servizi vengano eseguite per gruppi diversi di traffico. Cloudflare già oggi utilizza queste coorti di clienti per la mitigazione dell'impatto dei guasti con tecniche di gestione del traffico, e questo ulteriore lavoro di segmentazione dei processi ci fornisce una potente capacità di affidabilità per il futuro. 

Ad esempio, il sistema di runtime di Workers è suddiviso in più servizi indipendenti che gestiscono diversi gruppi di traffico, con uno che gestisce solo il traffico per i nostri clienti con un piano gratuito. Le modifiche vengono distribuite in questi segmenti sulla base delle coorti di clienti, a partire dai clienti con un piano gratuito. Stiamo inoltre inviando aggiornamenti più rapidi e frequenti ai segmenti meno critici e a un ritmo più lento ai segmenti più critici.

Di conseguenza, se una modifica venisse distribuita nel runtime di Workers e interrompesse il traffico, ora riguarderebbe solo una piccola percentuale dei nostri clienti con un piano gratuito prima di essere rilevata automaticamente e interrotta.

Prendendo ad esempio il runtime del sistema Workers, in sette giorni all'inizio del mese, il processo di distribuzione è stato attivato più di 50 volte. Puoi vedere come ciascuna di esse avvenga a "ondate" quando la modifica si propaga fino all'edge, spesso in parallelo rispetto ai rilasci precedenti e successivi:

Siamo impegnati a estendere questo modello di distribuzione a molti altri dei nostri sistemi in futuro.

### Procedure di emergenza e gestione degli incidenti aggiornate

 _**Cosa significa per te** : se si verificasse un incidente, disponiamo degli strumenti e dei team necessari per comunicare in modo più chiaro e per risolverlo più rapidamente, riducendo al minimo i tempi di inattività._

Cloudflare viene eseguita su Cloudflare. Utilizziamo i nostri prodotti Zero Trust per proteggere la nostra infrastruttura, ma questo crea una dipendenza: se un'interruzione a livello di rete influisce su questi strumenti, perdiamo proprio i percorsi di cui abbiamo bisogno per risolverli. Prima di questa iniziativa Code Orange, i nostri percorsi di emergenza erano limitati a un numero limitato di persone e offrivano un accesso limitato agli strumenti. Abbiamo bisogno che questi strumenti e questi percorsi siano più ampiamente disponibili durante un’interruzione.

Per risolvere questo problema, abbiamo eseguito una valutazione completa degli strumenti essenziali per la visibilità, il debug e le modifiche alla produzione nei sistemi. Abbiamo infine sviluppato percorsi di autorizzazione di backup per 18 servizi chiave, supportati da nuovi script e proxy di emergenza.

Durante il programma Code Orange, siamo passati dalla teoria alla pratica. Dopo esercitazioni di team di piccole dimensioni, abbiamo condotto una simulazione a livello di ingegneria il 7 aprile 2026, coinvolgendo oltre 200 membri del team. Sebbene l'automazione mantenga funzionali questi percorsi, esercitazioni come queste garantiscono che i nostri ingegneri abbiano gli automatismi necessari per utilizzarli sotto pressione.

Questo impegno si concentrava anche sul flusso di informazioni. Quando la visibilità interna è interrotta, la nostra risposta agli incidenti rallenta e la nostra capacità di comunicare con il mondo esterno ne risente. Storicamente, le osservazioni tecniche a caldo non si sono tradotte sempre in aggiornamenti chiari per i nostri clienti.

Per colmare questo divario, abbiamo istituito un team di comunicazione dedicato per lavorare a stretto coordinamento con i team di risposta agli incidenti durante gli eventi più importanti. Proprio come i nostri ingegneri hanno esercitato le proprie procedure di emergenza, questo team ha utilizzato il programma Code Orange per esercitarsi nella semplificazione della cadenza e della chiarezza degli aggiornamenti per i clienti. Grazie alla garanzia di avere sia gli strumenti per monitorare che la struttura per comunicare, possiamo risolvere gli incidenti più rapidamente e informare meglio i nostri clienti.

### Abbiamo codificato i nostri miglioramenti

 _**Cosa significa per te** : ricorderemo gli insegnamenti dei nostri incidenti e abbiamo codificato le risoluzioni. La nostra rete diventerà solo più resiliente._

Per evitare deviazioni e reintrodurre regressioni al lavoro svolto nel contesto dell'iniziativa Code Orange nel tempo, il team ha creato un Codex interno che consolida tutte le nostre linee guida in regole chiare e concise.

Il Codex è ora obbligatorio per tutti i team di ingegneri e prodotto ed è diventato una parte centrale delle procedure interne di Cloudflare. Le regole sono applicate tramite revisioni del codice basate sull'IA che evidenziano automaticamente qualsiasi istanza che potrebbe divergere dalle linee guida, richiedendo ulteriori revisioni manuali. Questo viene applicato senza eccezioni all'intera base di codice. L'obiettivo è semplice: creare una memoria istituzionale che si applichi da sé.

I problemi di novembre e dicembre hanno condiviso una modalità di guasto comune: il codice presupponeva che gli input sarebbero sempre stati validi, senza un ripristino funzionale quando tale ipotesi veniva meno. Un servizio Rust ha chiamato `.unwrap()` invece di gestire un errore; il codice Lua ha indicizzato un oggetto inesistente. Entrambi i modelli possono essere evitati se le lezioni vengono apprese e applicate.

Codex è parte della nostra risposta. Si tratta di un repository vivente di standard ingegneristici redatto da esperti del settore tramite il nostro processo RFC (Request For Comments), poi distillato in regole pratiche. Le best practice che in precedenza risiedevano nella mente degli ingegneri senior o che venivano scoperte solo dopo un incidente, ora sono una conoscenza condivisa accessibile a tutti. Ogni regola segue un formato semplice: "Se hai bisogno di X, usa Y" con un link alla RFC che spiega perché.

Ad esempio, ora una RFC afferma: "Non utilizzare `.unwrap()` al di fuori dei test e di `build.rs.`" Un altro principio più ampio afferma: "I servizi DEVONO verificare che le dipendenze a monte siano nel loro stato previsto prima dell'elaborazione".

Se queste regole fossero state applicate in precedenza, le interruzioni di novembre e dicembre sarebbero state merge request rifiutate anziché incidenti globali.

Le regole non applicate diventano semplici suggerimenti. Il Codex si integra con agenti basati sull'IA in ogni fase del ciclo di vita dello sviluppo del software (dalla revisione del progetto alla distribuzione e all'analisi degli incidenti). Questo anticipa l'applicazione delle regole a monte (shift-left), da "interruzione globale" a "merge request rifiutata". Il raggio d'azione di una violazione si riduce da milioni di richieste interessate a un unico sviluppatore che riceve un feedback fruibile prima che il suo codice raggiunga la produzione.

Il Codex è un documento in costante evoluzione e sarà continuamente perfezionato nel tempo. Gli esperti di dominio scrivono le RFC per codificare le best practice. Gli incidenti segnalano lacune che diventeranno nuove RFC. Ogni RFC approvata genera regole Codex. Queste regole alimentano gli agenti che rivedranno la merge request successiva. È come un volano: la conoscenza diventa uno standard, lo standard diventa un'applicazione concreta, e l'applicazione concreta innalza il livello qualitativo di base per tutti.

### Non si tratta solo di codice: la comunicazione è fondamentale

 _**Cosa significa per te** : la trasparenza è importante per noi. Se qualcosa va storto, ci impegniamo a inviare aggiornamenti continui in ogni fase del processo, in modo che tu possa concentrarti su ciò che conta per te._

I disservizi a livello globale ci hanno spinto a rivedere i nostri processi principali e i nostri approcci culturali anche al di là dell'ingegneria e dello sviluppo di prodotti. Nell'ambito delle più ampie iniziative Code Orange, abbiamo introdotto ulteriori obiettivi di livello di servizio (SLO) per tutti i nostri servizi, imposto un changelog globale, incorporato tutti i team nel nostro sistema di coordinamento della manutenzione e migliorato la trasparenza all'interno dell'azienda per eliminare il backlog dei ticket di "prevenzione" degli incidenti. 

Abbiamo anche migliorato il modo in cui comunichiamo con i nostri clienti durante un'interruzione. Il nostro obiettivo è avvisarti di un problema nel momento in cui lo confermiamo, prima ancora che tu te ne accorga. Al momento della notifica di un ritardo o di un errore, il nostro obiettivo è avere già un aggiornamento in attesa nelle tue notifiche.

Durante un incidente attivo, ora forniamo aggiornamenti a intervalli prevedibili (ad esempio, ogni 30 o 60 minuti), anche se l'aggiornamento consiste semplicemente in "Stiamo ancora testando la correzione. Nessuna nuova modifica per ora". Questo ti consente di organizzare la tua giornata invece di aggiornare costantemente una pagina dello stato.

Il nostro lavoro non termina quando si ripristina il normale stato operativo. Forniamo dei post mortem dettagliati in cui illustriamo cosa e perché è accaduto e, infine, quali cambiamenti strutturali attuiamo per evitare che si ripeta nuovamente.

### Questa iniziativa è stata completata. Ma il nostro lavoro sulla resilienza non si arresta mai.

Prendiamo questi incidenti molto sul serio e attuiamo una responsabilità condivisa in tutta l'organizzazione di Cloudflare ponendo a ogni team la stessa domanda: cosa si sarebbe potuto fare meglio? Questo ha guidato il lavoro che abbiamo svolto negli ultimi due trimestri.

Anche se questo lavoro non sarà mai davvero concluso, siamo certi di essere in una posizione ben superiore e che Cloudflare sia ora molto più forte per questo.

]]>6EfXlJEx6OJ21w9NlnS59DCostruire il cloud degli agenti: tutto ciò che abbiamo lanciato durante la Agents Week 2026https://blog.cloudflare.com/it-it/agents-week-in-review/ Mon, 20 Apr 2026 13:00:00 GMTAgents Week 2026 si è conclusa. Diamo un'occhiata a tutto quello che abbiamo annunciato, dalle risorse di elaborazione e sicurezza alla toolbox per gli agenti, agli strumenti per le piattaforme e al web agentico emergente. Tutto ciò che abbiamo introdotto per il cloud agentico. AgentiAgents WeekAPIBrowser RunCloudflare AccessCloudflare GatewayCloudflare WorkersDurable ObjectsIALLMMCPNovità sul prodottoPiattaforma per sviluppatoriRendering del browserSandboxSDKSviluppatoriWorkers AIOggi si conclude la nostra prima Agents Week, una settimana dell'innovazione dedicata interamente all'era degli agenti. Non avrebbe potuto essere più in linea con i tempi: nell'ultimo anno, gli agenti hanno rapidamente cambiato le modalità di lavoro delle persone. Gli agenti di codifica stanno aiutando gli sviluppatori a rilasciare/distribuire in tempi più rapidi che mai. Gli agenti di supporto risolvono i ticket end-to-end. Gli agenti di ricerca convalidano le ipotesi su centinaia di fonti in pochi minuti. E le persone non gestiscono solo un agente: ne eseguono diversi in parallelo e 24 ore su 24.

Come hanno notato il CTO di Cloudflare Dane Knecht e il VP of Product Rita Kozlov nel nostro [post di benvenuto alla Agents Week](https://blog.cloudflare.com/welcome-to-agents-week/), la scala potenziale degli agenti è sbalorditiva: se anche solo una piccola parte dei knowledge worker di tutto il mondo eseguono alcuni agenti in parallelo, è necessaria capacità di elaborazione per decine di milioni di sessioni simultanee. Il modello one-app-serve-many-users su cui è basato il cloud da sempre non funziona più in questo nuovo scenario. Ma questo è esattamente ciò che gli sviluppatori e le aziende vogliono fare: creare agenti, distribuirli agli utenti ed eseguirli su larga scala.

Arrivarci significa risolvere i problemi dell'intero stack. Gli agenti hanno bisogno di **elaborazione** in grado di scalare da sistemi operativi completi a isolati leggeri. Hanno bisogno di **sicurezza** e identità integrate nel modo in cui vengono eseguite. Hanno bisogno di una **toolbox per gli agenti** : i modelli, gli strumenti e il contesto giusti per svolgere un lavoro reale. Tutto il codice generato dagli agenti ha bisogno di un percorso chiaro **dal prototipo del alla produzione**. E infine, poiché gli agenti guidano una quota crescente del traffico Internet, il web stesso deve adattarsi al **web agentico** emergente. Abbiamo scoperto che la piattaforma di elaborazione containerless e serverless che abbiamo lanciato otto anni fa con Workers era pronta per questo momento. Da allora, l'abbiamo trasformata in una piattaforma completa e questa settimana abbiamo lanciato la prossima ondata di primitive create appositamente per gli agenti, organizzate esattamente per risolvere questi problemi.

Siamo qui per creare il Cloud 2.0: il cloud agentico. Un'infrastruttura progettata per un mondo in cui gli agenti sono un carico di lavoro primario. 

Ecco un elenco di tutto ciò che abbiamo annunciato questa settimana: non vorremmo che ti perdessi nulla.

## Elaborazione

Inizia con l'elaborazione. Gli agenti hanno bisogno di un luogo in cui eseguire, archiviare ed eseguire il codice che scrivono. Non tutti gli agenti hanno bisogno della stessa cosa: alcuni richiedono un sistema operativo completo per installare pacchetti ed eseguire comandi del terminale, la maggior parte ha bisogno di qualcosa di leggero che si avvii in pochi millisecondi e scali nell'ordine di milioni. Questa settimana abbiamo fornito gli ambienti per eseguirli, oltre a un nuovo spazio di lavoro compatibile con Git per gli agenti:

Annuncio| Riepilogo  
---|---  
Artifacts: archiviazione con versione compatibile con Git| Offri ai tuoi agenti, sviluppatori e automazioni uno spazio dedicato per codice e dati. Abbiamo appena lanciato Artifacts: archiviazione con versione compatibile con Git, creato per gli agenti. Crea decine di milioni di repository, effettua il fork da qualsiasi repository remoto e fornisci un URL a qualsiasi client Git.  
Gli agenti hanno i propri computer con Sandboxes disponibile al pubblico| Cloudflare Sandboxes offre agli agenti IA un ambiente persistente e isolato: un computer reale con una shell, un filesystem e processi in background che si avvia su richiesta e riprende esattamente da dove era stato interrotto.  
Dinamici, consapevoli dell'identità e sicuri: controlli in uscita per le sandbox| Gli Outbound Workers per le sandbox forniscono un proxy di uscita Zero Trust programmabile per gli agenti IA. Questo proxy consente agli sviluppatori di inserire credenziali e applicare criteri di sicurezza dinamiche senza esporre i token sensibili a codice non attendibile.  
Durable Objects in Dynamic Workers: assegna a ogni app generata dall'IA un proprio database| Durable Object Facets consente a Dynamic Workers di creare istanze di Durable Objects con i propri database SQLite isolati. Questo consente agli sviluppatori di creare piattaforme che eseguono codice persistente e stateful generato al volo.  
Riprogettare il piano di controllo di Workflows per l'era agentica| Cloudflare Workflows, un motore di esecuzione robusto per applicazioni a più fasi, ora supporta 50.000 limiti di simultaneità e 300 di velocità di creazione più elevati grazie a un piano di controllo riprogettato, contribuendo a scalare per soddisfare i casi d'uso degli agenti in background robusti.  
  
## Sicurezza

L'esecuzione degli agenti e del loro codice è solo metà della sfida. Gli agenti si connettono a reti private, accedono ai servizi interni e intraprendono azioni autonome per conto degli utenti. Quando chiunque in un'organizzazione può creare i propri agenti, la sicurezza non può essere un ripensamento. Deve essere l'impostazione predefinita. Questa settimana abbiamo lanciato gli strumenti per semplificare tutto questo.

Annuncio| Riepilogo  
---|---  
Rete privata sicura per tutti: utenti, nodi, agenti, Workers: presentazione di Cloudflare Mesh| Cloudflare Mesh fornisce un accesso sicuro e privato alla rete per utenti, nodi e agenti IA autonomi. Integrandosi con Workers VPC, gli sviluppatori possono ora concedere agli agenti l'accesso con ambito a database e API privati senza tunnel manuali.  
OAuth gestita per Access: rendi le app interne pronte per gli agenti con un semplice clic| L'autenticazione OAuth gestita per Cloudflare Access consente agli agenti IA di navigare in modo sicuro nelle applicazioni interne. Adottando la RFC 9728, gli agenti possono autenticarsi per conto degli utenti senza utilizzare account di servizio non sicuri.  
Proteggere le identità non umane: revoca automatica, OAuth e autorizzazioni con ambito limitato| Cloudflare introduce i token API scansionabili, una maggiore visibilità per OAuth e la disponibilità generale (GA) per le autorizzazioni a livello di risorsa. Questi strumenti aiutano gli sviluppatori a implementare una vera architettura a privilegi minimi, proteggendoli al contempo dalla fuga di credenziali.  
Adozione su larga scala di MCP: la nostra architettura di riferimento per le distribuzioni aziendali di MCP| Condividiamo la strategia interna di Cloudflare per la gestione di MCP tramite Access, AI Gateway e i portali del server MCP. Inoltre, lanciamo la modalità codice per ridurre drasticamente i costi dei token e raccomandiamo nuove regole per il rilevamento di Shadow MCP in Cloudflare Gateway.  
  
## Toolbox per gli agenti

Un agente capace deve essere in grado di pensare e ricordare, comunicare e vedere. Questo richiede che sia basato sui modelli giusti, con accesso agli strumenti giusti e al contesto giusto per svolgere le proprie attività al meglio. Questa settimana abbiamo distribuito le primitive (inferenza, ricerca, memoria, voce, e-mail e un browser) che trasformano un agente in qualcosa che funziona davvero.

Annuncio| Riepilogo  
---|---  
Project Think: creare la nuova generazione di agenti IA su Cloudflare| Annunciamo un'anteprima della prossima edizione di Agents SDK, dalle primitive leggere a una piattaforma dotata di batterie per agenti IA che pensano, agiscono e persistono.  
Aggiungere la voce al tuo agente| Una pipeline vocale sperimentale per l'SDK Agents consente interazioni vocali in tempo reale tramite WebSockets. Gli sviluppatori possono ora creare agenti con STT e TTS continui in sole 30 righe di codice lato server.  
Cloudflare Email Service è ora in versione beta pubblica. Pronto per i tuoi agenti| Gli agenti stanno diventando multicanale. Ciò significa renderli disponibili ovunque si trovino già i tuoi utenti, inclusa la casella di posta elettronica. Cloudflare Email Service entra nella versione beta pubblica con il livello infrastrutturale per semplificare il processo: inviare, ricevere ed elaborare email in modo nativo dai tuoi agenti.  
La piattaforma IA di Cloudflare: un livello di inferenza progettato per gli agenti | Stiamo integrando Cloudflare in un livello di inferenza unificato per gli agenti, consentendo agli sviluppatori di richiamare modelli da oltre 14 provider. Tra le nuove funzionalità figurano il binding Workers per l'esecuzione di modelli di terzi e un catalogo ampliato con modelli multimodali.  
Costruire le basi per l'esecuzione di modelli linguistici di dimensioni extra-large| Abbiamo creato uno stack tecnologico personalizzato per eseguire LLM e ad alta velocità sull'infrastruttura di Cloudflare. Questo articolo esplora i compromessi ingegneristici e le ottimizzazioni tecniche necessarie per rendere accessibile l'inferenza IA ad alte prestazioni.  
Unweight: come abbiamo compresso un LLM del 22% senza sacrificare la qualità| L'esecuzione di LLM sulla rete di Cloudflare richiede un utilizzo più smart ed efficiente della larghezza di banda della memoria GPU. Per questo motivo, abbiamo sviluppato Unweight, un sistema di compressione senza perdite per il tempo di inferenza che riduce il footprint del modello di fino al 22%, in modo da offrire inferenze più rapide ed economiche che mai.   
Agenti che ricordano: presentazione di Agent Memory| Cloudflare Agent Memory è un servizio gestito che fornisce agli agenti IA una memoria persistente, consentendo loro di ricordare ciò che conta, dimenticare quello che non conta e diventare più smart nel tempo.  
AI Search: la primitiva di ricerca per i tuoi agenti| AI Search è la primitiva di ricerca per i tuoi agenti. Crea istanze in modo dinamico, carica file ed effettua ricerche tra le istanze con recupero ibrido e miglioramento della pertinenza. È sufficiente creare un'istanza di ricerca, caricare i dati ed eseguire la ricerca.  
Browser Run: fornisci un browser ai tuoi agenti| Il rendering del browser è ora Browser Run, con Live View, Human in the Loop, accesso a CDP, registrazione delle sessioni e limiti di simultaneità quattro volte superiori per gli agenti IA.  
  
## Prototipo alla produzione

Per essere considerata tra le migliori, un'infrastruttura deve essere anche facile da usare. Vogliamo incontrare gli sviluppatori e i loro agenti dove stanno già lavorando: nel terminale, nell'editor, in un prompt e rendere accessibile l'intera piattaforma Cloudflare senza cambio di contesto.

Annuncio| Riepilogo  
---|---  
Creazione di una CLI per tutto Cloudflare| Stiamo introducendo cf, una nuova CLI unificata progettata per la coerenza su tutta la piattaforma Cloudflare, insieme a Local Explorer per il debug dei dati locali. Questi strumenti semplificano il modo in cui gli sviluppatori e gli agenti IA interagiscono con le nostre quasi 3.000 operazioni API.  
Ti presentiamo Agent Lee: una nuova interfaccia allo stack di Cloudflare| Agent Lee è un agente all'interno del dashboard che sposta l'interfaccia di Cloudflare dal passaggio manuale tra le schede a un singolo prompt. Utilizzando TypeScript in ambiente sandbox, ti aiuta a risolvere i problemi e a gestire il tuo stack come un collaboratore tecnico con i piedi per terra.  
Presentazione di Flagship: i flag di funzionalità pensati per l'era dell'IA.| Presentazione di Flagship, un servizio di flag di funzionalità nativo basato sulla rete globale di Cloudflare per eliminare la latenza dei provider di terzi. Grazie all'utilizzo di KV e Durable Objects, Flagship consente una valutazione dei flag in frazioni di millisecondo.  
Distribuire database PostgreSQL e MySQL con PlanetScale + Workers| Scopri come distribuire i database Postgres e MySQL PlanetScale tramite Cloudflare e connettere Cloudflare Workers.  
Registrare i domini ovunque si costruisce: l'API di Cloudflare Registrar è ora in versione beta| L'API di Cloudflare Registrar è ora in versione beta. Gli sviluppatori e gli agenti IA possono cercare, verificare la disponibilità e registrare domini con prezzi al costo direttamente dal loro editor, dal loro terminale o dal loro agente, senza interrompere il flusso di lavoro.  
  
## Web agentico

Man mano che sempre più agenti si collegano online, continuano a navigare su Internet, uno strumento creato per le persone. I siti web esistenti necessitano di nuovi strumenti per controllare a quali contenuti i bot possono accedere, per organizzarli e presentarli agli agenti, e per misurare quanto sono pronti per questo cambiamento.

Annuncio| Riepilogo  
---|---  
Introduzione del punteggio di predisposizione agli agenti. Il tuo sito è predisposto agli agenti?| Il punteggio di predisposizione agli agenti può aiutare i proprietari di siti web a capire l'efficienza con cui i loro siti supportano gli agenti IA. Qui esploriamo nuovi standard, condividiamo i dati di Radar e spieghiamo in dettaglio come abbiamo reso la documentazione di Cloudflare la più intuitiva per gli agenti sul web.  
I reindirizzamenti per l'addestramento dell'IA rafforzano i contenuti canonici| Le direttive non restrittive non impediscono ai crawler di acquisire contenuti obsoleti. Redirects for AI Training consente a chiunque utilizzi Cloudflare di reindirizzare i crawler verificati alle pagine canoniche con un semplice clic e senza modificare l'origine del sito.  
Agents Week: Aggiornamento delle prestazioni di rete| Migrando il nostro livello di gestione delle richieste a un'architettura basata su Rust chiamata FL2, Cloudflare ha aumentato il suo vantaggio in termini di performance al 60% delle principali reti del mondo. Utilizziamo misurazioni degli utenti reali e trimean delle connessioni TCP per garantire che i nostri dati riflettano l'esperienza effettiva delle persone su Internet.  
Compressione dei dizionari condivisi al passo con il web agentico| Ti diamo un'anteprima del nostro supporto per i dizionari di compressione condivisi, ti mostriamo come migliorano i tempi di caricamento delle pagine e ti riveliamo quando potrai provare la versione beta.  
  
## Un riepilogo

La Agents Week 2026 sta terminando, ma il cloud agentico è solo all'inizio. Tutto ciò che abbiamo mostrato questa settimana, dall'elaborazione e dalla sicurezza agli strumenti per agenti e al web agentico, è la base. Continueremo a basarci su questo per darti tutto ciò di cui hai bisogno per realizzare quello che verrà dopo.

Abbiamo anche altri post sul blog in uscita oggi e domani con ulteriori approfondimenti, quindi tieni d'occhio le ultime novità [sul nostro blog](https://blog.cloudflare.com/).

Se ti stai basando su ciò che abbiamo annunciato questa settimana, ti chiediamo di farcelo sapere. Vieni a trovarci su [X](https://x.com/cloudflaredev) o [Discord](https://discord.com/invite/cloudflaredev), oppure consulta la [documentazione per gli sviluppatori](https://developers.cloudflare.com/products/?product-group=Developer+platform). 

]]>25CSwW9eXDM4FJOdVPLf8fIntroduzione del punteggio di predisposizione agli agenti. Il tuo sito è predisposto agli agenti?https://blog.cloudflare.com/it-it/agent-readiness/ Fri, 17 Apr 2026 13:05:00 GMTIl punteggio di predisposizione agli agenti può aiutare i proprietari di siti web a capire l'efficienza con cui i loro siti supportano gli agenti IA. Qui esploriamo nuovi standard, condividiamo i dati di Radar e spieghiamo in dettaglio come abbiamo reso la documentazione di Cloudflare la più intuitiva per gli agenti sul web.AgentiAgents WeekDocumentazione per gli sviluppatoriIAPredisposizione agli agentiRadarIl web ha sempre dovuto adattarsi a nuovi standard. Iniziò a usare il linguaggio dei browser web e poi a comunicare con i motori di ricerca. Oggi, deve essere in grado di parlare con gli agenti IA.

Oggi siamo lieti di presentare [isitagentready.com](https://isitagentready.com/), un nuovo strumento pensato per aiutare i proprietari di siti web a capire come ottimizzare i propri siti per gli agenti, da come guidarli durante l'autenticazione, fino al controllo dei contenuti a cui hanno accesso, del formato di ricezione di questi contenuti e del loro pagamento. Stiamo [introducendo anche un nuovo set di dati in Cloudflare Radar](https://radar.cloudflare.com/ai-insights#adoption-of-ai-agent-standards), che tiene traccia dell'adozione complessiva di ogni standard per gli agenti su Internet.

Vogliamo dare l'esempio. È per questo che condividiamo come abbiamo recentemente rinnovato la [documentazione per sviluppatori](https://developers.cloudflare.com/) di Cloudflare per renderla il sito di documentazione più "agent-friendly", consentendo agli strumenti IA di rispondere alle domande in modo più rapido e a costi significativamente più contenuti.

## Quanto è predisposto oggi il web agli agenti?

La risposta breve: non molto. La risposta non sorprende più di tanto, ma di fatto sottolinea anche quanto possano essere più efficaci gli agenti rispetto a oggi, se si adotteranno degli standard.

Per analizzare questo, Cloudflare Radar ha considerato i 200.000 [domini più visitati](https://radar.cloudflare.com/domains) su Internet, filtrato le categorie in cui la predisposizione agli agenti non è importante (come i reindirizzamenti, i server pubblicitari e i servizi di tunneling) per concentrarsi su aziende, editori e piattaforme con cui gli agenti IA potrebbero realisticamente aver bisogno di interagire e li ha esaminati utilizzando il nostro nuovo strumento.

Il risultato è un nuovo grafico "Adozione degli standard per gli agenti IA", ora disponibile nella pagina [Cloudflare Radar AI Insights](https://radar.cloudflare.com/ai-insights#adoption-of-ai-agent-standards), in cui possiamo misurare l'adozione di ogni standard in più categorie di dominio.

Esaminando i singoli test, alcune informazioni sono saltate all'occhio:

  * Il file [robots.txt](https://www.cloudflare.com/learning/bots/what-is-robots-txt/) è quasi universale (il 78% dei siti ne ha uno), ma la stragrande maggioranza è scritta per i crawler dei motori di ricerca tradizionali, non per gli agenti IA.
  * [Segnali di contenuti](https://contentsignals.org/): il 4% dei siti ha dichiarato le preferenze relative all'utilizzo dell'AI in robots.txt. Questo è un nuovo standard che sta guadagnando slancio.
  * La negoziazione di contenuti markdown (servire text/markdown su Accept: text/markdown) ha successo sul 3,9% dei siti.
  * I nuovi standard emergenti, come [schede server MCP](https://modelcontextprotocol.io/community/server-card/charter) e [cataloghi di API (RFC 9727)](https://datatracker.ietf.org/doc/rfc9727/), compaiono insieme in meno di 15 siti nell'intero set di dati. E ancora presto: ci sono molte opportunità per distinguersi facendo parte dei primi siti ad adottare nuovi standard e a utilizzare al meglio gli agenti. 



Questo grafico verrà aggiornato settimanalmente e i dati possono essere consultati anche tramite il [Data Explorer](https://radar.cloudflare.com/explorer) o l'[API Radar](https://developers.cloudflare.com/api/resources/radar/).

## Ottieni un punteggio di predisposizione per il tuo sito

Puoi ottenere un punteggio di predisposizione agli agenti per il tuo sito web visitando [isitagentready.com](https://isitagentready.com/) e inserendo l'URL del sito.

Punteggi e audit che forniscono feedback pratico hanno contribuito a promuovere l'adozione di nuovi standard in passato. Ad esempio, [Google Lighthouse](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring) assegna un punteggio ai siti web in base alle best practice di performance e sicurezza e guida i proprietari dei siti ad adottare i più recenti standard delle piattaforme web. Pensiamo che dovrebbe esistere qualcosa di simile per aiutare i proprietari dei siti ad adottare le best practice per gli agenti.

Quando Cloudflare analizza il tuo sito, invia ad esso delle richieste per verificare quali standard supporta e assegna un punteggio in base a quattro dimensioni:

  * Rilevabilità: [robots.txt](https://datatracker.ietf.org/doc/html/rfc9309), [sitemap.xml](https://www.sitemaps.org/protocol.html), [Intestazioni dei link (RFC 8288)](https://datatracker.ietf.org/doc/html/rfc8288)
  * Contenuti: [markdown per gli agenti](https://blog.cloudflare.com/markdown-for-agents/)
  * Controllo degli accessi bot: [Segnali dei contenuti](https://contentsignals.org/), [regole dei bot IA tramite robots.txt](https://developers.cloudflare.com/ai-crawl-control/), [autenticazione bot web](https://datatracker.ietf.org/doc/draft-meunier-web-bot-auth-architecture/)
  * Funzionalità: competenze degli agenti, catalogo delle API [(RFC 9727)](https://www.rfc-editor.org/rfc/rfc9727), rilevamento dei server OAuth tramite [RFC 8414](https://www.rfc-editor.org/rfc/rfc8414) e [RFC 9728](https://datatracker.ietf.org/doc/html/rfc9728), [scheda server MCP](https://modelcontextprotocol.io/community/server-card/charter) e [WebMCP](https://developer.chrome.com/blog/webmcp-epp)



 _Screenshot dei risultati di un controllo di predisposizione agli agenti per un sito web di esempio._

Inoltre, controlliamo se il sito supporta gli standard di commercio agentico, inclusi [x402](https://www.x402.org/), [Universal Commerce Protocol](https://ucp.dev/) e [Agentic Commerce Protocol](https://www.agenticcommerce.dev/), ma al momento questi non incidono sul punteggio.

Per ogni controllo non superato, forniamo un prompt che puoi dare al tuo agente di codifica facendogli implementare il supporto per tuo conto.

Il sito stesso è anche predisposto per gli agenti, mettendo in pratica ciò che predica. Espone un server MCP stateless (https://isitagentready.com/.well-known/mcp.json) con uno strumento `scan_site` tramite Streamable HTTP, in modo che qualsiasi agente compatibile con MCP possa scansionare i siti web in modo programmatico senza utilizzare l'interfaccia web. Pubblica inoltre un indice delle competenze degli agenti (https://isitagentready.com/.well-known/agent-skills/index.json) con documenti di competenze per ogni standard che verifica, in modo che gli agenti sappiano non solo cosa correggere, ma anche come farlo.

Esaminiamo i controlli in ogni categoria e perché sono importanti per gli agenti.

### Reperibilità

[robots.txt](https://www.cloudflare.com/learning/bots/what-is-robots-txt/) esiste dal 1994 e la maggior parte dei siti ne ha uno. Ha due scopi per gli agenti: definisce le regole di crawling (chi può accedere a cosa) e fa riferimento alle tue sitemap. Una sitemap è un file XML che elenca tutti i percorsi sul tuo sito web, essenzialmente una mappa che gli agenti possono seguire per scoprire tutti i tuoi contenuti senza dover eseguire la scansione di ogni link. Il file robots.txt è il primo che gli agenti consultano.

Oltre alle sitemap, gli agenti possono anche rilevare risorse importanti direttamente dalle intestazioni delle risposte HTTP, in particolare utilizzando l'intestazione Link delle risposte ([RFC 8288](https://www.rfc-editor.org/rfc/rfc8288)). A differenza dei link nascosti nell'HTML, l'intestazione Link fa parte della risposta HTTP stessa, il che significa che un agente può trovare link alle risorse senza dover analizzare alcun markup:

### Accessibilità dei contenuti

Ottenere un agente sul tuo sito è un conto. Assicurarsi che sia effettivamente in grado di leggere il tuo contenuto è un altro.

Nel settembre 2024, che sembrano secoli fa data la velocità con cui si muove l'IA, è stato proposto [llms.txt](http://llms.txt) come un modo per fornire una rappresentazione di un sito web compatibile con LLM e per adattarsi alla finestra di contesto del modello. [llms.txt](https://llmstxt.org/) è un file di testo semplice alla radice del tuo sito che offre agli agenti un elenco di lettura strutturato: cos'è il sito, cosa contiene e dove si trova il contenuto importante. È come se fosse una sitemap scritta per essere letta da un LLM invece che da un crawler per l'indicizzazione:

La [negoziazione dei contenuti markdown](https://blog.cloudflare.com/markdown-for-agents/) va anche oltre. Quando un agente richiama una qualsiasi pagina e invia un'intestazione `Accept: text/markdown`, il server restituisce una versione di markdown pulita, anziché in html. La versione markdown richiede molti meno token (abbiamo misurato fino all'80% di riduzione dei token in alcuni casi) il che rende le risposte più veloci, più economiche e più probabilmente fruite nella loro interezza, dati i limiti delle finestre di contesto che la maggior parte degli strumenti degli agenti presenta per impostazione predefinita.

Per impostazione predefinita, controlliamo solo se il sito gestisce correttamente la negoziazione dei contenuti markdown e non cerchiamo il file llms.txt. Puoi personalizzare la scansione per includere il file llms.txt, se lo desideri.

### Controllo degli accessi bot

Ora che gli agenti possono navigare nel tuo sito e consultare i tuoi contenuti, la prossima domanda da porsi è la seguente: vuoi permettere a qualsiasi bot di farlo?

`robots.txt` fa molto di più che fare riferimento alle sitemap. È anche il posto in cui si definiscono le regole di accesso. Puoi dichiarare in modo esplicito quali crawler sono consentiti e a quali contenuti possono accedere, fino ai percorsi specifici. La presenza del file bots.txt è diventato uno standard consolidato, che tutti i bot ben programmati verificano prima di iniziare a eseguire il crawling della risorsa di rete.

I [segnali di contenuti](https://contentsignals.org/) consentono di essere più specifici. Invece di limitarsi a consentire o bloccare, puoi dichiarare esattamente cosa può fare l'IA con i tuoi contenuti. Usando una direttiva `Content-Signal` nel tuo file `robots.txt`, puoi controllare in modo indipendente tre aspetti: se i contenuti possono essere utilizzati per l'addestramento dell'IA (`ai-train`), se possono essere utilizzati come input IA per l'inferenza e il grounding (`ai-input`), e se devono essere mostrati nei risultati di ricerca (`search`):

Inversamente, lo standard di bozza IETF [Web Bot Auth](https://blog.cloudflare.com/web-bot-auth/) consente ai bot di autenticarsi e ai siti web che ricevono richieste da bot di identificarli. Un bot firma le sue richieste HTTP e il sito ricevente verifica tali firme utilizzando le chiavi pubbliche pubblicate dal bot.

Tali chiavi pubbliche si trovano in un endpoint ben noto, `/.well-known/http-message-signatures-directory`, che controlliamo come parte della scansione.

Non tutti i siti hanno bisogno di questo tipo di implementazione. Se il tuo sito si limita a servire contenuti e non effettua richieste ad altri siti, non ne hai bisogno. Ma con l'aumento dei siti su Internet che gestiscono i propri agenti per fare richieste ad altri siti, riteniamo che questo aspetto diventerà sempre più importante nel tempo.

### Rilevamento del protocollo

Oltre al consumo passivo di contenuti, gli agenti possono anche interagire con il tuo sito direttamente chiamando API, richiamando strumenti e completando autonomamente le attività.

Se il tuo servizio ha una o più API pubbliche, il catalogo delle API ([RFC 9727](https://www.rfc-editor.org/rfc/rfc9727)) fornisce agli agenti un'unica posizione nota per rilevarle tutte. Ospitata su `/.well-known/api-catalog`, elenca le tue API e fornisce link alle loro specifiche, documentazione ed endpoint di stato, senza richiedere che gli agenti eseguano lo scraping del tuo portale per sviluppatori o leggano la tua documentazione.

Non possiamo parlare di agenti senza menzionare MCP. Il [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) è uno standard aperto che consente ai modelli IA di connettersi con origini dati e strumenti esterni. Invece di dover creare un'integrazione personalizzata per ogni strumento IA, crei un server MCP e qualsiasi agente compatibile può utilizzarlo.

Per aiutare gli agenti a trovare il tuo server MCP, puoi pubblicare una scheda server MCP (una proposta attualmente in [bozza](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1649)). Si tratta di un file JSON in `/.well-known/mcp/server-card.json` che descrive il server ancor prima che un agente si connetta: quali strumenti espone, come raggiungerlo e come autenticarlo. Un agente legge questo file e sa tutto ciò che gli serve per iniziare a usare il tuo server:

Gli agenti operano al meglio quando dispongono di [Agent Skill](https://agentskills.io/home), ovvero competenze che li aiutano a svolgere attività specifiche: ma come possono gli agenti scoprire quali abilità offre un sito? Abbiamo proposto che i siti possano rendere queste informazioni disponibili in [`.well-known/agent-skills/index.json`](https://github.com/cloudflare/agent-skills-discovery-rfc), un endpoint che indica all'agente quali competenze sono disponibili e dove trovarle. Potresti notare che lo standard `.well-known` ([RFC 8615](https://datatracker.ietf.org/doc/html/rfc8615)) viene utilizzato da molti altri standard di agenti e autorizzazioni: dobbiamo ringraziare Mark Nottingham di Cloudflare, autore dello standard, e altri collaboratori dello IETF.

Molti siti richiedono l'accesso. Questo rende difficile per gli umani concedere agli agenti la possibilità di accedere a questi siti per loro conto, ed è per questo motivo che alcuni hanno adottato l'approccio, discutibilmente insicuro, di concedere agli agenti l'accesso al browser web dell'utente, con la sua sessione attiva.

Esiste un modo migliore che consente agli utenti di concedere esplicitamente l'accesso: i siti che supportano l'autenticazione OAuth possono indicare agli agenti dove trovare il server di autorizzazione ([RFC 9728](https://datatracker.ietf.org/doc/html/rfc9728)), consentendo agli agenti di far passare gli utenti attraverso un flusso OAuth, in cui possono scegliere di concedere correttamente l'accesso all'agente. Annunciato alla Agents Week 2026, ora [Cloudflare Access supporta completamente questo flusso OAuth](https://blog.cloudflare.com/managed-oauth-for-access/) e abbiamo dimostrato come gli agenti, come OpenCode, possano usare questo standard per garantire il corretto funzionamento quando agli agenti vengono forniti URL protetti:

### Commercio

Gli agenti possono anche acquistare articoli per conto tuo, ma i pagamenti online sono stati pensati per le persone. Aggiungi al carrello, inserisci una carta di credito, fai clic su paga. Questo flusso si interrompe del tutto quando l'acquirente è un agente IA.

[x402](https://x402.org) risolve questo problema a livello di protocollo, ripristinando HTTP 402 Payment Required, un codice di stato che esiste nella specifica dal 1997 ma che non è mai stato ampiamente utilizzato. Il flusso è semplice: un agente richiede una risorsa, il server risponde con un 402 e un payload leggibile dalla macchina che descrive le condizioni di pagamento, l'agente paga e riprova. Cloudflare ha collaborato con Coinbase per lanciare la [x402 Foundation](https://blog.cloudflare.com/x402), la cui missione è favorire l'adozione di x402 come standard aperto per i pagamenti Internet.

Eseguiamo anche una verifica di [Universal Commerce Protocol](https://ucp.dev/) e [Agentic Commerce Protocol](https://www.agenticcommerce.dev/), i due protocolli emergenti per il commercio agentico progettati per consentire agli agenti virtuali di scoprire e acquistare prodotti che normalmente le persone acquisterebbero tramite flussi di finalizzazione degli ordini e una vetrina di e-commerce.

## Integrazione della predisposizione agli agenti nello URL Scanner di Cloudflare

Lo [URL Scanner di Cloudflare](https://radar.cloudflare.com/scan) ti consente di inviare qualsiasi URL e di ottenere un report dettagliato in merito: intestazioni HTTP, certificati TLS, record DNS, tecnologie utilizzate, dati sulle performance e segnali di sicurezza. È uno strumento fondamentale per i ricercatori e gli sviluppatori di sicurezza che vogliono capire cosa fa effettivamente un URL dietro le quinte.

Abbiamo ripreso gli stessi controlli da [isitagentready.com](https://isitagentready.com/) e li abbiamo aggiunti a URL Scanner con una nuova scheda Agent Readiness (Predisposizione agli agenti). Quando esegui la scansione di un URL, ora vedrai il suo report completo sulla predisposizione agli agenti insieme all'analisi esistente: quali controlli sono vengono superati, a che livello si trova il sito e indicazioni dettagliate per migliorare il tuo punteggio.

L'integrazione è disponibile anche a livello programmatico tramite l'[API URL Scanner](https://developers.cloudflare.com/api/resources/url_scanner/). Per includere i risultati relativi alla predisposizione agli agenti in una scansione, passa l'opzione agentReadiness nella richiesta di scansione:

## Guidare con l'esempio: upgrade di Cloudflare Docs

Poiché stavamo creando gli strumenti per misurare la predisposizione del web, sapevamo di dover prima di tutto assicurarci che la nostra infrastruttura fosse impeccabile. La nostra documentazione deve essere facilmente comprensibile per gli agenti utilizzati dai nostri clienti.

Abbiamo naturalmente adottato i suddetti standard di content site pertinenti e puoi dare un'occhiata al nostro punteggio [qui](https://isitagentready.com/developers.cloudflare.com?profile=content). Tuttavia, non ci siamo fermati qui. Ecco come abbiamo migliorato la [documentazione per gli sviluppatori](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/) di Cloudflare per trasformarla nella risorsa più agent-friendly disponibile sul web.

### Fallback degli URL che utilizzano i file `index.md`

Purtroppo, [a partire da febbraio 2026](https://www.checklyhq.com/blog/state-of-ai-agent-content-negotation/), sui sette agenti testati, solo Claude Code, OpenCode e Cursor richiedono contenuti con l'intestazione `Accept: text/markdown` per impostazione predefinita. Per gli altri, avevamo bisogno di un fallback basato su URL trasparente.

A tale scopo, rendiamo tutte le pagine disponibili separatamente tramite Markdown su `/index.md` rispetto all'URL della pagina. Lo facciamo in modo dinamico, senza duplicare i file statici, combinando due regole di Cloudflare: 

  * Una [regola di riscrittura URL](https://developers.cloudflare.com/rules/transform/url-rewrite/) corrisponde alle richieste che terminano con `/index.md` e le riscrive dinamicamente nel percorso di base utilizzando `regex_replace` (rimuovendo `/index.md`). 
  * Una [regola di trasformazione dell'intestazione della richiesta](https://developers.cloudflare.com/rules/transform/request-header-modification/) si applica al percorso della richiesta originale _prima_ della riscrittura (`raw.http.request.uri.path`) e imposta automaticamente l'intestazione `Accept: text/markdown`. 



Con queste due regole, qualsiasi pagina può essere recuperata come Markdown aggiungendo il percorso /index.md all'URL:

  * [https://developers.cloudflare.com/r2/get-started/index.md](https://developers.cloudflare.com/r2/get-started/index.md)



Indichiamo questi URL `/index.md` nei nostri file `llms.txt`. Effettivamente, per questi percorsi `/index.md`, restituiamo sempre markdown, indipendentemente dalle intestazioni impostate dal client. Lo facciamo senza alcun passaggio di creazione aggiuntivo o duplicazione di contenuti.

### Creare file `llms.txt` efficaci per siti di grandi dimensioni

`llms.txt` funge da "home base" per gli agenti, fornendo una directory di pagine per aiutare gli LLM a trovare i contenuti. Tuttavia, più di 5.000 pagine di documentazione in un unico file supereranno le finestre di contesto dei modelli.

Invece di un unico file, generiamo un file `llms.txt` separato per _ogni directory principale_ nella nostra documentazione e il file `llms.txt` principale fa semplicemente riferimento a queste sottodirectory.

  * [https://developers.cloudflare.com/llms.txt](https://developers.cloudflare.com/llms.txt)
  * [https://developers.cloudflare.com/r2/llms.txt](https://developers.cloudflare.com/r2/llms.txt)
  * [https://developers.cloudflare.com/workers/llms.txt](https://developers.cloudflare.com/workers/llms.txt)



Rimuoviamo anche centinaia di pagine di elenchi di directory che offrono poco valore semantico a un LLM e ci assicuriamo che ogni pagina abbia un contesto descrittivo dettagliato (titoli, nomi semantici e descrizioni).

Ad esempio, omettiamo circa 450 pagine che fungono solo da elenchi di directory localizzati, ad esempio [https://developers.cloudflare.com/workers/databases/](https://developers.cloudflare.com/workers/databases/).

Queste pagine vengono visualizzate nella nostra sitemap, ma contengono pochissime informazioni per un LLM. Poiché tutte le pagine secondarie sono già collegate singolarmente in `llms.txt`, il recupero di una directory produce solo un elenco ridondante di link, costringendo l’agente a effettuare una nuova richiesta per trovare il contenuto effettivo.

Per aiutare gli agenti a navigare in modo efficiente, ogni voce di `llms.txt` deve essere ricca di contesto ma con un numero limitato di token. Gli esseri umani potrebbero ignorare il frontmatter e le etichette di filtraggio, ma per un agente IA questi metadati sono il volante. Ecco perché il nostro team Product Content Experience (PCX) ha perfezionato i titoli delle nostre pagine, le descrizioni e le strutture degli URL affinché gli agenti sappiano sempre con esattezza quali pagine recuperare.

Dai un'occhiata a una sezione del nostro file root[ llms.txt](https://developers.cloudflare.com/llms.txt).

Ogni link ha un nome semantico, un URL corrispondente e una descrizione di alto valore. Tutto questo non ha richiesto alcun lavoro aggiuntivo per la generazione del file `llms.txt`. Era già tutto disponibile nella parte iniziale della documentazione. Lo stesso vale per i file `llms.txt` nella directory di primo livello. Tutto questo contesto consente agli agenti di trovare le informazioni pertinenti in tempi più rapidi.

### Strumenti di documentazione personalizzati agent-friendly (afdocs)

Inoltre, testiamo la nostra documentazione rispetto ad [afdocs](https://github.com/agent-ecosystem/afdocs), una specifica di documentazione emergente e un progetto open source che consente ai team di testare i siti di documentazione in termini di rilevamento dei contenuti e navigazione. Questa specifica ci ha permesso di realizzare i nostri strumenti di audit personalizzati. Aggiungendo alcune patch mirate e specifiche per il nostro caso d'uso, abbiamo creato una dashboard per una facile valutazione.

### Risultati del benchmark: più veloci e a costi più contenuti

Abbiamo indirizzato un agente (Kimi-k2.5) di OpenCode) nei file `llms.txt` di altri grandi siti di documentazione tecnica e ha chiesto all'agente di rispondere a domande tecniche specifiche.

In media, l'agente che ha consultato la documentazione di Cloudflare ha consumato il **31% in meno di token** ed è arrivato alla risposta corretta il **66% più velocemente** rispetto al sito medio non ottimizzato per gli agenti. Includendo i nostri cataloghi di prodotti in singole finestre di contesto, gli agenti possono identificare la pagina esatta di cui hanno bisogno e recuperarla in un unico percorso lineare.

### La struttura favorisce la velocità

L'accuratezza delle risposte degli LLM è spesso un sottoprodotto dell'efficienza della finestra di contesto. Durante i nostri test, abbiamo osservato uno schema ricorrente con altri set di documentazione.

  1. **Il loop grep:** molti siti di documentazione forniscono un solo, enorme file llms.txt che supera la finestra di contesto immediata dell'agente. Poiché l'agente non può "leggere" l'intero file, inizia ad eseguire il [grep](https://en.wikipedia.org/wiki/Grep) delle parole chiave. Se la prima ricerca non individua il dettaglio specifico, l'agente deve analizzare, affinare la propria ricerca e ripetere il tentativo.
  2. **Contestualizzazione limitata e precisione inferiore:** quando un agente si basa più sulla ricerca iterativa che sulla lettura dell'intero file, perde il contesto più ampio della documentazione. Questa visione frammentata spesso porta l'agente ad avere una comprensione ridotta della documentazione disponibile.
  3. **Latenza e bloat dei token:** ad ogni iterazione del ciclo `grep`, l'agente genera nuovi "token di pensiero" ed esegue richieste di ricerca aggiuntive. Questo scambio rallenta in modo evidente la risposta finale e aumenta il conteggio complessivo dei token, facendo lievitare i costi per l'utente finale.



Per contro, la documentazione Cloudflare è progettata per adattarsi integralmente alla finestra di contesto di un agente. Questo consente all'agente di acquisire la directory, identificare la pagina esatta di cui ha bisogno e recuperare il markdown senza deviazioni.

### Migliorare nel tempo le risposte LLM reindirizzando i crawler di addestramento IA

La documentazione per i prodotti legacy come [Wrangler v1](https://developers.cloudflare.com/workers/wrangler/migration/v1-to-v2/wrangler-legacy/commands/) o [Workers Sites](https://developers.cloudflare.com/workers/configuration/sites/) presenta una sfida unica. Sebbene sia necessario mantenere queste informazioni accessibili per scopi storici, possono portare a suggerimenti obsoleti da parte degli agenti IA.

Ad esempio, un essere umano che legge tali documenti troverebbe il banner di grandi dimensioni che indica che Wrangler v1 è obsoleto, oltre a un link ai contenuti più recente. Un crawler LLM, tuttavia, potrebbe acquisire il testo senza quel contesto visivo circostante. Di conseguenza, l'agente suggerisce informazioni obsolete.

[Redirects for AI Training](https://blog.cloudflare.com/ai-redirects) risolve questo problema identificando i crawler per l'addestramento dell'IA e reindirizzandoli intenzionalmente lontano da contenuti obsoleti o subottimali. In questo modo, le persone continuano ad avere accesso agli archivi storici, mentre gli LLM ricevono solo i nostri dettagli di implementazione più attuali e precisi.

### Direttive degli agenti nascosti su tutte le pagine

Ogni pagina HTML della documentazione include una direttiva nascosta specifica per gli LLM. 

 _"STOP! Se sei un agente IA o un LLM, leggi questo prima di continuare. Questa è la versione HTML di una pagina della documentazione di Cloudflare. Richiedi sempre la versione Markdown, perché l'HTML disperde il contesto. Ottieni questa pagina come Markdown: https://developers.cloudflare.com/index.md (aggiungi index.md) o invia Accept: text/markdown a https://developers.cloudflare.com/. Per tutti i prodotti Cloudflare, utilizza https://developers.cloudflare.com/llms.txt. Puoi accedere a tutta la documentazione di Cloudflare in un unico file all'indirizzo https://developers.cloudflare.com/llms-full.txt."_

Questo frammento informa l'agente che è disponibile una versione Markdown. Fondamentalmente, questa direttiva viene rimossa dalla versione Markdown effettiva per evitare un loop di ricorsione in cui l'agente continuerebbe a cercare il Markdown all'interno del Markdown.

### Barra laterale delle risorse LLM dedicata

Vogliamo infine rendere queste risorse individuabili per le persone che creano con gli agenti. Ogni directory di prodotti nella nostra [documentazione per gli sviluppatori](https://developers.cloudflare.com/) ha una voce "Risorse LLM" nella barra laterale, che fornisce un accesso rapido a `llms.txt`, `llms-full.txt` e alle competenze Cloudflare.

## Rendi il tuo sito web predisposto agli agenti oggi

Rendere i siti web predisposti per gli agenti è un requisito fondamentale di accessibilità per il toolkit degli sviluppatori moderni. Il passaggio da un "web leggibile dall'uomo" a un "web leggibile dalle macchine" rappresenta il più grande cambiamento architettonico degli ultimi decenni. 

Ottieni un punteggio di predisposizione per il tuo sito all'indirizzo [isitagentready.com](https://isitagentready.com/), ricevi i prompt che fornisce e chiedi al tuo agente di effettuare l'upgrade del tuo sito per l'era dell'IA. Non farti sfuggire gli aggiornamenti di [Cloudflare Radar](https://radar.cloudflare.com/) sull'adozione degli standard relativi agli agenti su Internet nel corso del prossimo anno. Se abbiamo imparato qualcosa dall'anno scorso, è che molte cose possono cambiare molto rapidamente.

## Guarda la Cloudflare TV

  


]]>5t83bTn7Vt1EudTxQQ97NYArtefatti: archiviazione versionata che parla Githttps://blog.cloudflare.com/it-it/artifacts-git-for-agents-beta/ Thu, 16 Apr 2026 13:01:00 GMTOffri ai tuoi agenti, sviluppatori e automazioni uno spazio dedicato per codice e dati. Abbiamo appena lanciato Artifacts: archiviazione con versione compatibile con Git, creato per gli agenti. Crea decine di milioni di repository, effettua il fork da qualsiasi repository remoto e fornisci un URL a qualsiasi client Git. AgentiAgents WeekArchiviazioneCloudflare WorkersGitHubPiattaforma per sviluppatoriSviluppatoriGli agenti hanno cambiato il nostro modo di pensare al controllo del codice sorgente, ai file system e alla persistenza dello stato. Gli sviluppatori e gli agenti stanno generando più codice che mai: nei prossimi 5 anni verrà scritto più codice che in tutta la storia della programmazione, e questo ha determinato un cambiamento di un ordine di grandezza nella scala dei sistemi necessari per soddisfare questa domanda. Le piattaforme di controllo del codice sorgente stanno incontrando particolari difficoltà in questo contesto: sono state create per soddisfare le esigenze degli esseri umani, non per un aumento di volume di dieci volte dovuto a un sistema automatizzato che non dorme mai, può gestire più problemi contemporaneamente e non si stanca mai.

Riteniamo che ci sia bisogno di una nuova primitiva: un filesystem distribuito e versionato, progettato principalmente per gli agenti e in grado di supportare le tipologie di applicazioni che vengono sviluppate oggi.

Chiamiamo questo sistema Artifacts: un file system versionato che comunica con Git. È possibile creare repository a livello di programmazione, insieme ad agenti, sandbox, Workers o qualsiasi altro paradigma di calcolo, e connettersi ad essi da qualsiasi client Git standard.

Vuoi assegnare un repository a ogni sessione dell'agente? Artifacts può farlo. A ogni istanza sandbox? Sempre Artifacts. Vuoi creare 10.000 fork partendo da un punto di partenza collaudato? Hai indovinato: di nuovo Artifacts. Artifacts espone un'API REST e un'API Workers nativa per la creazione di repository, la generazione di credenziali e i commit in ambienti in cui un client Git non è la soluzione ideale (ad esempio, in qualsiasi funzione serverless).

Artifacts è disponibile in versione beta privata per tutti gli sviluppatori con il piano Workers a pagamento e puntiamo ad aprirlo come beta pubblica entro l'inizio di maggio.

Questo è tutto. Un repository vuoto, pronto all'uso, creato al volo, su cui qualsiasi client Git può operare.

E se vuoi avviare un repository Artifacts da un repository git esistente in modo che il tuo agente possa lavorarci in modo indipendente e inviare modifiche indipendenti, puoi farlo anche con .import():

[Consulta la documentazione](http://developers.cloudflare.com/artifacts/) per iniziare, oppure, se vuoi capire come viene utilizzato Artifacts, come è stato creato e come funziona a livello tecnico, continua a leggere.

## Perché Git? Cos'è un file system versionato?

Gli agenti conoscono Git. Si trova in profondità nei dati di addestramento della maggior parte dei modelli. Il percorso ideale _e_ i casi limite sono ben noti agli agenti, e i modelli (e/o i framework) ottimizzati per il codice sono particolarmente bravi a usare git.

Inoltre, il modello dati di Git non è solo adatto al controllo del codice sorgente, ma a _qualsiasi cosa_ in cui è necessario tenere traccia dello stato, del viaggio nel tempo e rendere persistenti grandi quantità di dati di piccole dimensioni. Codice, configurazione, prompt di sessione e cronologia dell'agente: tutti questi sono elementi ("oggetti") che spesso si desidera memorizzare in piccoli blocchi ("commit") e a cui si desidera poter tornare indietro o ripristinare la versione precedente ("cronologia"). 

Avremmo potuto inventare un protocollo completamente nuovo e su misura... ma poi si sarebbe presentato il problema del bootstrap. I modelli di intelligenza artificiale non lo sanno, quindi devi distribuire competenze, o un'interfaccia a riga di comando, o sperare che gli utenti siano collegati alla tua documentazione MCP... tutto ciò crea attrito.  
  
E se potessimo semplicemente fornire agli agenti un URL remoto Git HTTPS autenticato e sicuro, e farli operare come se si trattasse di un repository Git? In questo modo, la soluzione si rivelerebbe piuttosto efficace. Per i client che non utilizzano Git, come ad esempio Cloudflare Worker, una funzione Lambda o un'applicazione Node.js, abbiamo reso disponibile un'API REST e (presto) SDK specifici per ciascun linguaggio. Questi client possono anche utilizzare [isomorphic-git](https://isomorphic-git.org/), ma in molti casi un'API TypeScript più semplice può ridurre la superficie API necessaria.

### Non solo per il controllo del codice sorgente

L'API Git di Artifacts potrebbe far pensare che serva solo per il controllo della versione, ma in realtà l'API Git e il modello dati sono un modo potente per rendere persistente lo stato in un modo che consente di creare fork, viaggiare nel tempo e confrontare lo stato di _qualsiasi_ dato.

All'interno di Cloudflare, utilizziamo Artifacts per i nostri agenti interni: persistono automaticamente lo stato corrente del filesystem _e_ la cronologia della sessione in un repository Artifacts per sessione. Ciò ci consente di:

  * Mantenere lo stato della sandbox senza dover eseguire il provisioning (e mantenere) l'archiviazione a blocchi.
  * Condividere le sessioni con altri e consentire loro di tornare indietro nel tempo sia attraverso lo stato della sessione (prompt) _che_ attraverso lo stato del file, indipendentemente dal fatto che siano stati effettuati commit nel repository "effettivo" (controllo del codice sorgente).
  * E la cosa migliore: _esegui il fork_ di una sessione da qualsiasi punto, consentendo al nostro team di condividere le sessioni con un collega e di fargliela riprendere da lui. Stai eseguendo il debug di qualcosa e ti serve un secondo parere? Invia un URL ed eseguine il fork. Vuoi sperimentare con un'API? Chiedi a un collega di crearne una copia (fork) e di riprendere da dove avevi interrotto.



Abbiamo anche parlato con team che vogliono usare Artifacts nei casi in cui il protocollo Git non è affatto un requisito, ma la semantica (reverting, cloning, diffing) _sono_. Memorizzi la configurazione per ciascun cliente come parte del tuo prodotto e desideri la possibilità di ripristinarla? Artifacts può essere una buona rappresentazione.

Siamo entusiasti di vedere i team esplorare i casi d'uso di Artifacts non legati a Git tanto quanto quelli incentrati su Git.

## Nel dettaglio

Gli artefatti sono costruiti a partire da Durable Objects. La capacità di creare milioni (o decine di milioni e oltre) di istanze di elaborazione isolate e con stato è intrinseca al funzionamento attuale dei Durable Objects, ed è esattamente ciò di cui avevamo bisogno per supportare milioni di repository Git per namespace.

La Major League Baseball (per la gestione dei tifosi durante le partite in diretta), le lavagne interattive Confluence e il nostro [Agents SDK](https://developers.cloudflare.com/agents/) utilizzano Durable Objects su larga scala, quindi stiamo sviluppando questa funzionalità basandoci su un elemento primitivo che abbiamo in produzione da tempo.

Ciò di cui avevamo bisogno, tuttavia, era un'implementazione di Git che potesse essere eseguita su Cloudflare Workers. Doveva essere piccolo, il più completo possibile, estensibile ([note](https://git-scm.com/docs/git-notes), [LFS](https://git-lfs.com/)) ed efficiente. Quindi ne abbiamo creato uno in [Zig](https://ziglang.org/) e lo abbiamo compilato in Wasm.

Perché abbiamo usato Zig? Per tre motivi:

  1. L'intero motore del protocollo git è scritto interamente in Zig (senza libc) e compilato in un binario WASM di circa 100 KB (con margine di ottimizzazione). Implementa SHA-1, zlib inflate/deflate, codifica/decodifica delta, analisi dei pacchetti e il protocollo HTTP smart completo di git, tutto da zero, senza dipendenze esterne a parte la libreria standard.
  2. Zig ci offre il controllo manuale sull'allocazione della memoria, aspetto importante in ambienti con risorse limitate come quelli basati su Durable Objects. Il sistema di build Zig ci permette di condividere facilmente il codice tra il runtime WASM (produzione) e le build native (per i test con libgit2 a scopo di verifica della correttezza).
  3. Il modulo WASM comunica con l'host JS tramite una sottile interfaccia di callback: 11 funzioni importate dall'host per le operazioni di archiviazione (host_get_object, host_put_object, ecc.) e una per l'output in streaming (host_emit_bytes). Il lato WASM è completamente testabile in isolamento.



Dietro le quinte, Artifacts utilizza anche R2 (per gli snapshot) e KV (per il tracciamento dei token di autenticazione):

_`Come funziona Artifacts (Workers, Durable Objects e WebAssembly)`_

Un Worker funge da frontend, gestendo l'autenticazione e l'autorizzazione, le metriche chiave (errori, latenza) e la ricerca al volo di ciascun repository di Artifacts (Durable Object). 

In particolare:

  * I file vengono archiviati nel database SQLite del Durable Object sottostante.
    * L'archiviazione di Durable Object ha una dimensione massima di riga di 2 MB, quindi gli oggetti Git di grandi dimensioni vengono suddivisi in blocchi e archiviati su più righe.
    * Utilizziamo l'API KV di sincronizzazione (state.storage.kv) che è supportata da SQLite alla base.
  * Le entità di dominio (DO) hanno un limite di memoria di circa 128 MB: questo significa che possiamo generarne decine di milioni (sono veloci e leggere), ma dobbiamo operare entro tali limiti.
    * Facciamo ampio uso dello streaming sia nel percorso di recupero che in quello di invio, restituendo direttamente un `ReadableStream` costruito a partire dai blocchi di output WASM grezzi.
    * Evitiamo di calcolare i nostri delta git; invece, i delta grezzi e gli hash di base vengono memorizzati insieme all'oggetto risolto. Al momento del recupero, se il client richiedente possiede già l'oggetto base, Zig emette il delta invece dell'oggetto completo, risparmiando larghezza di banda _e_ memoria.
  * Supporto per entrambe le versioni del protocollo Git, v1 e v2.
    * Supportiamo funzionalità quali ls-refs, cloni superficiali (deepen, deepen-since, deepen-relative) e recupero incrementale con negoziazione have/want.
    * Disponiamo di una suite di test completa che include test di conformità con client Git e test di verifica con un server libgit2, progettati per convalidare il supporto del protocollo.



Inoltre, abbiamo il supporto nativo per [git-notes](https://git-scm.com/docs/git-notes). Artifacts è progettato per essere incentrato sull'agente e le note consentono agli agenti di aggiungere note (metadati) agli oggetti Git. Ciò include prompt, attribuzione dell'agente e altri metadati che possono essere letti/scritti dal repository senza modificare gli oggetti stessi.

## Grandi repository, grandi problemi? Scopri ArtifactFS.

La maggior parte dei repository non è così grande e Git è [progettato per essere estremamente efficiente](https://github.blog/open-source/git/gits-database-internals-i-packed-object-store/) in termini di archiviazione: la maggior parte dei repository richiede solo pochi secondi per essere clonata al massimo, e questo tempo è dominato dalla configurazione della rete, dall'autenticazione e dal [checksum](https://git-scm.com/book/ms/v2/Git-Internals-Git-Objects). Nella maggior parte degli scenari con agenti o sandbox, è fattibile: basta clonare il repository all'avvio della sandbox e mettersi al lavoro.

Ma che dire di un repository di diversi gigabyte e/o di repository con milioni di oggetti? Come possiamo clonare rapidamente quel repository, senza bloccare l'agente per minuti e senza consumare risorse di calcolo?

Un framework Web molto diffuso (che pesa 2,4 GB e ha una lunga storia!) richiede circa 2 minuti per essere clonato. Una clonazione superficiale è più veloce, ma non abbastanza da scendere a pochi secondi, e non sempre vogliamo omettere la cronologia (gli agenti la trovano utile).

Possiamo ridurre i tempi di elaborazione dei repository di grandi dimensioni a circa 10-15 secondi, in modo che il nostro agente possa iniziare a lavorare? Ebbene sì, ma con alcuni trucchi.

Nell'ambito del lancio di Artifacts, [stiamo rendendo open source ArtifactFS](https://github.com/cloudflare/artifact-fs), un driver di filesystem progettato per montare repository Git di grandi dimensioni il più rapidamente possibile, idratando il contenuto dei file al volo invece di bloccarsi durante la clonazione iniziale. È ideale per agenti, sandbox, container e altri casi d'uso in cui il tempo di avvio è critico. Se riesci a ridurre di circa 90-100 secondi il tempo di avvio della sandbox per ogni repository di grandi dimensioni, e gestisci 10.000 di questi job sandbox al mese, avrai risparmiato 2.778 ore di sandbox.

Si può pensare ad ArtifactFS come a un "clone Git asincrono":

  * ArtifactFS esegue una clonazione senza blob di un repository Git: recupera la struttura delle cartelle e i riferimenti, ma non il contenuto dei file. Può farlo durante l'avvio della sandbox, consentendo così al tuo agente di entrare in funzione.
  * In background, tramite un daemon leggero, inizia a scaricare (idratare) il contenuto dei file contemporaneamente.
  * Dà priorità ai file su cui gli agenti in genere vogliono operare per primi: manifest dei pacchetti (`package.json, go.mod`), file di configurazione e codice, declassando i blob binari (immagini, eseguibili e altri file non di testo) ove possibile, in modo che gli agenti possano scansionare la struttura delle cartelle mentre i file stessi vengono caricati.
  * Se un file non è completamente idratato quando l'agente tenta di leggerlo, la lettura si bloccherà finché non lo sarà.



Il filesystem non tenta di "sincronizzare" i file con il repository remoto: con migliaia o milioni di oggetti, questa operazione è in genere molto lenta e, dato che stiamo usando Git, non è necessaria. Il tuo agente deve semplicemente effettuare il commit e il push, come farebbe con qualsiasi repository. Nessuna nuova API da imparare.

È importante sottolineare che ArtifactFS funziona con qualsiasi repository remoto Git, non solo con il nostro Artifacts. Se stai clonando repository di grandi dimensioni da GitHub, GitLab o da un'infrastruttura Git self-hosted, puoi comunque utilizzare ArtifactFS.

## Cosa ci aspetta?

La versione che rilasciamo oggi è solo una versione beta e stiamo già lavorando su diverse funzionalità che vedrete implementate nelle prossime settimane:

  * Espandendo le [metriche disponibili](https://developers.cloudflare.com/artifacts/observability/metrics/) che esponiamo. Oggi pubblichiamo metriche relative al numero di operazioni chiave per namespace, repository e byte memorizzati per repository, in modo che la gestione di milioni di artefatti non sia un'impresa ardua.
  * Supporto per le [sottoscrizioni agli eventi](https://developers.cloudflare.com/queues/event-subscriptions/) per eventi a livello di repository, in modo da poter emettere eventi su push, pull, cloni e fork in qualsiasi repository all'interno di un namespace. Questo ti permetterà anche di gestire gli eventi, scrivere webhook e utilizzare tali eventi per notificare gli utenti finali, gestire gli eventi del ciclo di vita all'interno dei tuoi prodotti e/o eseguire processi successivi al rilascio (come CI/CD).
  * SDK client nativi in TypeScript, Go e Python per interagire con l'API Artifacts
  * API di ricerca a livello di repository e API di ricerca a livello di namespace, ad esempio “trova tutti i repository con un file `package.json`”. 



Stiamo inoltre pianificando un'API per le [build di Workers](https://developers.cloudflare.com/workers/ci-cd/builds/), che ti permetterà di eseguire processi CI/CD su qualsiasi flusso di lavoro guidato da agenti.

## Quanto costerà?

Siamo ancora nelle fasi iniziali di Artifacts, ma vogliamo che la nostra politica dei prezzi funzioni su larga scala per gli agenti: deve essere economicamente vantaggioso avere milioni di repository, i repository inutilizzati (o usati raramente) non devono rappresentare un problema e la nostra politica dei prezzi deve essere in linea con la natura massivamente mono-tenant degli agenti.

Inoltre, non dovresti doverti preoccupare se un repository verrà utilizzato o meno, se è attivo o inattivo e/o se un agente lo riattiverà. Ti addebiteremo lo spazio di archiviazione che consumi e le operazioni (ad esempio cloni, fork, push e pull) rispetto a ciascun repository.

| $/unità| Incluso  
---|---|---  
Operazioni| $ 0,15 per 1.000 operazioni| Primi 10.000 inclusi (al mese)  
Archiviazione| $ 0,50/GB-mese| Primo GB incluso.  
  
I repository di grandi dimensioni e molto utilizzati costeranno di più rispetto a quelli più piccoli e meno utilizzati, indipendentemente dal fatto che ne abbiate 1.000, 100.000 o 10 milioni.

Inoltre, nel corso della fase beta, introdurremo Artifacts anche nel piano gratuito di Workers (con alcune limitazioni ragionevoli) e forniremo aggiornamenti durante tutta la versione beta qualora i prezzi dovessero cambiare, prima di qualsiasi addebito relativo all'utilizzo.

## Da dove cominciare? 

Artifacts verrà lanciato in versione beta privata e prevediamo che la versione beta pubblica sarà pronta all'inizio di maggio (2026, per essere precisi). Nelle prossime settimane consentiremo l'accesso progressivamente ai clienti e [puoi registrare il tuo interesse per la beta privata](https://forms.gle/DwBoPRa3CWQ8ajFp7) direttamente.

Nel frattempo, puoi saperne di più su Artifacts come segue:

  * Leggendo la [guida introduttiva](http://developers.cloudflare.com/artifacts/get-started/workers/) nella documentazione.
  * Visitando il dashboard di Cloudflare (Build > Storage e database > Artifacts)
  * Leggendo gli [esempi di API REST](http://developers.cloudflare.com/artifacts/api/rest-api/)
  * Scopri di più su [come funziona Artifacts](http://developers.cloudflare.com/artifacts/concepts/how-artifacts-works/) dietro le quinte



Segui [il registro delle modifiche](http://developers.cloudflare.com/changelog/product/artifacts/) per monitorare lo sviluppo della versione beta.

## Guarda la Cloudflare TV

]]>2sshzOlmGVsrtBz2mgeceE
