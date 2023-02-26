# Appendice B - Setup di TensorFlow

!!!tip "Versione video"
    Una versione video di questa procedura di installazione è in arrivo.

In questa sezione, vedremo come effettuare il setup di TensorFlow su tre diversi sistemi operativi, ovvero Windows, Linux e MacOS.

!!!warning "TensorFlow e Windows"
    A partire dalla versione 2.11, TensorFlow **non è più supportato su Windows**. Di conseguenza, è necessario seguire una procedura differente, dettagliata in questa guida.

=== "Windows WSL2"

    ##### 1. Requisiti di sistema

    I requisiti necessari sono:
    
    * Windows 10 aggiornato almeno alla versione 21H2;
    * Windows Subsystem on Linux (WSL2), reperibile [da qui](https://docs.microsoft.com/windows/wsl/install).

    ##### 2. (Opzionale) Setup della GPU NVIDIA in WSL

    Qualora si disponga di una GPU NVIDIA, si potrà effettuare il setup della stessa su WSL2. 
    
    Supponendo di aver installato Ubuntu sul WSL2, dovremo per prima cosa entrare nel sottosistema Linux scrivendo da terminale l'istruzione:
    
    ```sh
    wsl
    ```

    Una volta dentro, dovremo eseguire le seguenti istruzioni da riga di comando:

    ```sh
    sudo apt-key del 7fa2af80
    wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-wsl-ubuntu.pin
    sudo mv cuda-wsl-ubuntu.pin /etc/apt/preferences.d/cuda-repository-pin-600
    wget https://developer.download.nvidia.com/compute/cuda/12.0.0/local_installers/cuda-repo-wsl-ubuntu-12-0-local_12.0.0-1_amd64.deb
    sudo dpkg -i cuda-repo-wsl-ubuntu-12-0-local_12.0.0-1_amd64.deb
    sudo cp /var/cuda-repo-wsl-ubuntu-12-0-local/cuda-*-keyring.gpg /usr/share/keyrings/
    sudo apt-get update
    sudo apt-get -y install cuda
    ```

    Per maggior informazioni, potete consultare la guida completa disponibile a [questo indirizzo](https://docs.nvidia.com/cuda/wsl-user-guide/index.html).

    ##### 3. Installazione di Miniconda

    A partire dalla versione 2.11, il metodo raccomandato per l'utilizzo di TensorFlow è quello di utilizzare [Miniconda](https://docs.conda.io/en/latest/miniconda.html), creando un ambiente virtuale separato all'interno del quale andare ad installare tutte le dipendenze necessarie.

    Da terminale, scriviamo:

    ```sh
    curl https://repo.anaconda.com/miniconda Miniconda3-latest-Linux-x86_64.sh -o Miniconda3-latest-Linux-x86_64.sh
    bash Miniconda3-latest-Linux-x86_64.sh
    ```

    Durante l'installazione, rispondiamo sempre `yes` alle domande che ci verranno fatte, premendo successivamente `Invio`.

    ##### 4. Creazione di un ambiente virtuale

    Una volta terminata l'installazione, riavviamo il sottosistema Linux (per farlo, scriviamo `exit` e, una volta usciti, `wsl`). A questo punto potremo creare un nuovo ambiente virtuale basato su Python 3.9 che chiameremo `pcs`:

    ```sh
    conda create --name pcs python=3.9
    ```

    Possiamo quindi attivare questo ambiente virtuale scrivendo:

    ```sh
    conda deactivate
    conda activate pcs
    ```

    ##### 5. (Opzionale) Setup della GPU

    Questo step ci permette di configurare ed utilizzare la GPU nell'ambiente virtuale del nostro sistema Linux. Per prima cosa, verifichiamo che i driver siano installati usando la seguente istruzione:

    ```sh
    nvidia-smi
    ```

    Qualora non siano installati, occorrerà farlo prelevandoli dal [sito ufficiale](https://www.nvidia.com/Download/index.aspx).

    Configuriamo il PATH del sistema:

    ```sh
    mkdir -p $CONDA_PREFIX/etc/conda/activate.d
    echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/' > $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
    ```

    ##### 6. Installazione di TensorFlow

    Installiamo TensorFlow usando un package manager a nostra scelta (ad esempio, `pip`):

    ```sh
    pip install tensorflow
    ```

    Verifichiamo l'installazione per la CPU:

    ```sh
    python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
    ```

    e per la GPU:

    ```sh
    python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
    ```

=== "Linux"

    ##### 1. Requisiti di sistema

    I requisiti necessari sono:
    
    * Ubuntu aggiornato almeno alla versione 16.04.

    ##### 2. Installazione di Miniconda

    A partire dalla versione 2.11, il metodo raccomandato per l'utilizzo di TensorFlow è quello di utilizzare [Miniconda](https://docs.conda.io/en/latest/miniconda.html), creando un ambiente virtuale separato all'interno del quale andare ad installare tutte le dipendenze necessarie.

    Da terminale, scriviamo:

    ```sh
    curl https://repo.anaconda.com/miniconda Miniconda3-latest-Linux-x86_64.sh -o Miniconda3-latest-Linux-x86_64.sh
    bash Miniconda3-latest-Linux-x86_64.sh
    ```

    Durante l'installazione, rispondiamo sempre `yes` alle domande che ci verranno fatte, premendo successivamente `Invio`.

    ##### 3. Creazione di un ambiente virtuale

    Una volta terminata l'installazione, riavviamo il sottosistema Linux (per farlo, scriviamo `exit` e, una volta usciti, `wsl`). A questo punto potremo creare un nuovo ambiente virtuale basato su Python 3.9 che chiameremo `pcs`:

    ```sh
    conda create --name pcs python=3.9
    ```

    Possiamo quindi attivare questo ambiente virtuale scrivendo:

    ```sh
    conda deactivate
    conda activate pcs
    ```

    ##### 4. (Opzionale) Setup della GPU

    Questo step ci permette di configurare ed utilizzare la GPU nell'ambiente virtuale del nostro sistema Linux. Per prima cosa, verifichiamo che i driver siano installati usando la seguente istruzione:

    ```sh
    nvidia-smi
    ```

    Qualora non siano installati, occorrerà farlo prelevandoli dal [sito ufficiale](https://www.nvidia.com/Download/index.aspx).

    Configuriamo il PATH del sistema:

    ```sh
    mkdir -p $CONDA_PREFIX/etc/conda/activate.d
    echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/' > $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
    ```

    ##### 5. Installazione di TensorFlow

    Installiamo TensorFlow usando un package manager a nostra scelta (ad esempio, `pip`):

    ```sh
    pip install tensorflow
    ```

    Verifichiamo l'installazione per la CPU:

    ```sh
    python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
    ```

    e per la GPU:

    ```sh
    python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
    ```

    ##### Errori in Ubuntu 22.04

    Nel caso si utilizzi la versione 22.04 di Ubuntu, potremmo trovarci di fronte al seguente errore:

    ```sh
    Can't find libdevice directory ${CUDA_DIR}/nvvm/libdevice.
    ...
    Couldn't invoke ptxas --version
    ...
    InternalError: libdevice not found at ./libdevice.10.bc [Op:__some_op]
    ```

    Per risolverlo, eseguiamo le seguenti istruzioni:

    ```sh
    conda install -c nvidia cuda-nvcc=11.3.58
    mkdir -p $CONDA_PREFIX/etc/conda/activate.d
    printf 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/\nexport XLA_FLAGS=--xla_gpu_cuda_data_dir=$CONDA_PREFIX/lib/\n' > $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
    source $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
    mkdir -p $CONDA_PREFIX/lib/nvvm/libdevice
    cp $CONDA_PREFIX/lib/libdevice.10.bc $CONDA_PREFIX/lib/nvvm/libdevice/
    ```

=== "macOS"

    ##### 1. Requisiti di sistema

    I requisiti necessari sono:
    
    * macOS aggiornato almeno alla versione 10.12.6 (Sierra).

    ##### 2. Verifica della versione di Python installata

    Verifichiamo che sia installato Python dalla versione 3.7 alla 3.10:

    ```sh
    python3 --version
    ```

    e pip nella versione superiore alla 20.3:

    ```sh
    python3 -m pip --version
    ```

    ##### 2. Installazione di Miniconda

    A partire dalla versione 2.11, il metodo raccomandato per l'utilizzo di TensorFlow è quello di utilizzare [Miniconda](https://docs.conda.io/en/latest/miniconda.html), creando un ambiente virtuale separato all'interno del quale andare ad installare tutte le dipendenze necessarie.

    Da terminale, scriviamo:

    ```sh
    curl https://repo.anaconda.com/miniconda Miniconda3-latest-Linux-x86_64.sh -o Miniconda3-latest-Linux-x86_64.sh
    bash Miniconda3-latest-Linux-x86_64.sh
    ```

    Durante l'installazione, rispondiamo sempre `yes` alle domande che ci verranno fatte, premendo successivamente `Invio`.

    ##### 3. Creazione di un ambiente virtuale

    Una volta terminata l'installazione, riavviamo il sottosistema Linux (per farlo, scriviamo `exit` e, una volta usciti, `wsl`). A questo punto potremo creare un nuovo ambiente virtuale basato su Python 3.9 che chiameremo `pcs`:

    ```sh
    conda create --name pcs python=3.9
    ```

    Possiamo quindi attivare questo ambiente virtuale scrivendo:

    ```sh
    conda deactivate
    conda activate pcs
    ```

    ##### 4. Installazione di TensorFlow

    Installiamo TensorFlow usando un package manager a nostra scelta (ad esempio, `pip`):

    ```sh
    pip install tensorflow
    ```

    Verifichiamo l'installazione:

    ```sh
    python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
    ```
