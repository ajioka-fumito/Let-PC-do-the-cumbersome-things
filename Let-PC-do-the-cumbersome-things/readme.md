# __Let pc do the cumbersome things__

### VOCdevkit.py  
VOCデータセットからセグメンテーションモデル用データセットを作成できます.  
シンプルなパターンマッチングを用いているつもりですがもっと効率的に作成できそう。。。

### crop.py  
segmegmentaion model用データセット作成時にクロップしてaugumentationしたくなるときがある.
そんなときに単位画像から最大枚クロップできるようにした.  
回転して最適化とかしてるわけじゃないけど暇なときにやりたい
