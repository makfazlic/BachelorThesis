#!/bin/bash
pretrained_model=microsoft/codebert-base
output_dir=finetuned-cl-medium

#add eventually -m torch.distributed.launch --nproc_per_node 3 

python3 run.py \
       --do_train \
       --do_eval \
       --model_type roberta \
       --model_name_or_path $pretrained_model \
       --config_name roberta-base \
       --tokenizer_name roberta-base \
       --train_filename ../dataCL/medium/train.buggy-fixed.1.buggy,../dataCL/medium/train.buggy-fixed.1.fixed \
       --dev_filename ../data/medium/valid.buggy-fixed.buggy,../data/medium/valid.buggy-fixed.fixed \
       --output_dir $output_dir \
       --max_source_length 256 \
       --max_target_length 256 \
       --beam_size 1 \
       --train_batch_size 16 \
       --eval_batch_size 16 \
       --train_steps 100000 \
       --eval_steps 5000
