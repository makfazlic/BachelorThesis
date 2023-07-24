#!/bin/bash
output_dir=b_buckets_v2_inf/merged
python run.py \
    		--do_test \
		--model_type roberta \
		--model_name_or_path roberta-base \
		--config_name roberta-base \
		--tokenizer_name roberta-base  \
		--load_model_path /home/mfazlic/CodeXGLUE/Code-Code/code-refinement/code/b_buckets_v2/merged_finetuned/checkpoint-60000/pytorch_model.bin \
		--test_filename ../data/merged/test.buggy-fixed.buggy,../data/merged/test.buggy-fixed.fixed \
		--output_dir $output_dir \
		--max_source_length 256 \
		--max_target_length 256 \
		--beam_size 1 \
		--eval_batch_size 4
