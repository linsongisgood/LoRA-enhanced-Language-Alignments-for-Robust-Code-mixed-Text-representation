# coding=gbk
import os
import random
import re
import numpy as np
import torch
from sklearn.metrics import classification_report
from transformers import WEIGHTS_NAME, CONFIG_NAME
from models_o.xlm_roberta4 import xlm_robertamodel


sentences = []
tags = []
tags_en = []
path1 =''
path2 =''
path3 =''
path4 =''
path5 =''
path6 =''
labels = []
with open(path1, "r") as f:
    lines = f.readlines()
    for line in lines:
        a = re.split(r"\s+", line, maxsplit=1)
        x = a[0]
        labels.append(int(x))

with open(path1, "r") as f:
    lines = f.readlines()
    for line in lines:
        a = re.split(r"\s+", line, maxsplit=1)
        y = a[1]
        sentences.append(y)

with open(path2 , "r") as f:
    lines = f.readlines()
    for line in lines:
        a = re.split(r"\s+", line, maxsplit=1)
        y = a[1]
        tags.append(y)

with open(path3, "r") as f:
    lines = f.readlines()
    for line in lines:
        a = re.split(r"\s+", line, maxsplit=1)
        y = a[1]
        tags_en.append(y)

sentences2 = []
tags2 = []
tags_en2 = []
labels2 = []
with open(path4, "r") as f:
    lines = f.readlines()
    for line in lines:
        a = re.split(r"\s+", line, maxsplit=1)
        x = a[0]
        labels2.append(int(x))

with open(path4, "r") as f:
    lines = f.readlines()
    for line in lines:
        a = re.split(r"\s+", line, maxsplit=1)
        x = a[1]
        sentences2.append(x)

with open(path5, "r") as f:
    lines = f.readlines()
    for line in lines:
        a = re.split(r"\s+", line, maxsplit=1)
        x = a[1]
        tags2.append(x)
with open(path6, "r") as f:
    lines = f.readlines()
    for line in lines:
        a = re.split(r"\s+", line, maxsplit=1)
        x = a[1]
        tags_en2.append(x)


from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("../../../root/autodl-tmp/xlm-roberta-large")

input_ids = []
attention_masks = []
p1 = []
input_ids_1 = []
attention_masks_1 = []
p2 = []
input_ids_2 = []
attention_masks_2= []
p3 = []
input_ids2 = []
attention_masks2 = []
p4 = []
input_ids2_2 = []
attention_masks2_2 = []
p5 = []
input_ids2_3 = []
attention_masks2_3 = []
p6 = []

for sent in sentences:
    encoded_dict = tokenizer(
        sent,  # Sentence to encode.
        add_special_tokens=True,  # Add '[CLS]' and '[SEP]'
        max_length=60,  # Pad & truncate all sentences.
        pad_to_max_length=True,
        return_attention_mask=True,  # Construct attn. masks.
        return_tensors='pt',  # Return pytorch tensors.
    )
    # 把编码的句子加入list.
    input_ids.append(encoded_dict['input_ids'])
    # 加上 attention mask (simply differentiates padding from non-padding).
    attention_masks.append(encoded_dict['attention_mask'])
from language_tag import lang_tag
p1 = torch.tensor(lang_tag(sentences))

for sent in tags:
    encoded_dict = tokenizer(
        sent,  # Sentence to encode.
        add_special_tokens=True,  # Add '[CLS]' and '[SEP]'
        max_length=60,  # Pad & truncate all sentences.
        pad_to_max_length=True,
        return_attention_mask=True,  # Construct attn. masks.
        return_tensors='pt',  # Return pytorch tensors.
    )
    # 把编码的句子加入list.
    input_ids_1.append(encoded_dict['input_ids'])
    # 加上 attention mask (simply differentiates padding from non-padding).
    attention_masks_1.append(encoded_dict['attention_mask'])
p2 = torch.tensor(lang_tag(tags))

for sent in tags_en:
    encoded_dict = tokenizer(
        sent,  # Sentence to encode.
        add_special_tokens=True,  # Add '[CLS]' and '[SEP]'
        max_length=60,  # Pad & truncate all sentences.
        pad_to_max_length=True,
        return_attention_mask=True,  # Construct attn. masks.
        return_tensors='pt',  # Return pytorch tensors.
    )
    # 把编码的句子加入list.
    input_ids_2.append(encoded_dict['input_ids'])
    # 加上 attention mask (simply differentiates padding from non-padding).
    attention_masks_2.append(encoded_dict['attention_mask'])
p3 = torch.tensor(lang_tag(tags_en))

for sent in sentences2:
    encoded_dict2 = tokenizer(
        sent,  # Sentence to encode.
        add_special_tokens=True,  # Add '[CLS]' and '[SEP]'
        max_length=60,  # Pad & truncate all sentences.
        pad_to_max_length=True,
        return_attention_mask=True,  # Construct attn. masks.
        return_tensors='pt',  # Return pytorch tensors.
    )
    # 把编码的句子加入list.
    input_ids2.append(encoded_dict2['input_ids'])
    # 加上 attention mask (simply differentiates padding from non-padding).
    attention_masks2.append(encoded_dict2['attention_mask'])
p4 = torch.tensor(lang_tag(sentences2))

for sent in tags2:
    encoded_dict = tokenizer(
        sent,  # Sentence to encode.
        add_special_tokens=True,  # Add '[CLS]' and '[SEP]'
        max_length=60,  # Pad & truncate all sentences.
        pad_to_max_length=True,
        return_attention_mask=True,  # Construct attn. masks.
        return_tensors='pt',  # Return pytorch tensors.
    )
    # 把编码的句子加入list.
    input_ids2_2.append(encoded_dict['input_ids'])
    # 加上 attention mask (simply differentiates padding from non-padding).
    attention_masks2_2.append(encoded_dict['attention_mask'])
p5 = torch.tensor(lang_tag(tags2))
for sent in tags_en2:
    encoded_dict = tokenizer(
        sent,  # Sentence to encode.
        add_special_tokens=True,  # Add '[CLS]' and '[SEP]'
        max_length=60,  # Pad & truncate all sentences.
        pad_to_max_length=True,
        return_attention_mask=True,  # Construct attn. masks.
        return_tensors='pt',  # Return pytorch tensors.
    )
    # 把编码的句子加入list.
    input_ids2_3.append(encoded_dict['input_ids'])
    # 加上 attention mask (simply differentiates padding from non-padding).
    attention_masks2_3.append(encoded_dict['attention_mask'])
p6 = torch.tensor(lang_tag(tags_en2))
# 把lists 转为 tensors.
input_ids = torch.cat(input_ids, dim=0)
attention_masks = torch.cat(attention_masks, dim=0)
input_ids_1 = torch.cat(input_ids_1, dim=0)
attention_masks_1 = torch.cat(attention_masks_1, dim=0)
input_ids_2 = torch.cat(input_ids_2, dim=0)
attention_masks_2 = torch.cat(attention_masks_2, dim=0)
labels = torch.tensor(labels)

input_ids2 = torch.cat(input_ids2, dim=0)
attention_masks2 = torch.cat(attention_masks2, dim=0)
input_ids2_2 = torch.cat(input_ids2_2, dim=0)
attention_masks2_2 = torch.cat(attention_masks2_2, dim=0)
input_ids2_3 = torch.cat(input_ids2_3, dim=0)
attention_masks2_3 = torch.cat(attention_masks2_3, dim=0)
labels2 = torch.tensor(labels2)

from torch.utils.data import TensorDataset
# 把input 放入 TensorDataset。
dataset = TensorDataset(input_ids, attention_masks,p1, input_ids_1, attention_masks_1,p2,input_ids_2, attention_masks_2,p3, labels)
val_dataset = TensorDataset(input_ids2, attention_masks2,p4, input_ids2_2, attention_masks2_2,p5,input_ids2_3, attention_masks2_3,p6, labels2)

from torch.utils.data import DataLoader, RandomSampler

batch_size = 32
train_dataloader = DataLoader(
    dataset,  # 训练数据.
    sampler=RandomSampler(dataset),  # 打乱顺序
    batch_size=batch_size
)

validation_dataloader = DataLoader(
    val_dataset,  # 验证数据.
    # sampler = RandomSampler(val_dataset), # 打乱顺序
    batch_size=batch_size
)
from transformers import AdamW, AutoConfig
config = AutoConfig.from_pretrained('../../../root/autodl-tmp/xlm-roberta-large', trust_remote_code=True)
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
model = xlm_robertamodel(config=config)
model.to('cuda:0')

# AdamW 是一个 huggingface library 的类，'W' 是'Weight Decay fix"的意思。
optimizer = AdamW(model.parameters(),
                  lr=1e-5,  # args.learning_rate - 默认是 5e-5
                  eps=1e-8  # args.adam_epsilon  - 默认是 1e-8， 是为了防止衰减率分母除到0
                  )

from transformers import get_linear_schedule_with_warmup

# bert 推荐 epochs 在2到4之间为好。
epochs = 15

# training steps 的数量: [number of batches] x [number of epochs].
total_steps = len(train_dataloader) * epochs

# 设计 learning rate scheduler.
scheduler = get_linear_schedule_with_warmup(optimizer,
                                            num_warmup_steps=50,  # Default value in run_glue.py
                                            num_training_steps=total_steps)


def flat_accuracy(preds,labels):
    pred_flat = np.argmax(preds, axis=1).flatten()
    labels_flat = labels.flatten()
    return np.sum(pred_flat == labels_flat) / len(labels_flat)


import time
import datetime


def format_time(elapsed):
    elapsed_rounded = int(round((elapsed)))
    # 返回 hh:mm:ss 形式的时间
    return str(datetime.timedelta(seconds=elapsed_rounded))

if torch.cuda.is_available():
    device = torch.device("cuda")
    print('There are %d GPU(s) available.' % torch.cuda.device_count())
    print('We will use the GPU:', torch.cuda.get_device_name(0))
else:
    print('No GPU available, using the CPU instead.')
    device = torch.device("cpu")


output_dir = "./binary3"
output_model_file = os.path.join(output_dir, WEIGHTS_NAME)
output_config_file = os.path.join(output_dir, CONFIG_NAME)

# 设置随机种子.
'''seed_val = 62
random.seed(seed_val)
np.random.seed(seed_val)
torch.manual_seed(seed_val)
torch.cuda.manual_seed_all(seed_val)'''

# 记录training ,validation loss ,validation accuracy and timings.
training_stats = []

# 设置总时间.
total_t0 = time.time()
best_val_accuracy = 0

for epoch_i in range(0, epochs):
    print('Epoch {:} / {:}'.format(epoch_i + 1, epochs))

    # 记录每个 epoch 所用的时间
    t0 = time.time()
    total_train_loss = 0
    total_train_accuracy = 0
    model.train()
    tmp  = 10
    for step, batch in enumerate(train_dataloader):

        # 每隔40个batch 输出一下所用时间.
        if step % 50 == 0 and not step == 0:
            elapsed = format_time(time.time() - t0)
            print('  Batch {:>5,}  of  {:>5,}.    Elapsed: {:}.  loss:{:}'.format(step, len(train_dataloader), elapsed,loss))
        b_input_ids = batch[0].to(device)
        b_input_mask = batch[1].to(device)
        p1 = batch[2].to(device)
        b_input_ids_1 = batch[3].to(device)
        b_input_mask_1 = batch[4].to(device)
        p2 = batch[5].to(device)
        b_input_ids_2 = batch[6].to(device)
        b_input_mask_2 = batch[7].to(device)
        p3 = batch[8].to(device)
        b_labels = batch[9].to(device)

        # 清空梯度
        model.zero_grad()
        # forward
        outputs = model(input_ids = b_input_ids,attention_mask = b_input_mask,p1= p1,
                        b_input_ids_1  = b_input_ids_1, b_input_mask_1 = b_input_mask_1,p2 = p2,
                        b_input_ids_2 =  b_input_ids_2, b_input_mask_2 =  b_input_mask_2,p3 = p3,
                        b_labels = b_labels,tmp = tmp)
        loss, logits = outputs[:2]
        total_train_loss += loss.item()
        # backward 更新 gradients.
        loss.backward()
        # 减去大于1 的梯度，将其设为 1.0, 以防梯度爆炸.
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        # 更新模型参数
        optimizer.step()
        # 更新 learning rate.
        scheduler.step()

        logit = logits.detach().cpu().numpy()
        label_id = b_labels.to('cpu').numpy()
        # 计算training 句子的准确度.
        total_train_accuracy += flat_accuracy(logit, label_id)

        # 计算batches的平均损失.
    avg_train_loss = total_train_loss / len(train_dataloader)
    # 计算训练时间.
    training_time = format_time(time.time() - t0)

    # 训练集的准确率.
    avg_train_accuracy = total_train_accuracy / len(train_dataloader)
    #print("  训练准确率: {0:.2f}".format(avg_train_accuracy))
    print("  平均训练损失 loss: {0:.2f}".format(avg_train_loss))
    print("  训练时间: {:}".format(training_time))


    t0 = time.time()
    # 设置 model 为valuation 状态，在valuation状态 dropout layers 的dropout rate会不同
    model.eval()
    # 设置参数
    labels_pred1 = []
    total_eval_accuracy = 0
    total_eval_loss = 0

    for batch in validation_dataloader:
        b_input_ids = batch[0].to(device)
        b_input_mask = batch[1].to(device)
        p1 = batch[2].to(device)
        b_input_ids_1 = batch[3].to(device)
        b_input_mask_1 = batch[4].to(device)
        p2 = batch[5].to(device)
        b_input_ids_2 = batch[6].to(device)
        b_input_mask_2 = batch[7].to(device)
        p3 = batch[8].to(device)
        b_labels = batch[9].to(device)

        # 在valuation 状态，不更新权值，不改变计算图
        with torch.no_grad():
             outputs2 = model(input_ids = b_input_ids,attention_mask = b_input_mask,p1= p1, b_input_ids_1  = b_input_ids_1,
                              b_input_mask_1 = b_input_mask_1,p2 = p2,b_input_ids_2 =  b_input_ids_2,
                              b_input_mask_2 =  b_input_mask_2,p3 = p3, b_labels = b_labels,tmp = tmp)

        loss2, logits2 = outputs2[:2]
        # 计算 validation loss.
        total_eval_loss += loss2.item()
        logit = logits2.detach().cpu().numpy()

        label_id = b_labels.to('cpu').numpy()
        pred_flat = np.argmax(logit, axis=1).flatten()
        labels_pred1 = np.append(labels_pred1, pred_flat)
        # 计算 validation 句子的准确度.
        total_eval_accuracy += flat_accuracy(logit, label_id)

    # 计算 validation 的准确率.
    print(classification_report(labels2, labels_pred1, digits=4))
    avg_val_accuracy = total_eval_accuracy / len(validation_dataloader)
    print("")
    print("  测试准确率: {0:.2f}".format(avg_val_accuracy))

    if avg_val_accuracy > best_val_accuracy:
        best_val_accuracy = avg_val_accuracy
        torch.save(model.state_dict(), output_model_file)

    # 计算batches的平均损失.
    avg_val_loss = total_eval_loss / len(validation_dataloader)

    # 计算validation 时间.
    validation_time = format_time(time.time() - t0)

    print("  平均测试损失 Loss: {0:.2f}".format(avg_val_loss))
    print("  测试时间: {:}".format(validation_time))


print("训练一共用了 {:} (h:mm:ss)".format(format_time(time.time() - total_t0)))

