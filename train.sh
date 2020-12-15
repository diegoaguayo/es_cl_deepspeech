#!/bin/sh
set -xe
if [ ! -f DeepSpeech.py ]; then
    echo "Please make sure you run this from DeepSpeech's top level directory."
    exit 1
fi;

echo $(date -u) "Empezo entrenamiento"

python -u DeepSpeech.py --noshow_progressbar \
  --log_level 1 \
  --train_files data/training_sets/train.csv \
  --test_files data/training_sets/test.csv \
  --dev_files data/training_sets/dev.csv \
  --early_stop \
  --reduce_lr_on_plateau \
  --train_batch_size 32 \
  --dev_batch_size 32 \
  --test_batch_size 32 \
  --epochs 60 \
  --checkpoint_dir ./es_checkpoint/ \
  --export_dir ./es_model_export/ \
  --scorer data/kenlm_es.scorer \
  --alphabet_config_path data/alphabet_es.txt \
  --n_hidden 2048\
  --train_cudnn \
  "$@"

echo $(date -u) "Termino el entrenamiento"