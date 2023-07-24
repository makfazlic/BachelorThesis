#!/bin/bash
output_dir=run-on-test-overall
python run.py \
    		--do_test \
		--model_type roberta \
		--model_name_or_path roberta-base \
		--config_name roberta-base \
		--tokenizer_name roberta-base  \
		--load_model_path /home/mastro1996/CodeXGLUE/Code-Code/code-refinement/code/finetuned-overall-vanilla/checkpoint-40000/pytorch_model.bin \
		--test_filename ../data/overall/test.buggy-fixed.buggy,../data/overall/test.buggy-fixed.fixed \
		--output_dir $output_dir \
		--max_source_length 256 \
		--max_target_length 256 \
		--beam_size 5 \
		--eval_batch_size 16 
