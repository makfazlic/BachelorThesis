lang=java #programming language
lr=5e-5
batch_size=16
beam_size=10
source_length=256
target_length=128
data_dir=../dataset
output_dir=models/$lang/cl_3
train_file=$data_dir/$lang/train_cl_3.jsonl
dev_file=$data_dir/$lang/valid.jsonl
epochs=10 
load_model_path=models/$lang/cl_2/checkpoint-best-bleu/pytorch_model.bin
pretrained_model=microsoft/codebert-base #Roberta: roberta-base

python run.py --do_train --do_eval --model_type roberta --model_name_or_path $pretrained_model --load_model_path $load_model_path --train_filename $train_file --dev_filename $dev_file --output_dir $output_dir --max_source_length $source_length --max_target_length $target_length --beam_size $beam_size --train_batch_size $batch_size --eval_batch_size $batch_size --learning_rate $lr --num_train_epochs $epochs