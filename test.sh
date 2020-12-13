#!/bin/sh
set -xe
if [ ! -f DeepSpeech.py ]; then
    echo "Please make sure you run this from DeepSpeech's top level directory."
    exit 1
fi;

# Force only one visible device because we have a single-sample dataset
# and when trying to run on multiple devices (like GPUs), this will break
export CUDA_VISIBLE_DEVICES=0

python -u DeepSpeech.py --noshow_progressbar \
  --train_files data/training_sets/train.csv \
  --test_files data/training_sets/test.csv \
  --dev_files data/training_sets/dev.csv \
  --train_batch_size 16 \
  --test_batch_size 8 \
  --epochs 10 \
  --checkpoint_dir ./es_checkpoint/ \
  --export_dir ./es_model_export/ \
  --save_checkpoint_dir ./es_save_ckp/ \
  --scorer data/kenlm_es.scorer \
  --alphabet_config_path data/alphabet_es.txt \
  --n_hidden 2048\
  --train_cudnn \
  "$@"
