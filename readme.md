# Repositorio DeepSpeech para español chileno

El objetivo de este proyecto es hacer un modelo de transcripción de voz a texto (STT por sus siglas en ingles), especializado en español chileno. Dentro de este repositorio se encuentra una descripción del trabajo realizado hasta ahora y queda abierto a otras personas para que continúen desarrollando.

## DeepSpeech

DeepSpeech es un proyecto desarrollado por Mozilla, con la intención de desarrollar un framework open source para desarrollar modelos de STT, basado en inteligencia artificial. Se puede encontrar más información en su [repositorio oficial](https://github.com/mozilla/DeepSpeech).

La documentación para la utilizar DeepSpeech, ya sea para inferencia o entrenamiento se encuentra en el siguiente [link](https://deepspeech.readthedocs.io/).

## Nuestro Modelo

Una de las grandes ventajas que tiene DeepSpeech sobre otros modelos, es que permite continuar el entrenamiento sobre un modelo existente. De esta forma, podemos 'especializar' un modelo de español, para él dialecto chileno. Para nuestro modelo, continuamos en entrenamiento sobre un modelo de español llamado **DeepSpeech-Polyglot** (tiene modelos para varios lenguajes mas). Y se utilizaron dos datasets de español chileno para continuar el entrenamiento. A continuación se detalla sobre el modelo utilizado y los datasets.

### DeepSpeech-Polyglot

Dentro de este [repositorio](https://gitlab.com/Jaco-Assistant/deepspeech-polyglot) se puede encontrar toda la información de este gran proyecto, que trabaja con multiples idiomas.

El modelo de español se generó a través de una metodología llamada [transfer learning](https://deepspeech.readthedocs.io/en/latest/TRAINING.html#transfer-learning-new-alphabet), a partir de un modelo entrenado para ingles. Se utilizaron las siguientes bases de datos:

- Mozilla Common Voice ~390h
- CSS10 ~24h
- LinguaLibre ~1h
- M-AILABS Speech Dataset ~108h
- Tatoeba ~59h
- Voxforge ~52h

Consiguiendo un [WER](https://es.wikipedia.org/wiki/Word_Error_Rate) de 0.165126. 

Para nuestro modelo, continuamos el entrenamiento sobre los [checkpoints](https://drive.google.com/drive/folders/1-3UgQBtzEf8QcH2qc8TJHkUqCBp5BBmO) publicados de este proyecto.

### Datasets

Para continuar el entrenamiento, combinamos dos bases de datos de español chileno.

#### Crowdsourced high-quality Chilean Spanish [es-cl] multi-speaker speech dataset
[Acceso](https://research.google/tools/datasets/chilean-spanish-tts/). Esta base de datos contiene ~7horas de 31 participantes distintos.

#### Common Voice Corpus 5.1 - Español
[Acceso](https://commonvoice.mozilla.org/es/datasets). La base de datos originalmente contiene ~521horas de audio, pero luego de filtrar para hablantes chilenos(~2%) y audios validados, quedan ~4horas útiles para entrenamiento.

Para información de como se pre-procesó y juntó estas bases de datos, leer el **README** de [preprocesamiento](https://github.com/diegoaguayo/es_cl_deepspeech/tree/master/preprocesamiento).
## Entrenamiento
Para el entrenamiento se utilizaron las bases de datos mencionadas anteriormente. El script utilizado para el entrenamiento es [train.sh](). Información sobre los hiper-parámetros utilizados se puede encontrar [acá](https://deepspeech.readthedocs.io/en/latest/Flags.html#training-flags).

## Resultados

Posterior al entrenamiento, el modelo obtuvo un WER de 0.122763, sobre nuestro set de *test*. El modelo original, sobre este mismo set de test, obtuvo un WER de 0.131423. Se pueden destacar dos cosas de estos resultados. 

Primero, el WER del modelo original es menor de lo esperado (0.165126), probablemente porque la calidad del dataset era buena y sin ruido ambiente.

Segundo, el modelo no mejoró mucho respecto al modelo original. Esto no es muy sorprendente, ya que la base de datos con la que se contaba es pequeña. Se necesita un orden de cientas de horas para obtener un buen modelo.


### Desafíos

Conseguir bases de datos mas grandes ... ...

## Sobre el proyecto