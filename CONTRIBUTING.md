# Linee guida per contribuire alla repository 🚀

Questa guida è pensata per offrire a chiunque un modo semplice di contribuire alla repository del corso.

## Creare una Pull Request (PR) 🛠️

Creare una PR è molto semplice. In questo esempio, vediamo come crearne una per aggiornare il file `index.md`.

### 1. Scegliere il file da aggiornare

Scegliamo il file `index.md` dall'interfaccia di GitHub.

### 2. Cliccare su 'Edit this file'

Cliccare sul pulsante 'Edit this file' nell'angolo in alto a destra.

### 3. Modificare il file

Modifichiamo il file `index.md` nella maniera più opportuna.

### 4. Controllare le modifiche e sottomettere la PR

Selezioniamo il tab **Preview changes** per verificare le modifiche apportate. In basso scegliamo l'opzione 'Create a **new branch**
for this commit', assegnamo al nostro branch un nome sufficientemente significativo, come `fix/updated_index`, e clicchiamo sul pulsante **Propose changes**. La nostra PR verrà quindi sottomessa per essere revisionata (ed approvata 😃)!

### Suggerimenti

Ecco una serie di consigli per integrare al meglio il vostro lavoro:

- ✅ verificate che la PR si **riferisca al branch master presente sulla repository remota**. Se la PR non è aggiornata, potete provare a fare un merge su un branch locale:

  ```bash
  git remote add upstream https://github.com/anhelus/python-calcolo-numerico.git
  git fetch upstream
  git checkout feature  # <----- sostituiamo 'feature' con il nome del nostro branch
  git merge upstream/master
  git push -u origin -f
  ```

- ✅ fate in modo che le modifiche siano **minime** e **strettamente inerenti il bug o la feature** che vogliamo risolvere o introdurre.

## Segnalare un Bug 🐛

Se notate un problema con la repository del corso, potete segnalarlo! Tuttavia, è importante descrivere il problema in modo da creare un [esempio riproducibile](https://stackoverflow.com/help/minimal-reproducible-example) del problema. Questo esempio dovrebbe essere:

* ✅ **minimalistico**: usiamo il quantitativo di codice minimo ed indispensabile per riprodurre lo stesso problema;
* ✅ **completo**: forniamo **tutte** le istruzioni necessarie a riprodurre il problema;
* ✅ **riproducibile**: testiamo il codice che stiamo per fornire in modo tale che riproduca il problema.

Oltre a questi prerequisiti, è opportuno controllare che il nostro codice sia:

* ✅ **attualizzato**: verifichiamo che il codice sia aggiornato all'attuale branch [master](https://github.com/anhelus/python-calcolo-numerico/tree/master). Se necessario, aggiorniamo questo codice mediante una `git pull` o `git clone`.
* ✅ **non modificato**: verifichiamo che il problema possa essere riprodotto senza dover apportare alcuna modifica alla codebase della repository.

Se il bug che abbiamo individuato rispetta tutti questi criteri, possiamo creare un nuovo issue mediante l'apposito [template](https://github.com/anhelus/python-calcolo-numerico/issues/new/choose).

## Licenza

I vostri contributi saranno soggetti alla stessa licenza della repository, ovvero la [MIT](./LICENSE).
