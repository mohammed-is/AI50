# Traffic Sign Classifier

This is a CNN (convolutional neural network) model built to classify traffic signs, trained with TensorFlow framework.

## Dataset

Used the [German Traffic Sign Recognition Benchmark](http://benchmark.ini.rub.de/?section=gtsrb&subsection=news) (GTSRB) dataset, the [original dataset](https://cdn.cs50.net/ai/2023/x/projects/5/gtsrb.zip) contains thousands of images of 43 different kinds of road signs, but you can use the [modified dataset](https://github.com/m-ismail-x2/AI50/tree/main/5_neural_networks/gtsrb-small)

## Tweeks and Results

I tested some tweeks to optimize accuracy:
| Model Tweek | Result |
|------------ | ------ |
| 2 convs | faster training, simpler features; less complex patterns recognition |
| 3 convs | more detailed features; slower training |
| 0.5 dropout | Reduced overfitting and stabilized training |
| 256 dense units | Minimal improvement, slower training |

### Final Testing Output

```shell
Epoch 1/10
500/500 ━━━━━━━━━━━━━━━━━━━━ 46s 24ms/step - accuracy: 0.0699 - loss: 5.3452
Epoch 2/10
500/500 ━━━━━━━━━━━━━━━━━━━━ 20s 23ms/step - accuracy: 0.2468 - loss: 2.7108
Epoch 3/10
500/500 ━━━━━━━━━━━━━━━━━━━━ 21s 23ms/step - accuracy: 0.4105 - loss: 1.8993
Epoch 4/10
500/500 ━━━━━━━━━━━━━━━━━━━━ 20s 23ms/step - accuracy: 0.5447 - loss: 1.4302
Epoch 5/10
500/500 ━━━━━━━━━━━━━━━━━━━━ 11s 23ms/step - accuracy: 0.6484 - loss: 1.1037
Epoch 6/10
500/500 ━━━━━━━━━━━━━━━━━━━━ 11s 23ms/step - accuracy: 0.7327 - loss: 0.8413
Epoch 7/10
500/500 ━━━━━━━━━━━━━━━━━━━━ 11s 22ms/step - accuracy: 0.8130 - loss: 0.5902
Epoch 8/10
500/500 ━━━━━━━━━━━━━━━━━━━━ 11s 22ms/step - accuracy: 0.8460 - loss: 0.5045
Epoch 9/10
500/500 ━━━━━━━━━━━━━━━━━━━━ 20s 22ms/step - accuracy: 0.8806 - loss: 0.3881
Epoch 10/10
500/500 ━━━━━━━━━━━━━━━━━━━━ 11s 22ms/step - accuracy: 0.9002 - loss: 0.3283
333/333 - 2s - 7ms/step - accuracy: 0.9674 - loss: 0.1188
Model saved to model.keras.
```