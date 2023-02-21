# Appendice A - Configurazione dell'ambiente di sviluppo Python

## Installazione di Python

1. Andare al seguente [indirizzo](https://www.python.org/downloads/release/python-3912/), e selezionare la versione adatta al proprio sistema operativo.
2. Iniziare la procedura di installazione (ad esempio, in Windows, cliccando sull'eseguibile appena scaricato). **E' fortemente consigliato aggiungere Python al proprio PATH spuntando l'opportuna casella durante l'installazione**, come mostrato in figura 1.

<figure markdown>
    ![python_installation](./images/python_installation.png){: .center, width="450"}
    <figcaption>Figura 1 - Aggiunta di Python al PATH</figcaption>
</figure>


3. Una volta completata la procedura di installazione, aprire uno shell (ad esempio, il prompt dei comandi), e digitare `python`. Se tutto è andato per il verso giusto, apparirà una schermata simile a quella mostrata in figura 2.

<figure markdown>
    ![python_interpreter](./images/python_interpreter.png){: .center, width="450"}
    <figcaption>Figura 2 - Lancio dell'interprete Python</figcaption>
</figure>

## Installazione di Visual Studio Code

1. Andare al seguente [indirizzo](https://code.visualstudio.com/download), e selezionare la versione adatta al proprio sistema operativo.
2. Seguire la procedura di installazione mostrata a schermo. **E' anche in questo caso consigliata l'aggiunta di Visual Studio Code al path, come mostrato in figura 3.**

<figure markdown>
    ![vscode_installation](./images/vscode_installation.png){: .center, width="450"}
    <figcaption>Figura 3 - Installazione di Visual Studio Code</figcaption>
</figure>

## Setup di TensorFlow

In questa sezione, vedremo come effettuare il setup di TensorFlow su tre diversi sistemi operativi, ovvero Windows, Linux e MacOS.

!!!warning "TensorFlow e Windows"
    A partire dalla versione 2.11, TensorFlow **non è più supportato su Windows**. Di conseguenza, è necessario seguire una procedura differente, dettagliata in questa guida.

=== Windows WSL2

    **Requisiti di sistema**
    
    Sono necessari:
    
    * una versione di Windows 10 aggiornata almeno alla versione 21H2;
    * il Windows Subsystem on Linux (WSL2);
    * il supporto alla GPU Nvidia su WSL2.

    




=== Linux

=== MacOS
