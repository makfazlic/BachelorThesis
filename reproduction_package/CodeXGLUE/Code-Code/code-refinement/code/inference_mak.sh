#!/bin/bash
output_dir=inference-bucket_merged_cl_4
python run.py \
    		--do_test \
		--model_type roberta \
		--model_name_or_path roberta-base \
		--config_name roberta-base \
		--tokenizer_name roberta-base  \
		--load_model_path /home/mfazlic/CodeXGLUE/Code-Code/code-refinement/code/bucket_merged_cl_4/checkpoint-20000/pytorch_model.bin \
		--test_filename ../data/merged/test.buggy-fixed.buggy,../data/merged/test.buggy-fixed.fixed \
		--output_dir $output_dir \
		--max_source_length 256 \
		--max_target_length 256 \
		--beam_size 10 \
		--eval_batch_size 4
