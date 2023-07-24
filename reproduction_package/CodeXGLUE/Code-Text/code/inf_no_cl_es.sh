lang=java #programming language
data_dir=../dataset
output_dir=models/$lang/inf_no_cl_es_1
batch_size=8
beam_size=1
source_length=256
target_length=128
dev_file=$data_dir/$lang/valid.jsonl
test_file=$data_dir/$lang/test.jsonl
test_model=models/$lang/no_cl_es/checkpoint-175235/pytorch_model.bin #checkpoint for test

python run.py --do_test --model_type roberta --model_name_or_path microsoft/codebert-base --load_model_path $test_model --dev_filename $dev_file --test_filename $test_file --output_dir $output_dir --max_source_length $source_length --max_target_length $target_length --beam_size $beam_size --eval_batch_size $batch_size