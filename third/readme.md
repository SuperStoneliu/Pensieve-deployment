此轮训练的基础模型为second/model 中的模型
熵值权重为0.5
select_rl_no_training.py,select_plot_results.py,modelselect.py 为自动测试脚本，model中每一个模型的期望奖励值都会被记录在mr.txt 中

tp.py为模型转移脚本，放在sim/results中，在训练过程中生成的模型都会被转移到sim/allmodels中。


