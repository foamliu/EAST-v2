from coco_text import COCO_Text
from tqdm import tqdm

coco = COCO_Text('data/train/COCO_Text.json')
train_ids = set()

for key in tqdm(coco.anns.keys()):
    train_ids.add(coco.anns[key]['image_id'])

print(len(train_ids))
print(train_ids)