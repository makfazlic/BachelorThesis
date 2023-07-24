#!/bin/bash
pretrained_model=microsoft/codebert-base
output_dir=buckets_v2/medium_finetuned_1

CUDA_VISIBLE_DEVICES=1 python3 run.py \
       --do_train \
       --do_eval \
       --model_type roberta \
       --model_name_or_path $pretrained_model \
       --config_name roberta-base \
       --tokenizer_name roberta-base \
       --train_filename ../dataCL_v2/medium/train.buggy-fixed.1.buggy,../dataCL_v2/medium/train.buggy-fixed.1.fixed \
       --dev_filename ../data/medium/valid.buggy-fixed.buggy,../data/medium/valid.buggy-fixed.fixed \
       --output_dir $output_dir \
       --max_source_length 256 \
       --max_target_length 256 \
       --beam_size 1 \
       --train_batch_size 4 \
       --eval_batch_size 4 \
       --learning_rate 5e-5 \
       --train_steps 100000 \
       --eval_steps 5000
