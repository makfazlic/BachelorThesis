#!/bin/bash
output_dir=buckets_v2_inf/merged/bs_5
python run.py \
    		--do_test \
		--model_type roberta \
		--model_name_or_path roberta-base \
		--config_name roberta-base \
		--tokenizer_name roberta-base  \
		--load_model_path /home/mfazlic/CodeXGLUE/Code-Code/code-refinement/code/buckets_v2/merged_finetuned_4/checkpoint-25000/pytorch_model.bin \
		--test_filename ../data/merged/test.buggy-fixed.buggy,../data/merged/test.buggy-fixed.fixed \
		--output_dir $output_dir \
		--max_source_length 256 \
		--max_target_length 256 \
		--beam_size 5 \
		--eval_batch_size 4
